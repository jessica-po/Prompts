from __future__ import annotations

import argparse
import os
from pathlib import Path
import runpy
from src.methods import available_methods


def run_generation_pipeline(dataset_path: str, model_name: str | None, method: str, output_path: str | None) -> None:
    """Entry point to execute the dataset-driven generation pipeline.

    Delegates execution to src/run/run.py via runpy, passing parameters via
    environment variables to avoid fragile import paths.
    """
    if model_name:
        os.environ["LOCAL_LLM_MODEL"] = model_name
    os.environ["PIPELINE_DATASET_PATH"] = dataset_path
    os.environ["PROMPT_METHOD"] = method
    if output_path:
        os.environ["PIPELINE_OUTPUT_PATH"] = output_path
    # Optional generation ratio
    gen_ratio = os.getenv("PIPELINE_GEN_RATIO")
    if gen_ratio:
        os.environ["PIPELINE_GEN_RATIO"] = gen_ratio

    script_path = Path(__file__).parent / "run" / "run.py"
    runpy.run_path(str(script_path), run_name="__main__")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dataset-driven code generation pipeline")
    parser.add_argument(
        "--dataset",
        "-d",
        type=str,
        required=True,
        help="Path to the input dataset CSV",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default=None,
        help="Hugging Face model id to use (sets LOCAL_LLM_MODEL)",
    )
    parser.add_argument(
        "--method",
        "-p",
        choices=available_methods(),
        required=True,
        help="Prompting method to use",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Output CSV path (directory or file). If directory, a filename is auto-generated.",
    )
    parser.add_argument(
        "--gen-ratio",
        type=float,
        default=None,
        help="Fraction of output tokens to reserve for generation (0.0-1.0). Overrides default split.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.gen_ratio is not None:
        os.environ["PIPELINE_GEN_RATIO"] = str(args.gen_ratio)
    run_generation_pipeline(dataset_path=args.dataset, model_name=args.model, method=args.method, output_path=args.output)


if __name__ == "__main__":
    main()


