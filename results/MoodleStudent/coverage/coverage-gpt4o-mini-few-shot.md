# Test Coverage Report

**Ground Truth:** MoodleStudent GT v2.2  
**Generated Suite:** openai/gpt-4o-mini-few-shot — 45 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 137 |
| GT cases covered by GEN | 36 |
| GT cases not covered by GEN | 101 |
| **Overall coverage** | **26.3%** |
| GEN cases with no GT counterpart (extras) | ~11 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 5 | 7 | **42%** |
| Dashboard | 20 | 6 | 14 | **30%** |
| My Courses | 14 | 5 | 9 | **36%** |
| Course Page | 12 | 3 | 9 | **25%** |
| Participants | 15 | 3 | 12 | **20%** |
| Grades | 10 | 2 | 8 | **20%** |
| Assignment | 18 | 5 | 13 | **28%** |
| Activities | 11 | 3 | 8 | **27%** |
| Profile | 17 | 4 | 13 | **24%** |
| Logout | 8 | 0 | 8 | **0%** |
| **Total** | **137** | **36** | **101** | **26.3%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (7 missing)
- MS-LOGIN-002 Guest access
- MS-LOGIN-003 Login page elements displayed
- MS-LOGIN-005 Empty username
- MS-LOGIN-006 Empty password
- MS-LOGIN-014 Submit with invalid username format
- MS-LOGIN-011 Whitespace retained after fail
- MS-LOGIN-012 Rapid double submission

### Dashboard (14 missing)
- MS-DASH-003 Timeline search filters content
- MS-DASH-006 Add student dashboard block in edit mode
- MS-DASH-013 Delete student dashboard block
- MS-DASH-016 Reset dashboard to default in edit mode
- MS-DASH-007 Dashboard blocked while unauthenticated
- MS-DASH-008 Add block unavailable outside edit mode
- MS-DASH-009 Timeline search with no matches
- MS-DASH-017 Delete Timeline block via block menu
- MS-DASH-019 Reset page to default completes without error
- MS-DASH-020 Attempt to filter events without selecting a course
- MS-DASH-012 Rapid edit-mode toggle
- MS-DASH-015 Timeline search with special characters
- MS-DASH-022 Search with minimum and maximum character lengths
- MS-DASH-023 Empty timeline dropdown filters handled gracefully

### My Courses (9 missing)
- MS-COURSES-004 Star course from card
- MS-COURSES-009 Remove course from view
- MS-COURSES-006 Search no matching course
- MS-COURSES-015 Invalid option in status
- MS-COURSES-008 Long symbol search
- MS-COURSES-010 Very long search query
- MS-COURSES-011 Search with special characters
- MS-COURSES-012 Rapid star action
- MS-COURSES-016 Search with whitespaces and emojis

### Course Page (9 missing)
- MS-COURSE-001 Student course tabs displayed
- MS-COURSE-005 Open activity from course page
- MS-COURSE-006 Student cannot access Settings tab
- MS-COURSE-015 Save activity Name blank
- MS-COURSE-016 Open activity with missing name
- MS-COURSE-010 Rapid section toggles
- MS-COURSE-013 Rapid single-section toggle
- MS-COURSE-014 Collapse all after zero sections
- MS-COURSE-017 Add one more section than allowed

### Participants (12 missing)
- MS-PART-002 Filter participants by name
- MS-PART-004 Open participant profile
- MS-PART-005 Student cannot enrol users
- MS-PART-006 Student cannot edit/remove roles
- MS-PART-014 Attempt to clear filters when no filters
- MS-PART-015 Attempt to view participant without selecting
- MS-PART-008 Filter no matching users
- MS-PART-009 Multiple filter conditions
- MS-PART-011 Rapid First Name initial changes
- MS-PART-013 Student role enrollment features not visible
- MS-PART-016 Checkbox selection caching
- MS-PART-017 Apply filter with empty condition

### Grades (8 missing)
- MS-GRADE-002 Expand course group
- MS-GRADE-003 Course total row displayed
- MS-GRADE-005 Student cannot access full gradebook
- MS-GRADE-014 Attempt to view grade details without auth
- MS-GRADE-015 Modify grades access denied
- MS-GRADE-009 Rapid consecutive course-group toggle
- MS-GRADE-011 Long feedback text truncated
- MS-GRADE-013 Whitespace-only feedback displays as empty

### Assignment (13 missing)
- MS-ASGN-001 Assignment details displayed
- MS-ASGN-005 Remove submission when allowed
- MS-ASGN-006 View grade and feedback
- MS-ASGN-008 Edit submission blocked when teacher does not permit
- MS-ASGN-009 Late submission blocked when closed
- MS-ASGN-019 View submission when no submissions
- MS-ASGN-012 Resubmit after grading not allowed
- MS-ASGN-014 Edit submission exactly today
- MS-ASGN-015 Edit submission passed by one day
- MS-ASGN-016 Online text with whitespace
- MS-ASGN-017 File with special char
- MS-ASGN-018 Rapid re-submission via Back
- MS-ASGN-020 Text editor unicode fuzzing

### Activities (8 missing)
- MS-ACT-002 Assignment activity rows visible
- MS-ACT-004 Open activity from overview
- MS-ACT-006 Hidden activity not visible
- MS-ACT-014 Attempt to navigate when no activities
- MS-ACT-009 Rapid double-click
- MS-ACT-010 Expand then immediately click
- MS-ACT-011 Activity name 200+ chars
- MS-ACT-013 Cannot click in collapsed section

### Profile (13 missing)
- MS-PROFILE-001 Profile details displayed
- MS-PROFILE-002 Profile information cards displayed
- MS-PROFILE-003 Edit profile form opens
- MS-PROFILE-015 Data Retention Summary
- MS-PROFILE-016 Browser sessions report
- MS-PROFILE-017 Compose message
- MS-PROFILE-007 Cannot edit another user
- MS-PROFILE-018 First name blank update
- MS-PROFILE-020 HTML/XSS injection
- MS-PROFILE-010 Cancel edit profile
- MS-PROFILE-013 Non-Latin Unicode in names
- MS-PROFILE-014 Rapid re-submit
- MS-PROFILE-021 Rapid double-submit

### Logout (8 missing)
- MS-LOGOUT-001 Logout from user menu
- MS-LOGOUT-002 Protected page requires re-auth
- MS-LOGOUT-003 Browser back after logout
- MS-LOGOUT-005 Double-click logout
- MS-LOGOUT-006 Session timeout behaves like logout
- MS-LOGOUT-007 Logout in Tab A blocks Tab B
- MS-LOGOUT-008 Multi-tab simultaneous logout
- MS-LOGOUT-009 Logout immediately after login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (1 extra)
- TC-006 (Log in with a password at maximum length)

### Dashboard (1 extra)
- TC-008 (Attempt to filter the Timeline block with an invalid course selection)

### My Courses (1 extra)
- TC-016 (Attempt to star a course that is already starred)

### Course Page (1 extra)
- TC-022 (View a section with no activities or resources)

### Participants (2 extra)
- TC-026 (Apply filters with the 'Any' toggle and no specific conditions)
- TC-027 (Sort participants by Last name in descending order)

### Grades (2 extra)
- TC-029 (Attempt to access another student's grades)
- TC-031 (View grades with maximum number of graded activities)

### Assignment (1 extra)
- TC-034 (Submit an assignment with maximum length text in the online text editor)

### Activities (1 extra)
- TC-039 (Attempt to access an activity that does not exist)

### Profile (1 extra)
- TC-044 (Upload a profile picture with maximum file size)

### Logout (0 extra)


