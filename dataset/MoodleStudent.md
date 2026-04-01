# Moodle Student

## Website URL

<http://localhost:8080> (local setup) / <https://school.moodledemo.net/> (reference demo)

## Navigation

Students navigate using the top bar (Home, Dashboard, My courses), course tabs, breadcrumbs, and the Course Index sidebar. The user menu provides Profile, Grades, Calendar, Reports, Preferences, and Log out.

## Functional Description

### 1. Login

The login page provides Username, Password, Log in, Lost password? (may be disabled), Access as a guest, and cookies notice controls. Valid student credentials redirect to Dashboard; invalid or empty input returns inline authentication or validation errors and keeps correction flow usable.

### 2. Dashboard

Dashboard shows a personalized greeting with Timeline and Calendar blocks. Students can view upcoming work, open Full calendar, create personal events where allowed, and observe empty states when no timeline work exists.

### 3. My Courses

My Courses displays enrolled courses as cards with search, filter, sort, and layout controls. Students can open a course, star it, or remove it from the current overview display, and list state should persist consistently after reload.

### 4. Course Page

Student course tabs typically include Course, Participants, Grades, Activities, and Competencies. Students can browse collapsible sections, open activities, use Collapse all, and jump via Course Index. Teacher-only settings and edit controls are not available.

### 5. Participants

Participants view lists enrolled users with name or role filters and profile links. Students can view participant information but cannot enroll users, edit roles, or perform course-level participant management; restricted controls should be hidden or blocked.

### 6. Adding Activities

Students can browse existing activities but cannot add activities/resources, open the teacher Activity Chooser, or use course authoring controls.

### 7. Course Settings

Course Settings is a teacher-managed area. Students can see course information presented on course pages but cannot edit course metadata, format, dates, or configuration values.

### 8. Assignment Submission

Students can open an assignment, review dates and instructions, and submit online text, file uploads, or both based on assignment configuration. Submission status, timestamps, and teacher feedback are shown after save and grading, with validation for required fields and size limits.

### 9. Assignment Review and Grading

Students can view their own submission state and returned feedback, but grading interfaces (submissions table, grading actions, quick grading, advanced grading forms) are not available.

### 10. Grades

Student Grades shows only the user report for the logged-in student, including activity grades, feedback, and course total. It is read-only and does not expose grader report controls or other students' grades; access isolation must hold across direct URL attempts.

### 11. Activities

Activities provides grouped activity lists (for example Assignments, Forums, Resources), each linking to the activity page. Students can review due dates and submission status where applicable.

### 12. Profile

Profile shows user details, course-related info, reports, and login activity. Edit profile allows updating permitted fields such as personal details, picture, interests, and optional profile metadata, with validation for required and unsupported values.

### 13. Logout

Log out ends the authenticated session and returns to the login page. Accessing protected pages afterward requires re-authentication.
