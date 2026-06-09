# Test Cases — Moodleteacher

Generated: 2026-06-09T11:52:55.680787Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 12 | 63 | 17 | 25 | 21 | 31 | 21 | 11 |

## Login

Total: **0** (positive: 0, negative: 0, edge: 0)

---

## Dashboard

Total: **0** (positive: 0, negative: 0, edge: 0)

---

## Dashboard — Edit Mode

Total: **6** (positive: 4, negative: 2, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Add a block page from Edit mode | User logged in as <User>, Edit mode is enabled | 1. Click '+ Add a block' button | opens Add a block page | high |
| TC-002 | WF-001 | Persist layout changes using Reset Page button | User logged in as <User>, Edit mode is enabled | 1. Click 'Reset_Page' button | persists layout changes per user | medium |
| TC-003 | WF-001 | Return to Dashboard from Add a block page | User logged in as <User>, Edit mode is enabled, Add a block page is open | 1. Click 'Cancel_Link' | returns to Dashboard | medium |
| TC-004 | WF-001 | Verify existing block actions are available | User logged in as <User>, Edit mode is enabled | 1. Observe existing blocks on the Dashboard | Each existing block shows a move icon and a three-dot options menu for configure, move, and delete actions | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to add a block without selecting a block type |  | 1. Click on '+ Add a block'<br>2. Leave the Block Types dropdown unselected<br>3. Click Submit | Form does not submit; Block Types field is highlighted with an error indicating selection is required | high |
| TC-006 |  | Attempt to reset the page without any changes made |  | 1. Click on 'Reset page to default' | No changes are made; the layout remains unchanged | medium |

---

## My Courses

Total: **0** (positive: 0, negative: 0, edge: 0)

---

## Course Page

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Collapse all sections | User logged in as <Student> | 1. Click 'Collapse all' link | All sections are collapsed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to collapse all sections when no sections are expanded |  | 1. Ensure all sections are collapsed<br>2. Click on the 'Collapse all' link | No sections collapse; the state remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Collapse all sections after expanding one | User is on the Course Page, At least one section is expanded | 1. Click to expand 'Section 1'<br>2. Click 'Collapse all' link | 'Section 1' collapses; all sections are collapsed | medium |
| TC-004 (interaction_edge) |  | Rapidly expand and collapse sections | User is on the Course Page | 1. Click to expand 'Section 1'<br>2. Immediately click to collapse 'Section 1'<br>3. Click to expand 'Section 2'<br>4. Immediately click to collapse 'Section 2' | Both sections can be expanded and collapsed without errors; their states reflect the last action | medium |

---

## Course Settings

Total: **10** (positive: 0, negative: 4, edge: 6)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Leave the Course Full Name field blank |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-002 |  | Leave the Course Short Name field blank |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-003 |  | Leave the Course Category field blank |  | 1. Leave the Course Category field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-004 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Save and display | Form does not submit; Course Full Name, Course Short Name, and Course Category fields display errors indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (boundary) |  | Enter exactly 1 character in Course Full Name |  | 1. Enter 'A' in the Course Full Name field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Form submits successfully; entity is created with the Course Full Name set to 'A' | medium |
| TC-006 (boundary) |  | Enter exactly 200 characters in Course Summary |  | 1. Enter a string of 200 characters in the Course Summary field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Form submits successfully; Course Summary is saved with 200 characters | medium |
| TC-007 (input_edge) |  | Enter a very long string in Course Short Name |  | 1. Enter a string of 300 characters in the Course Short Name field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Form submits successfully; Course Short Name is saved with 300 characters | low |
| TC-008 (input_edge) |  | Enter special characters in Course ID Number |  | 1. Enter '@#$%^&*()' in the Course ID Number field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Form submits successfully; Course ID Number is saved with special characters | low |
| TC-009 (data_edge) |  | Upload a file exactly at the maximum upload size limit |  | 1. Upload a file with the maximum allowed size in the Course Image Upload field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Form submits successfully; file is uploaded without errors | medium |
| TC-010 (data_edge) |  | Upload a file exceeding the maximum upload size limit |  | 1. Upload a file that is one byte over the maximum allowed size in the Course Image Upload field<br>2. Fill all other required fields with valid data<br>3. Click Save and display | Upload is blocked; error message displayed indicating the file exceeds the maximum upload size | medium |

---

## Assignment — Teacher View

Total: **9** (positive: 6, negative: 0, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open grading interface for individual students | User logged in as <Teacher>, Assignment is displayed with metadata | 1. Click the 'Grade' button | opens grading interface for individual students | high |
| TC-002 |  | Navigate to Assignment tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the 'Assignment' tab | The Assignment tab is active and displayed | medium |
| TC-003 |  | Navigate to Settings tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the 'Settings' tab | The Settings tab is active and displayed | medium |
| TC-004 |  | Navigate to Submissions tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the 'Submissions' tab | The Submissions tab is active and displayed | medium |
| TC-005 |  | Navigate to Advanced grading tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the 'Advanced grading' tab | The Advanced grading tab is active and displayed | medium |
| TC-006 |  | Navigate to More tab | User logged in as <Teacher>, Assignment page is open | 1. Click on the 'More' tab | The More tab is active and displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully submitted an assignment | 1. Click the 'Grade' button to open the grading interface<br>2. Press the browser back button | User is redirected to the assignment page without the grading interface being pre-filled | medium |
| TC-008 (input_edge) |  | Long description input | User is on the Assignment page | 1. Enter a description with 200+ characters in the description field | The description is accepted and displayed correctly without truncation | low |
| TC-009 (input_edge) |  | Special characters in description | User is on the Assignment page | 1. Enter a description containing special characters and emojis | The description is accepted and displayed correctly without errors | low |

---

## Assignment Submissions

Total: **18** (positive: 4, negative: 11, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Filter submissions by student name | User logged in as <Teacher>, Submissions table is visible | 1. Enter <valid student name> in the Student Name search field<br>2. Click the Search button | The Submissions Table displays only rows matching <valid student name>; unrelated rows are no longer visible | high |
| TC-002 |  | Filter submissions by submission status | User logged in as <Teacher>, Submissions table is visible | 1. Select 'Submitted for grading' from the Submission Status Filter dropdown<br>2. Click the Apply Filter button | The Submissions Table displays only rows with the status 'Submitted for grading'; unrelated rows are no longer visible | high |
| TC-003 |  | Filter submissions by grading status | User logged in as <Teacher>, Submissions table is visible | 1. Select 'Graded' from the Grading Status Filter dropdown<br>2. Click the Apply Filter button | The Submissions Table displays only rows with the grading status 'Graded'; unrelated rows are no longer visible | high |
| TC-004 |  | Open grading workflow for a submission | User logged in as <Teacher>, Submissions table is visible | 1. Click the action menu for a submission row<br>2. Select 'Open Grading Workflow' | The grading workflow for the selected student submission is opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Student Identity field blank and submit |  | 1. Leave the Student Identity field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Student Identity field indicating it is required | high |
| TC-006 |  | Leave the Submission Status field blank and submit |  | 1. Leave the Submission Status field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submission Status field indicating it is required | high |
| TC-007 |  | Leave the Grading Status field blank and submit |  | 1. Leave the Grading Status field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Grading Status field indicating it is required | high |
| TC-008 |  | Leave the Submission Date Time field blank and submit |  | 1. Leave the Submission Date Time field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submission Date Time field indicating it is required | high |
| TC-009 |  | Leave the Time Since Submission field blank and submit |  | 1. Leave the Time Since Submission field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Time Since Submission field indicating it is required | high |
| TC-010 |  | Leave the Online Text Preview field blank and submit |  | 1. Leave the Online Text Preview field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Online Text Preview field indicating it is required | high |
| TC-011 |  | Leave the File Submission Links field blank and submit |  | 1. Leave the File Submission Links field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the File Submission Links field indicating it is required | high |
| TC-012 |  | Leave the Submission Comments field blank and submit |  | 1. Leave the Submission Comments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submission Comments field indicating it is required | high |
| TC-013 |  | Leave the Feedback Comments field blank and submit |  | 1. Leave the Feedback Comments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Feedback Comments field indicating it is required | high |
| TC-014 |  | Leave the Feedback Files field blank and submit |  | 1. Leave the Feedback Files field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Feedback Files field indicating it is required | high |
| TC-015 |  | Leave the Final Grade field blank and submit |  | 1. Leave the Final Grade field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Final Grade field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (input_edge) |  | Enter a very long string in the Student Name field |  | 1. Navigate to the Search Filter Controls<br>2. Enter a string of 200+ characters in the Student Name field | The input is accepted or truncated with a visible indicator | low |
| TC-017 (input_edge) |  | Enter special characters in the Submission Comments field |  | 1. Navigate to the Submissions_Table<br>2. Enter special characters in the Submission Comments field | The input is accepted or a specific error is shown | low |
| TC-018 (input_edge) |  | Enter a value with leading/trailing whitespace in the Submission Comments field |  | 1. Navigate to the Submissions_Table<br>2. Enter '   Sample comment   ' in the Submission Comments field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Gradebook — Grader Report

Total: **6** (positive: 0, negative: 2, edge: 4)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Attempt to save changes with grades outside the configured range | Edit mode is enabled | 1. Enter a grade value outside the configured grade range in any editable grade cell<br>2. Click on 'Save changes' | Inline validation error appears indicating 'Values must be within configured grade range'; changes are not saved | high |
| TC-002 |  | Attempt to save changes without entering any grades | Edit mode is enabled | 1. Leave all grade cells blank<br>2. Click on 'Save changes' | Inline validation error appears indicating 'Values must be within configured grade range'; changes are not saved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (boundary) |  | Test grade value at lower boundary | User is in edit mode with grade range configured | 1. Enter the minimum allowed grade value in the grade cell<br>2. Click 'Save changes' | Changes are saved successfully; grade cell reflects the minimum allowed value | medium |
| TC-004 (boundary) |  | Test grade value just below lower boundary | User is in edit mode with grade range configured | 1. Enter a grade value one unit below the minimum allowed in the grade cell<br>2. Click 'Save changes' | Inline error displayed indicating the value is outside the configured grade range; changes are not saved | medium |
| TC-005 (boundary) |  | Test grade value at upper boundary | User is in edit mode with grade range configured | 1. Enter the maximum allowed grade value in the grade cell<br>2. Click 'Save changes' | Changes are saved successfully; grade cell reflects the maximum allowed value | medium |
| TC-006 (boundary) |  | Test grade value just above upper boundary | User is in edit mode with grade range configured | 1. Enter a grade value one unit above the maximum allowed in the grade cell<br>2. Click 'Save changes' | Inline error displayed indicating the value is outside the configured grade range; changes are not saved | medium |

---

## Profile

Total: **3** (positive: 0, negative: 0, edge: 3)

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 (input_edge) |  | Enter a long string in the Email Address field |  | 1. Navigate to the Profile page<br>2. Enter a string of 200+ characters in the Email Address field | Email Address field accepts the input and displays the full string | low |
| TC-002 (input_edge) |  | Enter special characters in the Visibility Note field |  | 1. Navigate to the Profile page<br>2. Enter special characters (e.g., @#$%^&*) in the Visibility Note field | Visibility Note field accepts the input and displays the special characters | low |
| TC-003 (input_edge) |  | Enter leading and trailing whitespace in the Timezone field |  | 1. Navigate to the Profile page<br>2. Enter '   GMT+0   ' in the Timezone field | Timezone field displays 'GMT+0' without leading or trailing spaces | low |

---

## Profile Edit

Total: **7** (positive: 2, negative: 5, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid information | User logged in as <User> | 1. Open the Edit Profile form<br>2. Expand all sections<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid email> in the Email Address field<br>6. Upload a <valid image file> in the New Picture Upload area<br>7. Click Update Profile | The profile page refreshes | high |
| TC-002 | WF-001 | Cancel profile edit without changes | User logged in as <User> | 1. Open the Edit Profile form<br>2. Expand all sections<br>3. Click Cancel | The user exits without making changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Upload a file that does not meet the drag-and-drop constraints |  | 1. Select a file that does not meet the upload constraints<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form does not submit; error shown indicating upload constraints are not met | high |
| TC-007 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Form does not submit; Inline validation errors appear on First_Name, Last_Name, and Email_Address fields indicating they are required | high |

---

## Logout

Total: **0** (positive: 0, negative: 0, edge: 0)

---
