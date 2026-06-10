# Correctness Verification: MoodleStudent (gpt-5-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleStudent/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleStudent.md`  
**Total Generated Test Cases:** 161  
**Modules Covered:** Login (11), Dashboard (20), My Courses (16), Course Page (13), Participants (18), Grades (16), Assignment (20), Activities (18), Profile (20), Logout (9)

---

## Error Analysis

### A. Precondition Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** All preconditions are valid within the system scope.

---

### B. Test Steps Errors

**Total:** 3

- **TC IDs:** Dashboard TC-015 *(Customize page)*, Grades TC-012 *(Export grades)*, Activities TC-010 *(Filter by due soon)*
- *Reasoning:*
  - **Dashboard TC-015:** Instructs the student to click "Customize this page". This is a Teacher/Admin feature; students cannot customize standard dashboard blocks.
  - **Grades TC-012:** Instructs the student to "Export grades as Excel". Students can view their user report but cannot export the gradebook.
  - **Activities TC-010:** Instructs the student to filter the activities list by "Due soon". This filter does not exist in the basic activities view.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Logout TC-007 *(Explicit timeout popup)*
- *Reasoning:*
  - **Logout TC-007:** Asserts that a "Session timeout" popup explicitely warns the user. Moodle relies on silent redirect to the login screen upon the next action.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Dashboard TC-015 | Dashboard | Test Steps |
| Grades TC-012 | Grades | Test Steps |
| Activities TC-010 | Activities | Test Steps |
| Logout TC-007 | Logout | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 161
- **Total Test Cases with Errors:** 4
- **Total Correct Test Cases:** 157

**Overall Success Rate: 157 / 161 (97.51%)**

---

## Thesis Analysis

The GPT-5-mini Zero-Shot Per Module approach achieved a strong **97.51% correctness rate** across 161 test cases. It hallucinated several role-based permissions (assuming students can export grades or customize dashboards). While it generated a respectable **157 valid tests**, it fell slightly short of the Agent approach in both absolute volume and accuracy rate.
