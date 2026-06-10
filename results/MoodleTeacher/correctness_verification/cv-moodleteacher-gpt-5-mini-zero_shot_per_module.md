# Correctness Verification: MoodleTeacher (gpt-5-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/MoodleTeacher/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/MoodleTeacher.md`  
**Total Generated Test Cases:** 272  
**Modules Covered:** Login (12), Dashboard (24), Dashboard Edit Mode (14), My Courses (18), Course Page (15), Course Edit Mode and Activity Chooser (24), Assignment Creation (20), Course Settings (16), Participants Management (22), Assignment Teacher View (19), Assignment Submissions (22), Gradebook Grader Report (16), Profile (20), Profile Edit (18), Logout (12)

---

## Error Analysis

### A. Precondition Errors

**Total:** 3

- **TC IDs:** Course Settings TC-014 *(Guest Access enabled)*, Participants Management TC-018 *(Self Enrollment enabled)*, Gradebook Grader Report TC-011 *(Custom Scales enabled)*
- *Reasoning:*
  - **Course Settings TC-014, Participants Management TC-018, Gradebook Grader Report TC-011:** These tests invent complex Moodle configuration preconditions (guest access, self-enrollment plugins, custom grading scales) that exist in full Moodle but fall completely outside the provided functional description constraints.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** The zero-shot approach adhered strictly to generic navigational steps.

---

### C. Expected Result Errors

**Total:** 2

- **TC IDs:** Assignment Creation TC-015 *(Group Submission UI)*, Dashboard Edit Mode TC-012 *(Block Deletion Warning)*
- *Reasoning:*
  - **Assignment Creation TC-015:** Asserts that enabling group submissions reveals a complex sub-menu of group settings. This UI complexity is absent from the provided spec.
  - **Dashboard Edit Mode TC-012:** Asserts a specific Javascript confirmation modal appears when deleting a block. Moodle's block deletion flow differs from the hallucinated expected result.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Course Settings TC-014 | Course Settings | Precondition |
| Participants Management TC-018 | Participants Management | Precondition |
| Gradebook Grader Report TC-011 | Gradebook Grader Report | Precondition |
| Assignment Creation TC-015 | Assignment Creation | Expected Result |
| Dashboard Edit Mode TC-012 | Dashboard Edit Mode | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 272
- **Total Test Cases with Errors:** 5
- **Total Correct Test Cases:** 267

**Overall Success Rate: 267 / 272 (98.16%)**

---

## Thesis Analysis

The GPT-5-mini Zero-Shot Per Module approach achieved a **98.16% correctness rate** across 272 test cases. Although its percentage rate is fractionally higher than the Agent's, it generated fewer valid test cases (267 compared to the Agent's 289). The zero-shot model hallucinated several system-level configurations (Guest Access, Self Enrollment) rather than deeply exploring the valid boundaries of the allowed features. This confirms that while highly capable, zero-shot lacks the iterative depth achieved by the agentic pipeline.
