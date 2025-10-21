from pathlib import Path
import re
from typing import Dict, Optional

def load_prompt_template(prompt_file: Path) -> str:
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_file}")
    with open(prompt_file, "r", encoding="utf-8") as f:
        return f.read()

def sanitize_for_path(text: str) -> str:
    # Replace any non filename-friendly chars with dashes
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    return sanitized.strip("-")

class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # type: ignore[override]
        return ""

def safe_format(template: str, mapping: Dict[str, str]) -> str:
    """Safely format a template using mapping, leaving missing keys empty.

    This mirrors str.format_map with a dict that returns empty strings for missing keys.
    """
    return template.format_map(_SafeDict(mapping))

def load_dotenv_vars() -> Dict[str, str]:
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
                val = val.strip().strip("\"'")
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
                return parsed
    return {}

def truncate_text_for_prompt(
    tokenizer,
    max_input_tokens: int,
    system_prompt: str,
    user_prompt_template: str,
    placeholder_key: str,
    text: str,
    safety_ratio: float = 0.1,
    safety_min_tokens: int = 64,
    min_allowed_tokens: int = 128,
) -> str:
    """Truncate text to fit within model input token budget.

    Args:
        tokenizer: HuggingFace tokenizer instance for encoding/decoding text.
        max_input_tokens: Maximum input token limit for the model.
        system_prompt: System prompt template string.
        user_prompt_template: User prompt template containing a placeholder.
        placeholder_key: Name of the placeholder in the user template (e.g., "code", "description").
        text: Content to insert into the template and truncate if necessary.
        safety_ratio: Fraction of max tokens to reserve as safety margin (default: 0.1).
        safety_min_tokens: Minimum safety margin in tokens (default: 64).
        min_allowed_tokens: Minimum tokens allowed for the text content (default: 128).

    Returns:
        str: The original text if it fits, otherwise truncated text that fits within the token budget.

    Note:
        Calculates token overhead from system and user prompts, applies safety margins,
        and truncates the input text to fit within the remaining token allowance.
    """
    try:
        empty_user = user_prompt_template.format(**{placeholder_key: ""})
    except Exception:
        empty_user = user_prompt_template

    sys_tokens = len(tokenizer.encode(system_prompt, add_special_tokens=False))
    user_tokens = len(tokenizer.encode(empty_user, add_special_tokens=False))
    overhead = sys_tokens + user_tokens

    safety_margin = max(safety_min_tokens, int(safety_ratio * max_input_tokens))
    allowed_tokens = max(min_allowed_tokens, max_input_tokens - overhead - safety_margin)

    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) <= allowed_tokens:
        return text

    truncated_ids = input_ids[:allowed_tokens]
    return tokenizer.decode(truncated_ids, skip_special_tokens=True)

def parse_repo_and_filename(description_file_path: Path) -> tuple[str, str]:
    """Parse repo name and output filename (.py) from a description file path.

    Expected description filename patterns (base name without the trailing .txt):
    - reponame--filename.py
    - reponame--filename (".py" will be appended)
    - filename.py (repo will default to "misc")
    - filename (".py" will be appended; repo defaults to "misc")
    """
    stem = description_file_path.stem  # removes only the last suffix (.txt)
    if "--" in stem:
        repo_part, file_part = stem.split("--", 1)
        repo_name = repo_part.strip() or "misc"
        file_name = file_part.strip()
    else:
        repo_name = "misc"
        file_name = stem.strip()

    if not file_name.endswith(".py"):
        file_name = f"{file_name}.py"

    repo_name = sanitize_for_path(repo_name)
    file_name = sanitize_for_path(file_name)
    return repo_name, file_name