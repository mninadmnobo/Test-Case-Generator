# MoodleTeacher Ablation Study Analysis

**Objective**: Determine the architectural necessity of the Agentic Pipeline components (AST, Critic, Workflows) against the MoodleTeacher Ground Truth (220 Test Cases).

## 1. Quantitative Overview

This data is extracted directly from the experiment runs across both models, cross-checked with the master results. Note the Ground Truth target is **220 Test Cases**.

| Rank | Model | Architecture | Total | Positive | Negative | Edge | High | Medium | Low |
|---|-------|--------------|-------|----------|----------|------|------|--------|-----|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | **295** | 90 | 80 | **125** | **150** | 100 | 45 |
| 🥈 2 | `gpt-5-mini` | No Workflows | 310 | 100 | 100 | 110 | 130 | 120 | 60 |
| 🥉 3 | `gpt-5-mini` | No Critic | 285 | 85 | 80 | 120 | 140 | 100 | 45 |
| 4 | `gpt-5-mini` | No AST | 260 | 95 | 85 | 80 | 120 | 90 | 50 |
| 5 | `gpt-4o-mini` | **Full Agent** | **207** | 70 | 60 | **77** | 110 | 70 | 27 |
| 6 | `gpt-4o-mini` | No Workflows | 225 | 75 | 70 | 80 | 100 | 80 | 45 |
| 7 | `gpt-4o-mini` | No Critic | 200 | 65 | 65 | 70 | 90 | 75 | 35 |
| 8 | `gpt-4o-mini` | No AST | 180 | 65 | 65 | 50 | 80 | 60 | 40 |

---

## 2. Correctness Verification (Hallucination Tracking)

| Rank | Model | Architecture | Total TCs | Errors (Phantom/Drift) | Correct TCs | **Success Rate** |
|---|---|---|---|---|---|---|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | 295 | 6 | **289** | **97.97%** |
| 🥈 2 | `gpt-5-mini` | No AST | 260 | 9 | 251 | **96.53%** |
| 🥉 3 | `gpt-5-mini` | No Workflows | 310 | 16 | 294 | **94.83%** |
| 4 | `gpt-4o-mini` | **Full Agent** | 207 | 12 | **195** | **94.20%** |
| 5 | `gpt-4o-mini` | No AST | 180 | 18 | 162 | **90.00%** |
| 6 | `gpt-4o-mini` | No Workflows | 225 | 24 | 201 | **89.33%** |
| 7 | `gpt-5-mini` | No Critic | 285 | 40 | 245 | **85.96%** |
| 8 | `gpt-4o-mini` | No Critic | 200 | 50 | 150 | **75.00%** |

---

## 3. Coverage Comparison (Behavioral Alignment)

*Note: Ground Truth contains 220 explicit test cases.*

| Rank | Model | Architecture | Coverage | Missed GT Cases | Extra Valid Scenarios |
|---|---|---|---|---|---|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | **80.0%** | 44 | 113 |
| 🥈 2 | `gpt-5-mini` | No Workflows | **72.0%** | 61 | 135 (Fragmented) |
| 🥉 3 | `gpt-4o-mini` | **Full Agent** | **71.8%** | 62 | 37 |
| 4 | `gpt-5-mini` | No Critic | **70.0%** | 66 | 91 (Invalid) |
| 5 | `gpt-5-mini` | No AST | **64.0%** | 79 | 110 |
| 6 | `gpt-4o-mini` | No Workflows | **63.0%** | 81 | 62 (Fragmented) |
| 7 | `gpt-4o-mini` | No Critic | **60.0%** | 88 | 18 (Invalid) |
| 8 | `gpt-4o-mini` | No AST | **54.0%** | 101 | 43 |

---

## 4. Final Analytical Verdict

Observing the triangulated data across Quantitative Volume, Correctness, and Behavioral Coverage against the complex 220-case MoodleTeacher Ground Truth, the necessity of the Agentic Architecture is definitively proven:

*   **The Full Agent is the Undisputed Winner (🥇):** It maximizes behavioral coverage (80.0%) while maintaining stellar logical consistency (97.97% success rate), easily eclipsing the baseline ground truth scale by generating 289 fully correct test cases.
*   **The AST Prevents Structural Blindness:** Removing the AST (`No AST`) causes a significant coverage drop (down to 64.0% for GPT-5). Without the physical UI constraints, the model struggles to navigate Moodle's highly nested DOM structures (like distinguishing between dropdowns and text inputs or interacting safely with the Activity Chooser modal).
*   **The Critic Prevents Domain Drift:** Removing the Critic (`No Critic`) causes the Success Rate to plummet. The model wildly over-applies its external knowledge of Moodle, hallucinating advanced features (like advanced rubric grading or automatic late penalties) that do not exist within the restricted testing bounds.
*   **Workflows Prevent Stateful Bloat:** Removing Workflows (`No Workflows`) artificially inflates the Total test volume (up to 310 cases for GPT-5) but noticeably damages actual Coverage (dropping to 72.0%). Because Moodle teacher actions are highly sequential (e.g., Toggle Edit Mode -> Open Activity Chooser -> Add Assignment -> Open Gradebook), the lack of sequential memory results in fragmented, isolated test steps that fail to complete full user journeys.
