from __future__ import annotations

from typing import Dict, Any

from src.methods import MethodRunner, register_method
from src.models.llm_base import GenerationParams


class XaiRunner:
    def __init__(self) -> None:
        self._context: Dict[str, Any] = {}

    def setup(self, context: Dict[str, Any]) -> None:
        self._context = dict(context)

    def run_sample(self, mapping: Dict[str, str], model: Any, system_template: str, user_template: str, gen_max_new_tokens: int | None = None) -> Dict[str, Any]:
        # For now, same as single-shot; future methods can diverge without touching core pipeline
        user_prompt = user_template.format_map(_SafeDict(mapping))
        messages = [
            {"role": "system", "content": system_template},
            {"role": "user", "content": user_prompt},
        ]
        if gen_max_new_tokens is not None:
            completion = model.generate(messages, params=GenerationParams(max_new_tokens=gen_max_new_tokens))
        else:
            completion = model.generate(messages)
        return {
            "messages": messages,
            "completion": completion,
        }

    def cleanup(self) -> None:
        self._context.clear()


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # type: ignore[override]
        return ""


register_method("2_xai", XaiRunner)


