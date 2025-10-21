import argparse
import csv
import json
import os
import re
from typing import Dict, Iterable, Iterator, List, Tuple


DEFAULT_FIELDNAMES: List[str] = [
    "lang",
    "vulnerability",
    "system",
    "question",
    "chosen",
    "rejected",
]


LANGUAGE_FILENAME_MAP: Dict[str, str] = {
    "c++": "cpp",
    "objective-c++": "objective_cpp",
    "objective-c": "objective_c",
    "c#": "csharp",
    "f#": "fsharp",
}


def canonicalize_language_for_filename(lang_value: str) -> str:
    """Return a safe filename stem for a language value."""
    normalized = (lang_value or "").strip().lower()
    if not normalized:
        return "unknown"
    if normalized in LANGUAGE_FILENAME_MAP:
        return LANGUAGE_FILENAME_MAP[normalized]
    slug = re.sub(r"[^a-z0-9]+", "_", normalized).strip("_")
    return slug or "unknown"


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def detect_json_container_type(input_path: str) -> str:
    """Detect whether the file is a JSON array or JSON Lines (jsonl).

    Returns:
        "array" or "jsonl"
    """
    with open(input_path, "r", encoding="utf-8-sig") as f:
        while True:
            ch = f.read(1)
            if ch == "":
                return "jsonl"
            if ch.isspace():
                continue
            return "array" if ch == "[" else "jsonl"


def iter_records(input_path: str) -> Iterator[dict]:
    container_type = detect_json_container_type(input_path)
    if container_type == "array":
        with open(input_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    yield item
        return

    # JSON Lines fallback
    with open(input_path, "r", encoding="utf-8-sig") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                obj = json.loads(stripped)
            except json.JSONDecodeError:
                # Skip malformed lines
                continue
            if isinstance(obj, dict):
                yield obj


def project_record_fields(record: dict) -> dict:
    return {key: record.get(key, "") for key in DEFAULT_FIELDNAMES}


def open_writer_for_language(
    output_dir: str, language_value: str, append: bool
) -> Tuple[str, csv.DictWriter, object]:
    filename_stem = canonicalize_language_for_filename(language_value)
    output_path = os.path.join(output_dir, f"{filename_stem}.csv")
    mode = "a" if append else "w"
    file_handle = open(output_path, mode, encoding="utf-8", newline="")
    writer = csv.DictWriter(file_handle, fieldnames=DEFAULT_FIELDNAMES)
    if file_handle.tell() == 0:
        writer.writeheader()
    return output_path, writer, file_handle


def split_dataset_by_language(input_path: str, output_dir: str, append: bool) -> Dict[str, int]:
    ensure_directory(output_dir)

    writers: Dict[str, Tuple[str, csv.DictWriter, object]] = {}
    counts: Dict[str, int] = {}

    try:
        for record in iter_records(input_path):
            language_value = record.get("lang") or "unknown"
            filename_stem = canonicalize_language_for_filename(language_value)

            if filename_stem not in writers:
                writers[filename_stem] = open_writer_for_language(output_dir, language_value, append)

            _, writer, _ = writers[filename_stem]
            writer.writerow(project_record_fields(record))
            counts[filename_stem] = counts.get(filename_stem, 0) + 1
    finally:
        # Close all file handles
        for _, _, fh in writers.values():
            try:
                fh.close()
            except Exception:
                pass

    return counts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split HF secure_programming_dpo dataset into per-language CSV files."
    )
    parser.add_argument(
        "-i",
        "--input",
        default=os.path.join(
            "data", "original_dataset", "hf_cybernative_code_vuln", "secure_programming_dpo.json"
        ),
        help="Path to input JSON/JSONL dataset",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=os.path.join("data", "processed_dataset", "hf"),
        help="Output directory for per-language CSV files",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to existing per-language CSVs instead of overwriting",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input
    output_dir = args.output
    append = args.append

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input dataset not found: {input_path}")

    counts = split_dataset_by_language(input_path, output_dir, append)

    total = sum(counts.values())
    print(f"Wrote {total} rows across {len(counts)} CSV files in '{output_dir}'.")
    for filename_stem, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  - {filename_stem}.csv: {count} rows")


if __name__ == "__main__":
    main()


