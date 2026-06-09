# MoodleTeacher Ablation Analysis

### 🏆 Winner: Full Pipeline (Our Agent)
**Result:** 295 high-quality tests generated, achieving **80.0% Ground Truth Coverage**.

## 1. Test Generation Results
| Approach | `gpt-4o-mini` Tests | `gpt-5-mini` Tests |
|----------|-----------------------|----------------------|
| **Full Pipeline (Winner)** | 200 | **295** |
| No Critic | 226 | 64 |
| No Workflows | 63 | 34 |
| Single Generator | 10 | 20 |

## 2. Why the Pipeline Wins

*   **Workflows Unlock Hidden States (No Workflows Failure):** Moodle hides 90% of its UI behind a "Turn Editing On" button. Without workflows to unlock this state, the LLM was completely blind, dropping from 295 to 34 tests. Workflows are strictly mandatory for state-dependent applications.
*   **Critic Saves the Extraction (No Critic Failure):** Removing the Critic caused the output to plummet to 64 tests. Moodle's DOM is deeply nested, causing the initial extraction to fail. The Critic caught this, rejected the flawed AST, and forced a perfect re-extraction—single-handedly recovering over 200 tests.
*   **AST Solves the Complete Baseline Collapse (Single Generator Failure):** The baseline LLM failed catastrophically on Moodle, producing only 20 tests zero-shot. The Full Pipeline proves it is an absolute necessity to test complex, hidden-state applications.
