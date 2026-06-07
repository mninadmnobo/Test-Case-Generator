# Test Coverage Report

**Ground Truth:** MoodleTeacher GT v1.0  
**Generated Suite:** openai/gpt-5-mini-agent â€” 295 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 176 |
| GT cases not covered by GEN | 44 |
| **Overall coverage** | **80.0%** |
| GEN cases with no GT counterpart (extras) | ~119 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 11 | 1 | **91.7%** |
| Dashboard | 13 | 11 | 2 | **84.6%** |
| Dashboard Edit Mode | 17 | 10 | 7 | **58.8%** |
| My Courses | 11 | 10 | 1 | **90.9%** |
| Course Page | 9 | 7 | 2 | **77.8%** |
| Course Edit Mode | 22 | 18 | 4 | **81.8%** |
| Assignment Creation | 19 | 15 | 4 | **78.9%** |
| Course Settings | 18 | 15 | 3 | **83.3%** |
| Participants | 17 | 13 | 4 | **76.5%** |
| Assignment Teacher View | 10 | 9 | 1 | **90.0%** |
| Assignment Submissions | 15 | 13 | 2 | **86.7%** |
| Grades | 16 | 13 | 3 | **81.3%** |
| Profile | 14 | 13 | 1 | **92.9%** |
| Profile Edit | 18 | 15 | 3 | **83.3%** |
| Logout | 9 | 3 | 6 | **33.3%** |
| **Total** | **220** | **176** | **44** | **80.0%** |

---

## Missing Scenarios (Gaps)

*Note: The following are verified gaps reflecting the exact test cases the Agent failed to generate.*

### Login (1 missing)
- MT-LOGIN-009 Rapid double login click

### Dashboard (2 missing)
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-013 Rapid toggle of Timeline sort by date/courses

### Dashboard Edit Mode (7 missing)
- MT-DEDIT-006 Dashboard layout resets gracefully when toggled
- MT-DEDIT-007 Block drag handles visible
- MT-DEDIT-008 Collapse block in edit mode
- MT-DEDIT-012 Hide a block from the dashboard
- MT-DEDIT-013 Access configure options on hidden block
- MT-DEDIT-014 Rapid consecutive toggle of Edit Mode
- MT-DEDIT-017 Concurrent block deletion cancels out cleanly

### My Courses (1 missing)
- MT-COURSES-005 My Courses blocked while unauthenticated

### Course Page (2 missing)
- MT-COURSE-008 Rapid section toggles
- MT-COURSE-009 Rapid double-click on activity link causes single navigation

### Course Edit Mode (4 missing)
- MT-CEDIT-011 Nested subsection creation
- MT-CEDIT-016 Rapid consecutive clicks on hide/show activity toggle
- MT-CEDIT-018 Delete section containing activities warns of cascading delete
- MT-CEDIT-019 Rapid double-click on Add activity button

### Assignment Creation (4 missing)
- MT-ACREATE-010 Disabled availability dates are not enforced
- MT-ACREATE-014 Negative maximum points blocked
- MT-ACREATE-016 Rapid double-click on Save and return to course
- MT-ACREATE-019 Maximum points boundary value

### Course Settings (3 missing)
- MT-CSET-009 End date earlier than start date
- MT-CSET-013 Very long Course Full Name (200+ chars)
- MT-CSET-017 Very large file upload for Course Image

### Participants (4 missing)
- MT-PART-006 Suspend user enrolment
- MT-PART-011 Rapid First Name initial changes
- MT-PART-012 Role assignment conflicts handled gracefully
- MT-PART-016 Delete enrolments for multiple users simultaneously

### Assignment Teacher View (1 missing)
- MT-ATVIEW-009 Assignment blocked while unauthenticated

### Assignment Submissions (2 missing)
- MT-ASUB-008 Search no matching student
- MT-ASUB-011 Bulk grading operations

### Grades (3 missing)
- MT-GRADE-009 Rapid consecutive course-group toggle
- MT-GRADE-011 Maximum grade overflow prevention
- MT-GRADE-015 Export grades to invalid format rejected

### Profile (1 missing)
- MT-PROFILE-009 Profile image broken URL handling

### Profile Edit (3 missing)
- MT-PEDIT-011 Empty required email field
- MT-PEDIT-016 Invalid timezone selection
- MT-PEDIT-018 Submit with no changes

### Logout (6 missing)
- MT-LOGOUT-002 Browser back after logout redirects
- MT-LOGOUT-003 Logout from deep page
- MT-LOGOUT-004 Direct access to logout endpoint blocked
- MT-LOGOUT-005 Rapid double-click Logout
- MT-LOGOUT-007 Accessing Dashboard after logout redirects
- MT-LOGOUT-009 Logout while multiple tabs open syncs session state

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### General (~5 extra types)
- Extra edge cases not mapped directly to GT scope
