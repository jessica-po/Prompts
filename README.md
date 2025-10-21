# Prompts
Exploration of LLM-applied Automated Vulnerability Repair (AVR) and explainability techniques

# Installation
We use Python 3.10, packages available within `requirements.txt`

# Dataset
## Dataset Pre-Processing

As we utilize a variety of different datasets in our method, and we simplify out approach to standardize and examine only the Python programming language, we must pre-process each incoming dataset into a similar schema for use within our methodology.

### KAGGLE_VULNERABILITY_FIX
This project contains untagged vulnerable and fixed code from a variety of datasets. As such, we create a utility file to parse out Python projects

1. Remove "No response generated" cases.
```bash
python -m data.utils.kaggle.process_missing_data data/original_dataset/kaggle_vulnerability_fix/vulnerability_fix_dataset.csv --output data/original_dataset/kaggle_vulnerability_fix/vulnerability_fix_dataset_clean.csv
```

Results:
```
Input rows: 35000
Output rows (clean): 32370
Rows dropped: 2630
Missing in vulnerable_code: 2507
Missing in fixed_code: 2508
Missing in both: 2385
Missing in either: 2630
Clean file: data\original_dataset\kaggle_vulnerability_fix\vulnerability_fix_dataset_clean.csv
```

2. Split Dataset
```bash
python -m data.utils.kaggle.process_vulnerability_fix data/original_dataset/kaggle_vulnerability_fix/vulnerability_fix_dataset_clean.csv --output data/processed_dataset/kaggle/vulnerability_fix.csv
```
Results:
```
Incoming rows: 32370
Outgoing rows (total): 32370
  java:   32246 -> data\processed_dataset\kaggle\vulnerability_fix_java.csv
  python: 0 -> data\processed_dataset\kaggle\vulnerability_fix_python.csv
  c:      0 -> data\processed_dataset\kaggle\vulnerability_fix_c.csv
  js:     0 -> data\processed_dataset\kaggle\vulnerability_fix_js.csv
  other:  124 -> data\processed_dataset\kaggle\vulnerability_fix_other.csv
```

Since this repository lacks Python snippets, we exclude from our study.

### HUGGINGFACE CYBERNATIVE CODE VULN

1. Split Dataset
```bash
python -m data.utils.hf_code_vuln.process_code_vuln_data -i data/original_dataset/hf_cybernative_code_vuln/secure_programming_dpo.json -o data/processed_dataset/hf/full_split
```

2. Process to Schema
```bash
python -m data.utils.hf_code_vuln.structure_data_to_schema --input "data\processed_dataset\hf\full_split\python.csv" --output "data\processed_dataset\hf\python_structured.csv" --overwrite
```

Results:
```
Wrote 4656 rows across 11 CSV files in 'data/processed_dataset/hf'.
  - cpp.csv: 424 rows
  - java.csv: 424 rows
  - javascript.csv: 424 rows
  - python.csv: 424 rows
  - csharp.csv: 423 rows
  - go.csv: 423 rows
  - kotlin.csv: 423 rows
  - php.csv: 423 rows
  - ruby.csv: 423 rows
  - swift.csv: 423 rows
  - fortran.csv: 422 rows
```

# Inference

### Pipeline overview
The dataset-driven pipeline reads a CSV, constructs prompts using a selected prompting method, runs a chosen Hugging Face model locally, and writes per-row artifacts to an output directory.

- **Input**: CSV with vulnerability/problem context and/or code
- **Prompts**: `src/prompts/{method}/system.txt` and `src/prompts/{method}/user.txt`
- **Model**: Pulled from Hugging Face Hub (cached locally)
- **Output**: Per-instance folders containing the effective prompts and model output

### CLI
Run the pipeline via `src.main`:

```powershell
python -m src.main --dataset <path/to.csv> --method <1_single_shot|2_xai|3_planning|4_planning_explanation|5_prompt_then_explain> [--model <org/model-id>] [--output <file-or-dir>]
```

Example
python -m src.main --dataset data/processed_dataset/hf/python_structured_with_cwe.csv --method 3_planning --model distilbert/distilgpt2 --output data/results/3_planning/distillgpt
python -m src.main --dataset data/processed_dataset/hf/python_structured_with_cwe.csv --method 4_planning_explanation --model distilbert/distilgpt2 --output data/results/4_planning_explanation/distillgpt
python -m src.main --dataset data/processed_dataset/hf/python_structured_with_cwe.csv --method 5_prompt_then_explain --model distilbert/distilgpt2 --output data/results/5_prompt_then_explain/distillgpt

#### Flags
- **--dataset, -d (required)**: Path to input CSV.
- **--method, -p (required)**: Prompting method. Options include `1_single_shot`, `2_xai`, `3_planning`, `4_planning_explanation`, `5_prompt_then_explain` (auto-discovered from `src/methods`).
- **--model, -m (optional)**: Hugging Face model id (e.g., `meta-llama/Llama-3.1-8B-Instruct`). If omitted, uses `LOCAL_LLM_MODEL` if set, else defaults to `google/gemma-3-27b-it`.
- **--output, -o (optional)**: Output directory behavior:
  - If you pass a directory or a path without an extension, that directory is used (created if needed).
  - If you pass a file-like path with an extension (e.g., `.csv`), a sibling directory with the same stem is used.
  - If omitted, a timestamped directory is created next to the dataset: `<dataset-stem>-<method>-<model>-<timestamp>`.
