## Coverage Comparison

| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **85.4%** | 12              |
| 🥈 2 | GPT-5-mini  | Few-shot (Per module)     | **64.6%** | 29              |
| 🥉 3 | GPT-5-mini  | Zero-shot (Per module)    | **63.4%** | 30              |
| 4    | GPT-4o-mini | Agent                     | **56.1%** | 36              |
| 5    | GPT-4o-mini | Few-shot (Per module)     | **43.9%** | 46              |
| 6    | GPT-4o-mini | Zero-shot (Per module)    | **43.9%** | 46              |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| GPT-5 beats GPT-4o in every setting              | **Model quality matters a lot**             |
| Few-shot improves only ~1% over zero-shot        | **Examples add little value**               |
| Agent improves 12–21% over non-agent             | **Agentic reasoning is the biggest factor** |
| GPT-5 Agent misses only 12/82 GT tests           | **Most complete suite**                     |
| GPT-5 Agent generates useful advanced edge cases | **Best QA thinking**                        |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest coverage, best edge cases | More extra tests               |
| GPT-5 Few-shot   | Good balance                      | Large coverage drop from Agent |
| GPT-5 Zero-shot  | Simple, decent coverage           | Misses many workflow cases     |
| GPT-4o Agent     | Better than other 4o modes        | Still misses 36 GT cases       |
| GPT-4o Few-shot  | Cheap                             | Low coverage                   |
| GPT-4o Zero-shot | Cheapest                          | Lowest quality                 |
