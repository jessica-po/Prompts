from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
try:
    from huggingface_hub import snapshot_download
except Exception:  # pragma: no cover - optional dependency surface
    snapshot_download = None  # type: ignore
try:
    # Optional helpers for authenticating to the Hub
    from huggingface_hub import HfFolder, login as hf_login
except Exception:  # pragma: no cover - optional dependency surface
    HfFolder = None  # type: ignore
    hf_login = None  # type: ignore
try:
    # Optional API for verifying auth state
    from huggingface_hub import HfApi
except Exception:  # pragma: no cover - optional dependency surface
    HfApi = None  # type: ignore

from src.models.token_limits import get_token_limits
from src.utils.logging import get_logger, setup_logging


setup_logging()
logger = get_logger(__name__)


RoleMessage = Dict[str, str]


@dataclass
class GenerationParams:
    max_new_tokens: int
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.05


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _has_chat_template(tokenizer: AutoTokenizer) -> bool:
    try:
        return hasattr(tokenizer, "chat_template") and tokenizer.chat_template is not None
    except Exception:
        return False


def _build_fallback_prompt(messages: List[RoleMessage]) -> str:
    lines: List[str] = []
    for msg in messages:
        role = msg.get("role", "user").strip().lower()
        content = msg.get("content", "")
        if role == "system":
            lines.append(f"System: {content}")
        elif role == "user":
            lines.append(f"User: {content}")
        else:
            lines.append(f"{role.capitalize()}: {content}")
    lines.append("Assistant:")
    return "\n\n".join(lines)


def _strip_markdown_fences(text: str) -> str:
    lines = text.split("\n")
    cleaned: List[str] = []
    in_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_block = not in_block
            continue
        if not in_block:
            cleaned.append(line)
        else:
            cleaned.append(line)
    return "\n".join(cleaned).strip()


