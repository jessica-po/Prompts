import argparse
import csv
import os
import sys
import uuid
from typing import List, Optional


REQUIRED_INPUT_COLUMNS: List[str] = [
    "lang",
    "vulnerability",
    "system",
    "question",
    "chosen",
    "rejected",
]

OUTPUT_COLUMNS: List[str] = [
    "id",
    "lang",
    "vulnerability",
    "system",
    "question",
    "vulnerable_code",
    "patched_code",
]


def structure_data_to_schema(input_csv_path: str, output_csv_path: Optional[str] = None, overwrite: bool = False) -> str:
    """Transform input CSV to the target schema.

    Reads rows with columns: lang, vulnerability, system, question, chosen, rejected
    and writes rows with columns: id, lang, vulnerability, system, question, vulnerable_code, patched_code

    Args:
        input_csv_path: Path to the source CSV file.
        output_csv_path: Optional path to write the structured CSV. Defaults to '<input>_structured.csv'.
        overwrite: Whether to overwrite the output file if it already exists.

    Returns:
        The path to the written CSV file.
    """

    if not os.path.isfile(input_csv_path):
        raise FileNotFoundError(f"Input CSV not found: {input_csv_path}")

    if output_csv_path is None:
        base, ext = os.path.splitext(input_csv_path)
        ext = ext or ".csv"
        output_csv_path = f"{base}_structured{ext}"

    # Prevent writing to the same path as input
    if os.path.abspath(input_csv_path) == os.path.abspath(output_csv_path):
        raise ValueError("Output CSV path must differ from input CSV path.")

    if os.path.exists(output_csv_path) and not overwrite:
        raise FileExistsError(
            f"Output file already exists: {output_csv_path}. Use --overwrite to replace it."
        )

    # Read and validate header first without creating the output file prematurely.
    with open(input_csv_path, mode="r", encoding="utf-8", newline="") as input_file:
        input_reader = csv.DictReader(input_file)
        if input_reader.fieldnames is None:
            raise ValueError("Input CSV is missing a header row.")

        missing_columns = [col for col in REQUIRED_INPUT_COLUMNS if col not in input_reader.fieldnames]
        if missing_columns:
            missing_str = ", ".join(missing_columns)
            raise ValueError(
                f"Input CSV is missing required columns: {missing_str}. "
                f"Found columns: {', '.join(input_reader.fieldnames)}"
            )

        # Now open output and write transformed rows
        with open(output_csv_path, mode="w", encoding="utf-8", newline="") as output_file:
            output_writer = csv.DictWriter(output_file, fieldnames=OUTPUT_COLUMNS, extrasaction="ignore")
            output_writer.writeheader()

            rows_written = 0
            for row in input_reader:
                # Build transformed row
                transformed_row = {
                    "id": str(uuid.uuid4()),
                    "lang": (row.get("lang") or "").strip(),
                    "vulnerability": (row.get("vulnerability") or "").strip(),
                    "system": row.get("system") or "",
                    "question": row.get("question") or "",
                    "vulnerable_code": row.get("rejected") or "",
                    "patched_code": row.get("chosen") or "",
                }

                output_writer.writerow(transformed_row)
                rows_written += 1

    # Basic sanity check: ensure file has at least header written
    if rows_written == 0:
        # Allow empty datasets, but warn via stderr
        print(
            f"Warning: No data rows found in input. Wrote only header to: {output_csv_path}",
            file=sys.stderr,
        )

    return output_csv_path


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Transform a CSV with columns [lang, vulnerability, system, question, chosen, rejected] "
            "into a structured CSV with [id, lang, vulnerability, system, question, vulnerable_code, patched_code]."
        )
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input_csv",
        required=True,
        help="Path to the input CSV file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_csv",
        required=False,
        help="Optional path for the output CSV file. Defaults to '<input>_structured.csv'.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    try:
        args = _parse_args(argv)
        written_path = structure_data_to_schema(
            input_csv_path=args.input_csv,
            output_csv_path=args.output_csv,
            overwrite=args.overwrite,
        )
        print(f"Wrote structured CSV to: {written_path}")
        return 0
    except (FileNotFoundError, FileExistsError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    except Exception as unexpected:
        print(f"Unexpected error: {unexpected}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())


