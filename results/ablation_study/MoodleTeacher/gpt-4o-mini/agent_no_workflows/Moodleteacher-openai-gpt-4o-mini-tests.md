# Test Cases — Moodleteacher

Generated: 2026-06-10T21:13:47.257916Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 186 | 70 | 55 | 61 | 58 | 99 | 25 |

## Login

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <Teacher> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click 'Log in' | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click 'Log in' | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click 'Log in' | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Submit with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click 'Log in' | Form does not submit; error shown: 'Invalid or empty credentials'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) |  | Enter maximum length string in Username field |  | 1. Enter a string with maximum allowed length in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Form submits successfully; user is redirected to Dashboard | medium |
| TC-007 (boundary) |  | Enter empty string in Password field |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message displays: 'Invalid or empty credentials'; Password field is cleared; Username remains | medium |
| TC-008 (input_edge) |  | Enter long string with special characters in Username field |  | 1. Enter a long string with special characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message displays: 'Invalid or empty credentials'; Password field is cleared; Username remains | low |
| TC-009 (input_edge) |  | Enter leading/trailing whitespace in Username field |  | 1. Enter leading and trailing spaces in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Dashboard

Total: **15** (positive: 7, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display upcoming activities in the Timeline block | User logged in as <User Role> | 1. Select 'Next 7 days' from the Time Range dropdown | The Timeline block displays upcoming teaching actions for the next 7 days | high |
| TC-002 |  | Create a new calendar entry | User logged in as <User Role> | 1. Click the New Event button | A success notification is displayed; the calendar entry is created | high |
| TC-003 |  | Navigate to the previous month in the Calendar block | User logged in as <User Role> | 1. Click the Previous Month button | The Calendar block displays the previous month's events | medium |
| TC-004 |  | Navigate to the next month in the Calendar block | User logged in as <User Role> | 1. Click the Next Month button | The Calendar block displays the next month's events | medium |
| TC-005 |  | Open the full calendar view | User logged in as <User Role> | 1. Click the Full calendar link | The dedicated calendar view opens | medium |
| TC-006 |  | Open the calendar data management view | User logged in as <User Role> | 1. Click the Import or export calendars link | The calendar data management view opens | medium |
| TC-007 |  | Display empty state in the Timeline block | User logged in as <User Role>, No upcoming activities exist | 1. Select 'Next 7 days' from the Time Range dropdown | The Timeline block shows an empty state message indicating no activities found | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave Time Range dropdown unselected and submit |  | 1. Leave the Time Range dropdown blank<br>2. Click on any other button or link | No action occurs; Time Range field is highlighted indicating it is required | high |
| TC-009 |  | Attempt to create a new event without selecting a course |  | 1. Click on the New Event button without selecting a course from the All Courses dropdown | No calendar entry is created; error shown indicating a course must be selected | high |
| TC-010 |  | Click on Full calendar link without being logged in |  | 1. Click on the Full calendar link | User is redirected to the login page | high |
| TC-011 |  | Click on Import or export calendars link without being logged in |  | 1. Click on the Import or export calendars link | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) |  | Enter a long search term in the Search Activities field |  | 1. Click on the Search Activities field<br>2. Enter a string of 200+ characters | Search Activities field displays a truncation message or error if not accepted | low |
| TC-013 (input_edge) |  | Enter special characters in the Search Activities field |  | 1. Click on the Search Activities field<br>2. Enter a string with special characters (e.g., @#$%^&*) | Search Activities field displays a specific error indicating invalid characters or accepts the input | low |
| TC-014 (interaction_edge) |  | Navigate to the previous month rapidly |  | 1. Click on the Month Navigation button for Previous Month<br>2. Immediately click on the Previous Month button again | The action to navigate to the previous month is blocked with a visible error message or the calendar remains on the current month | medium |
| TC-015 (interaction_edge) |  | Click on the Full calendar link after creating a new event | An event has been created | 1. Click on the New Event button to create a calendar entry<br>2. Click on the Full calendar link | User is redirected to the dedicated calendar view without creating a duplicate event | medium |

---

## Dashboard — Edit Mode

Total: **15** (positive: 6, negative: 6, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Reset page to default | User logged in as <User>, Edit mode is enabled | 1. Click 'Reset page to default' | The layout resets to default | high |
| TC-002 |  | Open Add a block page | User logged in as <User>, Edit mode is enabled | 1. Click '+ Add a block' | The Add a block page opens listing all available block types | high |
| TC-003 |  | Return to Dashboard without adding a block | User logged in as <User>, Edit mode is enabled | 1. Click 'Cancel' | Returns to Dashboard without adding a block | medium |
| TC-004 |  | Configure existing block | User logged in as <User>, Edit mode is enabled | 1. Click the three-dot options menu on an existing block<br>2. Select 'Configure' | The configuration options for the block are displayed | medium |
| TC-005 |  | Move existing block | User logged in as <User>, Edit mode is enabled | 1. Click the move icon on an existing block | The block is ready to be moved | medium |
| TC-006 |  | Delete existing block | User logged in as <User>, Edit mode is enabled | 1. Click the three-dot options menu on an existing block<br>2. Select 'Delete' | The block is no longer visible on the Dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to reset page to default | Edit mode is toggled on | 1. Click 'Reset page to default' | Status remains unchanged; layout is not reset; no error shown | medium |
| TC-008 |  | Attempt to add a block without valid selection | Edit mode is toggled on | 1. Click '+ Add a block' | Page opens to Add a block; no block is added; no error shown | medium |
| TC-009 |  | Click 'Cancel' without adding a block | Edit mode is toggled on | 1. Click '+ Add a block'<br>2. Click 'Cancel' | Returns to Dashboard without adding a block; no error shown | medium |
| TC-010 |  | Attempt to configure a block without a valid selection | Edit mode is toggled on | 1. Click 'Configure' on an existing block | No configuration changes occur; no error shown | medium |
| TC-011 |  | Attempt to move a block without a valid selection | Edit mode is toggled on | 1. Click 'Move' on an existing block | No movement occurs; no error shown | medium |
| TC-012 |  | Attempt to delete a block without confirmation | Edit mode is toggled on | 1. Click 'Delete' on an existing block | No deletion occurs; no error shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) |  | Rapidly click the Reset page to default button | Edit mode is toggled on | 1. Click the 'Reset page to default' button<br>2. Immediately click the 'Reset page to default' button again | Second click is ignored; layout remains reset to default | medium |
| TC-014 (interaction_edge) |  | Click Cancel after opening Add a block page | Edit mode is toggled on | 1. Click the '+ Add a block' button<br>2. Click the 'Cancel' link | Returns to Dashboard without adding a block; no new block appears | medium |
| TC-015 (interaction_edge) |  | Attempt to delete a block rapidly | Edit mode is toggled on, At least one block exists | 1. Click the 'Delete' action for an existing block<br>2. Immediately click the 'Delete' action for the same block again | Second delete action is ignored; block remains deleted | medium |

---

## My Courses

Total: **13** (positive: 5, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Star a course | User logged in as <Teacher>, Course is visible in the course grid | 1. Click the three-dot menu on the course card<br>2. Select 'Star this course' from the menu | The course is pinned to the top | high |
| TC-002 |  | Remove a course from view | User logged in as <Teacher>, Course is visible in the course grid | 1. Click the three-dot menu on the course card<br>2. Select 'Remove from view' from the menu | The course is hidden without affecting enrollment | high |
| TC-003 |  | Filter courses by status | User logged in as <Teacher> | 1. Select 'In progress' from the Status_Dropdown | Only courses with 'In progress' status are displayed | medium |
| TC-004 |  | Search for a course | User logged in as <Teacher> | 1. Enter <valid course name> in the Search_Field | Only courses matching <valid course name> are displayed | medium |
| TC-005 |  | Sort courses by layout | User logged in as <Teacher> | 1. Select 'List' from the Layout_Dropdown | Courses are displayed in a list layout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to submit with the Status Dropdown unselected |  | 1. Leave the Status Dropdown unselected<br>2. Click on the Search button | The Status Dropdown remains unselected; no search results are displayed |  |
| TC-007 |  | Attempt to submit with the Layout Dropdown unselected |  | 1. Leave the Layout Dropdown unselected<br>2. Click on the Search button | The Layout Dropdown remains unselected; no layout change occurs |  |
| TC-008 |  | Attempt to star a course when no course is selected |  | 1. Do not select any course<br>2. Click on 'Star this course' | No course is starred; the action is blocked |  |
| TC-009 |  | Attempt to remove a course when no course is selected |  | 1. Do not select any course<br>2. Click on 'Remove from view' | No course is removed; the action is blocked |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) |  | Enter a very long search term in the Search Field |  | 1. Enter a string of 200+ characters in the Search_Field | Search_Field displays an error indicating the input exceeds the maximum allowed length or is truncated | low |
| TC-011 (input_edge) |  | Enter special characters in the Search Field |  | 1. Enter special characters (e.g., @#$%^&*) in the Search_Field | Search_Field displays an error indicating invalid characters or accepts the input without error | low |
| TC-012 (input_edge) |  | Enter leading and trailing whitespace in the Search Field |  | 1. Enter '   course name   ' in the Search_Field | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |
| TC-013 (interaction_edge) |  | Rapidly toggle the Status Dropdown |  | 1. Click on the Status_Dropdown<br>2. Rapidly select different options from the dropdown | Status_Dropdown reflects the last selected option without errors or delays | medium |

---

## Course Page

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify navigation tab bar is displayed | User logged in as <Student> | 1. Open the Course Page | The navigation tab bar is visible at the top of the page | high |
| TC-002 |  | Verify sections are displayed | User logged in as <Student> | 1. Open the Course Page | The course content is displayed with collapsible sections and section names | high |
| TC-003 |  | Verify 'Collapse All' functionality | User logged in as <Student>, Sections are expanded | 1. Click on the 'Collapse All' link | All sections are collapsed | medium |
| TC-004 |  | Verify navigation to activity/resource | User logged in as <Student>, At least one section is expanded | 1. Click on the name of an activity/resource | User is navigated to the corresponding activity/resource page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to navigate to an activity/resource without any sections present |  | 1. Open the Course Page<br>2. Ensure no sections are listed | No activities/resources are available to navigate to; no action occurs | high |
| TC-006 |  | Click 'Collapse All' when no sections are expanded |  | 1. Open the Course Page<br>2. Click on 'Collapse All' link | 'Collapse All' action has no effect; all sections remain in their current state | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) |  | Rapidly collapse and expand sections | User is on the Course Page | 1. Click on the first section to expand it<br>2. Immediately click the same section again to collapse it<br>3. Click on the second section to expand it<br>4. Immediately click the same section again to collapse it | Each section expands and collapses successfully without errors or delays. | medium |
| TC-008 (interaction_edge) |  | Collapse all sections | User has multiple sections expanded | 1. Click on the 'Collapse All' link | All sections collapse successfully, and the chevrons change to indicate collapsed state. | medium |
| TC-009 (interaction_edge) |  | Expand a section after collapsing all | User has collapsed all sections | 1. Click on the first section to expand it | The first section expands successfully, displaying its activities and resources. | medium |
| TC-010 (interaction_edge) |  | Attempt to navigate to an activity/resource | User is on the Course Page with sections expanded | 1. Click on an activity/resource link within a section | User is navigated to the corresponding activity/resource page. | medium |

---

## Course Edit Mode and Activity Chooser

Total: **19** (positive: 8, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Edit a section from the course page | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on the section row<br>2. Click 'Edit'<br>3. Enter <new section name> in the section name field<br>4. Click 'Save' | The section name updates to '<new section name>' on the course page | high |
| TC-002 |  | Duplicate a section from the course page | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on the section row<br>2. Click 'Duplicate' | A new section appears below the original section with the same name | high |
| TC-003 |  | Hide a section from the course page | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on the section row<br>2. Click 'Hide' | The section is no longer visible on the course page | high |
| TC-004 |  | Delete a section from the course page | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on the section row<br>2. Click 'Delete'<br>3. Click Confirm on the Delete dialog | The section is no longer visible on the course page | high |
| TC-005 |  | Move a section to a different position on the course page | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on the section row<br>2. Click 'Move'<br>3. Select the new position for the section<br>4. Click 'Confirm' | The section is moved to the selected position on the course page | high |
| TC-006 |  | Add an activity using the Activity Chooser modal | User logged in as <Teacher>, Edit mode is enabled | 1. Click '+ Add an activity or resource'<br>2. Select 'Assignment' tile from the Activity Chooser modal<br>3. Click 'Add' | The Assignment creation form opens | high |
| TC-007 |  | Filter activities in the Activity Chooser modal | User logged in as <Teacher>, Edit mode is enabled | 1. Click '+ Add an activity or resource'<br>2. Select 'Activities' from the Category_Filter_Bar dropdown | Only activity tiles are displayed in the Activity Chooser modal | medium |
| TC-008 |  | Search for an activity in the Activity Chooser modal | User logged in as <Teacher>, Edit mode is enabled | 1. Click '+ Add an activity or resource'<br>2. Enter 'Quiz' in the Search_Field<br>3. Click 'Search' | Only the Quiz tile is displayed in the Activity Chooser modal | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to add an activity without selecting a category |  | 1. Click on '+ Add an activity or resource'<br>2. Leave the Category_Filter_Bar blank<br>3. Click 'Add' | Inline validation error appears on the Category_Filter_Bar field indicating it is required | high |
| TC-010 |  | Attempt to search with an empty search field |  | 1. Click on '+ Add an activity or resource'<br>2. Leave the Search_Field blank<br>3. Click 'Search' | Inline validation error appears on the Search_Field field indicating it is required | high |
| TC-011 |  | Attempt to add an activity without selecting a tile |  | 1. Click on '+ Add an activity or resource'<br>2. Select a category<br>3. Click 'Add' without selecting any tile | Inline validation error appears indicating a tile must be selected before adding | high |
| TC-012 |  | Attempt to delete a section without confirmation |  | 1. Click on 'Section Actions'<br>2. Click 'Delete' | No action occurs; a confirmation dialog appears asking for confirmation to delete | medium |
| TC-013 |  | Attempt to perform bulk actions without selecting any items |  | 1. Click on 'Bulk Actions'<br>2. Click 'Delete' | Inline validation error appears indicating that at least one item must be selected for bulk actions | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Add maximum number of activities | User is in Course Edit Mode | 1. Click '+ Add an activity or resource'<br>2. Add the maximum allowed number of activities | All activities are added successfully; the count reflects the maximum allowed. | medium |
| TC-015 (boundary) |  | Attempt to add one more activity than allowed | User is in Course Edit Mode, Maximum number of activities is already added | 1. Click '+ Add an activity or resource'<br>2. Attempt to add one additional activity | Adding the activity is blocked; an error message indicates the maximum limit has been reached. | medium |
| TC-016 (input_edge) |  | Enter a long search term in the search field | User is in Activity Chooser Modal | 1. Enter a string longer than 200 characters in the Search_Field | The input is either truncated or a visible error is shown indicating the input exceeds the maximum length. | low |
| TC-017 (input_edge) |  | Enter special characters in the search field | User is in Activity Chooser Modal | 1. Enter special characters (e.g., @#$%^&*) in the Search_Field | The input is either accepted or a specific error message is shown. | low |
| TC-018 (interaction_edge) |  | Rapidly click 'Add' after selecting an activity tile | User is in Activity Chooser Modal, An activity tile is selected | 1. Click 'Add' button multiple times in quick succession | Only one activity is added; subsequent clicks are ignored or blocked with a message indicating the action is in progress. | medium |
| TC-019 (state_edge) |  | Navigate back after adding an activity | User has successfully added an activity and is redirected to the course page | 1. Press the browser back button | The course page displays without pre-filled values from the previous submission. | medium |

---

## Assignment Creation

Total: **20** (positive: 3, negative: 11, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create assignment and redirect to course page | User logged in as <Teacher>, Assignment creation form is open | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Enter <Description> in the Description rich text editor<br>3. Enter <valid date> in the Allow Submissions From field<br>4. Enter <valid date> in the Due Date field<br>5. Enter <valid date> in the Cut Off Date field<br>6. Click Save and return to course | Assignment is created and redirects to course page | high |
| TC-002 |  | Create assignment and display new assignment's page | User logged in as <Teacher>, Assignment creation form is open | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Enter <Description> in the Description rich text editor<br>3. Enter <valid date> in the Allow Submissions From field<br>4. Enter <valid date> in the Due Date field<br>5. Enter <valid date> in the Cut Off Date field<br>6. Click Save and display | Assignment is created and opens new assignment's page | high |
| TC-003 |  | Cancel assignment creation | User logged in as <Teacher>, Assignment creation form is open | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Click Cancel | All changes are discarded | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Assignment Name blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other required fields<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-005 |  | Leave all required fields empty and submit |  | 1. Leave the Assignment_Name field blank<br>2. Leave the Allow_Submissions_From field blank<br>3. Leave the Due_Date field blank<br>4. Leave the Cut_Off_Date field blank<br>5. Leave the Max_Attempts field blank<br>6. Leave the Grouping_Selection field blank<br>7. Click 'Save and return to course' | Inline validation errors appear on the Assignment_Name, Allow_Submissions_From, Due_Date, Cut_Off_Date, Max_Attempts, and Grouping_Selection fields indicating they are required | high |
| TC-006 |  | Enter invalid date in Allow Submissions From field |  | 1. Enter <invalid date format> in the Allow_Submissions_From field<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Allow_Submissions_From field indicating it must be a valid date | medium |
| TC-007 |  | Enter invalid date in Due Date field |  | 1. Enter <invalid date format> in the Due_Date field<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Due_Date field indicating it must be a valid date | medium |
| TC-008 |  | Enter invalid date in Cut Off Date field |  | 1. Enter <invalid date format> in the Cut_Off_Date field<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Cut_Off_Date field indicating it must be a valid date | medium |
| TC-009 |  | Enter non-numeric value in Max Uploaded Files field |  | 1. Check the File_Submissions checkbox<br>2. Enter <non-numeric value> in the Max_Uploaded_Files field<br>3. Fill all other required fields with valid data<br>4. Click 'Save and return to course' | Inline validation error appears on the Max_Uploaded_Files field indicating it must be a number | medium |
| TC-010 |  | Enter non-numeric value in Max Submission Size field |  | 1. Check the File_Submissions checkbox<br>2. Enter <non-numeric value> in the Max_Submission_Size field<br>3. Fill all other required fields with valid data<br>4. Click 'Save and return to course' | Inline validation error appears on the Max_Submission_Size field indicating it must be a number | medium |
| TC-011 |  | Leave Accepted File Types field blank when File Submissions is enabled |  | 1. Check the File_Submissions checkbox<br>2. Leave the Accepted_File_Types field blank<br>3. Fill all other required fields with valid data<br>4. Click 'Save and return to course' | Inline validation error appears on the Accepted_File_Types field indicating it is required | medium |
| TC-012 |  | Attempt to save without clicking the Submit Button when required |  | 1. Leave the Require_Submit_Button_Click checkbox unchecked<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Require_Submit_Button_Click field indicating it is required | medium |
| TC-013 |  | Attempt to save without entering Max Attempts when required |  | 1. Leave the Max_Attempts field blank<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Max_Attempts field indicating it is required | medium |
| TC-014 |  | Attempt to save without entering Grouping Selection when required |  | 1. Leave the Grouping_Selection field blank<br>2. Fill all other required fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Grouping_Selection field indicating it is required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Max_Attempts set to maximum allowed value | User is on the Assignment Creation form | 1. Enter a valid Assignment Name in the Assignment_Name field<br>2. Expand the Submission_Settings panel<br>3. Enter the maximum allowed value in the Max_Attempts field | Form submits successfully; assignment is created with Max_Attempts set to the maximum allowed value | medium |
| TC-016 (boundary) |  | Max_Attempts set to one unit over maximum allowed value | User is on the Assignment Creation form | 1. Enter a valid Assignment Name in the Assignment_Name field<br>2. Expand the Submission_Settings panel<br>3. Enter one unit over the maximum allowed value in the Max_Attempts field | Max_Attempts field displays an error indicating the value exceeds the maximum allowed | medium |
| TC-017 (boundary) |  | Allow_Submissions_From date set to today's date | User is on the Assignment Creation form | 1. Enter a valid Assignment Name in the Assignment_Name field<br>2. Expand the Availability panel<br>3. Set Allow_Submissions_From to today's date | Form submits successfully; assignment is created with Allow_Submissions_From set to today's date | medium |
| TC-018 (boundary) |  | Allow_Submissions_From date set to one day in the past | User is on the Assignment Creation form | 1. Enter a valid Assignment Name in the Assignment_Name field<br>2. Expand the Availability panel<br>3. Set Allow_Submissions_From to one day before today's date | Allow_Submissions_From field displays an error indicating the date cannot be in the past | medium |
| TC-019 (input_edge) |  | Enter a very long string in the Assignment_Name field | User is on the Assignment Creation form | 1. Enter a string longer than 200 characters in the Assignment_Name field | Assignment_Name field displays an error indicating the maximum length is exceeded | low |
| TC-020 (input_edge) |  | Enter special characters in the Assignment_Name field | User is on the Assignment Creation form | 1. Enter a string containing special characters in the Assignment_Name field | Assignment_Name field accepts the input without error | low |

---

## Course Settings

Total: **14** (positive: 2, negative: 4, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Course Settings with all required fields filled | User logged in as <Admin>, Course Settings form is open | 1. Enter <valid course full name> in the Course Full Name field<br>2. Enter <valid course short name> in the Course Short Name field<br>3. Select <valid course category> from the Course Category dropdown<br>4. Select 'Show' from the Course Visibility dropdown<br>5. Click 'Save and display' | The configuration persists and returns to the course page | high |
| TC-002 |  | Cancel Course Settings changes | User logged in as <Admin>, Course Settings form is open | 1. Enter <valid course full name> in the Course Full Name field<br>2. Enter <valid course short name> in the Course Short Name field<br>3. Select <valid course category> from the Course Category dropdown<br>4. Click 'Cancel' | Existing settings remain unchanged | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Course Full Name field blank and submit |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-004 |  | Leave the Course Short Name field blank and submit |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-005 |  | Leave the Course Category field blank and submit |  | 1. Leave the Course Category field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the Course Full Name field blank<br>2. Leave the Course Short Name field blank<br>3. Leave the Course Category field blank<br>4. Click Save and display | Inline validation error appears on the Course Full Name, Course Short Name, and Course Category fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Enter maximum length string in Course Full Name |  | 1. Enter a string at the maximum allowed length in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the maximum length string in the Course Full Name | medium |
| TC-008 (boundary) |  | Enter one character below maximum length in Course Short Name |  | 1. Enter a string one character below the maximum allowed length in the Course Short Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the string in the Course Short Name | medium |
| TC-009 (data_edge) |  | Enter today's date in Course Start Date |  | 1. Enter today's date in the Course Start Date field<br>2. Click Save and display | Form submits successfully; today's date is saved in the Course Start Date | medium |
| TC-010 (data_edge) |  | Enter yesterday's date in Course End Date when toggle is enabled | Enable toggle is on | 1. Enter yesterday's date in the Course End Date field<br>2. Click Save and display | Form submits successfully; yesterday's date is saved in the Course End Date | medium |
| TC-011 (data_edge) |  | Upload a file at the exact size limit in Course Image Upload |  | 1. Upload a file exactly at the maximum upload size limit in the Course Image Upload field<br>2. Click Save and display | File upload succeeds and is indicated as successfully uploaded | medium |
| TC-012 (data_edge) |  | Upload a file one byte over the maximum size in Course Image Upload |  | 1. Upload a file one byte over the maximum upload size limit in the Course Image Upload field<br>2. Click Save and display | Upload is blocked; error shown indicating the file exceeds the maximum upload size | medium |
| TC-013 (input_edge) |  | Enter a very long string in Course Summary |  | 1. Enter a string longer than 200 characters in the Course Summary field<br>2. Click Save and display | Form submits successfully; the Course Summary is saved with the long string or truncated with a visible indicator | low |
| TC-014 (input_edge) |  | Enter special characters in Course ID Number |  | 1. Enter special characters in the Course ID Number field<br>2. Click Save and display | Form submits successfully or shows a specific error indicating invalid characters in the Course ID Number | low |

---

## Participants Management

Total: **14** (positive: 6, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open enrollment dialog | User logged in as <Role> | 1. Click the 'Enrol users' button | opens enrollment dialog | high |
| TC-002 |  | Apply filters successfully | User logged in as <Role> | 1. Fill in the filter fields as desired<br>2. Click the 'Apply Filters' button | applies the filters | medium |
| TC-003 |  | Clear all filters | User logged in as <Role>, Filters have been applied | 1. Click the 'Clear Filters' button | clears all filters | medium |
| TC-004 |  | Add a new condition to filters | User logged in as <Role> | 1. Click the '+ Add condition' link | adds a new condition | medium |
| TC-005 |  | Filter by alphabetical order A-Z | User logged in as <Role> | 1. Click the 'A–Z' alphabetical filter button | Participants table displays users sorted from A to Z | medium |
| TC-006 |  | Confirm enrollment of a user | User logged in as <Role>, Enrollment dialog is open | 1. Enter <valid user> in the User Search Field<br>2. Select <role> from the Role dropdown<br>3. Click the 'Confirm Enrollment' button | adds user to course at specified role | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to enroll user without filling the required User Search Field |  | 1. Click on the 'Enrol users' button<br>2. Leave the User Search Field blank<br>3. Click the Confirm Enrollment Button | Form does not submit; error shown on User Search Field indicating it is required | high |
| TC-008 |  | Attempt to apply filters without any conditions |  | 1. Click on the Apply Filters Button | Form does not submit; no filters applied; error shown indicating filters are required | medium |
| TC-009 |  | Attempt to add a condition without selecting an attribute |  | 1. Click on the Add Condition Link<br>2. Leave the Select Attribute dropdown blank<br>3. Click the Apply Filters Button | Form does not submit; error shown on Select Attribute indicating it is required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Add condition to filter system at maximum limit | User is on the Participants page | 1. Click on the '+ Add condition' link in the filter system<br>2. Repeat the action until the maximum number of conditions is reached | Adding a new condition succeeds; all conditions are displayed in the filter system. | medium |
| TC-011 (boundary) |  | Attempt to add one more condition beyond maximum limit | User has reached the maximum number of conditions in the filter system | 1. Click on the '+ Add condition' link in the filter system | Adding a new condition is blocked; an error message is displayed indicating the maximum limit has been reached. | medium |
| TC-012 (input_edge) |  | Enter a very long string in the User Search Field | User is in the Enrol users dialog | 1. Enter a string of 200+ characters in the User Search Field | The input is either accepted without truncation or an error message is shown indicating the input is too long. | low |
| TC-013 (input_edge) |  | Enter special characters in the User Search Field | User is in the Enrol users dialog | 1. Enter special characters (e.g., @#$%^&*) in the User Search Field | The input is either accepted or an error message is displayed indicating invalid characters. | low |
| TC-014 (interaction_edge) |  | Rapid re-submission after enrollment dialog success | User has successfully enrolled a user | 1. Click the Confirm Enrollment Button<br>2. Immediately press the back button in the browser | The enrollment dialog is shown blank; no duplicate enrollment occurs. | medium |

---

## Assignment — Teacher View

Total: **8** (positive: 6, negative: 2, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open grading interface for individual students | User logged in as <Teacher>, Assignment page is open | 1. Click the Grade button | opens grading interface for individual students | high |
| TC-002 |  | Navigate to Assignment tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the Assignment tab | The Assignment tab is active and displayed | medium |
| TC-003 |  | Navigate to Settings tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the Settings tab | The Settings tab is active and displayed | medium |
| TC-004 |  | Navigate to Submissions tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the Submissions tab | The Submissions tab is active and displayed | medium |
| TC-005 |  | Navigate to Advanced grading tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the Advanced grading tab | The Advanced grading tab is active and displayed | medium |
| TC-006 |  | Navigate to More tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the More tab | The More tab is active and displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to access the grading interface without any submissions |  | 1. Click on the 'Grade' button | The grading interface does not open; a message indicates 'No submissions available for grading.' | high |
| TC-008 |  | Attempt to navigate to a tab that has no fields or actions |  | 1. Click on the 'Settings' tab | The page displays 'No settings available.' | medium |

---

## Assignment Submissions

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open Grading Workflow for a submission | User logged in as <Teacher>, Submissions table is displayed | 1. Click the action menu for a submission<br>2. Select 'Open Grading Workflow' | The Grading Workflow page for the selected student submission is displayed | high |
| TC-002 |  | Perform Quick Grading on a submission | User logged in as <Teacher>, Quick grading mode is enabled, Submissions table is displayed | 1. Click the action menu for a submission<br>2. Select 'Quick Grading'<br>3. Enter <valid grade> in the grading field | The grading field updates to reflect the entered grade inline in the table | high |
| TC-003 |  | Filter submissions by Submission Status | User logged in as <Teacher>, Submissions table is displayed | 1. Select 'Submitted for grading' from the Submission Status filter<br>2. Click 'Apply Filter' | Only submissions with the status 'Submitted for grading' are displayed in the table; unrelated submissions are no longer visible | medium |
| TC-004 |  | Filter submissions by Grading Status | User logged in as <Teacher>, Submissions table is displayed | 1. Select 'Graded' from the Grading Status filter<br>2. Click 'Apply Filter' | Only submissions with the grading status 'Graded' are displayed in the table; unrelated submissions are no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to open grading workflow without quick grading mode enabled | Quick grading mode is not enabled | 1. Navigate to the Submissions table<br>2. Select a submission row<br>3. Click on 'Open Grading Workflow' | Action is blocked; 'Open Grading Workflow' is not available for selection | high |
| TC-006 |  | Attempt to use quick grading when quick grading mode is not enabled | Quick grading mode is not enabled | 1. Navigate to the Submissions table<br>2. Select a submission row<br>3. Click on 'Quick Grading' | Action is blocked; 'Quick Grading' option is not available for selection | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long string in Submission Comments |  | 1. Navigate to the Submissions table<br>2. Click on the Submission Comments field for a student<br>3. Enter a string of 200+ characters in the Submission Comments field | Submission Comments field displays the entered long text or truncates it with a visible indicator | low |
| TC-008 (input_edge) |  | Enter special characters in Submission Comments |  | 1. Navigate to the Submissions table<br>2. Click on the Submission Comments field for a student<br>3. Enter special characters (e.g., @#$%^&*()!) in the Submission Comments field | Submission Comments field accepts the special characters without error | low |
| TC-009 (input_edge) |  | Enter leading and trailing whitespace in Submission Comments |  | 1. Navigate to the Submissions table<br>2. Click on the Submission Comments field for a student<br>3. Enter a value with leading and trailing spaces in the Submission Comments field | Leading and trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |
| TC-010 (interaction_edge) |  | Rapid re-submission after opening grading workflow |  | 1. Click on the 'Open Grading Workflow' action for a student<br>2. After the grading workflow opens, quickly click the 'Open Grading Workflow' action again | The second action attempt is blocked; the grading workflow does not open a second time until the first is closed | medium |

---

## Gradebook — Grader Report

Total: **11** (positive: 5, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Edit a grade entry successfully | User logged in as <Teacher>, Edit mode is enabled | 1. Click the three-dot menu on a grade cell<br>2. Enter <valid grade> in the grade cell<br>3. Click 'Save Changes' | The grade cell updates to the entered <valid grade> and displays 'applies edits' | high |
| TC-002 |  | Edit grade settings for an activity | User logged in as <Teacher> | 1. Click the action menu on the Grade Column header<br>2. Select 'Edit Grade Settings'<br>3. Adjust the settings as needed<br>4. Click 'Save Changes' | The grade settings are updated and reflected in the Grade Column | medium |
| TC-003 |  | Filter grades by group | User logged in as <Teacher> | 1. Select 'Group 1' from the Group Filter dropdown | The grade table displays only rows for students in 'Group 1'; unrelated rows are no longer visible | medium |
| TC-004 |  | Search for a user in the gradebook | User logged in as <Teacher> | 1. Enter <valid student name> in the User Search field | The grade table displays only rows for <valid student name>; unrelated rows are no longer visible | medium |
| TC-005 |  | View overall average row | User logged in as <Teacher> | 1. Verify the overall average row is visible | The overall average row shows the class average per activity | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to save changes with grades outside the configured range | Edit mode is enabled | 1. Edit a grade cell to a value outside the configured grade range<br>2. Click 'Save Changes' | Form does not submit; grades are not saved; error shown indicating 'Cannot save if values are outside configured grade range' | high |
| TC-007 |  | Attempt to save changes with all grades outside the configured range | Edit mode is enabled | 1. Edit all grade cells to values outside the configured grade range<br>2. Click 'Save Changes' | Form does not submit; grades are not saved; error shown indicating 'Cannot save if values are outside configured grade range' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Edit grade cell with minimum valid grade value | Edit mode is enabled | 1. Navigate to a grade cell<br>2. Enter the minimum valid grade value in the grade cell<br>3. Click 'Save Changes' | Changes are saved successfully; the grade cell displays the minimum valid grade value. | medium |
| TC-009 (boundary) |  | Edit grade cell with maximum valid grade value | Edit mode is enabled | 1. Navigate to a grade cell<br>2. Enter the maximum valid grade value in the grade cell<br>3. Click 'Save Changes' | Changes are saved successfully; the grade cell displays the maximum valid grade value. | medium |
| TC-010 (boundary) |  | Edit grade cell with value below minimum valid grade | Edit mode is enabled | 1. Navigate to a grade cell<br>2. Enter a value below the minimum valid grade in the grade cell<br>3. Click 'Save Changes' | Saving is blocked; an inline error indicates the value is outside the configured grade range. | medium |
| TC-011 (boundary) |  | Edit grade cell with value above maximum valid grade | Edit mode is enabled | 1. Navigate to a grade cell<br>2. Enter a value above the maximum valid grade in the grade cell<br>3. Click 'Save Changes' | Saving is blocked; an inline error indicates the value is outside the configured grade range. | medium |

---

## Profile

Total: **13** (positive: 10, negative: 0, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display Profile Page with User Details | User logged in as <Teacher> | 1. Open the Profile page | The Profile page displays the teacher's circular initials icon, full name, and a 'Message' button | high |
| TC-002 |  | Click Edit Profile Link | User logged in as <Teacher>, Profile page is open | 1. Click on the 'Edit profile' link in the User Details Card | User is redirected to the Edit Profile page | high |
| TC-003 |  | View Data Retention Summary | User logged in as <Teacher>, Profile page is open | 1. Click on the Data Retention Summary link in the Privacy and Policies Card | User is redirected to the Data Retention Summary page | medium |
| TC-004 |  | View Associated Course Profiles | User logged in as <Teacher>, Profile page is open | 1. Click on the Course Profiles link in the Course Details Card | User is redirected to the associated Course Profiles page | medium |
| TC-005 |  | View Blog Entries | User logged in as <Teacher>, Profile page is open | 1. Click on the Blog Entries link in the Miscellaneous Card | User is redirected to the Blog Entries page | medium |
| TC-006 |  | View Forum Posts | User logged in as <Teacher>, Profile page is open | 1. Click on the Forum Posts link in the Miscellaneous Card | User is redirected to the Forum Posts page | medium |
| TC-007 |  | View Forum Discussions | User logged in as <Teacher>, Profile page is open | 1. Click on the Forum Discussions link in the Miscellaneous Card | User is redirected to the Forum Discussions page | medium |
| TC-008 |  | View Learning Plans | User logged in as <Teacher>, Profile page is open | 1. Click on the Learning Plans link in the Miscellaneous Card | User is redirected to the Learning Plans page | medium |
| TC-009 |  | View Browser Sessions | User logged in as <Teacher>, Profile page is open | 1. Click on the Browser Sessions link in the Reports Card | User is redirected to the Browser Sessions page | medium |
| TC-010 |  | View Grades Overview | User logged in as <Teacher>, Profile page is open | 1. Click on the Grades Overview link in the Reports Card | User is redirected to the Grades Overview page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long profile description |  | 1. Navigate to the Profile page<br>2. Enter a string of 200+ characters in the Profile Description field | Profile Description field accepts the input without error; the saved value shows the entire string | low |
| TC-012 (input_edge) |  | Enter special characters in the email address field |  | 1. Navigate to the Profile page<br>2. Enter 'user!@example.com' in the Email Address field | Email Address field displays an error indicating invalid email format | low |
| TC-013 (input_edge) |  | Enter leading and trailing whitespace in the email address field |  | 1. Navigate to the Profile page<br>2. Enter '   user@example.com   ' in the Email Address field | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Profile Edit

Total: **13** (positive: 2, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid information | User logged in as <User> | 1. Open the Edit Profile form<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid email> in the Email Address field<br>5. Click the Update_Profile button | The profile page refreshes to show the updated information | high |
| TC-002 | WF-002 | Cancel profile edit without changes | User logged in as <User> | 1. Open the Edit Profile form<br>2. Click the Cancel button | Exits without making changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Update_Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Update_Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email_Address field blank<br>2. Fill all other required fields<br>3. Click Update_Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First_Name field blank<br>2. Leave the Last_Name field blank<br>3. Leave the Email_Address field blank<br>4. Click Update_Profile | Form does not submit; errors shown on First_Name, Last_Name, and Email_Address fields indicating they are required | high |
| TC-007 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email_Address field<br>2. Fill all other required fields<br>3. Click Update_Profile | Email_Address field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter valid email address at the edge of format validation |  | 1. Enter 'user@example.com' in the Email Address field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Form submits successfully; profile is updated with the email 'user@example.com' | medium |
| TC-009 (boundary) |  | Enter an invalid email address format |  | 1. Enter 'user@.com' in the Email Address field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Email Address displays an error indicating the format is invalid | medium |
| TC-010 (boundary) |  | Upload a file at the maximum size limit for New Picture |  | 1. Upload a file that meets the maximum size limit in the New Picture field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Form submits successfully; profile is updated with the new picture | medium |
| TC-011 (boundary) |  | Upload a file exceeding the maximum size limit for New Picture |  | 1. Upload a file that exceeds the maximum size limit in the New Picture field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | New Picture displays an error indicating the file size exceeds the limit | medium |
| TC-012 (input_edge) |  | Enter a very long string in the Description field |  | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Form submits successfully; profile is updated with the long description | low |
| TC-013 (input_edge) |  | Enter special characters in the First Name field |  | 1. Enter '@John!' in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Form submits successfully; profile is updated with the first name '@John!' | low |

---

## Logout

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User logs out successfully | User logged in as <Authenticated User> | 1. Click the Logout button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to log out while unauthenticated | User is not authenticated | 1. Attempt to click the Logout button | Logout action is blocked; user remains on the current page without being logged out | high |

---
