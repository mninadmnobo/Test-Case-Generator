# Test Cases — Moodlestudent

Generated: 2026-06-10T21:41:26.501763Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 101 | 33 | 34 | 34 | 38 | 34 | 21 |

## Login

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <Student> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with a valid password<br>3. Click 'Log in' | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with a valid username<br>2. Leave the Password field blank<br>3. Click 'Log in' | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click 'Log in' | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Submit with an invalid Password format |  | 1. Fill the Username field with a valid username<br>2. Fill the Password field with an invalid format<br>3. Click 'Log in' | Inline error message shows indicating invalid credentials; Password field is cleared and Username is retained | medium |
| TC-006 |  | Attempt to access the Lost password link |  | 1. Click on the 'Lost password?' link | No action occurs; the link is disabled | medium |
| TC-007 |  | Attempt to access the Login page as an unauthenticated user |  | 1. Attempt to access the Login page without logging in | User is redirected to the Login page; no access granted | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message shown indicating the username is too long or the form submits successfully with the username truncated. | low |
| TC-009 (input_edge) |  | Enter special characters in the username |  | 1. Enter '@#$%^&*()' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message shown indicating invalid characters in the username or the form submits successfully. | low |
| TC-010 (input_edge) |  | Enter leading and trailing whitespace in the username |  | 1. Enter '   username   ' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Leading/trailing whitespace is trimmed; saved value shown on the dashboard has no extra spaces. | low |
| TC-011 (state_edge) |  | Rapid consecutive submissions with valid and invalid credentials |  | 1. Enter a valid username in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in<br>4. Immediately click Log in again | First submission redirects to Dashboard; second submission is blocked with an inline error message indicating the user is already logged in. | medium |

---

## Dashboard

