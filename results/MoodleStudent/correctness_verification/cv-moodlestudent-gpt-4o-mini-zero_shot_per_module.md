# Correctness Verification: MoodleStudent (gpt-4o-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleStudent/gpt-4o-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleStudent.md`  
**Total Generated Test Cases:** 67  
**Modules Covered:** Login (7), Dashboard (10), My Courses (8), Course Page (6), Participants (7), Grades (6), Assignment (7), Activities (6), Profile (7), Logout (3)

---

## Error Analysis

### A. Precondition Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** Valid preconditions.

---

### B. Test Steps Errors

**Total:** 2

- **TC IDs:** Profile TC-005 *(Change password)*, Dashboard TC-006 *(Drag course cards)*
- *Reasoning:*
  - **Profile TC-005:** Instructs changing the password. The spec does not grant password change capabilities to the student UI.
  - **Dashboard TC-006:** Instructs dragging and dropping course cards to reorder them, which is not a feature of the standard dashboard layout defined.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Grades TC-004 *(Grade prediction)*
- *Reasoning:*
  - **Grades TC-004:** Asserts the presence of a "Grade Prediction Tool", an enterprise hallucination.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Profile TC-005 | Profile | Test Steps |
| Dashboard TC-006 | Dashboard | Test Steps |
| Grades TC-004 | Grades | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 67
- **Total Test Cases with Errors:** 3
- **Total Correct Test Cases:** 64

**Overall Success Rate: 64 / 67 (95.52%)**

---

## Thesis Analysis

The GPT-4o-mini Zero-Shot Per Module approach achieved a **95.52% correctness rate**. However, it only generated a meager 67 total tests, yielding **64 valid cases**. This falls far below the 137-case ground truth and the agentic approach (100 valid cases).
