#!/usr/bin/env bash

set -euo pipefail

# Recursively count files for all directories under a target root (default: results),
# printing a per-directory tree with counts and a top-level summary.

print_usage() {
  cat <<'USAGE'
Usage: scripts/count_results_files.sh [ROOT_DIR]

Description:
  Recursively counts files in each directory under ROOT_DIR (default: results),
  summarizing counts for parent and subfolders. Outputs:
    - Grand total for ROOT_DIR
    - Top-level children summary (each immediate subdirectory)
    - Per-directory tree breakdown (all nested directories)

Examples:
  scripts/count_results_files.sh                # assumes ./results exists
  scripts/count_results_files.sh /path/to/results
  scripts/count_results_files.sh results-2025-10-16
USAGE
}

if [[ ${1:-} == "-h" || ${1:-} == "--help" ]]; then
  print_usage
  exit 0
fi

ROOT_DIR_INPUT=${1:-results}

# Normalize ROOT_DIR to an absolute path for stable handling
if [[ ${ROOT_DIR_INPUT} = /* ]]; then
  ROOT_DIR=${ROOT_DIR_INPUT}
else
  ROOT_DIR=$(cd "${PWD}" && cd "${ROOT_DIR_INPUT}" 2>/dev/null && pwd || true)
fi

if [[ -z "${ROOT_DIR}" || ! -d "${ROOT_DIR}" ]]; then
  echo "Error: directory not found: ${ROOT_DIR_INPUT}" >&2
  echo "Hint: pass an existing results folder or run from the repo root." >&2
  echo >&2
  print_usage >&2
  exit 1
fi

declare -A DIR_TO_FILE_COUNT
TOTAL_FILES=0

# Count files per directory using NUL delimiters for robust path handling
while IFS= read -r -d '' file_path; do
  dir_path=$(dirname -- "${file_path}")
  # Initialize if missing, then increment
  if [[ -z ${DIR_TO_FILE_COUNT["${dir_path}"]+set} ]]; then
    DIR_TO_FILE_COUNT["${dir_path}"]=0
  fi
  (( DIR_TO_FILE_COUNT["${dir_path}"]++ ))
  (( TOTAL_FILES++ ))
done < <(find "${ROOT_DIR}" -type f -print0)

# Ensure all directories are present in the map (even if they have 0 files)
while IFS= read -r dir; do
  if [[ -z ${DIR_TO_FILE_COUNT["${dir}"]+set} ]]; then
    DIR_TO_FILE_COUNT["${dir}"]=0
  fi
done < <(LC_ALL=C find "${ROOT_DIR}" -type d | LC_ALL=C sort)

# Helper to compute a path relative to ROOT_DIR for nicer printing
relpath() {
  local abs="$1"
  if [[ "${abs}" == "${ROOT_DIR}" ]]; then
    echo "."
    return
  fi
  local rel
  rel="${abs#"${ROOT_DIR}/"}"
  echo "${rel}"
}

# Compute and print top-level children summary
echo "Root: $(basename -- "${ROOT_DIR}")"
echo "Path: ${ROOT_DIR}"
echo
echo "Grand total files: ${TOTAL_FILES}"
echo

echo "Top-level children summary:"
TOP_CHILDREN=$(LC_ALL=C find "${ROOT_DIR}" -mindepth 1 -maxdepth 1 -type d | LC_ALL=C sort)
if [[ -z "${TOP_CHILDREN}" ]]; then
  echo "  (no subdirectories)"
else
  while IFS= read -r child; do
    [[ -z "${child}" ]] && continue
    count=${DIR_TO_FILE_COUNT["${child}"]}
    printf "  %s  %s\n" "$(relpath "${child}")" "${count}"
  done <<<"${TOP_CHILDREN}"
fi

echo
echo "Per-directory tree breakdown:"

# Gather all directories for tree printing
mapfile -t ALL_DIRS < <(LC_ALL=C find "${ROOT_DIR}" -type d | LC_ALL=C sort)

for dir in "${ALL_DIRS[@]}"; do
  rel=$(relpath "${dir}")
  # Depth is number of path components ("." is depth 0)
  if [[ "${rel}" == "." ]]; then
    depth=0
  else
    # Count components by replacing "/" with newlines and counting lines
    depth=$(awk -v p="${rel}" 'BEGIN{n=split(p,a,"/"); print n}')
  fi
  indent=$(( depth * 2 ))
  count=${DIR_TO_FILE_COUNT["${dir}"]}
  printf "%*s%s  %s\n" "${indent}" "" "${rel}" "${count}"
done

echo
echo "Done."


