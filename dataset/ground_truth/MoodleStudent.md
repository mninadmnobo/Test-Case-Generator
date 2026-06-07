# Moodle Student Test Cases

**Website URL:** http://localhost:8080
**Test Suite Version:** 2.2 (Moodle gold oracle)
**Role Scope:** Student learner workflows only

---

## Table of Contents
1. [Login](#1-login)
2. [Dashboard](#2-dashboard)
3. [My Courses](#3-my-courses)
4. [Course Page](#4-course-page)
5. [Participants](#5-participants)
6. [Grades](#6-grades)
7. [Assignment](#7-assignment)
8. [Activities](#8-activities)
9. [Profile](#9-profile)
10. [Logout](#10-logout)

---

## Test Credentials

| Field | Value |
|-------|-------|
| Student account | `student1`, seeded student enrolled in the test course |
| Teacher account | `teacher1`, seeded teacher for setup/grading preconditions |
| Test course | `QA Automation 101`, containing participants, grades, activities, and an assignment |
| Reference assignment | `Essay Draft`, online text and file submission enabled, open for submission, no separate submit-button confirmation |
| Boundary grade range | 0 to 100 points for `Essay Draft` |
| Boundary upload limit | 10 MB maximum upload size for assignment/profile upload checks |
| Boundary files | `essay-draft.pdf` under 1 MB, `essay-limit-10mb.pdf` exactly at limit, `oversize-11mb.pdf` over limit |
| Boundary text | `GT-LONG-TEXT-START` + 10,000 characters + `GT-LONG-TEXT-END` |

## Moodle Gold Oracle Contract

| Rule | Requirement |
|------|-------------|
| Source anchoring | Every module below maps to `dataset/functional_description/MoodleStudent.md`; inferred Moodle behaviour is allowed only when the expected result names observable UI evidence. |
| Student-only scope | Student ground truth must not include teacher authoring, enrollment administration, or full-gradebook administration workflows. |
| Observable result | Expected results must name visible UI state, persisted submission/grade state, redirect, access denial, validation feedback, or absence of privileged controls. |
| Deterministic oracle | Avoid generic success words, conditional applicability, ambiguous alternatives, and implementation-variable outcomes. A reviewer should be able to mark pass/fail without guessing. |
| Fixture stability | Use seeded student, teacher, course, assignment, file, grade, and activity fixtures rather than unspecified users or courses. |
| Permission boundary | Student tests should explicitly verify absence of teacher-only controls where relevant. |
| Persistence check | Submission, profile, dashboard layout, and course-card preference tests should verify state after save and refresh when practical. |
| Data cleanup | Tests that mutate data must restore the named fixture or create disposable records with the `Ground Truth` suffix for cleanup. |

## Quality and Traceability Rules

| Rule | Requirement |
|------|-------------|
| `MS-NAV` | Shared navigation, user menu, breadcrumbs, course tabs, Course Index, notifications, and messaging. |
| `MS-LOGIN` | Authentication form, guest entry, cookies notice, and login validation. |
| `MS-DASH` | Student Dashboard timeline, calendar, personal event entry, edit mode, and empty states. |
| `MS-COURSES` | My Courses filtering, searching, sorting, layout, starring, and hidden-course behaviour. |
| `MS-COURSE` | Course page content, tabs, section collapse, Course Index navigation, and no-authoring permission boundary. |
| `MS-PART` | Participants viewing, filtering, profile navigation, and enrollment/role-management denial. |
| `MS-GRADE` | Student User report, own-grade visibility, course total, ungraded placeholders, and full-gradebook denial. |
| `MS-ASGN` | Assignment details, online text/file submission, edit/remove submission, feedback, late/required-field boundaries. |
| `MS-ACT` | Activities overview, grouped activity tables, activity navigation, hidden activity denial, and empty course state. |
| `MS-PROFILE` | Student profile display, own profile edit, picture upload, validation, and other-user edit denial. |
| `MS-LOGOUT` | Logout, protected-route reauthentication, browser-back protection, and timeout behaviour. |

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-001 | Valid student login | Student account exists and is active | 1. Navigate to the Moodle login page<br>2. Enter a valid student username<br>3. Enter the student password<br>4. Click "Log in" | Student is redirected to Dashboard and the user menu shows the student initials/name | High |
| MS-LOGIN-002 | Guest access from login page | Guest access is enabled | 1. Open login page<br>2. Click "Access as a guest" | Guest browsing opens without authenticating as student | Medium |
| MS-LOGIN-003 | Login page elements displayed | None | 1. Open login page | Username, Password, Log in, Lost password, Access as guest, and Cookies notice controls are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-004 | Invalid student credentials | Login page is visible | 1. Enter a valid student username<br>2. Enter an incorrect password<br>3. Click "Log in" | Login error is shown, password is cleared, username remains populated, and Dashboard is not opened | High |
| MS-LOGIN-005 | Empty username | Login page is visible | 1. Leave Username empty<br>2. Enter the student password<br>3. Click "Log in" | Login is rejected, username field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-006 | Empty password | Login page is visible | 1. Enter a valid student username<br>2. Leave Password empty<br>3. Click "Log in" | Login is rejected, password field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-013 | Submit with invalid credentials — authentication failure response | Login page is visible | 1. Enter any existing or non-existing username<br>2. Enter an incorrect password<br>3. Click "Log in" | Authentication fails with an inline error message near the form; the password field is cleared; the username field retains the entered value; no redirect to Dashboard occurs | Medium |
| MS-LOGIN-014 | Submit with invalid username format containing special characters | Login page is visible | 1. Enter a username string containing special characters (e.g. `user@!#$`)<br>2. Enter any password<br>3. Click "Log in" | Login is rejected with an inline error; password field is cleared; username field retains the entered string; no authenticated page opens | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-009 | Long username failure handling | Login page is visible | 1. Enter 200+ character username and invalid password<br>2. Submit | Login error is shown, password is cleared, the long username remains in the username field, and Log in remains clickable | Low |
| MS-LOGIN-010 | Both fields empty — all validation errors shown simultaneously | Login page is visible | 1. Leave Username and Password both empty<br>2. Click "Log in" | Both username and password fields are flagged with validation errors simultaneously; no authenticated page opens | High |
| MS-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Login page is visible | 1. Enter a username with leading and trailing spaces<br>2. Enter an incorrect password<br>3. Click "Log in" | Login is rejected with error; username field retains the entered string including the surrounding whitespace | Low |
| MS-LOGIN-012 | Rapid double submission of Log in results in single failure response | Login page is visible; invalid credentials ready | 1. Enter invalid credentials<br>2. Double-click "Log in" rapidly | Exactly one login-error response is displayed; the form is not submitted twice and no duplicate error message is stacked | Medium |

---

## 2. Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-001 | Dashboard page loads with user information visible | Student is logged in | 1. Open Dashboard | Dashboard loads and displays information identifying the logged-in student (name, initials, or personalised greeting) in the page or user menu area | High |
| MS-DASH-002 | Timeline block displays activities | Student is logged in and has at least one upcoming activity | 1. Open Dashboard<br>2. Inspect the Timeline block | Timeline block is visible and renders at least one activity row containing an activity name, associated course, and due date | High |
| MS-DASH-003 | Timeline search filters content | Student is on Dashboard with Timeline block visible | 1. Enter a search term in the Timeline search field<br>2. Apply the search | Timeline updates to show only rows matching the search term; rows not matching the term are hidden; the search input retains the entered term | High |
| MS-DASH-004 | Calendar block supports personal event flow | Calendar block is visible | 1. Click "New event" | Personal calendar event form or modal opens with event title, date, and save/cancel controls | Medium |
| MS-DASH-005 | Calendar navigation and links | Calendar block is visible | 1. Navigate to next month and back<br>2. Click Full calendar | Calendar heading changes then returns to the original month; Full calendar opens successfully | Medium |
| MS-DASH-006 | Add student dashboard block in edit mode | Student is on Dashboard and Edit mode is enabled | 1. Click "+ Add a block"<br>2. Select a block type from the list<br>3. Refresh Dashboard | The selected block appears on the Dashboard after refresh | Medium |
| MS-DASH-013 | Delete student dashboard block | A block is visible on the Dashboard in Edit mode | 1. Open the block action menu<br>2. Delete the block<br>3. Refresh Dashboard | The deleted block is absent from the Dashboard after refresh | Medium |
| MS-DASH-016 | Reset dashboard to default in edit mode reverts layout | Student is on Dashboard with Edit mode enabled | 1. Click the "Reset page to default" option in Edit mode<br>2. Confirm the reset | Dashboard layout reverts to the default block arrangement; any added or repositioned blocks return to their original positions | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-007 | Dashboard blocked while unauthenticated | User is logged out | 1. Navigate directly to Dashboard URL | User is redirected to login | High |
| MS-DASH-008 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect Dashboard controls | "+ Add a block", configure, move, and delete controls are not rendered on the Dashboard | High |
| MS-DASH-009 | Timeline search with no matches | Student is logged in | 1. Search for a term that matches no activity | Empty/no-results state is displayed in the Timeline block | Medium |
| MS-DASH-017 | Delete Timeline block via block menu removes it from dashboard | Student is on Dashboard with Edit mode enabled and Timeline block visible | 1. Open the block action menu on the Timeline block<br>2. Click "Delete" and confirm<br>3. Refresh Dashboard | Timeline block is absent from the Dashboard after refresh; no error message is shown | Medium |
| MS-DASH-019 | Reset page to default completes without error | Student is on Dashboard with Edit mode enabled | 1. Click "Reset page to default"<br>2. Confirm if prompted | Reset action completes; Dashboard is displayed in the default layout without error | Medium |
| MS-DASH-020 | Attempt to filter events without selecting a course | Calendar block is visible | 1. Open course filter<br>2. Leave selection blank<br>3. Apply filter | Inline validation blocks filter indicating course selection is required | High |
| MS-DASH-021 | Attempt to create a new event without entering required details | Calendar block is visible | 1. Click "New event"<br>2. Leave event details blank<br>3. Save | Save is blocked with validation errors on required fields | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-012 | Rapid edit-mode toggle | Dashboard is visible | 1. Toggle Edit mode repeatedly | Final UI state matches final toggle | Medium |
| MS-DASH-014 | Timeline empty state when selected range has zero activities | Student is on Dashboard; a date range with no activities is known | 1. Select a date range that contains no scheduled activities | Timeline block displays its empty-state message and no activity rows are rendered | Low |
| MS-DASH-015 | Timeline search with special characters and emoji accepted | Student is on Dashboard | 1. Type `@@##🎓` into the Timeline search field | Search field accepts the input without error; timeline shows empty-results state or matching items; no crash or validation dialog appears | Low |
| MS-DASH-022 | Search with minimum and maximum character lengths | Timeline block is visible | 1. Enter exactly 1 character and search<br>2. Enter 200+ characters and search | Search accepts both inputs without crashing; empty or matching results are shown | Medium |
| MS-DASH-023 | Empty timeline dropdown filters handled gracefully | Timeline block is visible | 1. Open Timeline dropdown filters<br>2. Leave filters completely blank<br>3. Apply | Filter handles empty state gracefully without crashing; Timeline displays default or empty state | Medium |

---

## 3. My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-001 | Student course cards displayed | Student is enrolled in courses | 1. Open My Courses | Course cards show image, course name, and category | High |
| MS-COURSES-002 | Filter and search controls update the course list | Student is enrolled in multiple courses | 1. Select a status filter<br>2. Enter a search term<br>3. Sort by course name | Only matching course cards remain visible and the order follows the sort selection | High |
| MS-COURSES-003 | Open course from course card | At least one course is visible | 1. Click course name | Student opens course main page | High |
| MS-COURSES-004 | Star course from course card | Course card menu is visible | 1. Open card menu<br>2. Click "Star this course"<br>3. Refresh My Courses | Course appears in the Starred filter | Medium |
| MS-COURSES-009 | Remove course from view without unenrolling | Course card menu is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Select Hidden filter | Course appears under Hidden and opens successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-006 | Search no matching course | Student is logged in | 1. Search for a non-existent course | Empty/no-results state is shown | Medium |
| MS-COURSES-014 | Leave the search field blank and submit | My Courses is visible | 1. Clear search field<br>2. Apply search | Course grid displays all enrolled courses without error | Medium |
| MS-COURSES-015 | Select an invalid option in the Status dropdown | My Courses is visible | 1. Force an invalid status option<br>2. Apply filter | Filter is blocked or ignored; error message is shown and courses are not incorrectly filtered | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-007 | Hidden-course filter | A course was removed from view | 1. Select Hidden filter | The hidden course is listed in the Hidden filter; non-hidden courses are absent | Medium |
| MS-COURSES-008 | Long symbol search | My Courses is visible | 1. Search with a long string containing symbols and numbers | Search field retains the entered string, no error dialog appears, and the course list shows matching or no-results content | Low |
| MS-COURSES-010 | Very long search query (200+ chars) accepted without error | My Courses is visible | 1. Enter a 200+ character string into the course search field<br>2. Submit | Search field accepts and retains the long string; no error dialog appears; matching or empty-results list is displayed without page crash | Low |
| MS-COURSES-011 | Search with special characters and emoji accepted | My Courses is visible | 1. Enter `@@##🎓 courses` into the search field<br>2. Submit | Search field accepts the input; no crash or validation error appears; list shows matching or empty-results content | Low |
| MS-COURSES-012 | Rapid star action on same course card is idempotent | Course card is visible and not starred | 1. Click "Star this course"<br>2. Immediately repeat the star action | Course is starred once; the Starred filter shows the course exactly once with no duplicate entries | Medium |
| MS-COURSES-016 | Search with whitespaces and emojis | My Courses is visible | 1. Enter leading/trailing whitespaces and special emojis into the search field<br>2. Apply search | Search executes normally and displays matching courses or an empty-results state without error | Low |

---

## 4. Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-001 | Student course tabs displayed and Settings tab absent | Student is enrolled in a course | 1. Open the course page | Course, Participants, Grades, Activities, and Competencies tabs are visible; Settings tab and edit controls are not visible | High |
| MS-COURSE-002 | Course sections and activities displayed | Course contains sections | 1. Inspect course content | Sections, activity icons, and activity/resource names are visible | High |
| MS-COURSE-003 | Collapse all sections | Sections are expanded | 1. Click "Collapse all" | Sections collapse | Medium |
| MS-COURSE-005 | Open activity from course page | Activity link is visible | 1. Click an activity or resource link | Activity/resource page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-006 | Student cannot access Settings tab | Student is on course page | 1. Inspect course tabs | Settings tab and teacher settings controls are absent | High |
| MS-COURSE-007 | Student cannot enable course edit mode | Student is on course page | 1. Inspect page controls<br>2. Navigate directly to the edit-mode course URL | Edit toggle is absent; direct edit-mode URL returns to read-only course view or access denied without authoring controls | High |
| MS-COURSE-015 | Attempt to save an activity/resource with the Name field left blank | Edit mode enabled | 1. Add new activity<br>2. Leave Name blank<br>3. Save | Save is blocked with inline validation on the Name field | High |
| MS-COURSE-016 | Attempt to open an activity/resource that has an empty/missing Name | Course contains item with missing name | 1. Click the blank name area | Navigation is blocked; inline validation indicator is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-010 | Rapid section toggles | A section is visible | 1. Expand/collapse a section three times | Section ends in the final clicked state and each activity row appears once | Medium |
| MS-COURSE-013 | Rapid single-section toggle ends in final clicked state | A section is visible | 1. Click the section toggle arrow rapidly three times in quick succession | Section ends in the state corresponding to the final click; no intermediate state is permanently locked | Medium |
| MS-COURSE-014 | Collapse all after zero sections succeeds silently | Course page is open with zero sections | 1. Click "Collapse all" | Collapse all completes silently; no error is displayed and the empty course page remains rendered | Low |
| MS-COURSE-017 | Attempt to add one more section than allowed | Course is at max sections | 1. Click Add Row to add a section | Addition is blocked; error message is shown indicating maximum reached | Medium |

---

## 5. Participants

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-001 | Participants table displayed | Student opens Participants tab | 1. Open Participants | Filters, alphabetical filters, and participant table are visible | High |
| MS-PART-002 | Filter participants by name | Participants page is visible | 1. Add a First name filter<br>2. Apply filters | Participants table shows matching rows and hides unrelated participant rows | High |
| MS-PART-003 | Alphabetical filters | Participants exist | 1. Select a first-name or last-name initial | Table filters by the selected initial | Medium |
| MS-PART-004 | Open participant profile | Participant row exists | 1. Click participant name | Participant profile page opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-005 | Student cannot enrol users | Student is on Participants page | 1. Inspect page toolbar | Enrol users button, role dropdown, and enrollment duration controls are not rendered | High |
| MS-PART-006 | Student cannot edit/remove roles | Student is on Participants page | 1. Inspect row menus<br>2. Navigate directly to a role-management URL | Role edit and remove actions are not rendered; direct role-management URL shows access denied before any role form renders | High |
| MS-PART-014 | Attempt to clear filters when no filters are applied | Participants page is visible | 1. Ensure no filters are applied<br>2. Click "Clear filters" | Action completes silently; list remains unchanged | Medium |
| MS-PART-015 | Attempt to view participant profile without selecting a participant | Participants page is visible | 1. Trigger "View Profile" action without selecting a row | Action is blocked; no profile is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-008 | Filter no matching users | Participants page is visible | 1. Apply a filter condition that matches no participant | Empty/no-results state is displayed | Medium |
| MS-PART-009 | Multiple filter conditions | Participants include both student and teacher accounts | 1. Add a Role filter for Teacher<br>2. Add a name filter<br>3. Apply filters | Table shows only the matching teacher row; student and non-matching rows are absent | Medium |
| MS-PART-010 | Apply filters with empty condition row — no error | Participants page is visible with filter panel open | 1. Add a filter condition row but leave its value empty<br>2. Click "Apply filters" | Participants list updates or shows all participants without a JavaScript error; no page crash | Low |
| MS-PART-011 | Rapid First Name initial changes resolve to final selection only | Participants page is visible | 1. Click alphabetical initial "A"<br>2. Immediately click "B"<br>3. Immediately click "C" | Table reflects the last-clicked initial ("C") only; no stale intermediate filter result is shown | Medium |
| MS-PART-013 | Student role enrollment management features not visible | Student is on the Participants page | 1. Inspect each participant row for role-edit controls<br>2. Inspect the toolbar for enrollment management buttons | Role-edit icons, "Enrol users" button, and enrollment duration controls are not rendered for any row | High |
| MS-PART-016 | Checkbox selection caching | Participants list is visible | 1. Select a participant row checkbox<br>2. Navigate to their profile<br>3. Press browser back | The checkbox selection on the participant table persists | Medium |
| MS-PART-017 | Apply filter with empty condition | Participants list is visible | 1. Add a filter condition row<br>2. Leave the condition attribute completely empty<br>3. Click "Apply filters" | Page handles the invalid filter gracefully without a JavaScript error or crash | Low |

---

## 6. Grades

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-001 | Student User report displayed | Student opens Grades | 1. Open Grades page | Grade item, calculated weight, grade, range, percentage, feedback, and contribution columns are visible | High |
| MS-GRADE-002 | Expand course group | Grades contain a course group with activities | 1. Collapse a course group<br>2. Expand it again | Child grade items are hidden after collapse and visible again after expand | Medium |
| MS-GRADE-003 | Course total row displayed | Student has grade items | 1. Scroll to total row | AGGREGATION Course total displays cumulative grade | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-005 | Student cannot access full gradebook | Student is logged in | 1. Navigate directly to Grader report/full gradebook URL | Access denied page is shown before grader report rows render; other students' names and grades are not visible | High |
| MS-GRADE-014 | Attempt to view grade details without proper authentication | User is logged out | 1. Navigate directly to grade details URL | User is redirected to login page | High |
| MS-GRADE-015 | Modify grades access denied | Student User report is displayed | 1. Inspect Gradebook rows | No input fields or edit buttons exist for the student to modify their own grades | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-007 | No graded activities yet | Student has no graded activities | 1. Open Grades | User report opens with empty grade placeholders for activity rows and no other students' grades | Low |
| MS-GRADE-009 | Rapid consecutive course-group toggle ends in stable state | Student is on the Grades page; a course group is visible | 1. Click the course-group collapse control three times in rapid succession | Course group ends in the state corresponding to the final click; no intermediate state is locked and no JavaScript error appears | Medium |
| MS-GRADE-011 | Long feedback text truncated in cell; full text accessible on hover | Teacher has entered 200+ character feedback for a grade item | 1. Open Grades page<br>2. Locate the Feedback cell for the graded item<br>3. Hover over the cell | Feedback cell displays truncated text within the column width; full feedback text is accessible via tooltip or hover reveal | Low |
| MS-GRADE-013 | Whitespace-only feedback displays as empty placeholder | Teacher has entered whitespace-only feedback for a grade item | 1. Open Grades page<br>2. Inspect the Feedback cell for the whitespace-feedback item | Feedback cell shows the empty-placeholder indicator (dash or blank); no visible whitespace block occupies the cell | Low |

---

## 7. Assignment

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-001 | Assignment details displayed | Assignment is available | 1. Open assignment page | Opened date, due date, description, and submission status are visible | High |
| MS-ASGN-002 | Submit online text | Assignment accepts online text and is open for submissions | 1. Click "Add submission"<br>2. Enter text in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission status shows Submitted for grading and the entered text is visible in the submission preview | High |
| MS-ASGN-003 | Submit file upload | Assignment accepts file submissions and is open for submissions | 1. Click "Add submission"<br>2. Upload a file within the allowed size/type<br>3. Save/submit<br>4. Reopen the assignment page | Submission status includes the uploaded file as a downloadable file link | High |
| MS-ASGN-004 | Edit submission before deadline | Editable submission exists before due date | 1. Click "Edit submission"<br>2. Replace text with updated content<br>3. Save changes<br>4. Reopen the assignment page | Updated text is shown and the previous text is no longer the active submission content | Medium |
| MS-ASGN-005 | Remove submission when allowed | Removable submission exists before due date | 1. Click "Remove submission"<br>2. Confirm removal<br>3. Reopen the assignment page | Submission file/text is removed and submission status returns to not submitted or draft-empty state | Medium |
| MS-ASGN-006 | View grade and feedback | Teacher has graded submission | 1. Open assignment page | Earned grade and teacher feedback are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-007 | Submission blocked when assignment is closed | Due/cut-off date has passed and late submissions are disabled | 1. Open assignment<br>2. Inspect submission controls<br>3. Navigate directly to the submission edit URL | Add/Edit submission controls are not rendered and direct submission edit URL shows the assignment-closed message before an editor appears | High |
| MS-ASGN-008 | Edit submission blocked when teacher does not permit resubmission | Assignment has been submitted; teacher has disabled resubmission | 1. Open assignment page<br>2. Click the "Edit submission" action | Edit submission action is blocked; Submission Form does not open; submission remains in Submitted for grading state | High |
| MS-ASGN-009 | Late submission blocked when closed | Due/cut-off date has passed and late submissions are disabled | 1. Open assignment<br>2. Inspect submission controls<br>3. Navigate directly to the submission edit URL | Add/Edit submission controls are not rendered and direct submission edit URL shows the assignment-closed message before an editor appears | High |
| MS-ASGN-019 | Attempt to view submission when there are no submissions made | Assignment has no submissions | 1. Click "View submission" action if available | Action blocked or page displays "No submissions have been made yet" | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-012 | Resubmit after grading not allowed | Assignment is graded and resubmission disabled | 1. Open assignment page | Edit/resubmit controls are absent or disabled | Medium |
| MS-ASGN-013 | Submit when no input areas are enabled still succeeds | Assignment is configured with no online text and no file submission enabled | 1. Open the assignment page<br>2. Click "Add submission"<br>3. Click "Save changes" without entering any content | Submission status changes to Submitted for grading; no validation error is raised for an empty submission when no input types are enabled | Medium |
| MS-ASGN-014 | Edit submission allowed when due date is exactly today and teacher permits resubmission | Assignment due date is set to today; teacher has enabled resubmission | 1. Open assignment page<br>2. Click "Edit submission" | Edit submission form opens without a late-submission or access-denied message | Medium |
| MS-ASGN-015 | Edit submission blocked when due date passed by one day even if teacher permits resubmission | Assignment due date was yesterday; teacher has enabled resubmission but late submissions are disabled | 1. Open assignment page<br>2. Inspect submission controls | Edit/resubmit controls are absent or show an assignment-closed message; submission form does not render | High |
| MS-ASGN-016 | Online text with leading/trailing whitespace is trimmed on save | Assignment is open for online text submission | 1. Click "Add submission"<br>2. Enter text with leading and trailing spaces in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission preview shows the text without the surrounding whitespace | Low |
| MS-ASGN-017 | File with special-character/emoji filename uploads and filename is preserved | Assignment accepts file submissions | 1. Click "Add submission"<br>2. Upload a file whose name contains special characters and emoji<br>3. Click "Save changes"<br>4. Reopen the assignment page | The file appears in the submission file list with its original filename preserved including the special characters and emoji | Low |
| MS-ASGN-018 | Rapid re-submission via browser Back does not create duplicate submission | Student has just saved an assignment submission | 1. Immediately after saving, press browser Back<br>2. Resubmit the form if prompted<br>3. Reopen the assignment page | Only one submission record exists; no duplicate submission entry or duplicate file appears | Medium |
| MS-ASGN-020 | Text editor unicode fuzzing | Assignment accepts online text | 1. Click "Add submission"<br>2. Enter extremely long text with unicode/emoji characters<br>3. Click "Save changes" | Submission accepts characters and saves without truncation or database error | Low |

---

## 8. Activities

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-001 | Activities overview displayed with activity groups visible | Course has activities | 1. Open Activities tab | Activities tab opens and activity groups (including Assignments) are rendered; at least one activity group is visible | High |
| MS-ACT-002 | Assignment activity rows visible in Activities tab | Assignments exist in the course | 1. Open Activities tab<br>2. Inspect the Assignments section | Assignment rows are visible showing activity name and associated details; the Assignments section is not empty | High |
| MS-ACT-003 | Expand collapsed activity type | Forums or Resources section is collapsed | 1. Click section arrow | Section expands and displays activities | Medium |
| MS-ACT-004 | Open activity from overview | Activity row exists | 1. Click activity name | Activity page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-006 | Hidden activity not visible to student | Teacher has hidden an activity | 1. Open Activities page as student<br>2. Browse activity groups for the hidden activity<br>3. Try the direct activity URL | Activity is absent from Activities page and the direct URL shows an access restriction page without rendering the assignment content | High |
| MS-ACT-014 | Attempt to navigate to an activity without any activities listed | Activities page is open but empty | 1. Attempt to click an activity link area | No navigation occurs; empty state remains visible | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-007 | Course with no activities | Course has no activities | 1. Open Activities tab | Activities page shows an empty-state message and no activity-group table is rendered | Low |
| MS-ACT-009 | Rapid double-click on assignment name causes only one navigation | Activities tab is open; at least one assignment row is visible | 1. Double-click the assignment name link rapidly | Browser navigates to the assignment page exactly once; no duplicate page-load or error page appears | Medium |
| MS-ACT-010 | Expand collapsed section then immediately click first activity — succeeds | Activities tab is open; a section is collapsed | 1. Click the section arrow to expand it<br>2. Immediately click the first activity name | Section expands and the activity page opens successfully; no stale-state error appears | Medium |
| MS-ACT-011 | Activity name with 200+ chars and special characters is displayed and clickable | An activity with a 200+ character name containing special characters exists | 1. Open Activities tab<br>2. Locate the long-name activity row<br>3. Click the activity name | Activity name is displayed (possibly truncated) without overflow breaking the table layout; clicking the name opens the activity page | Low |
| MS-ACT-013 | Cannot click activity name in collapsed activity type section | Activities tab is open; at least one section is collapsed | 1. Locate a collapsed activity section<br>2. Attempt to click an activity name inside that collapsed section | Activity names inside the collapsed section are not visible or not clickable; no navigation occurs until the section is expanded | Medium |

---

## 9. Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-001 | Student profile details displayed | Student is logged in | 1. Open Profile | Initials icon, full name, message button, and optional description are visible | High |
| MS-PROFILE-002 | Profile information cards displayed | Profile page is open | 1. Inspect information cards | User details, privacy/policies, course details, miscellaneous, reports, and login activity are visible | High |
| MS-PROFILE-003 | Edit profile form opens | Profile page is open | 1. Click "Edit profile" | Edit profile form opens | High |
| MS-PROFILE-004 | Update own profile | Edit profile form is open | 1. Edit City/town and Description fields<br>2. Click "Update profile"<br>3. Reopen Profile | City/town and description updates are visible on profile | High |
| MS-PROFILE-015 | Open Data Retention Summary from Privacy and policies card | Profile page is open | 1. Click "Data Retention Summary" link | Data retention view opens | Low |
| MS-PROFILE-016 | Open Browser sessions report from Reports card | Profile page is open | 1. Click "Browser sessions" link | Browser sessions report opens | Medium |
| MS-PROFILE-017 | Compose a message to the user via the Message button | Profile page is open | 1. Click "Message" button | Message composer opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-007 | Student cannot edit another user's profile | Student opens another user's profile | 1. Inspect profile controls<br>2. Navigate directly to that user's edit-profile URL | Edit controls are not rendered and direct edit URL shows access denied before the edit form renders | High |
| MS-PROFILE-008 | Required profile field empty | Edit profile form is open | 1. Clear First name, Last name, or Email<br>2. Save | Required-field validation blocks save | High |
| MS-PROFILE-009 | Invalid profile email | Edit profile form is open | 1. Enter invalid email<br>2. Save | Email validation blocks save | High |
| MS-PROFILE-018 | Leave First name blank and attempt to Update profile | Edit profile form is open | 1. Clear First name<br>2. Update profile | Save is blocked with validation error on First name field | High |
| MS-PROFILE-020 | HTML/XSS injection in Profile Description is sanitised | Edit profile form is open | 1. Inject HTML script tags (e.g., `<script>alert(1)</script>`) into the Description<br>2. Click "Update profile" | HTML is sanitised or escaped; script does not execute when viewing the profile | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-010 | Cancel edit profile | Edit profile form has unsaved changes | 1. Click "Cancel" | Unsaved changes are discarded | Medium |
| MS-PROFILE-012 | Very long Description field (200+ chars) accepted or blocked with visible feedback | Edit profile form is open | 1. Enter a 200+ character string in the Description field<br>2. Click "Update profile" | Either the description is saved and visible on the profile page, or a clear validation message explains the length limit; no silent data loss or crash occurs | Low |
| MS-PROFILE-013 | Non-Latin Unicode and emoji in First/Last name fields accepted or blocked with visible feedback | Edit profile form is open | 1. Enter Unicode and emoji characters in the First name field and Last name field<br>2. Click "Update profile" | Either the names are saved and rendered correctly, or a clear validation message explains the character restriction; no garbled text or silent failure occurs | Low |
| MS-PROFILE-014 | Rapid re-submit of Update profile does not create duplicate profile records | Edit profile form is open with a change ready | 1. Click "Update profile" rapidly twice | Profile is saved once; no duplicate profile record is created and no duplicate success/error message is stacked | Medium |
| MS-PROFILE-021 | Rapid double-submit profile form | Edit profile form is open | 1. Click "Update profile" rapidly twice in succession | Profile updates exactly once; no duplicate records or stacked error messages appear | Medium |

---

## 10. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-001 | Logout from user menu | Student is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and login page is displayed | High |
| MS-LOGOUT-002 | Protected page requires re-authentication after logout | Student has logged out | 1. Navigate directly to Dashboard, course, or assignment URL | User is redirected to login | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-003 | Browser back after logout | Student logged out from protected page | 1. Press browser Back | Login page remains active or protected page immediately redirects to login; dashboard/course content is not rendered from browser cache | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-005 | Double-click logout | Student is logged in | 1. Double-click "Log out" | Logout completes once without visible error | Low |
| MS-LOGOUT-006 | Session timeout behaves like logout | Student session has expired | 1. Open protected page | User is required to authenticate again | High |
| MS-LOGOUT-007 | Logout in Tab A blocks protected page reload in Tab B | Student is logged in on two browser tabs showing a protected page | 1. In Tab A, log out via the user menu<br>2. Switch to Tab B<br>3. Reload the protected page in Tab B | Tab B redirects to the login page; no authenticated content from the previous session is rendered | High |
| MS-LOGOUT-008 | Multi-tab simultaneous logout | Student is logged in on two browser tabs | 1. Log out via the user menu in Tab A<br>2. Switch to Tab B and refresh the page | Tab B immediately redirects to the login page; session is terminated globally | High |
| MS-LOGOUT-009 | Logout immediately after login | Login page is visible | 1. Log in with valid credentials<br>2. Immediately click "Log out" upon reaching Dashboard | Session clears cleanly without any rapid-action caching or redirection issues | Low |

---

## Test Summary

| Area | Count |
|------|-------|
| Modules covered | 10 |
| Ground-truth test cases | 137 |
| Primary role | Student |
| Source functional description | dataset/functional_description/MoodleStudent.md |
