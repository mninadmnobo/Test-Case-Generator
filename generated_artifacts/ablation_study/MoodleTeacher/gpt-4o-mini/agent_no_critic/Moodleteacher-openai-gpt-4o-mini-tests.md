# Test Cases — Moodleteacher

Generated: 2026-06-09T11:50:42.516363Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 226 | 71 | 71 | 84 | 74 | 121 | 26 |

## Login

Total: **16** (positive: 4, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <Teacher> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | User is redirected to Dashboard | high |
| TC-002 | WF-002 | Failed login due to invalid credentials | User logged in as <Teacher> | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Inline error message 'Invalid or empty credentials' is displayed; Password field is cleared and Username field retains the entered value | high |
| TC-003 | WF-003 | Access as guest | User logged in as <Guest> | 1. Click Access as a guest | User is allowed unauthenticated browsing | medium |
| TC-004 | WF-004 | View cookies notice | User logged in as <Teacher> | 1. Click Cookies notice | Cookie usage information is displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-006 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-008 |  | Submit with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Form does not submit; error shown: 'Invalid or empty credentials'; Password field is cleared | high |
| TC-009 |  | Attempt to access the disabled Lost password link |  | 1. Attempt to click on the Lost password? link | No action occurs; the Lost password? link is disabled | medium |
| TC-010 |  | Attempt to access as guest without logging in |  | 1. Click Access as a guest | Unauthenticated browsing occurs; user remains on the login page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-002 | Submit with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message 'Invalid or empty credentials' is shown; Password field is cleared, Username field retains its empty state. | medium |
| TC-012 (boundary) | WF-002 | Submit with valid Username and empty Password |  | 1. Enter a valid Username in the Username field<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message 'Invalid or empty credentials' is shown; Password field is cleared, Username field retains the entered Username. | medium |
| TC-013 (boundary) | WF-002 | Submit with empty Username and valid Password |  | 1. Leave the Username field empty<br>2. Enter a valid Password in the Password field<br>3. Click Log in | Inline error message 'Invalid or empty credentials' is shown; Password field is cleared, Username field retains its empty state. | medium |
| TC-014 (input_edge) |  | Enter a very long Username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click Log in | Form submission behavior is observed; either the long Username is accepted or truncated with a visible indicator. | low |
| TC-015 (input_edge) |  | Enter special characters in Username |  | 1. Enter special characters in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click Log in | Form submission behavior is observed; either the special characters are accepted or an error is shown. | low |
| TC-016 (input_edge) |  | Enter leading/trailing whitespace in Username |  | 1. Enter leading and trailing spaces in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click Log in | Leading/trailing whitespace is trimmed; saved Username displayed on the detail page has no extra spaces. | low |

---

## Dashboard

Total: **15** (positive: 5, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar entry | User logged in as <Role> | 1. Click the 'New Event' button | creates calendar entry | high |
| TC-002 | WF-002 | Navigate to the previous month in the calendar | User logged in as <Role> | 1. Click the Left Arrow button | navigates to previous month | medium |
| TC-003 | WF-003 | Navigate to the next month in the calendar | User logged in as <Role> | 1. Click the Right Arrow button | navigates to next month | medium |
| TC-004 | WF-004 | Open the full calendar view | User logged in as <Role> | 1. Click the 'Full Calendar' link | opens dedicated calendar view | medium |
| TC-005 | WF-005 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or Export Calendars' link | opens calendar data management | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to create a new calendar entry without filling required fields |  | 1. Click on the 'New Event' button | Form does not submit; no calendar entry is created; error shown on required fields |  |
| TC-007 |  | Attempt to navigate to previous month without any events |  | 1. Click on the 'Left Arrow' button | Calendar remains on the current month; no navigation occurs |  |
| TC-008 |  | Attempt to navigate to next month without any events |  | 1. Click on the 'Right Arrow' button | Calendar remains on the current month; no navigation occurs |  |
| TC-009 |  | Attempt to open full calendar view without authentication |  | 1. Click on the 'Full Calendar' link | User is redirected to the login page |  |
| TC-010 |  | Attempt to open calendar data management without authentication |  | 1. Click on the 'Import or Export Calendars' link | User is redirected to the login page |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid submission of new calendar entry | User is on the Dashboard | 1. Click the 'New Event' button<br>2. Immediately click the 'New Event' button again | Only one calendar entry is created; no duplicate entries are shown | medium |
| TC-012 (interaction_edge) | WF-002 | Rapid navigation to previous month | User is on the Calendar block | 1. Click the 'Left Arrow' button<br>2. Immediately click the 'Left Arrow' button again | User navigates to the previous month only once; the calendar displays the correct month | medium |
| TC-013 (interaction_edge) | WF-003 | Rapid navigation to next month | User is on the Calendar block | 1. Click the 'Right Arrow' button<br>2. Immediately click the 'Right Arrow' button again | User navigates to the next month only once; the calendar displays the correct month | medium |
| TC-014 (input_edge) |  | Special characters in search field | User is on the Dashboard | 1. Enter special characters in the 'Search_Field' | The search field accepts special characters; no error is shown | low |
| TC-015 (input_edge) |  | Leading and trailing whitespace in search field | User is on the Dashboard | 1. Enter leading and trailing spaces in the 'Search_Field' | Leading/trailing whitespace is trimmed; saved value shown in the search results has no extra spaces | low |

---

## Dashboard — Edit Mode

Total: **18** (positive: 6, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset layout to default | User logged in as <Role>, Edit mode is enabled | 1. Click 'Reset page to default' | The layout resets to default | high |
| TC-002 | WF-002 | Open Add a block page | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block' | opens Add a block page | high |
| TC-003 | WF-003 | Cancel adding a block | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block'<br>2. Click 'Cancel' | returns to Dashboard without adding a block | medium |
| TC-004 | WF-004 | Configure existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the options menu of an existing block<br>2. Select 'Configure' | Configuration options for the block are displayed | medium |
| TC-005 | WF-005 | Move existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the move icon of an existing block<br>2. Drag the block to a new position | Block is moved to a new position | medium |
| TC-006 | WF-006 | Delete existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the options menu of an existing block<br>2. Select 'Delete' | Block is removed from the layout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Attempt to reset page layout without any changes |  | 1. Click 'Reset page to default' | Status remains unchanged; layout is not reset | high |
| TC-008 | WF-002 | Attempt to add a block without any selection |  | 1. Click '+ Add a block' | No block is added; remains on the current page | high |
| TC-009 | WF-003 | Click Cancel without adding a block |  | 1. Click 'Cancel' | Returns to Dashboard without adding a block | high |
| TC-010 | WF-004 | Attempt to configure a block that does not exist |  | 1. Click 'Configure' on a non-existent block | No configuration options are displayed; error shown | medium |
| TC-011 | WF-005 | Attempt to move a block that does not exist |  | 1. Click 'Move' on a non-existent block | Block is not moved; error shown | medium |
| TC-012 | WF-006 | Attempt to delete a block that does not exist |  | 1. Click 'Delete' on a non-existent block | Block is not removed; error shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapidly click Reset page to default twice | User is in Edit mode | 1. Click the 'Reset page to default' button<br>2. Immediately click the 'Reset page to default' button again | First reset action completes; layout resets to default without errors on second click | medium |
| TC-014 (interaction_edge) | WF-002 | Rapidly click + Add a block twice | User is in Edit mode | 1. Click the '+ Add a block' button<br>2. Immediately click the '+ Add a block' button again | First action opens Add a block page; second action does not create duplicate entries | medium |
| TC-015 (interaction_edge) | WF-003 | Click Cancel after adding a block | User is in Edit mode, User has opened Add a block page | 1. Click the 'Cancel' link | Returns to Dashboard without adding a block; no new block appears | medium |
| TC-016 (input_edge) |  | Add a block with special characters in name | User is in Edit mode | 1. Click the '+ Add a block' button<br>2. Enter special characters in the block name field | Block name is accepted or an error message is displayed indicating invalid characters | low |
| TC-017 (input_edge) |  | Add a block with leading/trailing whitespace | User is in Edit mode | 1. Click the '+ Add a block' button<br>2. Enter a block name with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved block name shows without extra spaces | low |
| TC-018 (data_edge) |  | Attempt to add more than maximum allowed blocks | User is in Edit mode | 1. Add maximum allowed blocks to the dashboard<br>2. Attempt to add one more block | Adding one more block is blocked; an error message indicates the limit has been reached | medium |

---

## My Courses

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Teacher>, At least one course is visible in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' from the menu | The course is pinned to the top | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Teacher>, At least one course is visible in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' from the menu | The course is hidden without affecting enrollment | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to star a course when it is already starred | The course is already starred | 1. Click on the 'Star this course' option for the already starred course | Status remains unchanged; the course remains starred; no visual indication of change occurs. | high |
| TC-004 |  | Attempt to remove a course from view when it is already hidden | The course is already hidden | 1. Click on the 'Remove from view' option for the already hidden course | Status remains unchanged; the course remains hidden; no visual indication of change occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapidly star the same course multiple times | User is on the My Courses page, At least one course is available to star | 1. Click the three-dot menu on a course card<br>2. Click 'Star this course'<br>3. Immediately click 'Star this course' again | The course remains starred; no duplicate action is performed. | medium |
| TC-006 (interaction_edge) | WF-002 | Rapidly remove the same course from view multiple times | User is on the My Courses page, At least one course is available to remove from view | 1. Click the three-dot menu on a course card<br>2. Click 'Remove from view'<br>3. Immediately click 'Remove from view' again | The course is hidden from view; no error occurs. | medium |
| TC-007 (input_edge) |  | Search with leading and trailing whitespace | User is on the My Courses page | 1. Enter '   Course Name   ' in the Search field<br>2. Press Enter | Leading and trailing whitespace is trimmed; the search results display correctly without extra spaces. | low |
| TC-008 (input_edge) |  | Search with special characters | User is on the My Courses page | 1. Enter '!@#$%^&*()' in the Search field<br>2. Press Enter | The system displays a message indicating no courses match the search criteria. | low |

---

## Course Page

Total: **15** (positive: 5, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Activity 1 | User logged in as <role> | 1. Click on 'Activity 1' in Section 1 | User accesses Activity 1 | high |
| TC-002 | WF-002 | Access Resource 1 | User logged in as <role> | 1. Click on 'Resource 1' in Section 1 | User accesses Resource 1 | high |
| TC-003 | WF-003 | Access Activity 2 | User logged in as <role> | 1. Click on 'Activity 2' in Section 2 | User accesses Activity 2 | high |
| TC-004 | WF-004 | Access Resource 2 | User logged in as <role> | 1. Click on 'Resource 2' in Section 2 | User accesses Resource 2 | high |
| TC-005 | WF-005 | Collapse All Sections | User logged in as <role> | 1. Click on 'Collapse All' link | All sections collapsed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Access Activity 1 without proper authentication | User is not logged in | 1. Navigate to the Course Page<br>2. Click on Activity 1 | User is redirected to the login page; Activity 1 is not accessed | high |
| TC-007 | WF-002 | Access Resource 1 without proper authentication | User is not logged in | 1. Navigate to the Course Page<br>2. Click on Resource 1 | User is redirected to the login page; Resource 1 is not accessed | high |
| TC-008 | WF-003 | Access Activity 2 without proper authentication | User is not logged in | 1. Navigate to the Course Page<br>2. Click on Activity 2 | User is redirected to the login page; Activity 2 is not accessed | high |
| TC-009 | WF-004 | Access Resource 2 without proper authentication | User is not logged in | 1. Navigate to the Course Page<br>2. Click on Resource 2 | User is redirected to the login page; Resource 2 is not accessed | high |
| TC-010 | WF-005 | Collapse all sections without proper authentication | User is not logged in | 1. Navigate to the Course Page<br>2. Click on Collapse All | User is redirected to the login page; all sections remain expanded | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-005 | Rapidly click Collapse All link twice | User is on the Course Page | 1. Click the Collapse All link<br>2. Immediately click the Collapse All link again | All sections remain collapsed; no error shown. | medium |
| TC-012 (interaction_edge) | WF-001 | Access Activity 1 after collapsing sections | User has collapsed all sections | 1. Click on Activity 1 link | User accesses Activity 1; the page displays Activity 1 content. | medium |
| TC-013 (interaction_edge) | WF-002 | Access Resource 1 after collapsing sections | User has collapsed all sections | 1. Click on Resource 1 link | User accesses Resource 1; the page displays Resource 1 content. | medium |
| TC-014 (interaction_edge) | WF-003 | Access Activity 2 after collapsing sections | User has collapsed all sections | 1. Click on Activity 2 link | User accesses Activity 2; the page displays Activity 2 content. | medium |
| TC-015 (interaction_edge) | WF-004 | Access Resource 2 after collapsing sections | User has collapsed all sections | 1. Click on Resource 2 link | User accesses Resource 2; the page displays Resource 2 content. | medium |

---

## Course Edit Mode and Activity Chooser

Total: **31** (positive: 15, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Enable Edit Mode | User logged in as <Role> | 1. Click the Edit_Mode button | turns the Course page into an authoring interface | high |
| TC-002 | WF-002 | Open Activity Chooser Modal | User logged in as <Role>, Edit mode is enabled | 1. Click the Add_Activity_Button | opens Activity Chooser modal | high |
| TC-003 | WF-003 | Add Subsection | User logged in as <Role>, Edit mode is enabled | 1. Click the Add_Subsection_Control | allows nesting content hierarchically | medium |
| TC-004 | WF-004 | Perform Batch Edit | User logged in as <Role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Edit from the Bulk_Actions_Toolbar | Batch edit action performed | medium |
| TC-005 | WF-005 | Perform Batch Duplicate | User logged in as <Role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Duplicate from the Bulk_Actions_Toolbar | Batch duplicate action performed | medium |
| TC-006 | WF-006 | Perform Batch Hide | User logged in as <Role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Hide from the Bulk_Actions_Toolbar | Batch hide action performed | medium |
| TC-007 | WF-007 | Perform Batch Delete | User logged in as <Role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Delete from the Bulk_Actions_Toolbar | Batch delete action performed | medium |
| TC-008 | WF-008 | Perform Batch Move | User logged in as <Role>, Edit mode is enabled | 1. Select multiple activities<br>2. Click Batch Move from the Bulk_Actions_Toolbar | Batch move action performed | medium |
| TC-009 | WF-009 | Quick Rename Activity | User logged in as <Role>, Edit mode is enabled | 1. Click the edit icon on an activity row | quick renaming | medium |
| TC-010 | WF-010 | Duplicate Activity | User logged in as <Role>, Edit mode is enabled | 1. Click the Section Menu on an activity row<br>2. Select duplicate | Activity duplicated | medium |
| TC-011 | WF-011 | Hide Activity | User logged in as <Role>, Edit mode is enabled | 1. Click the Activity Menu on an activity row<br>2. Select hide | Activity hidden | medium |
| TC-012 | WF-012 | Delete Activity | User logged in as <Role>, Edit mode is enabled | 1. Click the Activity Menu on an activity row<br>2. Select delete | Activity deleted | medium |
| TC-013 | WF-013 | Move Activity | User logged in as <Role>, Edit mode is enabled | 1. Click the Activity Menu on an activity row<br>2. Select move | Activity moved | medium |
| TC-014 | WF-014 | Set Access Restrictions | User logged in as <Role>, Edit mode is enabled | 1. Click the Activity Menu on an activity row<br>2. Select set access restrictions | Access restrictions set | medium |
| TC-015 | WF-015 | Add Activity from Activity Chooser | User logged in as <Role>, Edit mode is enabled, Activity Chooser modal is open | 1. Select a tile from the Activity_Resource_Tiles<br>2. Click the Add_Button | opens the activity's creation form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 | WF-001 | Attempt to enable Edit Mode without proper authorization | User is not logged in | 1. Click on the Edit_Mode button | User is redirected to the login page; Edit Mode is not enabled | high |
| TC-017 | WF-002 | Attempt to add an activity without enabling Edit Mode | Edit Mode is not enabled | 1. Click on the Add_Activity_Button | Activity Chooser modal does not open; no action occurs | high |
| TC-018 | WF-003 | Attempt to add a subsection without enabling Edit Mode | Edit Mode is not enabled | 1. Click on the Add_Subsection_Control | No subsection is added; action is blocked | high |
| TC-019 | WF-004 | Attempt to perform Batch Edit without selecting any activities | Activities are not selected | 1. Click on the Batch Edit action | Batch edit action is not performed; no activities are edited | medium |
| TC-020 | WF-010 | Attempt to duplicate an activity without selecting it | No activity is selected | 1. Click on the duplicate option in the Activity Menu | Activity is not duplicated; no action occurs | medium |
| TC-021 | WF-011 | Attempt to hide an activity without selecting it | No activity is selected | 1. Click on the hide option in the Activity Menu | Activity is not hidden; no action occurs | medium |
| TC-022 | WF-012 | Attempt to delete an activity without selecting it | No activity is selected | 1. Click on the delete option in the Activity Menu | Activity is not deleted; no action occurs | medium |
| TC-023 | WF-015 | Attempt to add an activity without selecting a tile in Activity Chooser | No tile is selected | 1. Click on the Add_Button | Activity creation form does not open; no action occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 (boundary) | WF-001 | Enable Edit Mode with valid user role | User is logged in with appropriate permissions | 1. Click on the Edit Mode button | Course page turns into an authoring interface | medium |
| TC-025 (boundary) | WF-002 | Add Activity or Resource with valid user role | User is in Edit Mode | 1. Click on the + Add an activity or resource button | Activity Chooser modal opens | medium |
| TC-026 (boundary) | WF-003 | Add Subsection with valid user role | User is in Edit Mode | 1. Click on the + Add a subsection control | Allows nesting content hierarchically | medium |
| TC-027 (boundary) | WF-015 | Add Activity from Activity Chooser with valid selection | User is in Activity Chooser modal | 1. Select a tile from the Activity Resource Tiles<br>2. Click on the Add button | Opens the activity's creation form | medium |
| TC-028 (interaction_edge) | WF-007 | Batch Delete action on multiple selected activities | User has selected multiple activities in Edit Mode | 1. Click on Batch Delete action | Batch delete action performed | medium |
| TC-029 (input_edge) |  | Search Field with long string input | User is in Activity Chooser modal | 1. Enter a very long string (200+ characters) in the Search Field | Search field accepts input without errors or truncation | low |
| TC-030 (input_edge) |  | Search Field with special characters | User is in Activity Chooser modal | 1. Enter special characters (e.g., !@#$%^&*) in the Search Field | Search field accepts input without errors | low |
| TC-031 (input_edge) |  | Search Field with leading/trailing whitespace | User is in Activity Chooser modal | 1. Enter leading and trailing whitespace in the Search Field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Assignment Creation

Total: **18** (positive: 4, negative: 9, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create assignment and redirect to course page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and return to course' | Assignment is created and redirects to the course page | high |
| TC-002 | WF-002 | Create assignment and display new assignment's page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and display' | Assignment is created and opens the new assignment's page | high |
| TC-003 | WF-003 | Discard changes and return to previous state | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Click 'Cancel' | All changes are discarded | medium |
| TC-004 |  | Enable file submissions and reveal additional controls | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Check the File Submissions checkbox | Additional controls for maximum number of uploaded files, maximum submission size, and accepted file types are revealed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Assignment Name field blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other fields as desired<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-006 | WF-002 | Leave the Assignment Name field blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other fields as desired<br>3. Click 'Save and display' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-007 |  | Attempt to save with invalid date in Allow Submissions From |  | 1. Enable the Allow_Submissions_From toggle<br>2. Enter <invalid date format> in the Allow_Submissions_From field<br>3. Click 'Save and return to course' | Inline validation error appears on the Allow_Submissions_From field indicating it must be a valid date | medium |
| TC-008 |  | Attempt to save with invalid date in Due Date |  | 1. Enable the Due_Date toggle<br>2. Enter <invalid date format> in the Due_Date field<br>3. Click 'Save and return to course' | Inline validation error appears on the Due_Date field indicating it must be a valid date | medium |
| TC-009 |  | Attempt to save with invalid date in Cut Off Date |  | 1. Enable the Cut_Off_Date toggle<br>2. Enter <invalid date format> in the Cut_Off_Date field<br>3. Click 'Save and return to course' | Inline validation error appears on the Cut_Off_Date field indicating it must be a valid date | medium |
| TC-010 |  | Attempt to save with a negative number in Max Uploaded Files |  | 1. Enable the File_Submissions checkbox<br>2. Enter <negative number> in the Max_Uploaded_Files field<br>3. Click 'Save and return to course' | Inline validation error appears on the Max_Uploaded_Files field indicating it must be a positive number | medium |
| TC-011 |  | Attempt to save with an excessively large number in Max Submission Size |  | 1. Enable the File_Submissions checkbox<br>2. Enter <amount exceeding maximum allowed> in the Max_Submission_Size field<br>3. Click 'Save and return to course' | Inline validation error appears on the Max_Submission_Size field indicating it exceeds the maximum allowed size | medium |
| TC-012 |  | Attempt to save with a duplicate tag |  | 1. Enter <duplicate tag> in the Tags field<br>2. Click 'Save and return to course' | Inline validation error appears on the Tags field indicating it must be unique | medium |
| TC-013 |  | Attempt to add a restriction without selecting a type |  | 1. Click on '+ Add restriction'<br>2. Click 'Save and return to course' | Inline validation error appears indicating a restriction type must be selected | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Enter exactly one character in the Assignment Name field |  | 1. Enter 1 character in the Assignment Name field<br>2. Fill all other required fields<br>3. Click 'Save and return to course' | Form submits successfully; entity is created with the Assignment Name | medium |
| TC-015 (boundary) | WF-001 | Enter exactly 200 characters in the Description field |  | 1. Enter a 200 character string in the Description field<br>2. Fill all other required fields<br>3. Click 'Save and return to course' | Form submits successfully; entity is created with the Description | medium |
| TC-016 (boundary) | WF-001 | Upload a file at the maximum file size limit |  | 1. Click on the Additional Files upload area<br>2. Upload a file that is exactly at the maximum submission size limit<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | File uploads successfully; entity is created with the uploaded file | medium |
| TC-017 (boundary) | WF-001 | Attempt to upload a file that exceeds the maximum file size limit |  | 1. Click on the Additional Files upload area<br>2. Upload a file that is one byte over the maximum submission size limit<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | Form submission is blocked; inline error shown indicating the file exceeds the maximum size limit | medium |
| TC-018 (interaction_edge) | WF-002 | Rapidly click Save and display after a successful submission |  | 1. Fill in the form with valid data<br>2. Click 'Save and display'<br>3. Immediately click 'Save and display' again | Second submission attempt is blocked; user is redirected to the new assignment's page without creating a duplicate entity | low |

---

## Course Settings

Total: **13** (positive: 2, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Course Settings with all required fields | User logged in as <Role> | 1. Open the Course Settings form<br>2. Enter <valid course full name> in the Course Full Name field<br>3. Enter <valid course short name> in the Course Short Name field<br>4. Select <valid course category> from the Course Category dropdown<br>5. Select 'Show' from the Course Visibility dropdown<br>6. Click 'Save and display' | persists the configuration and returns to the course page | high |
| TC-002 | WF-002 | Cancel Course Settings changes | User logged in as <Role> | 1. Open the Course Settings form<br>2. Enter <valid course full name> in the Course Full Name field<br>3. Enter <valid course short name> in the Course Short Name field<br>4. Select <valid course category> from the Course Category dropdown<br>5. Click 'Cancel' | leaves existing settings unchanged | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Course Full Name field blank |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-004 | WF-001 | Leave the Course Short Name field blank |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Course Category field unselected |  | 1. Leave the Course Category field unselected<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-006 | WF-001 | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Save and display | Inline validation errors appear on the Course Full Name, Course Short Name, and Course Category fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Enter maximum length string in Course Full Name |  | 1. Enter a string with maximum allowed length in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the maximum length string in the Course Full Name | medium |
| TC-008 (boundary) | WF-001 | Enter one character less than required in Course Short Name |  | 1. Enter a string with one character less than the required minimum in the Course Short Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submission is blocked; error shown indicating the Course Short Name is too short | medium |
| TC-009 (input_edge) |  | Enter a very long string in Course Summary |  | 1. Enter a string longer than 200 characters in the Course Summary field<br>2. Click Save and display | Form submits successfully; Course Summary is truncated to the maximum allowed length | low |
| TC-010 (input_edge) |  | Enter special characters in Course Full Name |  | 1. Enter a string with special characters in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; special characters are accepted in the Course Full Name | low |
| TC-011 (state_edge) |  | Toggle Course End Date visibility and enter a date |  | 1. Enable the toggle for Course End Date<br>2. Enter today's date in the Course End Date field<br>3. Click Save and display | Form submits successfully; Course End Date is saved with today's date | medium |
| TC-012 (data_edge) |  | Upload a file exactly at maximum upload size |  | 1. Upload a file that is exactly at the maximum upload size limit<br>2. Click Save and display | File upload is accepted; visible success indicator shown | medium |
| TC-013 (data_edge) |  | Upload a file exceeding maximum upload size |  | 1. Upload a file that exceeds the maximum upload size limit<br>2. Click Save and display | Form submission is blocked; error shown indicating the file exceeds the maximum upload size | medium |

---

## Participants Management

Total: **22** (positive: 10, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open enrollment dialog | User logged in as <role> | 1. Click the Enrol Users button | opens enrollment dialog | high |
| TC-002 | WF-002 | Apply filters | User logged in as <role> | 1. Fill in the filter conditions<br>2. Click the Apply Filters button | applies the filters | high |
| TC-003 | WF-003 | Clear filters | User logged in as <role>, Filters are applied | 1. Click the Clear Filters button | clears all filters | medium |
| TC-004 | WF-004 | Filter by first name | User logged in as <role> | 1. Click the First Name alphabetical filter button | filters the list by first name | medium |
| TC-005 | WF-005 | Filter by last name | User logged in as <role> | 1. Click the Last Name alphabetical filter button | filters the list by last name | medium |
| TC-006 | WF-006 | View profile of participant | User logged in as <role>, Participants are listed | 1. Click the View Profile action for a participant | views participant profile | medium |
| TC-007 | WF-007 | Edit role of participant | User logged in as <role>, Participants are listed | 1. Click the Edit Role action for a participant | edits participant role | medium |
| TC-008 | WF-008 | Send message to participant | User logged in as <role>, Participants are listed | 1. Click the Send Message action for a participant | sends message to participant | medium |
| TC-009 | WF-009 | Bulk action with selected users | User logged in as <role>, Select multiple participants | 1. Select users from the participants table<br>2. Choose an action from the With Selected Users dropdown | applies bulk actions to checked participants | medium |
| TC-010 | WF-010 | Confirm enrollment of user | User logged in as <role>, Enrollment dialog is open | 1. Enter a valid user in the User Search Field<br>2. Select a role from the Role dropdown<br>3. Click the Confirm Enrollment button | adds user to the course at specified role | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-010 | Leave the User Search Field blank and submit |  | 1. Open the enrollment dialog<br>2. Leave the User Search Field blank<br>3. Click Confirm Enrollment Button | Form does not submit; User Search Field displays an error: 'This field is required.' | high |
| TC-012 | WF-002 | Attempt to apply filters with no conditions set |  | 1. Click Apply Filters Button | Form does not submit; no filters are applied; error shown indicating that at least one condition must be set. | high |
| TC-013 | WF-009 | Attempt bulk action with no users selected |  | 1. Click With Selected Users dropdown<br>2. Select an action from the dropdown<br>3. Click the action button | Action does not execute; error shown indicating that no users are selected for the action. | high |
| TC-014 | WF-001 | Attempt to open enrollment dialog without required user input |  | 1. Click Enrol Users Button | Enrollment dialog opens; User Search Field is empty. | medium |
| TC-015 | WF-004 | Attempt to filter by first name without entering a name |  | 1. Click filter by first name<br>2. Leave the first name input blank<br>3. Click Apply Filters Button | Form does not submit; First Name filter displays an error: 'This field is required.' | medium |
| TC-016 | WF-005 | Attempt to filter by last name without entering a name |  | 1. Click filter by last name<br>2. Leave the last name input blank<br>3. Click Apply Filters Button | Form does not submit; Last Name filter displays an error: 'This field is required.' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-002 | Apply filters with no conditions | Filters are empty | 1. Click Apply Filters Button | Filters are applied successfully, and the participant list remains unchanged | medium |
| TC-018 (boundary) | WF-003 | Clear filters when none are set | No filters are currently set | 1. Click Clear Filters Button | All filters are cleared successfully; no visible change occurs | medium |
| TC-019 (boundary) | WF-010 | Confirm enrollment with empty search field | Enrollment dialog is open | 1. Leave User Search Field empty<br>2. Click Confirm Enrollment Button | Enrollment is blocked; an error message indicates that the search field cannot be empty | medium |
| TC-020 (input_edge) |  | Search field with special characters | Enrollment dialog is open | 1. Enter special characters in User Search Field<br>2. Click Confirm Enrollment Button | Error message displayed indicating invalid input in search field | low |
| TC-021 (input_edge) |  | Search field with leading/trailing whitespace | Enrollment dialog is open | 1. Enter '   John Doe   ' in User Search Field<br>2. Click Confirm Enrollment Button | Leading/trailing whitespace is trimmed; user is searched successfully | low |
| TC-022 (interaction_edge) | WF-001 | Rapid re-submission of enrollment dialog | Enrollment dialog is open and user has been added | 1. Press the browser back button<br>2. Click Enrol Users Button again | Enrollment dialog opens blank; no duplicate entries are created | medium |

---

## Assignment — Teacher View

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open grading interface for individual students | User logged in as <Teacher> | 1. Navigate to the Assignment tab<br>2. Click the Grade button | opens grading interface for individual students | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to open grading interface without any submissions |  | 1. Navigate to the Assignment page<br>2. Click on the Grade button | The grading interface does not open; a message indicates 'No submissions available for grading.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapidly click the Grade button multiple times | User is on the Assignment page | 1. Click the Grade button<br>2. Immediately click the Grade button again | Grading interface opens successfully; no duplicate interfaces are created. | medium |
| TC-004 (input_edge) |  | Navigate to each tab in quick succession | User is on the Assignment page | 1. Click on the Settings tab<br>2. Click on the Submissions tab<br>3. Click on the Advanced Grading tab<br>4. Click on the More tab<br>5. Click back to the Assignment tab | User can navigate between tabs without any errors; all tabs display correctly. | low |

---

## Assignment Submissions

Total: **6** (positive: 1, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Grading Workflow for a submission | User logged in as <Teacher>, At least one submission exists in the table | 1. Locate the submission for <Student Name> in the Submissions Table<br>2. Click on the action menu for the submission<br>3. Select 'Open Grading Workflow' from the menu | Grading workflow opened for the selected submission | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to open grading workflow without selecting a submission |  | 1. Navigate to the Submissions view<br>2. Click on 'Open Grading Workflow' without selecting any submission | No grading workflow opens; an error message is displayed indicating that a submission must be selected first. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (input_edge) |  | Enter a very long student name in the search field |  | 1. Enter a string of 200+ characters in the Search field<br>2. Click the Search button | Search results display correctly or show a truncation message | low |
| TC-004 (input_edge) |  | Enter special characters in the student name filter |  | 1. Enter special characters (e.g., @#$%^&*) in the Filter_Student_Name field<br>2. Click the Search button | Search results display correctly or show a specific error message for invalid input | low |
| TC-005 (input_edge) |  | Enter a value with leading/trailing whitespace in the student name filter |  | 1. Enter '   John Doe   ' in the Filter_Student_Name field<br>2. Click the Search button | Leading/trailing whitespace is trimmed; search results display for 'John Doe' | low |
| TC-006 (interaction_edge) | WF-001 | Rapidly open the grading workflow for a submission | At least one submission is displayed in the table | 1. Click the 'Open Grading Workflow' action for a submission<br>2. Immediately click the 'Open Grading Workflow' action again for the same submission | Grading workflow opens successfully without errors or duplicate actions | medium |

---

## Gradebook — Grader Report

Total: **11** (positive: 3, negative: 2, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit Grade Settings for a specific activity | User logged in as <Role>, Edit mode is enabled | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Click the three-dot menu on the header of the specific activity column<br>3. Select 'Edit Grade Settings' from the dropdown<br>4. Make necessary changes in the grade settings<br>5. Click 'Save changes' | Grade settings updated | high |
| TC-002 | WF-002 | Edit Grade Entry for a specific student and activity | User logged in as <Role>, Edit mode is enabled | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Click the three-dot menu on the cell corresponding to the specific student and activity<br>3. Select 'Edit Grade Entry' from the dropdown<br>4. Enter a new grade value within the configured grade range<br>5. Click 'Save changes' | Grade entry updated | high |
| TC-003 | WF-003 | Save changes after editing grades | User logged in as <Role>, Edit mode is enabled | 1. Select 'Grader report' from the Report Type Selector dropdown<br>2. Click on a cell to edit a grade entry<br>3. Enter a new grade value within the configured grade range<br>4. Click 'Save changes' | applies edits | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Attempt to save changes with grades outside the configured grade range | Edit mode is enabled | 1. Enable Edit mode<br>2. Enter <value outside configured grade range> in a grade cell<br>3. Click 'Save changes' | Inline validation error appears on the grade cell indicating 'Values must be within configured grade range'; form does not submit; changes are not saved. | high |
| TC-005 |  | Attempt to save changes without entering any grades | Edit mode is enabled | 1. Enable Edit mode<br>2. Leave all grade cells blank<br>3. Click 'Save changes' | Inline validation error appears on the grade cells indicating 'Values must be within configured grade range'; form does not submit; changes are not saved. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-003 | Save grade entry at minimum configured grade value | Edit mode is enabled, Configured grade range includes a minimum value | 1. Enter the minimum configured grade value in the grade cell<br>2. Click 'Save changes' | Grade entry is updated successfully; inline confirmation message displayed | medium |
| TC-007 (boundary) | WF-003 | Attempt to save grade entry below minimum configured grade value | Edit mode is enabled, Configured grade range includes a minimum value | 1. Enter a value below the minimum configured grade value in the grade cell<br>2. Click 'Save changes' | Saving is blocked; inline error message indicates the value is below the minimum allowed | medium |
| TC-008 (boundary) | WF-003 | Save grade entry at maximum configured grade value | Edit mode is enabled, Configured grade range includes a maximum value | 1. Enter the maximum configured grade value in the grade cell<br>2. Click 'Save changes' | Grade entry is updated successfully; inline confirmation message displayed | medium |
| TC-009 (boundary) | WF-003 | Attempt to save grade entry above maximum configured grade value | Edit mode is enabled, Configured grade range includes a maximum value | 1. Enter a value above the maximum configured grade value in the grade cell<br>2. Click 'Save changes' | Saving is blocked; inline error message indicates the value is above the maximum allowed | medium |
| TC-010 (input_edge) |  | Enter a very long string in the User Search field |  | 1. Enter a string longer than 200 characters in the User Search field<br>2. Press Enter | Input is either accepted or truncated with a visible indicator | low |
| TC-011 (input_edge) |  | Enter special characters in the User Search field |  | 1. Enter special characters (e.g., @, #, $, %) in the User Search field<br>2. Press Enter | Input is accepted or a specific error message is displayed | low |

---

## Profile

Total: **30** (positive: 10, negative: 10, edge: 10)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit Profile | User logged in as <Teacher> | 1. Click the 'Edit Profile' link in the User Details Card | Profile edited successfully | high |
| TC-002 | WF-002 | View Data Retention Summary | User logged in as <Teacher> | 1. Click the 'Data Retention Summary' link in the Privacy and Policies Card | Data retention summary displayed | medium |
| TC-003 | WF-003 | View Associated Course Profiles | User logged in as <Teacher> | 1. Click the 'Associated Course Profiles' link in the Course Details Card | Associated course profiles displayed | medium |
| TC-004 | WF-004 | View Blog Entries | User logged in as <Teacher> | 1. Click the 'Blog Entries' link in the Miscellaneous Card | Blog entries displayed | medium |
| TC-005 | WF-005 | View Forum Posts | User logged in as <Teacher> | 1. Click the 'Forum Posts' link in the Miscellaneous Card | Forum posts displayed | medium |
| TC-006 | WF-006 | View Forum Discussions | User logged in as <Teacher> | 1. Click the 'Forum Discussions' link in the Miscellaneous Card | Forum discussions displayed | medium |
| TC-007 | WF-007 | View Learning Plans | User logged in as <Teacher> | 1. Click the 'Learning Plans' link in the Miscellaneous Card | Learning plans displayed | medium |
| TC-008 | WF-008 | View Browser Sessions | User logged in as <Teacher> | 1. Click the 'Browser Sessions' link in the Reports Card | Browser sessions displayed | medium |
| TC-009 | WF-009 | View Grades Overview | User logged in as <Teacher> | 1. Click the 'Grades Overview' link in the Reports Card | Grades overview displayed | medium |
| TC-010 | WF-010 | Send Message | User logged in as <Teacher> | 1. Click the 'Message' button<br>2. Enter <message content> in the message field<br>3. Click 'Send' | Message sent successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Attempt to edit profile without any changes |  | 1. Click on the 'Edit Profile' link<br>2. Leave all fields unchanged<br>3. Click Save | Form does not submit; no changes made to the profile; error shown indicating that no changes were detected. | high |
| TC-012 | WF-002 | Attempt to view data retention summary without permission |  | 1. Click on the 'Data Retention Summary Link' | User is blocked from viewing the data retention summary; access denied message is displayed. | high |
| TC-013 | WF-003 | Attempt to view associated course profiles without permission |  | 1. Click on the 'Associated Course Profiles Links' | User is blocked from viewing associated course profiles; access denied message is displayed. | high |
| TC-014 | WF-004 | Attempt to view blog entries without permission |  | 1. Click on the 'Blog Entries Links' | User is blocked from viewing blog entries; access denied message is displayed. | high |
| TC-015 | WF-005 | Attempt to view forum posts without permission |  | 1. Click on the 'Forum Posts Links' | User is blocked from viewing forum posts; access denied message is displayed. | high |
| TC-016 | WF-006 | Attempt to view forum discussions without permission |  | 1. Click on the 'Forum Discussions Links' | User is blocked from viewing forum discussions; access denied message is displayed. | high |
| TC-017 | WF-007 | Attempt to view learning plans without permission |  | 1. Click on the 'Learning Plans Links' | User is blocked from viewing learning plans; access denied message is displayed. | high |
| TC-018 | WF-008 | Attempt to view browser sessions without permission |  | 1. Click on the 'Browser Sessions Link' | User is blocked from viewing browser sessions; access denied message is displayed. | high |
| TC-019 | WF-009 | Attempt to view grades overview without permission |  | 1. Click on the 'Grades Overview Link' | User is blocked from viewing grades overview; access denied message is displayed. | high |
| TC-020 | WF-010 | Attempt to send a message without being logged in |  | 1. Click on the 'Message' button | User is redirected to the login page; message sending is blocked. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Edit profile with valid data | User is logged in, User has valid profile data | 1. Click on the 'Edit Profile' link<br>2. Modify the profile fields as needed<br>3. Click 'Save' | Profile edited successfully; updated profile data is displayed | medium |
| TC-022 (boundary) | WF-002 | View data retention summary | User is logged in | 1. Click on the 'Data Retention Summary Link' | Data retention summary displayed | medium |
| TC-023 (boundary) | WF-003 | View associated course profiles | User is logged in | 1. Click on the 'Associated Course Profiles Links' | Associated course profiles displayed | medium |
| TC-024 (boundary) | WF-004 | View blog entries | User is logged in | 1. Click on the 'Blog Entries Links' | Blog entries displayed | medium |
| TC-025 (boundary) | WF-005 | View forum posts | User is logged in | 1. Click on the 'Forum Posts Links' | Forum posts displayed | medium |
| TC-026 (boundary) | WF-006 | View forum discussions | User is logged in | 1. Click on the 'Forum Discussions Links' | Forum discussions displayed | medium |
| TC-027 (boundary) | WF-007 | View learning plans | User is logged in | 1. Click on the 'Learning Plans Links' | Learning plans displayed | medium |
| TC-028 (boundary) | WF-008 | View browser sessions | User is logged in | 1. Click on the 'Browser Sessions Link' | Browser sessions displayed | medium |
| TC-029 (boundary) | WF-009 | View grades overview | User is logged in | 1. Click on the 'Grades Overview Link' | Grades overview displayed | medium |
| TC-030 (boundary) | WF-010 | Send message | User is logged in | 1. Click on the 'Message' button<br>2. Enter message content<br>3. Click 'Send' | Message sent successfully | medium |

---

## Profile Edit

Total: **15** (positive: 2, negative: 5, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update Profile with all required fields filled | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid email> in the Email Address field<br>4. Click 'Update Profile' | The profile page refreshes to show the updated information. | high |
| TC-002 | WF-002 | Cancel profile edit | User logged in as <Role> | 1. Click 'Cancel' | Exits without making changes. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First Name, Last Name, and Email Address fields blank<br>2. Click Update Profile | Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required | high |
| TC-007 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email Address field<br>2. Fill all other required fields<br>3. Click Update Profile | Email_Address field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | First Name field at minimum character length | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | Form submits successfully; profile is updated with the first name containing 1 character | medium |
| TC-009 (boundary) | WF-001 | First Name field below minimum character length | User is on the Edit Profile page | 1. Enter 0 characters in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | First Name field displays an error indicating the value is below the minimum allowed | medium |
| TC-010 (boundary) | WF-001 | Last Name field at minimum character length | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | Form submits successfully; profile is updated with the last name containing 1 character | medium |
| TC-011 (boundary) | WF-001 | Last Name field below minimum character length | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 0 characters in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | Last Name field displays an error indicating the value is below the minimum allowed | medium |
| TC-012 (data_edge) | WF-001 | Email field with valid format | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | Form submits successfully; profile is updated with the valid email address | medium |
| TC-013 (data_edge) | WF-001 | Email field with invalid format | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter an invalid email format in the Email Address field<br>4. Click Update Profile | Email Address field displays an error indicating the email format is invalid | medium |
| TC-014 (input_edge) |  | Long text in Description field | User is on the Edit Profile page | 1. Enter 1 character in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Enter a long text string (200+ characters) in the Description field<br>5. Click Update Profile | Form submits successfully; profile is updated with the long description | low |
| TC-015 (input_edge) |  | Special characters in First Name field | User is on the Edit Profile page | 1. Enter special characters in the First Name field<br>2. Enter 1 character in the Last Name field<br>3. Enter a valid email address in the Email Address field<br>4. Click Update Profile | First Name field displays an error indicating special characters are not allowed | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click on the Logout button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | user must be authenticated | 1. Ensure the user is not authenticated<br>2. Click the Logout button | Logout action is not performed; user remains on the current page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid logout attempts | User is authenticated | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is blocked; user remains on the login page without any session termination. | medium |
| TC-004 (input_edge) |  | Logout without authentication | User is not authenticated | 1. Attempt to click the Logout button | Logout action is not performed; user remains on the current page with no session termination. | low |

---
