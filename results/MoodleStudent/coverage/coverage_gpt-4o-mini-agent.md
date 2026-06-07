# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-4o-mini — 106 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 85 |
| GT cases not covered by GEN | 52 |
| **Overall coverage** | **62.0%** |
| GEN cases with no GT counterpart (extras) | ~21 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 12 | 0 | **100%** |
| Dashboard | 20 | 13 | 7 | **65%** |
| My Courses | 14 | 9 | 5 | **64%** |
| Course Page | 12 | 6 | 6 | **50%** |
| Participants | 15 | 10 | 5 | **67%** |
| Grades | 10 | 5 | 5 | **50%** |
| Assignment | 18 | 9 | 9 | **50%** |
| Activities | 11 | 7 | 4 | **64%** |
| Profile | 17 | 11 | 6 | **65%** |
| Logout | 8 | 3 | 5 | **38%** |
| **Total** | **137** | **85** | **52** | **62.0%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (0 missing)
- None

### Dashboard (7 missing)
- MS-DASH-001 Dashboard page loads with user info
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-008 Add block unavailable outside edit mode
- MS-DASH-012 Rapid edit-mode toggle
- MS-DASH-013 Delete student dashboard block
- MS-DASH-015 Timeline search with special characters
- MS-DASH-017 Delete Timeline block via block menu

### My Courses (5 missing)
- MS-COURSES-001 Student course cards displayed
- MS-COURSES-002 Filter and search controls
- MS-COURSES-003 Open course from card
- MS-COURSES-006 Search no matching course
- MS-COURSES-007 Hidden-course filter

### Course Page (6 missing)
- MS-COURSE-001 Student course tabs displayed, Settings absent
- MS-COURSE-006 Student cannot access Settings tab
- MS-COURSE-007 Student cannot enable course edit mode
- MS-COURSE-010 Rapid section toggles
- MS-COURSE-013 Rapid single-section toggle
- MS-COURSE-016 Open activity with missing name

### Participants (5 missing)
- MS-PART-003 Alphabetical filters
- MS-PART-005 Student cannot enrol users
- MS-PART-006 Student cannot edit/remove roles
- MS-PART-008 Filter no matching users
- MS-PART-013 Student role enrollment features not visible

### Grades (5 missing)
- MS-GRADE-005 Student cannot access full gradebook
- MS-GRADE-009 Rapid consecutive course-group toggle
- MS-GRADE-011 Long feedback text truncated
- MS-GRADE-013 Whitespace-only feedback displays as empty
- MS-GRADE-015 Modify grades access denied

### Assignment (9 missing)
- MS-ASGN-005 Remove submission when allowed
- MS-ASGN-006 View grade and feedback
- MS-ASGN-007 Submission blocked when closed
- MS-ASGN-009 Late submission blocked when closed
- MS-ASGN-013 Submit when no input areas enabled
- MS-ASGN-014 Edit submission exactly today
- MS-ASGN-015 Edit submission passed by one day
- MS-ASGN-016 Online text with whitespace
- MS-ASGN-017 File with special char

### Activities (4 missing)
- MS-ACT-006 Hidden activity not visible
- MS-ACT-010 Expand then immediately click
- MS-ACT-011 Activity name 200+ chars
- MS-ACT-013 Cannot click in collapsed section

### Profile (6 missing)
- MS-PROFILE-002 Profile information cards displayed
- MS-PROFILE-009 Invalid profile email
- MS-PROFILE-015 Data Retention Summary
- MS-PROFILE-016 Browser sessions report
- MS-PROFILE-017 Compose message
- MS-PROFILE-020 HTML/XSS injection

### Logout (5 missing)
- MS-LOGOUT-003 Browser back after logout
- MS-LOGOUT-006 Session timeout behaves like logout
- MS-LOGOUT-007 Logout in Tab A blocks Tab B
- MS-LOGOUT-008 Multi-tab simultaneous logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (1 extra)
- TC-009 (Disabled Lost password link)

### Dashboard (3 extra)
- TC-009 (import/export)
- TC-011 (blank search submit)
- TC-019 (one char over max)

### My Courses (2 extra)
- TC-003 (star without selecting)
- TC-004 (remove without selecting)

### Course Page (5 extra)
- TC-003 (blank section name)
- TC-006 (duplicate collapse all)
- TC-007 (add max sections success)
- TC-009 (long section name)
- TC-010 (special chars section name)

### Participants (2 extra)
- TC-007 (rapidly apply filters)
- TC-008 (clear after applying)

### Grades (3 extra)
- TC-007 (exact grade value 85)
- TC-008 (not graded dash)
- TC-009 (aggregation exact value)

### Assignment (2 extra)
- TC-009 (max file size success)
- TC-010 (file over limit blocked)

### Activities (0 extra)
- None

### Profile (1 extra)
- TC-007 (all fields valid submit)

### Logout (2 extra)
- TC-002 (unauthenticated logout duplicate)
- TC-003 (unauthenticated logout duplicate)

