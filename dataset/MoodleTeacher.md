# Moodle Teacher

## Website URL

<http://localhost:8080> (local setup) / <https://school.moodledemo.net/> (reference demo)

## Navigation

Teachers navigate with the top bar (Home, Dashboard, My courses), course tabs, breadcrumbs, and Course Index. The user menu includes Profile, Grades, Calendar, Reports, Preferences, and Log out. Teacher courses expose authoring and management controls not available to students.

## Functional Description

### 1. Login

The login page includes Username, Password, Log in, guest access (if enabled), and cookie notice controls. Valid teacher credentials redirect to Dashboard; invalid or empty input returns authentication or validation errors with clear correction flow.

### 2. Dashboard

Dashboard shows Timeline and Calendar blocks with course/event navigation. In edit mode, teachers can add blocks, reorder blocks, open block options, and reset the page layout to default; no-data timeline states should remain stable.

### 3. My Courses

My Courses lists accessible courses with search, filter, sort, and layout controls. Teachers can open a course, star it, or remove it from the current overview display.

### 4. Course Page

Teacher course tabs typically include Course, Settings, Participants, Grades, Activities, and More. Teachers can browse sections, use Course Index, and manage course content when edit mode is enabled, including section-level and activity-level actions.

### 5. Participants

Participants management provides enrolled-user lists, filter conditions, profile links, role and group visibility, and bulk actions. Teachers can enroll users and manage roles according to permissions, with proper handling for unmatched filters and multi-condition searches.

### 6. Adding Activities

With edit mode enabled, teachers can add an activity or resource from the Activity Chooser (for example Assignment, Forum, Quiz, File, Page, URL). Chooser search/filter controls and add actions support structured course authoring with validation when required fields are missing.

### 7. Course Settings

Course settings include full name, short name, category, visibility, dates, summary, format, appearance, upload limits, completion tracking, groups, and tags. Required fields and invalid values trigger inline validation.

### 8. Assignment Submission

Teachers configure how students submit assignments by setting availability windows, submission types (online text and/or files), limits, and related validation behavior. The teacher view also shows assignment status and submission progress across learners, including no-submission and late-submission states.

### 9. Assignment Review and Grading

Teacher assignment pages include grading summary, submissions table, search/filter controls, grading status, and grade/feedback workflows. Quick grading and advanced grading (such as rubric) are available where configured, with expected fallback when advanced forms are invalid or unpublished.

### 10. Grades

The gradebook (grader report) provides student rows, graded-activity columns, editable grade cells, and save actions with grade-range validation. Report filters and overall calculations support monitoring class performance, and invalid grade inputs should block save with clear feedback.

### 11. Activities

Activities view groups course activities by type and links to each item. Teachers can review activity status and navigate directly to activity configuration or content pages.

### 12. Profile

Profile and Edit profile expose account details, reports, login activity, and user picture/preferences updates. Teachers can modify permitted profile fields but not platform-level admin controls, and invalid profile inputs should be validated before save.

### 13. Logout

Log out ends the current session and redirects to login. Protected course and grading pages require authentication after logout.
