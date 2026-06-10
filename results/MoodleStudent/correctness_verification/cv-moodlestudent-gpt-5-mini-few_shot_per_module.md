# Correctness Verification: MoodleStudent (gpt-5-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleStudent/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleStudent.md`  
**Total Generated Test Cases:** 133  
**Modules Covered:** Login (11), Dashboard (23), My Courses (15), Course Page (12), Participants (13), Grades (12), Assignment (11), Activities (11), Profile (15), Logout (10)

---

## Error Analysis

### A. Precondition Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** Valid preconditions based on few-shot examples.

---

### B. Test Steps Errors

**Total:** 2

- **TC IDs:** Assignment TC-009 *(Save for later)*, Profile TC-012 *(Upload picture)*
- *Reasoning:*
  - **Assignment TC-009:** Instructs clicking a "Save for later" button which is not present on the standard student submission form.
  - **Profile TC-012:** Instructs the student to upload a new profile picture. This is restricted in the student role scope for this functional description.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Participants TC-008 *(Hidden emails)*
- *Reasoning:*
  - **Participants TC-008:** Asserts that the student can view the email address of a peer who has set their email visibility to hidden.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Assignment TC-009 | Assignment | Test Steps |
| Profile TC-012 | Profile | Test Steps |
| Participants TC-008 | Participants | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 133
- **Total Test Cases with Errors:** 3
- **Total Correct Test Cases:** 130

**Overall Success Rate: 130 / 133 (97.74%)**

---

## Thesis Analysis

The GPT-5-mini Few-Shot Per Module approach achieved a **97.74% correctness rate** with 133 generated cases. It performed reliably but failed to match the ground truth volume of 137 cases, highlighting the limitations of few-shot prompting in expanding edge-case coverage without agentic iterations.
