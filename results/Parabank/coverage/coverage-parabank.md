## Coverage Comparison

| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **85.0%** | 30              |
| 🥈 2 | GPT-4o-mini | Agent                     | **71.0%** | 58              |
| 🥉 3 | GPT-5-mini  | Few-shot (Per module)     | **60.0%** | 80              |
| 4    | GPT-5-mini  | Zero-shot (Per module)    | **59.5%** | 81              |
| 5    | GPT-4o-mini | Zero-shot (Per module)    | **47.0%** | 106             |
| 6    | GPT-4o-mini | Few-shot (Per module)     | **28.5%** | 143             |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| Agents outperform non-agents across both models  | **Agentic reasoning is critical for high coverage** |
| GPT-4o-mini Agent (71.0%) beats GPT-5-mini Zero-shot (59.5%) | **A weaker model with an agent beats a stronger model without one** |
| GPT-5 Few-shot (60.0%) and Zero-shot (59.5%) are nearly identical | **Few-shot prompting adds negligible value for the advanced model** |
| GPT-4o-mini Few-shot (28.5%) performed much worse than Zero-shot (47.0%) | **Examples severely constrain the weaker model's generation scope** |
| GPT-5-mini Agent achieves highest coverage (85.0%) | **Most comprehensive test suite**           |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest overall coverage (85.0%), misses only 30 cases | Generates additional overhead with extra cases |
| GPT-4o Agent     | Excellent cost-to-performance ratio, beating base GPT-5 | Leaves a significant 58-case gap |
| GPT-5 Few-shot   | Marginal improvement over zero-shot (+0.5%) | High prompt cost for minimal gain |
| GPT-5 Zero-shot  | Good baseline performance without prompting overhead | Fails to explore complex edge cases |
| GPT-4o Zero-shot | Cheap and fast to execute         | Misses over half the GT cases (106 missed) |
| GPT-4o Few-shot  | None evident (worst performance)  | Severe coverage drop, highly constrained generation |
