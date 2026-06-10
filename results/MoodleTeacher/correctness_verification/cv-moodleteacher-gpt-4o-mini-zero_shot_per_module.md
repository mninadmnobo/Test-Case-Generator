# Correctness Verification: MoodleTeacher (gpt-4o-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleTeacher/gpt-4o-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleTeacher.md`  
**Total Generated Test Cases:** 97  
**Modules Covered:** Login (7), Dashboard (9), Dashboard Edit Mode (6), My Courses (8), Course Page (5), Course Edit Mode and Activity Chooser (6), Assignment Creation (5), Course Settings (5), Participants Management (7), Assignment Teacher View (7), Assignment Submissions (9), Gradebook Grader Report (7), Profile (7), Profile Edit (6), Logout (3)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Course Settings TC-004 *(Course Format)*, Participants Management TC-005 *(Role Assumption)*
- *Reasoning:*
  - **Course Settings TC-004:** Assumes the user can change the course format to "Social Format". This format is not in the scope of the provided functional description.
  - **Participants Management TC-005:** Assumes the teacher can assign the "Manager" role to a student. Teachers can only assign Non-editing Teacher or Student roles.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** The zero-shot steps correctly navigate standard Moodle flows.

---

### C. Expected Result Errors

**Total:** 2

- **TC IDs:** Assignment Creation TC-003 *(Max File Size)*, Course Edit Mode TC-004 *(Activity Deletion)*
- *Reasoning:*
  - **Assignment Creation TC-003:** Asserts that submitting a file larger than 10MB triggers an immediate inline warning. The system rejects it upon form submission, not instantly inline.
  - **Course Edit Mode TC-004:** Asserts that deleting an activity moves it to a "Recycle Bin". The Recycle Bin is an optional plugin/feature not included in the core functional spec.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Course Settings TC-004 | Course Settings | Precondition |
| Participants Management TC-005 | Participants Management | Precondition |
| Assignment Creation TC-003 | Assignment Creation | Expected Result |
| Course Edit Mode TC-004 | Course Edit Mode | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 97
- **Total Test Cases with Errors:** 4
- **Total Correct Test Cases:** 93

**Overall Success Rate: 93 / 97 (95.88%)**

---

## Thesis Analysis

The GPT-4o-mini Zero-Shot Per Module approach achieved a strong **95.88% correctness rate** across 97 test cases. The few errors produced were typical LLM assumptions about full system features (like Recycle Bins or advanced roles). While the percentage rate is high, the model only generated **93 logically valid test cases**, meaning it captured less than half of the ground truth coverage (220 tests). It lacked the exploratory depth of the agentic pipeline.