Total: **20** (positive: 10, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display upcoming activities in Timeline block | User logged in as <User Role>, Timeline block is visible | 1. Select 'Next 7 days' from the Time Range dropdown<br>2. Observe the Timeline block | The Timeline block displays upcoming activities and deadlines for the next 7 days. | high |
| TC-002 |  | Display empty state in Timeline block | User logged in as <User Role>, Timeline block is visible | 1. Select 'Next 7 days' from the Time Range dropdown<br>2. Ensure there are no activities in the selected range<br>3. Observe the Timeline block | The message 'No activities found in the selected range.' is displayed in the Timeline block. | high |
| TC-003 |  | Create a new event in Calendar block | User logged in as <User Role>, Calendar block is visible | 1. Click the 'New Event' button in the Calendar block<br>2. Fill in the event details<br>3. Save the event | The new event appears in the Calendar block for the current month. | high |
| TC-004 |  | Navigate to previous month in Calendar block | User logged in as <User Role>, Calendar block is visible | 1. Click the 'Left Arrow' button in the Month Navigation<br>2. Observe the Calendar block | The Calendar block displays the previous month. | medium |
| TC-005 |  | Navigate to next month in Calendar block | User logged in as <User Role>, Calendar block is visible | 1. Click the 'Right Arrow' button in the Month Navigation<br>2. Observe the Calendar block | The Calendar block displays the next month. | medium |
| TC-006 |  | Open full calendar view from Links | User logged in as <User Role>, Links are visible | 1. Click on the 'Full calendar' link | The dedicated calendar view opens. | medium |
| TC-007 |  | Open calendar data management from Links | User logged in as <User Role>, Links are visible | 1. Click on the 'Import or export calendars' link | The calendar data management page opens. | medium |
| TC-008 |  | Enable Edit mode and observe changes | User logged in as <User Role>, Dashboard is visible | 1. Toggle on Edit mode<br>2. Observe the Dashboard | The 'Reset page to default' button and '+ Add a block' button are visible. | high |
| TC-009 |  | Reset page to default in Edit mode | User logged in as <User Role>, Edit mode is enabled | 1. Click the 'Reset Page' button | The Dashboard resets to its default state. | medium |
| TC-010 |  | Open block type listing in Edit mode | User logged in as <User Role>, Edit mode is enabled | 1. Click the '+ Add a block' button | A page listing all available block types opens. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Attempt to submit with Sort Order dropdown empty |  | 1. Leave the Sort Order dropdown blank<br>2. Select a time range from the Time Range dropdown<br>3. Enter a search term in the Search Field<br>4. Click on the search button | Form does not submit; Sort Order field is highlighted with an error indicating it is required | high |
| TC-012 |  | Attempt to submit with All Courses dropdown empty |  | 1. Leave the All Courses dropdown blank<br>2. Click on the New Event Button | Form does not submit; All Courses field is highlighted with an error indicating it is required | high |
| TC-013 |  | Attempt to navigate to previous month without any events |  | 1. Click on the Left Arrow button | No events are displayed for the previous month; empty state message is shown | medium |
| TC-014 |  | Attempt to navigate to next month without any events |  | 1. Click on the Right Arrow button | No events are displayed for the next month; empty state message is shown | medium |
| TC-015 |  | Attempt to access Full calendar link without proper permissions |  | 1. Click on the Full calendar link | Access denied message is displayed; user is not redirected to the calendar view | medium |
| TC-016 |  | Attempt to access Import or export calendars link without proper permissions |  | 1. Click on the Import or export calendars link | Access denied message is displayed; user is not redirected to the calendar data management | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (input_edge) |  | Search field with long input |  | 1. Enter a string longer than 200 characters in the Search_Field | Search field displays an error indicating the input exceeds the maximum allowed length | low |
| TC-018 (input_edge) |  | Search field with special characters |  | 1. Enter special characters (e.g., @#$%^&*) in the Search_Field | Search field displays an error indicating invalid characters or accepts the input and displays results accordingly | low |
| TC-019 (interaction_edge) |  | Rapid month navigation |  | 1. Click the Right Arrow button to navigate to the next month<br>2. Immediately click the Right Arrow button again | Calendar block updates to show the next month without delay or displays a loading indicator while processing | medium |
| TC-020 (input_edge) |  | Leading and trailing whitespace in search field |  | 1. Enter a value with leading and trailing spaces in the Search_Field | Leading/trailing whitespace is trimmed; saved value shown in the search results has no extra spaces | low |

---

## My Courses

Total: **15** (positive: 7, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Filter courses by status 'In progress' | User logged in as <Student> | 1. Select 'In progress' from the Status dropdown | Only courses with status 'In progress' are displayed in the course grid; unrelated courses are no longer visible | high |
| TC-002 |  | Search for a specific course | User logged in as <Student> | 1. Enter <course name> in the Search field | Only courses matching <course name> are displayed in the course grid; unrelated courses are no longer visible | high |
| TC-003 |  | Sort courses by name | User logged in as <Student> | 1. Select <sort option> from the Sort dropdown | Courses are displayed in sorted order based on <sort option> | medium |
| TC-004 |  | Change layout to List | User logged in as <Student> | 1. Select 'List' from the Layout dropdown | Courses are displayed in a List layout | medium |
| TC-005 |  | Star a course | User logged in as <Student> | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' | The course is pinned to the top of the course grid | high |
| TC-006 |  | Remove a course from view | User logged in as <Student> | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' | The course is no longer visible in the course grid | high |
| TC-007 |  | Navigate to course details by clicking course name | User logged in as <Student> | 1. Click on the course name link of a course card | User is navigated to the main page of the selected course | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the Search field blank and submit |  | 1. Leave the Search field blank<br>2. Click the Search button | No courses are displayed; the Search field remains empty |  |
| TC-009 |  | Select an invalid option in the Status dropdown |  | 1. Select an invalid option in the Status dropdown<br>2. Click the Apply button | No courses are displayed; the Status dropdown reverts to the previous valid selection |  |
| TC-010 |  | Select an invalid option in the Sort dropdown |  | 1. Select an invalid option in the Sort dropdown<br>2. Click the Apply button | No courses are displayed; the Sort dropdown reverts to the previous valid selection |  |
| TC-011 |  | Select an invalid option in the Layout dropdown |  | 1. Select an invalid option in the Layout dropdown<br>2. Click the Apply button | Layout remains unchanged; the Layout dropdown reverts to the previous valid selection |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) |  | Search with a long string |  | 1. Enter a very long string (200+ characters) in the Search field<br>2. Press Enter or click the search button | Search results display with the long string; if truncated, a visible indicator shows truncation. | low |
| TC-013 (input_edge) |  | Search with special characters |  | 1. Enter special characters (e.g., '!@#$%^&*()') in the Search field<br>2. Press Enter or click the search button | Search results display; if invalid, an error message indicates invalid input. | low |
| TC-014 (input_edge) |  | Search with leading/trailing whitespace |  | 1. Enter a course name with leading and trailing spaces in the Search field<br>2. Press Enter or click the search button | Search results display without leading/trailing spaces; saved value in the Search field shows trimmed output. | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after search |  | 1. Perform a search for a course<br>2. Quickly press the search button again before results load | The second search attempt is blocked; the first search results are displayed without duplication. | medium |

---

## Course Page

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Collapse all sections | User logged in as <Student>, Course page is open | 1. Click 'Collapse all' link | All sections are collapsed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to enable Edit mode on the course page |  | 1. Navigate to the Course Page<br>2. Attempt to enable Edit mode | User is blocked from enabling Edit mode; no changes are made to the course page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapidly click 'Collapse all' multiple times | Course page is loaded with multiple sections expanded | 1. Click 'Collapse all' link<br>2. Immediately click 'Collapse all' link again | 'Collapse all' action succeeds; all sections are collapsed without error message shown | medium |
| TC-004 (interaction_edge) |  | Click 'Collapse all' after all sections are already collapsed | Course page is loaded with all sections collapsed | 1. Click 'Collapse all' link | No visible change occurs; all sections remain collapsed | low |

---

## Participants

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Apply filters with Any toggle checked | User logged in as <Student> | 1. Check the Any toggle<br>2. Click Apply filters | Participants table displays users matching the applied filter conditions | high |
| TC-002 |  | Clear filters | User logged in as <Student> | 1. Click Clear filters | Participants table displays all users enrolled in the course | high |
| TC-003 |  | View participant profile | User logged in as <Student> | 1. Click on a participant's First name or Last name in the Participants table | Profile page of the selected participant is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to apply filters without any conditions |  | 1. Leave all filter fields empty<br>2. Click 'Apply filters' | No filters are applied; the participants table remains unchanged |  |
| TC-005 |  | Attempt to clear filters when no filters are set |  | 1. Click 'Clear filters' | No filters are cleared; the participants table remains unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) |  | Rapidly apply filters after clearing | User has added conditions to the filter system | 1. Click 'Clear filters' button<br>2. Immediately click 'Apply filters' button | Filters are applied as if no conditions were set; the participants table displays all users without any filters applied. | medium |
| TC-007 (interaction_edge) |  | Attempt to apply filters without conditions | User has not added any conditions | 1. Click 'Apply filters' button | Filters are applied; the participants table remains unchanged as no conditions were set. | medium |
| TC-008 (input_edge) |  | Add a condition with special characters | User is in the filter system | 1. Click '+ Add condition' link<br>2. Enter special characters in the condition input field | Condition is accepted and displayed in the filter system, indicating that special characters are allowed. | low |
| TC-009 (input_edge) |  | Add a condition with leading/trailing whitespace | User is in the filter system | 1. Click '+ Add condition' link<br>2. Enter a condition with leading and trailing spaces | Condition is trimmed; the saved condition in the filter system shows no extra spaces. | low |

---

## Grades

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View grades for the course | User logged in as <Student>, User is enrolled in the course | 1. Navigate to the Grades page | The Grades table displays the student's grades including 'Course Name' with a grade of '85', and the 'AGGREGATION Course total' shows '82%' for the cumulative grade. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access grades without authentication |  | 1. Navigate to the Grades page without logging in | User is redirected to the login page |  |
| TC-003 |  | Attempt to view another student's grades |  | 1. Log in as a student<br>2. Attempt to access the grades of another student | Access is denied; user cannot view other students' grades |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Enter a very long feedback string |  | 1. Navigate to the Grades page<br>2. Expand the Grade item row<br>3. Enter a feedback string longer than 200 characters in the Feedback column | Feedback input is either accepted or truncated with a visible indicator | low |
| TC-005 (input_edge) |  | Enter special characters in the Feedback field |  | 1. Navigate to the Grades page<br>2. Expand the Grade item row<br>3. Enter special characters (e.g., @#$%^&*) in the Feedback column | Feedback input is accepted or an error message is displayed | low |
| TC-006 (input_edge) |  | Enter leading and trailing whitespace in the Feedback field |  | 1. Navigate to the Grades page<br>2. Expand the Grade item row<br>3. Enter a feedback string with leading and trailing spaces in the Feedback column | Leading/trailing whitespace is trimmed; saved value shown in the table has no extra spaces | low |

---

## Assignment

Total: **13** (positive: 5, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open submission form | User logged in as <Student> | 1. Click the 'Add submission' button | The submission form opens | high |
| TC-002 | WF-001 | Submit assignment with online text | User logged in as <Student>, Submission form is open | 1. Enter <valid text> in the Online Text Editor<br>2. Click Submit | The submission status updates to 'Submitted for grading' | high |
| TC-003 | WF-001 | Submit assignment with file upload | User logged in as <Student>, Submission form is open | 1. Upload a <valid file> in the File Upload Area<br>2. Click Submit | The submission status updates to 'Submitted for grading' | high |
| TC-004 | WF-002 | View submission status | User logged in as <Student>, Due date has not passed, Teacher permits resubmission | 1. Click 'View Submission' in the Submission Status Section | The submission details are displayed | medium |
| TC-005 | WF-002 | Edit submission | User logged in as <Student>, Due date has not passed, Teacher permits resubmission | 1. Click 'Edit Submission' in the Submission Status Section<br>2. Make changes in the submission form<br>3. Click Submit | The submission status updates to 'Submitted for grading' | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to view submission after due date has passed | due date has passed, teacher permits resubmission | 1. Navigate to the Submission Status Section<br>2. Click on 'View Submission' | Action is blocked; 'View Submission' button is not visible | high |
| TC-007 |  | Attempt to edit submission after due date has passed | due date has passed, teacher permits resubmission | 1. Navigate to the Submission Status Section<br>2. Click on 'Edit Submission' | Action is blocked; 'Edit Submission' button is not visible | high |
| TC-008 |  | Attempt to view submission when teacher does not permit resubmission | due date has not passed, teacher does not permit resubmission | 1. Navigate to the Submission Status Section<br>2. Click on 'View Submission' | Action is blocked; 'View Submission' button is not visible | high |
| TC-009 |  | Attempt to edit submission when teacher does not permit resubmission | due date has not passed, teacher does not permit resubmission | 1. Navigate to the Submission Status Section<br>2. Click on 'Edit Submission' | Action is blocked; 'Edit Submission' button is not visible | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (data_edge) |  | Upload a file at the maximum size limit | The file upload area is available | 1. Prepare a file exactly at the size limit<br>2. Upload the file in the File Upload Area<br>3. Click Submit | File upload succeeds; confirmation message is displayed. | medium |
| TC-011 (data_edge) |  | Upload a file exceeding the maximum size limit | The file upload area is available | 1. Prepare a file that is one byte over the size limit<br>2. Attempt to upload the file in the File Upload Area<br>3. Click Submit | File upload is blocked; error message indicating the file exceeds the size limit is shown. | medium |
| TC-012 (input_edge) |  | Enter a very long text in the online text editor | The online text editor is available | 1. Open the submission form<br>2. Enter a string of 200+ characters in the Online Text Editor | Text is accepted and displayed correctly in the submission preview. | low |
| TC-013 (input_edge) |  | Enter special characters in the online text editor | The online text editor is available | 1. Open the submission form<br>2. Enter a string with special characters (e.g., @#$%^&*!) in the Online Text Editor | Text is accepted and displayed correctly in the submission preview. | low |

---

## Activities

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Navigate to an activity from the Assignments section | User logged in as <Student> | 1. Click on the activity name in the Assignments section | redirects to activity page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to navigate to an activity without any activities listed |  | 1. Ensure no activities are present in the Assignments section<br>2. Click on any activity name | No navigation occurs; the page remains unchanged and displays a message indicating no activities are available. | high |
| TC-003 |  | Attempt to expand a collapsed section |  | 1. Click on the arrow to expand the Forums section<br>2. Click on the arrow to expand the Resources section<br>3. Click on the arrow to expand the Additional Activity Types section | Each section remains collapsed; no content is displayed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Enter a very long name in the Assignments section |  | 1. Navigate to the Activities page<br>2. In the Assignments section, enter a string longer than 200 characters in the Name column | The input is either accepted or truncated with a visible indicator | low |
| TC-005 (input_edge) |  | Enter special characters in the Assignments section Name |  | 1. Navigate to the Activities page<br>2. In the Assignments section, enter a name with special characters (e.g., @#$%^&*) | The input is accepted or a specific error is shown | low |
| TC-006 (interaction_edge) |  | Rapidly click on an activity name |  | 1. Navigate to the Activities page<br>2. Click on an activity name in the Assignments section<br>3. Immediately click on the same activity name again before the page redirects | The first click navigates to the activity page; the second click does not create a duplicate navigation action | medium |

---

## Profile

Total: **15** (positive: 3, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open profile form from Profile page | User logged in as <Student>, User is on the Profile page | 1. Click on the 'Edit profile' link | opens profile form | high |
| TC-002 |  | Update profile with valid data | User logged in as <Student>, User is on the Profile page, User has clicked 'Edit profile' | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid email> in the Email Address field<br>4. Click 'Update Profile' | validates all required fields before saving | high |
| TC-003 |  | Cancel profile edit | User logged in as <Student>, User is on the Profile page, User has clicked 'Edit profile' | 1. Click 'Cancel' | exits without changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave First Name field blank and submit |  | 1. Click on 'Edit profile' to open the profile form<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click 'Update Profile' | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-005 |  | Leave Last Name field blank and submit |  | 1. Click on 'Edit profile' to open the profile form<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click 'Update Profile' | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-006 |  | Leave Email Address field blank and submit |  | 1. Click on 'Edit profile' to open the profile form<br>2. Leave the Email Address field blank<br>3. Fill all other required fields<br>4. Click 'Update Profile' | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-007 |  | Submit profile form with all required fields empty |  | 1. Click on 'Edit profile' to open the profile form<br>2. Leave all required fields blank<br>3. Click 'Update Profile' | Form does not submit; errors shown on First_Name, Last_Name, and Email_Address fields | high |
| TC-008 |  | Enter invalid email format and submit |  | 1. Click on 'Edit profile' to open the profile form<br>2. Enter <invalid email format> in the Email Address field<br>3. Fill all other required fields with valid data<br>4. Click 'Update Profile' | Email_Address field displays an error: 'Must be a valid email address' | medium |
| TC-009 |  | Attempt to update profile without being a student | user is not a student | 1. Click on 'Edit profile' to open the profile form<br>2. Fill all required fields with valid data<br>3. Click 'Update Profile' | Form does not submit; user is blocked from modifying the profile | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter minimum length for First Name |  | 1. Enter exactly 1 character in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; entity is created with the First Name as 1 character | medium |
| TC-011 (boundary) |  | Enter minimum length for Last Name |  | 1. Enter exactly 1 character in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; entity is created with the Last Name as 1 character | medium |
| TC-012 (boundary) |  | Enter valid email address format |  | 1. Enter a valid email address in the Email Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; entity is created with the valid email address | medium |
| TC-013 (input_edge) |  | Enter long text in Description field |  | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; entity is created with the long description | low |
| TC-014 (input_edge) |  | Enter special characters in First Name field |  | 1. Enter special characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; entity is created with the special characters in First Name | low |
| TC-015 (interaction_edge) |  | Rapid resubmission after profile update |  | 1. Fill all required fields with valid data<br>2. Click Update Profile<br>3. Immediately click Update Profile again after the first submission | Second submission attempt is blocked; user is shown a loading indicator or a message indicating the first submission is processing | medium |

---

## Logout

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User logs out successfully | User logged in as <Authenticated User> | 1. Click on the Logout button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to log out while unauthenticated | user must be authenticated | 1. Ensure the user is not authenticated<br>2. Click on the Logout button | Logout action is blocked; user remains on the current page and is not redirected to the login page | high |

---
