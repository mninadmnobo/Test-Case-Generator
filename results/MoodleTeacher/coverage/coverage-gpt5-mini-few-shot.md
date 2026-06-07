# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v1.0  
**Generated Suite:** openai/gpt-5-mini-few-shot â€” 202 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 162 |
| GT cases not covered by GEN | 58 |
| **Overall coverage** | **73.6%** |
| GEN cases with no GT counterpart (extras) | ~40 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 11 | 1 | **91.7%** |
| Dashboard | 13 | 11 | 2 | **84.6%** |
| Dashboard Edit Mode | 17 | 9 | 8 | **52.9%** |
| My Courses | 11 | 8 | 3 | **72.7%** |
| Course Page | 9 | 6 | 3 | **66.7%** |
| Course Edit Mode | 22 | 16 | 6 | **72.7%** |
| Assignment Creation | 19 | 14 | 5 | **73.7%** |
| Course Settings | 18 | 14 | 4 | **77.8%** |
| Participants | 17 | 14 | 3 | **82.4%** |
| Assignment Teacher View | 10 | 8 | 2 | **80.0%** |
| Assignment Submissions | 15 | 11 | 4 | **73.3%** |
| Grades | 16 | 12 | 4 | **75.0%** |
| Profile | 14 | 11 | 3 | **78.6%** |
| Profile Edit | 18 | 15 | 3 | **83.3%** |
| Logout | 9 | 2 | 7 | **22.2%** |
| **Total** | **220** | **162** | **58** | **73.6%** |

---

## Missing Scenarios (Gaps)

*Note: The following are verified gaps reflecting the exact test cases the LLM failed to generate.*

### Login (1 missing)
- MT-LOGIN-009 Rapid double login click

### Dashboard (2 missing)
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-013 Rapid toggle of Timeline sort by date/courses

### Dashboard Edit Mode (8 missing)
- MT-DEDIT-006 Dashboard layout resets gracefully when toggled
- MT-DEDIT-007 Block drag handles visible
- MT-DEDIT-008 Collapse block in edit mode
- MT-DEDIT-012 Hide a block from the dashboard
- MT-DEDIT-013 Access configure options on hidden block
- MT-DEDIT-014 Rapid consecutive toggle of Edit Mode
- MT-DEDIT-015 Special characters in block configuration
- MT-DEDIT-017 Concurrent block deletion cancels out cleanly

### My Courses (3 missing)
- MT-COURSES-005 My Courses blocked while unauthenticated
- MT-COURSES-007 Hidden-course filter
- MT-COURSES-010 Very long search query (200+ chars) accepted without error

### Course Page (3 missing)
- MT-COURSE-005 Course page blocked while unauthenticated
- MT-COURSE-008 Rapid section toggles
- MT-COURSE-009 Rapid double-click on activity link causes single navigation

### Course Edit Mode (6 missing)
- MT-CEDIT-010 Activity chooser search no results
- MT-CEDIT-011 Nested subsection creation
- MT-CEDIT-016 Rapid consecutive clicks on hide/show activity toggle
- MT-CEDIT-018 Delete section containing activities warns of cascading delete
- MT-CEDIT-019 Rapid double-click on Add activity button
- MT-CEDIT-021 Bulk action bar clears selection when closed

### Assignment Creation (5 missing)
- MT-ACREATE-010 Disabled availability dates are not enforced
- MT-ACREATE-012 Due date earlier than Allow submissions from date
- MT-ACREATE-014 Negative maximum points blocked
- MT-ACREATE-016 Rapid double-click on Save and return to course
- MT-ACREATE-019 Maximum points boundary value

### Course Settings (4 missing)
- MT-CSET-009 End date earlier than start date
- MT-CSET-013 Very long Course Full Name (200+ chars)
- MT-CSET-014 Special characters and emoji in Course Short Name
- MT-CSET-017 Very large file upload for Course Image

### Participants (3 missing)
- MT-PART-010 Enrol non-existent user rejected
- MT-PART-011 Rapid First Name initial changes
- MT-PART-012 Role assignment conflicts handled gracefully

### Assignment Teacher View (2 missing)
- MT-ATVIEW-009 Assignment blocked while unauthenticated
- MT-ATVIEW-010 Very long assignment description does not break layout

### Assignment Submissions (4 missing)
- MT-ASUB-008 Search no matching student
- MT-ASUB-011 Bulk grading operations
- MT-ASUB-014 Student Name search with leading and trailing whitespace is trimmed
- MT-ASUB-015 Grade assignment that is already graded (override)

### Grades (4 missing)
- MT-GRADE-009 Rapid consecutive course-group toggle
- MT-GRADE-011 Maximum grade overflow prevention
- MT-GRADE-013 Whitespace-only feedback displays as empty
- MT-GRADE-015 Export grades to invalid format rejected

### Profile (3 missing)
- MT-PROFILE-009 Profile image broken URL handling
- MT-PROFILE-011 Invalid email link handling
- MT-PROFILE-013 Special characters in profile description

### Profile Edit (3 missing)
- MT-PEDIT-011 Empty required email field
- MT-PEDIT-016 Invalid timezone selection
- MT-PEDIT-018 Submit with no changes

### Logout (7 missing)
- MT-LOGOUT-002 Browser back after logout redirects
- MT-LOGOUT-003 Logout from deep page
- MT-LOGOUT-004 Direct access to logout endpoint blocked
- MT-LOGOUT-005 Rapid double-click Logout
- MT-LOGOUT-007 Accessing Dashboard after logout redirects
- MT-LOGOUT-008 Multi-tab simultaneous logout
- MT-LOGOUT-009 Logout while multiple tabs open syncs session state

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### General (~5 extra types)
- Extra edge cases not mapped directly to GT scope
