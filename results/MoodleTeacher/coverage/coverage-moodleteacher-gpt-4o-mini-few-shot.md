# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v1.0  
**Generated Suite:** openai/gpt-4o-mini-few-shot â€” 109 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 92 |
| GT cases not covered by GEN | 128 |
| **Overall coverage** | **41.8%** |
| GEN cases with no GT counterpart (extras) | ~17 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 7 | 5 | **58.3%** |
| Dashboard | 13 | 5 | 8 | **38.5%** |
| Dashboard Edit Mode | 17 | 6 | 11 | **35.3%** |
| My Courses | 11 | 5 | 6 | **45.5%** |
| Course Page | 9 | 5 | 4 | **55.6%** |
| Course Edit Mode | 22 | 9 | 13 | **40.9%** |
| Assignment Creation | 19 | 8 | 11 | **42.1%** |
| Course Settings | 18 | 7 | 11 | **38.9%** |
| Participants | 17 | 8 | 9 | **47.1%** |
| Assignment Teacher View | 10 | 6 | 4 | **60.0%** |
| Assignment Submissions | 15 | 7 | 8 | **46.7%** |
| Grades | 16 | 7 | 9 | **43.8%** |
| Profile | 14 | 6 | 8 | **42.9%** |
| Profile Edit | 18 | 4 | 14 | **22.2%** |
| Logout | 9 | 2 | 7 | **22.2%** |
| **Total** | **220** | **92** | **128** | **41.8%** |

---

## Missing Scenarios (Gaps)

*Note: Due to the exceptionally high number of gaps (128), only a representative sample of missing GT test cases is listed below.*

### Login (5 missing)
- MT-LOGIN-006 Empty password
- MT-LOGIN-007 Disabled lost-password link
- MT-LOGIN-009 Rapid double login click
- MT-LOGIN-010 Both fields empty shows simultaneous validation
- MT-LOGIN-012 Very long username rejected without crash

### Dashboard (8 missing)
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-007 Timeline search with no matches
- MT-DASH-008 Calendar year boundary
- MT-DASH-009 Very long timeline search
- MT-DASH-011 Timeline search with special characters and emoji accepted
- MT-DASH-012 Navigate calendar to previous month removes current-date highlight
- MT-DASH-013 Rapid toggle of Timeline sort by date/courses

### Dashboard Edit Mode (11 missing)
- MT-DEDIT-006 Dashboard layout resets gracefully when toggled
- MT-DEDIT-010 Move a block via drag and drop
- MT-DEDIT-012 Hide a block from the dashboard
- MT-DEDIT-014 Rapid consecutive toggle of Edit Mode
- MT-DEDIT-017 Concurrent block deletion cancels out cleanly

### Course Edit Mode (13 missing)
- MT-CEDIT-007 Edit controls hidden when edit mode is off
- MT-CEDIT-008 Add action with no tile selected
- MT-CEDIT-011 Nested subsection creation
- MT-CEDIT-015 Drag and drop a section to reorder
- MT-CEDIT-018 Delete section containing activities warns of cascading delete
- MT-CEDIT-020 Activity chooser search with special characters
- MT-CEDIT-022 Edit settings action opens activity form

### Assignment Creation (11 missing)
- MT-ACREATE-006 Assignment name empty
- MT-ACREATE-007 Oversized additional file
- MT-ACREATE-010 Disabled availability dates are not enforced
- MT-ACREATE-014 Negative maximum points blocked
- MT-ACREATE-015 Very long assignment description
- MT-ACREATE-018 Additional file with emoji filename

### Course Settings (11 missing)
- MT-CSET-004 Configure format, completion, groups, and tags
- MT-CSET-005 Course full name empty
- MT-CSET-009 End date earlier than start date
- MT-CSET-013 Very long Course Full Name (200+ chars)
- MT-CSET-014 Special characters and emoji in Course Short Name

### Participants (9 missing)
- MT-PART-006 Suspend user enrolment
- MT-PART-010 Enrol non-existent user rejected
- MT-PART-012 Role assignment conflicts handled gracefully
- MT-PART-016 Delete enrolments for multiple users simultaneously

### Assignment Submissions (8 missing)
- MT-ASUB-006 Filter by requires grading
- MT-ASUB-008 Search no matching student
- MT-ASUB-014 Student Name search with leading and trailing whitespace is trimmed

### Grades (9 missing)
- MT-GRADE-008 Setup gradebook categories
- MT-GRADE-011 Maximum grade overflow prevention
- MT-GRADE-015 Export grades to invalid format rejected

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### General (~5 extra types)
- Extra edge cases not mapped directly to GT scope
