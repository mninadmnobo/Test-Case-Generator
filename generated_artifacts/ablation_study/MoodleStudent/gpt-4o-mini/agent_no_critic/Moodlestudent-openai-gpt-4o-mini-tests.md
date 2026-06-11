# Test Cases — Moodlestudent

Generated: 2026-06-10T21:42:20.844479Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 116 | 43 | 33 | 40 | 36 | 55 | 16 |

## Login

Total: **15** (positive: 4, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log in with valid credentials | User logged in as <Student> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |
| TC-002 | WF-002 | Log in with invalid credentials | User logged in as <Student> | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | shows inline error message | high |
| TC-003 | WF-003 | Access as a guest | User logged in as <Guest> | 1. Click Access as a guest | Allows unauthenticated browsing | medium |
| TC-004 | WF-004 | View cookies notice | User logged in as <Student> | 1. Click Cookies notice | Provides cookie usage information | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-006 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-008 |  | Submit with invalid Username format |  | 1. Enter <invalid username format> in the Username field<br>2. Fill the Password field with <valid password><br>3. Click Log in | Inline error message is shown; password field is cleared and username is retained for correction | medium |
| TC-009 |  | Submit with invalid Password format |  | 1. Fill the Username field with <valid username><br>2. Enter <invalid password format> in the Password field<br>3. Click Log in | Inline error message is shown; password field is cleared and username is retained for correction | medium |
| TC-010 |  | Attempt to log in as a guest without authentication |  | 1. Click Access as a guest | Allows unauthenticated browsing | medium |
| TC-011 |  | Attempt to view cookies notice |  | 1. Click Cookies notice | Provides cookie usage information | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-002 | Enter empty Username and Password |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message is shown indicating that both fields are required; password field is cleared. | medium |
| TC-013 (input_edge) |  | Enter long Username and Password |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a string of 200+ characters in the Password field<br>3. Click Log in | Inline error message is shown indicating that the input exceeds the maximum allowed length. | low |
| TC-014 (input_edge) |  | Enter Username with special characters |  | 1. Enter a Username containing special characters (e.g., !@#$%^&*)<br>2. Enter a valid Password<br>3. Click Log in | Inline error message is shown indicating that the Username contains invalid characters. | low |
| TC-015 (state_edge) | WF-001 | Rapid consecutive logins with valid credentials |  | 1. Enter valid Username<br>2. Enter valid Password<br>3. Click Log in<br>4. Immediately click Log in again after redirection to Dashboard | User remains on the Dashboard; no second login attempt is processed. | medium |

---

## Dashboard

Total: **21** (positive: 10, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar event | User logged in as <Role>, Edit mode is enabled | 1. Click the 'New Event' button | A personal calendar entry is created | high |
| TC-002 | WF-002 | Navigate to previous month | User logged in as <Role> | 1. Click the 'Previous Month' button | The calendar displays the previous month | medium |
| TC-003 | WF-003 | Navigate to next month | User logged in as <Role> | 1. Click the 'Next Month' button | The calendar displays the next month | medium |
| TC-004 | WF-004 | Reset dashboard to default settings | User logged in as <Role>, Edit mode is enabled | 1. Click the 'Reset page to default' button | The dashboard resets to default settings | high |
| TC-005 | WF-005 | Add a new block | User logged in as <Role>, Edit mode is enabled | 1. Click the '+ Add a block' button | A page listing all available block types opens | medium |
| TC-006 | WF-006 | Configure existing block | User logged in as <Role> | 1. Click the three-dot menu on an existing block<br>2. Select 'Configure' | Configuration options for the block open | medium |
| TC-007 | WF-007 | Move existing block | User logged in as <Role> | 1. Click the three-dot menu on an existing block<br>2. Select 'Move' | The block moving process is initiated | medium |
| TC-008 | WF-008 | Delete existing block | User logged in as <Role> | 1. Click the three-dot menu on an existing block<br>2. Select 'Delete' | The block is removed from the dashboard | medium |
| TC-009 | WF-009 | Open full calendar view | User logged in as <Role> | 1. Click the 'Full calendar' link | The dedicated calendar view opens | medium |
| TC-010 | WF-010 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or export calendars' link | The calendar data management opens | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Attempt to create a new calendar event without filling required fields |  | 1. Click on the 'New event' button | Form does not submit; no calendar entry is created; error shown on the required fields |  |
| TC-012 |  | Attempt to reset the dashboard while not in Edit mode | User is not in Edit mode | 1. Click on the 'Reset page to default' button | Status remains unchanged; no reset occurs; error message displayed indicating action is not allowed |  |
| TC-013 |  | Attempt to add a new block while not in Edit mode | User is not in Edit mode | 1. Click on the '+ Add a block' button | Status remains unchanged; no block is added; error message displayed indicating action is not allowed |  |
| TC-014 |  | Attempt to navigate to the previous month while no events are present |  | 1. Click on the 'Previous Month' button | Status remains unchanged; no navigation occurs; error message displayed indicating no events found |  |
| TC-015 |  | Attempt to navigate to the next month while no events are present |  | 1. Click on the 'Next Month' button | Status remains unchanged; no navigation occurs; error message displayed indicating no events found |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (state_edge) | WF-004 | Rapid consecutive state transitions between Edit and default states | User is in Edit mode | 1. Click 'Reset page to default'<br>2. Immediately click 'Reset page to default' again | Second reset action is blocked; a message indicates the dashboard is already at default settings | medium |
| TC-017 (boundary) | WF-005 | Attempt to add a block in Edit mode when no blocks exist | User is in Edit mode, No blocks are currently added | 1. Click '+ Add a block' | Opens page listing all available block types; user can select a block to add | medium |
| TC-018 (input_edge) |  | Search activities with special characters |  | 1. Enter special characters in the 'Search Activities' field | Search results are displayed or a specific error is shown indicating invalid characters | low |
| TC-019 (input_edge) |  | Search activities with leading/trailing whitespace |  | 1. Enter leading and trailing spaces in the 'Search Activities' field | Leading/trailing whitespace is trimmed; saved value shown in the search results has no extra spaces | low |
| TC-020 (interaction_edge) | WF-002 | Navigate to previous month rapidly |  | 1. Click 'Previous Month'<br>2. Immediately click 'Previous Month' again | Second navigation attempt is blocked; the calendar remains on the current month | medium |
| TC-021 (interaction_edge) | WF-003 | Navigate to next month rapidly |  | 1. Click 'Next Month'<br>2. Immediately click 'Next Month' again | Second navigation attempt is blocked; the calendar remains on the current month | medium |

---

## My Courses

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Student>, At least one course is displayed in the Course Grid | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' from the menu | A success message is shown; the course is pinned to the top of the Course Grid | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Student>, At least one course is displayed in the Course Grid | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' from the menu | A success message is shown; the course is no longer visible in the Course Grid | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to star a course without being logged in | User is not authenticated | 1. Navigate to the My Courses page<br>2. Click on 'Star this course' for any course | User is redirected to the login page | high |
| TC-004 |  | Attempt to remove a course from view without being logged in | User is not authenticated | 1. Navigate to the My Courses page<br>2. Click on 'Remove from view' for any course | User is redirected to the login page | high |
| TC-005 | WF-001 | Attempt to star a course when the user is not enrolled | User is not enrolled in the course | 1. Navigate to the My Courses page<br>2. Click on 'Star this course' for a course | Action is blocked; no course is starred | medium |
| TC-006 | WF-002 | Attempt to remove a course from view that is already hidden | Course is already hidden | 1. Navigate to the My Courses page<br>2. Click on 'Remove from view' for the hidden course | Action is blocked; course remains hidden | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly star a course twice | User is on the My Courses page with at least one course displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Star this course'<br>3. Immediately click the three-dot menu again on the same course card<br>4. Click 'Star this course' again | Only one success message is shown; the course remains starred without duplication. | medium |
| TC-008 (interaction_edge) | WF-002 | Rapidly remove a course from view twice | User is on the My Courses page with at least one course displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Remove from view'<br>3. Immediately click the three-dot menu again on the same course card<br>4. Click 'Remove from view' again | Only one success message is shown; the course is removed from view without duplication. | medium |
| TC-009 (input_edge) |  | Search with leading and trailing whitespace | User is on the My Courses page | 1. Enter '   Course Name   ' in the Search field<br>2. Press Enter | Search results display correctly without leading or trailing spaces in the displayed course names. | low |
| TC-010 (input_edge) |  | Search with special characters | User is on the My Courses page | 1. Enter '@#Course$%^' in the Search field<br>2. Press Enter | Search results display correctly, either showing no results or relevant courses without errors. | low |

---

## Course Page

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Collapse all sections | User logged in as <Student> | 1. Click the 'Collapse all' link | All sections are collapsed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to collapse all sections while in Edit mode | User is in Edit mode | 1. Click on the 'Collapse all' link | Action is blocked; no sections are collapsed; user remains in Edit mode. | high |
| TC-003 |  | Attempt to submit a section with empty Activity Resource Name |  | 1. Leave the Activity Resource Name blank<br>2. Attempt to save the section | Form does not submit; Activity Resource Name is highlighted; inline validation error appears indicating it is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Collapse all sections after adding maximum allowed entries | At least one section is present with activities and resources | 1. Add the maximum allowed number of sections to the course page<br>2. Click the 'Collapse all' link | All sections are collapsed; no sections remain expanded | medium |
| TC-005 (interaction_edge) |  | Rapid collapse and expand actions | At least one section is present | 1. Click the 'Collapse all' link<br>2. Immediately click the 'Collapse all' link again | No error occurs; all sections remain collapsed | low |
| TC-006 (input_edge) |  | Add section with maximum length name | No sections currently exist | 1. Add a new section with a name that is 255 characters long | Section is created successfully and displayed with the full name | medium |
| TC-007 (input_edge) |  | Add section with special characters in name | No sections currently exist | 1. Add a new section with a name containing special characters like @#$%^&*() | Section is created successfully and displayed with the special characters in the name | low |

---

## Participants

Total: **13** (positive: 5, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Clear all filters | User logged in as <Role> | 1. Click 'Clear Filters' button | Filters cleared | high |
| TC-002 | WF-002 | Apply filters successfully | User logged in as <Role> | 1. Select <attribute> from the Select Attribute dropdown<br>2. Click 'Apply Filters' button | Filters applied | high |
| TC-003 | WF-003 | View participant profile | User logged in as <Role>, Participants table is visible | 1. Click on a participant's First Name or Last Name | Profile displayed | high |
| TC-004 | WF-004 | Filter participants by First Name | User logged in as <Role>, Participants table is visible | 1. Click 'First Name' alphabetical filter button | Filtered by First Name | medium |
| TC-005 | WF-005 | Filter participants by Last Name | User logged in as <Role>, Participants table is visible | 1. Click 'Last Name' alphabetical filter button | Filtered by Last Name | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to apply filters without any conditions set |  | 1. Leave all filter fields blank<br>2. Click 'Apply Filters' | Form does not submit; no filters applied; error shown indicating that at least one condition must be set | high |
| TC-007 | WF-002 | Attempt to clear filters when no filters are set |  | 1. Ensure no filters are currently applied<br>2. Click 'Clear Filters' | No action occurs; filters remain unchanged; message indicating no filters to clear | medium |
| TC-008 | WF-004 | Attempt to filter by First Name without selecting a name |  | 1. Click 'Filter by First Name' | No action occurs; filters remain unchanged; message indicating a name must be selected to filter | medium |
| TC-009 | WF-005 | Attempt to filter by Last Name without selecting a name |  | 1. Click 'Filter by Last Name' | No action occurs; filters remain unchanged; message indicating a name must be selected to filter | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (interaction_edge) | WF-001 | Rapid re-submission of Clear Filters | Filters are applied | 1. Click 'Clear Filters'<br>2. Immediately click 'Clear Filters' again | Filters are cleared; the form shows no filters applied. | medium |
| TC-011 (interaction_edge) | WF-002 | Rapid re-submission of Apply Filters | Filters are set | 1. Click 'Apply Filters'<br>2. Immediately click 'Apply Filters' again | Filters are applied; the table shows filtered results without duplicates. | medium |
| TC-012 (interaction_edge) | WF-004 | Filter by First Name with empty selection | No filters applied | 1. Click 'First Name' filter button<br>2. Observe the table | Table displays all participants sorted by First Name. | medium |
| TC-013 (interaction_edge) | WF-005 | Filter by Last Name with empty selection | No filters applied | 1. Click 'Last Name' filter button<br>2. Observe the table | Table displays all participants sorted by Last Name. | medium |

---

## Grades

Total: **6** (positive: 2, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display student's grades in the Grades table | User logged in as <Student>, User has grades recorded for the course | 1. Navigate to the Grades page | The Grades table displays the student's grades with columns for Grade item, Calculated weight, Grade, Range, Percentage, Feedback, and Contribution to course total | high |
| TC-002 |  | Display aggregation course total | User logged in as <Student>, User has grades recorded for the course | 1. Navigate to the Grades page | The AGGREGATION Course total row displays the cumulative grade across all weighted items | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user attempts to access the Grades page |  | 1. Navigate to the Grades page without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Enter a very long string in the Feedback column |  | 1. Navigate to the Grades page<br>2. Enter a string of 200+ characters in the Feedback column | Feedback column displays the entered text correctly or truncates it with an indication | low |
| TC-005 (input_edge) |  | Enter special characters in the Grade column |  | 1. Navigate to the Grades page<br>2. Enter special characters in the Grade column | Grade column displays an error indicating invalid input or accepts the special characters | low |
| TC-006 (input_edge) |  | Enter leading and trailing whitespace in the Grade item |  | 1. Navigate to the Grades page<br>2. Enter a Grade item with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved value shown in the table has no extra spaces | low |

---

## Assignment

Total: **12** (positive: 5, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open submission form | User logged in as <Student> | 1. Click Add submission button | Submission form opens | high |
| TC-002 | WF-002 | Submit with Online Text Editor | User logged in as <Student>, Submission form is open | 1. Enter text in the Online Text Editor<br>2. Click Submit | Submission created | high |
| TC-003 | WF-003 | Submit with File Upload | User logged in as <Student>, Submission form is open | 1. Upload a valid file in the File Upload area<br>2. Click Submit | Submission created | high |
| TC-004 | WF-004 | View submission | User logged in as <Student>, Due date has not passed, Teacher permits resubmission | 1. Click View in the Submission Status Section | Submission details displayed | medium |
| TC-005 | WF-005 | Edit submission | User logged in as <Student>, Due date has not passed, Teacher permits resubmission | 1. Click Edit in the Submission Status Section | Submission form opened for editing | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to open submission form without any preconditions met |  | 1. Click on the Add submission button | Submission form does not open; no action occurs | high |
| TC-007 | WF-004 | Attempt to view submission after due date has passed | due date has passed | 1. Click on the View button for a submission | View action is blocked; no submission details are displayed | high |
| TC-008 | WF-005 | Attempt to edit submission when teacher does not permit resubmission | teacher does not permit resubmission | 1. Click on the Edit button for a submission | Edit action is blocked; no submission form opens for editing | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (interaction_edge) | WF-001 | Rapid re-submission after opening the submission form |  | 1. Click the 'Add submission' button<br>2. Immediately click the 'Add submission' button again | The submission form opens successfully without errors |  |
| TC-010 (input_edge) |  | Long text input in the online text editor |  | 1. Click the 'Add submission' button<br>2. Enter a string of 200+ characters in the Online Text Editor | The text is accepted and displayed correctly in the submission details |  |
| TC-011 (data_edge) |  | File upload at exact size limit |  | 1. Click the 'Add submission' button<br>2. Upload a file that is exactly at the size limit | The file is uploaded successfully with a visible success indicator |  |
| TC-012 (data_edge) |  | File upload one byte over the size limit |  | 1. Click the 'Add submission' button<br>2. Upload a file that is one byte over the size limit | An error is shown indicating the file exceeds the size limit |  |

---

## Activities

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Navigate to Activity from Assignments Section | User logged in as <Role> | 1. Click on the activity name in the Assignments section | redirects to activity's page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to navigate to an activity without clicking any link |  | 1. Load the Activities page<br>2. Do not click any activity name | No navigation occurs; the user remains on the Activities page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid navigation to activity after clicking link | User is on the Activities page, Assignments section is visible | 1. Click on an activity name in the Assignments section<br>2. Immediately click on another activity name in the Assignments section | User is redirected to the second activity's page; the first activity's navigation does not occur. | medium |
| TC-004 (input_edge) |  | Long text in activity name | User is on the Activities page, Assignments section is visible | 1. Observe the activity names in the Assignments section<br>2. Verify if any activity name exceeds 200 characters | Activity names are either truncated or display an error indicating the name is too long. | low |
| TC-005 (input_edge) |  | Special characters in activity name | User is on the Activities page, Assignments section is visible | 1. Check for activity names containing special characters or emojis | Activity names with special characters are displayed correctly or an error is shown. | low |

---

## Profile

Total: **23** (positive: 12, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send a message | User logged in as <Student> | 1. Click the 'Message' button | Message sent | high |
| TC-002 | WF-002 | Open profile form | User logged in as <Student> | 1. Click the 'Edit Profile' link | Profile form opened | high |
| TC-003 | WF-003 | View data retention summary | User logged in as <Student> | 1. Click the 'Data Retention Summary' link | Data retention summary displayed | medium |
| TC-004 | WF-004 | View course profiles | User logged in as <Student> | 1. Click the 'Course Details' link | Course profiles displayed | medium |
| TC-005 | WF-005 | View blog entries | User logged in as <Student> | 1. Click the 'Blog Entries' link | Blog entries displayed | medium |
| TC-006 | WF-006 | View forum posts | User logged in as <Student> | 1. Click the 'Forum Posts' link | Forum posts displayed | medium |
| TC-007 | WF-007 | View forum discussions | User logged in as <Student> | 1. Click the 'Forum Discussions' link | Forum discussions displayed | medium |
| TC-008 | WF-008 | View learning plans | User logged in as <Student> | 1. Click the 'Learning Plans' link | Learning plans displayed | medium |
| TC-009 | WF-009 | View browser sessions | User logged in as <Student> | 1. Click the 'Browser Sessions' link | Browser sessions displayed | medium |
| TC-010 | WF-010 | View grades overview | User logged in as <Student> | 1. Click the 'Grades Overview' link | Grades overview displayed | medium |
| TC-011 | WF-011 | Update profile with valid data | User logged in as <Student>, Profile form is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid email> in the Email Address field<br>4. Click 'Update Profile' | saves profile changes | high |
| TC-012 | WF-012 | Cancel profile update | User logged in as <Student>, Profile form is open | 1. Click 'Cancel' | exits without changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 | WF-011 | Attempt to update profile with required fields empty |  | 1. Click on the 'Edit Profile' link<br>2. Leave the First Name, Last Name, and Email Address fields blank<br>3. Click 'Update Profile' | Form does not submit; error shown on First Name, Last Name, and Email Address fields indicating they are required | high |
| TC-014 | WF-011 | Attempt to update profile with only required fields empty |  | 1. Click on the 'Edit Profile' link<br>2. Leave all required fields empty<br>3. Click 'Update Profile' | Form does not submit; error shown on First Name, Last Name, and Email Address fields indicating they are required | high |
| TC-015 | WF-011 | Attempt to update profile with invalid email format |  | 1. Click on the 'Edit Profile' link<br>2. Enter <invalid email format> in the Email Address field<br>3. Fill in valid values for First Name and Last Name<br>4. Click 'Update Profile' | Form does not submit; error shown on Email Address field indicating it must be a valid email address | medium |
| TC-016 | WF-011 | Attempt to update profile with duplicate email |  | 1. Click on the 'Edit Profile' link<br>2. Enter <existing email> in the Email Address field<br>3. Fill in valid values for First Name and Last Name<br>4. Click 'Update Profile' | Form does not submit; error shown on Email Address field indicating it must be unique | medium |
| TC-017 | WF-012 | Attempt to cancel profile update without making changes |  | 1. Click on the 'Edit Profile' link<br>2. Click 'Cancel' | Exits without changes; profile remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-011 | Update profile with all required fields filled correctly | User is logged in, Profile form is opened | 1. Enter valid value in the First Name field<br>2. Enter valid value in the Last Name field<br>3. Enter valid email address in the Email Address field<br>4. Click Update Profile | Profile updates successfully; changes are saved | medium |
| TC-019 (boundary) | WF-011 | Attempt to update profile with missing required fields | User is logged in, Profile form is opened | 1. Leave First Name field empty<br>2. Leave Last Name field empty<br>3. Leave Email Address field empty<br>4. Click Update Profile | Profile update is blocked; error messages indicate required fields are missing | medium |
| TC-020 (input_edge) |  | Enter a very long description in the Description field | User is logged in, Profile form is opened | 1. Enter a string of 200+ characters in the Description field<br>2. Click Update Profile | Form submits successfully; the saved description displays the full text or is truncated with a visible indicator | low |
| TC-021 (input_edge) |  | Enter special characters in the First Name field | User is logged in, Profile form is opened | 1. Enter special characters (e.g., @#&*) in the First Name field<br>2. Click Update Profile | Profile update is blocked; an error message indicates invalid characters | low |
| TC-022 (input_edge) |  | Enter leading and trailing whitespace in the Email Address field | User is logged in, Profile form is opened | 1. Enter '   user@example.com   ' in the Email Address field<br>2. Click Update Profile | Leading/trailing whitespace is trimmed; saved email address shows 'user@example.com' | low |
| TC-023 (interaction_edge) | WF-012 | Cancel profile update and verify no changes are made | User is logged in, Profile form is opened | 1. Enter changes in the First Name field<br>2. Click Cancel | User exits without changes; profile page displays original First Name | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click Logout_Button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | user must be authenticated | 1. Ensure the user is not authenticated<br>2. Click the Logout button | Logout action is blocked; user remains on the current page and is not logged out | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Attempt to log out when not authenticated | user is not authenticated | 1. Click the Logout button | Logout action is blocked; user remains on the current page with a visible error indicating the user must be authenticated to log out. | medium |
| TC-004 (interaction_edge) | WF-001 | Rapid consecutive logout attempts | user is authenticated | 1. Click the Logout button<br>2. Immediately click the Logout button again | First logout terminates the session and redirects to the login page; second attempt is ignored or blocked. | medium |

---
