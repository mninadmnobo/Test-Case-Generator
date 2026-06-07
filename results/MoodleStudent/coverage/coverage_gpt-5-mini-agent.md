# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-5-mini — 168 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 116 |
| GT cases not covered by GEN | 21 |
| **Overall coverage** | **84.7%** |
| GEN cases with no GT counterpart (extras) | ~43 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 11 | 1 | **92%** |
| Dashboard | 20 | 15 | 5 | **75%** |
| My Courses | 14 | 12 | 2 | **86%** |
| Course Page | 12 | 9 | 3 | **75%** |
| Participants | 15 | 12 | 3 | **80%** |
| Grades | 10 | 10 | 0 | **100%** |
| Assignment | 18 | 17 | 1 | **94%** |
| Activities | 11 | 8 | 3 | **73%** |
| Profile | 17 | 16 | 1 | **94%** |
| Logout | 8 | 6 | 2 | **75%** |
| **Total** | **137** | **116** | **21** | **84.7%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (1 missing)
- MS-LOGIN-014 Submit with invalid username format containing special characters

### Dashboard (5 missing)
- MS-DASH-001 Dashboard page loads with user information visible
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-020 Attempt to filter events without selecting a course
- MS-DASH-021 Attempt to create a new event without entering required details
- MS-DASH-023 Empty timeline dropdown filters handled gracefully

### My Courses (2 missing)
- MS-COURSES-014 Leave the search field blank and submit
- MS-COURSES-015 Select an invalid option in the Status dropdown

### Course Page (3 missing)
- MS-COURSE-001 Student course tabs displayed and Settings tab absent
- MS-COURSE-006 Student cannot access Settings tab
- MS-COURSE-017 Attempt to add one more section than allowed

### Participants (3 missing)
- MS-PART-008 Filter no matching users
- MS-PART-014 Attempt to clear filters when no filters are applied
- MS-PART-015 Attempt to view participant profile without selecting a participant

### Grades (0 missing)
- None

### Assignment (1 missing)
- MS-ASGN-005 Remove submission when allowed

### Activities (3 missing)
- MS-ACT-006 Hidden activity not visible to student
- MS-ACT-007 Course with no activities
- MS-ACT-014 Attempt to navigate to an activity without any activities listed

### Profile (1 missing)
- MS-PROFILE-020 HTML/XSS injection in Profile Description is sanitised

### Logout (2 missing)
- MS-LOGOUT-006 Session timeout behaves like logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~1 extra types)
- "Lost password?" link disabled (GT treats it as a standard enabled link)

### Dashboard (~5 extra types)
- Block drag handles
- Block Configure/Move via menu
- Calendar import/export
- Keyboard accessibility for collapse
- All edit-mode-off negative cases (plus others, ~17 total)

### My Courses (~2 extra types)
- Summary layout switch
- Unauthenticated direct course URL

### Course Page (~4 extra types)
- Dual-role edit mode boundary
- Keyboard collapse activation
- Mixed-state collapse all
- Add-all-required-blank scenario (plus 1 other)

### Participants (~2 extra types)
- Last-name initial filter as separate case
- Student role summary case

### Grades (~4 extra types)
- Keyboard course group activation
- Special chars in feedback
- Precision/rounding display
- Student B blocked from Student A report

### Assignment (~4 extra types)
- Combined online-text + file upload
- Wrong-state action tests (view feedback when not graded, add submission when already submitted)
- Very long online text boundary (plus 2 others)
- View submission when no submissions (TC-014 asserts this perfectly, which was misidentified as missing in old report)

### Activities (~2 extra types)
- Add Row for new Activity Type
- Rapid toggle of multiple sections simultaneously

### Profile (~5 extra types)
- Blog entries
- Forum posts
- Forum discussions
- Learning plans links
- Zero-byte picture upload

### Logout (~0 extra types)
- None

