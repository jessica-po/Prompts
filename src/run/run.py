from __future__ import annotations

import logging
import os
from pathlib import Path
from datetime import datetime
import time
from typing import Dict, Any, List

import pandas as pd

from src.models.llm_base import LLMBase, GenerationParams
from src.utils.utils import load_prompt_template, sanitize_for_path, truncate_text_for_prompt, load_dotenv_vars
from src.methods import get_method
from src.utils.logging import get_logger, setup_logging, add_file_logging
from src.utils.gpu import log_gpu_overview, PeriodicGpuMonitor

# Import OpenAI wrapper
try:
    from src.models.llm_openai import LLMOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


setup_logging()
logger = get_logger(__name__)


DEFAULT_MODEL = os.getenv("LOCAL_LLM_MODEL", "google/gemma-3-27b-it")


class SafeDict(dict):
    def __missing__(self, key: str) -> str:  # type: ignore[override]
        return ""


def _resolve_prompt_files(method: str) -> tuple[Path, Path]:
    root = Path(__file__).resolve().parent.parent
    system = root  / "prompts" / method / "system.txt"
    user = root  / "prompts" / method / "user.txt"
    if not system.exists():
        raise FileNotFoundError(f"System prompt not found for method '{method}': {system}")
    if not user.exists():
        raise FileNotFoundError(f"User prompt not found for method '{method}': {user}")
    return system, user


def _detect_preferred_placeholder(user_template: str) -> str:
    # Prefer common names if present in template; fallback to 'description'
    candidates = ["vulnerable_code", "description", "question", "code", "input", "text"]
    for key in candidates:
        token = "{" + key + "}"
        if token in user_template:
            return key
    return "description"


def _build_mapping_for_row(row: pd.Series) -> Dict[str, str]:
    # Normalize to strings and provide multiple synonymous keys so templates are flexible
    get = lambda k: str(row.get(k, "")) if k in row and pd.notna(row[k]) else ""
    vulnerability = get("vulnerability") or get("vulnerability_type")
    question = get("question")
    rejected = get("rejected") or get("vulnerable_code")
    chosen = get("chosen") or get("fixed_code")
    lang = get("lang") or get("language")
    vulnerable_code = get("vulnerable_code") or get("rejected")
    patched_code = get("patched_code") or get("fixed_code") or get("chosen")
    cwe_ids = get("cwe_ids")

    # A general description if question is not present
    description_parts: List[str] = []
    if vulnerability:
        description_parts.append(f"Vulnerability: {vulnerability}")
    if question:
        description_parts.append(question)
    elif vulnerable_code:
        description_parts.append("Provide a secure fix for the following code while preserving behavior.")
    if vulnerable_code:
        description_parts.append("\nVulnerable Code:\n" + vulnerable_code)
    description = "\n\n".join([p for p in description_parts if p])

    return {
        "vulnerability": vulnerability,
        "question": question,
        "code": vulnerable_code or chosen,
        "rejected": rejected,
        "cwe_ids": cwe_ids or "",
        "chosen": chosen,
        "vulnerable_code": vulnerable_code,
        "patched_code": patched_code,
        "lang": lang,
        "description": description or question or vulnerable_code or "",
        "input": description or question or vulnerable_code or "",
        "text": description or question or vulnerable_code or "",
    }


def _render_user_prompt(user_template: str, mapping: Dict[str, str]) -> str:
    return user_template.format_map(SafeDict(mapping))


