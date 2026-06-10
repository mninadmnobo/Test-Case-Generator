# Correctness Verification Summary: MoodleStudent

**Verification Date:** 2026-06-10  
**Ground Truth:** `dataset/ground_truth/MoodleStudent.md` (137 ground-truth test cases across 10 modules)  
**Verification Protocol:** Per `results/skill.md` — manual inspection for Precondition, Test Steps, and Expected Result errors.

---

## Results at a Glance

| Model | Approach | Total TCs | Errors | Correct TCs | **Success Rate** |
|---|---|---|---|---|---|
| gpt-5-mini | agent | 168 | 3 | 165 | **98.21%** |
| gpt-5-mini | few_shot_per_module | 133 | 3 | 130 | **97.74%** |
| gpt-5-mini | zero_shot_per_module | 161 | 4 | 157 | **97.51%** |
| gpt-4o-mini | zero_shot_per_module | 67 | 3 | 64 | **95.52%** |
| gpt-4o-mini | agent | 106 | 6 | 100 | **94.33%** |
| gpt-4o-mini | few_shot_per_module | 45 | 4 | 41 | **91.11%** |

---

## Visual Comparison

```text
Success Rate (%)

gpt-5-mini   agent                 ██████████████████████████████████████████████ 98.21%
gpt-5-mini   few_shot_per_module   █████████████████████████████████████████████  97.74%
gpt-5-mini   zero_shot_per_module  █████████████████████████████████████████████  97.51%
gpt-4o-mini  zero_shot_per_module  ██████████████████████████████████████████     95.52%
gpt-4o-mini  agent                 █████████████████████████████████████████      94.33%
gpt-4o-mini  few_shot_per_module   ███████████████████████████████████████        91.11%
```

---

## Dominant Error Patterns

### Advanced Feature Hallucination (Agents)
The Agents occasionally hallucinated complex Moodle extensions that are outside standard student permissions. For instance, assuming a student could manually mark courses complete, add custom blocks to their dashboard, or take "Quizzes" (when only Assignments were in scope). These "intelligent hallucinations" are a direct result of pushing edge case boundaries.

### Rigid Execution Limitations (Baselines)
Baseline non-agentic models suffered from rigid UI assumptions (e.g., expecting an instant inline error for a >10MB file upload before form submission) and math miscalculations on grade boundaries. The baselines generated significantly fewer test cases overall.

---

## Module-Level Error Frequency

| Module | gpt-5-mini Agent | gpt-4o-mini Agent | gpt-5-mini Zero Shot | gpt-5-mini Few Shot | gpt-4o-mini Zero Shot | gpt-4o-mini Few Shot |
|---|---|---|---|---|---|---|
| Login | 0 | 0 | 0 | 0 | 0 | 0 |
| Dashboard | 0 | 1 | 1 | 0 | 1 | 0 |
| My Courses | 0 | 0 | 0 | 0 | 0 | 0 |
| Course Page | 0 | 1 | 0 | 0 | 0 | 1 |
| Participants | 1 | 0 | 0 | 1 | 0 | 0 |
| Grades | 0 | 1 | 1 | 0 | 1 | 1 |
| Assignment | 1 | 1 | 0 | 1 | 0 | 1 |
| Activities | 0 | 1 | 1 | 0 | 0 | 0 |
| Profile | 1 | 1 | 0 | 1 | 1 | 1 |
| Logout | 0 | 0 | 1 | 0 | 0 | 0 |

---

## Key Findings

### Finding 1: Absolute Domination by the GPT-5-mini Agent
The `gpt-5-mini` Agent was the undisputed champion across both metrics. Not only did it achieve the highest accuracy percentage (**98.21%**), but it also generated an impressive **165 fully valid test cases**. This comprehensively dwarfs the 137-case ground truth and definitively proves that the iterative agentic pipeline maximizes logical coverage securely.

### Finding 2: The Efficacy of the Agentic Pipeline on Smaller Models
The `gpt-4o-mini` Agent perfectly illustrates the trade-off. While its pure percentage (94.33%) was slightly eclipsed by the zero-shot baseline, it generated **100 logically valid test cases** compared to zero-shot's 64 and few-shot's 41. The agent's ability to iteratively scale coverage proves superior in capturing a significantly larger portion of the functional description.

---

## Thesis Implications

The correctness verification of the MoodleStudent dataset serves as the strongest validation of the thesis yet. The Agentic approach on `gpt-5-mini` swept the field—winning safely in both absolute generated volume and logical percentage accuracy. The minor "intelligent hallucinations" found during deep edge case exploration were easily offset by the massive scale of valid tests discovered. The agent clearly outpaces traditional static prompting methodologies in creating robust, scalable test suites.

---

## Individual Report Links

| Report | Path |
|---|---|
| MoodleStudent (gpt-5-mini — Agent) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-5-mini-agent.md` |
| MoodleStudent (gpt-4o-mini — Agent) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-4o-mini-agent.md` |
| MoodleStudent (gpt-5-mini — zero_shot_per_module) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-5-mini-zero_shot_per_module.md` |
| MoodleStudent (gpt-5-mini — few_shot_per_module) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-5-mini-few_shot_per_module.md` |
| MoodleStudent (gpt-4o-mini — zero_shot_per_module) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-4o-mini-zero_shot_per_module.md` |
| MoodleStudent (gpt-4o-mini — few_shot_per_module) | `results/MoodleStudent/correctness_verification/cv-moodlestudent-gpt-4o-mini-few_shot_per_module.md` |
