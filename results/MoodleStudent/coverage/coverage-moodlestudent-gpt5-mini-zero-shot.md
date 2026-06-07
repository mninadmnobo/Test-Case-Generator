# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-5-mini-zero-shot — 161 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 87 |
| GT cases not covered by GEN | 50 |
| **Overall coverage** | **63.5%** |
| GEN cases with no GT counterpart (extras) | ~61 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 8 | 4 | **67%** |
| Dashboard | 20 | 13 | 7 | **65%** |
| My Courses | 14 | 7 | 7 | **50%** |
| Course Page | 12 | 6 | 6 | **50%** |
| Participants | 15 | 11 | 4 | **73%** |
| Grades | 10 | 7 | 3 | **70%** |
| Assignment | 18 | 9 | 9 | **50%** |
| Activities | 11 | 7 | 4 | **64%** |
| Profile | 17 | 13 | 4 | **76%** |
| Logout | 8 | 6 | 2 | **75%** |
| **Total** | **137** | **87** | **50** | **63.5%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (4 missing)
- MS-LOGIN-005 Empty username
- MS-LOGIN-011 Username with leading/trailing whitespace
- MS-LOGIN-012 Rapid double submission
- MS-LOGIN-014 Submit with invalid username format

### Dashboard (7 missing)
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-009 Timeline search with no matches
- MS-DASH-012 Rapid edit-mode toggle
- MS-DASH-015 Timeline search with special characters
- MS-DASH-020 Attempt to filter events without selecting a course
- MS-DASH-022 Search with minimum and maximum character lengths
- MS-DASH-023 Empty timeline dropdown filters handled gracefully

### My Courses (7 missing)
- MS-COURSES-001 Student course cards displayed
- MS-COURSES-006 Search no matching course
- MS-COURSES-008 Long symbol search
- MS-COURSES-012 Rapid star action
- MS-COURSES-014 Leave search blank
- MS-COURSES-015 Invalid option in status
- MS-COURSES-016 Search with whitespaces and emojis

### Course Page (6 missing)
- MS-COURSE-006 Student cannot access Settings tab
- MS-COURSE-010 Rapid section toggles
- MS-COURSE-013 Rapid single-section toggle
- MS-COURSE-015 Save activity Name blank
- MS-COURSE-016 Open activity with missing name
- MS-COURSE-017 Add one more section than allowed

### Participants (4 missing)
- MS-PART-011 Rapid First Name initial changes
- MS-PART-014 Attempt to clear filters when no filters
- MS-PART-015 Attempt to view participant without selecting
- MS-PART-016 Checkbox selection caching

### Grades (3 missing)
- MS-GRADE-009 Rapid consecutive course-group toggle
- MS-GRADE-013 Whitespace-only feedback displays as empty
- MS-GRADE-014 Attempt to view grade details without auth

### Assignment (9 missing)
- MS-ASGN-005 Remove submission when allowed
- MS-ASGN-012 Resubmit after grading not allowed
- MS-ASGN-013 Submit when no input areas enabled
- MS-ASGN-014 Edit submission exactly today
- MS-ASGN-015 Edit submission passed by one day
- MS-ASGN-016 Online text with whitespace
- MS-ASGN-018 Rapid re-submission via Back
- MS-ASGN-019 View submission when no submissions
- MS-ASGN-020 Text editor unicode fuzzing

### Activities (4 missing)
- MS-ACT-009 Rapid double-click
- MS-ACT-010 Expand then immediately click
- MS-ACT-013 Cannot click in collapsed section
- MS-ACT-014 Attempt to navigate when no activities

### Profile (4 missing)
- MS-PROFILE-014 Rapid re-submit
- MS-PROFILE-016 Browser sessions report
- MS-PROFILE-020 HTML/XSS injection
- MS-PROFILE-021 Rapid double-submit

### Logout (2 missing)
- MS-LOGOUT-006 Session timeout behaves like logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (2 extra)
- TC-008 (Lost password link disabled)
- TC-010 (SQL-injection-like input)

### Dashboard (6 extra)
- TC-014 (Change sort order in Timeline)
- TC-017 (Calendar current month/highlight)
- TC-018 (Filter calendar by All courses)
- TC-020 (Create event on Feb 29)
- TC-022 (Navigate many months forward/back)
- TC-023 (Dates with events display event names inline)

### My Courses (5 extra)
- TC-043 (Search case-insensitive)
- TC-044 (Star multiple courses)
- TC-045 (Hidden course persists after refresh)
- TC-046 (Rapid toggle layout)
- TC-047 (Clicking course offline)

### Course Page (6 extra)
- TC-049 (Expand collapse individual section)
- TC-053 (Broken link error)
- TC-054 (Extremely long section name)
- TC-055 (Very large number of sections)
- TC-057 (Expand empty section)
- TC-059 (Keyboard accessibility)

### Participants (6 extra)
- TC-065 (Sort by name)
- TC-069 (Add conditions until UI limit)
- TC-070 (Filter special chars)
- TC-074 (Empty participants list)
- TC-075 (Very long names)
- TC-078 (Sorting duplicate names)

### Grades (7 extra)
- TC-084 (Cannot view another student's grades via URL)
- TC-086 (Zero-weight activity)
- TC-088 (Very large number of graded items)
- TC-090 (Boundary grades 0 and maximum)
- TC-092 (Missing range value handled gracefully)
- TC-093 (Feedback column displays feedback)
- TC-094 (Rounding consistent)

### Assignment (9 extra)
- TC-100 (Submit both text and file)
- TC-103 (Empty required online text)
- TC-104 (Disallowed file type)
- TC-105 (Exceeding size limit)
- TC-107 (Submit exactly at max size)
- TC-110 (Time remaining 0)
- TC-111 (Comments excessively long)
- TC-112 (Submission status summary shows correct)
- TC-113 (No due date configured)

### Activities (8 extra)
- TC-117 (Activity name shows parent section)
- TC-124 (Clicking deleted activity 404)
- TC-125 (Invalid activity id URL)
- TC-126 (Network/server failure)
- TC-129 (Special chars and Unicode)
- TC-130 (Large number of activities)
- TC-131 (Missing due date)
- TC-132 (Opens in same tab)

### Profile (7 extra)
- TC-137 (Course details links open course profiles)
- TC-140 (Upload valid picture)
- TC-145 (Unsupported image format)
- TC-146 (Oversized image)
- TC-150 (Timezone boundary)
- TC-151 (Hide email address)
- TC-152 (Image exactly at max size)

### Logout (5 extra)
- TC-154 (Direct /logout endpoint)
- TC-155 (Logout from deep page)
- TC-156 (Logout when no session)
- TC-157 (Network failure during logout)
- TC-161 (CSRF token missing)


