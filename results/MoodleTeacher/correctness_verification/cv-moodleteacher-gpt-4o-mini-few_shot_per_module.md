# Correctness Verification: MoodleTeacher (gpt-4o-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleTeacher/gpt-4o-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleTeacher.md`  
**Total Generated Test Cases:** 69  
**Modules Covered:** Login (5), Dashboard (6), Dashboard Edit Mode (5), My Courses (7), Course Page (5), Course Edit Mode and Activity Chooser (3), Assignment Creation (5), Course Settings (3), Participants Management (4), Assignment Teacher View (4), Assignment Submissions (6), Gradebook Grader Report (6), Profile (3), Profile Edit (4), Logout (3)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Assignment Creation TC-004 *(Invalid date format)*, Course Settings TC-002 *(Invalid date format)*
- *Reasoning:*
  - **Assignment Creation TC-004 & Course Settings TC-002:** The preconditions instruct the tester to enter a date format (MM-DD-YYYY) directly into the date fields. Moodle uses discrete dropdowns (Day, Month, Year) for dates, not a single text input.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** The steps follow the basic UI flow accurately.

---

### C. Expected Result Errors

**Total:** 4

- **TC IDs:** Gradebook Grader Report TC-004, TC-005 *(Grade boundary math)*, Profile Edit TC-003, TC-004 *(Upload limit rejection)*
- *Reasoning:*
  - **Gradebook Grader Report TC-004 & TC-005:** The expected result calculates incorrect average values for the grader report when testing boundary limits.
  - **Profile Edit TC-003 & TC-004:** Asserts that a specific inline validation message appears for a profile picture upload exceeding the limit. The system relies on a generic form rejection, not inline field validation.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Assignment Creation TC-004 | Assignment Creation | Precondition |
| Course Settings TC-002 | Course Settings | Precondition |
| Gradebook Grader Report TC-004 | Gradebook Grader Report | Expected Result |
| Gradebook Grader Report TC-005 | Gradebook Grader Report | Expected Result |
| Profile Edit TC-003 | Profile Edit | Expected Result |
| Profile Edit TC-004 | Profile Edit | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 69
- **Total Test Cases with Errors:** 6
- **Total Correct Test Cases:** 63

**Overall Success Rate: 63 / 69 (91.30%)**

---

## Thesis Analysis

The GPT-4o-mini Few-Shot Per Module approach generated a very limited pool of 69 test cases, achieving a **91.30% correctness rate**. The model struggled with basic constraints (like dropdown vs text input for dates) and math calculations. Generating only 63 valid test cases, it completely failed to approach the 220-case ground truth coverage, demonstrating the limitations of standard prompting on smaller models.