- **--gen-ratio (optional)**: Fraction of the model's output token budget to use for generation (0.0–1.0). If set, the runner reserves that many output tokens and adjusts prompt truncation accordingly.

### Prompt methods
- **1_single_shot**: Single-pass generation using `src/prompts/1_single_shot/` templates.
- **2_xai**: XAI-oriented prompting using `src/prompts/2_xai/` templates.
- **3_planning**: Two-stage approach using `src/prompts/3_planning/`.
  - Stage 1 uses `system.txt` and `user.txt` to produce a plan.
  - Stage 2 consumes the plan and uses `system_2.txt` and `user_2.txt` if present. If `system_2.txt`/`user_2.txt` are missing, it falls back to Stage 1 templates and appends the plan into the user prompt via `{plan}`.
- **4_planning_explanation**: Like `3_planning` but emphasizes producing a thorough final explanation in stage 2. Prompts under `src/prompts/4_planning_explanation/`.
- **5_prompt_then_explain**: First produce the best answer/fix, then explain it in stage 2. Prompts under `src/prompts/5_prompt_then_explain/`.

You can customize prompts by editing:
- `src/prompts/<method>/system.txt`
- `src/prompts/<method>/user.txt`
- For two-stage methods like `3_planning`, you can optionally add `system_2.txt` and `user_2.txt`.

### Dataset schema (flexible)
The runner is tolerant to common field names and will map what it finds:

- **vulnerability | vulnerability_type**: High-level context
- **question**: Natural-language task/requirement
- **rejected | vulnerable_code**: Vulnerable code snippet (preferred for injection when present)
- **chosen | fixed_code**: Reference fixed code, if available
- **lang | language**: Language hint (optional)

The user prompt template will use whichever placeholder it contains among `{vulnerable_code}`, `{description}`, `{question}`, `{code}`, `{input}`, `{text}`. The runner auto-detects and truncates the injected field to respect the model's input token budget. If the preferred placeholder has no content for a row, it falls back to `{question}` → `{code}` → `{description}`.

### Outputs
- **Output root**: Resolved from `--output` as described above. If `--output` is a file-like path (e.g., `results.csv`), the directory with the same stem (e.g., `results`) is created and used. If omitted, a timestamped directory is created next to the dataset.
- **Per-instance folders**: For each row, a folder named by a stable row id is created. The id is taken from `id | ID | Id | uid | unique_id` if present, otherwise `row-XXXXXX`.
  - `vulnerable_code.txt`: Raw vulnerable code from the dataset (`vulnerable_code` or `rejected`).
  - `input.txt`: The exact prompts used, in the form `[SYSTEM]...` and `[USER]...`.
  - `output.txt`: Model completion or `ERROR: <message>` if the row failed.
- **Logging**: A log file is written by default to `logs/<run_name>/<YYYY-MM-DD>_<method>`, or to the path specified via `PIPELINE_LOG_FILE`/`PIPELINE_LOG_DIR`.

### Examples (PowerShell)
Generate with single-shot prompting using Llama 3.1 8B:
```powershell
python -m src.main --dataset data/processed_dataset/hf/python_structured.csv --method 1_single_shot --model gpt-4 --output data/results/1_single_shot/RunA
```



Generate with XAI prompting using Gemma 3 27B and explicit output file:
```powershell
python -m src.main -d data/processed_dataset/kaggle/vulnerability_fix_other.csv -m google/gemma-3-27b-it -p 2_xai -o data/results/kaggle_xai_outputs.csv
```
Note: The second command will create and use the directory `data/results/kaggle_xai_outputs` as the output root.

Generate with the planning method (two-stage):
```powershell
python -m src.main --dataset data/processed_dataset/hf/python_structured.csv --method 3_planning --model meta-llama/Llama-3.1-8B-Instruct --output data/results/3_planning/RunA
```

### Adding a new method
1. Create a new module in `src/methods/` and register it:
   - Implement `setup(context)`, `run_sample(mapping, model, system_template, user_template)`, `cleanup()`.
   - Call `register_method("<name>", YourRunner)`.
2. Add prompts under `src/prompts/<name>/system.txt` and `user.txt` (plus optional stage-specific files like `system_2.txt`, `user_2.txt`).
3. Run with `--method <name>`. Methods are auto-discovered; no core pipeline edits needed.

## SLURM scripts
Use these job scripts on an HPC cluster with Slurm to run the pipeline with specific Hugging Face models. Ensure `HF_TOKEN` is set in your environment with access to the models.

```bash
sbatch run_gemma_3_27b_it.sh
sbatch run_codellama_34b.sh
sbatch run_qwen3_32b_instruct.sh
sbatch run_qwen3_coder_30b_a3b.sh
sbatch run_gemma_3_1b_it.sh
sbatch run_gpt_4o.sh
sbatch run_gpt_4o_mini.sh
sbatch run_gpt_4.sh
```

Each script installs requirements, configures HF caches in `$SLURM_TMPDIR`, and runs:

- **dataset**: `data/processed_dataset/hf/python_structured.csv`
- **method**: `1_single_shot`
- **model**: as per script name
- **output**: writes a CSV under `data/results/1_single_shot/` and per-instance artifacts under a sibling directory.

For OpenAI models (`gpt-4o`, `gpt-4o-mini`, `gpt-4`), you must also export a valid OpenAI API key before submitting:

```bash
export OPENAI_API_KEY=sk-...
```
