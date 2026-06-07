# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v2.1  
**Generated Suite:** gpt-5-mini/agent/test-cases.json — 295 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 190 |
| GT cases not covered by GEN | 30 |
| **Overall coverage** | **86.4%** |
| Generated suite total cases | 295 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------:|--------:|-----------:|-----------:|
| Login | 12 | 11 | 1 | 91.7% |
| Dashboard | 13 | 12 | 1 | 92.3% |
| Dashboard — Edit Mode | 17 | 9 | 8 | 52.9% |
| My Courses | 11 | 11 | 0 | 100% |
| Course Page | 9 | 5 | 4 | 55.6% |
| Course Edit Mode and Activity Chooser | 22 | 22 | 0 | 100% |
| Assignment Creation | 19 | 16 | 3 | 84.2% |
| Course Settings | 18 | 17 | 1 | 94.4% |
| Participants Management | 17 | 17 | 0 | 100% |
| Assignment — Teacher View | 10 | 9 | 1 | 90.0% |
| Assignment Submissions | 15 | 14 | 1 | 93.3% |
| Gradebook — Grader Report | 16 | 14 | 2 | 87.5% |
| Profile | 14 | 14 | 0 | 100% |
| Profile Edit | 18 | 11 | 7 | 61.1% |
| Logout | 9 | 8 | 1 | 88.9% |
| **Total** | **220** | **190** | **30** | **86.4%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were not found in the generated suite (verified programmatically; 30 total):

### Login (1 missing)
- MT-LOGIN-012 Very long username rejected without crash

### Dashboard (1 missing)
- MT-DASH-002 Timeline block displays teaching actions

### Dashboard — Edit Mode (8 missing)
- MT-DEDIT-010 Move a block via drag and drop
- MT-DEDIT-005 Add block unavailable outside edit mode
- MT-DEDIT-006 Block menu unavailable outside edit mode
- MT-DEDIT-013 Move handle is hidden when edit mode is off
- MT-DEDIT-014 Reset dashboard button hidden when edit mode is off
- MT-DEDIT-015 Toggle edit mode off closes Add block page
- MT-DEDIT-016 Reset to default immediately after adding a block
- MT-DEDIT-017 Rapid Add block double-click

### Course Page (4 missing)
- MT-COURSE-001 Teacher course tabs displayed
- MT-COURSE-004 Course index navigation
- MT-COURSE-005 Course page blocked while unauthenticated
- MT-COURSE-007 Hide Course Index sidebar

### Assignment Creation (3 missing)
- MT-ACREATE-003 Configure availability dates
- MT-ACREATE-005 Configure grade and completion settings
- MT-ACREATE-010 Disabled availability dates are not enforced

### Course Settings (1 missing)
- MT-CSET-010 Maximum upload size option

### Assignment — Teacher View (1 missing)
- MT-ATVIEW-008 Expired due date

### Assignment Submissions (1 missing)
- MT-ASUB-005 Download submitted file

### Gradebook — Grader Report (2 missing)
- MT-GRADE-002 Switch report type
- MT-GRADE-008 Student cannot access grader report

### Profile Edit (7 missing)
- MT-PEDIT-003 Edit additional names and interests
- MT-PEDIT-007 Invalid email address
- MT-PEDIT-011 Submit with all required fields cleared
- MT-PEDIT-012 Missing email domain
- MT-PEDIT-013 File size exactly one byte over limit
- MT-PEDIT-010 Maximum valid picture size
- MT-PEDIT-018 Add and immediately remove repeating group item

### Logout (1 missing)
- MT-LOGOUT-006 Session timeout behaves like logout

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope (grouped by module; counts are approximate):

### Dashboard — Edit Mode (~16 extra types)
- Rapid repeated-next-month / multi-step calendar interaction variations and many additional Drag/Block permutations not enumerated in GT

### Course Edit Mode and Activity Chooser (~20 extra types)
- More extensive Activity Chooser tile-favorite toggles, persistence race conditions, and additional boundary/interleaving interaction tests beyond GT

### Course Settings (~11 extra types)
- Additional combinations of visibility/grouping toggles, many input-edge cases (emoji/special chars, long names) and re-submission timing tests

### Assignment Creation (~8 extra types)
- Extra interaction-edge tests for rapid resubmission and more boundary permutations for file/submission controls

### Participants Management (~6 extra types)
- Expanded Enrol dialog edge-cases, long-search/Unicode inputs and additional bulk-action timing variants

### Gradebook — Grader Report (~3 extra types)
- Extra long-comment and boundary/precision permutations beyond the GT list

### Profile (~4 extra types)
- Additional login-activity/time-offset scenarios and some input-edge permutations

### Profile Edit (~1 extra types)
- Minor extra input-edge/interaction checks (timing and whitespace permutations)

### Login (~2 extra types)
- Extra interaction-edge variants and rapid-click/edge behaviors

### My Courses (~1 extra types)
- One extra input-edge search/trim permutation

**Approximate total extras:** ~76 generated cases that extend GT with additional edge/interaction/boundary checks.

---
