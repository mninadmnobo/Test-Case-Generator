# Test Cases — Moodleteacher

Generated: 2026-06-10T21:11:04.549656Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 170 | 59 | 55 | 56 | 86 | 51 | 30 |

## Login

Total: **14** (positive: 3, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log in with valid credentials | User logged in as <Teacher> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Log in button | Redirect to the Dashboard | high |
| TC-002 | WF-002 | Log in with invalid credentials | User logged in as <Teacher> | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Log in button | Show inline error message; clear password field; retain username | high |
| TC-003 | WF-002 | Log in with empty credentials | User logged in as <Teacher> | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Log in button | Show inline error message; clear password field; retain username | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with invalid Username and valid Password |  | 1. Enter <invalid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | Inline error message shows; Password field is cleared; Username retains <invalid username> | high |
| TC-008 |  | Submit with valid Username and invalid Password |  | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Log in | Inline error message shows; Password field is cleared; Username retains <valid username> | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Enter empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Log in button | Inline error message is shown; both fields remain empty | medium |
| TC-010 (boundary) | WF-002 | Enter valid Username and empty Password |  | 1. Enter valid Username in the Username field<br>2. Leave the Password field empty<br>3. Click the Log in button | Inline error message is shown; Password field is cleared; Username remains in the Username field | medium |
| TC-011 (boundary) | WF-002 | Enter empty Username and valid Password |  | 1. Leave the Username field empty<br>2. Enter valid Password in the Password field<br>3. Click the Log in button | Inline error message is shown; Username field remains empty; Password field is cleared | medium |
| TC-012 (input_edge) |  | Enter very long Username |  | 1. Enter a string longer than the maximum allowed length in the Username field<br>2. Enter valid Password in the Password field<br>3. Click the Log in button | Inline error message is shown indicating the Username is too long | low |
| TC-013 (input_edge) |  | Enter special characters in Username |  | 1. Enter special characters in the Username field<br>2. Enter valid Password in the Password field<br>3. Click the Log in button | Inline error message is shown indicating invalid characters in the Username | low |
| TC-014 (input_edge) |  | Enter leading and trailing whitespace in Username |  | 1. Enter '   validUsername   ' in the Username field<br>2. Enter valid Password in the Password field<br>3. Click the Log in button | Leading/trailing whitespace is trimmed; Username is saved as 'validUsername' | low |

---

## Dashboard

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar event | User logged in as <Role> | 1. Click the 'New event' button<br>2. Fill in the event details<br>3. Click 'Save' to create the event | A success notification is displayed; the new event appears in the Calendar block | high |
| TC-002 | WF-002 | Open full calendar view | User logged in as <Role> | 1. Click the 'Full calendar' link | Full calendar view opened | medium |
| TC-003 | WF-003 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or export calendars' link | Calendar data management opened | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to create a new calendar event without filling in required fields |  | 1. Click on the 'New event' button | Form does not submit; no calendar event is created; required fields are highlighted |  |
| TC-005 | WF-002 | Attempt to open full calendar view without authentication |  | 1. Click on the 'Full calendar' link | User is redirected to the login page |  |
| TC-006 | WF-003 | Attempt to open calendar data management without authentication |  | 1. Click on the 'Import or export calendars' link | User is redirected to the login page |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long search term in the search field |  | 1. Navigate to the Dashboard<br>2. Enter a string of 200+ characters in the search field | Search field accepts the input without error or truncation | low |
| TC-008 (input_edge) |  | Enter special characters in the search field |  | 1. Navigate to the Dashboard<br>2. Enter a string containing special characters (e.g., @#$%^&*) in the search field | Search field accepts the input without error | low |
| TC-009 (input_edge) |  | Enter a search term with leading and trailing whitespace |  | 1. Navigate to the Dashboard<br>2. Enter a string with leading and trailing spaces in the search field | Leading/trailing whitespace is trimmed; saved value shown in the search field has no extra spaces | low |

---

## Dashboard — Edit Mode

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Add a block page | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block' button | Add a block page opens with available block types | high |
| TC-002 | WF-002 | Reset layout to default | User logged in as <Role>, Edit mode is enabled | 1. Click 'Reset page to default' button | Layout changes reverted to default | high |
| TC-003 | WF-003 | Open block configuration options | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot options menu on an existing block<br>2. Select 'Configure' | Block configuration options displayed | medium |
| TC-004 | WF-004 | Move an existing block | User logged in as <Role>, Edit mode is enabled | 1. Click and drag the move icon on an existing block to a new position | Block moved to new position | medium |
| TC-005 | WF-005 | Delete an existing block | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot options menu on an existing block<br>2. Select 'Delete'<br>3. Confirm deletion | Block deleted from the dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to add a block without selecting a block type | Edit mode is toggled on | 1. Click on the '+ Add a block' button<br>2. Leave the block type unselected<br>3. Click on the 'Add' button | Error shown indicating that a block type must be selected before adding a block | high |
| TC-007 | WF-002 | Attempt to reset page to default when no changes have been made | Edit mode is toggled on | 1. Click on the 'Reset page to default' button | No changes occur; the layout remains unchanged and a message indicates no changes to revert | medium |
| TC-008 | WF-003 | Attempt to configure a block when no blocks are present | Edit mode is toggled on | 1. Click on the 'Configure' option for a block | Error shown indicating that there are no blocks to configure | high |
| TC-009 | WF-004 | Attempt to move a block when no blocks are present | Edit mode is toggled on | 1. Click on the 'Move' option for a block | Error shown indicating that there are no blocks to move | high |
| TC-010 | WF-005 | Attempt to delete a block when no blocks are present | Edit mode is toggled on | 1. Click on the 'Delete' option for a block | Error shown indicating that there are no blocks to delete | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid consecutive attempts to add a block | Edit mode is toggled on | 1. Click '+ Add a block' button<br>2. Immediately click '+ Add a block' button again | Add a block page opens with available block types; no duplicate block pages are opened | medium |
| TC-012 (interaction_edge) | WF-002 | Attempt to reset page to default after making changes | Edit mode is toggled on, At least one block has been added or moved | 1. Click 'Reset page to default' button | Layout changes reverted to default; all blocks return to their original positions | medium |
| TC-013 (input_edge) |  | Check handling of special characters in block configuration | Edit mode is toggled on, At least one block exists | 1. Click on the three-dot options menu of an existing block<br>2. Select 'Configure'<br>3. Enter special characters in the configuration field | Configuration accepts special characters without error; changes are displayed correctly | low |
| TC-014 (input_edge) |  | Check handling of long text in block configuration | Edit mode is toggled on, At least one block exists | 1. Click on the three-dot options menu of an existing block<br>2. Select 'Configure'<br>3. Enter a very long string (200+ characters) in the configuration field | Configuration either accepts the long text or truncates it with a visible indicator | low |

---

## My Courses

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View course details by clicking course name | User logged in as <Teacher>, Courses are available on the My Courses page | 1. Click on the course name of a displayed course card | Course details displayed | high |
| TC-002 | WF-002 | Star a course | User logged in as <Teacher>, Courses are available on the My Courses page | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' | Course pinned to the top | medium |
| TC-003 | WF-003 | Remove a course from view | User logged in as <Teacher>, Courses are available on the My Courses page | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' | Course hidden from view | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to view course details without selecting a course |  | 1. Navigate to My Courses page<br>2. Do not click on any course name | No course details displayed; user remains on My Courses page | high |
| TC-005 | WF-002 | Attempt to star a course without selecting a course |  | 1. Navigate to My Courses page<br>2. Do not click on any course's three-dot menu | Course not starred; no change in course order | high |
| TC-006 | WF-003 | Attempt to remove a course from view without selecting a course |  | 1. Navigate to My Courses page<br>2. Do not click on any course's three-dot menu | Course not removed from view; no change in course visibility | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly click on course name multiple times | User is on the My Courses page and has multiple courses displayed | 1. Click on the course name of any course card<br>2. Immediately click on the same course name again<br>3. Repeat the click action rapidly | Only the first click navigates to the course main page; subsequent clicks do not trigger additional navigation. | medium |
| TC-008 (interaction_edge) | WF-002 | Rapidly star a course multiple times | User is on the My Courses page and has at least one course displayed | 1. Click on the three-dot menu of a course card<br>2. Select 'Star this course'<br>3. Immediately click 'Star this course' again multiple times | The course is only starred once; no duplicate entries appear in the starred list. | medium |
| TC-009 (interaction_edge) | WF-003 | Rapidly remove a course from view multiple times | User is on the My Courses page and has at least one course displayed | 1. Click on the three-dot menu of a course card<br>2. Select 'Remove from view'<br>3. Immediately click 'Remove from view' again multiple times | The course is only removed from view once; it does not disappear multiple times from the list. | medium |

---

## Course Page

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify course content is displayed correctly | User logged in as <Student> | 1. Navigate to the Course page | The course name is displayed as the page heading, followed by the navigation tab bar and collapsible sections for activities and resources. | high |
| TC-002 |  | Verify collapsible sections functionality | User logged in as <Student>, Course page is open | 1. Click on a section's chevron to expand it | The selected section expands to show its activities and resources. | medium |
| TC-003 |  | Verify 'Collapse all' functionality | User logged in as <Student>, Course page is open with expanded sections | 1. Click on the 'Collapse all' link | All sections are collapsed, hiding their activities and resources. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to access the course page without authentication |  | 1. Navigate to the Course page URL without logging in | User is redirected to the login page | high |
| TC-005 |  | Attempt to access a non-existent course |  | 1. Navigate to a URL of a non-existent course | Page displays 'Course not found' error message | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long course name |  | 1. Navigate to the Course Page<br>2. Observe the course name field<br>3. Enter a string of 200+ characters in the course name | Course name is displayed correctly, either accepted or truncated with an indicator | low |
| TC-007 (input_edge) |  | Enter special characters in the course name |  | 1. Navigate to the Course Page<br>2. Observe the course name field<br>3. Enter a string with special characters (e.g., !@#$%^&*()) in the course name | Course name is accepted and displayed correctly or an error is shown | low |
| TC-008 (input_edge) |  | Enter whitespace in the course name |  | 1. Navigate to the Course Page<br>2. Observe the course name field<br>3. Enter a course name with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved value shown in the course name has no extra spaces | low |

---

## Course Edit Mode and Activity Chooser

Total: **16** (positive: 8, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Rename a section or activity | User logged in as <Role>, Edit mode is enabled | 1. Click the edit icon next to the section or activity<br>2. Enter <new name> in the rename field<br>3. Click Save | Section or activity renamed | high |
| TC-002 | WF-002 | Duplicate a section or activity | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot menu next to the section or activity<br>2. Select Duplicate | Section or activity duplicated | high |
| TC-003 | WF-003 | Hide a section or activity | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot menu next to the section or activity<br>2. Select Hide | Section or activity hidden | high |
| TC-004 | WF-004 | Delete a section or activity | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot menu next to the section or activity<br>2. Select Delete<br>3. Click Confirm on the Delete dialog | Section or activity deleted | high |
| TC-005 | WF-005 | Move a section or activity | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot menu next to the section or activity<br>2. Select Move<br>3. Choose a new location<br>4. Click Confirm | Section or activity moved | high |
| TC-006 | WF-006 | Add an activity or resource | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add an activity or resource' button<br>2. Select a category from the filter bar<br>3. Click on a tile for an activity or resource<br>4. Click Add | Activity or resource added | high |
| TC-007 | WF-007 | Open Activity Chooser | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add an activity or resource' button | Activity Chooser modal opened | high |
| TC-008 | WF-008 | Select activity/resource tile and add | User logged in as <Role>, Edit mode is enabled, Activity Chooser modal is open | 1. Click on a tile for an activity or resource<br>2. Click Add | Activity/resource creation form opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Attempt to rename a section or activity without entering a new name |  | 1. Click the edit icon for a section or activity<br>2. Leave the name field blank<br>3. Click Save | Inline validation error appears on the name field indicating it is required | high |
| TC-010 | WF-004 | Attempt to delete a section or activity without confirmation |  | 1. Click the delete option for a section or activity<br>2. Do not confirm the deletion | No deletion occurs; section or activity remains visible | high |
| TC-011 | WF-006 | Attempt to add an activity or resource without selecting a tile |  | 1. Click the '+ Add an activity or resource' button<br>2. Leave the Activity Chooser modal without selecting any tile<br>3. Click Add | Inline validation error appears indicating an activity or resource must be selected | high |
| TC-012 | WF-007 | Attempt to open Activity Chooser without proper permissions |  | 1. Attempt to click on the '+ Add an activity or resource' button | User is blocked from opening the Activity Chooser; access denied message displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-006 | Rapid re-submission after adding an activity | User is in Edit mode on the Course page | 1. Click '+ Add an activity or resource'<br>2. Select an activity tile from the Activity Chooser modal<br>3. Click 'Add'<br>4. Immediately click '+ Add an activity or resource' again | Second '+ Add an activity or resource' click opens the Activity Chooser modal again without creating a duplicate activity. | medium |
| TC-014 (interaction_edge) | WF-007 | Open Activity Chooser modal multiple times | User is in Edit mode on the Course page | 1. Click '+ Add an activity or resource'<br>2. Close the Activity Chooser modal<br>3. Click '+ Add an activity or resource' again | Activity Chooser modal opens successfully again without any errors. | low |
| TC-015 (interaction_edge) | WF-008 | Select activity tile and attempt to add without choosing a category | User is in the Activity Chooser modal | 1. Click on an activity tile (e.g., Assignment)<br>2. Do not select a category and click 'Add' | Activity/resource creation form opens successfully for the selected tile regardless of category selection. | low |
| TC-016 (input_edge) |  | Enter long text in the renaming field | User is editing a section or activity | 1. Click the edit icon on a section or activity<br>2. Enter a string of 200+ characters in the renaming field | The renaming field accepts the long text and displays it correctly after saving. | low |

---

## Assignment Creation

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create assignment and return to course | User logged in as <Role> | 1. Select Assignment from the Activity Chooser<br>2. Enter <valid assignment name> in the Assignment name field<br>3. Enter <valid description> in the Description rich text editor<br>4. Click 'Save and return to course' | Assignment created; redirected to course page | high |
| TC-002 | WF-002 | Create assignment and display it | User logged in as <Role> | 1. Select Assignment from the Activity Chooser<br>2. Enter <valid assignment name> in the Assignment name field<br>3. Enter <valid description> in the Description rich text editor<br>4. Click 'Save and display' | Assignment created; opened new assignment's page | high |
| TC-003 | WF-003 | Cancel assignment creation | User logged in as <Role> | 1. Select Assignment from the Activity Chooser<br>2. Click 'Cancel' | All changes discarded | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Assignment name field blank and submit |  | 1. Leave the Assignment name field blank<br>2. Fill all other fields as required<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment name field indicating it is required | high |
| TC-005 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click 'Save and return to course' | Inline validation errors appear on all required fields indicating they are required; form does not submit | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) |  | Enter the minimum required length in the Assignment name field |  | 1. Open the assignment creation form<br>2. Enter exactly <minimum length> characters in the Assignment name field<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | Form submits successfully; entity is created with the <minimum length> | medium |
| TC-007 (boundary) |  | Enter one character less than the minimum required length in the Assignment name field |  | 1. Open the assignment creation form<br>2. Enter <minimum length - 1> characters in the Assignment name field<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | Assignment name field displays an error indicating the value is below the minimum allowed | medium |
| TC-008 (input_edge) |  | Enter a very long string in the Description field |  | 1. Open the assignment creation form<br>2. Enter a string of 200+ characters in the Description field<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | Form submits successfully; Description field displays the entered text without truncation | low |
| TC-009 (input_edge) |  | Enter special characters in the Assignment name field |  | 1. Open the assignment creation form<br>2. Enter special characters in the Assignment name field<br>3. Fill all other required fields<br>4. Click 'Save and return to course' | Form submits successfully; the Assignment name is saved as entered | low |

---

## Course Settings

Total: **8** (positive: 1, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Course Settings with all required fields filled | User logged in as <Teacher>, Course Settings form is open | 1. Enter <valid course full name> in the Course full name field<br>2. Enter <valid course short name> in the Course short name field<br>3. Select <valid course category> from the Course category dropdown<br>4. Select <Show/Hide> from the Course visibility dropdown<br>5. Enter <valid start date> in the Course start date field<br>6. Click the Enable toggle for Course end date<br>7. Enter <valid end date> in the Course end date field<br>8. Enter <valid course ID number> in the Course ID number field<br>9. Enter <valid course summary> in the Course summary rich text editor<br>10. Upload a <valid course image> in the Course image upload field<br>11. Select <valid course format> from the Course format dropdown<br>12. Adjust layout controls as necessary based on selected format<br>13. Set appearance settings as required<br>14. Enter <valid maximum upload size> in the Maximum upload size field<br>15. Toggle Completion tracking on<br>16. Select <valid group mode> from the Groups dropdown<br>17. Enter <valid tags> in the Tags field<br>18. Click 'Save and display' | The course settings are saved, and the user is redirected to the course page displaying the updated settings. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Course full name field blank and submit |  | 1. Leave the Course full name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course full name field indicating it is required | high |
| TC-003 |  | Leave the Course short name field blank and submit |  | 1. Leave the Course short name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course short name field indicating it is required | high |
| TC-004 |  | Leave the Course category field unselected and submit |  | 1. Leave the Course category field unselected<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course category field indicating it is required | high |
| TC-005 |  | Submit with all required fields empty |  | 1. Leave the Course full name field blank<br>2. Leave the Course short name field blank<br>3. Leave the Course category field unselected<br>4. Click Save and display | Inline validation error appears on the Course full name, Course short name, and Course category fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a long string in Course full name |  | 1. Enter a string of 200+ characters in the Course full name field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; saved value in Course full name is truncated to the maximum allowed length | low |
| TC-007 (input_edge) |  | Enter special characters in Course summary |  | 1. Enter special characters in the Course summary field<br>2. Fill all other required fields<br>3. Click Save and display | Form submits successfully; Course summary displays the entered special characters correctly | low |
| TC-008 (input_edge) |  | Enter leading/trailing whitespace in Course ID number |  | 1. Enter leading and trailing spaces in the Course ID number field<br>2. Fill all other required fields<br>3. Click Save and display | Leading/trailing whitespace is trimmed; saved value in Course ID number has no extra spaces | low |

---

## Participants Management

Total: **17** (positive: 7, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters to participants list | User logged in as <role> | 1. Select <enrollment context> from the enrolled-users scope dropdown<br>2. Click 'Apply filters' button | Filters applied; participants list updated | high |
| TC-002 | WF-002 | Clear filters on participants list | User logged in as <role>, Filters are currently applied | 1. Click 'Clear filters' button | Filters cleared; participants list reset | high |
| TC-003 | WF-003 | Enroll users | User logged in as <role>, Enrol users dialog is open | 1. Enter <user search term> in the user search field<br>2. Select <role> from the Role dropdown<br>3. Enter <enrollment duration> in the Enrollment duration field<br>4. Click 'Confirm' to enroll the user | User enrolled; success message shown | high |
| TC-004 | WF-004 | View participant profile | User logged in as <role>, Participants list is displayed | 1. Click on the profile link of a participant | Profile displayed | medium |
| TC-005 | WF-005 | Edit participant role | User logged in as <role>, Participants list is displayed | 1. Click on the three-dot action menu of a participant<br>2. Select 'Edit role' from the menu<br>3. Choose <new role> from the Role dropdown<br>4. Click 'Save' to update the role | Role updated; success message shown | medium |
| TC-006 | WF-006 | Send message to participant | User logged in as <role>, Participants list is displayed | 1. Click on the three-dot action menu of a participant<br>2. Select 'Send message' from the menu<br>3. Enter <message> in the message field<br>4. Click 'Send' to deliver the message | Message sent; success notification shown | medium |
| TC-007 | WF-007 | Apply bulk action to selected users | User logged in as <role>, Participants list is displayed, At least one user is selected | 1. Select multiple users using the checkbox<br>2. Choose <bulk action> from the 'With selected users...' dropdown<br>3. Click 'Apply' to execute the bulk action | Bulk action applied to selected users | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to apply filters with no conditions set |  | 1. Leave all filter fields empty<br>2. Click Apply filters | Filters are not applied; participants list remains unchanged; error message displayed indicating no conditions set | high |
| TC-009 |  | Attempt to clear filters when no filters are applied |  | 1. Click Clear filters | Filters remain unchanged; no action taken; message displayed indicating no filters to clear | medium |
| TC-010 | WF-003 | Attempt to enroll users without filling required fields |  | 1. Click Enrol users<br>2. Leave the user search field blank<br>3. Click Enrol users | User is not enrolled; error shown on user search field indicating it is required | high |
| TC-011 | WF-005 | Attempt to edit participant role without selecting a user |  | 1. Click Edit role without selecting any participant | Edit role action is blocked; no role change occurs; error message displayed indicating no participant selected | high |
| TC-012 | WF-006 | Attempt to send message to participant without selecting a user |  | 1. Click Send message without selecting any participant | Send message action is blocked; no message sent; error message displayed indicating no participant selected | high |
| TC-013 | WF-007 | Attempt to apply bulk action without selecting any users |  | 1. Leave all users unchecked<br>2. Click Apply bulk action | Bulk action is not applied; no action taken; error message displayed indicating no users selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (interaction_edge) | WF-001 | Rapid re-application of filters | Participants list is displayed, Filters are applied | 1. Click 'Apply filters' button<br>2. Immediately click 'Apply filters' button again | Second filter application is blocked; participants list remains unchanged | medium |
| TC-015 (interaction_edge) | WF-002 | Rapid clearing of filters | Participants list is displayed, Filters are applied | 1. Click 'Clear filters' button<br>2. Immediately click 'Clear filters' button again | Second clear action is blocked; participants list remains reset | medium |
| TC-016 (interaction_edge) | WF-003 | Enroll user with maximum allowed roles | Enrollment dialog is open, User search field is filled | 1. Select the maximum number of roles from the Role dropdown<br>2. Click 'Enrol users' button | User enrolled successfully; success message shown | medium |
| TC-017 (interaction_edge) | WF-003 | Enroll user with no roles selected | Enrollment dialog is open | 1. Leave Role dropdown unselected<br>2. Click 'Enrol users' button | Enrollment is blocked; error message displayed indicating role must be selected | medium |

---

## Assignment — Teacher View

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open grading interface for individual students | User logged in as <Teacher>, Assignment page is displayed | 1. Click the 'Grade' button | Grading interface opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access the grading interface |  | 1. Attempt to click the 'Grade' button without logging in | User is redirected to the login page | high |
| TC-003 |  | Accessing the grading interface without the required role |  | 1. Log in as a user without teacher role<br>2. Attempt to click the 'Grade' button | Access is denied; 'You do not have permission to access this page' message is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapidly click the Grade button multiple times | User is on the Assignment page | 1. Click the Grade button<br>2. Immediately click the Grade button again | Only one grading interface opens; subsequent clicks do not create additional instances. | medium |
| TC-005 (input_edge) |  | Enter a very long description in the assignment metadata | User is on the Assignment page | 1. Attempt to view the full Description field<br>2. Verify if the description displays correctly or is truncated | The description displays correctly without truncation, or an indicator shows it has been truncated. | low |
| TC-006 (input_edge) |  | Enter special characters in the assignment description | User is on the Assignment page | 1. View the full Description field containing special characters<br>2. Verify the display of special characters | The description displays correctly with special characters without any errors. | low |

---

## Assignment Submissions

Total: **11** (positive: 4, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View student submission records | User logged in as <Role> | 1. Navigate to the Submissions view | Submission records displayed | high |
| TC-002 | WF-002 | Open grading workflow for a student | User logged in as <Role>, Submission records displayed | 1. Click the action menu for a specific student<br>2. Select 'Open Grading Workflow' from the menu | Grading workflow opened for selected student | high |
| TC-003 | WF-003 | Enable Quick grading mode | User logged in as <Role>, Submission records displayed | 1. Click the 'Enable Quick Grading' button | Quick grading mode activated | medium |
| TC-004 | WF-004 | Inline grade entry in Quick grading mode | User logged in as <Role>, Quick grading mode activated | 1. Enter a grade in the inline grading field for a specific student<br>2. Click 'Submit' | Grade submitted successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to view student submission records without authentication |  | 1. Navigate to the Submissions view without logging in | User is redirected to the login page | high |
| TC-006 | WF-002 | Attempt to open grading workflow for a student without proper role | User does not have grading permissions | 1. Click on the action menu for a student submission<br>2. Select 'Open Grading Workflow' | Action is blocked; user receives an error message indicating insufficient permissions | high |
| TC-007 | WF-003 | Attempt to enable Quick grading mode without proper role | User does not have permission to enable Quick grading | 1. Click on 'Enable Quick Grading' button | Action is blocked; user receives an error message indicating insufficient permissions | high |
| TC-008 | WF-004 | Attempt to submit grade in Quick grading mode without proper role | User does not have grading permissions | 1. Enable Quick grading mode<br>2. Enter a grade for a student<br>3. Click 'Submit Grade' | Action is blocked; user receives an error message indicating insufficient permissions | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (input_edge) |  | Enter a very long student name in the search filter | User is on the Submissions view | 1. Enter a string of 200+ characters in the student name search filter<br>2. Click the search button | Search results display, indicating whether the long name is accepted or truncated | low |
| TC-010 (input_edge) |  | Enter special characters in the search filter | User is on the Submissions view | 1. Enter a string with special characters (e.g., @#$%^&*) in the student name search filter<br>2. Click the search button | Search results display or an error message indicating invalid characters | low |
| TC-011 (input_edge) |  | Enter a student name with leading and trailing whitespace in the search filter | User is on the Submissions view | 1. Enter '   John Doe   ' in the student name search filter<br>2. Click the search button | Search results display with 'John Doe' shown without leading/trailing spaces | low |

---

## Gradebook — Grader Report

Total: **13** (positive: 8, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Switch to Grader report | User logged in as <role> | 1. Select 'Grader report' from the report-type selector dropdown | Grader report displayed | high |
| TC-002 | WF-002 | Switch to User report | User logged in as <role> | 1. Select 'User report' from the report-type selector dropdown | User report displayed | high |
| TC-003 | WF-003 | Switch to Overview report | User logged in as <role> | 1. Select 'Overview report' from the report-type selector dropdown | Overview report displayed | high |
| TC-004 | WF-004 | Search by student name | User logged in as <role> | 1. Enter <student name> in the search field<br>2. Click the search button | Filtered results displayed | medium |
| TC-005 | WF-005 | Filter by group | User logged in as <role> | 1. Select <group> from the group filter dropdown<br>2. Click the apply filter button | Filtered results displayed | medium |
| TC-006 | WF-006 | Edit grade settings for an activity | User logged in as <role>, Edit mode is enabled | 1. Click the action menu on the activity column header<br>2. Select 'Edit grade settings'<br>3. Modify the grade settings as needed<br>4. Click 'Save' | Grade settings updated | medium |
| TC-007 | WF-007 | Edit individual grade entry | User logged in as <role>, Edit mode is enabled | 1. Click the three-dot menu on the specific grade cell<br>2. Select 'Edit grade entry'<br>3. Enter <new grade> in the grade entry field<br>4. Click 'Save' | Grade entry updated | medium |
| TC-008 | WF-008 | Save changes in Edit mode | User logged in as <role>, Edit mode is enabled | 1. Make changes to the grade cells<br>2. Click 'Save changes' | Changes saved successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to save changes with grades outside the configured range | Edit mode is enabled | 1. Enter a grade value outside the configured grade range in any grade cell<br>2. Click 'Save changes' | Inline validation error appears on the grade cell indicating the value is outside the configured range; changes are not saved | high |
| TC-010 |  | Attempt to switch to the Grader report without proper role | User is not authorized to access the Grader report | 1. Attempt to switch to Grader report | Access is denied; user remains on the current report | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long student name in the search field |  | 1. Navigate to the Gradebook Grader report<br>2. Enter a string of 200+ characters in the student name search field | Search field accepts the input; results may be truncated or an error is shown indicating input length limit | low |
| TC-012 (input_edge) |  | Enter special characters in the search field |  | 1. Navigate to the Gradebook Grader report<br>2. Enter special characters (e.g., !@#$%^&*) in the student name search field | Search field accepts the input; results may be filtered or an error is shown indicating invalid characters | low |
| TC-013 (input_edge) |  | Enter a student name with leading and trailing whitespace |  | 1. Navigate to the Gradebook Grader report<br>2. Enter '   John Doe   ' in the student name search field | Leading/trailing whitespace is trimmed; search results display correctly without extra spaces | low |

---

## Profile

Total: **21** (positive: 7, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View User Details and Edit Profile | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on the 'Edit profile' link | User can edit their profile | high |
| TC-002 | WF-002 | View Privacy and Policies | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on the 'Data retention summary' link | User views data retention summary | high |
| TC-003 | WF-003 | View Course Details | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on a course profile link | User views associated course profiles | high |
| TC-004 | WF-004 | View Miscellaneous Links | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on a Blog entry link | User views blog entries | high |
| TC-005 | WF-005 | View Reports | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on the 'Browser sessions' link | User views browser sessions | high |
| TC-006 | WF-006 | View Login Activity | User logged in as <Teacher> | 1. Navigate to the Profile page | User views login activity | high |
| TC-007 | WF-007 | Send Message | User logged in as <Teacher> | 1. Navigate to the Profile page<br>2. Click on the 'Message' button | User sends a message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Unauthenticated user attempts to view user details |  | 1. Attempt to access the Profile page without logging in | User is redirected to the login page | high |
| TC-009 | WF-002 | Unauthenticated user attempts to view privacy and policies |  | 1. Attempt to access the Data retention summary link without logging in | User is redirected to the login page | high |
| TC-010 | WF-003 | Unauthenticated user attempts to view course details |  | 1. Attempt to access the Course profile link without logging in | User is redirected to the login page | high |
| TC-011 | WF-004 | Unauthenticated user attempts to view miscellaneous links |  | 1. Attempt to access the Blog entry link without logging in | User is redirected to the login page | high |
| TC-012 | WF-005 | Unauthenticated user attempts to view reports |  | 1. Attempt to access the Browser sessions link without logging in | User is redirected to the login page | high |
| TC-013 | WF-006 | Unauthenticated user attempts to view login activity |  | 1. Attempt to access the First and Last access information without logging in | User is redirected to the login page | high |
| TC-014 | WF-007 | Unauthenticated user attempts to send a message |  | 1. Attempt to click the Message button without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (interaction_edge) | WF-001 | Rapidly click 'Edit profile' after viewing user details | User is on the Profile page | 1. Click on 'Edit profile' link<br>2. Immediately click 'Edit profile' link again | Second click is ignored; user remains on the edit profile page without errors. | medium |
| TC-016 (interaction_edge) | WF-002 | Rapidly click 'Data retention summary' after viewing privacy policies | User is on the Profile page | 1. Click on 'Data retention summary' link<br>2. Immediately click on 'Data retention summary' link again | Second click is ignored; user remains on the data retention summary page without errors. | medium |
| TC-017 (interaction_edge) | WF-003 | Rapidly click a course profile link after viewing course details | User is on the Profile page | 1. Click on a course profile link<br>2. Immediately click on the same course profile link again | Second click is ignored; user remains on the course profile page without errors. | medium |
| TC-018 (interaction_edge) | WF-004 | Rapidly click a blog entry link after viewing miscellaneous links | User is on the Profile page | 1. Click on a blog entry link<br>2. Immediately click on the same blog entry link again | Second click is ignored; user remains on the blog entry page without errors. | medium |
| TC-019 (interaction_edge) | WF-005 | Rapidly click 'Browser sessions' after viewing reports | User is on the Profile page | 1. Click on 'Browser sessions' link<br>2. Immediately click on 'Browser sessions' link again | Second click is ignored; user remains on the browser sessions page without errors. | medium |
| TC-020 (interaction_edge) | WF-006 | Rapidly click 'First access' after viewing login activity | User is on the Profile page | 1. Click on 'First access' link<br>2. Immediately click on 'First access' link again | Second click is ignored; user remains on the login activity page without errors. | medium |
| TC-021 (interaction_edge) | WF-007 | Rapidly click 'Message' button after sending a message | User is on the Profile page | 1. Click on 'Message' button<br>2. Immediately click on 'Message' button again | Second click is ignored; user remains on the message confirmation without errors. | medium |

---

## Profile Edit

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid data | User logged in as <Role> | 1. Open the Edit profile form<br>2. Enter <valid first name> in the First name field<br>3. Enter <valid last name> in the Last name field<br>4. Enter <valid email> in the Email address field<br>5. Select <email visibility option> from the Email visibility dropdown<br>6. Enter <valid MoodleNet profile ID> in the MoodleNet profile ID field<br>7. Enter <valid city/town> in the City/town field<br>8. Select <valid country> from the Country dropdown<br>9. Select <valid timezone> from the Timezone dropdown<br>10. Enter <description> in the Description field<br>11. Upload a new picture<br>12. Enter <picture description> in the Picture description field<br>13. Click Update profile | Profile updated; profile page refreshed | high |
| TC-002 | WF-002 | Cancel profile edit | User logged in as <Role> | 1. Open the Edit profile form<br>2. Click Cancel | Exited without changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First name field blank and submit |  | 1. Leave the First name field blank<br>2. Fill all other required fields<br>3. Click Update profile | Inline validation error appears on the First name field indicating it is required | high |
| TC-004 |  | Leave the Last name field blank and submit |  | 1. Leave the Last name field blank<br>2. Fill all other required fields<br>3. Click Update profile | Inline validation error appears on the Last name field indicating it is required | high |
| TC-005 |  | Leave the Email address field blank and submit |  | 1. Leave the Email address field blank<br>2. Fill all other required fields<br>3. Click Update profile | Inline validation error appears on the Email address field indicating it is required | high |
| TC-006 |  | Submit the form with all required fields empty |  | 1. Leave the First name field blank<br>2. Leave the Last name field blank<br>3. Leave the Email address field blank<br>4. Click Update profile | Form does not submit; errors shown on First name, Last name, and Email address fields indicating they are required | high |
| TC-007 |  | Upload an invalid file type for the user picture |  | 1. Upload a file with an invalid format for the user picture<br>2. Fill all other required fields<br>3. Click Update profile | Inline validation error appears on the user picture upload area indicating invalid file type | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long description in the Description field |  | 1. Expand the General section<br>2. Enter a string of 200+ characters in the Description field | The Description field accepts the input and displays it correctly in the profile detail page. | low |
| TC-009 (input_edge) |  | Enter special characters in the First name field |  | 1. Expand the General section<br>2. Enter special characters (e.g., @#$%^&*) in the First name field | The First name field displays an error indicating invalid characters. | low |
| TC-010 (input_edge) |  | Enter a value with leading and trailing whitespace in the Last name field |  | 1. Expand the General section<br>2. Enter '  Smith  ' in the Last name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has 'Smith'. | low |
| TC-011 (input_edge) |  | Upload a file that exceeds the maximum size limit for the user picture |  | 1. Drag and drop a file larger than the allowed size into the new picture upload area | A visible error is shown indicating the file exceeds the size limit. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <role> | 1. Click on the Log out button | Redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access protected page after logout | User is not logged in | 1. Attempt to access a protected page | User is redirected to the login page; access to the protected page is denied. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after logout | User is logged in | 1. Click Log out<br>2. Immediately press the browser back button | User is redirected to the login page without the session being active again. | medium |
| TC-004 (input_edge) |  | Attempt to access protected page after logout | User is logged out | 1. Navigate to a protected page directly | User is redirected to the login page and prompted for re-authentication. | medium |

---
