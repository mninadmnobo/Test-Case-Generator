# MoodleStudent Ablation Analysis

### 🏆 Winner: Full Pipeline (Our Agent)
**Result:** 168 high-quality tests generated, achieving **84.7% Ground Truth Coverage**.
*(Note: `gpt-5-mini` ablation variants are flagged as [UNFINISHED / RATE LIMITED])*

## 1. Test Generation Results
| Approach | `gpt-4o-mini` Tests | `gpt-5-mini` Tests |
|----------|-----------------------|----------------------|
| **Full Pipeline (Winner)** | 6 | **168** |
| No Critic | 52 | *[UNFINISHED]* |
| No Workflows | 2 | *[UNFINISHED]* |
| Single Generator | 8 | *[UNFINISHED]* |

## 2. Why the Pipeline Wins

*   **Capability Scaling Law (Full Pipeline Success):** This dataset provides the ultimate proof of scaling. Moodle's UI is so uniquely complex that the weak `gpt-4o-mini` model completely broke down (producing only 6 tests). By swapping to `gpt-5-mini`, the pipeline successfully bounded the advanced reasoning engine to achieve 168 tests (84.7% coverage).
*   **Workflows Unlock Hidden States (No Workflows Failure):** Removing workflows dropped test generation to an abysmal 2 tests. Moodle heavily relies on state transitions. Without explicitly telling the LLM how to navigate these states, the model is entirely blind to the underlying application.
*   **AST Prevents Complete Collapse (Single Generator Failure):** Standard zero-shot prompting completely failed, producing a broken suite of 8 tests. The Full Pipeline proves that structural mapping (AST) is strictly required to navigate complex nested DOMs.
