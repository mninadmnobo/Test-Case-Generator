# AutoSpecTest Experiment Results & Coverage Analysis

This directory contains the complete experimental data, generated test suites, and comprehensive coverage analysis reports evaluating Large Language Models (LLMs) and agentic workflows on the task of automated software test case generation.

---

## 📂 Directory Structure & Audit Pipeline

The results are organized systematically to mirror our multi-stage validation and auditing pipeline:

*   **`[Project Name]/`**: Individual folders for each of the 6 evaluated applications (e.g., `Mifos`, `SwagLab`).
    *   **`gpt-5-mini/` & `gpt-4o-mini/`**: Contain the raw LLM outputs and parsed JSON test cases for each strategy.
        *   `agent/`, `zero_shot_per_module/`, etc.: Outputs from the models.
    *   **`coverage/`**: The auditing hub for this dataset.
        *   *Individual Audits:* Contains the detailed markdown reports mapping each generated test suite against the human-authored Ground Truth (GT).
        *   *Dataset Consolidation:* Contains the merged dataset-wide coverage report (e.g., `coverage-mifos.md`).
*   **`results.md`**: The final master document. All 6 dataset-wide coverage reports are merged and audited into this single file to generate the global findings.

---

## 🏆 1. Coverage Comparison & Key Findings

By aggregating the coverage data across all 6 projects (detailed fully in `results.md`), a striking and consistent story emerges about how AI approaches QA tasks.

### 🤖 The Dominance of the Agentic Loop
The **GPT-5-mini Agent** crushed the competition, achieving an astonishing **80–88% coverage** across every single project. Instead of guessing once, the agent thinks step-by-step. In highly restricted applications (like a student portal), the Agent was 21% better than standard prompting because it actively iterated to discover what a user *isn't* allowed to do.

### 📉 The "Example" Trap (Few-Shot Fallacy)
Showing the AI examples of good test cases (Few-shot prompting) actually **lowered** the final coverage compared to giving it no examples at all (Zero-shot). When the AI sees examples, it gets "tunnel vision"—it blindly copies the style of the examples instead of creatively exploring the application's unique edge cases. Zero-shot prompting allowed the models to brainstorm much more freely.

### 🧠 Brains Over Tactics
While adding an agent loop to the weaker GPT-4o-mini gave it a massive 23% coverage boost, it still wasn't enough to beat the premium model. A weak model working incredibly hard (62% average) still lost to a highly intelligent base model doing the bare minimum zero-shot prompting (70% average). For complex software testing, raw AI brainpower fundamentally dictates the coverage ceiling.

---

## 🧪 2. How Results Are Generated

The raw test generation is orchestrated by `run_experiments.py` at the project root. This script systematically queries the OpenAI API across a matrix of variables:

*   **6 Target Specifications:** Ranging from simple e-commerce (SwagLab) to highly complex enterprise ERPs (Mifos).
*   **2 Models:** `gpt-5-mini` (Premium/Advanced) and `gpt-4o-mini` (Fast/Efficient).
*   **3 Core Strategies:**
    1.  **Zero-Shot:** The model is given the raw specification without any examples.
    2.  **Few-Shot:** The model is provided with high-quality example test cases.
    3.  **Agent:** The model operates within the AutoSpecTest framework, utilizing an iterative loop to generate, review, and refine its test cases dynamically.

*   **2 Prompting Structures (for Baseline Strategies):**
    1.  **Monolithic (Whole-file):** The entire application specification is passed to the model in a single prompt.
    2.  **Modular (Per-module):** The specification is split into logical sections, and the model is prompted iteratively for each module.

For baseline strategies, the LLM is queried directly. For the agent strategy, a dedicated subprocess runs the multi-agent workflow. The final output is standardized into parsed `test-cases.json` files alongside the raw text responses.

---

## 📊 3. How Coverage is Calculated

Coverage is not measured by naive keyword matching or superficial text similarity. **Coverage is a measure of behavioral alignment**. We ask: *"Did the agent independently discover and test the same business logic and edge cases that a human expert deemed necessary?"*

### Standard Operating Procedure (SOP) for Coverage Evaluation

When evaluating whether a generated test covers a Ground Truth scenario, we apply relaxed, behavior-driven rules rather than strict keyword matching.

#### Core Principles
1.  **Semantic Equivalence vs. Textual Similarity:** We never rely on keyword matching. If the Ground Truth (GT) requires "Empty username rejected," and the Generated (GEN) test explicitly checks "Submit form with blank user ID," it is considered **Covered**. They test the identical technical behavior.
2.  **Core Boundaries vs. Generic Tests:** A generic test case does not cover a specific boundary or edge-case test. If GT requires "Submit with invalid username format containing special characters", a GEN test that simply says "Submit with invalid credentials" does **NOT** cover it. The specific boundary condition must be explicitly tested.
3.  **Fixture and Data Agnosticism:** We ignore specific test data or fixture names provided they achieve the exact same logical outcome (e.g., clicking "Course 101" vs "Math 102").
4.  **Combined vs. Split Scenarios:** Coverage is about the behavior, not the 1:1 mapping of test steps. If a single GEN test explicitly checks an empty username and an empty password, it successfully covers TWO separate GT scenarios. Conversely, two split GEN tests can cover a single combined GT scenario.
5.  **Negative Assertions & State Checks:** Tests verifying that something is *not* supposed to happen must be explicit. If GT requires "Student cannot access Settings", a GEN test verifying "Course tabs are visible" is insufficient; it must explicitly assert the *absence* of the Settings tab.
6.  **Equivalence Classes:** The exact field being tested can be flexible if it belongs to the same functional equivalence class (e.g., testing required field validation by leaving "Email" blank instead of "First name").
7.  **Implied and Partial Coverage:** If an agent tests a specific complex edge case of a feature (e.g., searching with special characters), it implicitly covers the basic functional requirement of that feature (e.g., standard search).

