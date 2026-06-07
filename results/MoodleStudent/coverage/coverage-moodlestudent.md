## Coverage Comparison
| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **84.7%** | 21              |
| 🥈 2 | GPT-5-mini  | Zero-shot (Per module)    | **63.5%** | 50              |
| 🥉 3 | GPT-4o-mini | Agent                     | **62.0%** | 52              |
| 4    | GPT-5-mini  | Few-shot (Per module)     | **61.3%** | 53              |
| 5    | GPT-4o-mini | Zero-shot (Per module)    | **38.7%** | 84              |
| 6    | GPT-4o-mini | Few-shot (Per module)     | **26.3%** | 101             |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| GPT-5-mini Agent achieves the highest coverage (84.7%) | **Agentic loop with a strong base model is optimal** |
| Few-shot performed worse than zero-shot across both models | **Examples restricted the generation scope on this project** |
| GPT-4o-mini Agent (62.0%) nearly matches GPT-5-mini Zero-shot (63.5%) | **Agents can elevate weaker models to compete with stronger ones** |
| Agent provides a massive +21.2% boost over Zero-shot (much larger than Teacher or Mifos) | **Agentic iteration excels at systematically uncovering constrained boundary cases (e.g., student permission limits and strict submission deadlines)** |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest overall coverage (84.7%), misses only 21 cases | Higher generation overhead and API cost |
| GPT-5 Zero-shot  | Solid baseline (63.5%) with zero prompting overhead | Misses many complex scenarios |
| GPT-4o Agent     | Excellent cost-to-performance ratio, almost matching base GPT-5 | Fails on deeper logical cases |
| GPT-5 Few-shot   | Still decent coverage (61.3%)     | High prompt cost and worse performance than zero-shot |
| GPT-4o Zero-shot | Cheap and fast to execute         | Lowest quality baseline, misses 84 cases |
| GPT-4o Few-shot  | None evident                      | Severe coverage drop, highly constrained generation (misses 101 cases) |
