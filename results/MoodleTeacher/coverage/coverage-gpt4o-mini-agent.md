# Test Coverage Report

**Ground Truth:** Moodle Teacher GT v2.1 (Moodle gold oracle)
**Generated Suite:** openai/gpt-4o-mini — 207 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording. Implied coverage and partial element coverage are accepted per the relaxed rules.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 220 |
| GT cases covered by GEN | 130 |
| GT cases not covered by GEN | 90 |
| **Overall coverage** | **59.1%** |
| GEN cases with no GT counterpart (extras) | ~55 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 9 | 3 | **75%** |
| Dashboard | 13 | 7 | 6 | **54%** |
| Dashboard Edit Mode | 17 | 10 | 7 | **59%** |
| My Courses | 11 | 6 | 5 | **55%** |
| Course Page | 9 | 5 | 4 | **56%** |
| Course Edit Mode and Activity Chooser | 22 | 13 | 9 | **59%** |
| Assignment Creation | 19 | 10 | 9 | **53%** |
| Course Settings | 18 | 8 | 10 | **44%** |
| Participants Management | 17 | 12 | 5 | **71%** |
| Assignment Teacher View | 10 | 3 | 7 | **30%** |
| Assignment Submissions | 15 | 9 | 6 | **60%** |
| Gradebook Grader Report | 16 | 8 | 8 | **50%** |
| Profile | 14 | 6 | 8 | **43%** |
| Profile Edit | 18 | 8 | 10 | **44%** |
| Logout | 9 | 4 | 5 | **44%** |
| **Total** | **220** | **130** | **90** | **59.1%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (3 missing)
- MT-LOGIN-007 Disabled lost-password link does not open recovery flow
- MT-LOGIN-008 Failed login retains username in field
- MT-LOGIN-009 Rapid double login click produces single error

### Dashboard (6 missing)
- MT-DASH-001 Personalized dashboard greeting is displayed
- MT-DASH-002 Timeline block displays teaching actions for the correct course
- MT-DASH-003 Timeline filtering, sorting, and search work together
- MT-DASH-006 Dashboard blocked while unauthenticated
- MT-DASH-010 Timeline empty state when selected date range has zero activities
- MT-DASH-013 Rapid toggle of Timeline sort stabilises at final click state

### Dashboard Edit Mode (7 missing)
- MT-DEDIT-002 Add a specific dashboard block (Latest announcements) and verify persistence
- MT-DEDIT-003 Configure a dashboard block and verify it does not affect student view
- MT-DEDIT-010 Move a block via drag and drop
- MT-DEDIT-011 Move a block via the block options menu
- MT-DEDIT-012 Add block submission blocked when block type is not selected
- MT-DEDIT-015 Toggling edit mode off closes the Add a block page
- MT-DEDIT-016 Reset to default immediately after adding a block removes the new block

### My Courses (5 missing)
- MT-COURSES-001 Course cards display image, name, and category
- MT-COURSES-002 Filter, search, sort, and layout controls work together and persist
- MT-COURSES-003 Open course from a course card
- MT-COURSES-007 Hidden-course filter shows only hidden courses
- MT-COURSES-010 Very long search query (200+ chars) accepted without error

### Course Page (4 missing)
- MT-COURSE-001 Teacher course tabs (including Settings) are all visible
- MT-COURSE-002 Sections, activity icons, and activity names are visible
- MT-COURSE-006 Hidden activity visible to teacher with indicator, blocked from student
- MT-COURSE-009 Rapid double-click on activity link causes single navigation

### Course Edit Mode and Activity Chooser (9 missing)
- MT-CEDIT-001 Enable course edit mode reveals authoring controls
- MT-CEDIT-002 Rename a course section inline and verify persistence after refresh
- MT-CEDIT-004 Bulk hide selected activities; unselected remain visible
- MT-CEDIT-007 Edit controls are hidden when edit mode is off
- MT-CEDIT-012 Rename section inline with empty text reverts or shows required-field error
- MT-CEDIT-013 Rename section inline with 200+ characters wraps without breaking layout
- MT-CEDIT-016 Rapid hide/show activity toggle ends in final state with no locked intermediate
- MT-CEDIT-020 Activity chooser search with special characters displays no-results state
- MT-CEDIT-021 Bulk action bar clears checkboxes when closed