### 🧠 The Agentic Evaluation Workflow (Skill File Integration)
To completely automate the grading process while maintaining human-level QA judgment, this README serves as a **Skill File (SOP)** for an AI agent. 

**How the Skill File is used:**
1.  **Context Loading:** The evaluation agent is fed three things: the human-authored Ground Truth (GT) suite, the model-Generated (GEN) suite, and this Skill File.
2.  **Autonomous Reasoning:** Instead of relying on a rigid, hardcoded python script for string matching, the agent reads the SOP and uses its LLM reasoning capabilities to apply the "Core Principles" defined above. It autonomously handles the complex, fuzzy logic of "behavioral alignment" and "semantic equivalence."
3.  **Strict Output Formatting:** The Skill File also enforces a strict document structure. The agent is instructed to output its findings using the exact markdown template provided in the SOP. This ensures every single coverage report generated across all projects perfectly adheres to the required layout: Executive Summary -> Per-Module Coverage -> Gaps -> Extras.

This workflow allows for massive scalability without losing the nuanced, relaxed evaluation rules required when comparing AI outputs to human text.

### 📈 The Audit & Aggregation Pipeline
To ensure absolute accuracy, coverage data flows through a strict three-tier auditing pipeline mirrored by the folder structure:

1.  **Tier 1: Individual Audit (`[Project]/coverage/[strategy]-coverage.md`)**  
    Each raw generated result (`test-cases.json`) is rigorously validated and audited against the human Ground Truth using the Skill File SOP. The output is a standalone markdown report.
2.  **Tier 2: Dataset Consolidation (`[Project]/coverage/coverage-[project].md`)**  
    All individual coverage audits for a particular dataset are merged. The aggregated data is audited to generate a single, comprehensive coverage file that compares all models and strategies for that specific dataset.
3.  **Tier 3: Master Consolidation (`results.md`)**  
    Finally, all 6 dataset-level coverage files are merged and audited one last time to generate the global Key Findings found in `results.md` at the root of this directory.

---

## 📜 4. Agent Evaluator SOP (Skill File Instructions)

*This section serves as the explicit prompt/skill file for the LLM agent tasked with generating coverage reports. It defines the exact output structure, tone, and formatting required. You can feed this entire document to an agent to evaluate new coverage.*

### A. Fixed Document Structure
A proper coverage report must be written in Markdown and contain the following exact sections in order. Do not deviate from this fixed structure.

#### 1. Header & Metadata
Include the Ground Truth version, the Generated Suite name (and total case count), the Analysis Date, and a brief statement defining the coverage rules.

#### 2. Executive Summary
A high-level markdown table summarizing the macro metrics:
- GT total cases
- GT cases covered by GEN
- GT cases not covered by GEN
- Overall coverage percentage
- GEN cases with no GT counterpart (extras)

#### 3. Per-Module Coverage
A summary table breaking down the coverage metrics module by module (e.g., Login, Dashboard, My Courses). Columns must include:
`Module` | `GT Cases` | `Covered` | `Not Covered` | `Coverage %`

#### 4. Missing Scenarios (Gaps)
A detailed bulleted list of all GT test cases that were entirely absent from the generated suite, grouped by module. Do not include a detailed table mapping all covered cases. Only document the gaps to keep the report concise and actionable.
**Format:**
```markdown
### [Module Name] ([X] missing)
- [GT-ID] [Test Case Name]
```

#### 5. Extra Scenarios
Document the test cases generated by the agent that exceed the scope of the Ground Truth. Group them by module using bullet points. Include the approximate count of extra types.
**Format:**
```markdown
### [Module Name] (~[X] extra types)
- [Brief description of the extra test case]
```

### B. Tone and Formatting Guidelines
- **Strict Adherence:** The format must perfectly match the bulleted structure. Do not introduce redundant mapping tables.
- **Active Voice:** Write "The agent missed the unauthenticated redirect" rather than "The unauthenticated redirect was missed by the agent."
- **Clear Assertions:** Avoid speculative language. If a test is missing, state it clearly based on behavioral analysis.
- **Avoid Cliché AI-isms:** Do not use excessive em-dashes. Avoid starting paragraphs with filler transition words ("Furthermore", "Moreover", "In conclusion").

### C. Generic Example Template
Below is a complete, generic example of how a coverage report must be formatted:

```markdown
# Test Coverage Report

**Ground Truth:** ExampleApp GT v1.0  
**Generated Suite:** openai/gpt-X — 100 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 50 |
| GT cases covered by GEN | 40 |
| GT cases not covered by GEN | 10 |
| **Overall coverage** | **80.0%** |
| GEN cases with no GT counterpart (extras) | ~15 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Authentication | 20 | 18 | 2 | **90%** |
| Dashboard | 30 | 22 | 8 | **73%** |
| **Total** | **50** | **40** | **10** | **80.0%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Authentication (2 missing)
- AUTH-005 Submit with invalid username format containing special characters
- AUTH-012 Rapid double submission of login form

### Dashboard (8 missing)
- DASH-001 Dashboard page loads with user information visible
- DASH-007 Dashboard blocked while unauthenticated

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Authentication (~1 extra types)
- "Lost password?" link is disabled under specific conditions

### Dashboard (~5 extra types)
- Block drag handles functionality
- Calendar import/export functionality
```
