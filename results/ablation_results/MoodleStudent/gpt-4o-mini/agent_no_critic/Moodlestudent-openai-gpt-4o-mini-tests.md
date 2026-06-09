# Test Cases — Moodlestudent

Generated: 2026-06-09T12:06:45.047776Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 8 | 52 | 22 | 13 | 17 | 15 | 19 | 13 |

## Login

Total: **0** (positive: 0, negative: 0, edge: 0)

---

## Dashboard

Total: **15** (positive: 10, negative: 5, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display upcoming activities in the Timeline block | User logged in as <User>, No specific preconditions | 1. Select 'Next 7 days' from the Time Range dropdown | The Timeline block displays upcoming activities for the next 7 days | high |
| TC-002 |  | Create a new calendar event | User logged in as <User>, No specific preconditions | 1. Click the 'New Event' button in the Calendar block | A personal calendar entry is created | high |
| TC-003 |  | Navigate to the previous month in the Calendar block | User logged in as <User>, No specific preconditions | 1. Click the 'Previous Month' button in the Calendar block | The Calendar block displays the previous month | medium |
| TC-004 |  | Navigate to the next month in the Calendar block | User logged in as <User>, No specific preconditions | 1. Click the 'Next Month' button in the Calendar block | The Calendar block displays the next month | medium |
| TC-005 |  | Open the full calendar view | User logged in as <User>, No specific preconditions | 1. Click the 'Full calendar' link | The dedicated calendar view opens | medium |
| TC-006 |  | Open the calendar data management | User logged in as <User>, No specific preconditions | 1. Click the 'Import or export calendars' link | The calendar data management opens | medium |
| TC-007 |  | Reset the page to default in Edit mode | User logged in as <User>, Edit mode is toggled on | 1. Click the 'Reset Page' button | The page resets to default | medium |
| TC-008 |  | Open the block types listing in Edit mode | User logged in as <User>, Edit mode is toggled on | 1. Click the 'Add Block' button | A page listing all available block types opens | medium |
| TC-009 |  | Check the visibility of move icons in existing blocks in Edit mode | User logged in as <User>, Edit mode is toggled on | 1. Observe the existing blocks | Each existing block shows a move icon | low |
| TC-010 |  | Check the visibility of three-dot menus in existing blocks in Edit mode | User logged in as <User>, Edit mode is toggled on | 1. Observe the existing blocks | Each existing block shows a three-dot menu for configure, move, and delete actions | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Attempt to create a new event without filling required fields | Edit mode is toggled on | 1. Click on the 'New Event' button | Form does not submit; no calendar entry is created; error shown on required fields |  |
| TC-012 |  | Attempt to navigate to the previous month in read-only mode | Edit mode is toggled off | 1. Click on the 'Previous Month' button | No navigation occurs; current month remains displayed |  |
| TC-013 |  | Attempt to reset the page without being in edit mode | Edit mode is toggled off | 1. Click on the 'Reset Page' button | No action occurs; page remains unchanged |  |
| TC-014 |  | Attempt to access 'Full calendar' link without authentication | User is not authenticated | 1. Click on the 'Full calendar' link | User is redirected to the login page |  |
| TC-015 |  | Attempt to access 'Import or export calendars' link without authentication | User is not authenticated | 1. Click on the 'Import or export calendars' link | User is redirected to the login page |  |

---

## Course Page

Total: **6** (positive: 0, negative: 2, edge: 4)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Attempt to enable Edit mode on the course page |  | 1. Navigate to the Course Page<br>2. Attempt to click on the Edit mode button | User is blocked from enabling Edit mode; no changes are made to the course content | high |
| TC-002 |  | Attempt to access a non-existent activity or resource link |  | 1. Navigate to the Course Page<br>2. Click on a link that does not exist | Page displays an error indicating the resource is not found; no navigation occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Attempt to collapse all sections after navigating away from the page | User is on the Course Page and has expanded sections | 1. Click on a section to expand it<br>2. Navigate away from the Course Page<br>3. Return to the Course Page | All sections remain in their last expanded state; 'Collapse all' link is still visible and clickable. | low |
| TC-004 (interaction_edge) |  | Rapidly click the 'Collapse all' link multiple times | User is on the Course Page with sections expanded | 1. Click the 'Collapse all' link<br>2. Immediately click the 'Collapse all' link again | 'Collapse all' action is processed once; all sections are collapsed and the link remains functional. | low |
| TC-005 (input_edge) |  | Check behavior when navigating to a section with long section names | User is on the Course Page | 1. Navigate to Section 1 with a long name that exceeds typical length | Section name is fully displayed without truncation or overflow issues. | low |
| TC-006 (input_edge) |  | Check behavior when navigating to a section with special characters in section names | User is on the Course Page | 1. Navigate to Section 2 with special characters in the name | Section name is displayed correctly without errors or encoding issues. | low |

---

## Grades

Total: **3** (positive: 3, negative: 0, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display student's own grades in the grade table | User logged in as <Student> | 1. Navigate to the Grades page | The Grades table displays the student's grades with the columns: Grade item, Calculated weight, Grade, Range, Percentage, Feedback, and Contribution to course total. | high |
| TC-002 |  | Collapse and expand grade items in the grade table | User logged in as <Student>, Grades page is open | 1. Click on a Grade item header to collapse it<br>2. Click on the same Grade item header to expand it | The Grade item collapses and expands correctly, showing or hiding the graded activities beneath it. | medium |
| TC-003 |  | Verify the aggregation course total is displayed | User logged in as <Student>, Grades page is open | 1. Observe the bottom of the Grades table | The 'AGGREGATION Course total' row displays the cumulative grade across all weighted items. | high |

---

## Assignment

Total: **9** (positive: 5, negative: 0, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open submission form | User logged in as <Student> | 1. Click the Add submission button | The submission form opens | high |
| TC-002 | WF-002 | Submit with Online Text Editor | User logged in as <Student>, Submission form is open | 1. Enter text in the Online Text Editor<br>2. Click Submit | Submission created | high |
| TC-003 | WF-003 | Submit with File Upload | User logged in as <Student>, Submission form is open | 1. Upload a valid file in the File Upload area<br>2. Click Submit | Submission created | high |
| TC-004 | WF-004 | View submission status | User logged in as <Student>, At least one submission has been made | 1. Click View on the Submission Status Section | Displays submission details | medium |
| TC-005 | WF-005 | Edit submission | User logged in as <Student>, Due date has not passed, Teacher permits resubmission, At least one submission has been made | 1. Click Edit on the Submission Status Section<br>2. Make changes in the submission form<br>3. Click Submit | Submission edited | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-003 | Upload a file at the maximum allowed size | File size limit is defined in the system | 1. Click on the 'Add submission' button<br>2. Upload a file that is exactly at the size limit<br>3. Click Submit | File upload succeeds; submission is created with the uploaded file | medium |
| TC-007 (boundary) | WF-003 | Upload a file exceeding the maximum allowed size | File size limit is defined in the system | 1. Click on the 'Add submission' button<br>2. Upload a file that is one byte over the size limit<br>3. Click Submit | Submission is blocked; an error is shown indicating the file exceeds the size limit | medium |
| TC-008 (input_edge) |  | Enter a very long text in the online text editor |  | 1. Click on the 'Add submission' button<br>2. Enter a string of 200+ characters in the Online Text Editor<br>3. Click Submit | Submission is accepted; the text is saved as entered without truncation | low |
| TC-009 (input_edge) |  | Enter special characters in the online text editor |  | 1. Click on the 'Add submission' button<br>2. Enter a string with special characters in the Online Text Editor<br>3. Click Submit | Submission is accepted; the text is saved as entered without errors | low |

---

## Activities

Total: **5** (positive: 0, negative: 1, edge: 4)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Attempt to navigate to an activity when no activities are present |  | 1. Ensure the Assignments section is displayed<br>2. Verify that no activities are listed in the Assignments section<br>3. Attempt to click on a non-existent activity link | No navigation occurs; the user remains on the Activities page with no error shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 (interaction_edge) |  | Rapid navigation after clicking an activity name | User is on the Activities page | 1. Click on an activity name in the Assignments section<br>2. Immediately press the back button in the browser | User is redirected to the Activities page without the activity name being pre-filled | medium |
| TC-003 (input_edge) |  | Long text in activity name | User is on the Activities page | 1. Enter a very long string (200+ characters) in the Name field of an activity | The input is either accepted or truncated with a visible indicator | low |
| TC-004 (input_edge) |  | Special characters in activity name | User is on the Activities page | 1. Enter a string with special characters (e.g., !@#$%^&*) in the Name field of an activity | The input is accepted or a specific error message is shown | low |
| TC-005 (input_edge) |  | Leading and trailing whitespace in activity name | User is on the Activities page | 1. Enter a string with leading and trailing spaces in the Name field of an activity | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Profile

Total: **14** (positive: 4, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update Profile with all required fields filled | User logged in as <Student>, Profile form is open | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email Address field<br>4. Click Update Profile | saves profile changes | high |
| TC-002 | WF-002 | Cancel profile editing | User logged in as <Student>, Profile form is open | 1. Click Cancel | exits without changes | medium |
| TC-003 | WF-003 | Open Profile Form from Profile Page | User logged in as <Student>, Profile page is displayed | 1. Click Edit Profile Link | Profile form is displayed | medium |
| TC-004 | WF-004 | Send Message from Profile Page | User logged in as <Student>, Profile page is displayed | 1. Click Message Button | Message sent successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to update profile with required fields left blank |  | 1. Click on the 'Edit Profile' link<br>2. Leave the 'First_Name' field blank<br>3. Leave the 'Last_Name' field blank<br>4. Leave the 'Email_Address' field blank<br>5. Click 'Update Profile' | Form does not submit; 'First_Name', 'Last_Name', and 'Email_Address' fields are highlighted with inline validation errors indicating they are required | high |
| TC-006 | WF-001 | Attempt to update profile with all required fields left blank |  | 1. Click on the 'Edit Profile' link<br>2. Leave all required fields blank<br>3. Click 'Update Profile' | Form does not submit; 'First_Name', 'Last_Name', and 'Email_Address' fields are highlighted with inline validation errors indicating they are required | high |
| TC-007 | WF-002 | Attempt to cancel profile editing without making changes |  | 1. Click on the 'Edit Profile' link<br>2. Click 'Cancel' | Exits without changes; profile remains unchanged | high |
| TC-008 | WF-003 | Attempt to open profile form without being authenticated |  | 1. Attempt to access the 'Edit Profile' link without logging in | Redirected to the login page | high |
| TC-009 | WF-004 | Attempt to send a message without being authenticated |  | 1. Attempt to click on the 'Message' button without logging in | Redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Fill all required fields with minimum valid data | User is on the Profile Form | 1. Enter minimum valid data in the First_Name field<br>2. Enter minimum valid data in the Last_Name field<br>3. Enter a valid email address in the Email_Address field<br>4. Click Update Profile | Profile changes are saved successfully; confirmation message displayed. | medium |
| TC-011 (boundary) | WF-001 | Attempt to submit profile with missing required fields | User is on the Profile Form | 1. Leave First_Name field empty<br>2. Leave Last_Name field empty<br>3. Leave Email_Address field empty<br>4. Click Update Profile | Form submission is blocked; inline errors displayed for First_Name, Last_Name, and Email_Address fields. | medium |
| TC-012 (input_edge) | WF-001 | Enter a long string in the Description field | User is on the Profile Form | 1. Enter a string longer than 200 characters in the Description field<br>2. Click Update Profile | Form submission is blocked; error message indicates the Description exceeds maximum length. | low |
| TC-013 (input_edge) | WF-001 | Enter special characters in the First_Name field | User is on the Profile Form | 1. Enter special characters in the First_Name field<br>2. Click Update Profile | Form submission is blocked; inline error indicates invalid characters in First_Name. | low |
| TC-014 (interaction_edge) | WF-004 | Rapidly click Send Message after sending a message | User is on the Profile Page | 1. Click Message_Button to send a message<br>2. Immediately click Message_Button again | Second click is ignored; user sees a message indicating the previous message is still being processed. | medium |

---

## Logout

Total: **0** (positive: 0, negative: 0, edge: 0)

---
