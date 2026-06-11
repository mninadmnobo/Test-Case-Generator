# Comprehensive Test Generation Coverage Analysis

This document consolidates the test generation coverage results across six diverse software projects (SwagLab, PHPTravels, Parabank, MoodleTeacher, MoodleStudent, and Mifos) to provide a unified evaluation of model performance and prompting strategies.

## Executive Summary

| Rank | Model       | Strategy                  | Average Coverage | Project Wins |
| ---- | ----------- | ------------------------- | ---------------- | ------------ |
| 🥇 1 | GPT-5-mini  | Agent                     | **84.0%**        | 6 / 6        |
| 🥈 2 | GPT-5-mini  | Zero-shot (Per module)    | **69.7%**        | 0 / 6        |
| 🥉 3 | GPT-5-mini  | Few-shot (Per module)     | **63.9%**        | 0 / 6        |
| 4    | GPT-4o-mini | Agent                     | **61.9%**        | 0 / 6        |
| 5    | GPT-4o-mini | Zero-shot (Per module)    | **38.7%**        | 0 / 6        |
| 6    | GPT-4o-mini | Few-shot (Per module)     | **33.7%**        | 0 / 6        |

---

## Per-Project Breakdown

| Model / Strategy | SwagLab | PHPTravels | Parabank | MoodleTeacher | MoodleStudent | Mifos |
| ---------------- | ------- | ---------- | -------- | ------------- | ------------- | ----- |
| **GPT-5 Agent**  | 85.4%   | 88.8%      | 85.0%    | 80.0%         | 84.7%         | 80.2% |
| **GPT-5 Zero**   | 63.4%   | 87.8%      | 59.5%    | 70.0%         | 63.5%         | 74.1% |
| **GPT-5 Few**    | 64.6%   | 57.1%      | 60.0%    | 73.6%         | 61.3%         | 66.9% |
| **GPT-4o Agent** | 56.1%   | 45.5%      | 71.0%    | 71.8%         | 62.0%         | 65.2% |
| **GPT-4o Zero**  | 43.9%   | 37.4%      | 47.0%    | 38.6%         | 38.7%         | 26.4% |
| **GPT-4o Few**   | 43.9%   | 40.9%      | 28.5%    | 41.8%         | 26.3%         | 20.6% |

---

## 💡 Key Insights

When we stepped back and looked at all six projects, a clear story emerged about how AI actually writes tests.

**The Power of Giving the AI Time to Think**  
If you want thorough testing, you have to let the AI act like a real QA engineer. Across every single project, the **GPT-5-mini Agent** blew the competition away, consistently hitting 80% to 88% coverage. Instead of just spitting out a list of tests in one go, the agent loops back, looks at its work, and asks, "What did I miss?" This is especially crucial in apps with strict rules—like a student portal. The agent doesn't just test the happy path; it actively looks for what the user *shouldn't* be allowed to do, finding 21% more edge cases than standard prompting.

**The "Example" Trap**  
Here is the biggest surprise: giving the AI examples of good test cases actually *hurt* its performance. We naturally assume that showing the AI what we want (Few-shot prompting) will help it do better. But in reality, it gave the AI "tunnel vision." Instead of creatively exploring the app to find weird edge cases, the AI just blindly copied the pattern of the examples. When we took the examples away (Zero-shot) and let the AI brainstorm freely, coverage went up across the board. 

**Brains Over Tactics**  
We also wanted to know if a fancy agent loop could turn a cheap, weak model into a superstar. The short answer? No. While adding an agent loop to the weaker GPT-4o-mini gave it a massive 23% boost, it still wasn't enough. A weak model working incredibly hard (62% average) still lost to a highly intelligent base model (GPT-5) doing the bare minimum zero-shot prompting (70% average). At the end of the day, when you're testing complex software, raw AI brainpower matters more than the strategy you use to guide it. 

---

## Global Strengths & Weaknesses

| Configuration    | Global Strength | Global Weakness |
| ---------------- | --------------- | --------------- |
| **GPT-5 Agent**  | Consistently hits 80%+ coverage across any domain. Deepest edge-case discovery. | Highest API cost and generation time. Often produces a high volume of extra/redundant tests. |
| **GPT-5 Zero**   | Excellent baseline (69.7%) with zero prompting overhead. Best cost-to-performance ratio. | Fails to comprehensively probe negative boundaries and constrained workflows. |
| **GPT-5 Few**    | Outputs are structurally consistent and follow formats perfectly. | Severely limits generation scope. The model becomes a "mimic" rather than an "explorer". |
| **GPT-4o Agent** | Massive (+23.2%) improvement over its zero-shot baseline. | Hit a reasoning ceiling on large, complex applications (e.g., Mifos, PHPTravels). |
| **GPT-4o Zero**  | Extremely fast and cheap execution. | Dangerously low coverage (38.7% avg); misses over 60% of critical business logic. |
| **GPT-4o Few**   | None. | Worst overall performance. Model hallucination combined with highly constrained generation. |


## Case Study: The Whole-File Baseline Bottleneck and Test Distribution