### Assignment Creation (9 missing)
- MT-ACREATE-003 Configure availability dates and verify they are saved
- MT-ACREATE-004 Configure submission and feedback types and verify they are saved
- MT-ACREATE-005 Configure grade, completion tracking, and tag; verify persistence
- MT-ACREATE-007 Oversized additional file upload is blocked with size validation
- MT-ACREATE-008 Invalid accepted file type blocks save
- MT-ACREATE-013 Cut-off date earlier than due date blocks save
- MT-ACREATE-017 Disabling all submission types blocks save
- MT-ACREATE-018 Additional file with emoji filename uploads and persists
- MT-ACREATE-019 Maximum points boundary value saves without system overflow

### Course Settings (10 missing)
- MT-CSET-002 Configure visibility and date fields; verify saved values after reopening
- MT-CSET-003 Configure course summary and image; verify after reopening
- MT-CSET-004 Configure format, completion, groups, and tag; verify after reopening
- MT-CSET-010 Maximum upload size option persists after save
- MT-CSET-011 Course end date exactly equal to start date saves successfully
- MT-CSET-013 Very long course full name (200+ chars) saves without crash
- MT-CSET-014 Special characters and emoji in course short name are preserved
- MT-CSET-015 Leading/trailing whitespace in course short name is trimmed on save
- MT-CSET-016 Non-numeric value in Number of Announcements field blocks save
- MT-CSET-018 Previously selected grouping value is restored when field becomes visible again

### Participants Management (5 missing)
- MT-PART-003 Alphabetical filtering of participants by initial
- MT-PART-005 Row action menu opens the correct participant's profile
- MT-PART-010 Multiple simultaneous filter conditions narrow results correctly
- MT-PART-015 Confirm enrollment then navigate back does not create duplicate row
- MT-PART-017 Alphabet filter with no matching participants shows empty state

### Assignment Teacher View (7 missing)
- MT-ATVIEW-001 Assignment metadata (opened date, due date, description, files) visible
- MT-ATVIEW-002 Grading summary panel visible with participant and submission counts
- MT-ATVIEW-004 Assignment tabs navigate and display correct headings
- MT-ATVIEW-005 Assignment blocked while unauthenticated
- MT-ATVIEW-006 Grade unavailable without permission; direct URL shows access denied
- MT-ATVIEW-008 Expired due date shows overdue/closed state
- MT-ATVIEW-010 Very long assignment description does not break layout

### Assignment Submissions (6 missing)
- MT-ASUB-001 Submission table columns (identity, status, date, files, feedback, grade) all visible
- MT-ASUB-004 Enable quick grading, enter grade and feedback, verify persistence after refresh
- MT-ASUB-005 Download submitted file returns the file without access-denied page
- MT-ASUB-006 Submissions blocked while unauthenticated
- MT-ASUB-011 Inline Final Grade cell is read-only when quick grading is disabled
- MT-ASUB-015 Clicking student name in submissions navigates to the student's profile

### Gradebook Grader Report (8 missing)
- MT-GRADE-001 Grader report table displays activity columns, student rows, and average row
- MT-GRADE-002 Switching report type opens the selected report
- MT-GRADE-003 Searching gradebook users filters to matching rows
- MT-GRADE-005 Opening activity column menu reveals grade settings action
- MT-GRADE-006 Gradebook blocked while unauthenticated
- MT-GRADE-008 Student cannot access the grader report
- MT-GRADE-011 Grade cell is read-only when edit mode is off
- MT-GRADE-012 Non-numeric value in grade cell blocks save

