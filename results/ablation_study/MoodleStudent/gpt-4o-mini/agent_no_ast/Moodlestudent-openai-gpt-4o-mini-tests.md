# Test Cases — Moodlestudent

Generated: 2026-06-10T21:40:06.879688Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 91 | 29 | 29 | 33 | 35 | 30 | 19 |

## Login

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <Student> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the 'Log in' button | Redirect to the Dashboard | high |
| TC-002 | WF-002 | Failed login with invalid credentials | User logged in as <Student> | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the 'Log in' button | Inline error message shown; password field cleared | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-004 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Enter invalid credentials and submit |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Inline error message shown; password field cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Enter minimum length valid username and password |  | 1. Enter minimum allowed length in the Username field<br>2. Enter minimum allowed length in the Password field<br>3. Click Log in | Redirect to the Dashboard | medium |
| TC-008 (boundary) | WF-002 | Enter invalid credentials with maximum length username |  | 1. Enter maximum allowed length in the Username field<br>2. Enter invalid value in the Password field<br>3. Click Log in | Inline error message shown; password field cleared | medium |
| TC-009 (input_edge) |  | Enter long username with special characters |  | 1. Enter a long string with special characters in the Username field<br>2. Enter a valid password<br>3. Click Log in | Inline error message shown or username accepted based on input handling | low |
| TC-010 (input_edge) |  | Enter username with leading and trailing whitespace |  | 1. Enter '   validUser   ' in the Username field<br>2. Enter a valid password<br>3. Click Log in | Trimmed username is shown in the detail page; successful login or error based on credentials | low |

---

## Dashboard

