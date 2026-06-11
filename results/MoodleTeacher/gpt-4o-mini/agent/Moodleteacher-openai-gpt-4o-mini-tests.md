# Test Cases — Moodleteacher

Generated: 2026-06-09T11:47:58.699575Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 200 | 68 | 61 | 71 | 71 | 90 | 31 |

## Login

Total: **15** (positive: 4, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log in with valid credentials | User logged in as <Teacher>, User is on the Login page | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |
| TC-002 | WF-002 | Log in with invalid credentials | User logged in as <Teacher>, User is on the Login page | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | shows inline error message | high |
| TC-003 | WF-003 | Access as a guest | User is on the Login page | 1. Click Access as a guest | grants unauthenticated browsing | medium |
| TC-004 | WF-004 | View cookies notice | User is on the Login page | 1. Click Cookies notice | displays cookie usage information | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-006 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-008 |  | Enter invalid format in the Password field |  | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password format> in the Password field<br>3. Click Log in | Inline error message is shown; Password field is cleared and retains Username for correction | medium |
| TC-009 |  | Attempt to access the Lost password? link |  | 1. Click on the Lost password? link | No action occurs; the link is disabled | medium |
| TC-010 |  | Attempt to log in with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Inline error message is shown; Password field is cleared and retains Username for correction | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message is shown indicating the username is too long or the form submits successfully with the username truncated. | low |
| TC-012 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter a username with special characters (e.g., !@#$%^&*) in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message is shown indicating invalid characters in the username or the form submits successfully. | low |
| TC-013 (input_edge) |  | Enter leading/trailing whitespace in the Username field |  | 1. Enter a username with leading and trailing spaces in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces. | low |
| TC-014 (input_edge) |  | Enter a zero-length password |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message is shown indicating that the password is required. | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully logged in | 1. Click Log in with valid credentials<br>2. Immediately press the browser back button | User is redirected to the Dashboard without a second entity being created. | medium |

---

## Dashboard

Total: **18** (positive: 7, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar entry | User logged in as <Role> | 1. Click the 'New Event' button in the Calendar block | A success notification is displayed; the calendar entry is created. | high |
| TC-002 | WF-002 | Navigate to the previous month in the calendar | User logged in as <Role> | 1. Click the 'Previous Month' button in the Calendar block | Calendar view updated to previous month | medium |
| TC-003 | WF-003 | Navigate to the next month in the calendar | User logged in as <Role> | 1. Click the 'Next Month' button in the Calendar block | Calendar view updated to next month | medium |
| TC-004 | WF-004 | Open the full calendar view | User logged in as <Role> | 1. Click the 'Full calendar' link | opens dedicated calendar view | medium |
| TC-005 | WF-005 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or export calendars' link | opens calendar data management | medium |
| TC-006 | WF-006 | Sort activities in the Timeline block | User logged in as <Role> | 1. Select an option from the Sort Order dropdown in the Timeline block | Activities sorted based on selected order | medium |
| TC-007 | WF-007 | Search activities in the Timeline block | User logged in as <Role> | 1. Enter <search term> in the Search Activities field in the Timeline block | Activities filtered based on search criteria | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the Time Range dropdown unselected and submit |  | 1. Leave the Time Range dropdown blank<br>2. Click on the Search button | Form does not submit; Time Range field is highlighted with an error indicating it is required | high |
| TC-009 |  | Attempt to create a new calendar entry without filling required fields |  | 1. Click on the New Event button | Form does not submit; required fields for creating a calendar entry are not specified, and an error is shown | high |
| TC-010 |  | Click on Previous Month button when already on the first month |  | 1. Click on the Previous Month button | No action occurs; Calendar view remains unchanged | medium |
| TC-011 |  | Click on Full calendar link without authentication |  | 1. Click on the Full calendar link | User is redirected to the login page | high |
| TC-012 |  | Click on Import or export calendars link without authentication |  | 1. Click on the Import or export calendars link | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapid submission of new calendar entry | User is on the Dashboard | 1. Click on the 'New Event' button to create a calendar entry<br>2. Immediately click on the 'New Event' button again | Second submission attempt is blocked; only one calendar entry is created. | medium |
| TC-014 (state_edge) | WF-002 | Navigate to previous month rapidly | User is on the Calendar block | 1. Click on the 'Previous Month' button<br>2. Immediately click on the 'Previous Month' button again | The action succeeds; the calendar view updates to the previous month without error. | medium |
| TC-015 (state_edge) | WF-003 | Navigate to next month rapidly | User is on the Calendar block | 1. Click on the 'Next Month' button<br>2. Immediately click on the 'Next Month' button again | The action succeeds; the calendar view updates to the next month without error. | medium |
| TC-016 (input_edge) |  | Search with special characters | User is on the Timeline block | 1. Enter special characters (e.g., '!@#$%^&*()') in the 'Search Activities' field<br>2. Click on the search button | The system displays an error indicating that the search criteria are invalid. | low |
| TC-017 (input_edge) |  | Search with leading and trailing whitespace | User is on the Timeline block | 1. Enter '   Activity Name   ' in the 'Search Activities' field<br>2. Click on the search button | Leading/trailing whitespace is trimmed; the search result shows 'Activity Name'. | low |
| TC-018 (input_edge) |  | Enter long text in search field | User is on the Timeline block | 1. Enter a very long string (200+ characters) in the 'Search Activities' field<br>2. Click on the search button | The system displays an error indicating that the input exceeds the maximum allowed length. | low |

---

## Dashboard — Edit Mode

Total: **15** (positive: 5, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Add a block page | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block' | opens Add a block page | high |
| TC-002 | WF-002 | Reset layout to default | User logged in as <Role>, Edit mode is enabled | 1. Click 'Reset page to default' | reverts layout changes | high |
| TC-003 | WF-003 | Configure existing block | User logged in as <Role>, Edit mode is enabled, At least one block exists | 1. Click 'Options' on the existing block<br>2. Select 'Configure' | Configuration options displayed for the block | medium |
| TC-004 | WF-004 | Move existing block | User logged in as <Role>, Edit mode is enabled, At least one block exists | 1. Click 'Move' on the existing block | Block moved to new position | medium |
| TC-005 | WF-005 | Delete existing block | User logged in as <Role>, Edit mode is enabled, At least one block exists | 1. Click 'Options' on the existing block<br>2. Select 'Delete' | Block removed from the dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to add a block without selecting a block type |  | 1. Click on '+ Add a block'<br>2. Leave the Available Block Types dropdown empty<br>3. Click Submit | Inline validation error appears on the Available Block Types field indicating it is required | high |
| TC-007 |  | Attempt to reset page to default when no changes have been made |  | 1. Click on 'Reset page to default' | Status remains unchanged; no layout changes are reverted | medium |
| TC-008 |  | Attempt to delete a block without confirmation |  | 1. Click on the Options Menu of an existing block<br>2. Click on 'Delete' | No block is removed from the dashboard; confirmation prompt is displayed | medium |
| TC-009 |  | Attempt to move a block without selecting a new position |  | 1. Click on the Move Icon of an existing block<br>2. Leave the new position unselected<br>3. Click Submit | Inline validation error appears indicating a new position must be selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Add maximum number of blocks | User is in Edit mode, Existing blocks are at maximum capacity | 1. Click '+ Add a block' button | Attempt to add a block is blocked; visible error indicates maximum number of blocks reached | medium |
| TC-011 (boundary) | WF-002 | Reset page with unsaved changes | User is in Edit mode, Layout changes have been made | 1. Click 'Reset page to default' button | Layout changes are reverted to default; all previous changes are lost | medium |
| TC-012 (interaction_edge) | WF-003 | Rapidly configure existing block | User is in Edit mode, At least one block exists | 1. Click 'Options' menu for a block<br>2. Click 'Configure'<br>3. Immediately click 'Configure' again | Second configuration attempt is blocked; only the first configuration options are displayed | low |
| TC-013 (interaction_edge) | WF-004 | Rapidly move existing block | User is in Edit mode, At least one block exists | 1. Click 'Move' icon for a block<br>2. Immediately click 'Move' again | Second move attempt is blocked; only the first move action is processed | low |
| TC-014 (interaction_edge) | WF-005 | Delete existing block and attempt to delete again | User is in Edit mode, At least one block exists | 1. Click 'Options' menu for a block<br>2. Click 'Delete'<br>3. Immediately click 'Delete' again | Second delete attempt is blocked; only the first block is removed from the dashboard | low |
| TC-015 (input_edge) |  | Enter long text in block type field | User is in Edit mode | 1. Click '+ Add a block' button<br>2. Enter a very long string (200+ characters) in the block type field | Input is either accepted or truncated with a visible indicator | low |

---

## My Courses

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Teacher>, At least one course is visible in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' from the menu | The course is pinned to the top | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Teacher>, At least one course is visible in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' from the menu | The course is hidden without affecting enrollment | high |
| TC-003 | WF-003 | Navigate to course main page | User logged in as <Teacher>, At least one course is visible in the course grid | 1. Click on the course name link on a course card | Navigates to course's main page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to star a course without selecting it |  | 1. Do not select any course<br>2. Click 'Star this course' | No course is starred; error message is displayed indicating that a course must be selected first | high |
| TC-005 |  | Attempt to remove a course from view without selecting it |  | 1. Do not select any course<br>2. Click 'Remove from view' | No course is removed from view; error message is displayed indicating that a course must be selected first | high |
| TC-006 |  | Attempt to search with an empty search field |  | 1. Leave the Search field blank<br>2. Click the search button | No courses are filtered; all courses remain visible | medium |
| TC-007 |  | Attempt to sort without selecting a sort option |  | 1. Leave the Sort dropdown unselected<br>2. Click the sort button | No sorting occurs; courses remain in their original order | medium |
| TC-008 |  | Attempt to change layout without selecting a layout option |  | 1. Leave the Layout dropdown unselected<br>2. Click the layout change button | No layout change occurs; courses remain in their original layout | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (interaction_edge) | WF-001 | Rapidly star the same course multiple times | User is on the My Courses page with at least one course displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Star this course'<br>3. Immediately click 'Star this course' again | The course is pinned to the top; no error is shown for the second action. | medium |
| TC-010 (interaction_edge) | WF-002 | Remove a course from view and attempt to remove it again | User is on the My Courses page with at least one course displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Remove from view'<br>3. Immediately click 'Remove from view' again | The course is hidden; no error is shown for the second action. | medium |
| TC-011 (input_edge) |  | Enter a long search term in the search field | User is on the My Courses page | 1. Enter a string of 200+ characters in the Search field<br>2. Press Enter or click the search button | The search executes successfully; the UI displays results or a message indicating no matches. | low |
| TC-012 (input_edge) |  | Enter special characters in the search field | User is on the My Courses page | 1. Enter special characters (e.g., @#$%^&*) in the Search field<br>2. Press Enter or click the search button | The search executes successfully; the UI displays results or a message indicating no matches. | low |

---

## Course Page

Total: **15** (positive: 9, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Overview Tab | User logged in as <Role> | 1. Click on the 'Overview' tab | Overview tab displayed | high |
| TC-002 | WF-002 | View Syllabus Tab | User logged in as <Role> | 1. Click on the 'Syllabus' tab | Syllabus tab displayed | high |
| TC-003 | WF-003 | View Assignments Tab | User logged in as <Role> | 1. Click on the 'Assignments' tab | Assignments tab displayed | high |
| TC-004 | WF-004 | View Resources Tab | User logged in as <Role> | 1. Click on the 'Resources' tab | Resources tab displayed | high |
| TC-005 | WF-005 | View Welcome Video | User logged in as <Role> | 1. Click on the 'Welcome Video' activity | Welcome video played | high |
| TC-006 | WF-006 | View Course Handbook | User logged in as <Role> | 1. Click on the 'Course Handbook' resource | Course handbook displayed | high |
| TC-007 | WF-007 | View Reading Assignment | User logged in as <Role> | 1. Click on the 'Reading Assignment' activity | Reading assignment displayed | high |
| TC-008 | WF-008 | View Lecture Slides | User logged in as <Role> | 1. Click on the 'Lecture Slides' resource | Lecture slides displayed | high |
| TC-009 | WF-009 | Collapse All Sections | User logged in as <Role> | 1. Click on the 'Collapse all' link | All sections collapsed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Attempt to access the Course Page without authentication |  | 1. Navigate to the Course Page URL | User is redirected to the login page | high |
| TC-011 | WF-009 | Attempt to collapse all sections when no sections are expanded |  | 1. Navigate to the Course Page<br>2. Click on 'Collapse all' link | No sections are collapsed; all sections remain in their current state | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (interaction_edge) | WF-009 | Collapse all sections after expanding | All sections are expanded | 1. Click on the 'Collapse all' link | All sections are collapsed; no sections are expanded. | medium |
| TC-013 (interaction_edge) | WF-001 | Rapidly switch between tabs | User is on the Course Page | 1. Click on the 'Overview' tab<br>2. Immediately click on the 'Syllabus' tab<br>3. Immediately click on the 'Assignments' tab<br>4. Immediately click on the 'Resources' tab | All tabs display their respective content without errors. | medium |
| TC-014 (interaction_edge) | WF-005 | View Welcome Video multiple times | User has viewed the Welcome Video once | 1. Click on the 'Welcome Video' activity<br>2. Watch the video<br>3. Click on the 'Welcome Video' activity again | Welcome video plays again without issues. | medium |
| TC-015 (interaction_edge) | WF-006 | View Course Handbook after navigating away | User has navigated to another tab | 1. Click on the 'Syllabus' tab<br>2. Click back to the 'Resources' tab<br>3. Click on the 'Course Handbook' activity | Course handbook displays correctly after tab navigation. | medium |

---

## Course Edit Mode and Activity Chooser

Total: **19** (positive: 7, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit a section | User logged in as <Role>, Edit mode is enabled | 1. Click the edit icon on the section<br>2. Enter <new section name> in the section name field<br>3. Click Save | Section edited; success message shown | high |
| TC-002 | WF-002 | Duplicate a section | User logged in as <Role>, Edit mode is enabled | 1. Click the three dot menu on the section<br>2. Select 'duplicate'<br>3. Confirm the duplication | Section duplicated; success message shown | high |
| TC-003 | WF-003 | Hide a section | User logged in as <Role>, Edit mode is enabled | 1. Click the three dot menu on the section<br>2. Select 'hide'<br>3. Confirm the hiding action | Section hidden; success message shown | high |
| TC-004 | WF-004 | Delete a section | User logged in as <Role>, Edit mode is enabled | 1. Click the three dot menu on the section<br>2. Select 'delete'<br>3. Confirm the deletion | Section deleted; success message shown | high |
| TC-005 | WF-005 | Move a section | User logged in as <Role>, Edit mode is enabled | 1. Click the three dot menu on the section<br>2. Select 'move'<br>3. Choose the new location<br>4. Confirm the move | Section moved; success message shown | high |
| TC-006 | WF-006 | Open Activity Chooser modal | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add an activity or resource' button | Activity chooser modal opened | medium |
| TC-007 | WF-007 | Add selected activity/resource | User logged in as <Role>, Edit mode is enabled, Activity chooser modal is opened | 1. Select 'Assignment' tile from the grid<br>2. Click 'Add' button | Activity/resource creation form opened | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the category filter blank and submit |  | 1. Open the Activity Chooser modal<br>2. Leave the category filter blank<br>3. Click Add | Form does not submit; error shown on category filter indicating it is required | high |
| TC-009 |  | Leave the search field blank and submit |  | 1. Open the Activity Chooser modal<br>2. Leave the search field blank<br>3. Click Add | Form does not submit; error shown on search field indicating it is required | high |
| TC-010 | WF-001 | Attempt to edit a section without required fields filled |  | 1. Click the edit icon for a section<br>2. Leave the required fields blank<br>3. Click Save | Form does not submit; error shown on required fields indicating they must be filled | high |
| TC-011 | WF-002 | Attempt to duplicate a section when it already exists |  | 1. Click the three-dot menu for a section<br>2. Select duplicate<br>3. Confirm duplication | Action is blocked; error shown indicating section must be unique | medium |
| TC-012 | WF-003 | Attempt to hide a section that is already hidden |  | 1. Click the three-dot menu for a hidden section<br>2. Select hide | Action is blocked; error shown indicating section is already hidden | medium |
| TC-013 | WF-004 | Attempt to delete a section that is already deleted |  | 1. Click the three-dot menu for a deleted section<br>2. Select delete | Action is blocked; error shown indicating section is already deleted | medium |
| TC-014 | WF-005 | Attempt to move a section that is already moved |  | 1. Click the three-dot menu for a moved section<br>2. Select move | Action is blocked; error shown indicating section cannot be moved again | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-006 | Open Activity Chooser modal | User is in Edit mode on the Course page | 1. Click on '+ Add an activity or resource' button | Activity chooser modal opens successfully | medium |
| TC-016 (boundary) | WF-007 | Add an activity/resource | User has opened the Activity Chooser modal | 1. Select 'Assignment' tile<br>2. Click 'Add' button | Activity creation form opens for 'Assignment' | medium |
| TC-017 (input_edge) |  | Search with long text | User is in Activity Chooser modal | 1. Enter a very long string (200+ characters) in the search field | Search field accepts input; no error shown, but search results may be empty | low |
| TC-018 (input_edge) |  | Search with special characters | User is in Activity Chooser modal | 1. Enter special characters (e.g., '@#$%^&*()') in the search field | Search field accepts input; no error shown, but search results may vary | low |
| TC-019 (interaction_edge) |  | Rapidly open and close Activity Chooser modal | User is in Edit mode on the Course page | 1. Click on '+ Add an activity or resource' button<br>2. Immediately close the modal<br>3. Click on '+ Add an activity or resource' button again | Activity chooser modal opens successfully without errors | low |

---

## Assignment Creation

Total: **22** (positive: 3, negative: 9, edge: 10)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create assignment and redirect to course page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and return to course' | creates assignment and redirects to course page | high |
| TC-002 | WF-002 | Create assignment and open new assignment's page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and display' | creates assignment and opens new assignment's page | high |
| TC-003 | WF-003 | Discard changes on assignment creation | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Click 'Cancel' | discards all changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Assignment Name field blank and submit |  | 1. Leave the Assignment_Name field blank<br>2. Fill all other fields as needed<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-005 |  | Submit with all required fields empty |  | 1. Leave the Assignment_Name field blank<br>2. Leave the Description field blank<br>3. Click 'Save and return to course' | Form does not submit; Assignment is not created; inline validation error appears on the Assignment_Name field indicating it is required | high |
| TC-006 |  | Attempt to submit with Allow Submissions From toggle off and fill in dates |  | 1. Toggle Allow_Submissions_From_Toggle off<br>2. Fill in Allow_Submissions_From with <invalid date><br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Allow_Submissions_From field indicating it is not enabled | medium |
| TC-007 |  | Attempt to submit with Due Date toggle off and fill in Due Date |  | 1. Toggle Due_Date_Toggle off<br>2. Fill in Due_Date with <invalid date><br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Due_Date field indicating it is not enabled | medium |
| TC-008 |  | Attempt to submit with Cut Off Date toggle off and fill in Cut Off Date |  | 1. Toggle Cut_Off_Date_Toggle off<br>2. Fill in Cut_Off_Date with <invalid date><br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Cut_Off_Date field indicating it is not enabled | medium |
| TC-009 |  | Attempt to submit with Maximum Number Of Uploaded Files filled while File Submissions is unchecked |  | 1. Leave File_Submissions unchecked<br>2. Fill in Maximum_Number_Of_Uploaded_Files with <invalid number><br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Maximum_Number_Of_Uploaded_Files field indicating it is not enabled | medium |
| TC-010 |  | Attempt to submit with Maximum Submission Size filled while File Submissions is unchecked |  | 1. Leave File_Submissions unchecked<br>2. Fill in Maximum_Submission_Size with <invalid number><br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Maximum_Submission_Size field indicating it is not enabled | medium |
| TC-011 |  | Attempt to submit with Grade To Pass filled while not specifying Grade Type |  | 1. Fill in Grade_To_Pass with <invalid number><br>2. Leave Grade_Type blank<br>3. Click 'Save and return to course' | Form does not submit; inline validation error appears on Grade_Type field indicating it is required | medium |
| TC-012 |  | Attempt to use the Add Restriction button without any prior selections |  | 1. Click on '+ Add restriction' button | No restriction type picker opens; user is informed that a selection must be made first | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Enter maximum number of uploaded files | File submissions toggle is enabled | 1. Enable the File Submissions toggle<br>2. Enter <maximum allowed value> in the Maximum Number Of Uploaded Files field<br>3. Click Save and return to course | Form submits successfully; assignment is created with maximum number of uploaded files set | medium |
| TC-014 (boundary) |  | Attempt to exceed maximum number of uploaded files | File submissions toggle is enabled | 1. Enable the File Submissions toggle<br>2. Enter <maximum allowed value + 1> in the Maximum Number Of Uploaded Files field<br>3. Click Save and return to course | Submission is blocked; error message indicates maximum number of uploaded files exceeded | medium |
| TC-015 (boundary) |  | Enter maximum submission size | File submissions toggle is enabled | 1. Enable the File Submissions toggle<br>2. Enter <maximum allowed size> in the Maximum Submission Size field<br>3. Click Save and return to course | Form submits successfully; assignment is created with maximum submission size set | medium |
| TC-016 (boundary) |  | Attempt to exceed maximum submission size | File submissions toggle is enabled | 1. Enable the File Submissions toggle<br>2. Enter <maximum allowed size + 1> in the Maximum Submission Size field<br>3. Click Save and return to course | Submission is blocked; error message indicates maximum submission size exceeded | medium |
| TC-017 (data_edge) |  | Test today's date for Allow Submissions From | Allow Submissions From toggle is enabled | 1. Enable the Allow Submissions From toggle<br>2. Set Allow Submissions From date to today's date<br>3. Click Save and return to course | Form submits successfully; assignment is created with today's date set for Allow Submissions From | medium |
| TC-018 (data_edge) |  | Test yesterday's date for Allow Submissions From | Allow Submissions From toggle is enabled | 1. Enable the Allow Submissions From toggle<br>2. Set Allow Submissions From date to yesterday's date<br>3. Click Save and return to course | Submission is blocked; error message indicates the date must not be before today | medium |
| TC-019 (data_edge) |  | Test far future date for Due Date | Due Date toggle is enabled | 1. Enable the Due Date toggle<br>2. Set Due Date to a far future date<br>3. Click Save and return to course | Form submits successfully; assignment is created with far future date set for Due Date | medium |
| TC-020 (input_edge) |  | Enter a long string in Assignment Name |  | 1. Enter a string of 200+ characters in the Assignment Name field<br>2. Click Save and return to course | Form submits successfully; assignment is created with the long Assignment Name | low |
| TC-021 (input_edge) |  | Enter special characters in Assignment Name |  | 1. Enter special characters in the Assignment Name field<br>2. Click Save and return to course | Form submits successfully; assignment is created with special characters in the Assignment Name | low |
| TC-022 (input_edge) |  | Enter leading and trailing whitespace in Assignment Name |  | 1. Enter leading and trailing whitespace in the Assignment Name field<br>2. Click Save and return to course | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Course Settings

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Save course settings with valid inputs | User logged in as <Role> | 1. Enter <valid course full name> in the Course Full Name field<br>2. Enter <valid course short name> in the Course Short Name field<br>3. Select <valid course category> from the Course Category dropdown<br>4. Select 'Show' from the Course Visibility dropdown<br>5. Click 'Save and display' | persists the configuration and returns to the course page | high |
| TC-002 | WF-002 | Cancel course settings without changes | User logged in as <Role> | 1. Click 'Cancel' | leaves existing settings unchanged | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Course Full Name field blank and submit |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-004 | WF-001 | Leave the Course Short Name field blank and submit |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Course Category field blank and submit |  | 1. Leave the Course Category field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the Course Full Name field blank<br>2. Leave the Course Short Name field blank<br>3. Leave the Course Category field blank<br>4. Click Save and display | Form does not submit; Course Full Name, Course Short Name, and Course Category fields display errors indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Enter maximum length in Course Full Name field |  | 1. Enter maximum allowed length string in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; entity is created with the maximum length string in the Course Full Name field | medium |
| TC-008 (boundary) | WF-001 | Enter one character below minimum in Course Short Name field |  | 1. Enter one character below the minimum allowed length in the Course Short Name field<br>2. Fill all other required fields<br>3. Click Save and display | Course Short Name field displays an error indicating the value is below the minimum allowed | medium |
| TC-009 (input_edge) |  | Enter long text in Course Summary field |  | 1. Enter a very long string (200+ characters) in the Course Summary field<br>2. Fill all other fields<br>3. Click Save and display | Form submits successfully; Course Summary displays the entered long text correctly | low |
| TC-010 (input_edge) |  | Enter special characters in Course Full Name field |  | 1. Enter special characters in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; Course Full Name displays the special characters correctly | low |

---

## Participants Management

Total: **25** (positive: 12, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters without conditions | User logged in as <role> | 1. Click Apply Filters Button | Filters applied to the participants list | high |
| TC-002 | WF-002 | Apply filters with conditions | User logged in as <role> | 1. Click Add Condition Link<br>2. Select <attribute> from Select Attribute dropdown<br>3. Click Apply Filters Button | Filters applied to the participants list | high |
| TC-003 | WF-003 | Clear filters | User logged in as <role> | 1. Click Clear Filters Button | Filters cleared from the participants list | medium |
| TC-004 | WF-004 | Open enrollment dialog | User logged in as <role> | 1. Click Enrol Users Button | opens enrollment dialog | high |
| TC-005 | WF-005 | Confirm enrollment | User logged in as <role>, Enrollment dialog is open | 1. Enter <user> in User Search Field<br>2. Select <role> from Role Dropdown<br>3. Click Confirm Enrollment Button | adds user to course at specified role | high |
| TC-006 | WF-006 | View user profile | User logged in as <role> | 1. Click View Profile on a participant row | User profile displayed | medium |
| TC-007 | WF-007 | Edit user role | User logged in as <role> | 1. Click Edit Role on a participant row | User role updated | medium |
| TC-008 | WF-008 | Send message to user | User logged in as <role> | 1. Click Send Message on a participant row | Message sent to user | medium |
| TC-009 | WF-009 | Enroll selected users | User logged in as <role>, Select users in the participants table | 1. Select 'Enroll' from the With selected users dropdown | Selected users enrolled | high |
| TC-010 | WF-010 | Remove selected users | User logged in as <role>, Select users in the participants table | 1. Select 'Remove' from the With selected users dropdown | Selected users removed | medium |
| TC-011 | WF-011 | Message selected users | User logged in as <role>, Select users in the participants table | 1. Select 'Message' from the With selected users dropdown | Message sent to selected users | medium |
| TC-012 | WF-012 | Add condition to filter | User logged in as <role> | 1. Click Add Condition Link | Condition added to filter system | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Attempt to apply filters without any conditions |  | 1. Click on the Apply Filters Button | Form does not submit; no filters applied; error shown indicating that conditions are required |  |
| TC-014 |  | Attempt to confirm enrollment without entering a user |  | 1. Click on the Enrol Users Button<br>2. Leave the User Search Field blank<br>3. Click on the Confirm Enrollment Button | Form does not submit; no user enrolled; error shown indicating that a user must be specified |  |
| TC-015 |  | Attempt to enroll selected users without selecting any users |  | 1. Click on the Enroll button in the With selected users dropdown | Form does not submit; no users enrolled; error shown indicating that at least one user must be selected |  |
| TC-016 |  | Attempt to remove selected users without selecting any users |  | 1. Click on the Remove button in the With selected users dropdown | Form does not submit; no users removed; error shown indicating that at least one user must be selected |  |
| TC-017 |  | Attempt to send message without selecting any users |  | 1. Click on the Message button in the With selected users dropdown | Form does not submit; no messages sent; error shown indicating that at least one user must be selected |  |
| TC-018 | WF-001 | Attempt to apply filters without selecting an attribute |  | 1. Click on the Add Condition Link<br>2. Leave the Select Attribute dropdown blank<br>3. Click on the Apply Filters Button | Form does not submit; no filters applied; error shown indicating that an attribute must be selected |  |
| TC-019 | WF-012 | Attempt to add condition to filter without any conditions |  | 1. Click on the Add Condition Link<br>2. Click on the Apply Filters Button | Form does not submit; no conditions added; error shown indicating that conditions must be specified |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 (boundary) | WF-002 | Apply filters with one condition | User is on the Participants page | 1. Select an attribute in the Select Attribute dropdown<br>2. Click Apply Filters Button | Filters applied to the participants list with the selected condition | medium |
| TC-021 (boundary) | WF-003 | Clear filters after applying conditions | User has applied filters with conditions | 1. Click Clear Filters Button | Filters cleared from the participants list, showing all users | medium |
| TC-022 (boundary) | WF-001 | Apply filters without any conditions | User is on the Participants page | 1. Click Apply Filters Button | Filters applied to the participants list with no conditions; list remains unchanged | medium |
| TC-023 (interaction_edge) | WF-004 | Rapid enrollment dialog opening | User is on the Participants page | 1. Click Enrol Users Button<br>2. Click Enrol Users Button again rapidly | Enrollment dialog opens without errors or duplicates | low |
| TC-024 (boundary) | WF-005 | Confirm enrollment with no role selected | User is in the Enrol Users Dialog | 1. Enter a user in the User Search Field<br>2. Click Confirm Enrollment Button | Enrollment is blocked; error message indicates a role must be selected | medium |
| TC-025 (input_edge) | WF-012 | Add condition with special characters | User is on the Participants page | 1. Click Add Condition Link<br>2. Enter special characters in the condition field | Condition added to filter system with special characters accepted | low |

---

## Assignment — Teacher View

Total: **10** (positive: 6, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open grading interface for individual students | User logged in as <Teacher> | 1. Click the 'Grade' button | opens grading interface for individual students | high |
| TC-002 |  | Navigate to Assignment tab | User logged in as <Teacher> | 1. Click on the 'Assignment' tab | The Assignment tab is active and displayed | medium |
| TC-003 |  | Navigate to Settings tab | User logged in as <Teacher> | 1. Click on the 'Settings' tab | The Settings tab is active and displayed | medium |
| TC-004 |  | Navigate to Submissions tab | User logged in as <Teacher> | 1. Click on the 'Submissions' tab | The Submissions tab is active and displayed | medium |
| TC-005 |  | Navigate to Advanced grading tab | User logged in as <Teacher> | 1. Click on the 'Advanced grading' tab | The Advanced grading tab is active and displayed | medium |
| TC-006 |  | Navigate to More tab | User logged in as <Teacher> | 1. Click on the 'More' tab | The More tab is active and displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Attempt to open grading interface without proper role | User is not logged in or lacks teacher role | 1. Click on the Grade button | User is blocked from accessing the grading interface; no action occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) | WF-001 | Rapid consecutive clicks on Grade button | User is on the Assignment page | 1. Click the Grade button<br>2. Immediately click the Grade button again | The grading interface opens successfully without duplication of actions or errors shown. | medium |
| TC-009 (input_edge) |  | Long description input | User is on the Assignment page | 1. Enter a very long string (200+ characters) in the Description field | The system accepts the long description or truncates it with a visible indicator. | low |
| TC-010 (input_edge) |  | Special characters in description | User is on the Assignment page | 1. Enter special characters (e.g., @#$%^&*) in the Description field | The system accepts the input or displays a specific error message. | low |

---

## Assignment Submissions

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Grading Workflow for a submission | User logged in as <Role>, At least one submission is available in the table | 1. Search for a submission by entering <valid student name> in the Student Name search field<br>2. Click the action menu for the submission row<br>3. Select 'Open Grading Workflow' from the action menu | Grading workflow opened for the selected submission | high |
| TC-002 | WF-001 | Open Grading Workflow for a submission with specific submission status | User logged in as <Role>, At least one submission with status 'Submitted for grading' is available in the table | 1. Select 'Submitted for grading' from the Submission Status dropdown<br>2. Click the action menu for the submission row<br>3. Select 'Open Grading Workflow' from the action menu | Grading workflow opened for the selected submission | high |
| TC-003 | WF-001 | Open Grading Workflow for a submission with specific grading status | User logged in as <Role>, At least one submission with grading status 'Not graded' is available in the table | 1. Select 'Not graded' from the Grading Status dropdown<br>2. Click the action menu for the submission row<br>3. Select 'Open Grading Workflow' from the action menu | Grading workflow opened for the selected submission | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to open grading workflow without selecting a submission |  | 1. Navigate to the Submissions view<br>2. Attempt to click 'Open Grading Workflow' without selecting any submission | Action is blocked; no grading workflow is opened |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid consecutive opening of grading workflows | User is on the Submissions view with multiple submissions listed | 1. Click on the action menu for the first submission.<br>2. Select 'Open Grading Workflow'.<br>3. Immediately click on the action menu for the second submission.<br>4. Select 'Open Grading Workflow'. | Both grading workflows open successfully without errors. | medium |
| TC-006 (input_edge) |  | Search with special characters in Student Name | User is on the Submissions view | 1. Enter special characters (e.g., '@#$%') in the Student Name search field.<br>2. Click the search button. | Search results are displayed; no error shown, indicating the system handles special characters. | low |
| TC-007 (input_edge) |  | Search with leading/trailing whitespace in Student Name | User is on the Submissions view | 1. Enter '   John Doe   ' in the Student Name search field.<br>2. Click the search button. | Leading/trailing whitespace is trimmed; search results show 'John Doe' without extra spaces. | low |

---

## Gradebook — Grader Report

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit individual grade entry | User logged in as <role>, Edit mode is disabled | 1. Click the three-dot menu on a grade entry cell<br>2. Select 'Edit Grade Entry' from the menu<br>3. Enter <valid grade> in the grade entry field<br>4. Click 'Save' to apply changes | Grade entry updated | high |
| TC-002 | WF-002 | Edit grade settings for an activity | User logged in as <role>, Edit mode is disabled | 1. Click the action menu on the 'Activity' column header<br>2. Select 'Edit Grade Settings' from the options<br>3. Modify the grade settings as needed<br>4. Click 'Save' to apply changes | Grade settings updated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to save a grade entry with a value outside the configured grade range | Edit mode is enabled | 1. Enter a grade value that is outside the configured grade range in a grade cell<br>2. Click 'Save changes' | Inline validation error appears indicating 'Values outside the configured grade range block saving'; grade entry is not updated | high |
| TC-004 | WF-002 | Attempt to save grade settings with invalid values | Edit mode is enabled | 1. Open the action menu for an activity<br>2. Select 'Edit Grade Settings'<br>3. Enter invalid settings that violate constraints<br>4. Click 'Save changes' | Inline validation error appears indicating 'Values outside the configured grade range block saving'; grade settings are not updated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (boundary) | WF-001 | Attempt to save a grade entry with the minimum allowed grade value | Edit mode is enabled | 1. Enter the minimum allowed grade value in the grade cell<br>2. Click Save changes | Grade entry updates successfully; the saved value is displayed in the grade cell | medium |
| TC-006 (boundary) | WF-001 | Attempt to save a grade entry with a value below the configured grade range | Edit mode is enabled | 1. Enter a value below the minimum allowed grade in the grade cell<br>2. Click Save changes | Saving is blocked; an inline error indicates that the value is outside the configured grade range | medium |
| TC-007 (boundary) | WF-002 | Attempt to save grade settings with the minimum allowed grade value | User is editing grade settings | 1. Set the minimum allowed grade value in the grade settings<br>2. Click Save changes | Grade settings update successfully; the new minimum grade value is displayed in the settings | medium |
| TC-008 (boundary) | WF-002 | Attempt to save grade settings with a value below the configured minimum grade | User is editing grade settings | 1. Set a value below the configured minimum grade in the grade settings<br>2. Click Save changes | Saving is blocked; an inline error indicates that the value is outside the configured grade range | medium |

---

## Profile

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Message interface | User logged in as <Teacher> | 1. Click the Message button | Message interface opened | high |
| TC-002 | WF-002 | View Last Access date | User logged in as <Teacher> | 1. Observe the Last Access field in the Login Activity card | Last access date displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to access the Profile page without authentication |  | 1. Navigate to the Profile page | User is redirected to the login page | high |
| TC-004 | WF-002 | Attempt to view Last Access without sufficient permissions | User does not have the required role | 1. Click on the Last Access field in the Login Activity card | Access is denied; Last Access information is not displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-002 | View Last Access with boundary date |  | 1. Navigate to the Profile page<br>2. Observe the Last Access field | Last access date displayed is today's date; the date format is correct. | medium |
| TC-006 (state_edge) | WF-002 | View Last Access with yesterday's date |  | 1. Navigate to the Profile page<br>2. Observe the Last Access field | Last access date displayed is yesterday's date; the date format is correct. | medium |
| TC-007 (input_edge) |  | Enter long text in Profile Description |  | 1. Navigate to the Profile page<br>2. Enter a string of 200+ characters in the Profile Description field | Profile Description field accepts the input without truncation or displays an error indicating the input is too long. | low |
| TC-008 (input_edge) |  | Enter special characters in Profile Description |  | 1. Navigate to the Profile page<br>2. Enter a string with special characters in the Profile Description field | Profile Description field accepts the input or displays a specific error indicating invalid characters. | low |

---

## Profile Edit

Total: **12** (positive: 2, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update Profile with valid data | User logged in as <Role> | 1. Open the Edit Profile form<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid email> in the Email Address field<br>5. Upload a <valid image file> in the New Picture Upload area<br>6. Click Update_Profile to submit the form | The profile page refreshes to show the updated profile information | high |
| TC-002 | WF-002 | Cancel profile edit | User logged in as <Role> | 1. Open the Edit Profile form<br>2. Click Cancel | Exits without making changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update_Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Email Address field blank<br>4. Click Update_Profile | Form does not submit; errors shown on First_Name, Last_Name, and Email_Address fields indicating they are required | high |
| TC-007 |  | Upload a file that does not meet the drag-and-drop constraints |  | 1. Select a file that does not meet the upload constraints<br>2. Click Update_Profile | Inline validation error appears indicating the file upload does not meet the required constraints | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Upload a picture at the maximum file size limit | User is on the Edit Profile form | 1. Click on the New Picture Upload area<br>2. Upload a file that is exactly at the size limit | File upload succeeds; visible confirmation message appears indicating the picture has been uploaded. | medium |
| TC-009 (boundary) | WF-001 | Attempt to upload a picture exceeding the maximum file size limit | User is on the Edit Profile form | 1. Click on the New Picture Upload area<br>2. Upload a file that is one byte over the size limit | Upload is blocked; an error message displays indicating the file exceeds the size limit. | medium |
| TC-010 (input_edge) |  | Enter a very long string in the First Name field | User is on the Edit Profile form | 1. Enter a string longer than 200 characters in the First Name field | The form accepts the input or shows a visible error indicating the input is too long. | low |
| TC-011 (input_edge) |  | Enter special characters in the Last Name field | User is on the Edit Profile form | 1. Enter special characters (e.g., !@#$%^&*) in the Last Name field | The form accepts the input or shows a specific error message indicating invalid characters. | low |
| TC-012 (interaction_edge) |  | Rapidly submit the form after a successful update | User has successfully submitted the form once | 1. Click the Update Profile button<br>2. Immediately click the Update Profile button again after the page refreshes | The second submission attempt is blocked; the form remains on the profile page without creating a duplicate submission. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click the Logout button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | user must be authenticated | 1. Ensure the user is not authenticated<br>2. Click Logout_Button | Logout action is blocked; user remains on the current page and is not logged out | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Logout button click while authenticated | User is authenticated | 1. Click the Logout button | User is redirected to the login page and the session is terminated successfully. | medium |
| TC-004 (interaction_edge) |  | Logout button click while not authenticated | User is not authenticated | 1. Click the Logout button | Logout action is blocked; no session termination occurs and the user remains on the current page. | medium |

---