### Profile (8 missing)
- MT-PROFILE-001 Profile displays initials icon, full name, message button, and description area
- MT-PROFILE-002 User details, privacy/policies, course details, and login activity cards visible
- MT-PROFILE-005 Profile blocked while unauthenticated
- MT-PROFILE-006 Other-user private fields are not rendered for teacher viewing another user
- MT-PROFILE-009 Non-existent user profile URL shows a user-not-found error page
- MT-PROFILE-010 Student viewing teacher profile cannot see private activity reports
- MT-PROFILE-011 Very long profile description renders without breaking layout
- MT-PROFILE-014 Teacher enrolled in 50+ courses shows courses in scrollable or paginated list

### Profile Edit (10 missing)
- MT-PEDIT-003 Additional names and interest tag persist after save
- MT-PEDIT-004 "Expand all" expands all collapsible profile sections
- MT-PEDIT-007 Invalid email address format blocks save
- MT-PEDIT-011 Clearing all required fields simultaneously shows multiple validation errors
- MT-PEDIT-012 Missing email domain (e.g., `teacher1@`) is explicitly rejected
- MT-PEDIT-014 10,000+ character description saves and is visible on profile
- MT-PEDIT-015 Emoji and non-Latin Unicode in First Name are preserved after save
- MT-PEDIT-016 Leading and trailing whitespace in First Name is trimmed on save
- MT-PEDIT-017 Rapid double-click on Update profile submits exactly once
- MT-PEDIT-018 Add and immediately remove a repeating group item saves without ghost entries

### Logout (5 missing)
- MT-LOGOUT-002 Protected page requires re-authentication after logout
- MT-LOGOUT-003 Browser back after logout does not expose cached dashboard content
- MT-LOGOUT-005 Double-click logout completes once without error
- MT-LOGOUT-007 Concurrent session in second tab redirects to login after first-tab logout
- MT-LOGOUT-008 Navigating to logout.php without a token is blocked (CSRF protection)

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Dashboard (~5 extra types)
- Create a new calendar event via the "New Event" button
- Rapid double-click on "New Event" is blocked
- Rapid previous/next month navigation is blocked (agent incorrectly expects navigation to be blocked rather than succeed with debouncing)
- Enter special characters in the timeline "Search Activities" field expecting a validation error (GT expects graceful no-results state, not an error)
- Enter a long string in the "Search Activities" field expecting a character-limit error

### Dashboard Edit Mode (~3 extra types)
- Attempt to reset page to default while already in edit mode without prerequisite customization
- Delete an existing block via rapid double-click; expects only one deletion
- Attempt to configure/move/delete a block without first selecting it (not a real Moodle scenario since block menus are contextual)

### Course Page (~5 extra types)
- Access individual activities (Activity 1, Resource 1, Activity 2, Resource 2) as distinct named test cases; agent treats these as separate positive and unauthenticated-negative scenarios
- Access resources after collapsing all sections (interaction-edge variant per individual resource)

### Course Edit Mode and Activity Chooser (~5 extra types)
- Attempt to add a subsection without any sections present
- Attempt to open Activity Chooser without any sections present
- Attempt to edit/move/duplicate/hide/set-restrictions/delete an activity that does not exist (agent enumerates all action types on a non-existent activity as separate cases)
- Set access restrictions on an activity (not covered in GT scope)
- Add maximum allowed subsections and verify the limit is enforced

### Participants Management (~4 extra types)
- Edit user role from the row action menu
- Send a message to a user from the participants table
- Bulk enroll selected users
- User search in enrollment dialog with special characters and emoji

### Profile (~9 extra types)
- View Blog entries, Forum posts, Forum discussions, Learning plans, Browser sessions, Grades overview, First access, Last access, relative time indicators as separate positive test cases (profile information card links)
- Negative counterparts for each of the above profile card links without authentication
- Attempt to edit profile without making any changes (expects a "no changes detected" error, which is not a Moodle behaviour)
- View Data retention summary as a standalone positive and negative test

### Gradebook Grader Report (~2 extra types)
- Edit grade value just below the lower boundary (negative boundary; GT covers min=0 and max=100 but not sub-zero)
- Edit grade value just above the upper boundary as a separate additional case beyond MT-GRADE-007/014

### Logout (~1 extra type)
- Attempt to log out when not authenticated / user is already unauthenticated (agent creates two variants: one negative and one edge, both testing the same scenario as MT-LOGOUT-004)