class LLMBase:
    """Lightweight local LLM wrapper on top of transformers.

    - Loads model/tokenizer by name
    - Supports HF chat templates when available
    - Provides text generation and save-to-file helpers
    """

    def __init__(self, model_name: str, torch_dtype: str | torch.dtype = "auto", device_map: str | Dict = "auto") -> None:
        self.model_name = model_name
        self.token_limits = get_token_limits(model_name)
        cache_dir = self._resolve_cache_dir()
        # Load .env and resolve/apply HF token from .env (preferred over shell env)
        self._dotenv_vars = self._load_dotenv_vars()
        # Resolve and apply HF token
        self._hf_token = self._resolve_hf_token_from_env(self._dotenv_vars)
        self._apply_hf_token(self._hf_token)
        self._log_hf_token_debug(self._hf_token)
        self._ensure_hf_auth_or_raise()
        self._maybe_prefetch_model(cache_dir)
        try:
            hub_kwargs = {"cache_dir": str(cache_dir)}
            auth_used = None
            if self._hf_token:
                hub_kwargs["token"] = self._hf_token
                auth_used = "token"

            try:
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    torch_dtype=torch_dtype,
                    device_map=device_map,
                    **hub_kwargs,
                )
            except TypeError as e:
                # Older transformers/hf-hub versions may not support 'token'
                if self._hf_token and "token" in str(e) and "unexpected" in str(e).lower():
                    hub_kwargs.pop("token", None)
                    hub_kwargs["use_auth_token"] = self._hf_token
                    auth_used = "use_auth_token"
                    logger.info("Retrying model load with use_auth_token (older HF versions detected).")
                    self.model = AutoModelForCausalLM.from_pretrained(
                        model_name,
                        torch_dtype=torch_dtype,
                        device_map=device_map,
                        **hub_kwargs,
                    )
                else:
                    raise

            try:
                self.tokenizer = AutoTokenizer.from_pretrained(model_name, **hub_kwargs)
            except TypeError as e:
                if self._hf_token and "token" in str(e) and "unexpected" in str(e).lower():
                    # Align tokenizer call too
                    hub_kwargs.pop("token", None)
                    hub_kwargs["use_auth_token"] = self._hf_token
                    auth_used = "use_auth_token"
                    logger.info("Retrying tokenizer load with use_auth_token (older HF versions detected).")
                    self.tokenizer = AutoTokenizer.from_pretrained(model_name, **hub_kwargs)
                else:
                    raise

            if self._hf_token and auth_used:
                logger.info(f"HF auth kwarg used for loading: {auth_used}")
            # Ensure a pad token is set; some models (e.g., GPT-2) lack one by default
            if getattr(self.tokenizer, "pad_token_id", None) is None:
                try:
                    self.tokenizer.pad_token = self.tokenizer.eos_token  # type: ignore[attr-defined]
                except Exception:
                    pass
            self.use_chat_template = _has_chat_template(self.tokenizer)
            logger.info(f"Loaded model: {model_name} (chat_template={self.use_chat_template})")
        except Exception as exc:
            logger.error(f"Failed to load model {model_name}: {exc}")
            raise
        # Choose a unified input device for tensors independent of device_map
        self._device = "cuda" if torch.cuda.is_available() else "cpu"

    @staticmethod
    def _resolve_cache_dir() -> Path:
        """Resolve and prepare a cache directory for HF models.

        Precedence:
        1) TRANSFORMERS_CACHE
        2) HF_HOME
        3) MODEL_CACHE_DIR (project-specific opt-in)
        4) Project-local ".hf_cache" folder
        """
        env_cache = os.getenv("TRANSFORMERS_CACHE") or os.getenv("HF_HOME") or os.getenv("MODEL_CACHE_DIR")
        if env_cache:
            path = Path(env_cache)
            path.mkdir(parents=True, exist_ok=True)
            # Ensure both envs point to the same location for consistency
            os.environ.setdefault("TRANSFORMERS_CACHE", str(path))
            os.environ.setdefault("HF_HOME", str(path))
            return path

        default_dir = Path(__file__).resolve().parent.parent / ".hf_cache"
        default_dir.mkdir(parents=True, exist_ok=True)
        os.environ.setdefault("TRANSFORMERS_CACHE", str(default_dir))
        os.environ.setdefault("HF_HOME", str(default_dir))
        return default_dir

    def _maybe_prefetch_model(self, cache_dir: Path) -> None:
        """Best-effort prefetch to populate cache and avoid redownloads.

        Uses huggingface_hub.snapshot_download when available. Falls back silently
        if the library is not present or when offline without local files.
        """
        if snapshot_download is None:
            logger.debug("huggingface_hub not available; skipping prefetch")
            return

        offline = os.getenv("HF_OFFLINE", "0") == "1" or os.getenv("TRANSFORMERS_OFFLINE", "0") == "1"
        if offline:
            logger.info("HF offline mode enabled; prefetch will use local files only.")
        try:
            kwargs = {
                "repo_id": self.model_name,
                "cache_dir": str(cache_dir),
                "local_files_only": offline,
                "resume_download": True,
            }
            auth_used = None
            if self._hf_token:
                kwargs["token"] = self._hf_token
                auth_used = "token"
            try:
                snapshot_download(**kwargs)
            except TypeError as e:
                if self._hf_token and "token" in str(e) and "unexpected" in str(e).lower():
                    kwargs.pop("token", None)
                    kwargs["use_auth_token"] = self._hf_token
                    auth_used = "use_auth_token"
                    logger.info("Retrying snapshot_download with use_auth_token (older HF versions detected).")
                    snapshot_download(**kwargs)
                else:
                    raise
            if self._hf_token and auth_used:
                logger.info(f"HF auth kwarg used for prefetch: {auth_used}")
            logger.info(f"Model available in cache: {self.model_name} (dir={cache_dir})")
        except Exception as exc:
            logger.warning(f"Prefetch skipped/failed for {self.model_name}: {exc}")

    @staticmethod
    def _resolve_hf_token_from_env(dotenv_vars: Optional[Dict[str, str]] = None) -> Optional[str]:
        """Resolve a Hugging Face token preferring `.env` over shell environment.

        Resolution order:
        1) Variables from `.env`: HF_TOKEN, HUGGINGFACE_HUB_TOKEN, HUGGINGFACE_TOKEN, HUGGINGFACE_API_TOKEN
        2) Token file referenced by `.env`: HF_TOKEN_FILE (first line)
        3) Shell env (fallback only): HF_TOKEN, HUGGINGFACE_HUB_TOKEN, HUGGINGFACE_TOKEN, HUGGINGFACE_API_TOKEN
        4) Cached login via HfFolder.get_token()
        """
        envmap = dotenv_vars or {}
        # 1) .env variables
        for key in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HUGGINGFACE_TOKEN", "HUGGINGFACE_API_TOKEN"):
            val = envmap.get(key)
            if val and val.strip():
                return val.strip()

        # 2) .env token file path
        token_file_from_env = envmap.get("HF_TOKEN_FILE")
        if token_file_from_env:
            try:
                path = Path(token_file_from_env)
                if path.is_file():
                    content = path.read_text(encoding="utf-8").strip()
                    if content:
                        return content.splitlines()[0].strip()
            except Exception:
                pass

        # 3) Shell environment (fallback)
        for key in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HUGGINGFACE_TOKEN", "HUGGINGFACE_API_TOKEN"):
            val = os.getenv(key)
            if val and val.strip():
                return val.strip()

        # 4) Cached login
        try:
            if HfFolder is not None:
                cached = HfFolder.get_token()  # type: ignore[attr-defined]
                if cached and cached.strip():
                    return cached.strip()
        except Exception:
            pass

        return None

    @staticmethod
    def _load_dotenv_vars() -> Dict[str, str]:
        """Load variables from a `.env` file without external dependencies.

        Search order for the `.env` file:
        - Project root (two levels up from this file)
        - Current working directory
        """
        def parse_env_file(path: Path) -> Dict[str, str]:
            data: Dict[str, str] = {}
            try:
                for raw in path.read_text(encoding="utf-8").splitlines():
                    line = raw.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("export "):
                        line = line[len("export "):].strip()
                    if "=" not in line:
                        continue
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("\"\'")
                    if key:
                        data[key] = val
            except Exception:
                return {}
            return data

        candidates = []
        try:
            project_root = Path(__file__).resolve().parent.parent
            candidates.append(project_root / ".env")
        except Exception:
            pass
        try:
            cwd_env = Path.cwd() / ".env"
            if cwd_env not in candidates:
                candidates.append(cwd_env)
        except Exception:
            pass

        for p in candidates:
            if p.is_file():
                parsed = parse_env_file(p)
                if parsed:
                    logger.info(f"Loaded .env from {p}")
                    return parsed
        return {}

    @staticmethod
    def _apply_hf_token(token: Optional[str]) -> None:
        """Apply token to environment and persist if possible.

        This makes both huggingface_hub and transformers pick up the token
        automatically in most versions.
        """
        if not token:
            return
        try:
            os.environ.setdefault("HF_TOKEN", token)
            os.environ.setdefault("HUGGINGFACE_HUB_TOKEN", token)
        except Exception:
            pass
        # Try to persist the token so future runs are authenticated
        try:
            if hf_login is not None:
                # Avoid touching git credentials; only cache for hf-hub
                hf_login(token=token, add_to_git_credential=False)  # type: ignore[call-arg]
            elif HfFolder is not None:
                HfFolder.save_token(token)  # type: ignore[attr-defined]
        except Exception:
            # Non-fatal if login helpers are unavailable or signatures differ
            pass

    @staticmethod
    def _mask_token(token: str) -> str:
        """Return a masked representation of a token suitable for logs."""
        try:
            t = token.strip()
            if len(t) <= 10:
                return "*" * max(4, len(t))
            return f"{t[:6]}{'*' * (len(t) - 10)}{t[-4:]}"
        except Exception:
            return "****"

    @staticmethod
    def _get_env_token_source(expected_token: Optional[str], dotenv_vars: Optional[Dict[str, str]] = None) -> Optional[str]:
        """Figure out where the token came from: `.env` or shell env (best-effort)."""
        if not expected_token:
            return None
        # Check .env first
        if dotenv_vars:
            for name in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HUGGINGFACE_TOKEN", "HUGGINGFACE_API_TOKEN"):
                val = dotenv_vars.get(name)
                if val and val.strip() == expected_token:
                    return f".env:{name}"
            token_file = dotenv_vars.get("HF_TOKEN_FILE")
            if token_file:
                try:
                    path = Path(token_file)
                    if path.is_file():
                        content = path.read_text(encoding="utf-8").strip().splitlines()[0].strip()
                        if content == expected_token:
                            return ".env:HF_TOKEN_FILE"
                except Exception:
                    pass
        # Shell env fallback
        mapping = [
            ("HF_TOKEN", os.getenv("HF_TOKEN")),
            ("HUGGINGFACE_HUB_TOKEN", os.getenv("HUGGINGFACE_HUB_TOKEN")),
            ("HUGGINGFACE_TOKEN", os.getenv("HUGGINGFACE_TOKEN")),
            ("HUGGINGFACE_API_TOKEN", os.getenv("HUGGINGFACE_API_TOKEN")),
        ]
        for name, val in mapping:
            if val and val.strip() == expected_token:
                return name
        return None

    def _log_hf_token_debug(self, token: Optional[str]) -> None:
        """Log a masked token and source so users can confirm it's picked up."""
        if not token:
            logger.info("HF token not found in environment.")
            return
        source = self._get_env_token_source(token, self._dotenv_vars) or "(unknown env var)"
        unmasked_flag = os.getenv("HF_PRINT_TOKEN_UNMASKED", "0").strip().lower() in {"1", "true", "yes", "on"}
        token_for_log = token if unmasked_flag else self._mask_token(token)
        logger.info(f"HF token detected from {source}: {token_for_log}")
        if unmasked_flag:
            logger.warning("HF token printed UNMASKED due to HF_PRINT_TOKEN_UNMASKED=1. Handle logs carefully.")

    def _verify_hf_auth(self, token: Optional[str]) -> None:
        """Call Hugging Face Hub to confirm authentication using the provided token."""
        if not token:
            return
        try:
            if HfApi is None:
                logger.info("huggingface_hub.HfApi unavailable; skipping whoami verification.")
                return
            api = HfApi()
            info = api.whoami(token=token)  # type: ignore[call-arg]
            # info typically includes: {"name": <username>, "email": ..., "orgs": [...]}
            username = info.get("name") or info.get("username") or "(unknown)"
            orgs = info.get("orgs")
            org_count = len(orgs) if isinstance(orgs, list) else 0
            logger.info(f"HF auth verified. User: {username}, Orgs: {org_count}")
        except Exception as exc:
            logger.warning(f"HF auth verification failed: {exc}")

    def _ensure_hf_auth_or_raise(self) -> None:
        """Ensure we are authenticated before any download; raise with guidance if not.

        Requires a valid token in HF_TOKEN (or resolved via other supported means).
        """
        token = self._hf_token
        if not token:
            raise RuntimeError(
                "HF_TOKEN not set or empty. Set $env:HF_TOKEN in PowerShell before running."
            )
        try:
            if HfApi is None:
                logger.info("huggingface_hub.HfApi unavailable; cannot verify auth strictly, continuing.")
                return
            api = HfApi()
            info = api.whoami(token=token)  # type: ignore[call-arg]
            username = info.get("name") or info.get("username") or "(unknown)"
            logger.info(f"HF authentication OK. User: {username}")
        except Exception as exc:
            masked = self._mask_token(token)
            raise RuntimeError(
                f"HF authentication failed with the provided token {masked}: {exc}. "
                f"Ensure the token is valid and has access to {self.model_name}."
            )

    def _build_text(self, messages: List[RoleMessage]) -> str:
        if self.use_chat_template:
            # If using a Qwen model, explicitly disable "thinking" in chat template when supported
            if "qwen" in self.model_name.lower():
                try:
                    return self.tokenizer.apply_chat_template(
                        messages,
                        tokenize=False,
                        add_generation_prompt=True,
                        enable_thinking=False,
                    )
                except TypeError:
                    # Fallback for tokenizers that don't support enable_thinking
                    return self.tokenizer.apply_chat_template(
                        messages,
                        tokenize=False,
                        add_generation_prompt=True,
                    )
            return self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
        return _build_fallback_prompt(messages)

    def generate(self, messages: List[RoleMessage], params: Optional[GenerationParams] = None) -> str:
        if params is None:
            params = GenerationParams(max_new_tokens=self.token_limits.output_tokens)

        text = self._build_text(messages)
        # Tokenize without automatic truncation; we'll enforce hard limits below
        tokenized = self.tokenizer([text], return_tensors="pt", add_special_tokens=False)
        input_ids = tokenized["input_ids"]
        attention_mask = tokenized.get("attention_mask")

        # Compute effective context window based on model config and our token limits
        model_ctx = getattr(self.model.config, "max_position_embeddings", None)
        if model_ctx is None or not isinstance(model_ctx, int) or model_ctx <= 0 or model_ctx > 1000000:
            # Fallback to tokenizer advertised length if reasonable
            tokenizer_ctx = getattr(self.tokenizer, "model_max_length", 0)
            if isinstance(tokenizer_ctx, int) and 0 < tokenizer_ctx <= 1000000:
                model_ctx = tokenizer_ctx
            else:
                model_ctx = self.token_limits.input_tokens

        effective_ctx = min(self.token_limits.input_tokens, model_ctx)
        # Keep a safety buffer and reserve space for generation tokens
        gen_budget = min(params.max_new_tokens, self.token_limits.output_tokens)
        safety = 16
        allowed_len = max(1, effective_ctx - gen_budget - safety)

        if input_ids.shape[1] > allowed_len:
            input_ids = input_ids[:, -allowed_len:]
            if attention_mask is not None:
                attention_mask = attention_mask[:, -allowed_len:]

        if attention_mask is None:
            attention_mask = torch.ones_like(input_ids)

        input_ids = input_ids.to(self._device)
        attention_mask = attention_mask.to(self._device)

        try:
            outputs = self.model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_new_tokens=min(params.max_new_tokens, self.token_limits.output_tokens),
                temperature=params.temperature,
                top_p=params.top_p,
                repetition_penalty=params.repetition_penalty,
                do_sample=True,
                pad_token_id=getattr(self.tokenizer, "pad_token_id", None) or self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

            # Remove the prompt portion
            prompt_len = input_ids.shape[1]
            generated_ids = outputs[0][prompt_len:]
            completion = self.tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

            return completion
        except Exception as exc:
            logger.error(f"Generation failed: {exc}")
            raise

    def generate_to_file(
        self,
        messages: List[RoleMessage],
        output_dir: Path | str,
        output_file_name: str,
        params: Optional[GenerationParams] = None,
        header: Optional[str] = None,
        sanitize_markdown_fences: bool = False,
    ) -> Path:
        out_dir = Path(output_dir)
        _ensure_dir(out_dir)

        content = self.generate(messages, params=params)
        if sanitize_markdown_fences:
            content = _strip_markdown_fences(content)

        out_path = out_dir / output_file_name
        with open(out_path, "w", encoding="utf-8") as f:
            if header:
                f.write(header.rstrip() + "\n\n")
            f.write(content)

        logger.info(f"Wrote generation to {out_path}")
        return out_path


__all__ = [
    "LLMBase",
    "GenerationParams",
]


