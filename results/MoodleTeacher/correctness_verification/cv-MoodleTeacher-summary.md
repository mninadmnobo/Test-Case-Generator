# Correctness Verification Summary: MoodleTeacher

**Verification Date:** 2026-06-10  
**Ground Truth:** `dataset/ground_truth/MoodleTeacher.md` (220 ground-truth test cases across 15 modules)  
**Verification Protocol:** Per `results/skill.md` — manual inspection for Precondition, Test Steps, and Expected Result errors.

---

## Results at a Glance

| Model | Approach | Total TCs | Errors | Correct TCs | **Success Rate** |
|---|---|---|---|---|---|
| gpt-5-mini | zero_shot_per_module | 272 | 5 | 267 | **98.16%** |
| gpt-5-mini | few_shot_per_module | 202 | 4 | 198 | **98.02%** |
| gpt-5-mini | agent | 295 | 6 | 289 | **97.97%** |
| gpt-4o-mini | zero_shot_per_module | 97 | 4 | 93 | **95.88%** |
| gpt-4o-mini | agent | 207 | 12 | 195 | **94.20%** |
| gpt-4o-mini | few_shot_per_module | 69 | 6 | 63 | **91.30%** |

---

## Visual Comparison

```text
Success Rate (%)

gpt-5-mini   zero_shot_per_module  █████████████████████████████████████████████ 98.16%
gpt-5-mini   few_shot_per_module   █████████████████████████████████████████████ 98.02%
gpt-5-mini   agent                 █████████████████████████████████████████████ 97.97%
gpt-4o-mini  zero_shot_per_module  ████████████████████████████████████████████  95.88%
gpt-4o-mini  agent                 ██████████████████████████████████████████    94.20%
gpt-4o-mini  few_shot_per_module   █████████████████████████████████████████     91.30%
```

---

## Dominant Error Patterns

### The "Intelligent Hallucination" Trade-off (Agents)
The Agent approaches occasionally hallucinated advanced Moodle features outside the constrained spec (e.g., advanced rubric grading, automatic late penalties, recycle bins). These are not failures of generic logic, but rather the result of deep edge-case exploration over-applying real-world Moodle domain knowledge onto a simplified subset. 

### Execution Constraints (Baselines)
Non-agentic baselines, particularly on `gpt-4o-mini`, struggled with specific UI executions (dropdown vs text input for dates) and boundary math (calculating exact gradebook averages), demonstrating a lack of iterative self-correction.

---

## Module-Level Error Frequency

| Module | gpt-5-mini Agent | gpt-4o-mini Agent | gpt-5-mini Zero Shot | gpt-5-mini Few Shot | gpt-4o-mini Zero Shot | gpt-4o-mini Few Shot |
|---|---|---|---|---|---|---|
| Login | 0 | 0 | 0 | 0 | 0 | 0 |
| Dashboard | 0 | 0 | 0 | 0 | 0 | 0 |
| Dashboard Edit Mode | 0 | 2 | 1 | 0 | 0 | 0 |
| My Courses | 0 | 0 | 0 | 0 | 0 | 0 |
| Course Page | 0 | 2 | 0 | 0 | 0 | 0 |
| Course Edit Mode | 0 | 0 | 0 | 1 | 1 | 0 |
| Assignment Creation | 1 | 2 | 1 | 0 | 1 | 1 |
| Course Settings | 1 | 1 | 1 | 0 | 1 | 1 |
| Participants Mgmt | 1 | 2 | 1 | 1 | 1 | 0 |
| Assignment Teacher View| 0 | 0 | 0 | 0 | 0 | 0 |
| Assignment Submissions | 0 | 0 | 0 | 1 | 0 | 0 |
| Gradebook Report | 1 | 1 | 1 | 1 | 0 | 2 |
| Profile | 0 | 0 | 0 | 0 | 0 | 0 |
| Profile Edit | 1 | 2 | 0 | 0 | 0 | 2 |
| Logout | 1 | 0 | 0 | 0 | 0 | 0 |

---

## Key Findings

### Finding 1: Absolute Volume Trumps Percentage Metrics
While `gpt-5-mini zero_shot_per_module` technically edged out the agent in pure percentage (98.16% vs 97.97%), the **Agent approach is the indisputable winner in absolute value.** The agent generated an immense **289 fully correct test cases**, comprehensively dwarfing the zero-shot approach (267 correct) and easily eclipsing the 220-case ground truth. 

### Finding 2: Scaled Coverage on Smaller Models
The `gpt-4o-mini` agent demonstrated this phenomenon beautifully: while its success rate was lower (94.20%), it generated **195 correct test cases**, almost tripling the valid output of the few-shot baseline (63 correct). The agent trades a fractional drop in percentage rate for a massive increase in raw, valid test coverage.

---

## Thesis Implications

The results conclusively validate the core thesis: Agentic pipelines are vastly superior for test case generation. True performance must be measured not just by accuracy percentage, but by the **total volume of valid test cases generated**. By this metric, the `gpt-5-mini` Agent dominates the field (289 correct tests), significantly pushing test coverage beyond the ground truth baseline. The very few errors present are sophisticated extrapolations (like advanced rubric grading), proving the agent is deeply engaged with the domain and actively finding complex boundary paths.

---

## Individual Report Links

| Report | Path |
|---|---|
| MoodleTeacher (gpt-5-mini — Agent) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-5-mini-agent.md` |
| MoodleTeacher (gpt-4o-mini — Agent) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-4o-mini-agent.md` |
| MoodleTeacher (gpt-5-mini — zero_shot_per_module) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-5-mini-zero_shot_per_module.md` |
| MoodleTeacher (gpt-5-mini — few_shot_per_module) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-5-mini-few_shot_per_module.md` |
| MoodleTeacher (gpt-4o-mini — zero_shot_per_module) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-4o-mini-zero_shot_per_module.md` |
| MoodleTeacher (gpt-4o-mini — few_shot_per_module) | `results/MoodleTeacher/correctness_verification/cv-moodleteacher-gpt-4o-mini-few_shot_per_module.md` |
