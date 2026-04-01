# TestWright

AI-powered test case generation from functional specifications.

TestWright reads a functional specification (JSON or markdown), analyzes it through an 11-agent LangGraph pipeline, and produces a comprehensive test suite with navigation graphs, post-verification plans, and execution sequences. It also includes 5 baseline prompting strategies for comparison experiments.

## Features

- **Specification-driven** — generate test cases from functional descriptions in JSON or markdown
- **Multi-agent pipeline** — 11 specialized agents (parser, navigator, chunker, summarizer, generator, assembler, verification flag/ideal/matcher, execution planner, finalizer)
- **5 baseline strategies** — Zero-Shot, Single-Shot, Few-Shot-2, Few-Shot-3, Multi-Shot for comparison
- **Multi-model experiment runner** — run across all configured LLMs per dataset
- **Navigation graph** — builds a directed graph of application pages and generates a PNG visualization
- **Post-verification** — flags state-changing tests, generates ideal verification scenarios, matches them to existing test cases via RAG
- **Multiple providers** — works with OpenAI, Google AI Studio (Gemini direct), OpenRouter, and GitHub Models
- **Dual output** — exports to both JSON and Markdown
- **6 dataset configs** — ParaBank, SwagLab, PHPTravels, Mifos, Moodle (student + teacher)

---

## Quick Start

### Practical LLM list

- `gpt-5-mini-2025-08-07`
- `gpt-4.1-mini-2025-04-14`

### 1. Create & activate virtual environment

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` includes all runtime dependencies plus the local `testwright`
package install for this repo, so this is the only install command needed.

Verify:

```bash
testwright --version    # → testwright 2.0.0
```

### 3. Configure API keys

Create a `.env` file in the project root with the keys for the providers you need:

```
OPENAI_API_KEY=sk-...          # for gpt-5-mini-2025-08-07, gpt-4.1-mini-2025-04-14
```

`run_all.py` loads `.env` automatically. You can also pass `--api-key` on the CLI for single-model runs.

---

## Running Experiments

### Full experiment (all models × all datasets)

```bash
# Run both agent + baselines across default matrix (72 runs)
python run_all.py --all

# Agent pipeline only
python run_all.py --agent

# Baselines only
python run_all.py --baselines
```

### Filtered runs

```bash
# Single dataset
python run_all.py --all --dataset Parabank

# Single model
python run_all.py --all --model-filter gpt-5-mini-2025-08-07

# Skip a baseline strategy
python run_all.py --baselines --skip-baseline multi_shot

# Combine filters
python run_all.py --baselines --dataset SwagLab --model-filter gpt-4.1-mini-2025-04-14
```

### Resume / completion workflow

`run_all.py` auto-checks existing outputs and only generates missing/invalid runs.

```bash
# Check what is still missing (no generation)
python run_all.py --all --verify-only

# Generate only missing runs
python run_all.py --all

# Force rerun everything
python run_all.py --all --force
```

### Single-model override (backward compatible)

```bash
# Pass model/provider/key directly — bypasses model matrix
python run_all.py --all \
  --model gpt-5-mini-2025-08-07 \
  --provider openai \
  --api-key "sk-..."
```

### List available datasets and models

```bash
python run_all.py --list
```

### Output structure

```
Output/
  Agent_output/
    <Dataset>/<model>/
      test-cases.json
      test-cases.md
      navigation_graph.png

  Baseline_output/
    <Dataset>/<model>/
      test-cases_<strategy>.json
```

---

## Running Individually

### Agent pipeline (single dataset)

```bash
testwright --generate \
  --input Datasets/Parabank_Demo_Banking/Parabank.json \
  --api-key "sk-..." \
  --provider openai \
  --model gpt-5-mini-2025-08-07 \
  --output Output/Agent_output/Parabank/gpt-5-mini-2025-08-07/
```

### Baseline generator (single run)

```bash
python -m testwright.baselines.baseline_generator \
  --input Datasets/Parabank_Demo_Banking/Parabank.json \
  --shots 0 \
  --api-key "sk-..." \
  --model gpt-5-mini-2025-08-07 \
  --provider openai \
  --temperature 0.3 \
  --output Output/Baseline_output/Parabank/gpt-5-mini-2025-08-07/test-cases_zero_shot.json
```

`--shots` values: `0` (zero-shot), `1` (single-shot), `2` (few-shot-2), `3` (few-shot-3), `5` (multi-shot)

### Export JSON to Markdown

```bash
testwright export-md \
  --input Output/Agent_output/Parabank/gpt-5-mini-2025-08-07/test-cases.json \
  --output Output/Agent_output/Parabank/gpt-5-mini-2025-08-07/test-cases.md
