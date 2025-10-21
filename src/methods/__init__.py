from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Dict, Callable, Any, List, Optional
from pathlib import Path
import importlib
import pkgutil


class MethodRunner(Protocol):
    def setup(self, context: Dict[str, Any]) -> None: ...
    def run_sample(self, mapping: Dict[str, str], model: Any, system_template: str, user_template: str, gen_max_new_tokens: Optional[int] | None = None) -> Dict[str, Any]: ...
    def cleanup(self) -> None: ...


_registry: Dict[str, Callable[[], MethodRunner]] = {}
_loaded: bool = False


def _ensure_loaded() -> None:
    global _loaded
    if _loaded:
        return
    try:
        pkg_path = Path(__file__).resolve().parent
        for modinfo in pkgutil.iter_modules([str(pkg_path)]):
            name = modinfo.name
            if name.startswith("_"):
                continue
            # Import submodule to trigger registration side-effects
            importlib.import_module(f"{__name__}.{name}")
        _loaded = True
    except Exception:
        # Best-effort; registry may be populated elsewhere
        _loaded = True


def register_method(name: str, factory: Callable[[], MethodRunner]) -> None:
    key = name.strip()
    if not key:
        raise ValueError("Method name cannot be empty")
    _registry[key] = factory


def get_method(name: str) -> MethodRunner:
    _ensure_loaded()
    key = name.strip()
    if key not in _registry:
        raise KeyError(f"Unknown method: {name}. Available: {sorted(_registry.keys())}")
    return _registry[key]()


def available_methods() -> List[str]:
    _ensure_loaded()
    return sorted(_registry.keys())


__all__ = [
    "MethodRunner",
    "register_method",
    "get_method",
    "available_methods",
]


