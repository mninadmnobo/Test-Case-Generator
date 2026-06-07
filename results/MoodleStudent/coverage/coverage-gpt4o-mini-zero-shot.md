# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-4o-mini-zero-shot — 67 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 53 |
| GT cases not covered by GEN | 84 |
| **Overall coverage** | **38.7%** |
| GEN cases with no GT counterpart (extras) | ~19 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 7 | 5 | **58%** |
| Dashboard | 20 | 8 | 12 | **40%** |
| My Courses | 14 | 7 | 7 | **50%** |
| Course Page | 12 | 3 | 9 | **25%** |
| Participants | 15 | 6 | 9 | **40%** |
| Grades | 10 | 5 | 5 | **50%** |
| Assignment | 18 | 5 | 13 | **28%** |
| Activities | 11 | 4 | 7 | **36%** |
| Profile | 17 | 6 | 11 | **35%** |
| Logout | 8 | 2 | 6 | **25%** |
| **Total** | **137** | **53** | **84** | **38.7%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (5 missing)
- MS-LOGIN-002 Guest access
- MS-LOGIN-003 Login page elements displayed
- MS-LOGIN-005 Empty username
- MS-LOGIN-006 Empty password
- MS-LOGIN-012 Rapid double submission

### Dashboard (12 missing)
- MS-DASH-003 Timeline search filters content
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-008 Add block unavailable outside edit mode
- MS-DASH-013 Delete student dashboard block
- MS-DASH-016 Reset dashboard to default in edit mode
- MS-DASH-017 Delete Timeline block via block menu
- MS-DASH-019 Reset page to default completes without error
- MS-DASH-020 Attempt to filter events without selecting a course
- MS-DASH-012 Rapid edit-mode toggle
- MS-DASH-015 Timeline search with special characters
- MS-DASH-022 Search with minimum and maximum character lengths
- MS-DASH-023 Empty timeline dropdown filters handled gracefully

### My Courses (7 missing)
- MS-COURSES-006 Search no matching course
- MS-COURSES-008 Long symbol search
- MS-COURSES-010 Very long search query
- MS-COURSES-011 Search with special characters
- MS-COURSES-012 Rapid star action
- MS-COURSES-015 Invalid option in status
- MS-COURSES-016 Search with whitespaces and emojis

### Course Page (9 missing)
- MS-COURSE-001 Student course tabs displayed, Settings absent
- MS-COURSE-005 Open activity from course page
- MS-COURSE-006 Student cannot access Settings tab
- MS-COURSE-015 Save activity Name blank
- MS-COURSE-016 Open activity with missing name
- MS-COURSE-010 Rapid section toggles
- MS-COURSE-013 Rapid single-section toggle
- MS-COURSE-014 Collapse all after zero sections
- MS-COURSE-017 Add one more section than allowed

### Participants (9 missing)
- MS-PART-001 Participants table displayed
- MS-PART-002 Filter participants by name
- MS-PART-005 Student cannot enrol users
- MS-PART-014 Attempt to clear filters when no filters
- MS-PART-015 Attempt to view participant without selecting
- MS-PART-008 Filter no matching users
- MS-PART-011 Rapid First Name initial changes
- MS-PART-016 Checkbox selection caching
- MS-PART-017 Apply filter with empty condition

### Grades (5 missing)
- MS-GRADE-002 Expand course group
- MS-GRADE-005 Student cannot access full gradebook
- MS-GRADE-015 Modify grades access denied
- MS-GRADE-009 Rapid consecutive course-group toggle
- MS-GRADE-013 Whitespace-only feedback displays as empty

### Assignment (13 missing)
- MS-ASGN-001 Assignment details displayed
- MS-ASGN-004 Edit submission before deadline
- MS-ASGN-005 Remove submission when allowed
- MS-ASGN-006 View grade and feedback
- MS-ASGN-008 Edit submission blocked when teacher does not permit
- MS-ASGN-019 View submission when no submissions
- MS-ASGN-012 Resubmit after grading not allowed
- MS-ASGN-014 Edit submission exactly today
- MS-ASGN-015 Edit submission passed by one day
- MS-ASGN-016 Online text with whitespace
- MS-ASGN-017 File with special char
- MS-ASGN-018 Rapid re-submission via Back
- MS-ASGN-020 Text editor unicode fuzzing

### Activities (7 missing)
- MS-ACT-001 Activities overview displayed
- MS-ACT-003 Expand collapsed activity type
- MS-ACT-006 Hidden activity not visible
- MS-ACT-014 Attempt to navigate when no activities
- MS-ACT-009 Rapid double-click
- MS-ACT-010 Expand then immediately click
- MS-ACT-013 Cannot click in collapsed section

### Profile (11 missing)
- MS-PROFILE-001 Profile details displayed
- MS-PROFILE-002 Profile information cards displayed
- MS-PROFILE-003 Edit profile form opens
- MS-PROFILE-015 Data Retention Summary
- MS-PROFILE-016 Browser sessions report
- MS-PROFILE-017 Compose message
- MS-PROFILE-007 Cannot edit another user
- MS-PROFILE-018 First name blank update
- MS-PROFILE-020 HTML/XSS injection
- MS-PROFILE-014 Rapid re-submit
- MS-PROFILE-021 Rapid double-submit

### Logout (6 missing)
- MS-LOGOUT-002 Protected page requires re-auth
- MS-LOGOUT-003 Browser back after logout
- MS-LOGOUT-005 Double-click logout
- MS-LOGOUT-007 Logout in Tab A blocks Tab B
- MS-LOGOUT-008 Multi-tab simultaneous logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (2 extra)
- TC-006 (Login attempt with special characters in username and password)
- TC-007 (Login attempt with whitespace in username and password)

### Dashboard (1 extra)
- TC-012 (Select maximum time range)

### My Courses (1 extra)
- TC-020 (No courses displayed when not enrolled)

### Course Page (3 extra)
- TC-027 (Collapse a section)
- TC-030 (View course with maximum sections)
- TC-031 (View course with empty sections)

### Participants (3 extra)
- TC-036 (Apply filters with maximum length of input)
- TC-037 (Clear filters after applying them)
- TC-038 (Check participants list with no participants enrolled)

### Grades (2 extra)
- TC-040 (Access another student's grades)
- TC-044 (View grades with empty fields)

### Assignment (3 extra)
- TC-049 (Submission with maximum file size)
- TC-050 (Submission with maximum character limit in text editor)
- TC-051 (Submission with special characters)

### Activities (2 extra)
- TC-054 (Attempt to access Activities page without logging in)
- TC-055 (Click on a non-existent activity name)

### Profile (1 extra)
- TC-064 (Update profile with empty description)

### Logout (1 extra)
- TC-066 (Logout without being logged in)