Total: **11** (positive: 6, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify personalized greeting is displayed | User logged in as <User> | 1. Open the Dashboard | The Dashboard displays a personalized greeting at the top | high |
| TC-002 |  | Verify Timeline block displays upcoming activities | User logged in as <User> | 1. Open the Dashboard<br>2. Select 'Next 7 days' from the time range dropdown | The Timeline block shows upcoming activities and deadlines across all enrolled courses | high |
| TC-003 |  | Verify Calendar block displays current month | User logged in as <User> | 1. Open the Dashboard | The Calendar block shows the current month and year as a heading | high |
| TC-004 |  | Verify 'New event' button functionality in Calendar block | User logged in as <User> | 1. Open the Dashboard<br>2. Click on 'New event' button | The page opens to create personal calendar entries | medium |
| TC-005 |  | Verify empty state in Timeline block | User logged in as <User>, No activities exist within the selected time range | 1. Open the Dashboard<br>2. Select 'Next 7 days' from the time range dropdown | The Timeline block shows an empty state message | medium |
| TC-006 |  | Verify Edit mode elements are displayed | User logged in as <User>, Edit mode is enabled | 1. Open the Dashboard | The 'Reset page to default' button and '+ Add a block' button are visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Unauthenticated user attempts to access the Dashboard |  | 1. Attempt to access the Dashboard page without logging in | User is redirected to the login page | high |
| TC-008 |  | User attempts to create a new event without filling required fields | User is in Edit mode | 1. Click on 'New event' button<br>2. Leave all required fields blank<br>3. Click 'Save' | Form does not submit; error shown on required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (input_edge) |  | Enter a very long search term in the search field |  | 1. Navigate to the Dashboard<br>2. Enter a string of 200+ characters in the search field | The search field accepts the input, but the displayed search result may be truncated or an error is shown indicating the input is too long | low |
| TC-010 (input_edge) |  | Enter special characters in the search field |  | 1. Navigate to the Dashboard<br>2. Enter a string with special characters (e.g., @#$%^&*) in the search field | The search field accepts the input, but the displayed search result may indicate no matches found or an error is shown | low |
| TC-011 (input_edge) |  | Enter a search term with leading and trailing whitespace |  | 1. Navigate to the Dashboard<br>2. Enter a search term with leading and trailing spaces in the search field | Leading/trailing whitespace is trimmed; saved search term displayed in the search field has no extra spaces | low |

---

## My Courses

Total: **18** (positive: 7, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View course details | User logged in as <Student> | 1. Click on the course name link on the course card | User is taken to the course's main page | high |
| TC-002 | WF-002 | Star a course | User logged in as <Student> | 1. Click on the three-dot menu of a course card<br>2. Select 'Star this course' | Course pinned to the top of the list | medium |
| TC-003 | WF-003 | Remove course from view | User logged in as <Student> | 1. Click on the three-dot menu of a course card<br>2. Select 'Remove from view' | Course hidden from the list | medium |
| TC-004 | WF-004 | Filter courses by status | User logged in as <Student> | 1. Select 'In progress' from the status dropdown | Courses filtered by selected status | medium |
| TC-005 | WF-005 | Search for a course | User logged in as <Student> | 1. Enter <valid course name> in the search field<br>2. Press Enter | Courses matching search criteria displayed | medium |
| TC-006 | WF-006 | Sort courses | User logged in as <Student> | 1. Select 'Name' from the sort dropdown | Courses sorted by selected criteria | medium |
| TC-007 | WF-007 | Change layout of courses | User logged in as <Student> | 1. Select 'List' from the layout dropdown | Courses displayed in selected layout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Attempt to navigate to course main page without selecting a course |  | 1. Leave the course selection unmade<br>2. Click on the course name link | No navigation occurs; the course selection remains unmade |  |
| TC-009 | WF-002 | Attempt to star a course without selecting a course |  | 1. Leave the course selection unmade<br>2. Click on the 'Star this course' option | No action occurs; the course remains unstarred |  |
| TC-010 | WF-003 | Attempt to remove a course from view without selecting a course |  | 1. Leave the course selection unmade<br>2. Click on the 'Remove from view' option | No action occurs; the course remains visible |  |
| TC-011 | WF-004 | Attempt to apply a status filter without selecting a status |  | 1. Leave the status dropdown unselected<br>2. Click on the 'Apply status filter' button | No filtering occurs; all courses remain displayed |  |
| TC-012 | WF-005 | Attempt to search for a course without entering a search term |  | 1. Leave the search field blank<br>2. Click on the 'Search' button | No search occurs; all courses remain displayed |  |
| TC-013 | WF-006 | Attempt to sort courses without selecting a sort criteria |  | 1. Leave the sort dropdown unselected<br>2. Click on the 'Apply sort' button | No sorting occurs; courses remain in their original order |  |
| TC-014 | WF-007 | Attempt to change layout without selecting a layout option |  | 1. Leave the layout dropdown unselected<br>2. Click on the 'Apply layout change' button | No layout change occurs; courses remain displayed in their original layout |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (interaction_edge) | WF-004 | Filter courses with an empty status selection | User is on the My Courses page | 1. Select the status dropdown<br>2. Leave the selection empty<br>3. Click Apply | No courses are displayed; a message indicates that no courses match the selected criteria. | medium |
| TC-016 (interaction_edge) | WF-005 | Search for a course with a very long string | User is on the My Courses page | 1. Enter a string of 200 characters in the search field<br>2. Click Search | The system displays a message indicating that no courses match the search criteria, as the input is too long. | low |
| TC-017 (interaction_edge) | WF-006 | Sort courses with an invalid option | User is on the My Courses page | 1. Select the sort dropdown<br>2. Choose an option that does not exist<br>3. Click Apply sort | The system displays an error message indicating that the selected sort option is invalid. | low |
| TC-018 (interaction_edge) | WF-007 | Change layout rapidly | User is on the My Courses page | 1. Select the layout dropdown<br>2. Change layout to Card<br>3. Immediately change layout to List<br>4. Immediately change layout to Summary | The layout changes successfully to Summary without any errors, and the courses are displayed in the selected layout. | medium |

---

## Course Page

Total: **10** (positive: 3, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Course Content | User logged in as <Student> | 1. Navigate to the Course page | Course content displayed | high |
| TC-002 | WF-002 | Collapse All Sections | User logged in as <Student>, Course content is displayed | 1. Click 'Collapse all' link | All sections collapsed | medium |
| TC-003 | WF-003 | Access Activity or Resource | User logged in as <Student>, Course content is displayed | 1. Click on the name of an activity or resource | Activity or resource opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Unauthenticated user attempts to view course content |  | 1. Navigate to the Course page without logging in | User is redirected to the login page | high |
| TC-005 | WF-002 | Attempt to collapse all sections while not logged in |  | 1. Navigate to the Course page without logging in<br>2. Click 'Collapse all' | User is redirected to the login page | high |
| TC-006 | WF-003 | Unauthenticated user attempts to access an activity or resource |  | 1. Navigate to the Course page without logging in<br>2. Click on an activity or resource | User is redirected to the login page | high |
| TC-007 |  | Attempt to enable Edit mode on course page |  | 1. Navigate to the Course page<br>2. Attempt to enable Edit mode | Edit mode is not enabled; no changes are made to the course page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) | WF-001 | Rapidly click on multiple sections to expand and collapse | User is on the Course Page | 1. Click on the first section to expand it<br>2. Immediately click on the second section to expand it<br>3. Click on the first section again to collapse it<br>4. Click on the third section to expand it | All sections respond correctly; the first section collapses, the second expands, and the third expands without errors. | medium |
| TC-009 (interaction_edge) | WF-002 | Click Collapse All rapidly after expanding sections | User has expanded multiple sections | 1. Click on the 'Collapse all' link immediately after expanding sections | 'Collapse all' action succeeds; all sections are collapsed regardless of the timing of the click. | medium |
| TC-010 (interaction_edge) | WF-003 | Access an activity or resource rapidly after opening | User is on the Course Page | 1. Click on an activity or resource link<br>2. Immediately attempt to click on another activity or resource link before the first has fully loaded | The first activity or resource opens successfully; the second click is either blocked until the first action completes or opens the second resource without error. | medium |

---

## Participants

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View participant profile | User logged in as <Student>, Participants page is open | 1. Click on <participant name> in the First/Last name column | Profile displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to view a participant profile |  | 1. Navigate to the Participants page as an unauthenticated user<br>2. Click on a participant's name to view their profile | User is redirected to the login page | high |
| TC-003 |  | Attempt to apply filters without any conditions |  | 1. Navigate to the Participants page<br>2. Click on 'Apply filters' without adding any conditions | No filters are applied; the participants list remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapidly click on participant names | User is on the Participants page with multiple participants listed | 1. Click on the first participant name<br>2. Wait for the profile to load<br>3. Immediately click on the second participant name | Second profile loads successfully without errors; user can view the new profile. | medium |
| TC-005 (input_edge) |  | Filter with special characters | User is on the Participants page | 1. Enter special characters in the First name filter<br>2. Click 'Apply filters' | Filters applied; results show no participants or an appropriate message indicating no matches. | low |
| TC-006 (input_edge) |  | Filter with leading and trailing whitespace | User is on the Participants page | 1. Enter '   John   ' in the First name filter<br>2. Click 'Apply filters' | Leading/trailing whitespace is trimmed; results show participants with the name 'John'. | low |
| TC-007 (input_edge) |  | Filter with long text input | User is on the Participants page | 1. Enter a very long string (200+ characters) in the First name filter<br>2. Click 'Apply filters' | Input is either rejected with an error message or the filter is ignored, showing all participants. | low |

---

## Grades

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify student's own grades are displayed correctly | User logged in as <Student> | 1. Navigate to the Grades page | The grade table displays the student's own grades with the correct Grade item, Calculated weight, Grade, Range, Percentage, Feedback, and Contribution to course total. | high |
| TC-002 |  | Verify AGGREGATION Course total is displayed | User logged in as <Student> | 1. Navigate to the Grades page | The AGGREGATION Course total row displays the cumulative grade across all weighted items. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user attempts to access the Grades page |  | 1. Navigate to the Grades page without logging in | User is redirected to the login page | high |
| TC-004 |  | Authenticated user attempts to access another student's grades | User is logged in | 1. Attempt to access the grades of another student | Access is denied; user cannot view other students' grades | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the feedback field |  | 1. Navigate to the Grades page<br>2. Enter a string of 200+ characters in the Feedback column | Feedback field accepts the long string or displays a truncation message | low |
| TC-006 (input_edge) |  | Enter special characters in the feedback field |  | 1. Navigate to the Grades page<br>2. Enter special characters in the Feedback column | Feedback field accepts the special characters or displays an error message | low |
| TC-007 (input_edge) |  | Enter leading and trailing whitespace in the feedback field |  | 1. Navigate to the Grades page<br>2. Enter a value with leading and trailing spaces in the Feedback column | Leading/trailing whitespace is trimmed; saved value shows no extra spaces | low |

---

## Assignment

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open submission form | User logged in as <Student> | 1. Click 'Add submission' button | Submission form opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access the submission form |  | 1. Attempt to click on the 'Add submission' button without being logged in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid submission after opening form | User has opened the submission form | 1. Click the 'Add submission' button<br>2. Immediately click the 'Add submission' button again | Second click is ignored; the submission form remains open without duplication. | medium |
| TC-004 (input_edge) |  | Long description input | User is on the submission form | 1. Enter a string of 200+ characters in the Description field | Description field accepts the input without truncation. | low |
| TC-005 (input_edge) |  | Special characters in description | User is on the submission form | 1. Enter a string with special characters (e.g., @#$%^&*()!) in the Description field | Description field accepts the input without errors. | low |

---

## Activities

Total: **8** (positive: 4, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify Assignments section is expanded by default | User logged in as <Role> | 1. Open the Activities page | The Assignments section is expanded and displays a table with columns for Name, Due date, and Submission status | high |
| TC-002 |  | Verify Forums section is collapsed by default | User logged in as <Role> | 1. Open the Activities page | The Forums section is collapsed and can be expanded | medium |
| TC-003 |  | Verify Resources section is collapsed by default | User logged in as <Role> | 1. Open the Activities page | The Resources section is collapsed and can be expanded | medium |
| TC-004 |  | Verify navigation to activity page when clicking on an assignment name | User logged in as <Role>, Assignments section is expanded | 1. Click on the name of an assignment in the Assignments table | User is navigated to the selected assignment's page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user attempts to access the Activities page |  | 1. Navigate to the Activities page without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long string in the Name field |  | 1. Navigate to the Activities page<br>2. Enter a string of 200+ characters in the Name field | The system accepts the input and displays the Name with the full string in the table | low |
| TC-007 (input_edge) |  | Enter special characters in the Name field |  | 1. Navigate to the Activities page<br>2. Enter special characters (e.g., @#$%^&*) in the Name field | The system accepts the input and displays the Name with the special characters in the table | low |
| TC-008 (input_edge) |  | Enter leading and trailing whitespace in the Name field |  | 1. Navigate to the Activities page<br>2. Enter '   Example Activity   ' in the Name field | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Profile

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit profile and update successfully | User logged in as <Student>, User is on the Profile page | 1. Click 'Edit profile'<br>2. Enter <First name> in the First name field<br>3. Enter <Last name> in the Last name field<br>4. Enter <valid email> in the Email address field<br>5. Select <visibility option> from the Email visibility dropdown<br>6. Enter <MoodleNet profile ID> in the MoodleNet profile ID field<br>7. Enter <City/town> in the City/town field<br>8. Select <Country> from the Country dropdown<br>9. Select <Timezone> from the Timezone dropdown<br>10. Enter <optional profile description> in the Description field<br>11. Click 'Update profile' | Profile updated successfully | high |
| TC-002 | WF-002 | Edit profile and cancel changes | User logged in as <Student>, User is on the Profile page | 1. Click 'Edit profile'<br>2. Enter <First name> in the First name field<br>3. Click 'Cancel' | Exited without changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to update profile with required fields blank |  | 1. Click on 'Edit profile'<br>2. Leave the First name, Last name, and Email address fields blank<br>3. Click 'Update profile' | Inline validation error appears on the First name, Last name, and Email address fields indicating they are required | high |
| TC-004 | WF-001 | Attempt to update profile with invalid email format |  | 1. Click on 'Edit profile'<br>2. Enter <invalid email format> in the Email address field<br>3. Fill all other required fields<br>4. Click 'Update profile' | Inline validation error appears on the Email address field indicating it must be a valid email address | medium |
| TC-005 | WF-001 | Attempt to update profile with duplicate MoodleNet profile ID |  | 1. Click on 'Edit profile'<br>2. Enter <duplicate MoodleNet profile ID> in the MoodleNet profile ID field<br>3. Fill all other required fields with valid data<br>4. Click 'Update profile' | Inline validation error appears on the MoodleNet profile ID field indicating it must be unique | medium |
| TC-006 | WF-001 | Attempt to update profile without required fields filled |  | 1. Click on 'Edit profile'<br>2. Leave all required fields blank<br>3. Click 'Update profile' | Form does not submit; profile is not updated; inline validation errors are shown on required fields | high |
| TC-007 | WF-002 | Attempt to cancel profile edit and check for changes |  | 1. Click on 'Edit profile'<br>2. Make changes to the profile fields<br>3. Click 'Cancel' | Exited without changes; no updates are made to the profile | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Update profile with maximum length description | User is logged in and on the Edit profile page | 1. Enter maximum allowed length string in the Description field<br>2. Fill all other required fields<br>3. Click Update profile | Profile updated successfully; Description displays the full entered text | medium |
| TC-009 (boundary) | WF-001 | Update profile with description exceeding maximum length | User is logged in and on the Edit profile page | 1. Enter string exceeding maximum allowed length in the Description field<br>2. Fill all other required fields<br>3. Click Update profile | Update is blocked; inline error shows 'Description exceeds maximum length' | medium |
| TC-010 (input_edge) | WF-001 | Update profile with leading and trailing whitespace in the Description | User is logged in and on the Edit profile page | 1. Enter '   Sample description   ' in the Description field<br>2. Fill all other required fields<br>3. Click Update profile | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-011 (interaction_edge) | WF-002 | Cancel profile edit after making changes | User is logged in and on the Edit profile page | 1. Fill in changes in the profile fields<br>2. Click Cancel | Exited without changes; profile remains unchanged on the detail page | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <role> | 1. Click on the Log out button | Redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access protected page | User is not logged in | 1. Attempt to access a protected page | User is redirected to the login page; access to the protected page is denied | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after logout | User is logged in and on a protected page | 1. Click the Log out button<br>2. After being redirected to the login page, immediately click the Log out button again | User is redirected to the login page without creating a new session | medium |
| TC-004 (input_edge) |  | Attempt to access protected page after logout | User has logged out | 1. Attempt to navigate to a protected page | User is prompted to re-authenticate to access the protected page | medium |

---