```

### Python API

```python
from testwright import TestCaseGenerator

generator = TestCaseGenerator(
    api_key="sk-...",
  model="gpt-5-mini-2025-08-07",
    provider="openai",
)

output = generator.generate(
    "Datasets/Parabank_Demo_Banking/Parabank.json",
  output_dir="Output/Agent_output/Parabank/gpt-5-mini-2025-08-07/"
)
print(f"Generated {output.summary['total_tests']} test cases")
```

```python
from testwright.baselines.baseline_generator import BaselineGenerator

gen = BaselineGenerator(
    api_key="sk-...",
    model="gpt-5-mini-2025-08-07",
    provider="openai",
    num_shots=0,         # zero-shot
    temperature=0.3,
    seed=1,
)
result = gen.generate(
    "Datasets/Parabank_Demo_Banking/Parabank.json",
  output_path="Output/Baseline_output/Parabank/gpt-5-mini-2025-08-07/test-cases_zero_shot.json"
)
print(f"Generated {result['summary']['total_tests']} test cases")
```

---

## Experiment Protocol

The experiment matrix follows the paper's protocol:

| Dimension | Values |
|-----------|--------|
| **Datasets** | Parabank, SwagLab, PHPTravels, Mifos, Moodle_Student, Moodle_Teacher |
| **Models** | gpt-5-mini-2025-08-07, gpt-4.1-mini-2025-04-14 |
| **Agent** | 11-node multi-agent pipeline |
| **Baselines** | Zero-Shot (0), Single-Shot (1), Few-Shot-2 (2), Few-Shot-3 (3), Multi-Shot (5) |
| **Temperature** | 0.3 (baselines) |

**Total runs:** 6 datasets × 2 models × (1 agent + 5 baselines) = **72 runs**

### Model → Provider mapping

| Model | `--provider` | `--model` value | API key env var |
|-------|-------------|-----------------|-----------------|
| GPT-5-mini-2025-08-07 | `openai` | `gpt-5-mini-2025-08-07` | `OPENAI_API_KEY` |
| GPT-4.1-mini-2025-04-14 | `openai` | `gpt-4.1-mini-2025-04-14` | `OPENAI_API_KEY` |

---

## Architecture

```
Input (functional spec JSON/MD)
  │
  v
[1] Parser ────> Structured modules & workflows
  │
  v
[2] Navigation ─> Directed page graph (nodes + edges)
  │
  v
[3] Chunker ───> Workflow-based chunks per module
  │
  v
[4] Summary ───> Module summaries (verify/action states)
  │
  v
[5] Generator ─> Raw test cases (positive, negative, edge)
  │
  v
[6] Assembler ─> Deduplicated, ID'd, nav-linked test suite
  │
  v
[7] Flag ──────> Flags state-changing tests
  │
  v
[8] Ideal ─────> Ideal verification scenarios per flag
  │
  v
[9] Matcher ───> RAG-matched verification test cases
  │
  v
[10] Planner ──> PRE → ACTION → POST execution plans
  │
  v
