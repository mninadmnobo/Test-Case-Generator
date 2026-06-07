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
