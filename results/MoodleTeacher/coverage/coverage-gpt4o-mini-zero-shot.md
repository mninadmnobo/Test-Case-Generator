# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v1.0  
**Generated Suite:** openai/gpt-4o-mini-zero-shot â€” 97 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 85 |
| GT cases not covered by GEN | 135 |
| **Overall coverage** | **38.6%** |
| GEN cases with no GT counterpart (extras) | ~12 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 6 | 6 | **50.0%** |
| Dashboard | 13 | 5 | 8 | **38.5%** |
| Dashboard Edit Mode | 17 | 5 | 12 | **29.4%** |
| My Courses | 11 | 4 | 7 | **36.4%** |
| Course Page | 9 | 4 | 5 | **44.4%** |
| Course Edit Mode | 22 | 8 | 14 | **36.4%** |
| Assignment Creation | 19 | 6 | 13 | **31.6%** |
| Course Settings | 18 | 7 | 11 | **38.9%** |
| Participants | 17 | 8 | 9 | **47.1%** |
| Assignment Teacher View | 10 | 5 | 5 | **50.0%** |
| Assignment Submissions | 15 | 6 | 9 | **40.0%** |
| Grades | 16 | 6 | 10 | **37.5%** |
| Profile | 14 | 5 | 9 | **35.7%** |
| Profile Edit | 18 | 7 | 11 | **38.9%** |
| Logout | 9 | 3 | 6 | **33.3%** |
| **Total** | **220** | **85** | **135** | **38.6%** |

---

## Missing Scenarios (Gaps)

*Note: Due to the high number of gaps (135), only a representative sample of missing GT test cases is listed below.*

### Login (6 missing)
- MT-LOGIN-007 Disabled lost-password link
- MT-LOGIN-008 Failed login retains username
- MT-LOGIN-009 Rapid double login click
- MT-LOGIN-010 Both fields empty shows simultaneous validation
- MT-LOGIN-011 Username with leading/trailing whitespace retained after failed login
- MT-LOGIN-012 Very long username rejected without crash

### Dashboard (8 missing)
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-007 Timeline search with no matches
- MT-DASH-008 Calendar year boundary
- MT-DASH-009 Very long timeline search
- MT-DASH-010 Timeline empty state when selected range has zero activities
- MT-DASH-011 Timeline search with special characters and emoji accepted
- MT-DASH-012 Navigate calendar to previous month removes current-date highlight
- MT-DASH-013 Rapid toggle of Timeline sort by date/courses

### Dashboard Edit Mode (12 missing)
- MT-DEDIT-006 Dashboard layout resets gracefully when toggled
- MT-DEDIT-010 Move a block via drag and drop
- MT-DEDIT-012 Hide a block from the dashboard
- MT-DEDIT-014 Rapid consecutive toggle of Edit Mode
- MT-DEDIT-017 Concurrent block deletion cancels out cleanly

### Course Edit Mode (14 missing)
- MT-CEDIT-008 Move activity between sections
- MT-CEDIT-011 Delete an activity
- MT-CEDIT-015 Drag and drop a section to reorder
- MT-CEDIT-018 Delete section containing activities warns of cascading delete
- MT-CEDIT-020 Activity chooser search with special characters
- MT-CEDIT-022 Edit settings action opens activity form

### Assignment Creation (13 missing)
- MT-ACREATE-007 Oversized additional file
- MT-ACREATE-010 Disabled availability dates are not enforced
- MT-ACREATE-014 Negative maximum points blocked
- MT-ACREATE-015 Very long assignment description
- MT-ACREATE-018 Additional file with emoji filename

### Course Settings (11 missing)
- MT-CSET-005 Course full name empty
- MT-CSET-009 End date earlier than start date
- MT-CSET-013 Very long Course Full Name (200+ chars)
- MT-CSET-014 Special characters and emoji in Course Short Name

### Participants (9 missing)
- MT-PART-006 Suspend user enrolment
- MT-PART-010 Enrol non-existent user rejected
- MT-PART-012 Role assignment conflicts handled gracefully
- MT-PART-016 Delete enrolments for multiple users simultaneously

### Assignment Submissions (9 missing)
- MT-ASUB-006 Filter by requires grading
- MT-ASUB-008 Search no matching student
- MT-ASUB-014 Student Name search with leading and trailing whitespace is trimmed

### Grades (10 missing)
- MT-GRADE-008 Setup gradebook categories
- MT-GRADE-011 Maximum grade overflow prevention
- MT-GRADE-015 Export grades to invalid format rejected

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### General (~5 extra types)
- Extra edge cases not mapped directly to GT scope
