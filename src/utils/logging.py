from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Optional


_LEVEL_NAME = os.getenv("LOG_LEVEL", "INFO").upper()
_LEVEL = getattr(logging, _LEVEL_NAME, logging.INFO)


def _get_default_fmt() -> str:
    return "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def _get_default_datefmt() -> str:
    return "%Y-%m-%d %H:%M:%S"


def setup_logging(level: int | str = _LEVEL, fmt: Optional[str] = None, datefmt: Optional[str] = None) -> None:
    """Initialize root logging once with a consistent format.

    Safe to call multiple times; subsequent calls only adjust levels.
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=level,
            format=fmt or _get_default_fmt(),
            datefmt=datefmt or _get_default_datefmt(),
        )
    else:
        logging.getLogger().setLevel(level)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a module-scoped logger after ensuring logging is configured."""
    setup_logging()
    return logging.getLogger(name if name is not None else __name__)


def add_file_logging(path: str | os.PathLike | Path, level: int | str | None = None, mode: str = "a") -> logging.Handler:
    """Attach a FileHandler to the root logger (idempotent per path)."""
    setup_logging()
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Deduplicate: reuse existing handler if already attached for the same path
    root = logging.getLogger()
    resolved = str(file_path.resolve())
    for h in root.handlers:
        try:
            existing = getattr(h, "baseFilename", None)
            if existing and str(Path(existing).resolve()) == resolved:
                if level is not None:
                    if isinstance(level, str):
                        h.setLevel(getattr(logging, level.upper(), logging.INFO))
                    else:
                        h.setLevel(level)
                return h
        except Exception:
            continue

    handler = logging.FileHandler(file_path, mode=mode, encoding="utf-8")
    handler.setFormatter(logging.Formatter(_get_default_fmt(), datefmt=_get_default_datefmt()))
    if level is None:
        level = logging.getLogger().level
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    handler.setLevel(level)
    root.addHandler(handler)
    return handler


__all__ = ["setup_logging", "get_logger", "add_file_logging"]


