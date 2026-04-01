#!/usr/bin/env python3
"""
Baseline Test Generator

Supports:
- Zero-shot (0 examples)
- Single-shot (1 example)
- Few-shot-2 (2 examples)
- Few-shot-3 (3 examples)
- Multi-shot (5 examples)

Outputs in the same JSON format as the TestWright multi-agent pipeline
so results are directly comparable without conversion.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List
import httpx


JSON_RETRY_INSTRUCTION = (
    "\n\nIMPORTANT: Your previous output was invalid JSON. "
    "Return ONLY valid JSON with double-quoted keys/strings, no markdown fences, "
    "no prose, and no trailing commas."
)

MISSING_MODULE_RETRY_TEMPLATE = (
    "\n\nIMPORTANT: Your previous output missed required modules. "
    "Regenerate the ENTIRE suite from scratch and ensure every listed module appears in test_cases. "
    "Do not return a patch or partial addendum. Return one complete JSON object only. "
    "Missing modules from the previous attempt:\n{missing_modules}"
)


class BaselineGenerator:
    """Baseline test case generator using monolithic prompting.

    Produces output matching TestWright's ``test-cases.json`` format:
    ``{ project_name, base_url, generated_at, test_cases[], summary }``
    """

    APPROACH_NAMES = {
        0: "zero-shot",
        1: "single-shot",
        2: "few-shot-2",
        3: "few-shot-3",
        5: "multi-shot",
    }

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        provider: str = "openai",
        num_shots: int = 0,
        temperature: float = 0.3,
        seed: int | None = None,
    ):
        self.api_key = api_key
        self.model = model
        self.provider = provider.lower()
        self.num_shots = num_shots
        self.temperature = temperature
        self.seed = seed
        self.total_tokens = 0
        self.generation_time = 0.0

    # ------------------------------------------------------------------
    # API helpers
    # ------------------------------------------------------------------

    def _get_api_endpoint(self) -> str:
        endpoints = {
            "openai": "https://api.openai.com/v1/chat/completions",
            "github": "https://models.inference.ai.azure.com/chat/completions",
            "openrouter": "https://openrouter.ai/api/v1/chat/completions",
            "google": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
            "ollama": "http://localhost:11434/v1/chat/completions",
        }
        if self.provider not in endpoints:
            raise ValueError(f"Unknown provider: {self.provider}")
        return endpoints[self.provider]

    def _use_openai_responses_api(self) -> bool:
        """GPT-5 model family is served via OpenAI Responses API."""
        return self.provider == "openai" and self.model.startswith("gpt-5")

    @staticmethod
    def _extract_responses_output_text(result: Dict[str, Any]) -> str:
        """Extract plain text from a Responses API payload."""
        if isinstance(result.get("output_text"), str) and result["output_text"].strip():
            return result["output_text"]

        output = result.get("output", [])
        texts: list[str] = []
        for item in output:
            if item.get("type") != "message":
                continue
            for block in item.get("content", []):
                if block.get("type") == "output_text" and isinstance(block.get("text"), str):
                    texts.append(block["text"])

        return "\n".join(texts).strip()

    def _get_headers(self) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
        }
        if self.provider != "ollama":
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    @staticmethod
    def _strip_code_fences(text: str) -> str:
        content = text.strip()
        if content.startswith("```json"):
            content = content[7:]
        elif content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        return content.strip()

    @staticmethod
    def _extract_json_object_text(text: str) -> str:
        """Best-effort extraction of the outermost JSON object text."""
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return text[start:end + 1].strip()
        return text.strip()

    @staticmethod
    def _sanitize_control_chars(text: str) -> str:
        """Escape bare control characters inside JSON strings."""
        result: list[str] = []
        in_string = False
        escaped = False
        for ch in text:
            if escaped:
                result.append(ch)
                escaped = False
            elif ch == "\\" and in_string:
                result.append(ch)
                escaped = True
            elif ch == '"':
                result.append(ch)
                in_string = not in_string
            elif in_string and ch == "\n":
                result.append("\\n")
            elif in_string and ch == "\r":
                result.append("\\r")
            elif in_string and ch == "\t":
                result.append("\\t")
            elif in_string and ord(ch) < 0x20:
                result.append(f"\\u{ord(ch):04x}")
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def _parse_json_response(content: str) -> Dict[str, Any]:
        """Parse model content as JSON with cleanup/sanitize/extract fallbacks."""
        cleaned = BaselineGenerator._strip_code_fences(content)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass
        try:
            return json.loads(BaselineGenerator._sanitize_control_chars(cleaned))
        except json.JSONDecodeError:
            pass
        extracted = BaselineGenerator._extract_json_object_text(cleaned)
        try:
            return json.loads(extracted)
        except json.JSONDecodeError:
            return json.loads(BaselineGenerator._sanitize_control_chars(extracted))

    @staticmethod
    def _save_raw_response(output_path: str | None, content: str, suffix: str):
        if not output_path:
            return
        base, _ = os.path.splitext(output_path)
        raw_path = f"{base}.{suffix}.raw.txt"
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ! Saved raw response for debugging: {raw_path}")

    @staticmethod
    def _normalize_module_name(name: str) -> str:
        cleaned = name.strip().lower()
        while cleaned and cleaned[0].isdigit():
            cleaned = cleaned[1:]
        cleaned = cleaned.lstrip(". ):-")
        return " ".join(cleaned.replace("&", " and ").split())

    @staticmethod
    def _extract_expected_modules(functional_desc: Dict[str, Any]) -> list[str]:
        for key in ("Functional Overview", "Functional Specification",
                    "Functional Modules", "Functional Description"):
            value = functional_desc.get(key)
            if isinstance(value, dict):
                return [str(module).strip() for module in value.keys() if str(module).strip()]

        modules = functional_desc.get("Modules")
        if isinstance(modules, list):
            extracted: list[str] = []
            for module in modules:
                if not isinstance(module, dict):
                    continue
                for field in ("module_title", "title", "name", "module"):
                    value = module.get(field)
                    if isinstance(value, str) and value.strip():
                        extracted.append(value.strip())
                        break
            return extracted

        return []

    @classmethod
    def _find_missing_modules(cls, raw_suite: Dict[str, Any], expected_modules: list[str]) -> list[str]:
        if not expected_modules:
            return []

        actual_modules = {
            cls._normalize_module_name(tc.get("module_title", ""))
            for tc in raw_suite.get("test_cases", [])
            if isinstance(tc, dict) and isinstance(tc.get("module_title"), str)
        }

        missing: list[str] = []
        for module in expected_modules:
            normalized = cls._normalize_module_name(module)
            if normalized and normalized not in actual_modules:
                missing.append(module)
        return missing

    def _call_llm_once(
        self,
        client: httpx.Client,
        system_prompt: str,
        user_message: str,
    ) -> tuple[str, int, str]:
        """Call the configured provider once and return (content, tokens, finish_reason)."""
        if self._use_openai_responses_api():
            payload = {
                "model": self.model,
                "input": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                # Larger outputs (Mifos/Moodle/PHPTravels) were truncating at 16k.
                "max_output_tokens": 32000,
                "temperature": self.temperature,
            }
            if self.seed is not None:
                payload["seed"] = self.seed

            endpoint = "https://api.openai.com/v1/responses"
            response = client.post(
                endpoint,
                headers=self._get_headers(),
                json=payload,
            )

            # Some GPT-5 configurations reject temperature overrides.
            if response.status_code == 400 and "temperature" in response.text:
                payload.pop("temperature", None)
                response = client.post(
                    endpoint,
                    headers=self._get_headers(),
                    json=payload,
                )

            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                raise Exception(
                    f"{exc}; body={exc.response.text[:1000]}"
                ) from exc

            result = response.json()
            content = self._extract_responses_output_text(result)
            usage = result.get("usage", {})
            tokens = usage.get("total_tokens") or (
                (usage.get("input_tokens") or 0) + (usage.get("output_tokens") or 0)
            )
            # Responses API surfaces truncation via incomplete_details
            finish_reason = "stop"
            if result.get("incomplete_details") or result.get("status") == "incomplete":
                finish_reason = "length"
            return content, int(tokens or 0), finish_reason

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            "temperature": self.temperature,
            # Match GPT-5 budget; gpt-4.1-mini supports up to 32768 output tokens.
            "max_tokens": 32000,
        }
        if self.seed is not None:
            payload["seed"] = self.seed

        endpoint = self._get_api_endpoint()
        response = client.post(
            endpoint,
            headers=self._get_headers(),
            json=payload,
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise Exception(
                f"{exc}; body={exc.response.text[:1000]}"
            ) from exc

        result = response.json()
        choice = result["choices"][0]
        content = choice["message"]["content"]
        finish_reason = choice.get("finish_reason", "stop")
        tokens = result.get("usage", {}).get("total_tokens", 0)
        return content, int(tokens or 0), finish_reason

    # ------------------------------------------------------------------
    # Prompt construction
    # ------------------------------------------------------------------

    def _load_system_prompt(self) -> str:
        prompt_file = "zero_shot.txt" if self.num_shots == 0 else "few_shot.txt"
        prompt_path = os.path.join(
            os.path.dirname(__file__), "prompts", prompt_file
        )
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()

    def _load_examples(self) -> List[Dict[str, Any]]:
        examples_path = os.path.join(
            os.path.dirname(__file__), "prompts", "examples.json"
        )
        with open(examples_path, "r", encoding="utf-8") as f:
            all_examples = json.load(f)
        return all_examples[: self.num_shots]

    def _build_coverage_guidance(self, functional_desc: Dict[str, Any]) -> str:
        expected_modules = self._extract_expected_modules(functional_desc)
        if not expected_modules:
            return ""

        checklist = "\n".join(f"- {module}" for module in expected_modules)
        return (
            "\n\n**MODULE COVERAGE CHECKLIST (mandatory):**\n"
            "You MUST cover every module below using the exact module title in each test case.\n"
            f"{checklist}\n"
            "Coverage-first rule: first ensure every module has at least 3 test cases before adding extra depth to any one module.\n"
            "Do not omit later modules because earlier modules became too detailed.\n"
            "If a module mentions navigation, validation, state change, personas, or logout/session behavior, include those behaviors in that module's tests."
        )

    def _build_strategy_guidance(self) -> str:
        if self.num_shots == 0:
            return (
                "\n\n**STRATEGY GOAL:** Produce a compact but complete suite that satisfies minimum module coverage and all critical validations."
            )
        if self.num_shots == 1:
            return (
                "\n\n**STRATEGY GOAL:** Match the coverage minimums first, then use the example pattern to improve specificity of data, steps, and expected results."
            )
        if self.num_shots in (2, 3):
            return (
                "\n\n**STRATEGY GOAL:** Preserve full module coverage while increasing diversity of negative and edge-case scenarios beyond the minimum examples."
            )
        return (
            "\n\n**STRATEGY GOAL:** Preserve full module coverage while maximizing scenario diversity, cross-page navigation checks, and state-persistence validations."
        )

    def _create_prompt(
        self, functional_desc: Dict[str, Any], credentials: Dict[str, Any] | None = None
    ) -> tuple[str, str]:
        system_prompt = self._load_system_prompt()

        user_message = f"**FUNCTIONAL DESCRIPTION:**\n\n{json.dumps(functional_desc, indent=2)}\n"
        user_message += self._build_coverage_guidance(functional_desc)
        user_message += self._build_strategy_guidance()

        if credentials:
            user_message += (
                f"\n\n**CREDENTIALS (for login scenarios):**\n\n"
                f"{json.dumps(credentials, indent=2)}\n"
            )

        if self.num_shots > 0:
            examples = self._load_examples()
            examples_text = ""
            for i, ex in enumerate(examples, 1):
                examples_text += f"\n**Example {i}:**\n```json\n{json.dumps(ex, indent=2)}\n```\n"
            system_prompt = system_prompt.replace("{examples}", examples_text)

        user_message += (
            "\n\nGenerate the complete test suite now. "
            "Before finalizing mentally, verify that every module from the checklist appears in test_cases and that summary.by_module reflects those same modules."
        )
        return system_prompt, user_message

    COMPACT_RETRY_INSTRUCTION = (
        "\n\nIMPORTANT: The previous response was TRUNCATED before it finished. "
        "Regenerate the COMPLETE test suite in a MORE CONCISE format so it fits within the token budget:\n"
        "- Keep the exact same module list (all modules must appear).\n"
        "- Limit each test case to 3-5 steps maximum (1 short sentence each).\n"
        "- Limit expected_result to 1 short sentence.\n"
        "- Aim for 3 test cases per module (at least 1 positive, 1 negative, 1 edge).\n"
        "- The summary.by_module MUST list every module with its test count.\n"
        "Return ONLY valid JSON. No markdown fences, no prose."
    )

    def _generate_parseable_suite(
        self,
        system_prompt: str,
        user_message: str,
        output_path: str | None,
    ) -> tuple[Dict[str, Any], int, int]:
        api_calls = 0
        total_tokens = 0

        with httpx.Client(timeout=300.0) as client:
            content, call_tokens, finish_reason = self._call_llm_once(client, system_prompt, user_message)
        api_calls += 1
        total_tokens += call_tokens

        was_truncated = finish_reason == "length"

        try:
            raw_suite = self._parse_json_response(content)
            return raw_suite, api_calls, total_tokens
        except json.JSONDecodeError as first_err:
            print(f"  ! Parse failed on first attempt: {first_err}")
            if was_truncated:
                print("  ! Detected output truncation (token limit hit) — retrying with compact instruction")
            self._save_raw_response(output_path, content, "invalid_json_first")

        if was_truncated:
            retry_prompt = user_message + self.COMPACT_RETRY_INSTRUCTION
        else:
            retry_prompt = user_message + JSON_RETRY_INSTRUCTION

        with httpx.Client(timeout=300.0) as client:
            retry_content, retry_tokens, _ = self._call_llm_once(client, system_prompt, retry_prompt)
        api_calls += 1
        total_tokens += retry_tokens
        print("  ! Retried generation with strict JSON instruction")

        try:
            raw_suite = self._parse_json_response(retry_content)
            return raw_suite, api_calls, total_tokens
        except json.JSONDecodeError as second_err:
            self._save_raw_response(output_path, retry_content, "invalid_json_retry")
            raise Exception(
                f"Invalid JSON after retry: {second_err}"
            ) from second_err

    # ------------------------------------------------------------------
    # Core generation
    # ------------------------------------------------------------------

    def generate(
        self,
        functional_desc: str | Dict[str, Any],
        output_path: str | None = None,
    ) -> Dict[str, Any]:
        """Generate test cases from a functional description path or dict.

        Returns a dict in the same shape as TestWright's test-cases.json.
        """
        approach_name = self.APPROACH_NAMES.get(self.num_shots, f"{self.num_shots}-shot")

        print("=" * 80)
        print(f"{approach_name.upper()} BASELINE TEST GENERATION")
        print("=" * 80)

        # Load inputs
        print(f"\n[1/4] Loading input files...")
        if isinstance(functional_desc, str):
            json_path = Path(functional_desc)
            with open(functional_desc, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = functional_desc
            json_path = None

        # Extract metadata
        project_name = data.get("Website URL", "Unknown")
        if json_path:
            project_name = json_path.stem.replace("-", " ").replace("_", " ").title()
        base_url = data.get("Website URL", "")

        # Extract credentials if present
        credentials = data.get("Credentials", None)

        print(f"  - Project: {project_name}")
        print(f"  - URL: {base_url}")
        if credentials:
            print(f"  - Found credentials")

        # Create prompt
        print(f"[2/4] Creating {approach_name} prompt...")
        system_prompt, user_message = self._create_prompt(data, credentials)
        expected_modules = self._extract_expected_modules(data)
        print(f"  - Number of examples: {self.num_shots}")
        print(f"  - Prompt length: {len(system_prompt) + len(user_message)} chars")
        if expected_modules:
            print(f"  - Expected modules: {len(expected_modules)}")

        # Call LLM
        print(f"[3/4] Calling {self.model} via {self.provider}...")
        start_time = time.time()
        raw_suite, api_calls, total_tokens = self._generate_parseable_suite(
            system_prompt, user_message, output_path
        )
        self.total_tokens = total_tokens

        first_call_time = time.time() - start_time

        print(f"  ✓ Generated in {first_call_time:.2f}s")
        print(f"  ✓ Tokens: {self.total_tokens:,}")

        # Parse JSON response
        print(f"[4/4] Parsing response...")
        missing_modules = self._find_missing_modules(raw_suite, expected_modules)
        if missing_modules:
            print(f"  ! Missing modules detected: {', '.join(missing_modules)}")
            coverage_retry_prompt = user_message + MISSING_MODULE_RETRY_TEMPLATE.format(
                missing_modules="\n".join(f"- {module}" for module in missing_modules)
            )
            coverage_suite, extra_calls, extra_tokens = self._generate_parseable_suite(
                system_prompt, coverage_retry_prompt, output_path
            )
            api_calls += extra_calls
            self.total_tokens += extra_tokens
            raw_suite = coverage_suite
            missing_modules = self._find_missing_modules(raw_suite, expected_modules)
            if missing_modules:
                raise Exception(
                    "Missing required modules after coverage retry: " + ", ".join(missing_modules)
                )

        # Includes any retry latency so reported metrics reflect actual runtime.
        self.generation_time = time.time() - start_time

        # Normalise into the agent output format
        test_cases = raw_suite.get("test_cases", [])
        raw_summary = raw_suite.get("summary", {})

        # Build summary if missing or incomplete
        summary = self._build_summary(test_cases, raw_summary)

        # Assemble in the same shape as TestWright test-cases.json
        output = {
            "project_name": project_name,
            "base_url": base_url,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "approach": approach_name,
            "model": self.model,
            "provider": self.provider,
            "temperature": self.temperature,
            "generation_time_seconds": round(self.generation_time, 2),
            "total_tokens": self.total_tokens,
            "api_calls": api_calls,
            "test_cases": test_cases,
            "summary": summary,
        }

        # Save if output_path provided
        if output_path:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"\n  ✓ Saved to: {output_path}")

        print(f"\n{'='*80}")
        print("GENERATION COMPLETE")
        print("=" * 80)
        print(f"  Total tests: {summary.get('total_tests', len(test_cases))}")
        print(f"  By type: {summary.get('by_type', {})}")
        print(f"  By module: {summary.get('by_module', {})}")

        return output

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_summary(test_cases: list, raw_summary: dict) -> dict:
        """Build/validate the summary dict from actual test case data."""
        by_type = {"positive": 0, "negative": 0, "edge_case": 0}
        by_priority = {"High": 0, "Medium": 0, "Low": 0}
        by_module: Dict[str, int] = {}

        for tc in test_cases:
            t = tc.get("test_type", "positive")
            if t in by_type:
                by_type[t] += 1

            p = tc.get("priority", "Medium")
            if p in by_priority:
                by_priority[p] += 1

            mod = tc.get("module_title", "Unknown")
            by_module[mod] = by_module.get(mod, 0) + 1

        return {
            "total_tests": len(test_cases),
            "by_type": by_type,
            "by_priority": by_priority,
            "by_module": by_module,
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Baseline test case generator")
    parser.add_argument("--input", required=True, help="Functional description JSON")
    parser.add_argument("--shots", type=int, default=0, choices=[0, 1, 2, 3, 5])
    parser.add_argument("--api-key", default="", help="API key (not required for provider=ollama)")
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--provider", default="openai", choices=["openai", "github", "openrouter", "google", "ollama"])
    parser.add_argument("--temperature", type=float, default=0.3, help="Sampling temperature")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument("--output", help="Output JSON path")
    args = parser.parse_args()

    gen = BaselineGenerator(
        api_key=args.api_key,
        model=args.model,
        provider=args.provider,
        num_shots=args.shots,
        temperature=args.temperature,
        seed=args.seed,
    )
    gen.generate(args.input, output_path=args.output)
