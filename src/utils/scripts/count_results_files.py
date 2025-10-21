#!/usr/bin/env python3
"""
Recursively count files under a target root (default: data/results) and print:
  - Grand total files under the root
  - Top-level children summary (direct and recursive totals)
  - Per-directory tree breakdown (direct and recursive totals)

Usage:
  python src/utils/scripts/count_results_files.py [--levels {1,2,3}] [ROOT_DIR]
  python -m src.utils.scripts.count_results_files [--levels {1,2,3}] [ROOT_DIR]

Examples:
  python src/utils/scripts/count_results_files.py                # assumes ./data/results exists
  python src/utils/scripts/count_results_files.py data/results
  python -m src.utils.scripts.count_results_files data/results
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Dict, List, Optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively counts files in each directory under ROOT_DIR, "
            "summarizing parent (recursive) and subfolder file counts."
        )
    )
    parser.add_argument(
        "-l",
        "--levels",
        type=int,
        choices=(1, 2, 3),
        help="Limit directory tree depth to N levels (1, 2, or 3).",
    )
    parser.add_argument(
        "root_dir",
        nargs="?",
        default="data/results",
        help="Root directory to scan (default: data/results)",
    )
    return parser.parse_args()


def build_directory_maps(root_dir: Path) -> tuple[
    Dict[Path, int], Dict[Path, List[Path]], List[Path]
]:
    """Build maps for direct file counts and directory hierarchy.

    Returns:
        dir_to_direct_count: number of files directly in each directory
        parent_to_children: mapping from directory to its immediate subdirectories
        all_dirs: list of all directories under root (including root)
    """
    dir_to_direct_count: Dict[Path, int] = {}
    parent_to_children: Dict[Path, List[Path]] = {}
    all_dirs: List[Path] = []

    # Ensure deterministic traversal order
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        dirnames.sort()
        filenames.sort()
        current_dir = Path(dirpath)
        all_dirs.append(current_dir)
        parent_to_children[current_dir] = [current_dir / d for d in dirnames]
        dir_to_direct_count[current_dir] = len(filenames)

    # Ensure all discovered directories have an entry
    for d in all_dirs:
        dir_to_direct_count.setdefault(d, 0)
        parent_to_children.setdefault(d, [])

    return dir_to_direct_count, parent_to_children, all_dirs


def compute_recursive_counts(
    root_dir: Path,
    dir_to_direct_count: Dict[Path, int],
    parent_to_children: Dict[Path, List[Path]],
    all_dirs: List[Path],
) -> Dict[Path, int]:
    """Compute recursive (aggregate) file counts per directory using post-order traversal."""

    def depth(p: Path) -> int:
        if p == root_dir:
            return 0
        return len(p.relative_to(root_dir).parts)

    # Post-order: deepest directories first
    ordered = sorted(all_dirs, key=lambda p: depth(p), reverse=True)
    dir_to_recursive_count: Dict[Path, int] = {}

    for d in ordered:
        total = dir_to_direct_count.get(d, 0)
        for child in parent_to_children.get(d, []):
            total += dir_to_recursive_count.get(child, 0)
        dir_to_recursive_count[d] = total

    return dir_to_recursive_count


def relpath(root_dir: Path, p: Path) -> str:
    if p == root_dir:
        return "."
    return str(p.relative_to(root_dir))


def print_top_level_summary(
    root_dir: Path,
    dir_to_direct_count: Dict[Path, int],
    dir_to_recursive_count: Dict[Path, int],
    parent_to_children: Dict[Path, List[Path]],
) -> None:
    children = sorted(parent_to_children.get(root_dir, []), key=lambda x: x.name)
    print("Top-level children summary:")
    if not children:
        print("  (no subdirectories)")
        return
    for child in children:
        direct = dir_to_direct_count.get(child, 0)
        recursive = dir_to_recursive_count.get(child, 0)
        print(f"  {relpath(root_dir, child)}  direct={direct}  total={recursive}")


def print_directory_tree(
    root_dir: Path,
    dir_to_direct_count: Dict[Path, int],
    dir_to_recursive_count: Dict[Path, int],
    levels: Optional[int] = None,
) -> None:
    print("Per-directory tree breakdown:")

    for dirpath, dirnames, _ in os.walk(root_dir, topdown=True):
        dirnames.sort()
        current_dir = Path(dirpath)
        depth = 0 if current_dir == root_dir else len(current_dir.relative_to(root_dir).parts)
        # If a depth limit is set, prune traversal beyond that limit and skip printing deeper paths.
        if levels is not None and depth > levels:
            # Should not occur due to pruning below, but kept as an extra guard.
            continue
        if levels is not None and depth >= levels:
            # Prevent descending into deeper subdirectories once limit is reached.
            dirnames[:] = []
        indent = " " * (depth * 2)
        direct = dir_to_direct_count.get(current_dir, 0)
        recursive = dir_to_recursive_count.get(current_dir, 0)
        print(f"{indent}{relpath(root_dir, current_dir)}  direct={direct}  total={recursive}")


def main() -> None:
    args = parse_args()
    root_input = Path(args.root_dir)
    root_dir = root_input if root_input.is_absolute() else (Path.cwd() / root_input)
    try:
        root_dir = root_dir.resolve()
    except Exception:  # pragma: no cover - safety for exotic FS
        pass

    if not root_dir.exists() or not root_dir.is_dir():
        print(f"Error: directory not found: {args.root_dir}")
        print("Hint: pass an existing results folder or run from the repo root.")
        return

    dir_to_direct_count, parent_to_children, all_dirs = build_directory_maps(root_dir)
    dir_to_recursive_count = compute_recursive_counts(
        root_dir, dir_to_direct_count, parent_to_children, all_dirs
    )

    print(f"Root: {root_dir.name}")
    print(f"Path: {root_dir}")
    print()
    grand_total = dir_to_recursive_count.get(root_dir, 0)
    print(f"Grand total files: {grand_total}")
    print()

    print_top_level_summary(
        root_dir, dir_to_direct_count, dir_to_recursive_count, parent_to_children
    )
    print()
    print_directory_tree(
        root_dir,
        dir_to_direct_count,
        dir_to_recursive_count,
        levels=getattr(args, "levels", None),
    )
    print()
    print("Done.")


if __name__ == "__main__":
    main()


