# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-5-mini-few-shot — 133 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 84 |
| GT cases not covered by GEN | 53 |
| **Overall coverage** | **61.3%** |
| GEN cases with no GT counterpart (extras) | ~48 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 9 | 3 | **75%** |
| Dashboard | 20 | 14 | 6 | **70%** |
| My Courses | 14 | 7 | 7 | **50%** |
| Course Page | 12 | 6 | 6 | **50%** |
| Participants | 15 | 11 | 4 | **73%** |
| Grades | 10 | 7 | 3 | **70%** |
| Assignment | 18 | 6 | 12 | **33%** |
| Activities | 11 | 6 | 5 | **55%** |
| Profile | 17 | 12 | 5 | **71%** |
| Logout | 8 | 6 | 2 | **75%** |
| **Total** | **137** | **84** | **53** | **61.3%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (3 missing)
- MS-LOGIN-010 Both fields empty
- MS-LOGIN-012 Rapid double submission
- MS-LOGIN-014 Submit with invalid username format

### Dashboard (6 missing)
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-008 Add block unavailable outside edit mode
- MS-DASH-009 Timeline search with no matches
- MS-DASH-012 Rapid edit-mode toggle
- MS-DASH-020 Attempt to filter events without selecting a course
- MS-DASH-023 Empty timeline dropdown filters handled gracefully

### My Courses (7 missing)
- MS-COURSES-006 Search no matching course
- MS-COURSES-008 Long symbol search
- MS-COURSES-010 Very long search query
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

### Assignment (12 missing)
- MS-ASGN-001 Assignment details displayed
- MS-ASGN-005 Remove submission when allowed
- MS-ASGN-008 Edit submission blocked when teacher does not permit
- MS-ASGN-012 Resubmit after grading not allowed
- MS-ASGN-013 Submit when no input areas enabled
- MS-ASGN-014 Edit submission exactly today
- MS-ASGN-015 Edit submission passed by one day
- MS-ASGN-016 Online text with whitespace
- MS-ASGN-017 File with special char
- MS-ASGN-018 Rapid re-submission via Back
- MS-ASGN-019 View submission when no submissions
- MS-ASGN-020 Text editor unicode fuzzing

### Activities (5 missing)
- MS-ACT-006 Hidden activity not visible to student
- MS-ACT-009 Rapid double-click on assignment name
- MS-ACT-010 Expand then immediately click
- MS-ACT-013 Cannot click in collapsed section
- MS-ACT-014 Attempt to navigate when no activities

### Profile (5 missing)
- MS-PROFILE-013 Non-Latin Unicode in names
- MS-PROFILE-014 Rapid re-submit
- MS-PROFILE-015 Open Data Retention Summary
- MS-PROFILE-020 HTML/XSS injection
- MS-PROFILE-021 Rapid double-submit

### Logout (2 missing)
- MS-LOGOUT-006 Session timeout behaves like logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (2 extra)
- TC-010 (SQL-injection-like input)
- TC-011 (Lost password link disabled)

### Dashboard (8 extra)
- TC-015 (Change sort order)
- TC-016 (Current month highlighted)
- TC-017 (Filter calendar by specific course)
- TC-020 (Event names inline in grid)
- TC-027 (End date before start date)
- TC-031 (Max length title boundary)
- TC-032 (Navigate across year boundary)
- TC-033 (Filter course with no events)

### My Courses (8 extra)
- TC-041 (Change layout)
- TC-042 (Three-dot menu open/close)
- TC-043 (Search HTML/JS tags)
- TC-044 (Star offline)
- TC-045 (Zero enrolled empty state)
- TC-046 (Very large number of enrollments)
- TC-047 (Extremely long name truncated)
- TC-049 (Star then remove)

### Course Page (4 extra)
- TC-051 (Toggle single section open and closed)
- TC-058 (Extremely long section name)
- TC-059 (Large number of sections and collapse all)
- TC-061 (Long activity name visible/clickable)

### Participants (4 extra)
- TC-066 (Sort participants by last name)
- TC-071 (Alphabetical filter special chars)
- TC-072 (Sort by Last access 'Never')
- TC-073 (Extremely long string into filter)

### Grades (4 extra)
- TC-078 (View feedback for a graded item)
- TC-081 (Zero-weight item)
- TC-082 (Cannot view another student's grades by changing URL)
- TC-086 (Boundary grade values 0 and max)

### Assignment (5 extra)
- TC-089 (Submit using both text and file)
- TC-093 (Exceeds max upload size)
- TC-094 (Save submission when required content missing)
- TC-096 (Description long HTML/images)
- TC-097 (Submit max allowed number of files)

### Activities (3 extra)
- TC-102 (Access when not logged in)
- TC-107 (No due date displayed)
- TC-108 (Large number of activities)

### Profile (5 extra)
- TC-112 (Upload valid picture)
- TC-114 (Course details navigate to enrolled profiles)
- TC-119 (Unsupported image type)
- TC-122 (Extreme timezone boundary)
- TC-123 (Image exactly at max size)

### Logout (5 extra)
- TC-125 (Logout from within a course page)
- TC-127 (Footer secondary logout link)
- TC-129 (Submit assignment after logout in another tab)
- TC-130 (Expired session cookie)
- TC-133 (Cached content after logout)

