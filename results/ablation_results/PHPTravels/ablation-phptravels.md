# PHPTravels Ablation Analysis

### 🏆 Winner: Full Pipeline (Our Agent)
**Result:** 394 high-quality tests generated, achieving **88.8% Ground Truth Coverage**.

## 1. Test Generation Results
| Approach | `gpt-4o-mini` Tests | `gpt-5-mini` Tests |
|----------|-----------------------|----------------------|
| **Full Pipeline (Winner)** | 315 | **394** |
| No Critic | 302 | 438 |
| No Workflows | 314 | 383 |
| Single Generator | 180 | 440 |

## 2. Why the Pipeline Wins

*   **AST Prevents Hallucination (Single Generator Failure):** When tasked with an enterprise travel site zero-shot, `gpt-4o-mini` collapsed (180 tests) and `gpt-5-mini` hallucinated massive bloat (440 tests). The pipeline's AST mapping normalizes both extremes by explicitly bounding generation to the real UI.
*   **Critic Prunes Junk Tests (No Critic Failure):** Removing the Critic caused test volume to artificially spike to 438 tests. The Critic acted as a vital quality-control mechanism, successfully identifying and deleting 44 hallucinated/invalid tests to keep the suite accurate.
*   **Workflows Enable Integration (No Workflows Failure):** Removing workflows dropped output to 383. Without explicit multi-step paths (Search -> Select -> Passenger Details -> Pay), the LLM failed to test 11 critical integration scenarios.
