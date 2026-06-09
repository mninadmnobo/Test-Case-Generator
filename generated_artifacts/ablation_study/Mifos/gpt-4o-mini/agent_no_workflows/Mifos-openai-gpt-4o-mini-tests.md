# Test Cases — Mifos

Generated: 2026-06-09T09:36:59.363063Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 519 | 142 | 207 | 170 | 239 | 207 | 68 |

## Login

Total: **11** (positive: 1, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with a valid email<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both Username and Password fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Form does not submit; error shown on Username and Password fields indicating they are required | high |
| TC-005 |  | Submit with invalid credentials |  | 1. Fill the Username field with an invalid email format<br>2. Fill the Password field with an invalid password<br>3. Click Login | Error message displayed: 'invalid credentials' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) |  | Enter valid email format in Username field |  | 1. Enter a valid email format in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Redirects to Dashboard | medium |
| TC-007 (boundary) |  | Enter invalid email format in Username field |  | 1. Enter an invalid email format in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Displays error message 'invalid credentials' | medium |
| TC-008 (input_edge) |  | Enter a very long string in Username field |  | 1. Enter a string longer than 254 characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Displays error indicating the value is too long | low |
| TC-009 (input_edge) |  | Enter special characters in Username field |  | 1. Enter special characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Displays error message 'invalid credentials' | low |
| TC-010 (input_edge) |  | Enter whitespace in Username field |  | 1. Enter leading and trailing whitespace in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Username is trimmed; redirects to Dashboard if credentials are valid | low |
| TC-011 (input_edge) |  | Leave required fields empty and click Login |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Login | Displays inline validation messages for empty required fields | medium |

---

