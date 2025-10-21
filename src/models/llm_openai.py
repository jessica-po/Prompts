from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from src.models.token_limits import TokenLimits
from src.utils.logging import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logger.warning("openai package not installed. Install with: pip install openai")

RoleMessage = Dict[str, str]


@dataclass
class GenerationParams:
    max_new_tokens: int
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.05


# OpenAI model token limits
OPENAI_TOKEN_LIMITS = {
    "gpt-4o": TokenLimits(input_tokens=128000, output_tokens=16384),
    "gpt-4o-mini": TokenLimits(input_tokens=128000, output_tokens=16384),
    "gpt-4": TokenLimits(input_tokens=8192, output_tokens=8192),
}


class LLMOpenAI:
    """OpenAI API wrapper compatible with LLMBase interface."""

    def __init__(self, model_name: str) -> None:
        if not OPENAI_AVAILABLE:
            raise ImportError(
                "openai package is required for OpenAI models. "
                "Install it with: pip install openai"
            )

        self.model_name = model_name
        self.token_limits = self._get_token_limits(model_name)
        
        # Resolve API key
        self._api_key = self._resolve_api_key()
        if not self._api_key:
            raise RuntimeError(
                "OPENAI_API_KEY not set. Set it in your environment or .env file:\n"
                "  export OPENAI_API_KEY=sk-..."
            )
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=self._api_key)
        logger.info(f"Initialized OpenAI model: {model_name}")
        
        # Create a mock tokenizer object for compatibility
        self.tokenizer = MockTokenizer()

    @staticmethod
    def _get_token_limits(model_name: str) -> TokenLimits:
        """Get token limits for OpenAI models."""
        # Try exact match
        if model_name in OPENAI_TOKEN_LIMITS:
            return OPENAI_TOKEN_LIMITS[model_name]
        
        # Try prefix match for versioned models
        for key, limits in OPENAI_TOKEN_LIMITS.items():
            if model_name.startswith(key):
                return limits
        
        # Default fallback
        return TokenLimits(input_tokens=8192, output_tokens=4096)

    @staticmethod
    def _resolve_api_key() -> Optional[str]:
        """Resolve OpenAI API key from environment."""
        # Try various environment variable names
        for key in ("OPENAI_API_KEY", "OPENAI_KEY"):
            val = os.getenv(key)
            if val and val.strip():
                return val.strip()
        
        # Try loading from .env file
        try:
            dotenv_vars = LLMOpenAI._load_dotenv_vars()
            for key in ("OPENAI_API_KEY", "OPENAI_KEY"):
                val = dotenv_vars.get(key)
                if val and val.strip():
                    return val.strip()
        except Exception:
            pass
        
        return None

    @staticmethod
    def _load_dotenv_vars() -> Dict[str, str]:
        """Load variables from a `.env` file without external dependencies."""
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
                    val = val.strip().strip("\"'")
                    if key:
                        data[key] = val
            except Exception:
                return {}
            return data

        candidates = []
        try:
            # Project root (two levels up from this file)
            project_root = Path(__file__).resolve().parent.parent.parent
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
                    return parsed
        return {}

    def generate(self, messages: List[RoleMessage], params: Optional[GenerationParams] = None) -> str:
        """Generate completion using OpenAI API."""
        if params is None:
            params = GenerationParams(max_new_tokens=self.token_limits.output_tokens)

        try:
            # o1 and GPT-5 models have different parameters (no temperature, top_p, or frequency_penalty)
            is_o1_model = self.model_name.startswith("o1")
            is_gpt5_model = self.model_name.startswith("gpt-5")
            
            if is_o1_model or is_gpt5_model:
                # o1 and GPT-5 models use max_completion_tokens and no sampling params
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    max_completion_tokens=min(params.max_new_tokens, self.token_limits.output_tokens),
                )
            else:
                # Standard GPT models (GPT-4, GPT-3.5, etc.)
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    max_tokens=min(params.max_new_tokens, self.token_limits.output_tokens),
                    temperature=params.temperature,
                    top_p=params.top_p,
                    frequency_penalty=max(0.0, params.repetition_penalty - 1.0),  # Convert to OpenAI format
                )
            
            completion = response.choices[0].message.content
            if completion is None:
                return ""
            
            return completion.strip()
        except Exception as exc:
            logger.error(f"OpenAI generation failed: {exc}")
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
        """Generate and save to file (compatibility method)."""
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        content = self.generate(messages, params=params)
        
        if sanitize_markdown_fences:
            content = self._strip_markdown_fences(content)

        out_path = out_dir / output_file_name
        with open(out_path, "w", encoding="utf-8") as f:
            if header:
                f.write(header.rstrip() + "\n\n")
            f.write(content)

        logger.info(f"Wrote generation to {out_path}")
        return out_path

    @staticmethod
    def _strip_markdown_fences(text: str) -> str:
        """Remove markdown code fences from text."""
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


class MockTokenizer:
    """Mock tokenizer for compatibility with truncate_text_for_prompt."""
    
    def encode(self, text: str, add_special_tokens: bool = False) -> List[int]:
        """Rough approximation: 1 token ≈ 4 characters for English text."""
        return [0] * (len(text) // 4)
    
    def decode(self, token_ids: List[int], skip_special_tokens: bool = False) -> str:
        """Mock decode - just return truncated based on token count."""
        # This is a simplification; in practice you'd need proper tokenization
        char_count = len(token_ids) * 4
        return "..." if char_count > 0 else ""


__all__ = [
    "LLMOpenAI",
    "GenerationParams",
    "OPENAI_TOKEN_LIMITS",
]
