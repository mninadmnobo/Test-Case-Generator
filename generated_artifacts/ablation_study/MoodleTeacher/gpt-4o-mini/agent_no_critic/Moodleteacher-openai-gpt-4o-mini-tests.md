# Test Cases — Moodleteacher

Generated: 2026-06-10T21:15:23.933145Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 217 | 67 | 74 | 76 | 93 | 92 | 20 |

## Login

Total: **15** (positive: 3, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <Teacher>, User has valid credentials | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |
| TC-002 | WF-003 | Access as a guest | User logged in as <Guest> | 1. Click Access as a guest | Access granted as a guest | medium |
| TC-003 | WF-004 | View cookies notice | User logged in as <Role> | 1. Click Cookies notice | Cookies usage information displayed | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Form does not submit; shows inline error message; Password field is cleared; Username field retains the value | high |
| TC-007 |  | Attempt to access the disabled Lost password link |  | 1. Attempt to click on the Lost password? link | No action occurs; link is disabled | medium |
| TC-008 |  | Attempt to log in as a guest without authentication |  | 1. Click Access as a guest | Access granted as a guest | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Submit with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message shows indicating that both fields are required | medium |
| TC-010 (boundary) | WF-002 | Submit with valid Username and empty Password |  | 1. Enter valid Username in the Username field<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message shows indicating that the Password field is required | medium |
| TC-011 (boundary) | WF-002 | Submit with empty Username and valid Password |  | 1. Leave the Username field empty<br>2. Enter valid Password in the Password field<br>3. Click Log in | Inline error message shows indicating that the Username field is required | medium |
| TC-012 (boundary) | WF-002 | Submit with invalid Username and Password |  | 1. Enter invalid Username in the Username field<br>2. Enter invalid Password in the Password field<br>3. Click Log in | Inline error message shows indicating that the credentials are invalid; Password field is cleared, Username field retains value | medium |
| TC-013 (input_edge) |  | Enter long string in Username field |  | 1. Enter a string longer than 255 characters in the Username field<br>2. Enter valid Password in the Password field<br>3. Click Log in | Inline error message shows indicating that the Username exceeds maximum length | low |
| TC-014 (input_edge) |  | Enter special characters in Username field |  | 1. Enter special characters in the Username field<br>2. Enter valid Password in the Password field<br>3. Click Log in | Inline error message shows indicating that the Username contains invalid characters | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after failed login | An invalid Username and Password have been entered | 1. Click Log in<br>2. Immediately click Log in again | Inline error message still shows; Password field is cleared, Username field retains value | low |

---

## Dashboard

Total: **17** (positive: 5, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar event | User logged in as <Role> | 1. Click the 'New Event' button | A success notification is displayed; the calendar entry is created | high |
| TC-002 | WF-002 | Navigate to the previous month in the calendar | User logged in as <Role> | 1. Click the 'Previous Month' button | The calendar displays the previous month | medium |
| TC-003 | WF-003 | Navigate to the next month in the calendar | User logged in as <Role> | 1. Click the 'Next Month' button | The calendar displays the next month | medium |
| TC-004 | WF-004 | Open the full calendar view | User logged in as <Role> | 1. Click the 'Full calendar' link | The dedicated calendar view is opened | medium |
| TC-005 | WF-005 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or export calendars' link | The calendar data management is opened | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Time Range dropdown blank and submit |  | 1. Leave the Time Range dropdown blank<br>2. Click on the New Event button | Form does not submit; Time Range field is highlighted and displays an error: 'This field is required.' | high |
| TC-007 |  | Attempt to create a new calendar event without selecting a course |  | 1. Click on the New Event button | Form does not submit; All Courses field is highlighted and displays an error: 'This field is required.' | high |
| TC-008 | WF-001 | Attempt to create a new calendar event without filling required fields |  | 1. Click on the New Event button | Form does not submit; All Courses field is highlighted and displays an error: 'This field is required.' | high |
| TC-009 | WF-002 | Attempt to navigate to the previous month when already in the first month |  | 1. Click on the Previous Month button | No navigation occurs; the current month remains displayed. | medium |
| TC-010 | WF-003 | Attempt to navigate to the next month when already in the last month |  | 1. Click on the Next Month button | No navigation occurs; the current month remains displayed. | medium |
| TC-011 | WF-004 | Attempt to open full calendar view without authentication |  | 1. Click on the Full calendar link | User is redirected to the login page. | high |
| TC-012 | WF-005 | Attempt to open calendar data management without authentication |  | 1. Click on the Import or export calendars link | User is redirected to the login page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapid submission of new calendar events | User is on the Dashboard | 1. Click the 'New event' button<br>2. Fill in the event details<br>3. Click 'Submit'<br>4. Immediately click 'New event' button again | The second submission attempt is blocked; the calendar entry is created successfully for the first submission. | medium |
| TC-014 (interaction_edge) | WF-002 | Navigate to previous month from the current month | User is on the Dashboard | 1. Click 'Previous Month' button | The calendar view updates to display the previous month. | medium |
| TC-015 (interaction_edge) | WF-003 | Navigate to next month from the current month | User is on the Dashboard | 1. Click 'Next Month' button | The calendar view updates to display the next month. | medium |
| TC-016 (interaction_edge) | WF-004 | Open full calendar view | User is on the Dashboard | 1. Click the 'Full calendar' link | The dedicated calendar view opens successfully. | medium |
| TC-017 (interaction_edge) | WF-005 | Open calendar data management | User is on the Dashboard | 1. Click the 'Import or export calendars' link | The calendar data management opens successfully. | medium |

---

## Dashboard — Edit Mode

Total: **18** (positive: 6, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset page to default | User logged in as <Role>, Edit mode is enabled | 1. Click 'Reset page to default' | The layout resets to default | high |
| TC-002 | WF-002 | Add a block | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block' | opens Add a block page | high |
| TC-003 | WF-003 | Cancel adding a block | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block'<br>2. Click 'Cancel' | returns to Dashboard without adding a block | medium |
| TC-004 | WF-004 | Configure existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the options menu of an existing block<br>2. Select 'Configure' | Configuration options for the block are displayed | medium |
| TC-005 | WF-005 | Move existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the move icon of an existing block<br>2. Drag the block to a new position | Block moved to new position | medium |
| TC-006 | WF-006 | Delete existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the options menu of an existing block<br>2. Select 'Delete' | Block deleted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to reset layout without any changes made |  | 1. Toggle Edit mode on<br>2. Click 'Reset page to default' | No changes occur; layout remains unchanged |  |
| TC-008 |  | Attempt to add a block without any existing blocks |  | 1. Toggle Edit mode on<br>2. Click '+ Add a block' | 'Add a block' page opens showing available block types |  |
| TC-009 |  | Click 'Cancel' without adding a block |  | 1. Toggle Edit mode on<br>2. Click 'Cancel' | Returns to Dashboard without adding a block |  |
| TC-010 |  | Attempt to configure a block that does not exist |  | 1. Toggle Edit mode on<br>2. Click 'Configure' on a non-existent block | Error message displayed indicating the block does not exist |  |
| TC-011 |  | Attempt to move a block that does not exist |  | 1. Toggle Edit mode on<br>2. Click 'Move' on a non-existent block | Error message displayed indicating the block does not exist |  |
| TC-012 |  | Attempt to delete a block that does not exist |  | 1. Toggle Edit mode on<br>2. Click 'Delete' on a non-existent block | Error message displayed indicating the block does not exist |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapidly click 'Reset page to default' multiple times | Edit mode is toggled on | 1. Click 'Reset page to default'<br>2. Immediately click 'Reset page to default' again | 'Reset page to default' action succeeds; layout is reset to default without errors. |  |
| TC-014 (interaction_edge) | WF-002 | Rapidly click '+ Add a block' multiple times | Edit mode is toggled on | 1. Click '+ Add a block'<br>2. Immediately click '+ Add a block' again | Only one 'Add a block' page opens; no duplicate pages are created. |  |
| TC-015 (interaction_edge) | WF-003 | Click 'Cancel' after opening 'Add a block' page | Edit mode is toggled on, Add a block page is opened | 1. Click 'Cancel' on the Add a block page | Returns to Dashboard without adding a block; no new block is created. |  |
| TC-016 (interaction_edge) | WF-004 | Attempt to configure a block while another configuration is open | Edit mode is toggled on, Configuration options for one block are open | 1. Click 'Configure' on another existing block | Only one configuration menu is open at a time; previous configuration options are closed. |  |
| TC-017 (interaction_edge) | WF-005 | Move an existing block while another move action is in progress | Edit mode is toggled on, Block is being moved | 1. Attempt to move another existing block | Only one block can be moved at a time; the action is blocked with a visible error. |  |
| TC-018 (interaction_edge) | WF-006 | Delete a block while another delete action is in progress | Edit mode is toggled on, Block is being deleted | 1. Attempt to delete another existing block | Only one block can be deleted at a time; the action is blocked with a visible error. |  |

---

## My Courses

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Teacher> | 1. Locate the course card for <Course Name><br>2. Click the three-dot menu on the course card<br>3. Select 'Star this course' from the menu | The course is pinned to the top | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Teacher> | 1. Locate the course card for <Course Name><br>2. Click the three-dot menu on the course card<br>3. Select 'Remove from view' from the menu | The course is hidden without affecting enrollment | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to star a course when it is already starred | The course is already starred | 1. Click on the 'Star this course' option for the already starred course | The course remains starred; no change occurs | high |
| TC-004 |  | Attempt to remove a course from view when it is already hidden | The course is already hidden | 1. Click on the 'Remove from view' option for the already hidden course | The course remains hidden; no change occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapidly star a course after pinning it | A course is currently displayed in the course grid | 1. Click the three-dot menu on the course card.<br>2. Select 'Star this course'.<br>3. Immediately click the three-dot menu again.<br>4. Select 'Star this course' again. | The course remains pinned to the top; no duplicate action occurs. | medium |
| TC-006 (interaction_edge) | WF-002 | Rapidly remove a course from view after hiding it | A course is currently displayed in the course grid | 1. Click the three-dot menu on the course card.<br>2. Select 'Remove from view'.<br>3. Immediately click the three-dot menu again.<br>4. Select 'Remove from view' again. | The course remains hidden; no duplicate action occurs. | medium |
| TC-007 (input_edge) |  | Search with leading and trailing whitespace | The search field is visible | 1. Enter '   course name   ' in the search field.<br>2. Click the search button. | The search results display 'course name' without leading or trailing spaces. | low |
| TC-008 (input_edge) |  | Search with special characters | The search field is visible | 1. Enter '@course#name$' in the search field.<br>2. Click the search button. | The search results display relevant courses or an error indicating invalid characters. | low |

---

## Course Page

Total: **15** (positive: 5, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Activity 1 | User logged in as <role> | 1. Click on 'Activity 1' | Navigated to Activity 1 | high |
| TC-002 | WF-002 | Access Resource 1 | User logged in as <role> | 1. Click on 'Resource 1' | Navigated to Resource 1 | high |
| TC-003 | WF-003 | Access Activity 2 | User logged in as <role> | 1. Click on 'Activity 2' | Navigated to Activity 2 | high |
| TC-004 | WF-004 | Access Resource 2 | User logged in as <role> | 1. Click on 'Resource 2' | Navigated to Resource 2 | high |
| TC-005 | WF-005 | Collapse All Sections | User logged in as <role> | 1. Click on 'Collapse all' link | All sections collapsed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to access Activity 1 without being logged in | User is not authenticated | 1. Navigate to the Course Page<br>2. Click on Activity 1 | User is redirected to the login page | high |
| TC-007 | WF-002 | Attempt to access Resource 1 without being logged in | User is not authenticated | 1. Navigate to the Course Page<br>2. Click on Resource 1 | User is redirected to the login page | high |
| TC-008 | WF-003 | Attempt to access Activity 2 without being logged in | User is not authenticated | 1. Navigate to the Course Page<br>2. Click on Activity 2 | User is redirected to the login page | high |
| TC-009 | WF-004 | Attempt to access Resource 2 without being logged in | User is not authenticated | 1. Navigate to the Course Page<br>2. Click on Resource 2 | User is redirected to the login page | high |
| TC-010 | WF-005 | Attempt to collapse all sections without being logged in | User is not authenticated | 1. Navigate to the Course Page<br>2. Click on Collapse all | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-005 | Rapidly click the Collapse All link twice | Course page is fully loaded with sections expanded | 1. Click the Collapse All link<br>2. Immediately click the Collapse All link again | All sections remain collapsed; no error shown | medium |
| TC-012 (interaction_edge) | WF-001 | Access Activity 1 after collapsing all sections | All sections are collapsed | 1. Click the Collapse All link<br>2. Click on Activity 1 link | Navigated to Activity 1; the page displays Activity 1 content | medium |
| TC-013 (interaction_edge) | WF-002 | Access Resource 1 after collapsing all sections | All sections are collapsed | 1. Click the Collapse All link<br>2. Click on Resource 1 link | Navigated to Resource 1; the page displays Resource 1 content | medium |
| TC-014 (interaction_edge) | WF-003 | Access Activity 2 after collapsing all sections | All sections are collapsed | 1. Click the Collapse All link<br>2. Click on Activity 2 link | Navigated to Activity 2; the page displays Activity 2 content | medium |
| TC-015 (interaction_edge) | WF-004 | Access Resource 2 after collapsing all sections | All sections are collapsed | 1. Click the Collapse All link<br>2. Click on Resource 2 link | Navigated to Resource 2; the page displays Resource 2 content | medium |

---

## Course Edit Mode and Activity Chooser

Total: **36** (positive: 14, negative: 14, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Enable Edit Mode | User logged in as <role> | 1. Click the Edit Mode button | turns the Course page into an authoring interface | high |
| TC-002 | WF-002 | Open Activity Chooser | User logged in as <role>, Edit mode is enabled | 1. Click the + Add an activity or resource button | opens Activity Chooser modal | high |
| TC-003 | WF-003 | Add Activity from Activity Chooser | User logged in as <role>, Edit mode is enabled, Activity Chooser modal is open | 1. Select a tile from the Activity Resource Tiles<br>2. Click the Add button | opens the selected activity's creation form | high |
| TC-004 | WF-004 | Batch Edit Activities | User logged in as <role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Edit in the Bulk Actions Toolbar | Batch edit action performed | medium |
| TC-005 | WF-005 | Batch Duplicate Activities | User logged in as <role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Duplicate in the Bulk Actions Toolbar | Batch duplicate action performed | medium |
| TC-006 | WF-006 | Batch Hide Activities | User logged in as <role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Hide in the Bulk Actions Toolbar | Batch hide action performed | medium |
| TC-007 | WF-007 | Batch Delete Activities | User logged in as <role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Delete in the Bulk Actions Toolbar | Batch delete action performed | medium |
| TC-008 | WF-008 | Batch Move Activities | User logged in as <role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Move in the Bulk Actions Toolbar | Batch move action performed | medium |
| TC-009 | WF-009 | Edit Activity | User logged in as <role>, Edit mode is enabled | 1. Click the edit icon for quick renaming on an activity | Activity edited | medium |
| TC-010 | WF-010 | Duplicate Activity | User logged in as <role>, Edit mode is enabled | 1. Click the section menu on an activity<br>2. Select duplicate | Activity duplicated | medium |
| TC-011 | WF-011 | Hide Activity | User logged in as <role>, Edit mode is enabled | 1. Click the section menu on an activity<br>2. Select hide | Activity hidden | medium |
| TC-012 | WF-012 | Delete Activity | User logged in as <role>, Edit mode is enabled | 1. Click the section menu on an activity<br>2. Select delete | Activity deleted | medium |
| TC-013 | WF-013 | Move Activity | User logged in as <role>, Edit mode is enabled | 1. Click the section menu on an activity<br>2. Select move | Activity moved | medium |
| TC-014 | WF-014 | Set Access Restrictions on Activity | User logged in as <role>, Edit mode is enabled | 1. Click the section menu on an activity<br>2. Select set access restrictions | Access restrictions set | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 | WF-001 | Attempt to enable Edit Mode without proper permissions | User is not authorized to edit | 1. Click on the Edit_Mode button | User is blocked from enabling Edit Mode; no changes occur to the Course page | high |
| TC-016 | WF-002 | Attempt to open Activity Chooser without enabling Edit Mode | Edit Mode is not enabled | 1. Click on the Add_Activity_Button | Activity Chooser modal does not open; no changes occur | high |
| TC-017 | WF-003 | Attempt to add activity without selecting an activity tile | Activity Chooser modal is open | 1. Click on the Add_Button without selecting any tile | No activity is added; error message indicates that a tile must be selected | high |
| TC-018 | WF-004 | Attempt to batch edit activities without selecting any activities | No activities are selected | 1. Click on the Batch Edit button | Batch edit action is blocked; no changes occur | high |
| TC-019 | WF-005 | Attempt to batch duplicate activities without selecting any activities | No activities are selected | 1. Click on the Batch Duplicate button | Batch duplicate action is blocked; no changes occur | high |
| TC-020 | WF-006 | Attempt to batch hide activities without selecting any activities | No activities are selected | 1. Click on the Batch Hide button | Batch hide action is blocked; no changes occur | high |
| TC-021 | WF-007 | Attempt to batch delete activities without selecting any activities | No activities are selected | 1. Click on the Batch Delete button | Batch delete action is blocked; no changes occur | high |
| TC-022 | WF-008 | Attempt to batch move activities without selecting any activities | No activities are selected | 1. Click on the Batch Move button | Batch move action is blocked; no changes occur | high |
| TC-023 | WF-009 | Attempt to edit an activity without selecting it | No activity is selected | 1. Click on the Edit icon | Edit action is blocked; no changes occur | high |
| TC-024 | WF-010 | Attempt to duplicate an activity without selecting it | No activity is selected | 1. Click on the duplicate option in the Section Menu | Duplicate action is blocked; no changes occur | high |
| TC-025 | WF-011 | Attempt to hide an activity without selecting it | No activity is selected | 1. Click on the hide option in the Activity Menu | Hide action is blocked; no changes occur | high |
| TC-026 | WF-012 | Attempt to delete an activity without selecting it | No activity is selected | 1. Click on the delete option in the Activity Menu | Delete action is blocked; no changes occur | high |
| TC-027 | WF-013 | Attempt to move an activity without selecting it | No activity is selected | 1. Click on the move option in the Activity Menu | Move action is blocked; no changes occur | high |
| TC-028 | WF-014 | Attempt to set access restrictions on an activity without selecting it | No activity is selected | 1. Click on the set access restrictions option in the Activity Menu | Set access restrictions action is blocked; no changes occur | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 (boundary) | WF-001 | Enable Edit Mode with valid user role | User is logged in with a valid role | 1. Click the Edit_Mode button | Course page turns into an authoring interface | medium |
| TC-030 (boundary) | WF-002 | Open Activity Chooser after enabling Edit Mode | User is in Edit Mode | 1. Click the + Add an activity or resource button | Activity Chooser modal opens | medium |
| TC-031 (boundary) | WF-003 | Add Activity from Activity Chooser with valid selection | Activity Chooser modal is open, A valid activity is selected | 1. Click the Add button | Selected activity's creation form opens | medium |
| TC-032 (boundary) | WF-004 | Batch Edit Activities with valid selection | Multiple activities are selected | 1. Click the Batch Edit button | Batch edit action performed | medium |
| TC-033 (boundary) | WF-005 | Batch Duplicate Activities with valid selection | Multiple activities are selected | 1. Click the Batch Duplicate button | Batch duplicate action performed | medium |
| TC-034 (boundary) | WF-006 | Batch Hide Activities with valid selection | Multiple activities are selected | 1. Click the Batch Hide button | Batch hide action performed | medium |
| TC-035 (boundary) | WF-007 | Batch Delete Activities with valid selection | Multiple activities are selected | 1. Click the Batch Delete button | Batch delete action performed | medium |
| TC-036 (boundary) | WF-008 | Batch Move Activities with valid selection | Multiple activities are selected | 1. Click the Batch Move button | Batch move action performed | medium |

---

## Assignment Creation

Total: **19** (positive: 4, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create assignment and redirect to course page | User logged in as <Role> | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Click 'Save and return to course' | Assignment is created and redirects to the course page | high |
| TC-002 | WF-002 | Create assignment and open new assignment's page | User logged in as <Role> | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Click 'Save and display' | Assignment is created and opens the new assignment's page | high |
| TC-003 | WF-003 | Discard changes on assignment creation | User logged in as <Role> | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Click 'Cancel' | All changes are discarded | medium |
| TC-004 | WF-001 | Create assignment with file submissions enabled | User logged in as <Role> | 1. Enter <Assignment Name> in the Assignment Name field<br>2. Check the 'File Submissions' checkbox<br>3. Enter <Max Uploaded Files> in the Max Uploaded Files field<br>4. Enter <Max Submission Size> in the Max Submission Size field<br>5. Click 'Save and return to course' | Assignment is created and redirects to the course page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Assignment Name field blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other fields with valid data<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-006 | WF-002 | Leave the Assignment Name field blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other fields with valid data<br>3. Click 'Save and display' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-007 |  | Attempt to submit with all required fields empty |  | 1. Leave the Assignment_Name field blank<br>2. Click 'Save and return to course' | Inline validation error appears on the Assignment_Name field indicating it is required; form does not submit; assignment is not created | high |
| TC-008 |  | Attempt to submit with all required fields empty |  | 1. Leave the Assignment_Name field blank<br>2. Click 'Save and display' | Inline validation error appears on the Assignment_Name field indicating it is required; form does not submit; assignment is not created | high |
| TC-009 |  | Attempt to submit with an invalid date in Allow Submissions From field when toggle is on |  | 1. Check the Allow_Submissions_From_Toggle<br>2. Enter <invalid date> in the Allow_Submissions_From field<br>3. Click 'Save and return to course' | Inline validation error appears on the Allow_Submissions_From field indicating it must be a valid date; form does not submit; assignment is not created | medium |
| TC-010 |  | Attempt to submit with an invalid date in Due Date field when toggle is on |  | 1. Check the Due_Date_Toggle<br>2. Enter <invalid date> in the Due_Date field<br>3. Click 'Save and return to course' | Inline validation error appears on the Due_Date field indicating it must be a valid date; form does not submit; assignment is not created | medium |
| TC-011 |  | Attempt to submit with an invalid date in Cut Off Date field when toggle is on |  | 1. Check the Cut_Off_Date_Toggle<br>2. Enter <invalid date> in the Cut_Off_Date field<br>3. Click 'Save and return to course' | Inline validation error appears on the Cut_Off_Date field indicating it must be a valid date; form does not submit; assignment is not created | medium |
| TC-012 |  | Attempt to add a restriction without selecting a restriction type |  | 1. Click on the Add_Restriction_Button<br>2. Click 'Save and return to course' | Inline validation error appears indicating a restriction type must be selected; form does not submit; assignment is not created | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Enter maximum allowed files for file submissions | File submissions checkbox is enabled | 1. Enable File submissions<br>2. Enter <maximum allowed files> in the Max Uploaded Files field | Form submits successfully; assignment is created with the maximum allowed files | medium |
| TC-014 (boundary) |  | Attempt to add one more file than the maximum allowed | File submissions checkbox is enabled | 1. Enable File submissions<br>2. Enter <maximum allowed files + 1> in the Max Uploaded Files field | Max Uploaded Files field displays an error indicating the value exceeds the maximum allowed | medium |
| TC-015 (boundary) |  | Enter maximum submission size | File submissions checkbox is enabled | 1. Enable File submissions<br>2. Enter <maximum submission size> in the Max Submission Size field | Form submits successfully; assignment is created with the maximum submission size | medium |
| TC-016 (boundary) |  | Attempt to exceed maximum submission size | File submissions checkbox is enabled | 1. Enable File submissions<br>2. Enter <maximum submission size + 1> in the Max Submission Size field | Max Submission Size field displays an error indicating the value exceeds the maximum allowed | medium |
| TC-017 (interaction_edge) | WF-001 | Rapid re-submission after creating assignment | Assignment is created successfully | 1. Click Save and return to course<br>2. Press the browser back button | User is redirected to the course page without a second assignment being created | low |
| TC-018 (input_edge) |  | Enter a very long assignment name |  | 1. Enter a string of 200+ characters in the Assignment Name field | Assignment Name field accepts the input without truncation or displays an error | low |
| TC-019 (input_edge) |  | Enter special characters in the Assignment Name field |  | 1. Enter special characters (e.g., !@#$%^&*) in the Assignment Name field | Assignment Name field accepts the special characters without error | low |

---

## Course Settings

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Save course settings with all required fields filled | User logged in as <Role> | 1. Enter <valid full course name> in the Course Full Name field<br>2. Enter <valid short course name> in the Course Short Name field<br>3. Select <valid category> from the Course Category dropdown<br>4. Select 'Show' from the Course Visibility dropdown<br>5. Click 'Save and display' | persists the configuration and returns to the course page | high |
| TC-002 | WF-002 | Cancel course settings without saving | User logged in as <Role> | 1. Enter <valid full course name> in the Course Full Name field<br>2. Enter <valid short course name> in the Course Short Name field<br>3. Select <valid category> from the Course Category dropdown<br>4. Click 'Cancel' | leaves existing settings unchanged | medium |
| TC-003 | WF-001 | Save course settings with optional fields filled | User logged in as <Role> | 1. Enter <valid full course name> in the Course Full Name field<br>2. Enter <valid short course name> in the Course Short Name field<br>3. Select <valid category> from the Course Category dropdown<br>4. Select 'Show' from the Course Visibility dropdown<br>5. Enter <valid start date> in the Course Start Date field<br>6. Enter <valid end date> in the Course End Date field<br>7. Enter <valid course ID number> in the Course ID Number field<br>8. Enter <valid summary> in the Course Summary field<br>9. Click 'Save and display' | persists the configuration and returns to the course page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Course Full Name field blank |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Course Short Name field blank |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-006 | WF-001 | Leave the Course Category field unselected |  | 1. Leave the Course Category field unselected<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Save and display | Inline validation errors appear on the Course Full Name, Course Short Name, and Course Category fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter maximum length string in Course Full Name |  | 1. Enter a string of maximum allowed length in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the maximum length string in the Course Full Name field | medium |
| TC-009 (boundary) |  | Enter one character less than maximum length in Course Short Name |  | 1. Enter a string of maximum allowed length - 1 in the Course Short Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the string in the Course Short Name field | medium |
| TC-010 (input_edge) |  | Enter a very long string in Course Summary |  | 1. Enter a string of 200+ characters in the Course Summary field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; Course Summary displays the long string or is truncated with a visible indicator | low |
| TC-011 (input_edge) |  | Enter special characters in Course ID Number |  | 1. Enter special characters in the Course ID Number field<br>2. Fill all other required fields<br>3. Click Save and display | Inline error is displayed indicating that the input is invalid for the Course ID Number field | low |
| TC-012 (input_edge) |  | Enter leading and trailing whitespace in Course Full Name |  | 1. Enter leading and trailing whitespace in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-013 (state_edge) |  | Rapidly toggle Course End Date visibility | Enable toggle is on | 1. Toggle the visibility of Course End Date<br>2. Immediately toggle back to hide Course End Date<br>3. Click Save and display | Form submits successfully; Course End Date visibility state is accurately reflected in the saved configuration | medium |

---

## Participants Management

Total: **19** (positive: 8, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters successfully | User logged in as <Role>, No filters are currently applied | 1. Click the Apply Filters Button | Filters are applied | high |
| TC-002 | WF-002 | Clear filters successfully | User logged in as <Role>, Some filters are currently applied | 1. Click the Clear Filters Button | All filters are cleared | high |
| TC-003 | WF-003 | Open enrollment dialog | User logged in as <Role> | 1. Click the Enrol Users Button | Enrollment dialog opens | high |
| TC-004 | WF-004 | Confirm user enrollment | User logged in as <Role>, Enrollment dialog is open | 1. Enter <valid user> in the User Search Field<br>2. Click the Confirm Enrollment Button | User is added to the course at specified role | high |
| TC-005 | WF-005 | View user profile | User logged in as <Role>, Participants Table is displayed | 1. Click the View Profile action for a user in the Participants Table | User profile is displayed | medium |
| TC-006 | WF-006 | Edit user role | User logged in as <Role>, Participants Table is displayed | 1. Click the Edit Role action for a user in the Participants Table | User role editing interface is displayed | medium |
| TC-007 | WF-007 | Send message to user | User logged in as <Role>, Participants Table is displayed | 1. Click the Send Message action for a user in the Participants Table | Message sending interface is displayed | medium |
| TC-008 | WF-008 | Apply bulk actions to selected users | User logged in as <Role>, Some users are selected in the Participants Table | 1. Click the With selected users… dropdown<br>2. Select an action from the dropdown | Bulk action is applied to checked participants | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the User Search Field blank in the enrollment dialog |  | 1. Click on the Enrol Users Button<br>2. Leave the User Search Field blank<br>3. Click Confirm Enrollment Button | Form does not submit; User Search Field is highlighted; inline validation error appears on the User Search Field indicating it is required | high |
| TC-010 |  | Attempt to apply filters without any conditions |  | 1. Click Apply Filters Button | Form does not submit; no filters applied; error shown indicating at least one condition is required | high |
| TC-011 |  | Attempt to confirm enrollment without filling the User Search Field |  | 1. Click on the Enrol Users Button<br>2. Leave the User Search Field blank<br>3. Click Confirm Enrollment Button | Form does not submit; User Search Field is highlighted; inline validation error appears on the User Search Field indicating it is required | high |
| TC-012 | WF-008 | Attempt bulk action with no selected users |  | 1. Click on the With selected users… dropdown<br>2. Select an action<br>3. Click Apply | Action does not execute; error shown indicating no users selected for bulk action | medium |
| TC-013 | WF-002 | Attempt to clear filters without applying any filters |  | 1. Click Clear Filters Button | No filters cleared; no changes made; confirmation message indicating no filters were applied | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Apply filters with maximum number of conditions | User is on the Participants page | 1. Click on 'Add Condition' link to add a condition<br>2. Repeat step 1 until the maximum number of conditions is reached<br>3. Click 'Apply Filters Button' | Filters are applied successfully with all conditions included | medium |
| TC-015 (boundary) | WF-001 | Attempt to apply filters with one condition over maximum allowed | User is on the Participants page | 1. Click on 'Add Condition' link to add a condition<br>2. Repeat step 1 until the maximum number of conditions is reached<br>3. Click on 'Add Condition' link one more time<br>4. Click 'Apply Filters Button' | Filters application is blocked; error message indicates maximum conditions exceeded | medium |
| TC-016 (boundary) | WF-004 | Confirm enrollment with maximum allowed duration | User is in the enrollment dialog | 1. Enter a valid user in the 'User Search Field'<br>2. Select a role from the 'Role Dropdown'<br>3. Set the 'Enrollment Duration Control' to the maximum allowed duration<br>4. Click 'Confirm Enrollment Button' | User is added to the course with the specified role and maximum duration | medium |
| TC-017 (boundary) | WF-004 | Attempt to confirm enrollment with duration exceeding maximum | User is in the enrollment dialog | 1. Enter a valid user in the 'User Search Field'<br>2. Select a role from the 'Role Dropdown'<br>3. Set the 'Enrollment Duration Control' to a value exceeding maximum allowed duration<br>4. Click 'Confirm Enrollment Button' | Enrollment confirmation is blocked; error message indicates duration exceeds maximum allowed | medium |
| TC-018 (input_edge) |  | Search with leading and trailing whitespace in user search field | User is in the enrollment dialog | 1. Enter '   testuser   ' in the 'User Search Field'<br>2. Click 'Confirm Enrollment Button' | Leading/trailing whitespace is trimmed; user search is executed for 'testuser' | low |
| TC-019 (input_edge) |  | Search with special characters in user search field | User is in the enrollment dialog | 1. Enter '@#$%^&*()' in the 'User Search Field'<br>2. Click 'Confirm Enrollment Button' | Search is executed; appropriate error message is shown for invalid input | low |

---

## Assignment — Teacher View

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open grading interface for individual students | User logged in as <Teacher>, Assignment page is open | 1. Click the Grade button on the Assignment tab | opens grading interface for individual students | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to open grading interface without required permissions | User is not logged in as a Teacher | 1. Attempt to click the Grade button | User is redirected to the login page; grading interface does not open | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapidly click the Grade button multiple times | User is on the Assignment page | 1. Click the Grade button<br>2. Immediately click the Grade button again | The grading interface opens successfully; no duplicate grading interfaces are shown. | medium |

---

## Assignment Submissions

Total: **8** (positive: 3, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Grading Workflow for a submission | User logged in as <Role> | 1. Search for a submission by entering <valid student name> in the Student Name search field<br>2. Click the action menu for the submission row<br>3. Select 'Open Grading Workflow' from the action menu | Grading workflow opened for the selected submission | high |
| TC-002 |  | Filter submissions by Submission Status | User logged in as <Role> | 1. Select 'Submitted for grading' from the Submission Status dropdown<br>2. Observe the submissions table | Only submissions with the status 'Submitted for grading' are displayed; unrelated submissions are no longer visible | medium |
| TC-003 |  | Filter submissions by Grading Status | User logged in as <Role> | 1. Select 'Graded' from the Grading Status dropdown<br>2. Observe the submissions table | Only submissions with the grading status 'Graded' are displayed; unrelated submissions are no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to open grading workflow without selecting a submission |  | 1. Navigate to the Submissions view<br>2. Click on 'Open Grading Workflow' without selecting any submission | No grading workflow opens; an error message indicates that a submission must be selected first. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long student name in the search field |  | 1. Enter a string of 200+ characters in the Student_Name search field<br>2. Click the search button | The search either succeeds and displays results or shows a truncation error message | low |
| TC-006 (input_edge) |  | Enter special characters in the search field |  | 1. Enter '@#$%^&*()' in the Student_Name search field<br>2. Click the search button | The search either succeeds and displays results or shows an error message indicating invalid input | low |
| TC-007 (input_edge) |  | Enter whitespace in the search field |  | 1. Enter '    ' (leading and trailing spaces) in the Student_Name search field<br>2. Click the search button | The search is processed, and the input is trimmed; the results show without extra spaces | low |
| TC-008 (interaction_edge) | WF-001 | Rapidly open grading workflow for the same submission | At least one submission is displayed in the table | 1. Click 'Open Grading Workflow' for a submission<br>2. Immediately click 'Open Grading Workflow' for the same submission again | The second action is blocked with a message indicating the workflow is already open or is queued for processing | medium |

---

## Gradebook — Grader Report

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit Grade Settings for an Activity | User logged in as <Role> | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Click the action menu on the 'Activity' column header<br>3. Select 'Edit Grade Settings' from the options | Edits applied to grade settings | high |
| TC-002 | WF-002 | Edit Grade Entry for a Student | User logged in as <Role> | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Click the three-dot menu on a grade cell for a student<br>3. Select 'Edit Grade Entry' from the options | Grade entry updated | high |
| TC-003 | WF-003 | Save changes in Edit Mode | User logged in as <Role>, Edit mode is enabled | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Edit a grade cell inline<br>3. Click 'Save changes' | applies edits | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Attempt to save changes with grades outside the configured range | Edit mode is enabled | 1. Enter <grade below minimum> in a grade cell<br>2. Click 'Save changes' | Inline validation error appears indicating 'Values must be within configured grade range'; changes are not saved | high |
| TC-005 |  | Attempt to access Edit Grade Settings without required permissions | User does not have permission to edit grade settings | 1. Click on the action menu for an activity<br>2. Select 'Edit Grade Settings' | Access is denied; the action is not available | high |
| TC-006 |  | Attempt to edit a grade entry without required permissions | User does not have permission to edit grade entries | 1. Click on the three-dot menu for a student's grade entry<br>2. Select 'Edit Grade Entry' | Access is denied; the action is not available | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-003 | Save changes with minimum grade value | Edit mode is enabled, Grade range is configured with a minimum value | 1. Enter the minimum allowed grade value in the grade cell<br>2. Click Save changes | Form submits successfully; edits are applied to the grade entry | medium |
| TC-008 (boundary) | WF-003 | Save changes with one unit below minimum grade value | Edit mode is enabled, Grade range is configured with a minimum value | 1. Enter one unit below the minimum allowed grade value in the grade cell<br>2. Click Save changes | Inline error displayed indicating the value is below the configured grade range | medium |
| TC-009 (boundary) | WF-003 | Save changes with maximum grade value | Edit mode is enabled, Grade range is configured with a maximum value | 1. Enter the maximum allowed grade value in the grade cell<br>2. Click Save changes | Form submits successfully; edits are applied to the grade entry | medium |
| TC-010 (boundary) | WF-003 | Save changes with one unit above maximum grade value | Edit mode is enabled, Grade range is configured with a maximum value | 1. Enter one unit above the maximum allowed grade value in the grade cell<br>2. Click Save changes | Inline error displayed indicating the value exceeds the configured grade range | medium |

---

## Profile

Total: **19** (positive: 7, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View User Details | User logged in as <Teacher> | 1. Navigate to the Profile page | User details displayed | high |
| TC-002 | WF-002 | View Privacy and Policies | User logged in as <Teacher> | 1. Navigate to the Profile page | Privacy and policies information displayed | high |
| TC-003 | WF-003 | View Course Details | User logged in as <Teacher> | 1. Navigate to the Profile page | Course details displayed | high |
| TC-004 | WF-004 | View Miscellaneous Links | User logged in as <Teacher> | 1. Navigate to the Profile page | Miscellaneous links displayed | high |
| TC-005 | WF-005 | View Reports | User logged in as <Teacher> | 1. Navigate to the Profile page | Reports information displayed | high |
| TC-006 | WF-006 | View Login Activity | User logged in as <Teacher> | 1. Navigate to the Profile page | Login activity information displayed | high |
| TC-007 | WF-007 | Send Message | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click the Message button | Message sent successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Attempt to view user details without being logged in | User is not authenticated | 1. Navigate to the Profile page | User is redirected to the login page | high |
| TC-009 | WF-002 | Attempt to view privacy and policies without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on Data Retention Summary Link | User is redirected to the login page | high |
| TC-010 | WF-003 | Attempt to view course details without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on Associated Course Profiles Links | User is redirected to the login page | high |
| TC-011 | WF-004 | Attempt to view miscellaneous links without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on Blog Entries Links | User is redirected to the login page | high |
| TC-012 | WF-005 | Attempt to view reports without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on Browser Sessions Link | User is redirected to the login page | high |
| TC-013 | WF-006 | Attempt to view login activity without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on First Access | User is redirected to the login page | high |
| TC-014 | WF-007 | Attempt to send a message without being logged in | User is not authenticated | 1. Navigate to the Profile page<br>2. Click on Message Button | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-001 | View User Details with empty Email Address |  | 1. Navigate to the Profile page<br>2. Ensure the Email Address field is empty<br>3. Click on the Edit_Profile_Link | User details displayed with Email Address field showing as empty | medium |
| TC-016 (boundary) | WF-006 | View Login Activity with no Last Access |  | 1. Navigate to the Profile page<br>2. Ensure the Last Access field is empty<br>3. Click on the First_Access field | Login activity information displayed with Last Access field showing as empty | medium |
| TC-017 (input_edge) |  | Enter long text in Associated Course Profiles Links |  | 1. Navigate to the Profile page<br>2. Enter a very long string (200+ characters) in the Associated Course Profiles Links field | Field displays an error indicating the input exceeds the maximum allowed length | low |
| TC-018 (input_edge) |  | Enter special characters in Visibility Note |  | 1. Navigate to the Profile page<br>2. Enter special characters (e.g., !@#$%^&*) in the Visibility Note field | Field accepts the input without error | low |
| TC-019 (interaction_edge) |  | Rapid re-submission after sending a message |  | 1. Navigate to the Profile page<br>2. Click on the Message_Button<br>3. Immediately click the Message_Button again after the first submission | Second submission attempt is blocked; a message indicating 'Please wait before sending another message' is shown | medium |

---

## Profile Edit

Total: **13** (positive: 2, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update Profile with all required fields filled | User logged in as <Role> | 1. Click the 'Edit Profile' link to open the profile edit form<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid email> in the Email Address field<br>5. Click 'Update Profile' button | Profile page shows updated information with a success message. | high |
| TC-002 | WF-002 | Cancel profile edit | User logged in as <Role> | 1. Click the 'Edit Profile' link to open the profile edit form<br>2. Click 'Cancel' button | Exits without making changes and returns to the previous page. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Email Address field blank<br>4. Click Update Profile | Form does not submit; errors shown on First_Name, Last_Name, and Email_Address fields | high |
| TC-007 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email Address field<br>2. Fill all other required fields<br>3. Click Update Profile | Email_Address field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter valid minimum length for First Name |  | 1. Enter exactly 1 character in the First Name field<br>2. Enter valid values in Last Name and Email Address fields<br>3. Click Update Profile | Form submits successfully; entity is created with the First Name 'A' | medium |
| TC-009 (boundary) | WF-001 | Enter valid minimum length for Last Name |  | 1. Enter valid values in First Name and Email Address fields<br>2. Enter exactly 1 character in the Last Name field<br>3. Click Update Profile | Form submits successfully; entity is created with the Last Name 'B' | medium |
| TC-010 (boundary) | WF-001 | Enter valid email format in Email Address |  | 1. Enter valid values in First Name and Last Name fields<br>2. Enter 'a@b.com' in the Email Address field<br>3. Click Update Profile | Form submits successfully; entity is created with the Email Address 'a@b.com' | medium |
| TC-011 (data_edge) | WF-001 | Upload a file exactly at size limit for New Picture Upload |  | 1. Enter valid values in First Name, Last Name, and Email Address fields<br>2. Upload a file that is exactly at the size limit for New Picture Upload<br>3. Click Update Profile | Form submits successfully; new picture is uploaded with a visible success indicator | medium |
| TC-012 (data_edge) | WF-001 | Upload a file one byte over size limit for New Picture Upload |  | 1. Enter valid values in First Name, Last Name, and Email Address fields<br>2. Upload a file that is one byte over the size limit for New Picture Upload<br>3. Click Update Profile | Form is blocked; error shown stating 'File exceeds maximum size limit' | medium |
| TC-013 (interaction_edge) | WF-002 | Cancel profile edit after making changes |  | 1. Enter values in First Name, Last Name, and Email Address fields<br>2. Click Cancel | User is redirected to the previous page without saving changes | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click the Logout_Button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | user must not be authenticated | 1. Ensure the user is not logged in<br>2. Click on the Logout button | Logout action is not performed; user remains on the current page and is not redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Logout action when user is authenticated | User is logged in | 1. Click the Logout button | User is redirected to the login page; session is terminated. | medium |
| TC-004 (interaction_edge) |  | Attempt to log out when user is not authenticated | User is not logged in | 1. Click the Logout button | No action is taken; user remains on the current page. | medium |

---