## Home Page

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify welcome message is displayed | User logged in as <User> | 1. Observe the Home page | The welcome card displays the message 'Welcome, mifos!' | high |
| TC-002 |  | Verify Search Activity input field is present | User logged in as <User> | 1. Observe the Home page | The 'Search Activity' input field is visible | medium |
| TC-003 |  | Click Dashboard button and verify redirect | User logged in as <User> | 1. Click the 'Dashboard' button | redirects to dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to access the Home Page without authentication |  | 1. Navigate to the Home Page URL | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the Search Activity input |  | 1. Enter a string of 200+ characters in the Search Activity Input field | Search Activity Input field accepts the input without truncation or shows a visible indicator if rejected | low |
| TC-006 (input_edge) |  | Enter special characters in the Search Activity input |  | 1. Enter special characters (e.g., @#$%^&*) in the Search Activity Input field | Search Activity Input field accepts the input or shows a specific error indicating invalid characters | low |
| TC-007 (input_edge) |  | Enter a value with leading and trailing whitespace in the Search Activity input |  | 1. Enter '   search term   ' in the Search Activity Input field | Leading/trailing whitespace is trimmed; saved value shown in the Search Activity Input field has no extra spaces | low |

---

## Dashboard

Total: **8** (positive: 4, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access the Dashboard | User logged in as <User Role> | 1. Click the Dashboard button on the Home page | User navigates to Dashboard | high |
| TC-002 |  | Verify Search Activity field is present | User logged in as <User Role>, User is on the Dashboard | 1. Observe the Dashboard page | The Search Activity field is visible at the top of the Dashboard | medium |
| TC-003 |  | Verify Client Trends chart is displayed | User logged in as <User Role>, User is on the Dashboard | 1. Observe the Dashboard page | The Client Trends chart is visible on the Dashboard | medium |
| TC-004 |  | Verify summary cards are displayed | User logged in as <User Role>, User is on the Dashboard | 1. Observe the Dashboard page | The summary cards for 'Amount Pending / Disbursed' and 'Amount Collected' are visible on the Dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to access Dashboard without authentication |  | 1. Navigate to the Dashboard URL without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter long text in Search Activity field |  | 1. Enter a string of 200+ characters in the Search Activity field | Search Activity field displays an error indicating the input is too long or is truncated to the maximum allowed length | low |
| TC-007 (input_edge) |  | Enter special characters in Search Activity field |  | 1. Enter a string containing special characters (e.g., @#$%^&*!) in the Search Activity field | Search Activity field accepts the input and displays it correctly, or shows a specific error message | low |
| TC-008 (input_edge) |  | Enter value with leading/trailing whitespace in Search Activity field |  | 1. Enter a string with leading and trailing spaces in the Search Activity field | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Global Search

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field | User logged in as <User> | 1. Click on the search icon in the top toolbar | The search input field is opened | high |
| TC-002 | WF-002 | Search for existing entity | User logged in as <User>, Search input field is opened | 1. Enter <partial name> in the search input field | Searches across Clients, Groups, Loans, and Savings accounts | high |
| TC-003 | WF-003 | Display search results for matching entities | User logged in as <User>, Search input field is opened, Enter <partial name> that matches existing entities | 1. Enter <partial name> in the search input field | Matching results appear in a dropdown grouped by entity type, showing entity name, identifier, and status | high |
| TC-004 | WF-004 | Display no results message | User logged in as <User>, Search input field is opened | 1. Enter <non-matching term> in the search input field | The message 'No results found' is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user attempts to access search |  | 1. Attempt to click on the Search Icon | User is redirected to the login page | high |
| TC-006 |  | Search with empty input | user must be logged in | 1. Click on the Search Icon<br>2. Leave the Search Input blank<br>3. Click the search button or press enter | No results found message is displayed | high |
| TC-007 |  | Search with invalid input format | user must be logged in | 1. Click on the Search Icon<br>2. Enter <invalid input format> in the Search Input<br>3. Click the search button or press enter | No results found message is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long search term | User is logged in | 1. Click on the Search Icon<br>2. Enter a string of 200+ characters in the Search Input | Search Input displays the entered long string; system processes the input without error | low |
| TC-009 (input_edge) |  | Enter special characters in the search input | User is logged in | 1. Click on the Search Icon<br>2. Enter a string with special characters (e.g., @#$%^&*) in the Search Input | Search Input displays the entered string with special characters; system processes the input without error | low |
| TC-010 (input_edge) |  | Enter leading and trailing whitespace in the search input | User is logged in | 1. Click on the Search Icon<br>2. Enter a string with leading and trailing spaces in the Search Input | Leading and trailing whitespace is trimmed; saved value shown in the Search Input has no extra spaces | low |
| TC-011 (state_edge) |  | Search with no matches found | User is logged in | 1. Click on the Search Icon<br>2. Enter a term that does not match any records in the Search Input | No Results Message displays 'No results found' | medium |

---

## Client Management

Total: **21** (positive: 5, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Bulk Import page from Clients page | User logged in as <Role> | 1. Click on 'Import Client' button | opens Bulk Import page | high |
| TC-002 | WF-002 | Create a new client successfully | User logged in as <Role> | 1. Click on 'Create Client' button<br>2. Fill in the Office field with <valid office><br>3. Fill in the First Name field with <valid first name><br>4. Fill in the Last Name field with <valid last name><br>5. Fill in the Submitted On field with <valid date><br>6. Click 'Submit' | creates client in Pending status | high |
| TC-003 | WF-003 | View client details from Clients page | User logged in as <Role>, At least one client exists | 1. Click on the Name link of the first client in the data table | Client Detail page displays the client name, account number, status badge, activation date, and office | medium |
| TC-004 | WF-004 | Search for a client by name | User logged in as <Role>, At least one client exists | 1. Enter <valid client name> in the search field<br>2. Press Enter | Only results matching <valid client name> are shown; unrelated items are no longer visible | medium |
| TC-005 | WF-005 | Filter clients by status | User logged in as <Role>, At least one client exists with status Pending | 1. Select 'Pending' from the status filter<br>2. Click 'Apply Filter' | Only clients with status 'Pending' are shown; unrelated items are no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Office field blank and submit the Create Client form |  | 1. Open the Create Client wizard<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 |  | Leave the First Name field blank and submit the Create Client form |  | 1. Open the Create Client wizard<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-008 |  | Leave the Last Name field blank and submit the Create Client form |  | 1. Open the Create Client wizard<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-009 |  | Submit the Create Client form with all required fields empty |  | 1. Open the Create Client wizard<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; client is not created; error shown on Office, First Name, and Last Name fields | high |
| TC-010 |  | Upload a non-Excel file in the Bulk Import page |  | 1. Open the Bulk Import page<br>2. Upload a file that is not an Excel format | Inline validation error appears indicating the file must be an Excel format | medium |
| TC-011 |  | Attempt to create a client with a duplicate External ID |  | 1. Open the Create Client wizard<br>2. Fill all required fields with valid data<br>3. Enter an existing External ID in the External ID field<br>4. Click Submit | Inline validation error appears on the External ID field indicating it must be unique | medium |
| TC-012 |  | Attempt to activate a client with Activation Date before submission date | Client is in Pending status | 1. Open the Client Detail page for the client<br>2. Click Activate<br>3. Enter a date in the Activation Date field that is before the Submitted On date<br>4. Click Submit | Inline validation error appears on the Activation Date field indicating it must not be before submission date | medium |
| TC-013 |  | Attempt to close an Active client with active accounts | Client is in Active status | 1. Open the Client Detail page for the client<br>2. Click Close<br>3. Fill the Closure Reason field<br>4. Click Submit | Inline validation error appears indicating cannot close with active accounts | medium |
| TC-014 |  | Attempt to transfer an Active client to the same office | Client is in Active status | 1. Open the Client Detail page for the client<br>2. Click Transfer Client<br>3. Select the same office in the Destination Office field<br>4. Click Submit | Inline validation error appears indicating same office is blocked | medium |
| TC-015 |  | Attempt to withdraw a Pending client without providing a reason | Client is in Pending status | 1. Open the Client Detail page for the client<br>2. Click Withdraw<br>3. Leave the Reason field blank<br>4. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) |  | Test unique External ID with a duplicate value | Existing client with a specific External ID | 1. Navigate to Create Client Wizard<br>2. Fill in all required fields<br>3. Enter the existing External ID in the External ID field<br>4. Click Submit | Form submission is blocked; an error message displays indicating that the External ID must be unique. | medium |
| TC-017 (boundary) |  | Test Activation Date with submission date | Client is in Pending status with a submitted date | 1. Navigate to Client Detail Page<br>2. Click Activate<br>3. Enter the submission date in the Activation Date field<br>4. Click Submit | Form submits successfully; the client status is updated to Active. | medium |
| TC-018 (boundary) |  | Test Activation Date with a date before submission date | Client is in Pending status with a submitted date | 1. Navigate to Client Detail Page<br>2. Click Activate<br>3. Enter a date before the submission date in the Activation Date field<br>4. Click Submit | Form submission is blocked; an error message displays indicating that the Activation Date must not be before the submission date. | medium |
| TC-019 (input_edge) |  | Test long text input in a free-text field |  | 1. Navigate to Create Client Wizard<br>2. Fill in all required fields<br>3. Enter a very long string (200+ characters) in the First Name field<br>4. Click Submit | Form submission is blocked; an error message displays indicating that the input exceeds the maximum length. | low |
| TC-020 (input_edge) |  | Test special characters in the Email Address field |  | 1. Navigate to Create Client Wizard<br>2. Fill in all required fields<br>3. Enter special characters in the Email Address field<br>4. Click Submit | Form submission is blocked; an error message displays indicating invalid email format. | low |
| TC-021 (interaction_edge) |  | Test rapid re-submission after successful client creation | Successfully created a client | 1. Click the browser back button<br>2. Observe the Create Client form | The Create Client form is shown blank, indicating no duplicate submission occurs. | low |

---

## Group Management

Total: **18** (positive: 5, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new group successfully | User logged in as <Admin> | 1. Click 'Create New Group' button<br>2. Enter <Group Name> in the Name field<br>3. Enter <Office> in the Office field<br>4. Enter <date> in the Submitted On field<br>5. Click 'Submit' button | The page shows 'creates the group' | high |
| TC-002 |  | Import groups successfully | User logged in as <Admin> | 1. Click 'Import Groups' button<br>2. Click 'Upload' button in the Groups Upload panel<br>3. Select a <valid file> from the OS dialog<br>4. Click 'Upload' button | The import history table shows the uploaded groups | high |
| TC-003 |  | Download groups template successfully | User logged in as <Admin> | 1. Click 'Import Groups' button<br>2. Click 'Download' button in the Groups Template panel | A file download is triggered in the browser | medium |
| TC-004 |  | View group details successfully | User logged in as <Admin>, Group exists | 1. Click on the <Group Name> link in the Groups table | The Group Detail Page displays the group name, account number, status, office, and staff | medium |
| TC-005 |  | Generate collection sheet successfully | User logged in as <Admin>, Group exists | 1. Click on the <Group Name> link in the Groups table<br>2. Click 'Generate Collection Sheet' button | A file download is triggered in the browser for the collection sheet | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Name field blank and submit the Create Group form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-007 |  | Leave the Office field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-008 |  | Leave the Submitted On field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-009 |  | Attempt to upload a file without selecting a file on the Bulk Import Groups page |  | 1. Leave the File Picker blank<br>2. Click Upload | Inline validation error appears on the File Picker field indicating it is required | high |
| TC-010 |  | Attempt to create a group without filling any required fields |  | 1. Leave the Name field blank<br>2. Leave the Office field blank<br>3. Leave the Submitted On field blank<br>4. Click Submit | Form does not submit; group is not created; error shown on Name, Office, and Submitted On fields | high |
| TC-011 |  | Attempt to activate a group from a state where activation is not allowed |  | 1. Navigate to the Group Detail page of a Closed group<br>2. Click Activate | Status remains Closed; no transition occurs; error message shown indicating the action cannot be performed | medium |
| TC-012 |  | Attempt to close a group that is already closed |  | 1. Navigate to the Group Detail page of a Closed group<br>2. Click Close | Status remains Closed; no transition occurs; error message shown indicating the action cannot be performed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Submit group creation with minimum allowed Name length |  | 1. Enter minimum allowed characters in the Name field<br>2. Enter minimum allowed characters in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum allowed Name length | medium |
| TC-014 (boundary) |  | Submit group creation with one character less than minimum Name length |  | 1. Enter one character less than minimum allowed characters in the Name field<br>2. Enter minimum allowed characters in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Name field displays an error indicating the value is below the minimum allowed | medium |
| TC-015 (input_edge) |  | Enter long text in the Name field |  | 1. Enter a very long string (200+ characters) in the Name field<br>2. Enter minimum allowed characters in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submission is either accepted or trimmed with a visible indicator | low |
| TC-016 (input_edge) |  | Enter special characters in the Name field |  | 1. Enter special characters in the Name field<br>2. Enter minimum allowed characters in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submission is either accepted or a specific error is shown | low |
| TC-017 (data_edge) |  | Upload file exactly at size limit in Bulk Import |  | 1. Select a file exactly at the size limit in the File Picker<br>2. Click Upload | File upload succeeds with a visible success indicator | medium |
| TC-018 (data_edge) |  | Upload file one byte over size limit in Bulk Import |  | 1. Select a file one byte over the size limit in the File Picker<br>2. Click Upload | File upload is blocked; error shown naming the size constraint | medium |

---

## Center Management

Total: **20** (positive: 8, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new center successfully | User logged in as <Admin>, Create Center form is open | 1. Enter <Center Name> in the Name field<br>2. Enter <Office Name> in the Office field<br>3. Enter <valid date> in the Submitted On field<br>4. Click Submit | A success notification is displayed; the center is listed in the Centers page | high |
| TC-002 | WF-002 | Import centers from a file successfully | User logged in as <Admin>, Bulk Import Centers page is open | 1. Click Template_Download to download the template<br>2. Select a <valid file> for upload in the File Upload field<br>3. Click Import | A success notification is displayed; centers are imported from the uploaded file | high |
| TC-003 | WF-003 | View center details | User logged in as <Admin>, Centers page is open | 1. Click on the Name link of a center in the data table | Center Detail page displays the center name, status, office, and staff | medium |
| TC-004 | WF-004 | Activate a center | User logged in as <Admin>, Center Detail page is open | 1. Click Activate | A success notification is displayed; the center status updates to 'Active' | medium |
| TC-005 | WF-005 | Edit center details | User logged in as <Admin>, Center Detail page is open | 1. Click Edit<br>2. Change <field> to <new value><br>3. Click Submit | A success notification is displayed; the center details are updated | medium |
| TC-006 | WF-006 | Close a center | User logged in as <Admin>, Center Detail page is open | 1. Click Close | A success notification is displayed; the center status updates to 'Closed' | medium |
| TC-007 | WF-007 | Assign staff to a center | User logged in as <Admin>, Center Detail page is open | 1. Click Assign Staff<br>2. Select <Staff Member> from the dropdown<br>3. Click Submit | A success notification is displayed; the staff member is assigned to the center | medium |
| TC-008 | WF-008 | Navigate through center detail tabs | User logged in as <Admin>, Center Detail page is open | 1. Click on the Groups tab<br>2. Click on the Loan Accounts tab<br>3. Click on the Savings Accounts tab<br>4. Click on the Notes tab<br>5. Click on the Calendar/Meeting tab | All tabs are navigable and display their respective content | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 |  | Leave the Office field blank and submit the Create Center form |  | 1. Leave the Office field blank<br>2. Fill in the Name field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-012 |  | Leave the File Upload field blank and submit the Bulk Import Centers page |  | 1. Leave the File Upload field blank<br>2. Click Import | Inline validation error appears on the File Upload field indicating it is required | high |
| TC-013 |  | Attempt to Activate a center when it is already Active | Center is in Active state | 1. Navigate to the Center Detail page<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-014 |  | Attempt to Close a center when it is already Closed | Center is in Closed state | 1. Navigate to the Center Detail page<br>2. Click Close | Status remains Closed; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Submit Create Center Form with minimum required fields |  | 1. Enter valid value in the Name field<br>2. Enter valid value in the Office field<br>3. Enter valid value in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum required fields | medium |
| TC-016 (boundary) |  | Submit Create Center Form with missing required fields |  | 1. Leave Name field empty<br>2. Leave Office field empty<br>3. Enter valid value in the Submitted On field<br>4. Click Submit | Form submission is blocked; error messages indicate that Name and Office fields are required | medium |
| TC-017 (data_edge) |  | Upload file exactly at size limit for Bulk Import |  | 1. Navigate to Bulk Import Centers page<br>2. Upload a file that is exactly at the size limit<br>3. Click Import | Import succeeds; centers are imported from the uploaded file | medium |
| TC-018 (data_edge) |  | Upload file over size limit for Bulk Import |  | 1. Navigate to Bulk Import Centers page<br>2. Upload a file that is one byte over the size limit<br>3. Click Import | Import is blocked; visible error indicates file exceeds size limit | medium |
| TC-019 (input_edge) |  | Enter long text in Name field |  | 1. Enter a very long string (200+ characters) in the Name field<br>2. Enter valid value in the Office field<br>3. Enter valid value in the Submitted On field<br>4. Click Submit | Form submission is either accepted or blocked with a visible error indicating the input length | low |
| TC-020 (input_edge) |  | Enter special characters in Office field |  | 1. Enter valid value in the Name field<br>2. Enter special characters in the Office field<br>3. Enter valid value in the Submitted On field<br>4. Click Submit | Form submission is either accepted or blocked with a specific error shown for invalid characters | low |

---

## Loan Products

Total: **25** (positive: 8, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Loan Product detail view | User logged in as <Role> | 1. Click the 'View' action on an existing loan product | opens detail view | high |
| TC-002 | WF-002 | Open Loan Product stepper wizard | User logged in as <Role> | 1. Click the '+ Create Loan Product' button | opens Loan Product stepper wizard | high |
| TC-003 | WF-002 | Complete Loan Product wizard - Step 1: Details | User logged in as <Role>, Loan Product stepper wizard is open | 1. Enter <Product Name> in the Product Name field<br>2. Enter <Short Name> in the Short Name field<br>3. Click Next | Step 2: Currency is visible | high |
| TC-004 | WF-002 | Complete Loan Product wizard - Step 2: Currency | User logged in as <Role>, Loan Product stepper wizard is open, Step 1 is completed | 1. Enter <Principal Amount> in the Principal Amount field<br>2. Click Next | Step 3: Settings is visible | high |
| TC-005 | WF-002 | Complete Loan Product wizard - Step 3: Settings | User logged in as <Role>, Loan Product stepper wizard is open, Step 2 is completed | 1. Select <Repayment Strategy> from the Repayment Strategy dropdown<br>2. Click Next | Step 4: Terms is visible | high |
| TC-006 | WF-002 | Complete Loan Product wizard - Step 4: Terms | User logged in as <Role>, Loan Product stepper wizard is open, Step 3 is completed | 1. Enter <Number of Repayments> in the Number of Repayments field<br>2. Enter <Nominal Interest Rate> in the Nominal Interest Rate field<br>3. Click Next | Step 5: Charges is visible | high |
| TC-007 | WF-002 | Complete Loan Product wizard - Step 5: Charges | User logged in as <Role>, Loan Product stepper wizard is open, Step 4 is completed | 1. Click Next | Step 6: Accounting is visible | high |
| TC-008 | WF-002 | Complete Loan Product wizard - Step 6: Accounting | User logged in as <Role>, Loan Product stepper wizard is open, Step 5 is completed | 1. Select <Accounting Method> from the Accounting Method radio options<br>2. Click Next | The Loan Product is successfully created | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Product Name field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Leave the Product Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-010 |  | Leave the Short Name field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Leave the Short Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-011 |  | Leave the Principal Amount field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields except Principal Amount<br>3. Click Next | Inline validation error appears on the Principal Amount field indicating it is required | high |
| TC-012 |  | Leave the Number of Repayments field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields except Number of Repayments<br>3. Click Next | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-013 |  | Leave the Nominal Interest Rate field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields except Nominal Interest Rate<br>3. Click Next | Inline validation error appears on the Nominal Interest Rate field indicating it is required | high |
| TC-014 |  | Enter a non-numeric value in the Principal Amount field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <non-numeric value> in the Principal Amount field<br>4. Click Next | Inline validation error appears on the Principal Amount field indicating it must be a number | medium |
| TC-015 |  | Enter a non-numeric value in the Number of Repayments field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <non-numeric value> in the Number of Repayments field<br>4. Click Next | Inline validation error appears on the Number of Repayments field indicating it must be a number | medium |
| TC-016 |  | Enter a negative value in the Nominal Interest Rate field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <negative value> in the Nominal Interest Rate field<br>4. Click Next | Inline validation error appears on the Nominal Interest Rate field indicating it must be a positive number | medium |
| TC-017 |  | Attempt to proceed without selecting a Repayment Strategy |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields except Repayment Strategy<br>3. Click Next | Inline validation error appears on the Repayment Strategy field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-001 | Enter minimum value in Principal Amount field | User is on the Loan Product stepper wizard, Step 2 | 1. Enter minimum value in the Principal Amount field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the minimum value in the Principal Amount field | medium |
| TC-019 (boundary) | WF-001 | Enter one unit below minimum value in Principal Amount field | User is on the Loan Product stepper wizard, Step 2 | 1. Enter one unit below minimum value in the Principal Amount field<br>2. Fill all other required fields<br>3. Click Next | Inline error displayed indicating the minimum value must be specified | medium |
| TC-020 (boundary) | WF-001 | Enter minimum value in Number of Repayments field | User is on the Loan Product stepper wizard, Step 4 | 1. Enter minimum value in the Number of Repayments field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the minimum value in the Number of Repayments field | medium |
| TC-021 (boundary) | WF-001 | Enter one unit below minimum value in Number of Repayments field | User is on the Loan Product stepper wizard, Step 4 | 1. Enter one unit below minimum value in the Number of Repayments field<br>2. Fill all other required fields<br>3. Click Next | Inline error displayed indicating the minimum value must be specified | medium |
| TC-022 (boundary) | WF-001 | Enter minimum value in Nominal Interest Rate field | User is on the Loan Product stepper wizard, Step 4 | 1. Enter minimum value in the Nominal Interest Rate field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the minimum value in the Nominal Interest Rate field | medium |
| TC-023 (boundary) | WF-001 | Enter one unit below minimum value in Nominal Interest Rate field | User is on the Loan Product stepper wizard, Step 4 | 1. Enter one unit below minimum value in the Nominal Interest Rate field<br>2. Fill all other required fields<br>3. Click Next | Inline error displayed indicating the minimum value must be specified | medium |
| TC-024 (input_edge) | WF-001 | Enter a very long string in Product Name field | User is on the Loan Product stepper wizard, Step 1 | 1. Enter a very long string (200+ characters) in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; saved value displayed in detail page shows the long string | low |
| TC-025 (input_edge) | WF-001 | Enter special characters in Short Name field | User is on the Loan Product stepper wizard, Step 1 | 1. Enter special characters in the Short Name field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; saved value displayed in detail page shows the special characters | low |

---

## Savings Products

Total: **17** (positive: 4, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new Savings Product with required fields | User logged in as <Admin> | 1. Click '+ Create Savings Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Charges step<br>8. Click Next to proceed to the Accounting step<br>9. Select 'Cash-based' for Accounting Method<br>10. Click Next to complete the wizard | The Savings Product is created successfully. | high |
| TC-002 | WF-001 | Create a new Savings Product with optional fields filled | User logged in as <Admin> | 1. Click '+ Create Savings Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Enter <Description> in the Description field<br>5. Enter <External Id> in the External Id field<br>6. Click Next to proceed to the Currency step<br>7. Click Next to proceed to the Terms step<br>8. Click Next to proceed to the Settings step<br>9. Click Next to proceed to the Charges step<br>10. Click Next to proceed to the Accounting step<br>11. Select 'Cash-based' for Accounting Method<br>12. Click Next to complete the wizard | The Savings Product is created successfully. | high |
| TC-003 | WF-001 | Create a new Savings Product with different interest compounding options | User logged in as <Admin> | 1. Click '+ Create Savings Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Select 'Monthly' for Interest Compounding Period<br>7. Click Next to proceed to the Settings step<br>8. Click Next to proceed to the Charges step<br>9. Click Next to proceed to the Accounting step<br>10. Select 'Cash-based' for Accounting Method<br>11. Click Next to complete the wizard | The Savings Product is created successfully. | high |
| TC-004 | WF-001 | Create a new Savings Product with overdraft settings | User logged in as <Admin> | 1. Click '+ Create Savings Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Check the Is Overdraft Allowed checkbox<br>8. Enter <Maximum Overdraft Amount> in the Maximum Overdraft Amount field<br>9. Enter <Overdraft Interest Rate> in the Overdraft Interest Rate field<br>10. Click Next to proceed to the Charges step<br>11. Click Next to proceed to the Accounting step<br>12. Select 'Cash-based' for Accounting Method<br>13. Click Next to complete the wizard | The Savings Product is created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Product Name blank and submit |  | 1. Leave the Product_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product_Name field indicating it is required | high |
| TC-006 |  | Leave Short Name blank and submit |  | 1. Leave the Short_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Short_Name field indicating it is required | high |
| TC-007 |  | Submit with all required fields empty |  | 1. Leave the Product_Name field blank<br>2. Leave the Short_Name field blank<br>3. Click Submit | Form does not submit; errors shown on Product_Name and Short_Name fields | high |
| TC-008 |  | Submit with invalid number in Decimal Places |  | 1. Enter <non-numeric value> in the Decimal_Places field<br>2. Click Submit | Inline validation error appears on the Decimal_Places field indicating it must be a number | medium |
| TC-009 |  | Submit with invalid number in Minimum Required Balance |  | 1. Enter <non-numeric value> in the Minimum_Required_Balance field<br>2. Click Submit | Inline validation error appears on the Minimum_Required_Balance field indicating it must be a number | medium |
| TC-010 |  | Attempt to submit with Pre-Mature Closure Applicable unchecked |  | 1. Leave the Pre-Mature Closure Applicable checkbox unchecked<br>2. Fill all other fields<br>3. Click Submit | Form does not submit; error shown indicating Pre-Mature Closure is not applicable | medium |
| TC-011 |  | Attempt to submit with Maximum Deposit Amount below Minimum Deposit Amount |  | 1. Enter <amount below minimum> in the Maximum_Deposit_Amount field<br>2. Enter <amount above maximum> in the Minimum_Deposit_Amount field<br>3. Click Submit | Form does not submit; error shown indicating Maximum Deposit Amount must be greater than Minimum Deposit Amount | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Enter a value of 0 in the Minimum Opening Balance field |  | 1. Navigate to the Settings step of the Savings Products wizard<br>2. Enter '0' in the Minimum Opening Balance field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; Minimum Opening Balance is saved as '0' | medium |
| TC-013 (boundary) |  | Enter a value of 1 in the Minimum Required Balance field |  | 1. Navigate to the Settings step of the Savings Products wizard<br>2. Enter '1' in the Minimum Required Balance field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; Minimum Required Balance is saved as '1' | medium |
| TC-014 (boundary) |  | Add exactly one GL account mapping in the Accounting step |  | 1. Navigate to the Accounting step of the Savings Products wizard<br>2. Add one GL account mapping<br>3. Fill in all fields for the mapping<br>4. Click Next | Form submits successfully; one GL account mapping is saved | medium |
| TC-015 (interaction_edge) |  | Attempt to navigate directly to the Charges step without completing previous steps |  | 1. Attempt to click on the Charges step tab in the Savings Products wizard | Navigation is blocked; the Details step remains active and prompts to complete required fields | medium |
| TC-016 (input_edge) |  | Enter a very long string in the Product Name field |  | 1. Navigate to the Details step of the Savings Products wizard<br>2. Enter a string of 200 characters in the Product Name field | Field accepts the long string; saved value is displayed correctly in the detail page | low |
| TC-017 (input_edge) |  | Enter special characters in the Short Name field |  | 1. Navigate to the Details step of the Savings Products wizard<br>2. Enter special characters in the Short Name field | Field accepts the special characters; saved value is displayed correctly in the detail page | low |

---

## Share Products

Total: **26** (positive: 10, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the Create Share Product wizard | User logged in as <Role> | 1. Click the '+ Create Share Product' button | The 7-step stepper wizard opens | high |
| TC-002 | WF-002 | Complete Step 1 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open | 1. Enter <Product Name> in the Product Name field<br>2. Enter <Short Name> in the Short Name field<br>3. Enter <Description> in the Description field<br>4. Click Next | Step 2 (Currency) is displayed | high |
| TC-003 | WF-003 | Complete Step 2 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 1 is completed | 1. Enter <Currency> in the Currency field<br>2. Enter <Decimal Places> in the Decimal Places field<br>3. Enter <Currency In Multiples Of> in the Currency In Multiples Of field<br>4. Click Next | Step 3 (Terms) is displayed | high |
| TC-004 | WF-004 | Complete Step 3 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 2 is completed | 1. Enter <Total Number of Shares> in the Total Number of Shares field<br>2. Enter <Nominal Unit Price> in the Nominal Unit Price field<br>3. Click Next | Step 4 (Settings) is displayed | high |
| TC-005 | WF-005 | Complete Step 4 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 3 is completed | 1. Check the Allow Dividends for Inactive Clients checkbox<br>2. Enter <Minimum Shares per Client> in the Minimum Shares per Client field<br>3. Click Next | Step 5 (Market Price) is displayed | high |
| TC-006 | WF-006 | Complete Step 5 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 4 is completed | 1. Click 'Add Row' in the Market Price table<br>2. Enter <From Date> in the From Date field<br>3. Enter <Share Value> in the Share Value field<br>4. Click Next | Step 6 (Charges) is displayed | high |
| TC-007 | WF-007 | Complete Step 6 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 5 is completed | 1. Enter <Search Term> in the Charges search field<br>2. Click Next | Step 7 (Accounting) is displayed | high |
| TC-008 | WF-008 | Complete Step 7 of the Create Share Product wizard | User logged in as <Role>, The 7-step stepper wizard is open, Step 6 is completed | 1. Select 'Cash-based' from the Accounting Method radio options<br>2. Enter <Share Reference> in the Share Reference field<br>3. Click Finish | A success message is displayed confirming the creation of the share product | high |
| TC-009 | WF-009 | Edit an existing share product | User logged in as <Role>, The Share Products page is open, At least one share product exists | 1. Click the Edit action for the existing share product<br>2. Modify <Product Name> in the Product Name field<br>3. Click Save | The updated share product details are displayed in the Share Products table | medium |
| TC-010 | WF-010 | Delete an existing share product | User logged in as <Role>, The Share Products page is open, At least one share product exists | 1. Click the Delete action for the existing share product<br>2. Click Confirm on the Delete dialog | The share product is no longer visible in the Share Products table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Leave the Product Name field blank and submit |  | 1. Open the Create Share Product wizard<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name and Description fields with valid data<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-012 |  | Leave the Short Name field blank and submit |  | 1. Open the Create Share Product wizard<br>2. Leave the Short Name field blank<br>3. Fill in the Product Name and Description fields with valid data<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-013 |  | Leave the Description field blank and submit |  | 1. Open the Create Share Product wizard<br>2. Leave the Description field blank<br>3. Fill in the Product Name and Short Name fields with valid data<br>4. Click Next | Inline validation error appears on the Description field indicating it is required | high |
| TC-014 |  | Leave Total Number of Shares field blank and submit |  | 1. Open the Create Share Product wizard<br>2. Fill in the Product Name, Short Name, and Description fields with valid data<br>3. Leave the Total Number of Shares field blank<br>4. Fill in the Nominal Unit Price field with valid data<br>5. Click Next | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-015 |  | Leave Nominal Unit Price field blank and submit |  | 1. Open the Create Share Product wizard<br>2. Fill in the Product Name, Short Name, and Description fields with valid data<br>3. Fill in the Total Number of Shares field with valid data<br>4. Leave the Nominal Unit Price field blank<br>5. Click Next | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-016 |  | Leave From Date field blank in Market Price step and submit |  | 1. Open the Create Share Product wizard<br>2. Fill in the Product Name, Short Name, Description, Total Number of Shares, and Nominal Unit Price fields with valid data<br>3. Click Next until Market Price step<br>4. Leave the From Date field blank<br>5. Fill in the Share Value field with valid data<br>6. Click Add | Inline validation error appears on the From Date field indicating it is required | high |
| TC-017 |  | Leave Share Value field blank in Market Price step and submit |  | 1. Open the Create Share Product wizard<br>2. Fill in the Product Name, Short Name, Description, Total Number of Shares, and Nominal Unit Price fields with valid data<br>3. Click Next until Market Price step<br>4. Fill in the From Date field with valid data<br>5. Leave the Share Value field blank<br>6. Click Add | Inline validation error appears on the Share Value field indicating it is required | high |
| TC-018 |  | Attempt to submit the wizard with all required fields empty |  | 1. Open the Create Share Product wizard<br>2. Leave all required fields empty<br>3. Click Next | Inline validation errors appear on the Product Name, Short Name, Description, Total Number of Shares, and Nominal Unit Price fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) |  | Total Number of Shares at minimum boundary | User is on the Create Share Product wizard, Step 3 (Terms) | 1. Enter exactly <minimum allowed value> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; user proceeds to Step 4 (Settings) | medium |
| TC-020 (boundary) |  | Total Number of Shares below minimum boundary | User is on the Create Share Product wizard, Step 3 (Terms) | 1. Enter <one unit below minimum> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Total Number of Shares displays an error indicating the value is below the minimum allowed | medium |
| TC-021 (boundary) |  | Nominal Unit Price at minimum boundary | User is on the Create Share Product wizard, Step 3 (Terms) | 1. Enter exactly <minimum allowed value> in the Nominal Unit Price field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; user proceeds to Step 4 (Settings) | medium |
| TC-022 (boundary) |  | Nominal Unit Price below minimum boundary | User is on the Create Share Product wizard, Step 3 (Terms) | 1. Enter <one unit below minimum> in the Nominal Unit Price field<br>2. Fill all other required fields<br>3. Click Next | Nominal Unit Price displays an error indicating the value is below the minimum allowed | medium |
| TC-023 (input_edge) |  | Leading and trailing whitespace in Product Name | User is on the Create Share Product wizard, Step 1 (Details) | 1. Enter '   Sample Product   ' in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-024 (input_edge) |  | Long text in Description field | User is on the Create Share Product wizard, Step 1 (Details) | 1. Enter a very long string (200+ characters) in the Description field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; user proceeds to Step 2 (Currency) or an error is shown if truncated | low |
| TC-025 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully submitted the Create Share Product wizard | 1. Press the browser back button | The Create Share Product form is shown blank (not pre-filled) | medium |
| TC-026 (interaction_edge) |  | Wizard step skip — enforced navigation | User is on the Create Share Product wizard | 1. Attempt to click on Step 3 (Terms) without completing Step 1 (Details) | Navigation is blocked and Step 1 (Details) remains active | medium |

---

## Charges

Total: **15** (positive: 3, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new charge definition successfully | User logged in as <Admin>, Charges page is open | 1. Click '+ Create Charge' button<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Select <valid currency> from the Currency dropdown<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <valid amount> in the Amount field<br>8. Click Submit | A success notification is displayed; the Charges Table shows the new charge definition | high |
| TC-002 |  | Edit an existing charge definition | User logged in as <Admin>, Charges page is open, At least one charge exists in the Charges Table | 1. Click the Name link of an existing charge in the Charges Table<br>2. Click Edit<br>3. Modify <Charge Name> in the Charge Name field<br>4. Click Submit | A success notification is displayed; the Charges Table reflects the updated charge definition | medium |
| TC-003 |  | Delete an existing charge definition | User logged in as <Admin>, Charges page is open, At least one charge exists in the Charges Table | 1. Click the Name link of an existing charge in the Charges Table<br>2. Click Delete<br>3. Confirm the deletion | The Charges Table no longer displays the deleted charge definition | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Charge Name blank and submit |  | 1. Open the Create Charge form<br>2. Leave the Charge Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-005 |  | Leave Charge Applies To blank and submit |  | 1. Open the Create Charge form<br>2. Leave the Charge Applies To field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-006 |  | Leave Currency blank and submit |  | 1. Open the Create Charge form<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-007 |  | Leave Amount blank and submit |  | 1. Open the Create Charge form<br>2. Leave the Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-008 |  | Submit with all required fields empty |  | 1. Open the Create Charge form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Charge Name, Charge Applies To, Currency, and Amount fields display errors indicating they are required | high |
| TC-009 |  | Select an invalid option for Charge Applies To |  | 1. Open the Create Charge form<br>2. Select an invalid option in the Charge Applies To dropdown<br>3. Fill all other required fields<br>4. Click Submit | Error shown indicating the selected option is invalid | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter minimum required characters in Charge Name |  | 1. Enter <minimum allowed value> in the Charge_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the minimum allowed value | medium |
| TC-011 (boundary) |  | Enter maximum allowed entries in Charge Applies To dropdown |  | 1. Select 'Loan' in the Charge_Applies_To dropdown<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the selected option | medium |
| TC-012 (boundary) |  | Enter a very large amount in Amount field |  | 1. Enter a very large number in the Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the large amount | medium |
| TC-013 (input_edge) |  | Enter a long string in Charge Name |  | 1. Enter a very long string (200+ characters) in the Charge_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; inline error shown indicating the name is too long | low |
| TC-014 (input_edge) |  | Enter special characters in Charge Name |  | 1. Enter special characters in the Charge_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; inline error shown indicating invalid characters | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after redirect | A charge has been successfully created | 1. Click the browser back button after submission<br>2. Observe the Charge Creation form | Charge Creation form is shown blank (not pre-filled) | medium |

---

## Floating Rates

Total: **13** (positive: 4, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new floating rate with valid details | User logged in as <Role> | 1. Click '+ Create Floating Rate' button<br>2. Enter <Floating Rate Name> in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Check the Is Active checkbox<br>5. Click 'Add Row' in the Rate Periods table<br>6. Enter <valid date> in the From Date field of the new row<br>7. Enter <valid interest rate> in the Interest Rate field of the new row<br>8. Click 'Save' to submit the form | A success notification is displayed; the new floating rate appears in the Floating Rates table with the entered Floating Rate Name | high |
| TC-002 |  | Edit an existing floating rate | User logged in as <Role>, At least one floating rate exists in the table | 1. Click the Edit action for the existing floating rate<br>2. Update <new Floating Rate Name> in the Floating Rate Name field<br>3. Click 'Save' to submit the changes | A success notification is displayed; the Floating Rate Name updates to <new Floating Rate Name> in the Floating Rates table | medium |
| TC-003 |  | Delete selected floating rates | User logged in as <Role>, At least one floating rate is selected in the table | 1. Select the floating rate(s) in the Floating Rates table<br>2. Click 'Delete Selected'<br>3. Confirm the deletion | The selected floating rate(s) are no longer visible in the Floating Rates table | medium |
| TC-004 |  | Add multiple rate periods to a floating rate | User logged in as <Role>, Click '+ Create Floating Rate' button | 1. Enter <Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Click 'Add Row' in the Rate Periods table<br>4. Enter <valid date> in the From Date field of the first new row<br>5. Enter <valid interest rate> in the Interest Rate field of the first new row<br>6. Click 'Add Row' in the Rate Periods table again<br>7. Enter <valid date> in the From Date field of the second new row<br>8. Enter <valid interest rate> in the Interest Rate field of the second new row<br>9. Click 'Save' to submit the form | A success notification is displayed; the new floating rate appears in the Floating Rates table with the entered Floating Rate Name and multiple rate periods are saved | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Floating Rate Name blank and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-006 |  | Attempt to create a second base lending rate |  | 1. Click on '+ Create Floating Rate' button<br>2. Fill the Floating Rate Name field with a valid name<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit<br>5. Open the creation form again<br>6. Fill the Floating Rate Name field with another valid name<br>7. Check the Is Base Lending Rate checkbox<br>8. Click Submit | Inline validation error appears indicating 'only one base rate can exist at a time' | high |
| TC-007 |  | Leave the From Date blank in Rate Periods and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Fill the Floating Rate Name field with a valid name<br>3. Add a Rate Period<br>4. Leave the From Date field blank<br>5. Fill the Interest Rate field with a valid number<br>6. Click Submit | Inline validation error appears on the From Date field indicating it is required | high |
| TC-008 |  | Leave the Interest Rate blank in Rate Periods and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Fill the Floating Rate Name field with a valid name<br>3. Add a Rate Period<br>4. Fill the From Date field with a valid date<br>5. Leave the Interest Rate field blank<br>6. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Add maximum allowed entries to Rate Periods | User is on the Create Floating Rate Form | 1. Add maximum allowed entries to the Rate Periods table | Form submits successfully; all entries are saved in the Rate Periods table | medium |
| TC-010 (boundary) |  | Attempt to add one more entry to Rate Periods beyond maximum | User is on the Create Floating Rate Form with maximum entries already added | 1. Attempt to add one more entry to the Rate Periods table | Entry addition is blocked; visible error shown indicating maximum entries reached | medium |
| TC-011 (input_edge) |  | Enter a very long Floating Rate Name | User is on the Create Floating Rate Form | 1. Enter a very long string (200+ characters) in the Floating Rate Name field | Field accepts the input or shows an error indicating the name is too long | low |
| TC-012 (input_edge) |  | Enter special characters in Floating Rate Name | User is on the Create Floating Rate Form | 1. Enter special characters in the Floating Rate Name field | Field accepts the input or shows a specific error indicating invalid characters | low |
| TC-013 (interaction_edge) |  | Rapid re-submission after successful creation | User has successfully created a Floating Rate | 1. Press the browser back button after successful submission | Creation form is shown blank; no duplicate entry is created | medium |

---

## Delinquency Management

Total: **16** (positive: 5, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new delinquency range with all required fields | User logged in as <Admin> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <valid classification> in the Classification field<br>4. Enter <valid minimum age days> in the Minimum Age Days field<br>5. Enter <valid maximum age days> in the Maximum Age Days field<br>6. Click 'Submit' | A success notification is displayed; the new delinquency range appears in the Delinquency Ranges table with the entered Classification, Minimum Age Days, and Maximum Age Days | high |
| TC-002 |  | Create a new delinquency range with optional maximum age days blank | User logged in as <Admin> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <valid classification> in the Classification field<br>4. Enter <valid minimum age days> in the Minimum Age Days field<br>5. Leave the Maximum Age Days field blank<br>6. Click 'Submit' | A success notification is displayed; the new delinquency range appears in the Delinquency Ranges table with the entered Classification and Minimum Age Days, and applies to all days beyond the minimum | high |
| TC-003 |  | Access delinquency range details from the data table | User logged in as <Admin>, At least one delinquency range exists | 1. Navigate to the Delinquency Ranges page<br>2. Click on the Classification link for the first delinquency range | The Delinquency Range detail page is displayed with the correct Classification and associated details | medium |
| TC-004 |  | Create a new delinquency bucket with required fields | User logged in as <Admin> | 1. Navigate to the Delinquency Buckets page<br>2. Click on 'Create Delinquency Bucket'<br>3. Enter <valid bucket name> in the Bucket Name field<br>4. Click 'Add Range'<br>5. Enter <valid range name> in the Range Name field<br>6. Enter <valid minimum age days> in the Minimum Age Days field<br>7. Leave the Maximum Age Days field blank<br>8. Click 'Submit' | A success notification is displayed; the new delinquency bucket appears in the Delinquency Buckets table with the entered Bucket Name and associated ranges | high |
| TC-005 |  | Access delinquency bucket details from the data table | User logged in as <Admin>, At least one delinquency bucket exists | 1. Navigate to the Delinquency Buckets page<br>2. Click on the Bucket Name link for the first delinquency bucket | The Delinquency Bucket detail page is displayed with the correct Bucket Name and associated ranges | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Classification field blank |  | 1. Open the Create Delinquency Range Form<br>2. Leave the Classification field blank<br>3. Fill in the Minimum Age Days with a valid number<br>4. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-007 |  | Leave the Minimum Age Days field blank |  | 1. Open the Create Delinquency Range Form<br>2. Fill in the Classification with a valid value<br>3. Leave the Minimum Age Days field blank<br>4. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-008 |  | Leave the Bucket Name field blank |  | 1. Open the Create Delinquency Bucket Form<br>2. Leave the Bucket Name field blank<br>3. Add a delinquency range with valid values<br>4. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty in Create Delinquency Range Form |  | 1. Open the Create Delinquency Range Form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; error shown on Classification and Minimum Age Days fields | high |
| TC-010 |  | Submit with all required fields empty in Create Delinquency Bucket Form |  | 1. Open the Create Delinquency Bucket Form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; error shown on Bucket Name field | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Minimum Age Days at lower boundary |  | 1. Enter exactly 1 in the Minimum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the Minimum Age Days set to 1 | medium |
| TC-012 (boundary) |  | Minimum Age Days below lower boundary |  | 1. Enter 0 in the Minimum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error displayed indicating Minimum Age Days must be greater than 0 | medium |
| TC-013 (boundary) |  | Maximum Age Days at upper boundary |  | 1. Enter a value in the Minimum Age Days field<br>2. Enter exactly 100 in the Maximum Age Days field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; entity is created with the Maximum Age Days set to 100 | medium |
| TC-014 (boundary) |  | Maximum Age Days above upper boundary |  | 1. Enter a value in the Minimum Age Days field<br>2. Enter 101 in the Maximum Age Days field<br>3. Fill all other required fields<br>4. Click Submit | Form submission is blocked; error displayed indicating Maximum Age Days must not exceed 100 | medium |
| TC-015 (boundary) |  | Repeating group: add maximum entries |  | 1. Open Create Delinquency Bucket Form<br>2. Add exactly 5 delinquency ranges<br>3. Fill all required fields for each range<br>4. Click Submit | Form submits successfully with all 5 delinquency ranges added | medium |
| TC-016 (boundary) |  | Repeating group: add one more than maximum entries |  | 1. Open Create Delinquency Bucket Form<br>2. Add 6 delinquency ranges<br>3. Fill all required fields for each range<br>4. Click Submit | Form submission is blocked; error displayed indicating maximum of 5 delinquency ranges allowed | medium |

---

## Loan Account

Total: **27** (positive: 2, negative: 19, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit loan application with valid details | User logged in as <Client>, Loan Application wizard is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer name> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number> in the Number of Repayments field<br>9. Enter <valid frequency> in the Repaid Every field<br>10. Enter <valid interest rate> in the Interest Rate field<br>11. Click Next to proceed to the Terms step<br>12. Select <Repayment Strategy> from the Repayment Strategy dropdown<br>13. Select <Amortization> from the Amortization dropdown<br>14. Select <Interest Method> from the Interest Method dropdown<br>15. Select <Interest Calculation Period> from the Interest Calculation Period dropdown<br>16. Click Next to proceed to the Charges step<br>17. Click Add Charge to add any additional charges<br>18. Click Next to proceed to the Collateral step<br>19. Click Submit to finalize the loan application | Loan is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-001 | Add collateral item in loan application | User logged in as <Client>, Loan Application wizard is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer name> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number> in the Number of Repayments field<br>9. Enter <valid frequency> in the Repaid Every field<br>10. Enter <valid interest rate> in the Interest Rate field<br>11. Click Next to proceed to the Terms step<br>12. Select <Repayment Strategy> from the Repayment Strategy dropdown<br>13. Select <Amortization> from the Amortization dropdown<br>14. Select <Interest Method> from the Interest Method dropdown<br>15. Select <Interest Calculation Period> from the Interest Calculation Period dropdown<br>16. Click Next to proceed to the Charges step<br>17. Click Add Charge to add any additional charges<br>18. Click Next to proceed to the Collateral step<br>19. Click 'Add Row' to add a collateral item<br>20. Enter <Collateral Type> in the Collateral Type field<br>21. Enter <valid value> in the Value field<br>22. Enter <Description> in the Description field<br>23. Click Submit to finalize the loan application | Loan is created in 'Submitted and Pending Approval' status with collateral item added | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-004 |  | Leave the Loan Officer field blank and submit |  | 1. Leave the Loan Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-005 |  | Leave the Loan Purpose field blank and submit |  | 1. Leave the Loan Purpose field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Purpose field indicating it is required | high |
| TC-006 |  | Leave the Fund field blank and submit |  | 1. Leave the Fund field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fund field indicating it is required | high |
| TC-007 |  | Leave the Submitted On date field blank and submit |  | 1. Leave the Submitted On date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-008 |  | Leave the Expected Disbursement Date field blank and submit |  | 1. Leave the Expected Disbursement Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it is required | high |
| TC-009 |  | Leave the Principal field blank and submit |  | 1. Leave the Principal field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is required | high |
| TC-010 |  | Leave the Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-011 |  | Leave the Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-012 |  | Leave the Interest Rate field blank and submit |  | 1. Leave the Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-013 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Form does not submit; all required fields are highlighted with validation errors | high |
| TC-014 |  | Enter a non-numeric value in the Principal field |  | 1. Enter <non-numeric value> in the Principal field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Principal field indicating it must be a number | medium |
| TC-015 |  | Enter a non-numeric value in the Interest Rate field |  | 1. Enter <non-numeric value> in the Interest Rate field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it must be a number | medium |
| TC-016 |  | Enter a past date in the Submitted On field |  | 1. Enter <past date> in the Submitted On field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it must be a future date | medium |
| TC-017 |  | Enter a past date in the Expected Disbursement Date field |  | 1. Enter <past date> in the Expected Disbursement Date field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it must be a future date | medium |
| TC-018 |  | Attempt to submit the loan application while the Principal exceeds product max |  | 1. Enter <amount exceeding product max> in the Principal field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is bounded by product min/max | medium |
| TC-019 |  | Attempt to submit the loan application while the Interest Rate exceeds product max |  | 1. Enter <amount exceeding product max> in the Interest Rate field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is bounded by product min/max | medium |
| TC-020 |  | Attempt to approve a loan that is not in Pending Approval status |  | 1. Navigate to the Loan Detail page of a loan not in Pending Approval status<br>2. Click Approve | Status remains <Current Status>; no transition occurs; error shown indicating the loan cannot be approved | medium |
| TC-021 |  | Attempt to make a repayment on a loan that is not Active |  | 1. Navigate to the Loan Detail page of a loan not in Active status<br>2. Click Make Repayment | Status remains <Current Status>; no transition occurs; error shown indicating the loan cannot be repaid | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (boundary) |  | Enter the minimum Principal amount allowed by the product |  | 1. Select a Product_Name from the dropdown<br>2. Enter <minimum Principal amount> in the Principal field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; loan is created with the <minimum Principal amount> | medium |
| TC-023 (boundary) |  | Enter one unit above the maximum Interest Rate allowed by the product |  | 1. Select a Product_Name from the dropdown<br>2. Enter <maximum Interest Rate + 1> in the Interest Rate field<br>3. Fill all other required fields<br>4. Click Submit | Form submission is blocked; error shown indicating the Interest Rate exceeds the maximum allowed | medium |
| TC-024 (input_edge) |  | Enter a very long string in the Loan Officer field |  | 1. Select a Product_Name from the dropdown<br>2. Enter a string of 200+ characters in the Loan Officer field<br>3. Fill all other required fields<br>4. Click Submit | Form submission is blocked; inline error shown indicating the input exceeds the maximum length | low |
| TC-025 (input_edge) |  | Enter a value with leading and trailing whitespace in the Loan Purpose field |  | 1. Select a Product_Name from the dropdown<br>2. Enter '   Loan Purpose   ' in the Loan Purpose field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-026 (interaction_edge) |  | Rapid re-submission after successful loan creation |  | 1. Complete the loan application form and click Submit<br>2. On the success page, press the browser back button | User is redirected to the loan application form, which is shown blank (not pre-filled) | medium |
| TC-027 (state_edge) |  | Attempt to approve a loan immediately after submission | Loan is in 'Submitted and Pending Approval' status | 1. Click Approve on the loan detail page<br>2. Enter the required approval details<br>3. Click Submit | Approval action succeeds; loan status changes to 'Approved' | medium |

---

## Savings Account

Total: **16** (positive: 4, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new savings account successfully | User logged in as <Client>, User is on the Client Detail page | 1. Select <Product Name> from the Product Name dropdown<br>2. Enter <Field Officer> in the Field Officer field<br>3. Enter <valid date> in the Submitted On date field<br>4. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>5. Select <Interest Compounding Period> from the Interest Compounding Period dropdown<br>6. Select <Interest Posting Period> from the Interest Posting Period dropdown<br>7. Select <Interest Calculated Using> from the Interest Calculated Using dropdown<br>8. Select <Days in Year> from the Days in Year dropdown<br>9. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>10. Enter <Lock-in Period> in the Lock-in Period field<br>11. Check the Allow Overdraft checkbox<br>12. Click 'Add' to include charges in the Charges section<br>13. Click 'Submit' | creates account in Submitted and Pending Approval status | high |
| TC-002 |  | Navigate to the Summary tab of the Savings Account Detail page | User logged in as <Client>, Savings account is created and in Submitted and Pending Approval status | 1. Click on the Savings Account Detail page<br>2. Click on the Summary tab | The Summary tab displays the account number, product name, client name, and status badge | medium |
| TC-003 | WF-001 | Approve a pending savings account application | User logged in as <Admin>, Savings account is in Pending status | 1. Click on the Savings Account Detail page<br>2. Click Approve on the Savings Account Actions bar | The account status updates to Approved | high |
| TC-004 | WF-002 | Withdraw from an active savings account | User logged in as <Client>, Savings account is in Active status | 1. Click on the Savings Account Detail page<br>2. Click Withdraw on the Savings Account Actions bar<br>3. Enter <valid date> in the Transaction Date field<br>4. Enter <Transaction Amount> in the Transaction Amount field<br>5. Select <Payment Type> from the Payment Type dropdown<br>6. Enter <Payment Details> in the Payment Details field<br>7. Click Submit | The account balance updates to reflect the withdrawal | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to submit the Savings Account Creation Form with all fields empty |  | 1. Leave all fields in the Savings Account Creation Form blank<br>2. Click Submit | Form does not submit; no account is created; error shown on required fields |  |
| TC-006 |  | Attempt to withdraw an amount exceeding available balance without overdraft enabled | Account is in Active status, Available balance is <amount> | 1. Click Withdraw from the Savings Account Actions<br>2. Enter <amount exceeding available balance> in the Transaction Amount field<br>3. Select a Payment Type<br>4. Click Submit | Form does not submit; withdrawal exceeds available balance; error shown on Transaction Amount field |  |
| TC-007 |  | Attempt to withdraw an amount that would breach minimum balance requirement | Account is in Active status, Minimum balance must be maintained, Available balance is <amount>, Withdrawal amount is <amount breaching minimum balance> | 1. Click Withdraw from the Savings Account Actions<br>2. Enter <amount breaching minimum balance> in the Transaction Amount field<br>3. Select a Payment Type<br>4. Click Submit | Form does not submit; withdrawal would breach minimum balance; error shown on Transaction Amount field |  |
| TC-008 |  | Attempt to approve an account that is not in Pending status | Account is in Active status | 1. Click Approve from the Savings Account Actions | Action is blocked; no approval occurs; error shown indicating the account must be in Pending status |  |
| TC-009 |  | Attempt to activate an account that is not in Approved status | Account is in Pending status | 1. Click Activate from the Savings Account Actions | Action is blocked; no activation occurs; error shown indicating the account must be in Approved status |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Test minimum opening balance boundary |  | 1. Enter the minimum opening balance in the Minimum Opening Balance field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with the minimum opening balance | medium |
| TC-011 (boundary) |  | Test minimum opening balance below threshold |  | 1. Enter one unit below the minimum opening balance in the Minimum Opening Balance field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error shown indicating minimum opening balance not met | medium |
| TC-012 (boundary) |  | Test maximum charges entries |  | 1. Add maximum allowed entries to the Charges section<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with maximum charges entries | medium |
| TC-013 (boundary) |  | Test adding one more charge entry beyond maximum |  | 1. Add maximum allowed entries to the Charges section<br>2. Attempt to add one more entry to the Charges section<br>3. Click Submit | Form submission is blocked; no additional charge entry is allowed | medium |
| TC-014 (input_edge) |  | Test long text in Field Officer field |  | 1. Enter a very long string (200+ characters) in the Field Officer field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is accepted or truncated; visible indicator shows the value saved correctly | low |
| TC-015 (input_edge) |  | Test special characters in Nominal Annual Interest Rate field |  | 1. Enter special characters in the Nominal Annual Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; specific error shown indicating invalid characters | low |
| TC-016 (interaction_edge) |  | Test rapid re-submission after successful creation |  | 1. Submit the Savings Account creation form successfully<br>2. Press the browser back button immediately after submission | The creation form is shown blank; no duplicate account is created | low |

---

## Share Account

Total: **27** (positive: 11, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Share Account Application with valid data | User logged in as <Client>, Client has active savings accounts | 1. Open the Share Account Application form<br>2. Select <valid share product> from the Share Product dropdown<br>3. Enter <valid date> in the Submitted On field<br>4. Enter <valid number within bounds> in the Requested Shares field<br>5. Enter <valid date> in the Application Date field<br>6. Select <active savings account> from the Savings Account for Charges dropdown<br>7. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-002 |  | Verify Purchased Shares tab is visible on Share Account Detail page | User logged in as <Client>, Account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page | The Purchased Shares tab is visible on the Share Account Detail page | medium |
| TC-003 |  | Verify Dividends tab is visible on Share Account Detail page | User logged in as <Client>, Account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page | The Dividends tab is visible on the Share Account Detail page | medium |
| TC-004 |  | Verify Charges tab is visible on Share Account Detail page | User logged in as <Client>, Account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page | The Charges tab is visible on the Share Account Detail page | medium |
| TC-005 |  | Approve Share Account in Pending status | User logged in as <Admin>, Account is in Pending status | 1. Navigate to the Share Account Detail page<br>2. Click Approve on the Share Account Detail Actions | The account status updates to Approved with Approved Shares and Approved Date | high |
| TC-006 |  | Reject Share Account in Pending status | User logged in as <Admin>, Account is in Pending status | 1. Navigate to the Share Account Detail page<br>2. Click Reject on the Share Account Detail Actions | The account status updates to Rejected | high |
| TC-007 |  | Activate Approved Share Account | User logged in as <Admin>, Account is in Approved status | 1. Navigate to the Share Account Detail page<br>2. Click Activate on the Share Account Detail Actions | The account status updates to Active | high |
| TC-008 |  | Undo Approval of Active Share Account | User logged in as <Admin>, Account is in Active status | 1. Navigate to the Share Account Detail page<br>2. Click Undo Approval on the Share Account Detail Actions | The account status updates back to Approved | high |
| TC-009 |  | Apply Additional Shares to Active Share Account | User logged in as <Client>, Account is in Active status | 1. Navigate to the Share Account Detail page<br>2. Click Apply Additional Shares on the Share Account Detail Actions<br>3. Enter <valid number of additional shares> in the Requested Shares field<br>4. Click Submit | The account reflects the updated number of shares | high |
| TC-010 |  | Redeem Shares from Active Share Account | User logged in as <Client>, Account is in Active status | 1. Navigate to the Share Account Detail page<br>2. Click Redeem Shares on the Share Account Detail Actions | Redemption amount is calculated as shares multiplied by current unit price and credited to the linked savings account | high |
| TC-011 |  | Close Active Share Account | User logged in as <Client>, Account is in Active status | 1. Navigate to the Share Account Detail page<br>2. Click Close on the Share Account Detail Actions | The account status updates to Closed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-013 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-014 |  | Leave the Requested Shares field blank and submit |  | 1. Leave the Requested Shares field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-015 |  | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-016 |  | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-017 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; error shown on Share Product, Submitted On, Requested Shares, Application Date, and Savings Account for Charges fields | high |
| TC-018 |  | Enter a non-numeric value in the Requested Shares field and submit |  | 1. Enter <non-numeric value> in the Requested Shares field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it must be a number | medium |
| TC-019 |  | Enter a past date in the Submitted On field and submit |  | 1. Enter <past date> in the Submitted On field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it must be a valid date | medium |
| TC-020 |  | Attempt to Approve a share account from the Active state |  | 1. Navigate to the Share Account Detail page<br>2. Attempt to click Approve action | No action occurs; the Approve button is not available in the Active state | medium |
| TC-021 |  | Attempt to Activate a share account from the Pending state |  | 1. Navigate to the Share Account Detail page<br>2. Attempt to click Activate action | No action occurs; the Activate button is not available in the Pending state | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (boundary) |  | Enter minimum requested shares | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges<br>6. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-023 (boundary) |  | Enter maximum requested shares | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the maximum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges<br>6. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-024 (boundary) |  | Enter one unit over maximum requested shares | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter one unit over the maximum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges<br>6. Click Submit | Form submission is blocked; error shown indicating that the number of shares exceeds the maximum allowed | medium |
| TC-025 (data_edge) |  | Enter today's date in Submitted On field | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter today's date in the Submitted On field<br>3. Fill in the Requested Shares<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges<br>6. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-026 (data_edge) |  | Enter yesterday's date in Submitted On field | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter yesterday's date in the Submitted On field<br>3. Fill in the Requested Shares<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges<br>6. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-027 (input_edge) |  | Enter a very long External ID | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter a very long string (200+ characters) in the External ID field<br>3. Fill in the Submitted On date<br>4. Fill in the Requested Shares<br>5. Fill in the Application Date<br>6. Select a Savings Account for Charges<br>7. Click Submit | Form submission is blocked; error shown indicating the External ID exceeds the maximum length | low |

---

## Fixed & Recurring Deposit Accounts

Total: **31** (positive: 6, negative: 18, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a Fixed Deposit Account with valid details | User logged in as <Client> | 1. Open the FD Account Creation Form<br>2. Select <Fixed Deposit Product> from the Fixed Deposit Product dropdown<br>3. Enter <valid deposit amount> in the Deposit Amount field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <unit> from the Deposit Period Unit dropdown<br>6. Select <Maturity Instruction> from the Maturity Instructions dropdown<br>7. Click Submit | A success notification is displayed; the FD Account Detail page shows the deposit amount and maturity date. | high |
| TC-002 |  | Create a Recurring Deposit Account with valid details | User logged in as <Client> | 1. Open the RD Account Creation Form<br>2. Select <Recurring Deposit Product> from the Recurring Deposit Product dropdown<br>3. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount Per Installment field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <Deposit Frequency> from the Deposit Frequency dropdown<br>6. Enter <valid date> in the Expected First Deposit On field<br>7. Click Submit | A success notification is displayed; the RD Account Detail page shows the total deposits made and maturity details. | high |
| TC-003 |  | Approve a Fixed Deposit Account | User logged in as <Bank Officer>, FD Account is created | 1. Open the FD Account Detail Page<br>2. Click Approve | The status updates to 'Approved' on the FD Account Detail page. | medium |
| TC-004 |  | Activate a Recurring Deposit Account | User logged in as <Bank Officer>, RD Account is created | 1. Open the RD Account Detail Page<br>2. Click Activate | The status updates to 'Active' on the RD Account Detail page. | medium |
| TC-005 |  | Navigate between tabs in FD Account Detail Page | User logged in as <Client>, FD Account is created | 1. Open the FD Account Detail Page<br>2. Click on the Summary tab<br>3. Click on the Transactions tab<br>4. Click on the Charges tab | All tabs are navigable and display the respective content. | low |
| TC-006 |  | Navigate between tabs in RD Account Detail Page | User logged in as <Client>, RD Account is created | 1. Open the RD Account Detail Page<br>2. Click on the Summary tab<br>3. Click on the Transactions tab<br>4. Click on the Charges tab | All tabs are navigable and display the respective content. | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Fixed Deposit Product dropdown blank and submit |  | 1. Leave the Fixed Deposit Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fixed Deposit Product field indicating it is required | high |
| TC-008 |  | Leave the Deposit Amount field blank and submit |  | 1. Leave the Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-009 |  | Leave the Deposit Period field blank and submit |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-010 |  | Leave the Deposit Period Unit dropdown blank and submit |  | 1. Leave the Deposit Period Unit dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period Unit field indicating it is required | high |
| TC-011 |  | Leave the Maturity Instructions dropdown blank and submit |  | 1. Leave the Maturity Instructions dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Maturity Instructions field indicating it is required | high |
| TC-012 |  | Leave the Recurring Deposit Product dropdown blank and submit |  | 1. Leave the Recurring Deposit Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Recurring Deposit Product field indicating it is required | high |
| TC-013 |  | Leave the Mandatory Deposit Amount Per Installment field blank and submit |  | 1. Leave the Mandatory Deposit Amount Per Installment field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mandatory Deposit Amount Per Installment field indicating it is required | high |
| TC-014 |  | Leave the Deposit Period field blank in RD form and submit |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-015 |  | Leave the Deposit Frequency dropdown blank and submit |  | 1. Leave the Deposit Frequency dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Frequency field indicating it is required | high |
| TC-016 |  | Leave the Expected First Deposit On date blank and submit |  | 1. Leave the Expected First Deposit On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected First Deposit On field indicating it is required | high |
| TC-017 |  | Attempt to Approve an FD Account without meeting preconditions | FD Account is not in a state that allows approval | 1. Navigate to the FD Account Detail Page<br>2. Click Approve | Status remains unchanged; no transition occurs | medium |
| TC-018 |  | Attempt to Activate an FD Account without meeting preconditions | FD Account is not in a state that allows activation | 1. Navigate to the FD Account Detail Page<br>2. Click Activate | Status remains unchanged; no transition occurs | medium |
| TC-019 |  | Attempt to Close on Maturity without meeting preconditions | FD Account is not in a state that allows closing on maturity | 1. Navigate to the FD Account Detail Page<br>2. Click Close on Maturity | Status remains unchanged; no transition occurs | medium |
| TC-020 |  | Attempt to Premature Close an FD Account without meeting preconditions | FD Account is not in a state that allows premature closing | 1. Navigate to the FD Account Detail Page<br>2. Click Premature Close | Status remains unchanged; no transition occurs | medium |
| TC-021 |  | Attempt to Approve an RD Account without meeting preconditions | RD Account is not in a state that allows approval | 1. Navigate to the RD Account Detail Page<br>2. Click Approve | Status remains unchanged; no transition occurs | medium |
| TC-022 |  | Attempt to Activate an RD Account without meeting preconditions | RD Account is not in a state that allows activation | 1. Navigate to the RD Account Detail Page<br>2. Click Activate | Status remains unchanged; no transition occurs | medium |
| TC-023 |  | Attempt to Close on Maturity without meeting preconditions | RD Account is not in a state that allows closing on maturity | 1. Navigate to the RD Account Detail Page<br>2. Click Close on Maturity | Status remains unchanged; no transition occurs | medium |
| TC-024 |  | Attempt to Premature Close an RD Account without meeting preconditions | RD Account is not in a state that allows premature closing | 1. Navigate to the RD Account Detail Page<br>2. Click Premature Close | Status remains unchanged; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 (boundary) |  | Test Deposit Amount at minimum allowed value |  | 1. Enter <minimum allowed value> in the <Deposit Amount> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <minimum allowed value> | medium |
| TC-026 (boundary) |  | Test Deposit Amount just below minimum allowed value |  | 1. Enter <one unit below minimum> in the <Deposit Amount> field<br>2. Fill all other required fields<br>3. Click Submit | <Deposit Amount> displays an error indicating the value is below the minimum allowed | medium |
| TC-027 (boundary) |  | Test Deposit Period at maximum allowed value |  | 1. Enter <maximum allowed value> in the <Deposit Period> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <maximum allowed value> | medium |
| TC-028 (boundary) |  | Test Deposit Period just above maximum allowed value |  | 1. Enter <one unit above maximum> in the <Deposit Period> field<br>2. Fill all other required fields<br>3. Click Submit | <Deposit Period> displays an error indicating the value exceeds the maximum allowed | medium |
| TC-029 (input_edge) |  | Enter a very long string in the Fixed Deposit Product dropdown |  | 1. Enter a very long string (200+ characters) in the <Fixed Deposit Product> field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked with an error indicating the input is too long | low |
| TC-030 (input_edge) |  | Enter special characters in the Mandatory Deposit Amount Per Installment field |  | 1. Enter special characters (e.g., @#$%) in the <Mandatory Deposit Amount Per Installment> field<br>2. Fill all other required fields<br>3. Click Submit | <Mandatory Deposit Amount Per Installment> displays an error indicating invalid characters | low |
| TC-031 (interaction_edge) |  | Rapid re-submission after successful FD account creation | FD account has been successfully created | 1. Click the browser back button<br>2. Click Submit again on the FD Account creation form | The creation form is shown blank (not pre-filled) | medium |

---

## Accounting — Chart of Accounts

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new GL Account with valid details | User logged in as <Accountant>, On the Chart of Accounts page | 1. Click '+ Create GL Account' button<br>2. Select <Account Type> from the Account Type dropdown<br>3. Enter <unique GL Code> in the GL Code field<br>4. Enter <Account Name> in the Account Name field<br>5. Select <Account Usage> from the Account Usage dropdown<br>6. Check the Manual Entries Allowed checkbox if applicable<br>7. Enter <Description> in the Description field<br>8. Click Submit | A success notification is displayed; the new account appears in the Chart of Accounts with the entered GL Code and Account Name | high |
| TC-002 |  | Edit an existing GL Account | User logged in as <Accountant>, On the Chart of Accounts page, An account with GL Code '<existing GL Code>' exists | 1. Click on the account name for GL Code '<existing GL Code>'<br>2. Click the Edit button<br>3. Update the Account Name to '<new Account Name>'<br>4. Click Save | The account's details are updated; the Chart of Accounts displays the new Account Name for GL Code '<existing GL Code>' | medium |
| TC-003 |  | Delete an existing GL Account | User logged in as <Accountant>, On the Chart of Accounts page, An account with GL Code '<existing GL Code>' exists | 1. Click on the account name for GL Code '<existing GL Code>'<br>2. Click the Delete button<br>3. Confirm the deletion | The account with GL Code '<existing GL Code>' is no longer visible in the Chart of Accounts | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Account Type field blank and submit |  | 1. Open the Create GL Account form<br>2. Leave the Account Type field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-005 |  | Leave the GL Code field blank and submit |  | 1. Open the Create GL Account form<br>2. Leave the GL Code field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-006 |  | Leave the Account Name field blank and submit |  | 1. Open the Create GL Account form<br>2. Leave the Account Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-007 |  | Submit with a duplicate GL Code |  | 1. Open the Create GL Account form<br>2. Enter a duplicate value in the GL Code field<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; GL Code is not created; error shown on GL Code field indicating it must be unique | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Attempt to create a GL account with a duplicate GL Code | A GL account with the same GL Code already exists | 1. Navigate to the Create GL Account form<br>2. Enter the duplicate GL Code in the GL Code field<br>3. Fill in all other required fields<br>4. Click Submit | Form submission is blocked; error message displays indicating 'GL Code must be unique' | medium |
| TC-009 (input_edge) |  | Enter a very long string in the Account Name field |  | 1. Navigate to the Create GL Account form<br>2. Enter a string of 200+ characters in the Account Name field<br>3. Fill in all other required fields<br>4. Click Submit | Form submission succeeds; Account Name is saved with the long string or an error is shown indicating the length limit | low |
| TC-010 (input_edge) |  | Enter special characters in the Description field |  | 1. Navigate to the Create GL Account form<br>2. Enter special characters (e.g., @#$%^&*) in the Description field<br>3. Fill in all other required fields<br>4. Click Submit | Form submission succeeds; Description is saved with the special characters or an error is shown | low |
| TC-011 (input_edge) |  | Enter leading and trailing whitespace in the Account Name field |  | 1. Navigate to the Create GL Account form<br>2. Enter '   Account Name   ' in the Account Name field<br>3. Fill in all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounting — Journal Entries & Closures

Total: **20** (positive: 5, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Add Journal Entry Form | User logged in as <Accountant>, Journal Entries page is open | 1. Click 'Add Journal Entry' button | opens the creation form | high |
| TC-002 | WF-001 | Submit Valid Journal Entry | User logged in as <Accountant>, Add Journal Entry form is open | 1. Select <valid office> from the Office dropdown<br>2. Select <valid currency> from the Currency dropdown<br>3. Enter <valid transaction date> in the Transaction Date field<br>4. Click 'Add Row' in Entry Lines<br>5. Select <valid GL Account> from the GL Account dropdown in the new row<br>6. Enter <valid amount> in the Amount field in the new row<br>7. Click 'Submit' button | total debits must equal total credits | high |
| TC-003 | WF-001 | Add Row in Journal Entry | User logged in as <Accountant>, Add Journal Entry form is open | 1. Select <valid office> from the Office dropdown<br>2. Select <valid currency> from the Currency dropdown<br>3. Enter <valid transaction date> in the Transaction Date field<br>4. Click 'Add Row' in Entry Lines<br>5. Select <valid GL Account> from the GL Account dropdown in the new row<br>6. Enter <valid amount> in the Amount field in the new row | adds additional entry line | medium |
| TC-004 | WF-002 | Open Create Closure Form | User logged in as <Accountant>, Closing Entries page is open | 1. Click 'Create Closure' button | opens the closure form | high |
| TC-005 | WF-002 | Submit Valid Closure | User logged in as <Accountant>, Create Closure form is open | 1. Select <valid office> from the Office dropdown<br>2. Enter <valid closing date> in the Closing Date field<br>3. Click 'Submit' button | prevents journal entries from being posted for dates on or before the closing date | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Office field blank in the Add Journal Entry form |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 |  | Leave the Transaction Date field blank in the Add Journal Entry form |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Transaction Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-008 |  | Leave the GL Account field blank in an Entry Line |  | 1. Click on '+ Add Journal Entry'<br>2. Fill in all required fields except for the GL Account in the first Entry Line<br>3. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-009 |  | Leave the Amount field blank in an Entry Line |  | 1. Click on '+ Add Journal Entry'<br>2. Fill in all required fields and leave the Amount field blank in the first Entry Line<br>3. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-010 |  | Submit with total debits not equal to total credits |  | 1. Click on '+ Add Journal Entry'<br>2. Fill in all required fields with total debits as <amount> and total credits as <amount less than total debits><br>3. Click Submit | Form does not submit; total debits must equal total credits error is shown | high |
| TC-011 |  | Leave the Office field blank in the Create Closure form |  | 1. Click on '+ Create Closure'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-012 |  | Leave the Closing Date field blank in the Create Closure form |  | 1. Click on '+ Create Closure'<br>2. Leave the Closing Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Closing Date field indicating it is required | high |
| TC-013 |  | Attempt to create a closure with a Closing Date before existing journal entries |  | 1. Click on '+ Create Closure'<br>2. Fill in all required fields with a Closing Date on or before the date of existing journal entries<br>3. Click Submit | Form does not submit; journal entries cannot be posted for dates on or before the closing date error is shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Ensure total debits equal total credits at the boundary | User is on the Add Journal Entry Form | 1. Add an entry line with GL Account and Amount as 100<br>2. Add another entry line with GL Account and Amount as 100<br>3. Click Submit | Form submits successfully; journal entry is created with total debits equal to total credits | medium |
| TC-015 (boundary) |  | Attempt submission with total debits less than total credits | User is on the Add Journal Entry Form | 1. Add an entry line with GL Account and Amount as 100<br>2. Add another entry line with GL Account and Amount as 50<br>3. Click Submit | Submission is blocked; error shown indicating 'Total debits must equal total credits' | medium |
| TC-016 (boundary) |  | Add maximum allowed entries to the Entry Lines repeating group | User is on the Add Journal Entry Form | 1. Add the maximum number of entry lines allowed<br>2. Click Submit | Form submits successfully; journal entry is created with maximum entry lines | medium |
| TC-017 (boundary) |  | Attempt to add one more entry line beyond the maximum allowed | User is on the Add Journal Entry Form | 1. Add the maximum number of entry lines allowed<br>2. Attempt to add one more entry line<br>3. Click Submit | Submission is blocked; error shown indicating maximum entry limit reached | medium |
| TC-018 (data_edge) |  | Test with today's date in Transaction Date field | User is on the Add Journal Entry Form | 1. Enter today's date in the Transaction Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; journal entry is created with today's date | medium |
| TC-019 (data_edge) |  | Test with a future date in Closing Date field | User is on the Create Closure Form | 1. Enter a future date in the Closing Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; closure is created with future date | medium |
| TC-020 (data_edge) |  | Test with a past date in Closing Date field | User is on the Create Closure Form | 1. Enter a past date in the Closing Date field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating closure cannot be created for past dates | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **15** (positive: 6, negative: 3, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new accounting rule successfully | User logged in as <Role> | 1. Click '+ Create Rule' button<br>2. Enter <valid rule name> in the Rule Name field<br>3. Select 'All Offices' from the Office dropdown<br>4. Click '+ Create Rule' button | A success notification is displayed; the accounting rule is listed in the Accounting Rules Table | high |
| TC-002 | WF-001 | Create a new financial activity mapping successfully | User logged in as <Role> | 1. Click '+ Create Mapping' button<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select <valid GL account> from the GL Account dropdown<br>4. Click '+ Create Mapping' button | A success notification is displayed; the financial activity mapping is listed in the Financial Activity Mappings Table | high |
| TC-003 | WF-002 | Edit an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule in the Accounting Rules Table<br>2. Click 'Edit' button<br>3. Change <field> to <new value><br>4. Click '+ Create Rule' button | A success notification is displayed; the accounting rule updates are reflected in the Accounting Rules Table | medium |
| TC-004 | WF-002 | Delete an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule in the Accounting Rules Table<br>2. Click 'Delete' button<br>3. Confirm deletion | The accounting rule is no longer present in the Accounting Rules Table | medium |
| TC-005 | WF-003 | Verify sortable columns in Accounting Rules Table | User logged in as <Role> | 1. Click on the 'Rule Name' column header<br>2. Observe the order of rows in the Accounting Rules Table<br>3. Click on the 'Office' column header<br>4. Observe the order of rows in the Accounting Rules Table | Rows in the Accounting Rules Table are sorted correctly by the selected column | low |
| TC-006 | WF-003 | Verify sortable columns in Financial Activity Mappings Table | User logged in as <Role> | 1. Click on the 'Financial Activity' column header<br>2. Observe the order of rows in the Financial Activity Mappings Table<br>3. Click on the 'GL Account' column header<br>4. Observe the order of rows in the Financial Activity Mappings Table | Rows in the Financial Activity Mappings Table are sorted correctly by the selected column | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Rule Name field blank and submit the Create Rule form |  | 1. Open the Create Rule form<br>2. Leave the Rule Name field blank<br>3. Click + Create Rule | Inline validation error appears on the Rule Name field indicating it is required | high |
| TC-008 |  | Leave all required fields blank and submit the Create Mapping form |  | 1. Open the Create Mapping form<br>2. Leave the Financial Activity field blank<br>3. Leave the GL Account field blank<br>4. Click + Create Mapping | Inline validation error appears on the Financial Activity field indicating it is required; Inline validation error appears on the GL Account field indicating it is required | high |
| TC-009 |  | Attempt to create a mapping with a duplicate Financial Activity |  | 1. Open the Create Mapping form<br>2. Select an existing Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click + Create Mapping<br>5. Open the Create Mapping form again<br>6. Select the same Financial Activity from the dropdown<br>7. Select a different GL Account from the dropdown<br>8. Click + Create Mapping | Form does not submit; error shown indicating that the Financial Activity must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter minimum length Rule Name |  | 1. Enter a single character in the Rule Name field<br>2. Click + Create Rule | Form submits successfully; entity is created with the minimum length Rule Name | medium |
| TC-011 (boundary) |  | Enter maximum length Rule Name |  | 1. Enter a string of maximum allowed length in the Rule Name field<br>2. Click + Create Rule | Form submits successfully; entity is created with the maximum length Rule Name | medium |
| TC-012 (boundary) |  | Add maximum allowed entries in Debit Tags/Debit Account |  | 1. Open the Create Rule Form<br>2. Add maximum allowed entries in the Debit Tags/Debit Account multi-select<br>3. Click + Create Rule | Form submits successfully with maximum allowed entries in the Debit Tags/Debit Account | medium |
| TC-013 (boundary) |  | Attempt to add one more entry in Debit Tags/Debit Account |  | 1. Open the Create Rule Form<br>2. Add maximum allowed entries in the Debit Tags/Debit Account multi-select<br>3. Attempt to add one more entry<br>4. Click + Create Rule | Submission is blocked; error shown indicating maximum entries exceeded | medium |
| TC-014 (input_edge) |  | Enter long text in Rule Name |  | 1. Enter a very long string (200+ characters) in the Rule Name field<br>2. Click + Create Rule | Form submission is either accepted or rejected with a visible indicator | low |
| TC-015 (input_edge) |  | Enter special characters in Rule Name |  | 1. Enter special characters in the Rule Name field<br>2. Click + Create Rule | Form submission is either accepted or rejected with a specific error shown | low |

---

## Provisioning

Total: **18** (positive: 5, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form from Provisioning Criteria page | User logged in as <Role> | 1. Click '+ Create' button on the Provisioning Criteria page | Creation form opens | high |
| TC-002 | WF-001 | Submit creation form with valid data | User logged in as <Role>, Creation form is open | 1. Enter <Criteria Name> in the Criteria Name field<br>2. Click 'Add Row' in the Definitions table<br>3. Enter <Loan_Product> in the Loan Product field<br>4. Select 'STANDARD' from the Category dropdown<br>5. Enter <Minimum Age> in the Minimum Age field<br>6. Enter <Maximum Age> in the Maximum Age field<br>7. Enter <Provisioning Percentage> in the Provisioning Percentage field<br>8. Select <Liability Account> from the Liability Account dropdown<br>9. Select <Expense Account> from the Expense Account dropdown<br>10. Click 'Submit' on the creation form | The new criteria is displayed in the Provisioning Criteria table | high |
| TC-003 | WF-002 | Generate new provisioning entries | User logged in as <Role>, Provisioning criteria are configured | 1. Click '+ Create Provisioning Entry' button on the Provisioning Entries page | New provisioning entries are generated based on current loan portfolio status | high |
| TC-004 | WF-002 | Review provisioning entry details | User logged in as <Role>, Provisioning entries are generated | 1. Click 'Review' on a provisioning entry in the Provisioning Entries table | Detailed breakdown by loan product and category is displayed | medium |
| TC-005 | WF-002 | Recreate a provisioning entry | User logged in as <Role>, Provisioning entries are generated | 1. Click 'Recreate' on a provisioning entry in the Provisioning Entries table | The provisioning entry is recreated and displayed in the Provisioning Entries table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave Criteria Name blank and submit |  | 1. Click on '+ Create' to open the creation form<br>2. Leave the Criteria Name field blank<br>3. Fill all other required fields in the Definitions table<br>4. Click Submit | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-007 |  | Leave all required fields empty and submit |  | 1. Click on '+ Create' to open the creation form<br>2. Leave all required fields in the Definitions table blank<br>3. Leave the Criteria Name field blank<br>4. Click Submit | Inline validation errors appear on the Criteria Name field and all required fields in the Definitions table indicating they are required | high |
| TC-008 |  | Enter non-numeric value in Minimum Age field |  | 1. Click on '+ Create' to open the creation form<br>2. Enter <non-numeric value> in the Minimum Age field<br>3. Fill all other required fields in the Definitions table<br>4. Click Submit | Inline validation error appears on the Minimum Age field indicating it must be a number | medium |
| TC-009 |  | Enter non-numeric value in Maximum Age field |  | 1. Click on '+ Create' to open the creation form<br>2. Enter <non-numeric value> in the Maximum Age field<br>3. Fill all other required fields in the Definitions table<br>4. Click Submit | Inline validation error appears on the Maximum Age field indicating it must be a number | medium |
| TC-010 |  | Enter Provisioning Percentage exceeding 100 |  | 1. Click on '+ Create' to open the creation form<br>2. Fill all required fields in the Definitions table<br>3. Enter <amount exceeding 100> in the Provisioning Percentage field<br>4. Click Submit | Inline validation error appears on the Provisioning Percentage field indicating it must be a valid percentage | medium |
| TC-011 |  | Enter Maximum Age less than Minimum Age |  | 1. Click on '+ Create' to open the creation form<br>2. Fill all required fields in the Definitions table<br>3. Enter <value for Minimum Age> in the Minimum Age field<br>4. Enter <value less than Minimum Age> in the Maximum Age field<br>5. Click Submit | Inline validation error appears indicating Maximum Age must be greater than Minimum Age | medium |
| TC-012 |  | Attempt to create provisioning entry without configured criteria |  | 1. Click on '+ Create Provisioning Entry'<br>2. Observe the state of the system without any configured criteria | Page displays an error: 'No configured criteria available to create provisioning entries' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Add minimum required Definitions row | User is on the Creation Form | 1. Click on the '+ Create' button<br>2. Fill in the Criteria Name field with a valid name<br>3. Add 1 row to the Definitions table with valid inputs for all fields | Form submits successfully; new criteria is created with 1 definition row | medium |
| TC-014 (boundary) |  | Attempt to add one more Definitions row than allowed | User is on the Creation Form with 1 Definitions row | 1. Click on the '+ Create' button<br>2. Fill in the Criteria Name field with a valid name<br>3. Add 2 rows to the Definitions table | Submission is blocked; a visible error indicates that only 1 row is allowed | medium |
| TC-015 (boundary) |  | Enter minimum value for Minimum Age | User is on the Creation Form | 1. Click on the '+ Create' button<br>2. Fill in the Criteria Name field with a valid name<br>3. Add a row to the Definitions table<br>4. Enter the minimum allowed value in the Minimum Age field | Form submits successfully; the Minimum Age is accepted | medium |
| TC-016 (boundary) |  | Enter one unit below minimum for Minimum Age | User is on the Creation Form | 1. Click on the '+ Create' button<br>2. Fill in the Criteria Name field with a valid name<br>3. Add a row to the Definitions table<br>4. Enter one unit below the minimum allowed value in the Minimum Age field | Submission is blocked; a visible error indicates that the age is below the minimum allowed | medium |
| TC-017 (input_edge) |  | Enter a long string in the Criteria Name field | User is on the Creation Form | 1. Click on the '+ Create' button<br>2. Enter a long string (over 200 characters) in the Criteria Name field | Form submission is either accepted or an error is shown indicating the string is too long | low |
| TC-018 (input_edge) |  | Enter special characters in the Criteria Name field | User is on the Creation Form | 1. Click on the '+ Create' button<br>2. Enter special characters (e.g., @#$%^&*) in the Criteria Name field | Form submission is either accepted or an error is shown indicating invalid characters | low |

---

## Offices

Total: **12** (positive: 2, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new office successfully | User logged in as <Admin>, User is on the Offices page | 1. Click + Create Office button<br>2. Enter <valid office name> in the Office Name field<br>3. Select <valid parent office> from the Parent Office dropdown<br>4. Enter <valid opening date> in the Opened On Date field<br>5. Click Submit | A success notification is displayed; the new office appears in the Offices table with the entered Office Name | high |
| TC-002 |  | Access office detail page by clicking office name | User logged in as <Admin>, User is on the Offices page | 1. Click on the Office Name link of an existing office | The Office Detail page shows the information for the selected office | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Office Name field blank and submit |  | 1. Leave the Office_Name field blank<br>2. Fill in the Parent_Office field with a valid value<br>3. Fill in the Opened_On_Date field with a valid date<br>4. Click the + Create Office button | Inline validation error appears on the Office_Name field indicating it is required | high |
| TC-004 |  | Leave the Parent Office field blank and submit |  | 1. Fill in the Office_Name field with a valid value<br>2. Leave the Parent_Office field blank<br>3. Fill in the Opened_On_Date field with a valid date<br>4. Click the + Create Office button | Inline validation error appears on the Parent_Office field indicating it is required | high |
| TC-005 |  | Leave the Opened On Date field blank and submit |  | 1. Fill in the Office_Name field with a valid value<br>2. Fill in the Parent_Office field with a valid value<br>3. Leave the Opened_On_Date field blank<br>4. Click the + Create Office button | Inline validation error appears on the Opened_On_Date field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the Office_Name field blank<br>2. Leave the Parent_Office field blank<br>3. Leave the Opened_On_Date field blank<br>4. Click the + Create Office button | Form does not submit; errors shown on Office_Name, Parent_Office, and Opened_On_Date fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Enter minimum required characters in Office Name |  | 1. Enter exactly 1 character in the Office Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; entity is created with the Office Name containing 1 character | medium |
| TC-008 (boundary) |  | Enter maximum length in Office Name |  | 1. Enter exactly 255 characters in the Office Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; entity is created with the Office Name containing 255 characters | medium |
| TC-009 (boundary) |  | Enter one character less than minimum required in Office Name |  | 1. Enter 0 characters in the Office Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Submission is blocked; inline error shows 'Office Name is required' | medium |
| TC-010 (boundary) |  | Enter an invalid date in Opened On Date |  | 1. Enter a date that is in the future in the Opened On Date field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Submission is blocked; inline error shows 'Opened On Date cannot be in the future' | medium |
| TC-011 (input_edge) |  | Enter a very long string in Office Name |  | 1. Enter a string of 300 characters in the Office Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Submission is blocked; inline error shows 'Office Name exceeds maximum length' | low |
| TC-012 (input_edge) |  | Enter special characters in Office Name |  | 1. Enter special characters in the Office Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; entity is created with the Office Name containing special characters | low |

---

## Employees

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open Create Employee form | User logged in as <Admin> | 1. Click the '+ Create Employee' button | The creation form opens | high |
| TC-002 |  | Submit Create Employee form with valid data | User logged in as <Admin>, Creation form is open | 1. Enter <Office> in the Office field<br>2. Enter <First Name> in the First Name field<br>3. Enter <Last Name> in the Last Name field<br>4. Click Submit | A success notification is displayed; the employee is added to the Employees table | high |
| TC-003 |  | Edit an employee's details | User logged in as <Admin>, Employees table is displayed | 1. Click on the Name link of an employee in the Employees table<br>2. Click the Edit option<br>3. Modify <First Name> in the First Name field<br>4. Click Submit | The employee's details are updated and displayed in the Employees table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Office field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Fill in First Name and Last Name with valid values<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-005 |  | Leave the First Name field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the First Name field blank<br>3. Fill in Office and Last Name with valid values<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-006 |  | Leave the Last Name field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Last Name field blank<br>3. Fill in Office and First Name with valid values<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-007 |  | Submit the Create Employee form with all required fields empty |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office, First Name, and Last Name fields blank<br>3. Click Submit | Form does not submit; errors shown on Office, First Name, and Last Name fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long string in the First Name field | User is on the Create Employee form | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates the First Name exceeds the maximum length. | low |
| TC-009 (input_edge) |  | Enter special characters in the Last Name field | User is on the Create Employee form | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates invalid characters in the Last Name field. | low |
| TC-010 (data_edge) |  | Enter today's date in the Joining Date field | User is on the Create Employee form | 1. Enter today's date in the Joining Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; employee record is created with today's date in the Joining Date field. | medium |
| TC-011 (data_edge) |  | Enter yesterday's date in the Joining Date field | User is on the Create Employee form | 1. Enter yesterday's date in the Joining Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; employee record is created with yesterday's date in the Joining Date field. | medium |

---

## Teller & Cashier Management

Total: **19** (positive: 6, negative: 8, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new teller with all required fields | User logged in as <Admin> | 1. Click '+ Create Teller' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid teller name> in the Teller Name field<br>4. Enter <valid start date> in the Start Date field<br>5. Click Submit | A success notification is displayed; the Teller Name appears in the Tellers page data table | high |
| TC-002 | WF-001 | Create a new teller with optional fields filled | User logged in as <Admin> | 1. Click '+ Create Teller' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid teller name> in the Teller Name field<br>4. Enter <valid start date> in the Start Date field<br>5. Enter <valid end date> in the End Date field<br>6. Select 'Active' from the Status dropdown<br>7. Enter <valid description> in the Description field<br>8. Click Submit | A success notification is displayed; the Teller Name appears in the Tellers page data table | high |
| TC-003 | WF-002 | Edit an existing teller | User logged in as <Admin>, At least one teller exists in the Tellers page | 1. Click the Edit action for the existing teller<br>2. Update the Description field with <new valid description><br>3. Click Submit | A success notification is displayed; the updated description is visible in the Teller Detail page | medium |
| TC-004 | WF-003 | Allocate a cashier to a teller | User logged in as <Admin>, At least one teller exists in the Tellers page | 1. Click '+ Allocate Cashier' button<br>2. Select <valid staff> from the Staff dropdown<br>3. Enter <valid start date> in the Start Date field<br>4. Click Submit | A success notification is displayed; the Cashier Name appears in the Cashiers section of the Teller Detail page | high |
| TC-005 | WF-004 | Allocate cash to a cashier | User logged in as <Admin>, At least one cashier exists in the Cashier Detail page | 1. Click 'Allocate Cash' action for the cashier<br>2. Enter <valid amount> in the Amount field<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click Submit | A success notification is displayed; the Cash In Hand updates to reflect the allocated amount | high |
| TC-006 | WF-005 | Settle cash for a cashier | User logged in as <Admin>, At least one cashier exists in the Cashier Detail page | 1. Click 'Settle Cash' action for the cashier<br>2. Enter <valid amount> in the Amount field<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click Submit | A success notification is displayed; the Cash In Hand updates to reflect the settled amount | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Office field blank when creating a teller |  | 1. Open the Create Teller form<br>2. Leave the Office field blank<br>3. Fill in the Teller Name, Start Date, and all other fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-008 |  | Leave the Teller Name field blank when creating a teller |  | 1. Open the Create Teller form<br>2. Leave the Teller Name field blank<br>3. Fill in the Office, Start Date, and all other fields<br>4. Click Submit | Inline validation error appears on the Teller Name field indicating it is required | high |
| TC-009 |  | Leave the Start Date field blank when creating a teller |  | 1. Open the Create Teller form<br>2. Leave the Start Date field blank<br>3. Fill in the Office, Teller Name, and all other fields<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 |  | Leave all required fields blank when creating a teller |  | 1. Open the Create Teller form<br>2. Leave the Office, Teller Name, and Start Date fields blank<br>3. Click Submit | Inline validation errors appear on the Office, Teller Name, and Start Date fields indicating they are required | high |
| TC-011 |  | Attempt to allocate a cashier without filling the Staff field |  | 1. Open the Allocate Cashier form<br>2. Leave the Staff field blank<br>3. Fill in the Start Date and all other fields<br>4. Click Submit | Inline validation error appears on the Staff field indicating it is required | high |
| TC-012 |  | Attempt to settle cash without filling the Amount field |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash<br>3. Leave the Amount field blank<br>4. Fill in the Currency and Transaction Date fields<br>5. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-013 |  | Attempt to settle cash without filling the Currency field |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash<br>3. Leave the Currency field blank<br>4. Fill in the Amount and Transaction Date fields<br>5. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-014 |  | Attempt to settle cash without filling the Transaction Date field |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash<br>3. Leave the Transaction Date field blank<br>4. Fill in the Amount and Currency fields<br>5. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Start Date equals End Date | Create Teller Form is open | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller Name field<br>3. Enter a valid description in the Description field<br>4. Enter today's date in the Start Date field<br>5. Enter today's date in the End Date field | Form submits successfully; teller is created with Start Date and End Date being the same | medium |
| TC-016 (boundary) |  | End Date is one day before Start Date | Create Teller Form is open | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller Name field<br>3. Enter a valid description in the Description field<br>4. Enter tomorrow's date in the Start Date field<br>5. Enter today's date in the End Date field | Form submission is blocked; error shown indicating End Date must be after Start Date | medium |
| TC-017 (input_edge) |  | Enter a very long description | Create Teller Form is open | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller Name field<br>3. Enter a string of 200+ characters in the Description field | Description field accepts the input without truncation or shows an error if there's a limit | low |
| TC-018 (input_edge) |  | Enter special characters in Teller Name | Create Teller Form is open | 1. Enter a valid value in the Office field<br>2. Enter special characters in the Teller Name field<br>3. Enter a valid description in the Description field<br>4. Enter today's date in the Start Date field | Form submission is blocked; error shown indicating invalid characters in Teller Name | low |
| TC-019 (interaction_edge) |  | Rapid re-submission after creating a teller | Create Teller Form is open | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller Name field<br>3. Enter a valid description in the Description field<br>4. Enter today's date in the Start Date field<br>5. Click Submit<br>6. Immediately click Submit again after the success message | Second submission attempt is blocked; the form remains blank without pre-filled data | medium |

---

## Users & Roles

Total: **20** (positive: 3, negative: 12, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new user successfully | User logged in as <Admin> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <same valid password> in the Repeat Password field<br>9. Click 'Submit' button | A success notification is displayed; the new user appears in the Users table with the entered Username. | high |
| TC-002 |  | View user details | User logged in as <Admin>, At least one user exists in the Users table | 1. Click on the Username link of the first user in the Users table | User detail page displays the selected user's information. | medium |
| TC-003 |  | Create a new role successfully | User logged in as <Admin> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Enter <description> in the Description field<br>4. Click 'Submit' button | A success notification is displayed; the new role appears in the Roles table with the entered Role Name. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-005 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-006 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-007 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-008 |  | Leave the Office field blank |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-009 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-010 |  | Leave the Repeat Password field blank |  | 1. Leave the Repeat Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repeat Password field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; all required fields are highlighted with validation errors | high |
| TC-012 |  | Enter an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Email field displays an error: 'Must be a valid email format' | medium |
| TC-013 |  | Enter a password that does not meet policy |  | 1. Enter <password that does not meet policy> in the Password field<br>2. Fill all other required fields<br>3. Click Submit | Password field displays an error: 'Password must meet password policy' | medium |
| TC-014 |  | Enter mismatched passwords |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Repeat Password field<br>3. Fill all other required fields<br>4. Click Submit | Repeat Password field displays an error: 'Passwords must match' | medium |
| TC-015 |  | Submit with a duplicate Username |  | 1. Enter <existing username> in the Username field<br>2. Fill all other required fields<br>3. Click Submit | Username field displays an error: 'Username must be unique' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) |  | Username uniqueness check at boundary | User with the username 'testuser' already exists | 1. Enter 'testuser' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; an error message displays indicating 'Username must be unique' | medium |
| TC-017 (boundary) |  | Email format validation at boundary | User with the email 'test@example.com' already exists | 1. Enter 'test@example.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; an error message displays indicating 'Email must be valid email format' | medium |
| TC-018 (input_edge) |  | Long username input |  | 1. Enter a string of 200 characters in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; an error message displays indicating the username is too long | low |
| TC-019 (input_edge) |  | Special characters in Username |  | 1. Enter '@username!' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; an error message displays indicating invalid characters in Username | low |
| TC-020 (input_edge) |  | Leading/trailing whitespace in Username |  | 1. Enter '  username  ' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Reports

Total: **14** (positive: 2, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open a report and generate it as a data table | User logged in as <User Role>, Reports page is open | 1. Click on the report 'Loans Awaiting Disbursal'<br>2. Fill in the Office field with <valid office><br>3. Fill in the Branch field with <valid branch><br>4. Fill in the Currency field with <valid currency><br>5. Fill in the Loan Product field with <valid loan product><br>6. Fill in the Date Range field with <valid date range><br>7. Fill in the Loan Officer field with <valid loan officer><br>8. Fill in the Fund field with <valid fund><br>9. Click 'Run Report' | generates the report as a data table | high |
| TC-002 |  | Open a report and check output options | User logged in as <User Role>, Reports page is open | 1. Click on the report 'Active Loans Summary'<br>2. Fill in the Office field with <valid office><br>3. Fill in the Branch field with <valid branch><br>4. Fill in the Currency field with <valid currency><br>5. Fill in the Loan Product field with <valid loan product><br>6. Fill in the Date Range field with <valid date range><br>7. Fill in the Loan Officer field with <valid loan officer><br>8. Fill in the Fund field with <valid fund><br>9. Click 'Run Report'<br>10. Verify the Output Options dropdown is visible | The Output Options dropdown is visible with options: View on Screen, Export to Excel, Export to CSV, Export to PDF | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Office field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Office field indicating it is required | high |
| TC-004 |  | Leave the Branch field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Branch field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Branch field indicating it is required | high |
| TC-005 |  | Leave the Currency field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Currency field indicating it is required | high |
| TC-006 |  | Leave the Loan Product field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Loan Product field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Loan Product field indicating it is required | high |
| TC-007 |  | Leave the Date Range field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Date Range field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Date Range field indicating it is required | high |
| TC-008 |  | Leave the Loan Officer field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Loan Officer field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-009 |  | Leave the Fund field blank and submit |  | 1. Open the report parameters form<br>2. Leave the Fund field blank<br>3. Fill all other required fields<br>4. Click Run Report | Inline validation error appears on the Fund field indicating it is required | high |
| TC-010 |  | Submit with all required fields empty |  | 1. Open the report parameters form<br>2. Leave all required fields empty<br>3. Click Run Report | Form does not submit; all required fields are highlighted with validation errors | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long string in the Office field |  | 1. Click on the report to open the Parameters Form<br>2. Enter a string of 200+ characters in the Office field<br>3. Fill all other required fields with valid data<br>4. Click 'Run Report' | Form submits successfully; report is generated as a data table | low |
| TC-012 (input_edge) |  | Enter special characters in the Branch field |  | 1. Click on the report to open the Parameters Form<br>2. Enter special characters in the Branch field<br>3. Fill all other required fields with valid data<br>4. Click 'Run Report' | Inline error shown indicating invalid input in the Branch field | low |
| TC-013 (input_edge) |  | Enter leading/trailing whitespace in the Currency field |  | 1. Click on the report to open the Parameters Form<br>2. Enter '  USD  ' (with spaces) in the Currency field<br>3. Fill all other required fields with valid data<br>4. Click 'Run Report' | Leading/trailing whitespace is trimmed; saved value shown in the report reflects 'USD' | low |
| TC-014 (input_edge) |  | Enter a zero value in the Loan Product field |  | 1. Click on the report to open the Parameters Form<br>2. Enter '0' in the Loan Product field<br>3. Fill all other required fields with valid data<br>4. Click 'Run Report' | Inline error shown indicating that the Loan Product field cannot be zero | low |

---

## Account Transfers & Standing Instructions

Total: **16** (positive: 6, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient for the transfer | 1. Enter <From Office> in the From Office field<br>2. Enter <From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <From Account> in the From Account field<br>5. Enter <To Office> in the To Office field<br>6. Enter <To Client> in the To Client field<br>7. Select 'Loan Account' from the To Account Type dropdown<br>8. Enter <To Account> in the To Account field<br>9. Enter <Transfer Amount> in the Transfer Amount field<br>10. Enter <Transfer Date> in the Transfer Date field<br>11. Enter <Description> in the Description field<br>12. Click Submit | The transfer is processed, debiting the source and crediting the destination | high |
| TC-002 |  | Display standing instructions in the table | User logged in as <Role> | 1. Navigate to the Standing Instructions page | The Standing Instructions table displays columns for Name, From Client, From Account, To Client, To Account, Amount, Validity, and Status | medium |
| TC-003 |  | Create a standing instruction with valid data | User logged in as <Role> | 1. Click '+ Create Standing Instruction'<br>2. Enter <Name> in the Name field<br>3. Enter <From Account> in the From Account field<br>4. Enter <To Account> in the To Account field<br>5. Select <Transfer Type> in the Transfer Type field<br>6. Enter <Priority> in the Priority field<br>7. Select 'Fixed' from the Instruction Type dropdown<br>8. Enter <Amount> in the Amount field<br>9. Enter <Validity From> in the Validity From field<br>10. Enter <Validity Till> in the Validity Till field<br>11. Select 'Periodic' from the Recurrence Type dropdown<br>12. Enter <Recurrence Frequency> in the Recurrence Frequency field<br>13. Enter <Recurrence Interval> in the Recurrence Interval field<br>14. Click Submit | The standing instruction is created and appears in the Standing Instructions table | high |
| TC-004 | WF-001 | Enable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Navigate to the Standing Instructions page<br>2. Click Enable on the first standing instruction | The standing instruction status updates to 'Active' | medium |
| TC-005 | WF-002 | Disable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Navigate to the Standing Instructions page<br>2. Click Disable on the first standing instruction | The standing instruction status updates to 'Disabled' | medium |
| TC-006 | WF-003 | Delete a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Navigate to the Standing Instructions page<br>2. Click Delete on the first standing instruction<br>3. Confirm the deletion | The standing instruction is removed from the Standing Instructions table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Submit transfer with Transfer Amount exceeding available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Enter a valid date in the Transfer Date field<br>3. Click Submit | Form does not submit; error shown on Transfer Amount field indicating 'Transfer amount exceeds available balance' | high |
| TC-008 |  | Leave Transfer Amount blank and submit |  | 1. Leave the Transfer Amount field blank<br>2. Enter a valid date in the Transfer Date field<br>3. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-009 |  | Leave Transfer Date blank and submit |  | 1. Enter a valid amount in the Transfer Amount field<br>2. Leave the Transfer Date field blank<br>3. Click Submit | Inline validation error appears on the Transfer Date field indicating it is required | high |
| TC-010 |  | Submit Create Standing Instruction form with Name field blank |  | 1. Leave the Name field blank<br>2. Click Submit | Inline validation error appears on the Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Transfer Amount equals available balance | User has an available balance equal to the transfer amount | 1. Enter the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; transfer is processed | medium |
| TC-012 (boundary) |  | Transfer Amount exceeds available balance | User has an available balance | 1. Enter an amount greater than the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Error is shown indicating the transfer amount exceeds the available balance | medium |
| TC-013 (boundary) |  | Transfer Date is today's date |  | 1. Enter today's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; transfer is processed | medium |
| TC-014 (boundary) |  | Transfer Date is yesterday's date |  | 1. Enter yesterday's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; transfer is processed | medium |
| TC-015 (input_edge) |  | Enter a long description |  | 1. Enter a very long string (200+ characters) in the Description field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; transfer is processed with the long description saved | low |
| TC-016 (input_edge) |  | Enter special characters in the Name field |  | 1. Enter special characters (e.g., @#$%^&) in the Name field of Create Standing Instruction Form<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; standing instruction is created with special characters in the Name | low |

---

## Tax Management

Total: **17** (positive: 4, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new tax component with all required fields filled | User logged in as <Admin> | 1. Click '+ Create Tax Component' button<br>2. Enter <valid name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Enter <valid debit account> in the Debit Account field<br>6. Select <valid credit account type> from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Enter <valid start date> in the Start Date field<br>9. Click Submit | A success notification is displayed; the new tax component appears in the Tax Components Table with the entered Name and Percentage | high |
| TC-002 |  | View a tax component from the Tax Components Table | User logged in as <Admin>, At least one tax component exists in the Tax Components Table | 1. Click the Name link of the first tax component in the Tax Components Table | The Tax Component Detail page is displayed with the details of the selected tax component | medium |
| TC-003 |  | Create a new tax group with all required fields filled | User logged in as <Admin> | 1. Click '+ Create Tax Group' button<br>2. Enter <valid group name> in the Name field<br>3. Click 'Add Tax Component'<br>4. Enter <valid start date> in the Start Date field of the new component<br>5. Click Submit | A success notification is displayed; the new tax group appears in the Tax Groups Table with the entered Name | high |
| TC-004 |  | View a tax group from the Tax Groups Table | User logged in as <Admin>, At least one tax group exists in the Tax Groups Table | 1. Click the Name link of the first tax group in the Tax Groups Table | The Tax Group Detail page is displayed with the details of the selected tax group | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Name field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Name field blank<br>3. Fill in the Percentage field with a valid value<br>4. Select a Debit Account Type<br>5. Fill in the Start Date<br>6. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Leave the Percentage field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Fill in the Name field with a valid value<br>3. Leave the Percentage field blank<br>4. Select a Debit Account Type<br>5. Fill in the Start Date<br>6. Click Submit | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-007 |  | Leave the Start Date field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Fill in the Name field with a valid value<br>3. Fill in the Percentage field with a valid value<br>4. Select a Debit Account Type<br>5. Leave the Start Date field blank<br>6. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-008 |  | Leave all required fields blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Name field blank<br>3. Leave the Percentage field blank<br>4. Leave the Start Date field blank<br>5. Click Submit | Form does not submit; errors shown on Name, Percentage, and Start Date fields indicating they are required | high |
| TC-009 |  | Leave the Name field blank in Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Leave the Name field blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 |  | Leave the Start Date field blank in Tax Components section of Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Fill in the Name field with a valid value<br>3. Add a Tax Component<br>4. Leave the Start Date field blank<br>5. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-011 |  | Leave all required fields blank in Tax Components section of Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Fill in the Name field with a valid value<br>3. Add a Tax Component<br>4. Leave the Start Date field blank<br>5. Click Submit | Form does not submit; error shown on Start Date field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Enter exactly 0% in the Percentage field | User is on the Create Tax Component Form | 1. Enter 'Tax Component Name' in the Name field<br>2. Enter '0' in the Percentage field<br>3. Select 'Asset' in the Debit Account Type dropdown<br>4. Enter 'Debit Account 1' in the Debit Account field<br>5. Enter 'Credit Account Type 1' in the Credit Account Type field<br>6. Enter 'Credit Account 1' in the Credit Account field<br>7. Enter today's date in the Start Date field<br>8. Click Submit | Form submits successfully; entity is created with the Percentage value of 0% | medium |
| TC-013 (boundary) |  | Enter exactly 100% in the Percentage field | User is on the Create Tax Component Form | 1. Enter 'Tax Component Name' in the Name field<br>2. Enter '100' in the Percentage field<br>3. Select 'Asset' in the Debit Account Type dropdown<br>4. Enter 'Debit Account 1' in the Debit Account field<br>5. Enter 'Credit Account Type 1' in the Credit Account Type field<br>6. Enter 'Credit Account 1' in the Credit Account field<br>7. Enter today's date in the Start Date field<br>8. Click Submit | Form submits successfully; entity is created with the Percentage value of 100% | medium |
| TC-014 (boundary) |  | Add exactly 5 entries to the Tax Components repeating group | User is on the Create Tax Group Form | 1. Enter 'Tax Group Name' in the Name field<br>2. Add a Tax Component with today's date in the Start Date field<br>3. Add a Tax Component with today's date in the Start Date field<br>4. Add a Tax Component with today's date in the Start Date field<br>5. Add a Tax Component with today's date in the Start Date field<br>6. Add a Tax Component with today's date in the Start Date field<br>7. Click Submit | Form submits successfully with 5 Tax Components added | medium |
| TC-015 (boundary) |  | Attempt to add 6 entries to the Tax Components repeating group | User is on the Create Tax Group Form | 1. Enter 'Tax Group Name' in the Name field<br>2. Add a Tax Component with today's date in the Start Date field<br>3. Add a Tax Component with today's date in the Start Date field<br>4. Add a Tax Component with today's date in the Start Date field<br>5. Add a Tax Component with today's date in the Start Date field<br>6. Add a Tax Component with today's date in the Start Date field<br>7. Add a Tax Component with today's date in the Start Date field<br>8. Click Submit | Submission is blocked; visible error indicates the maximum number of entries is exceeded | medium |
| TC-016 (data_edge) |  | Enter today's date in the Start Date field | User is on the Create Tax Component Form | 1. Enter 'Tax Component Name' in the Name field<br>2. Enter '20' in the Percentage field<br>3. Select 'Asset' in the Debit Account Type dropdown<br>4. Enter 'Debit Account 1' in the Debit Account field<br>5. Enter 'Credit Account Type 1' in the Credit Account Type field<br>6. Enter 'Credit Account 1' in the Credit Account field<br>7. Enter today's date in the Start Date field<br>8. Click Submit | Form submits successfully; entity is created with today's date as the Start Date | medium |
| TC-017 (data_edge) |  | Enter yesterday's date in the Start Date field | User is on the Create Tax Component Form | 1. Enter 'Tax Component Name' in the Name field<br>2. Enter '20' in the Percentage field<br>3. Select 'Asset' in the Debit Account Type dropdown<br>4. Enter 'Debit Account 1' in the Debit Account field<br>5. Enter 'Credit Account Type 1' in the Credit Account Type field<br>6. Enter 'Credit Account 1' in the Credit Account field<br>7. Enter yesterday's date in the Start Date field<br>8. Click Submit | Form submits successfully; entity is created with yesterday's date as the Start Date | medium |

---

## Organization Settings

Total: **15** (positive: 5, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new holiday with valid details | User logged in as <Admin> | 1. Navigate to the Holidays page<br>2. Click '+ Create Holiday'<br>3. Enter <Holiday Name> in the Name field<br>4. Select <Start Date> in the From_Date field<br>5. Select <To Date> in the To_Date field<br>6. Click Submit | A success notification is displayed; the new holiday appears in the Holidays table with the entered Name, Start Date, and To Date | high |
| TC-002 |  | Set working days successfully | User logged in as <Admin> | 1. Navigate to the Working Days page<br>2. Check the boxes for Monday, Wednesday, and Friday<br>3. Click Save | A success notification is displayed; the selected working days are saved and reflected on the Working Days page | high |
| TC-003 |  | Create a new fund with valid details | User logged in as <Admin> | 1. Navigate to the Funds page<br>2. Click 'Create Fund'<br>3. Enter <Fund Name> in the Fund_Name field<br>4. Enter <External ID> in the External_ID field<br>5. Click Submit | A success notification is displayed; the new fund appears in the Funds table with the entered Fund Name and External ID | high |
| TC-004 |  | Create a new payment type with valid details | User logged in as <Admin> | 1. Navigate to the Payment Types page<br>2. Click '+ Create'<br>3. Enter <Payment Type Name> in the Name field<br>4. Enter <Description> in the Description field<br>5. Check the Is Cash Payment checkbox<br>6. Enter <Position> in the Position field<br>7. Click Submit | A success notification is displayed; the new payment type appears in the Payment Types table with the entered Name and Description | high |
| TC-005 |  | Upload a file for bulk import | User logged in as <Admin> | 1. Navigate to the Bulk Import page<br>2. Select <valid entity type> from the Entity_Types multi_select<br>3. Click 'Upload' and select a <valid file> from the OS dialog<br>4. Click Submit | A success notification is displayed; the file is uploaded successfully for the selected entity type | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Name field blank and submit the Create Holiday form |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill in valid dates for From Date and To Date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-007 |  | Leave the From Date field blank and submit the Create Holiday form |  | 1. Click on '+ Create Holiday'<br>2. Leave the From Date field blank<br>3. Fill in valid values for Name and To Date<br>4. Click Submit | Inline validation error appears on the From_Date field indicating it is required | high |
| TC-008 |  | Leave the To Date field blank and submit the Create Holiday form |  | 1. Click on '+ Create Holiday'<br>2. Leave the To Date field blank<br>3. Fill in valid values for Name and From Date<br>4. Click Submit | Inline validation error appears on the To_Date field indicating it is required | high |
| TC-009 |  | Submit Create Holiday form with all required fields empty |  | 1. Click on '+ Create Holiday'<br>2. Leave all required fields (Name, From Date, To Date) blank<br>3. Click Submit | Form does not submit; error shown on Name, From_Date, and To_Date fields indicating they are required | high |
| TC-010 |  | Enter an invalid date in the From Date field |  | 1. Click on '+ Create Holiday'<br>2. Enter <invalid date format> in the From_Date field<br>3. Fill in valid values for Name and To Date<br>4. Click Submit | Inline validation error appears on the From_Date field indicating it must be a valid date | medium |
| TC-011 |  | Enter an invalid date in the To Date field |  | 1. Click on '+ Create Holiday'<br>2. Enter <invalid date format> in the To_Date field<br>3. Fill in valid values for Name and From Date<br>4. Click Submit | Inline validation error appears on the To_Date field indicating it must be a valid date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Create Holiday with From_Date and To_Date on the same day |  | 1. Click on '+ Create Holiday'<br>2. Enter 'Holiday Name' in the Name field<br>3. Set From_Date to today's date<br>4. Set To_Date to today's date<br>5. Click Submit | Holiday is created successfully with From_Date and To_Date set to today's date | medium |
| TC-013 (boundary) |  | Create Holiday with To_Date before From_Date |  | 1. Click on '+ Create Holiday'<br>2. Enter 'Holiday Name' in the Name field<br>3. Set From_Date to tomorrow's date<br>4. Set To_Date to today's date<br>5. Click Submit | Submission is blocked; error message displayed indicating that To_Date must be on or after From_Date | medium |
| TC-014 (input_edge) |  | Create Holiday with long Name |  | 1. Click on '+ Create Holiday'<br>2. Enter a string longer than 200 characters in the Name field<br>3. Set From_Date to today's date<br>4. Set To_Date to tomorrow's date<br>5. Click Submit | Submission is blocked; error message displayed indicating the Name exceeds the maximum length | low |
| TC-015 (input_edge) |  | Create Holiday with special characters in Name |  | 1. Click on '+ Create Holiday'<br>2. Enter special characters in the Name field (e.g., @#$%^&*)<br>3. Set From_Date to today's date<br>4. Set To_Date to tomorrow's date<br>5. Click Submit | Holiday is created successfully with special characters in the Name field | low |

---

## System Administration

Total: **17** (positive: 4, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Toggle the global Start/Stop scheduler | User logged in as <Admin> | 1. Navigate to the Manage Scheduler Jobs page<br>2. Toggle the Start/Stop Scheduler switch | The scheduler is now <active/inactive> based on the toggle state | high |
| TC-002 |  | Open code values for a specific code | User logged in as <Admin> | 1. Navigate to the Manage Codes page<br>2. Click on the code 'Client Type' | displays values for adding, editing, reordering, and deactivating entries | high |
| TC-003 |  | Create a new data table with column definitions | User logged in as <Admin> | 1. Navigate to the Manage Data Tables page<br>2. Enter 'Custom Data Table' in the Data Table Name field<br>3. Select 'm_client' from the Application Table Name dropdown<br>4. Check the Multi Row checkbox<br>5. Click 'Add Row' in Column Definitions<br>6. Enter 'Column1' in the Name field<br>7. Select 'string' from the Type dropdown<br>8. Enter '50' in the Length field<br>9. Check the Is Mandatory checkbox<br>10. Check the Is Unique checkbox<br>11. Click Submit | The new data table 'Custom Data Table' is created with the specified column definitions | high |
| TC-004 |  | Display audit trails filtered by Action Name | User logged in as <Admin> | 1. Navigate to the Audit Trails page<br>2. Enter 'Create' in the Action Name filter<br>3. Click Apply Filter | Only audit trails with Action Name 'Create' are displayed; unrelated entries are no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Data Table Name blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Leave the Data Table Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Data Table Name field indicating it is required | high |
| TC-006 |  | Leave the Application Table Name dropdown unselected and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Leave the Application Table Name dropdown unselected<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Application Table Name field indicating it is required | high |
| TC-007 |  | Leave the Name field in Column Definitions blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Add a new column definition<br>3. Leave the Name field blank<br>4. Fill all other required fields in the column definition<br>5. Click Submit | Inline validation error appears on the Name field in Column Definitions indicating it is required | high |
| TC-008 |  | Submit with all required fields empty in Manage Data Tables |  | 1. Navigate to the Manage Data Tables page<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; error shown on Data Table Name, Application Table Name, and Column Definitions fields | high |
| TC-009 |  | Enter a non-numeric value in the Length field in Column Definitions |  | 1. Navigate to the Manage Data Tables page<br>2. Add a new column definition<br>3. Enter <non-numeric value> in the Length field<br>4. Fill all other required fields in the column definition<br>5. Click Submit | Inline validation error appears on the Length field indicating it must be a number | medium |
| TC-010 |  | Attempt to approve an action when maker-checker is not enabled |  | 1. Navigate to the Audit Trails page<br>2. Attempt to click the Approve button for a pending action | The Approve button is not visible or clickable; no action is taken | medium |
| TC-011 |  | Attempt to toggle the Start/Stop Scheduler when jobs are not scheduled |  | 1. Navigate to the Manage Scheduler Jobs page<br>2. Attempt to toggle the Start/Stop Scheduler | The toggle does not change state; no jobs are started or stopped | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Add maximum allowed column definitions | User is on the Manage Data Tables page, User has filled in all required fields | 1. Add maximum allowed entries to the Column Definitions repeating group | Form submits successfully; all column definitions are saved correctly | medium |
| TC-013 (boundary) |  | Attempt to add one more column definition than allowed | User is on the Manage Data Tables page, User has filled in all required fields | 1. Add maximum allowed entries to the Column Definitions repeating group<br>2. Attempt to add one more entry | Submission is blocked; visible error indicates maximum entries exceeded | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Data Table Name field | User is on the Manage Data Tables page | 1. Enter a string longer than 200 characters in the Data Table Name field | Input is either truncated or a visible error is shown indicating the length limit | low |
| TC-015 (input_edge) |  | Enter special characters in the Name field of Column Definitions | User is on the Manage Data Tables page, User has filled in all required fields | 1. Enter special characters in the Name field of a Column Definition | Input is accepted or a specific error is shown indicating invalid characters | low |
| TC-016 (interaction_edge) |  | Rapidly toggle the Start/Stop Scheduler action | User is on the Manage Scheduler Jobs page | 1. Click the Start/Stop Scheduler toggle<br>2. Immediately click the Start/Stop Scheduler toggle again | The action succeeds without errors; the toggle reflects the last action taken | medium |
| TC-017 (state_edge) |  | Check the behavior of the Global Configuration toggle when maker-checker is enabled | User is on the Global Configuration page, maker-checker is enabled | 1. Toggle the Enabled checkbox for a configuration<br>2. Attempt to toggle it again without completing the approval process | The toggle action is blocked; a message indicates the need for approval | medium |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User logs out successfully | User logged in as <User> | 1. Click the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User is redirected to the login page after the session is terminated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access an authenticated page after logout | User is logged in | 1. Click on the User Profile Icon<br>2. Select 'Log Out' | User is redirected to the login page; authenticated session is terminated | high |
| TC-003 |  | Attempt to navigate to Profile Settings after logout | User is logged out | 1. Click on the User Profile Icon<br>2. Select 'Profile Settings' | User is redirected to the login page; access to Profile Settings is blocked | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) |  | Rapid logout attempts after successful logout | User is logged in | 1. Click the user profile icon<br>2. Select 'Log Out'<br>3. Immediately click the user profile icon again<br>4. Select 'Log Out' again | Second logout attempt is blocked; user remains on the login page without session termination. | medium |
| TC-005 (interaction_edge) |  | Navigate to an authenticated page after logout | User is logged in, User has logged out | 1. Click the user profile icon<br>2. Select 'Log Out'<br>3. Attempt to navigate to an authenticated page | User is redirected to the login page. | medium |

---
