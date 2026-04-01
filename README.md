# TestWright

AI-powered test case generation from functional specifications.

TestWright reads a functional specification (Markdown or JSON), runs a LangGraph multi-agent pipeline, and generates test suites in JSON and Markdown. This repository also includes baseline prompting strategies and a full experiment runner for multi-dataset, multi-model evaluation.

## What this repository contains

- Core package: `testwright/`
- Experiment runner: `run_all.py`
- Dataset specs and ground truth: `dataset/`
- Generated outputs: `Output/`

## Features

- Specification-driven generation from Markdown or JSON inputs
- Multi-agent pipeline with optional modes:
  - `full`: generation + verification + execution planning
  - `basic`: generation only (stops after assembler)
- Baseline generator with 5 prompting strategies:
  - zero-shot, single-shot, few-shot-2, few-shot-3, multi-shot
- Batch experiment orchestration across datasets and models
- JSON + Markdown outputs
- Navigation graph image for agent runs

## Requirements

- Python 3.10+
- API key for your provider (except local Ollama baseline runs)

## Install

```bash
# From repository root
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

Check install:

```bash
testwright --version
```

## Configuration

Create `.env` in the repository root when using `run_all.py`:

```env
OPENAI_API_KEY=your_openai_key
GITHUB_TOKEN=your_github_models_token
OPENROUTER_API_KEY=your_openrouter_key
GOOGLE_API_KEY=your_google_key
```

Notes:

- `run_all.py` loads `.env` automatically.
- You can override with `--api-key`.
- Current model matrix in `run_all.py` uses OpenAI models by default.

## Quick start

### 1) Run full experiment matrix

```bash
python run_all.py --all
```

Equivalent default:

```bash
python run_all.py
```

### 2) Run only agent or only baselines

```bash
python run_all.py --agent
python run_all.py --baselines
```

### 3) Filter runs

```bash
# Single dataset
python run_all.py --all --dataset Parabank

# Single model from configured matrix
python run_all.py --all --model-filter gpt-5-mini-2025-08-07

# Skip one baseline strategy
python run_all.py --baselines --skip-baseline multi_shot
```

### 4) Resume/verify workflow

```bash
# Verify completion only (no generation)
python run_all.py --all --verify-only

# Force rerun
python run_all.py --all --force
```

### 5) List available datasets/models

```bash
python run_all.py --list
```

## Single-run CLI usage

The package CLI is installed as `testwright` and supports generation + markdown export.

### Generate test cases

```bash
testwright --generate --input dataset/Parabank.md --api-key "<KEY>" --provider openai --model gpt-4o
```

Optional flags:

- `--output` / `-o`: output directory
- `--debug`: enable debug logging
- `--debug-file`: debug log file path (default: `debug_log.txt`)
- `--mode`: `full` (default) or `basic`
- `--spec` and `--nav`: manual markdown file overrides

Provider choices for `testwright` CLI:

- `openai`
- `github`
- `openrouter`

### Export JSON to Markdown

```bash
testwright export-md --input Output/Agent_output/Parabank/gpt-5-mini-2025-08-07/test-cases.json
```

If `--output` is omitted, output defaults to the same path with `.md` extension.

### Run as module

```bash
python -m testwright --generate --input dataset/Parabank.md --api-key "<KEY>"
```

## Baseline generator (single run)

You can run baselines directly:

```bash
python -m testwright.baselines.baseline_generator \
  --input dataset/Parabank.md \
  --shots 0 \
  --api-key "<KEY>" \
  --model gpt-5-mini-2025-08-07 \
  --provider openai \
  --temperature 0.3 \
  --output Output/Baseline_output/Parabank/gpt-5-mini-2025-08-07/test-cases_zero_shot.json
```

`--shots` values:

- `0` zero-shot
- `1` single-shot
- `2` few-shot-2
- `3` few-shot-3
- `5` multi-shot

Provider choices for baseline CLI:

- `openai`
- `github`
- `openrouter`
- `google`
- `ollama`

## Input formats

### A) Markdown file (used by this repo datasets)

`testwright --generate --input dataset/Parabank.md ...`

For best parsing, include a section:

- `## Functional Description`
- Module headings as `### ...`

### B) Directory input

`testwright --generate --input <directory> ...`

Directory conventions:

- `functional_specification.md` (required unless exactly one `.md` exists)
- `navigation.md` (optional)
- `mock_data.md` (optional)

### C) JSON input

`testwright --generate --input <file.json> ...`

Expected fields are flexible; common keys include website URL, credentials, navigation overview, and functional modules.

## Output structure

### Experiment runner (`run_all.py`)

```text
Output/
  Agent_output/
    <Dataset>/<model>/
      test-cases.json
      test-cases.md
      navigation_graph.png
  Baseline_output/
    <Dataset>/<model>/
      test-cases_zero_shot.json
      test-cases_single_shot.json
      test-cases_few_shot_2.json
      test-cases_few_shot_3.json
      test-cases_multi_shot.json
  run_manifest.json
```

### Single `testwright --generate` command

If `--output` is not provided, default output is generated as:

```text
<base_dir>/<project_name>-<model_slug>/
```

`base_dir` is derived from the input path.

## Current experiment defaults in this repo

From `run_all.py`:

- Datasets:
  - `Parabank`
  - `SwagLab`
  - `PHPTravels`
  - `Mifos`
  - `Moodle_Student`
  - `Moodle_Teacher`
- Models:
  - `gpt-5-mini-2025-08-07` (`openai`)
  - `gpt-4.1-mini-2025-04-14` (`openai`)
- Baseline strategies:
  - `zero_shot`, `single_shot`, `few_shot_2`, `few_shot_3`, `multi_shot`

## Project layout (actual)

```text
.
├── pyproject.toml
├── requirements.txt
├── run_all.py
├── README.md
├── dataset/
├── output/
├── Output/
└── testwright/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── agents/
    ├── baselines/
    ├── core/
    ├── exporters/
    └── models/
```

Note: both `output/` and `Output/` may exist; `run_all.py` writes to `Output/`.

## Python API

```python
from testwright import TestCaseGenerator

generator = TestCaseGenerator(
    api_key="<KEY>",
    model="gpt-5-mini-2025-08-07",
    provider="openai",
    mode="full",  # or "basic"
)

functional_desc = {
    "project_name": "Demo App",
    "website_url": "https://example.com",
    "navigation_overview": "...",
    "modules": [
        {"id": 1, "title": "Login", "description": "..."}
    ],
}

result = generator.generate(functional_desc, output_dir="Output/Agent_output/Demo/gpt-5-mini")
print(result.summary.get("total_tests", 0))
```

## License

MIT
