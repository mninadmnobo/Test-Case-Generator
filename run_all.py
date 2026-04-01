import argparse
import json
import os
import sys
import time
import re
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# .env loader (no external dependency)
# ---------------------------------------------------------------------------

def _load_dotenv(path: str = ".env"):
    """Load key=value pairs from a .env file into os.environ."""
    env_path = Path(path)
    if not env_path.exists():
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            # Strip surrounding quotes
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            if key:
                # Prefer explicit .env values so empty inherited vars do not mask real keys.
                os.environ[key] = value

# Load .env before anything else
_load_dotenv()

# ---------------------------------------------------------------------------
# Dataset registry
# ---------------------------------------------------------------------------

DATASETS = [
    {
        "name":     "Parabank",
        "input":    "dataset/Parabank.md",
    },
    {
        "name":     "SwagLab",
        "input":    "dataset/SwagLab.md",
    },
    {
        "name":     "PHPTravels",
        "input":    "dataset/PHPTravels.md",
    },
    {
        "name":     "Mifos",
        "input":    "dataset/Mifos.md",
    },
    {
        "name":     "Moodle_Student",
        "input":    "dataset/MoodleStudent.md",
    },
    {
        "name":     "Moodle_Teacher",
        "input":    "dataset/MoodleTeacher.md",
    },
]

# ---------------------------------------------------------------------------
# Model registry — practical run matrix
# ---------------------------------------------------------------------------

MODEL_CONFIGS = [
    {
        "name":     "gpt-5-mini-2025-08-07",
        "model":    "gpt-5-mini-2025-08-07",
        "provider": "openai",
        "env_key":  "OPENAI_API_KEY",
    },
    {
        "name":     "gpt-4.1-mini-2025-04-14",
        "model":    "gpt-4.1-mini-2025-04-14",
        "provider": "openai",
        "env_key":  "OPENAI_API_KEY",
    },
]

BASELINE_CONFIGS = [
    (0, "zero_shot",    "Zero-Shot"),
    (1, "single_shot",  "Single-Shot"),
    (2, "few_shot_2",   "Few-Shot-2"),
    (3, "few_shot_3",   "Few-Shot-3"),
    (5, "multi_shot",   "Multi-Shot (5 examples)"),
]

BASELINE_TEMPERATURE = 0.3
OUTPUT_ROOT = "Output"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def header(text: str):
    print(f"\n{'='*80}")
    print(f"  {text}")
    print(f"{'='*80}")


def _resolve_api_key(model_cfg: dict, cli_api_key: str | None) -> str | None:
    """Return an API key: CLI override > env variable."""
    # Local Ollama runs do not require API keys.
    if model_cfg.get("provider") == "ollama":
        return cli_api_key or "ollama"
    if cli_api_key:
        return cli_api_key
    env_key = model_cfg.get("env_key")
    if not env_key:
        return None
    return os.environ.get(env_key)


def _env_key_for_provider(provider: str) -> Optional[str]:
    mapping = {
        "openai": "OPENAI_API_KEY",
        "github": "GITHUB_TOKEN",
        "openrouter": "OPENROUTER_API_KEY",
        "google": "GOOGLE_API_KEY",
        "ollama": None,
    }
    return mapping.get(provider)


