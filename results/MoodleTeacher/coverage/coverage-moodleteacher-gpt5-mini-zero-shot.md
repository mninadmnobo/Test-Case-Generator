# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v1.0  
**Generated Suite:** openai/gpt-5-mini-zero-shot â€” 260 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 154 |
| GT cases not covered by GEN | 66 |
| **Overall coverage** | **70.0%** |
| GEN cases with no GT counterpart (extras) | ~106 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 10 | 2 | **83.3%** |
| Dashboard | 13 | 10 | 3 | **76.9%** |
| Dashboard Edit Mode | 17 | 7 | 10 | **41.2%** |
| My Courses | 11 | 6 | 5 | **54.5%** |
| Course Page | 9 | 5 | 4 | **55.6%** |
| Course Edit Mode | 22 | 15 | 7 | **68.2%** |
| Assignment Creation | 19 | 13 | 6 | **68.4%** |
| Course Settings | 18 | 13 | 5 | **72.2%** |
| Participants | 17 | 13 | 4 | **76.5%** |
| Assignment Teacher View | 10 | 7 | 3 | **70.0%** |
| Assignment Submissions | 15 | 11 | 4 | **73.3%** |
| Grades | 16 | 11 | 5 | **68.8%** |
| Profile | 14 | 10 | 4 | **71.4%** |
| Profile Edit | 18 | 15 | 3 | **83.3%** |
| Logout | 9 | 8 | 1 | **88.9%** |
| **Total** | **220** | **154** | **66** | **70.0%** |

---

## Missing Scenarios (Gaps)

*Note: The following are verified gaps reflecting the exact test cases the LLM failed to generate.*

### Login (2 missing)
- MT-LOGIN-009 Rapid double login click
- MT-LOGIN-012 Very long username rejected without crash

### Dashboard (3 missing)
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-012 Navigate calendar to previous month removes current-date highlight
- MT-DASH-013 Rapid toggle of Timeline sort by date/courses

### Dashboard Edit Mode (10 missing)
- MT-DEDIT-004 Reset dashboard to default
- MT-DEDIT-006 Dashboard layout resets gracefully when toggled
- MT-DEDIT-007 Block drag handles visible
- MT-DEDIT-008 Collapse block in edit mode
- MT-DEDIT-010 Move a block via drag and drop
- MT-DEDIT-012 Hide a block from the dashboard
- MT-DEDIT-013 Access configure options on hidden block
- MT-DEDIT-014 Rapid consecutive toggle of Edit Mode
- MT-DEDIT-015 Special characters in block configuration
- MT-DEDIT-017 Concurrent block deletion cancels out cleanly

### My Courses (5 missing)
- MT-COURSES-005 My Courses blocked while unauthenticated
- MT-COURSES-006 Search with no matching course
- MT-COURSES-007 Hidden-course filter
- MT-COURSES-010 Very long search query (200+ chars) accepted without error
- MT-COURSES-011 Search with leading and trailing whitespace is trimmed

### Course Page (4 missing)
- MT-COURSE-005 Course page blocked while unauthenticated
- MT-COURSE-007 Hide Course Index sidebar
- MT-COURSE-008 Rapid section toggles
- MT-COURSE-009 Rapid double-click on activity link causes single navigation

### Course Edit Mode (7 missing)
- MT-CEDIT-010 Activity chooser search no results
- MT-CEDIT-011 Nested subsection creation
- MT-CEDIT-012 Rename section inline with empty text
- MT-CEDIT-016 Rapid consecutive clicks on hide/show activity toggle
- MT-CEDIT-018 Delete section containing activities warns of cascading delete
- MT-CEDIT-019 Rapid double-click on Add activity button
- MT-CEDIT-021 Bulk action bar clears selection when closed

### Assignment Creation (6 missing)
- MT-ACREATE-010 Disabled availability dates are not enforced
- MT-ACREATE-012 Due date earlier than Allow submissions from date
- MT-ACREATE-013 Cut-off date earlier than Due date
- MT-ACREATE-014 Negative maximum points blocked
- MT-ACREATE-016 Rapid double-click on Save and return to course
- MT-ACREATE-019 Maximum points boundary value

### Course Settings (5 missing)
- MT-CSET-009 End date earlier than start date
- MT-CSET-013 Very long Course Full Name (200+ chars)
- MT-CSET-014 Special characters and emoji in Course Short Name
- MT-CSET-016 Empty course summary
- MT-CSET-017 Very large file upload for Course Image

### Participants (4 missing)
- MT-PART-010 Enrol non-existent user rejected
- MT-PART-011 Rapid First Name initial changes
- MT-PART-012 Role assignment conflicts handled gracefully
- MT-PART-016 Delete enrolments for multiple users simultaneously

### Assignment Teacher View (3 missing)
- MT-ATVIEW-006 Filter by requires grading
- MT-ATVIEW-009 Assignment blocked while unauthenticated
- MT-ATVIEW-010 Very long assignment description does not break layout

### Assignment Submissions (4 missing)
- MT-ASUB-008 Search no matching student
- MT-ASUB-011 Bulk grading operations
- MT-ASUB-014 Student Name search with leading and trailing whitespace is trimmed
- MT-ASUB-015 Grade assignment that is already graded (override)

### Grades (5 missing)
- MT-GRADE-009 Rapid consecutive course-group toggle
- MT-GRADE-011 Maximum grade overflow prevention
- MT-GRADE-013 Whitespace-only feedback displays as empty
- MT-GRADE-014 Export grades to valid format
- MT-GRADE-015 Export grades to invalid format rejected

### Profile (4 missing)
- MT-PROFILE-009 Profile image broken URL handling
- MT-PROFILE-011 Invalid email link handling
- MT-PROFILE-013 Special characters in profile description
- MT-PROFILE-014 Profile data export boundary test

### Profile Edit (3 missing)
- MT-PEDIT-011 Empty required email field
- MT-PEDIT-016 Invalid timezone selection
- MT-PEDIT-018 Submit with no changes

### Logout (1 missing)
- MT-LOGOUT-009 Logout while multiple tabs open syncs session state

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### General (~5 extra types)
- Extra edge cases not mapped directly to GT scope
