## Coverage Comparison

| Rank | Model       | Strategy                  | Coverage  | Missed GT Cases |
| ---- | ----------- | ------------------------- | --------- | --------------- |
| 🥇 1 | GPT-5-mini  | Agent                     | **88.8%** | 20              |
| 🥈 2 | GPT-5-mini  | Zero-shot (Per module)    | **87.8%** | 42              |
| 🥉 3 | GPT-5-mini  | Few-shot (Per module)     | **57.1%** | 149             |
| 4    | GPT-4o-mini | Agent                     | **45.5%** | 97              |
| 5    | GPT-4o-mini | Few-shot (Per module)     | **40.9%** | 205             |
| 6    | GPT-4o-mini | Zero-shot (Per module)    | **37.4%** | 217             |

## Key Findings

| Observation                                      | Conclusion                                  |
| ------------------------------------------------ | ------------------------------------------- |
| GPT-5-mini beats GPT-4o-mini in every setting    | **Model capability is the primary driver**  |
| Zero-shot (87.8%) outperformed Few-shot (57.1%) on GPT-5-mini | **Examples restricted generation scope**    |
| Agent loop helped GPT-4o-mini more (+8.1%) than GPT-5-mini (+1.0%) | **Agents compensate for weaker base models** |
| GPT-5-mini Agent achieves highest coverage (88.8%) | **Most complete test suite**                |
| GPT-5-mini Zero-shot matches Agent coverage closely | **Best cost-to-performance ratio**          |

---

## Strengths & Weaknesses

| Configuration    | Strength                          | Weakness                       |
| ---------------- | --------------------------------- | ------------------------------ |
| GPT-5 Agent      | Highest coverage, misses only 20 cases | Generates many extra/redundant tests |
| GPT-5 Zero-shot  | Incredible baseline performance (87.8%) | Misses some deep edge invariants |
| GPT-5 Few-shot   | More structured outputs           | Severe coverage drop from Zero-shot |
| GPT-4o Agent     | Best coverage for the 4o-mini tier | Still misses 97 core GT cases  |
| GPT-4o Few-shot  | Modest improvement over zero-shot | Very low overall coverage      |
| GPT-4o Zero-shot | Cheapest and fastest to run       | Lowest quality, misses 217 cases |
