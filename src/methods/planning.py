from __future__ import annotations

from pathlib import Path
from typing import Dict, Any, List

from src.methods import MethodRunner, register_method
from src.models.llm_base import GenerationParams
from src.utils.utils import load_prompt_template, safe_format


class PlanningRunner:
    def __init__(self) -> None:
        self._context: Dict[str, Any] = {}

    def setup(self, context: Dict[str, Any]) -> None:
        self._context = dict(context)

    def _resolve_stage2_prompts(self, fallback_system: str, fallback_user: str) -> tuple[str, str]:
        method = str(self._context.get("method", "3_planning")).strip() or "3_planning"
        try:
            prompts_dir = Path(__file__).resolve().parents[1] / "prompts" / method
            system2_path = prompts_dir / "system_2.txt"
            user2_path = prompts_dir / "user_2.txt"
            system2 = load_prompt_template(system2_path) if system2_path.exists() else fallback_system
            user2 = load_prompt_template(user2_path) if user2_path.exists() else (fallback_user + "\n\n[PREVIOUS_OUTPUT]\n{plan}")
            return system2, user2
        except Exception:
            return fallback_system, (fallback_user + "\n\n[PREVIOUS_OUTPUT]\n{plan}")

    def run_sample(self, mapping: Dict[str, str], model: Any, system_template: str, user_template: str, gen_max_new_tokens: int | None = None) -> Dict[str, Any]:
        # Stage 1: plan
        system1 = safe_format(system_template, mapping)
        user1 = safe_format(user_template, mapping)
        messages1: List[Dict[str, str]] = [
            {"role": "system", "content": system1},
            {"role": "user", "content": user1},
        ]
        if gen_max_new_tokens is not None:
            plan = model.generate(messages1, params=GenerationParams(max_new_tokens=gen_max_new_tokens))
        else:
            plan = model.generate(messages1)

        # Stage 2: act using plan
        system2_template, user2_template = self._resolve_stage2_prompts(system_template, user_template)
        mapping2 = dict(mapping)
        mapping2["plan"] = plan
        mapping2["output_1"] = plan
        mapping2["previous_output"] = plan
        system2 = safe_format(system2_template, mapping2)
        user2 = safe_format(user2_template, mapping2)
        messages2: List[Dict[str, str]] = [
            {"role": "system", "content": system2},
            {"role": "user", "content": user2},
        ]
        if gen_max_new_tokens is not None:
            completion = model.generate(messages2, params=GenerationParams(max_new_tokens=gen_max_new_tokens))
        else:
            completion = model.generate(messages2)

        # For logging, include a trace of both stages
        trace_messages: List[Dict[str, str]] = [
            {"role": "system", "content": system1},
            {"role": "user", "content": user1},
            {"role": "assistant", "content": plan},
            {"role": "system", "content": system2},
            {"role": "user", "content": user2},
        ]

        return {
            "messages": trace_messages,
            "completion": completion,
            "stages": [
                {
                    "stage": 1,
                    "messages": messages1,
                    "completion": plan,
                },
                {
                    "stage": 2,
                    "messages": messages2,
                    "completion": completion,
                },
            ],
        }

    def cleanup(self) -> None:
        self._context.clear()


register_method("3_planning", PlanningRunner)


