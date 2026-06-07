## Coverage Comparison

| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **80.0%** | 44              |
| 🥈 2 | GPT-5-mini  | Few-shot (Per module)     | **73.6%** | 58              |
| 🥉 3 | GPT-4o-mini | Agent                     | **71.8%** | 62              |
| 4    | GPT-5-mini  | Zero-shot (Per module)    | **70.0%** | 66              |
| 5    | GPT-4o-mini | Few-shot (Per module)     | **41.8%** | 128             |
| 6    | GPT-4o-mini | Zero-shot (Per module)    | **38.6%** | 135             |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| Agents outperform non-agents across both models  | **Agentic reasoning is critical for highest coverage** |
| Few-shot improves over zero-shot for both models | **Examples provide useful scaffolding for this application** |
| GPT-4o-mini Agent (71.8%) beats GPT-5-mini Zero-shot (70.0%) | **Agents can compensate for base model weaknesses** |
| GPT-5-mini Agent achieves highest coverage (80.0%) | **Most comprehensive test suite**           |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest overall coverage (80.0%), misses only 44 cases | Generates additional overhead with extra cases |
| GPT-5 Few-shot   | Solid balance between cost and coverage (73.6%) | Still misses a significant chunk of edge cases (58 missed) |
| GPT-4o Agent     | Excellent cost-to-performance ratio, beating base GPT-5 | Lower coverage ceiling than GPT-5 Agent |
| GPT-5 Zero-shot  | Good baseline without prompting overhead (70.0%) | Fails to explore complex edge cases |
| GPT-4o Few-shot  | Provides slight improvement over 4o zero-shot | Low overall coverage (41.8%) |
| GPT-4o Zero-shot | Cheapest and fastest to execute   | Lowest quality, misses 135 cases |
