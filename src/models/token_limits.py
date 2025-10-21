"""Token limit configuration per local model.

This module centralizes input/output token limits for locally hosted
Transformer chat models. Use these limits to constrain generation and
avoid exceeding context windows.

Note: Values are conservative defaults gathered from public model cards
and common runtimes. Adjust if you know your exact context window.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class TokenLimits:
    """Holds input and output token limits for a model."""

    input_tokens: int
    output_tokens: int


_DEFAULT_LIMITS = TokenLimits(input_tokens=8192, output_tokens=1024)


# Known models and their typical context windows (conservative).
# If your specific weights support larger windows, update here.
MODEL_TOKEN_LIMITS: Dict[str, TokenLimits] = {
    "google/gemma-3-27b-it": TokenLimits(input_tokens=8192, output_tokens=2048),
    "meta-llama/CodeLlama-34B-Instruct-hf": TokenLimits(input_tokens=16384, output_tokens=4096),
    "Qwen/Qwen3-32B": TokenLimits(input_tokens=32768, output_tokens=2048),
    "Qwen/Qwen3-Coder-30B-A3B-Instruct": TokenLimits(input_tokens=32768, output_tokens=16384),
    "google/gemma-3-1b-it": TokenLimits(input_tokens=8192, output_tokens=2048),

}


def get_token_limits(model_name: str) -> TokenLimits:
    """Return TokenLimits for the given model name.

    Falls back to a conservative default if the model is unknown.
    """

    # Exact match first
    if model_name in MODEL_TOKEN_LIMITS:
        return MODEL_TOKEN_LIMITS[model_name]

    # Try case-insensitive match
    lowered = model_name.lower()
    for key, val in MODEL_TOKEN_LIMITS.items():
        if key.lower() == lowered:
            return val

    return _DEFAULT_LIMITS


__all__ = [
    "TokenLimits",
    "MODEL_TOKEN_LIMITS",
    "get_token_limits",
]


