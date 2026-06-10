# Correctness Verification: MoodleTeacher (gpt-5-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleTeacher/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleTeacher.md`  
**Total Generated Test Cases:** 202  
**Modules Covered:** Login (12), Dashboard (16), Dashboard Edit Mode (12), My Courses (15), Course Page (10), Course Edit Mode and Activity Chooser (16), Assignment Creation (16), Course Settings (20), Participants Management (14), Assignment Teacher View (12), Assignment Submissions (14), Gradebook Grader Report (10), Profile (12), Profile Edit (15), Logout (8)

---

## Error Analysis

### A. Precondition Errors

**Total:** 1

- **TC IDs:** Participants Management TC-012 *(Cohorts assumption)*
- *Reasoning:*
  - **Participants Management TC-012:** Precondition assumes "Cohorts are enabled at the site level." Cohorts are not part of the defined functional scope for this assignment.

---

### B. Test Steps Errors

**Total:** 1

- **TC IDs:** Course Edit Mode and Activity Chooser TC-010 *(Drag and Drop)*
- *Reasoning:*
  - **Course Edit Mode and Activity Chooser TC-010:** Instructs the user to drag a file directly into the section header. While modern Moodle supports file drag-and-drop, the specific action of dragging into the section header to rename it is hallucinated.

---

### C. Expected Result Errors

**Total:** 2

- **TC IDs:** Gradebook Grader Report TC-008 *(Category Total Math)*, Assignment Submissions TC-013 *(File Size Limit Rejection)*
- *Reasoning:*
  - **Gradebook Grader Report TC-008:** Expected result miscalculates a category total based on the defined weights.
  - **Assignment Submissions TC-013:** Asserts an inline error for an 11MB file upload. The spec defines the boundary upload limit as 10MB, but the error behavior specified is a generic rejection rather than a specific inline field-level message.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Participants Management TC-012 | Participants Management | Precondition |
| Course Edit Mode and Activity Chooser TC-010 | Course Edit Mode and Activity Chooser | Test Steps |
| Gradebook Grader Report TC-008 | Gradebook Grader Report | Expected Result |
| Assignment Submissions TC-013 | Assignment Submissions | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 202
- **Total Test Cases with Errors:** 4
- **Total Correct Test Cases:** 198

**Overall Success Rate: 198 / 202 (98.02%)**

---

## Thesis Analysis

The GPT-5-mini Few-Shot Per Module approach achieved a strong **98.02% correctness rate** across 202 test cases. While the percentage is excellent, the total volume of generated test cases (202) is lower than the ground truth (220) and significantly lower than the Agent approach (295). This indicates that while few-shot prompting maintains high accuracy, it fails to dynamically expand the scope and discover deep edge cases the way an agentic pipeline can.
