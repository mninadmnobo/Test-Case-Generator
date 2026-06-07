## Coverage Comparison

| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **80.2%** | 120             |
| 🥈 2 | GPT-5-mini  | Zero-shot (Per module)    | **74.1%** | 157             |
| 🥉 3 | GPT-5-mini  | Few-shot (Per module)     | **66.9%** | 201             |
| 4    | GPT-4o-mini | Agent                     | **65.2%** | 211             |
| 5    | GPT-4o-mini | Zero-shot (Per module)    | **26.4%** | 447             |
| 6    | GPT-4o-mini | Few-shot (Per module)     | **20.6%** | 482             |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| GPT-5-mini Agent achieves the highest coverage (80.2%) | **Agentic loop scales effectively to large, complex applications** |
| Few-shot performed worse than zero-shot across both models | **Examples severely restricted generation scope on large codebases** |
| GPT-5-mini Zero-shot (74.1%) beats GPT-4o-mini Agent (65.2%) | **Base model capability matters more on highly complex tasks** |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest overall coverage (80.2%), covering 487 complex cases | Higher generation overhead and API cost |
| GPT-5 Zero-shot  | Very strong baseline (74.1%) with no prompting overhead | Misses 157 complex edge cases |
| GPT-5 Few-shot   | Decent coverage (66.9%)           | High prompt cost and worse performance than zero-shot |
| GPT-4o Agent     | Massive improvement over its base zero-shot (+38.8%) | Still beaten by the base GPT-5 model |
| GPT-4o Zero-shot | Cheap and fast to execute         | Unacceptably low coverage (26.4%) for a complex app |
| GPT-4o Few-shot  | None evident                      | Worst performance (20.6%), misses 482 cases |