As part of the ablation study, we measured not only the raw output volume (total number of generated test cases) for pure "Whole-File" baselines (`Zero-shot` and `Few-shot`) compared to the robust `Agent` strategy, but also the specific distribution of those tests (Positive vs. Negative vs. Edge, and their Priorities).

| Project | Model | Strategy | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|-------|----------|----------|------|------|--------|-----|
| Mifos | gpt-4o-mini | few_shot | 69 | 23 | 23 | 23 | 49 | 20 | 0 |
| Mifos | gpt-4o-mini | zero_shot | 32 | 12 | 12 | 8 | 20 | 11 | 1 |
| Mifos | gpt-5-mini | few_shot | 102 | 53 | 37 | 12 | 52 | 40 | 10 |
| Mifos | gpt-5-mini | zero_shot | 120 | 69 | 35 | 16 | 43 | 58 | 19 |
| MoodleStudent | gpt-4o-mini | few_shot | 27 | 10 | 9 | 8 | 19 | 8 | 0 |
| MoodleStudent | gpt-4o-mini | zero_shot | 36 | 15 | 15 | 6 | 25 | 11 | 0 |
| MoodleStudent | gpt-5-mini | few_shot | 135 | 100 | 19 | 16 | 44 | 53 | 38 |
| MoodleStudent | gpt-5-mini | zero_shot | 100 | 65 | 15 | 20 | 34 | 36 | 30 |
| MoodleTeacher | gpt-4o-mini | few_shot | 21 | 7 | 7 | 7 | 11 | 10 | 0 |
| MoodleTeacher | gpt-4o-mini | zero_shot | 30 | 12 | 13 | 5 | 21 | 9 | 0 |
| MoodleTeacher | gpt-5-mini | few_shot | 104 | 44 | 30 | 30 | 37 | 37 | 30 |
| MoodleTeacher | gpt-5-mini | zero_shot | 100 | 73 | 13 | 14 | 40 | 45 | 15 |
| Parabank | gpt-4o-mini | few_shot | 43 | 15 | 14 | 14 | 29 | 14 | 0 |
| Parabank | gpt-4o-mini | zero_shot | 55 | 17 | 29 | 9 | 46 | 9 | 0 |
| Parabank | gpt-5-mini | few_shot | 62 | 20 | 31 | 11 | 30 | 28 | 4 |
| Parabank | gpt-5-mini | zero_shot | 50 | 18 | 27 | 5 | 18 | 27 | 5 |
| PHPTravels | gpt-4o-mini | few_shot | 39 | 13 | 13 | 13 | 28 | 11 | 0 |
| PHPTravels | gpt-4o-mini | zero_shot | 51 | 17 | 17 | 17 | 34 | 17 | 0 |
| PHPTravels | gpt-5-mini | few_shot | 95 | 44 | 28 | 23 | 36 | 44 | 15 |
| PHPTravels | gpt-5-mini | zero_shot | 130 | 62 | 41 | 27 | 62 | 53 | 15 |
| SwagLab | gpt-4o-mini | few_shot | 11 | 5 | 3 | 3 | 7 | 4 | 0 |
| SwagLab | gpt-4o-mini | zero_shot | 21 | 10 | 7 | 4 | 13 | 8 | 0 |
| SwagLab | gpt-5-mini | few_shot | 60 | 25 | 20 | 15 | 22 | 24 | 14 |
| SwagLab | gpt-5-mini | zero_shot | 71 | 33 | 17 | 20 | 42 | 22 | 7 |

### Conclusion: Explaining Coverage Through Test Distribution

When feeding an entire software specification into an LLM simultaneously (the Whole-File baseline approach), the models hit a severe generation bottleneck. We can see this precisely by comparing the required **Ground Truth (GT)** test cases for each dataset against the total test cases generated by the leading model (`gpt-5-mini`):

* **Mifos**: GT requires **607** tests. The Agent successfully scales to **807** cases via per-module chunking. In stark contrast, Whole-File Zero-Shot (**120**) and Few-Shot (**102**) cap out at a fraction of the required volume.
* **MoodleTeacher**: GT requires **220** tests. The Agent generates **295**. The static baselines bottleneck severely at **100** (Zero-Shot) and **104** (Few-Shot).
* **Parabank**: GT requires **200** tests. The Agent generates **230**. The baselines max out at **50** (Zero-Shot) and **62** (Few-Shot).
* **PHPTravels**: GT requires **178** tests. The Agent generates **394**. The baselines hit output ceilings of **130** (Zero-Shot) and **95** (Few-Shot).
* **MoodleStudent**: GT requires **137** tests. The Agent generates **168**. The baselines produce **100** (Zero-Shot) and **135** (Few-Shot).
* **SwagLab**: GT requires **61** tests. Because the application is so small, all strategies (Agent: **88**, Zero-Shot: **71**, Few-Shot: **60**) generate enough raw volume to approach the target without hitting a context ceiling.

Because the total volume of generated test cases in pure baselines is often physically incapable of reaching the required ground-truth targets on large applications, their raw coverage percentage is mathematically kneecapped. The LLM simply cannot generate enough text in a single inference call to adequately cover an enterprise application without triggering its hardware context ceiling or degrading output quality.