def _resolve_output_path(dataset_path: Path, output_env: str | None, model_name: str, method: str) -> Path:
    if output_env:
        out_path = Path(output_env)
        if out_path.is_dir() or (not out_path.suffix):
            # Directory or missing suffix -> create file inside dir
            out_dir = out_path if out_path.is_dir() else out_path
            out_dir.mkdir(parents=True, exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            model_token = sanitize_for_path(model_name)
            filename = f"{dataset_path.stem}-{method}-{model_token}-{ts}.csv"
            return out_dir / filename
        # Specific file path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Ensure .csv suffix
        if out_path.suffix.lower() != ".csv":
            out_path = out_path.with_suffix(".csv")
        return out_path

    # Default location under dataset directory
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    model_token = sanitize_for_path(model_name)
    return dataset_path.parent / f"{dataset_path.stem}-{method}-{model_token}-{ts}.csv"


def _resolve_output_root(dataset_path: Path, output_env: str | None, model_name: str, method: str) -> Path:
    """Resolve a root directory under which per-instance folders will be created.

    If output_env is a directory or has no suffix, it is used directly.
    If output_env is a file path (e.g., .csv), a sibling directory with the same stem is used.
    If output_env is not provided, a directory is created next to the dataset with an auto-generated name.
    """
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    model_token = sanitize_for_path(model_name)

    if output_env:
        path = Path(output_env)
        # Treat as directory if it exists as dir or has no suffix
        if path.is_dir() or (not path.suffix):
            path.mkdir(parents=True, exist_ok=True)
            return path
        # If it's a file-like path (e.g., .csv), use a directory with the same stem
        dir_like = path.with_suffix("")
        dir_like.mkdir(parents=True, exist_ok=True)
        return dir_like

    # Default: create a directory under the dataset directory
    root = dataset_path.parent / f"{dataset_path.stem}-{method}-{model_token}-{ts}"
    root.mkdir(parents=True, exist_ok=True)
    return root


def _extract_row_id(row: pd.Series, fallback_index: int) -> str:
    """Best-effort extraction of a stable ID from a row.

    Prefers common ID column names; falls back to a zero-padded index-based id.
    """
    candidates = ["id", "ID", "Id", "uid", "unique_id"]
    for key in candidates:
        if key in row and pd.notna(row[key]) and str(row[key]).strip():
            return str(row[key]).strip()
    return f"row-{fallback_index:06d}"


def _format_duration(seconds: float) -> str:
    seconds = max(0.0, float(seconds))
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h {m}m {s}s"
    if m > 0:
        return f"{m}m {s}s"
    return f"{s}s"


def _is_openai_model(model_name: str) -> bool:
    """Check if the model name is an OpenAI model."""
    openai_prefixes = ["gpt-", "chatgpt", "text-davinci", "text-curie", "text-babbage", "text-ada", "o1-"]
    model_lower = model_name.lower()
    
    # Exact match for o1
    if model_lower == "o1":
        return True
    
    return any(model_lower.startswith(prefix) for prefix in openai_prefixes)


def _create_model(model_name: str):
    """Factory function to create the appropriate model instance."""
    if _is_openai_model(model_name):
        if not OPENAI_AVAILABLE:
            raise ImportError(
                f"Model '{model_name}' appears to be an OpenAI model, but the OpenAI wrapper is not available. "
                "Install openai with: pip install openai"
            )
        logger.info(f"Using OpenAI model: {model_name}")
        return LLMOpenAI(model_name)
    else:
        logger.info(f"Using HuggingFace model: {model_name}")
        return LLMBase(model_name)


def run_pipeline() -> None:
    # Apply GPU selection from pipeline env vars or .env, if provided
    try:
        dotenv_vars = load_dotenv_vars()
        pipeline_visible = os.getenv("PIPELINE_VISIBLE_DEVICES") or dotenv_vars.get("PIPELINE_VISIBLE_DEVICES")
        pipeline_gpu_id = os.getenv("PIPELINE_GPU_ID") or dotenv_vars.get("PIPELINE_GPU_ID")
        if pipeline_visible:
            os.environ["CUDA_VISIBLE_DEVICES"] = pipeline_visible
            logger.info(f"Applied CUDA_VISIBLE_DEVICES from PIPELINE_VISIBLE_DEVICES={pipeline_visible}")
        elif pipeline_gpu_id:
            os.environ["CUDA_VISIBLE_DEVICES"] = pipeline_gpu_id
            logger.info(f"Applied CUDA_VISIBLE_DEVICES from PIPELINE_GPU_ID={pipeline_gpu_id}")
    except Exception:
        pass

    dataset_path_str = os.getenv("PIPELINE_DATASET_PATH")
    if not dataset_path_str:
        raise RuntimeError("PIPELINE_DATASET_PATH not set. Provide --dataset to src/main.py.")
    dataset_path = Path(dataset_path_str)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

    method = os.getenv("PROMPT_METHOD", "1_single_shot").strip()
    system_path, user_path = _resolve_prompt_files(method)
    system_template = load_prompt_template(system_path)
    user_template = load_prompt_template(user_path)
    preferred_placeholder = _detect_preferred_placeholder(user_template)

    model_name = os.getenv("LOCAL_LLM_MODEL", DEFAULT_MODEL)
    model = _create_model(model_name)  # Use factory function

    output_root = _resolve_output_root(dataset_path, os.getenv("PIPELINE_OUTPUT_PATH"), model_name, method)

    # Optional file logging
    log_file_env = os.getenv("PIPELINE_LOG_FILE")
    log_dir_env = os.getenv("PIPELINE_LOG_DIR")
    if log_file_env:
        add_file_logging(log_file_env)
    else:
        # Build log file name as <YYYY-MM-DD>_<method>
        method_token = sanitize_for_path(method)
        date_token = datetime.now().strftime("%Y-%m-%d")
        log_basename = f"{date_token}_{method_token}"

        # Default: write to repo_root/logs/<run_name>/<YYYY-MM-DD>_<method>
        try:
            if log_dir_env:
                add_file_logging(Path(log_dir_env) / log_basename)
            else:
                repo_root = Path(__file__).resolve().parents[2]
                run_logs_dir = repo_root / "logs" / output_root.name
                add_file_logging(run_logs_dir / log_basename)
        except Exception:
            # Fall back silently if path invalid; console logging still works
            pass

    logger.info(f"Dataset: {dataset_path}")
    logger.info(f"Method: {method}")
    logger.info(f"Model: {model_name}")
    logger.info(
        f"Token limits - input: {model.token_limits.input_tokens}, output: {model.token_limits.output_tokens}"
    )
    logger.info(f"Output: {output_root}")

    # Job and environment context
    slurm_job_id = os.getenv("SLURM_JOB_ID")
    cuda_visible = os.getenv("CUDA_VISIBLE_DEVICES")
    if slurm_job_id:
        logger.info(f"SLURM_JOB_ID: {slurm_job_id}")
    if cuda_visible:
        logger.info(f"CUDA_VISIBLE_DEVICES: {cuda_visible}")

    # GPU overview and optional periodic monitoring
    try:
        log_gpu_overview(logger)
    except Exception:
        pass

    gpu_monitor_enabled = os.getenv("GPU_MONITOR", "1") not in ("0", "false", "False")
    gpu_monitor_interval = float(os.getenv("GPU_MONITOR_INTERVAL_SEC", "30"))
    gpu_monitor = PeriodicGpuMonitor(interval_sec=gpu_monitor_interval, logger=logger, enabled=gpu_monitor_enabled)
    try:
        gpu_monitor.start()
    except Exception:
        pass

    # Determine generation budget ratio
    try:
        gen_ratio_env = os.getenv("PIPELINE_GEN_RATIO")
        gen_ratio = float(gen_ratio_env) if gen_ratio_env is not None else None
        if gen_ratio is not None:
            if not (0.0 < gen_ratio < 1.0):
                logger.warning(f"PIPELINE_GEN_RATIO out of range: {gen_ratio}. Ignoring.")
                gen_ratio = None
    except Exception:
        gen_ratio = None

    df = pd.read_csv(dataset_path, dtype=str, keep_default_na=False)
    total_rows = len(df)
    start_time = time.time()

    # Initialize selected method runner
    method_runner = get_method(method)
    method_runner.setup({
        "dataset_path": str(dataset_path),
        "output_root": str(output_root),
        "model_name": model_name,
        "method": method,
    })

    for idx, row in df.iterrows():
        try:
            mapping = _build_mapping_for_row(row)

            # Truncate the primary injection field to respect context budget
            injection_key = preferred_placeholder if mapping.get(preferred_placeholder) else (
                "question" if mapping.get("question") else ("code" if mapping.get("code") else "description")
            )
            # Compute generation max tokens based on ratio if provided
            if gen_ratio is not None:
                gen_max_new_tokens = max(1, int(model.token_limits.output_tokens * gen_ratio))
            else:
                gen_max_new_tokens = model.token_limits.output_tokens

            truncated = truncate_text_for_prompt(
                tokenizer=model.tokenizer,
                max_input_tokens=model.token_limits.input_tokens,
                system_prompt=system_template,
                user_prompt_template=user_template,
                placeholder_key=injection_key,
                text=mapping.get(injection_key, ""),
            )
            mapping[injection_key] = truncated

            # Provide generation budget to method runner
            result = method_runner.run_sample(mapping=mapping, model=model, system_template=system_template, user_template=user_template, **{"gen_max_new_tokens": gen_max_new_tokens})
            messages = result.get("messages", [])
            completion = result.get("completion", "")
            # Best-effort to recover user prompt for logging
            if messages and isinstance(messages, list):
                try:
                    user_prompt = next((m.get("content", "") for m in messages if m.get("role") == "user"), "")
                except Exception:
                    user_prompt = ""
            else:
                user_prompt = _render_user_prompt(user_template, mapping)

            # Resolve per-instance directory using ID
            row_id = _extract_row_id(row, idx)
            instance_dir = output_root / sanitize_for_path(row_id)
            instance_dir.mkdir(parents=True, exist_ok=True)

            # Write vulnerable_code.txt (raw code from dataset if present)
            raw_vulnerable_code = str(row.get("vulnerable_code", "") if "vulnerable_code" in row else row.get("rejected", ""))
            with (instance_dir / "vulnerable_code.txt").open("w", encoding="utf-8") as f:
                f.write(raw_vulnerable_code or "")

            # Compose input.txt from the actual messages sequence used
            try:
                if messages and isinstance(messages, list):
                    parts = []
                    for m in messages:
                        role = str(m.get("role", "")).upper() or "USER"
                        content = m.get("content", "")
                        parts.append(f"[{role}]\n{content}")
                    input_content = "\n\n".join(parts)
                else:
                    input_content = f"[SYSTEM]\n{system_template}\n\n[USER]\n{user_prompt}"
            except Exception:
                input_content = f"[SYSTEM]\n{system_template}\n\n[USER]\n{user_prompt}"
            with (instance_dir / "input.txt").open("w", encoding="utf-8") as f:
                f.write(input_content)

            # Write output.txt with model completion
            with (instance_dir / "output.txt").open("w", encoding="utf-8") as f:
                f.write(completion)

            # If method returned per-stage results, write inputN/outputN files
            try:
                stages = result.get("stages")
                if isinstance(stages, list):
                    for i, stage in enumerate(stages, start=1):
                        s_messages = stage.get("messages", [])
                        s_completion = stage.get("completion", "")
                        # Build stage input content
                        try:
                            if s_messages and isinstance(s_messages, list):
                                s_parts = []
                                for m in s_messages:
                                    s_role = str(m.get("role", "")).upper() or "USER"
                                    s_content = m.get("content", "")
                                    s_parts.append(f"[{s_role}]\n{s_content}")
                                s_input_content = "\n\n".join(s_parts)
                            else:
                                s_input_content = input_content
                        except Exception:
                            s_input_content = input_content

                        with (instance_dir / f"input{i}.txt").open("w", encoding="utf-8") as f_in:
                            f_in.write(s_input_content)
                        with (instance_dir / f"output{i}.txt").open("w", encoding="utf-8") as f_out:
                            f_out.write(s_completion)
            except Exception:
                pass
        except Exception as exc:
            logger.error(f"Row {idx} failed: {exc}")
            # Resolve per-instance directory using ID and write files with error context
            row_id = _extract_row_id(row, idx)
            instance_dir = output_root / sanitize_for_path(row_id)
            instance_dir.mkdir(parents=True, exist_ok=True)

            raw_vulnerable_code = str(row.get("vulnerable_code", "") if "vulnerable_code" in row else row.get("rejected", ""))
            with (instance_dir / "vulnerable_code.txt").open("w", encoding="utf-8") as f:
                f.write(raw_vulnerable_code or "")

            input_content = f"[SYSTEM]\n{system_template}\n\n[USER]\n{user_prompt if 'user_prompt' in locals() else ''}"
            with (instance_dir / "input.txt").open("w", encoding="utf-8") as f:
                f.write(input_content)

            with (instance_dir / "output.txt").open("w", encoding="utf-8") as f:
                f.write(f"ERROR: {exc}")

        processed = idx + 1
        if processed == 1 or processed == total_rows or (processed % int(os.getenv("PROGRESS_LOG_EVERY", "10")) == 0):
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0.0
            remaining = max(0, total_rows - processed)
            eta = (remaining / rate) if rate > 0 else 0.0
            pct = (processed / total_rows * 100.0) if total_rows else 100.0
            logger.info(
                f"Progress: {processed}/{total_rows} ({pct:.1f}%) | elapsed {_format_duration(elapsed)} | "
                f"rate {rate:.2f} it/s | ETA {_format_duration(eta)}"
            )

    total_elapsed = time.time() - start_time
    logger.info(f"Completed {total_rows} rows in {_format_duration(total_elapsed)}")
    logger.info(f"Saved per-instance files under: {output_root}")

    # Final GPU snapshot
    try:
        log_gpu_overview(logger)
    except Exception:
        pass

    try:
        gpu_monitor.stop()
    except Exception:
        pass

    # Method-level cleanup
    try:
        method_runner.cleanup()
    except Exception:
        pass


def main() -> None:
    run_pipeline()


if __name__ == "__main__":
    main()