def _load_test_count(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        test_cases = data.get("test_cases", [])
        return len(test_cases)
    except Exception:
        return 0


def _normalize_module_name(name: str) -> str:
    cleaned = name.strip().lower()
    while cleaned and cleaned[0].isdigit():
        cleaned = cleaned[1:]
    cleaned = cleaned.lstrip(". ):-")
    return " ".join(cleaned.replace("&", " and ").split())


def _extract_expected_modules_from_dataset(dataset_path: str) -> list[str]:
    path = Path(dataset_path)
    if path.suffix.lower() == ".md":
        return []

    try:
        with open(dataset_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    if isinstance(data.get("modules"), list):
        modules = []
        for module in data["modules"]:
            if not isinstance(module, dict):
                continue
            value = module.get("title") or module.get("module_title") or module.get("name")
            if isinstance(value, str) and value.strip():
                modules.append(value.strip())
        return modules

    for key in ("Functional Overview", "Functional Modules", "Functional Description"):
        value = data.get(key)
        if isinstance(value, dict):
            return [str(module).strip() for module in value.keys() if str(module).strip()]

    return []


def _load_functional_description(dataset_path: str) -> dict:
    path = Path(dataset_path)
    if path.suffix.lower() == ".md":
        modules = []
        current_module: dict | None = None
        module_id = 0
        in_functional_section = False
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()

            if stripped in {"## Functional Description"}:
                in_functional_section = True
                continue

            if in_functional_section and stripped.startswith("## "):
                break

            if not in_functional_section:
                continue

            if stripped.startswith("### "):
                if current_module:
                    modules.append(current_module)
                module_id += 1
                current_module = {
                    "id": module_id,
                    "title": re.sub(r"^\d+\.\s*", "", stripped[4:]).strip(),
                    "description": "",
                }
            elif current_module:
                current_module["description"] += line + "\n"
        if current_module:
            modules.append(current_module)

        return {
            "project_name": path.stem,
            "website_url": "",
            "navigation_overview": "",
            "modules": modules,
        }

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _is_complete_test_suite_json(path: str, expected_modules: list[str] | None = None) -> tuple[bool, int]:
    """Validate a generated test-suite JSON file is structurally complete."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return False, 0

    if not isinstance(data, dict):
        return False, 0

    required = ["project_name", "base_url", "generated_at", "test_cases", "summary"]
    if any(key not in data for key in required):
        return False, 0

    test_cases = data.get("test_cases")
    if not isinstance(test_cases, list) or len(test_cases) == 0:
        return False, 0

    summary = data.get("summary")
    if not isinstance(summary, dict):
        return False, 0

    total_from_summary = summary.get("total_tests")
    if total_from_summary is not None and total_from_summary != len(test_cases):
        return False, 0

    if expected_modules:
        actual_modules = {
            _normalize_module_name(test_case.get("module_title", ""))
            for test_case in test_cases
            if isinstance(test_case, dict)
        }
        for module in expected_modules:
            normalized = _normalize_module_name(module)
            if normalized and normalized not in actual_modules:
                return False, 0

    return True, len(test_cases)


def _is_valid_agent_output(out_dir: str, dataset_json_path: str) -> tuple[bool, int]:
    json_path = os.path.join(out_dir, "test-cases.json")
    md_path = os.path.join(out_dir, "test-cases.md")
    graph_path = os.path.join(out_dir, "navigation_graph.png")
    if not (os.path.exists(json_path) and os.path.exists(md_path) and os.path.exists(graph_path)):
        return False, 0
    if os.path.getsize(md_path) == 0 or os.path.getsize(graph_path) == 0:
        return False, 0
    expected_modules = _extract_expected_modules_from_dataset(dataset_json_path)
    return _is_complete_test_suite_json(json_path, expected_modules=expected_modules)


def _is_valid_baseline_output(output_path: str) -> tuple[bool, int]:
    if not os.path.exists(output_path):
        return False, 0
    return _is_complete_test_suite_json(output_path)


def run_agent(dataset: dict, api_key: str, model_cfg: dict):
    """Run the 11-agent TestWright pipeline for one dataset/model."""
    from testwright.core.generator import TestCaseGenerator

    out_dir = os.path.join(
        OUTPUT_ROOT, "Agent_output", dataset["name"],
        model_cfg["name"],
    )

    header(f"AGENT — {dataset['name']} / {model_cfg['name']}")
    os.makedirs(out_dir, exist_ok=True)

    try:
        generator = TestCaseGenerator(
            api_key=api_key,
            model=model_cfg["model"],
            provider=model_cfg["provider"],
        )
        functional_desc = _load_functional_description(dataset["input"])
        output = generator.generate(functional_desc, output_dir=out_dir)

        # Also export markdown
        from testwright.exporters.markdown_exporter import load_test_cases, generate_markdown
        md_path = os.path.join(out_dir, "test-cases.md")
        data = load_test_cases(os.path.join(out_dir, "test-cases.json"))
        markdown = generate_markdown(data)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        total = output.summary.get("total_tests", 0)
        print(f"\n  OK {total} test cases -> {out_dir}/")
        return True, total
    except Exception as e:
        # Do not delete output folders on failure; keep any previously generated artifacts.
        print(f"\n  FAILED: {e}")
        return False, 0


def run_baseline(dataset: dict, shots: int, strategy: str, label: str,
                 api_key: str, model_cfg: dict):
    """Run one baseline strategy for one dataset/model."""
    from testwright.baselines.baseline_generator import BaselineGenerator

    out_dir = os.path.join(
        OUTPUT_ROOT, "Baseline_output", dataset["name"],
        model_cfg["name"],
    )
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, f"test-cases_{strategy}.json")

    print(f"\n  [{label}] {model_cfg['name']} -> {output_path}")
    try:
        gen = BaselineGenerator(
            api_key=api_key,
            model=model_cfg["model"],
            provider=model_cfg["provider"],
            num_shots=shots,
            temperature=BASELINE_TEMPERATURE,
        )
        functional_desc = _load_functional_description(dataset["input"])
        result = gen.generate(functional_desc, output_path=output_path)
        total = result.get("summary", {}).get("total_tests", 0)
        print(f"     OK  {total} test cases")
        return True, total
    except Exception as e:
        print(f"     FAILED: {e}")
        return False, 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run TestWright agent + baselines across all datasets and models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    # --- Mode selection ---
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--agent",     action="store_true", help="Run agent pipeline only")
    mode.add_argument("--baselines", action="store_true", help="Run baselines only")
    mode.add_argument("--all",       action="store_true", help="Run both agent + baselines (default)")

    # --- Filters ---
    parser.add_argument("--dataset", metavar="NAME",
                        help="Run a single dataset (e.g. Parabank, SwagLab)")
    parser.add_argument("--model-filter", metavar="NAME",
                        help="Run a single model by name (e.g. gpt-5-mini-2025-08-07, gpt-4.1-mini-2025-04-14)")
    parser.add_argument("--skip-baseline", metavar="FOLDER", action="append", default=[],
                        help="Skip a specific baseline (e.g. multi_shot)")
    parser.add_argument("--force", action="store_true",
                        help="Re-run all selected runs even if valid output files already exist")
    parser.add_argument("--verify-only", action="store_true",
                        help="Only check completion status; do not generate missing runs")

    # --- Single-model override (backward compat) ---
    parser.add_argument("--api-key", help="API key (overrides .env for all models)")
    parser.add_argument("--model", help="Model name (single-model override, skips model matrix)")
    parser.add_argument("--provider", choices=["openai", "github", "openrouter", "google", "ollama"],
                        help="Provider override (single-model or full matrix)")

    parser.add_argument("--list", action="store_true",
                        help="List available datasets and models, then exit")

    args = parser.parse_args()

    # --list
    if args.list:
        print("Datasets:")
        for ds in DATASETS:
            print(f"  - {ds['name']:20s}  {ds['input']}")
        print("\nModels:")
        for mc in MODEL_CONFIGS:
            print(f"  - {mc['name']:20s}  provider={mc['provider']:12s}  env={mc['env_key']}")
        print(f"\nBaseline strategies: {', '.join(f[1] for f in BASELINE_CONFIGS)}")
        return 0

    # Default: run both
    run_ag = args.agent or args.all or (not args.agent and not args.baselines)
    run_ba = args.baselines or args.all or (not args.agent and not args.baselines)

    # --- Resolve model list ---
    if args.model:
        # Single-model override (backward compat)
        provider = args.provider or "openai"
        models = [{
            "name":     args.model,
            "model":    args.model,
            "provider": provider,
            "env_key":  _env_key_for_provider(provider),
        }]
    else:
        models = MODEL_CONFIGS.copy()
        if args.provider:
            env_key = _env_key_for_provider(args.provider)
            models = [
                {
                    **m,
                    "provider": args.provider,
                    "env_key": env_key,
                }
                for m in models
            ]
        if args.model_filter:
            key = args.model_filter.lower()
            models = [m for m in models if m["name"].lower() == key]
            if not models:
                names = ", ".join(m["name"] for m in MODEL_CONFIGS)
                print(f"Error: model '{args.model_filter}' not found. Available: {names}")
                return 1

    # --- Filter datasets ---
    datasets = DATASETS
    if args.dataset:
        key = args.dataset.lower()
        datasets = [d for d in DATASETS if d["name"].lower() == key]
        if not datasets:
            names = ", ".join(d["name"] for d in DATASETS)
            print(f"Error: dataset '{args.dataset}' not found. Available: {names}")
            return 1

    # --- Check API keys ---
    if not args.verify_only:
        missing_keys = set()
        for mc in models:
            resolved = _resolve_api_key(mc, args.api_key)
            if not resolved and mc.get("env_key"):
                missing_keys.add(mc["env_key"])
        if missing_keys:
            print("Error: Missing API keys. Set them in .env or pass --api-key:")
            for k in sorted(missing_keys):
                print(f"  - {k}")
            print("\nAdd the missing keys to your .env file or pass --api-key for a single-model run.")
            return 1

    # --- Print plan ---
    start_time = time.time()
    all_results = []

    total_agent_runs = len(datasets) * len(models) if run_ag else 0
    total_baseline_runs = (
        len(datasets) * len(models)
        * (len(BASELINE_CONFIGS) - len(args.skip_baseline))
    ) if run_ba else 0

    print(f"\nTestWright — Full Experiment Runner")
    print(f"  Datasets:   {len(datasets)} ({', '.join(d['name'] for d in datasets)})")
    print(f"  Models:     {len(models)} ({', '.join(m['name'] for m in models)})")
    print(f"  Agent runs: {total_agent_runs}")
    print(f"  Baseline:   {total_baseline_runs} "
          f"({len(BASELINE_CONFIGS)} strategies × {len(models)} models)")
    print(f"  Total runs: {total_agent_runs + total_baseline_runs}")

    # ------------------------------------------------------------------
    # Agent runs
    # ------------------------------------------------------------------
    if run_ag:
        header("AGENT RUNS")
        for ds in datasets:
            for mc in models:
                out_dir = os.path.join(OUTPUT_ROOT, "Agent_output", ds["name"], mc["name"])
                if not args.force:
                    is_valid, existing_count = _is_valid_agent_output(out_dir, ds["input"])
                    if is_valid:
                        print(f"\n  [SKIP] {ds['name']} / {mc['name']} already complete ({existing_count} tests)")
                        all_results.append({
                            "dataset": ds["name"],
                            "mode": "agent",
                            "model": mc["name"],
                            "success": True,
                            "tests": existing_count,
                            "status": "existing",
                        })
                        continue
                    if args.verify_only:
                        print(f"\n  [MISSING] {ds['name']} / {mc['name']} agent output")
                        all_results.append({
                            "dataset": ds["name"],
                            "mode": "agent",
                            "model": mc["name"],
                            "success": False,
                            "tests": 0,
                            "status": "missing",
                        })
                        continue

                api_key = _resolve_api_key(mc, args.api_key)
                success, count = run_agent(ds, api_key, mc)
                all_results.append({
                    "dataset": ds["name"],
                    "mode": "agent",
                    "model": mc["name"],
                    "success": success,
                    "tests": count,
                    "status": "generated" if success else "failed",
                })
                if success:
                    time.sleep(1)

    # ------------------------------------------------------------------
    # Baseline runs
    # ------------------------------------------------------------------
    if run_ba:
        for ds in datasets:
            for mc in models:
                api_key = _resolve_api_key(mc, args.api_key)
                header(f"BASELINES — {ds['name']} / {mc['name']}")
                for shots, strategy, label in BASELINE_CONFIGS:
                    if strategy in args.skip_baseline:
                        print(f"\n  [SKIP] {label}")
                        continue

                    output_path = os.path.join(
                        OUTPUT_ROOT,
                        "Baseline_output",
                        ds["name"],
                        mc["name"],
                        f"test-cases_{strategy}.json",
                    )
                    if not args.force:
                        is_valid, existing_count = _is_valid_baseline_output(output_path)
                        if is_valid:
                            print(f"\n  [SKIP] {label} already complete ({existing_count} tests)")
                            all_results.append({
                                "dataset": ds["name"],
                                "mode": f"baseline/{strategy}",
                                "model": mc["name"],
                                "success": True,
                                "tests": existing_count,
                                "status": "existing",
                            })
                            continue
                        if args.verify_only:
                            print(f"\n  [MISSING] {label} output")
                            all_results.append({
                                "dataset": ds["name"],
                                "mode": f"baseline/{strategy}",
                                "model": mc["name"],
                                "success": False,
                                "tests": 0,
                                "status": "missing",
                            })
                            continue

                    success, count = run_baseline(
                        ds, shots, strategy, label,
                        api_key, mc,
                    )
                    all_results.append({
                        "dataset": ds["name"],
                        "mode": f"baseline/{strategy}",
                        "model": mc["name"],
                        "success": success,
                        "tests": count,
                        "status": "generated" if success else "failed",
                    })
                    if success:
                        time.sleep(1)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    elapsed = time.time() - start_time
    header("SUMMARY")
    print(f"  Total time: {elapsed/60:.1f} min\n")

    succeeded = [r for r in all_results if r["success"]]
    failed    = [r for r in all_results if not r["success"]]

    print(f"  {'DATASET':<20} {'MODE':<25} {'MODEL':<20} {'TESTS':>6}  STATUS")
    print(f"  {'-'*20} {'-'*25} {'-'*20} {'-'*4} {'-'*6}  {'-'*7}")
    for r in all_results:
        status = "OK" if r["success"] else "FAILED"
        print(f"  {r['dataset']:<20} {r['mode']:<25} {r['model']:<20} {r['tests']:>6}  {status}")

    print(f"\n  {len(succeeded)}/{len(all_results)} runs completed successfully.")
    if failed:
        print(f"  {len(failed)} failed runs:")
        for r in failed:
            print(f"    - {r['dataset']} / {r['mode']} / {r['model']}")

    # Save results manifest
    os.makedirs(OUTPUT_ROOT, exist_ok=True)
    manifest_path = os.path.join(OUTPUT_ROOT, "run_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "models": [m["name"] for m in models],
            "elapsed_seconds": round(elapsed, 1),
            "results": all_results,
        }, f, indent=2)
    print(f"\n  Manifest saved -> {manifest_path}")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