[11] Finalize ─> Summary, graph image, JSON export
```

### Agent Responsibilities

| Agent | File | Role |
|-------|------|------|
| Parser | `agents/parser.py` | Parse functional spec into structured modules |
| Navigation | `agents/navigation.py` | Build page graph, generate PNG |
| Chunker | `agents/chunker.py` | Split modules into workflow chunks |
| Summary | `agents/summary.py` | Summarize modules (verify/action states) |
| Test Generator | `agents/test_generator.py` | Generate positive, negative, edge-case tests |
| Assembler | `agents/assembler.py` | Deduplicate, assign IDs, link to nav graph |
| Verify Flag | `agents/verify_flag.py` | Flag tests that modify persistent state |
| Verify Ideal | `agents/verify_ideal.py` | Design ideal verification scenarios |
| Verify Matcher | `agents/verify_matcher.py` | Match ideal verifications to tests via RAG |
| Execution Planner | `agents/execution_planner.py` | Compile before/after execution sequences |
| RAG Indexer | `agents/rag_indexer.py` | Embedding-based test case search |

---

## Project Structure

```
testwright/
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── run_all.py                  # Full experiment orchestrator
├── README.md
│
├── Datasets/
│   ├── Parabank_Demo_Banking/
│   │   ├── Parabank.json       # Functional description
│   │   └── Parabank.md
│   ├── SwagLab_Ecommerce_System/
│   ├── PHPTravels_Travel_Booking/
│   ├── Mifos_Banking_System/
│   ├── Moodle_Learning_Management_System/
│   │   ├── moodle_student.json
│   │   ├── moodle_teacher.json
│   │   └── ...
│   ├── Ground_Truth_Reference_Tests/   # Manual reference test cases
│   ├── Agent_output/                  # Input dataset resources
│   └── Baseline_output/               # Input dataset resources
├── Output/
│   ├── Agent_output/                  # Generated by agent
│   └── Baseline_output/               # Generated by baselines
│
├── src/testwright/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py                  # CLI entry point
│   │
│   ├── core/
│   │   ├── generator.py        # TestCaseGenerator orchestrator
│   │   ├── state.py            # LangGraph PipelineState schema
│   │   ├── graph.py            # StateGraph builder (11 nodes)
│   │   └── nodes.py            # Node functions for each agent
│   │
│   ├── agents/                 # All 11 agents + RAG indexer
│   │   ├── base.py             # BaseAgent (LLM calls, debug, retry)
│   │   ├── parser.py
│   │   ├── navigation.py
│   │   ├── chunker.py
│   │   ├── summary.py
│   │   ├── test_generator.py
│   │   ├── assembler.py
│   │   ├── verify_flag.py
│   │   ├── verify_ideal.py
│   │   ├── verify_matcher.py
│   │   ├── execution_planner.py
│   │   └── rag_indexer.py
│   │
│   ├── baselines/
│   │   ├── baseline_generator.py   # Monolithic baseline generator
│   │   └── prompts/
│   │       ├── zero_shot.txt       # Zero-shot system prompt
│   │       ├── few_shot.txt        # Few-shot prompt with {examples}
│   │       └── examples.json       # 5 example test cases
│   │
│   ├── models/
│   │   ├── schemas.py          # Dataclasses (TestCase, NavGraph, etc.)
│   │   └── enums.py            # TestType, Priority, VerificationStatus
│   │
│   └── exporters/
│       ├── json_exporter.py
│       └── markdown_exporter.py
│
└── tests/
```

## Input Format

### Dataset JSON (recommended)

```json
{
  "Website URL": "https://example.com",
  "Credentials": {
    "Username": "testuser",
    "Password": "Test@1234"
  },
  "Navigation": "Description of site navigation structure...",
  "Functional Overview": {
    "1. Login": "Detailed description of the login page...",
    "2. Dashboard": "Detailed description of the dashboard..."
  }
}
```

### Markdown directory

A directory containing:

- `functional_specification.md` (required) — `## H2` headings for each module
- `navigation.md` (optional) — navigation structure description
- `mock_data.md` (optional) — test credentials and sample data

## Datasets

| Dataset | Directory | Modules | Description |
|---------|-----------|---------|-------------|
| **ParaBank** | `Parabank_Demo_Banking/` | 10 + Logout | Demo banking (login, accounts, transfers, loans) |
| **SwagLab** | `SwagLab_Ecommerce_System/` | 5 + Logout | E-commerce (login, inventory, cart, checkout) |
| **PHPTravels** | `PHPTravels_Travel_Booking/` | 20 + Logout | Travel booking (hotels, flights, tours, cars, visa) |
| **Mifos** | `Mifos_Banking_System/` | 30 + Logout | Core banking/microfinance on Apache Fineract |
| **Moodle** | `Moodle_Learning_Management_System/` | 9-12 + Logout | LMS with separate student and teacher specs |

## Output Format

### JSON (`test-cases.json`)

Both agent and baselines produce the same JSON structure:

```json
{
  "project_name": "Parabank",
  "base_url": "https://parabank.parasoft.com",
  "generated_at": "2025-01-01T12:00:00",
  "test_cases": [
    {
      "id": "LOGIN-001",
      "title": "Successful login with valid credentials",
      "module_id": 1,
      "module_title": "Login",
      "workflow": "User Authentication",
      "test_type": "positive",
      "priority": "High",
      "preconditions": "Registered user exists...",
      "steps": ["Navigate to login page", "Enter username..."],
      "expected_result": "User is redirected to Accounts Overview"
    }
  ],
  "summary": {
    "total_tests": 42,
    "by_type": {"positive": 20, "negative": 15, "edge_case": 7},
    "by_priority": {"High": 18, "Medium": 16, "Low": 8},
    "by_module": {"Login": 8, "Accounts Overview": 6}
  }
}
```

### Markdown (`test-cases.md`)

Human-readable report with summary tables, test cases grouped by module and type, and post-verification details.

### Navigation Graph (`navigation_graph.png`)

Visual representation of application page flow (agent output only).

## License

MIT
