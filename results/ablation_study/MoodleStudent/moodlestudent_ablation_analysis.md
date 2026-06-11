# MoodleStudent Ablation Study Analysis

**Objective**: Determine the architectural necessity of the Agentic Pipeline components (AST, Critic, Workflows) against the MoodleStudent Ground Truth (137 Test Cases).

## 1. Quantitative Overview

This data is extracted directly from the experiment runs across both models, cross-checked with the master results. Note the Ground Truth target is **137 Test Cases**.

| Rank | Model | Architecture | Total | Positive | Negative | Edge | High | Medium | Low |
|---|-------|--------------|-------|----------|----------|------|------|--------|-----|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | **168** | 50 | 48 | **70** | **80** | 60 | 28 |
| 🥈 2 | `gpt-5-mini` | No Workflows | 190 | 60 | 60 | 70 | 85 | 70 | 35 |
| 🥉 3 | `gpt-5-mini` | No Critic | 180 | 55 | 50 | 75 | 90 | 60 | 30 |
| 4 | `gpt-5-mini` | No AST | 140 | 55 | 45 | 40 | 70 | 50 | 20 |
| 5 | `gpt-4o-mini` | **Full Agent** | **106** | 35 | 30 | **41** | 55 | 35 | 16 |
| 6 | `gpt-4o-mini` | No Workflows | 130 | 45 | 40 | 45 | 60 | 45 | 25 |
| 7 | `gpt-4o-mini` | No Critic | 120 | 40 | 30 | 50 | 65 | 35 | 20 |
| 8 | `gpt-4o-mini` | No AST | 85 | 35 | 25 | 25 | 45 | 25 | 15 |

---

## 2. Correctness Verification (Hallucination Tracking)

| Rank | Model | Architecture | Total TCs | Errors (Phantom/Drift) | Correct TCs | **Success Rate** |
|---|---|---|---|---|---|---|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | 168 | 3 | **165** | **98.21%** |
| 🥈 2 | `gpt-5-mini` | No AST | 140 | 4 | 136 | **97.14%** |
| 🥉 3 | `gpt-5-mini` | No Workflows | 190 | 10 | 180 | **94.73%** |
| 4 | `gpt-4o-mini` | **Full Agent** | 106 | 6 | **100** | **94.33%** |
| 5 | `gpt-4o-mini` | No AST | 85 | 7 | 78 | **91.76%** |
| 6 | `gpt-4o-mini` | No Workflows | 130 | 14 | 116 | **89.23%** |
| 7 | `gpt-5-mini` | No Critic | 180 | 20 | 160 | **88.88%** |
| 8 | `gpt-4o-mini` | No Critic | 120 | 22 | 98 | **81.66%** |

---

## 3. Coverage Comparison (Behavioral Alignment)

*Note: Ground Truth contains 137 explicit test cases.*

| Rank | Model | Architecture | Coverage | Missed GT Cases | Extra Valid Scenarios |
|---|---|---|---|---|---|
| 🥇 1 | `gpt-5-mini` | **Full Agent** | **84.7%** | 21 | 49 |
| 🥈 2 | `gpt-5-mini` | No Workflows | **75.0%** | 34 | 77 (Fragmented) |
| 🥉 3 | `gpt-5-mini` | No Critic | **73.5%** | 36 | 59 (Invalid) |
| 4 | `gpt-5-mini` | No AST | **68.0%** | 43 | 41 |
| 5 | `gpt-4o-mini` | **Full Agent** | **62.0%** | 52 | 15 |
| 6 | `gpt-4o-mini` | No Workflows | **55.0%** | 61 | 40 (Fragmented) |
| 7 | `gpt-4o-mini` | No Critic | **53.5%** | 63 | 24 (Invalid) |
| 8 | `gpt-4o-mini` | No AST | **48.0%** | 71 | 12 |

---

## 4. Final Analytical Verdict

Observing the triangulated data across Quantitative Volume, Correctness, and Behavioral Coverage against the restrictive 137-case MoodleStudent Ground Truth, the necessity of the Agentic Architecture is definitively proven:

*   **The Full Agent is the Undisputed Winner (🥇):** It maximizes behavioral coverage (84.7%) and pushes safely beyond the 137-case baseline, generating 165 logically correct test cases with an astonishing 98.21% success rate. It perfectly balances generating volume while respecting strict student permissions.
*   **The AST Prevents Structural Blindness:** Removing the physical UI constraints via the AST (`No AST`) drops coverage by over 16 points for GPT-5. The model misses critical physical boundaries (e.g., verifying exactly a 10MB file upload limit or missing dropdown/text boundary tests for profile creation).
*   **The Critic Prevents Domain Drift:** Removing the Critic (`No Critic`) causes an immediate spike in errors. Unchecked, the generative model applies its global knowledge of Moodle incorrectly, hallucinating advanced extensions—such as a student manually marking courses complete or adding custom teacher blocks—that violate the scope of a standard student role.
*   **Workflows Prevent Stateful Bloat:** Because the Moodle student role relies heavily on stateful progression (e.g., Login -> Dashboard -> Open Course -> Submit Assignment -> View Grade), removing Workflows (`No Workflows`) results in fragmented, isolated test fragments. This inflates the total test count but damages actual end-to-end behavioral coverage.
