from __future__ import annotations

from typing import Dict, Any, List
from pathlib import Path

from src.methods import MethodRunner, register_method
from src.models.llm_base import GenerationParams
from src.utils.utils import load_prompt_template, safe_format


class PlanningExplanationRunner:
    def __init__(self) -> None:
        self._context: Dict[str, Any] = {}

    def setup(self, context: Dict[str, Any]) -> None:
        self._context = dict(context)

    def _resolve_prompts(self, fallback_system: str, fallback_user: str, suffix: str = "") -> tuple[str, str]:
        method = str(self._context.get("method", "4_planning_explanation")).strip() or "4_planning_explanation"
        try:
            prompts_dir = Path(__file__).resolve().parents[1] / "prompts" / method
            system_path = prompts_dir / ("system" + suffix + ".txt")
            user_path = prompts_dir / ("user" + suffix + ".txt")
            system = load_prompt_template(system_path) if system_path.exists() else fallback_system
            user = load_prompt_template(user_path) if user_path.exists() else fallback_user
            return system, user
        except Exception:
            return fallback_system, fallback_user

    def run_sample(self, mapping: Dict[str, str], model: Any, system_template: str, user_template: str, gen_max_new_tokens: int | None = None) -> Dict[str, Any]:
        # Stage 1
        s1_sys, s1_user = self._resolve_prompts(system_template, user_template, suffix="")
        system1 = safe_format(s1_sys, mapping)
        user1 = safe_format(s1_user, mapping)
        messages1: List[Dict[str, str]] = [
            {"role": "system", "content": system1},
            {"role": "user", "content": user1},
        ]
        if gen_max_new_tokens is not None:
            plan = model.generate(messages1, params=GenerationParams(max_new_tokens=gen_max_new_tokens))
        else:
            plan = model.generate(messages1)

        # Stage 2
        s2_sys, s2_user = self._resolve_prompts(system_template, user_template, suffix="_2")
        mapping2 = dict(mapping)
        mapping2["plan"] = plan
        mapping2["previous_output"] = plan
        system2 = safe_format(s2_sys, mapping2)
        user2 = safe_format(s2_user, mapping2)
        messages2: List[Dict[str, str]] = [
            {"role": "system", "content": system2},
            {"role": "user", "content": user2},
        ]
        if gen_max_new_tokens is not None:
            completion = model.generate(messages2, params=GenerationParams(max_new_tokens=gen_max_new_tokens))
        else:
            completion = model.generate(messages2)

        # Aggregate trace
        trace = [
            {"role": "system", "content": system1},
            {"role": "user", "content": user1},
            {"role": "assistant", "content": plan},
            {"role": "system", "content": system2},
            {"role": "user", "content": user2},
        ]

        return {
            "messages": trace,
            "completion": completion,
            "stages": [
                {"stage": 1, "messages": messages1, "completion": plan},
                {"stage": 2, "messages": messages2, "completion": completion},
            ],
        }

    def cleanup(self) -> None:
        self._context.clear()


register_method("4_planning_explanation", PlanningExplanationRunner)


