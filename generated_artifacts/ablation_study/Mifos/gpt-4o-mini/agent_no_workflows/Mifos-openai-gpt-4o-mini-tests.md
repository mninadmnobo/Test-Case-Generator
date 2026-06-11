# Test Cases — Mifos

Generated: 2026-06-10T19:15:11.496432Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 509 | 136 | 206 | 167 | 249 | 185 | 70 |

## Login

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User is on the Login page | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | User is redirected to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with a valid username<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both Username and Password fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Form does not submit; error shown on Username and Password fields indicating they are required | high |
| TC-005 |  | Submit with invalid credentials |  | 1. Fill the Username field with an invalid username<br>2. Fill the Password field with an invalid password<br>3. Click Login | Error displayed: 'invalid credentials' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Form submission is blocked; an error message indicates the username exceeds the maximum allowed length | low |
| TC-007 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter '@#$%^&*()' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Form submission is blocked; an error message indicates invalid characters in the Username field | low |
| TC-008 (input_edge) |  | Enter leading/trailing whitespace in Username |  | 1. Enter '   user   ' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Login | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |
| TC-009 (input_edge) |  | Enter zero-length password |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click Login | Form submission is blocked; an inline validation message indicates that the Password field is required | medium |

---

## Home Page

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Verify welcome message is displayed | User logged in as <User> | 1. Observe the Home page | The welcome card displays the message 'Welcome, mifos!' | high |
| TC-002 |  | Verify Search Activity input field is present | User logged in as <User> | 1. Observe the Home page | The 'Search Activity' input field is visible | medium |
| TC-003 |  | Navigate to Dashboard from Home page | User logged in as <User> | 1. Click on the 'Dashboard' button | redirects to dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to access Home Page without authentication |  | 1. Open the Home Page URL without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the Search Activity input |  | 1. Enter a string of 200+ characters in the Search Activity input field | Search Activity input accepts the long string without truncation or shows a specific error if there is a limit | low |
| TC-006 (input_edge) |  | Enter special characters in the Search Activity input |  | 1. Enter a string containing special characters (e.g., !@#$%^&*()_+) in the Search Activity input field | Search Activity input accepts the special characters or shows a specific error indicating invalid input | low |
| TC-007 (input_edge) |  | Enter leading and trailing whitespace in the Search Activity input |  | 1. Enter a string with leading and trailing spaces in the Search Activity input field | Leading and trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Dashboard

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Access the Dashboard from Home page | User logged in as <User Role> | 1. Click the 'Dashboard' button on the Home page | The Dashboard is displayed with the 'Search Activity' field at the top | high |
| TC-002 |  | Display Client Trends chart | User logged in as <User Role>, Dashboard is open | 1. Observe the 'Client Trends' chart | The 'Client Trends' chart visualizes client growth over time with legends for 'New Clients' and 'Closed Clients' | high |
| TC-003 |  | Display summary cards with data | User logged in as <User Role>, Dashboard is open | 1. Observe the summary cards below the chart | The summary cards display 'Amount Pending / Disbursed' and 'Amount Collected' | high |
| TC-004 |  | Display 'No Data' in summary cards when no information is available | User logged in as <User Role>, Dashboard is open | 1. Ensure no data is available for the selected office<br>2. Observe the summary cards | Both summary cards show 'No Data' if no information is available | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to access the Dashboard without authentication |  | 1. Navigate to the Dashboard URL without logging in | User is redirected to the login page | high |
| TC-006 |  | Check summary cards when no data is available |  | 1. Access the Dashboard<br>2. Observe the summary cards | Summary cards display 'No Data' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully accessed the Dashboard | 1. Click the 'Dashboard' button on the Home page<br>2. Wait for the Dashboard to load<br>3. Press the browser back button | User is redirected to the Dashboard without pre-filled fields; the page appears blank. | medium |
| TC-008 (input_edge) |  | Long text in Search Activity field | User is on the Dashboard | 1. Enter a string of 200+ characters in the 'Search Activity' field<br>2. Click the search button | Search input is either accepted or truncated with a visible indicator. | low |
| TC-009 (input_edge) |  | Leading/trailing whitespace in Search Activity field | User is on the Dashboard | 1. Enter '   search term   ' in the 'Search Activity' field<br>2. Click the search button | Leading/trailing whitespace is trimmed; the saved value shown in the search results has no extra spaces. | low |
| TC-010 (input_edge) |  | Special characters in Search Activity field | User is on the Dashboard | 1. Enter '@#$%^&*()' in the 'Search Activity' field<br>2. Click the search button | Input is accepted or a specific error is shown indicating invalid characters. | low |

---

## Global Search

Total: **13** (positive: 6, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open search input field | User logged in as <User> | 1. Click the Search Icon | The search input field is opened | high |
| TC-002 |  | Search for existing clients | User logged in as <User> | 1. Click the Search Icon<br>2. Enter <valid client name> in the search input field | Search results dropdown displays matching Clients with their entity name, identifier, and status | high |
| TC-003 |  | Search for existing groups | User logged in as <User> | 1. Click the Search Icon<br>2. Enter <valid group name> in the search input field | Search results dropdown displays matching Groups with their entity name, identifier, and status | high |
| TC-004 |  | Search for existing loans | User logged in as <User> | 1. Click the Search Icon<br>2. Enter <valid loan identifier> in the search input field | Search results dropdown displays matching Loans with their entity name, identifier, and status | high |
| TC-005 |  | Search for existing savings accounts | User logged in as <User> | 1. Click the Search Icon<br>2. Enter <valid savings account identifier> in the search input field | Search results dropdown displays matching Savings accounts with their entity name, identifier, and status | high |
| TC-006 |  | Display no results found message | User logged in as <User> | 1. Click the Search Icon<br>2. Enter <non-existing entity name> in the search input field | The message 'No results found' is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to access search input without logging in |  | 1. Click on the Search Icon | User is redirected to the login page; search input field does not open | high |
| TC-008 |  | Submit search input with no text | user must be logged in | 1. Click on the Search Icon<br>2. Leave the Search Input blank<br>3. Submit the search | Search does not execute; no results are displayed; 'No results found' message is shown | high |
| TC-009 |  | Submit search input with invalid format | user must be logged in | 1. Click on the Search Icon<br>2. Enter <invalid search term> in the Search Input<br>3. Submit the search | Search does not execute; no results are displayed; 'No results found' message is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) |  | Enter a very long search term | User is logged in | 1. Click on the search icon<br>2. Enter a string longer than 200 characters in the search input field | Search input field displays the long string correctly; no error shown | low |
| TC-011 (input_edge) |  | Enter special characters in the search input | User is logged in | 1. Click on the search icon<br>2. Enter a string with special characters (e.g., @#$%^&*) in the search input field | Search input accepts the special characters; results are displayed accordingly or an appropriate error is shown | low |
| TC-012 (input_edge) |  | Enter leading and trailing whitespace in the search input | User is logged in | 1. Click on the search icon<br>2. Enter a string with leading and trailing spaces in the search input field | Leading and trailing whitespace is trimmed; search results are displayed based on the trimmed input | low |
| TC-013 (input_edge) |  | Search with an empty input | User is logged in | 1. Click on the search icon<br>2. Leave the search input field empty and initiate the search | No results found message is displayed | low |

---

## Client Management

Total: **26** (positive: 8, negative: 10, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View client details from the Clients table | User logged in as <Role> | 1. Click on the Name link of a client in the Clients table | Client Detail page displays the client name, account number, status badge, activation date, and office | high |
| TC-002 | WF-002 | Search for a client by name | User logged in as <Role> | 1. Enter <valid client name> in the Search field<br>2. Press Enter | Clients table displays only rows matching <valid client name>; unrelated rows are no longer visible | high |
| TC-003 | WF-003 | Filter clients by status | User logged in as <Role> | 1. Select 'Active' from the Status_Filter dropdown<br>2. Click Apply | Clients table displays only rows with status 'Active'; unrelated rows are no longer visible | high |
| TC-004 | WF-004 | Open Bulk Import page from the Clients page | User logged in as <Role> | 1. Click on the 'Import Client' button | Bulk Import page opens | high |
| TC-005 | WF-005 | Download client Excel template from Bulk Import page | User logged in as <Role>, Bulk Import page is open | 1. Click on the 'Download Template' button | downloads client Excel template | medium |
| TC-006 | WF-006 | Create a new client using the Create Client wizard | User logged in as <Role> | 1. Click on the 'Create Client' button<br>2. Fill in the required fields in Step 1: Office, First Name, Last Name, External ID, Submitted On<br>3. Click Next<br>4. Click Next<br>5. Click Next<br>6. Click Next<br>7. Click Submit | Client is created in Pending status | high |
| TC-007 | WF-007 | Activate a client from Pending status | User logged in as <Role>, Client is in Pending status | 1. Click on the 'Activate' button<br>2. Enter <valid activation date> in the Activation_Date field<br>3. Click Confirm on the Activation dialog | Client status updates to Active | medium |
| TC-008 | WF-008 | Edit a client's details | User logged in as <Role>, Client is in Active status | 1. Click on the 'Edit' button<br>2. Modify <specific field> with <new value><br>3. Click Save | <specific field> updates to <new value> | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Office field blank in Create Client wizard |  | 1. Open Create Client wizard<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Office field displays an error: 'This field is required.' | high |
| TC-010 |  | Leave the First Name field blank in Create Client wizard |  | 1. Open Create Client wizard<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; First Name field displays an error: 'This field is required.' | high |
| TC-011 |  | Leave the Last Name field blank in Create Client wizard |  | 1. Open Create Client wizard<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Last Name field displays an error: 'This field is required.' | high |
| TC-012 |  | Leave the External ID field blank in Create Client wizard |  | 1. Open Create Client wizard<br>2. Leave the External ID field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; External ID field displays an error: 'This field is required.' | high |
| TC-013 |  | Submit Create Client wizard with duplicate External ID |  | 1. Open Create Client wizard<br>2. Fill all required fields with valid data<br>3. Enter a duplicate value in the External ID field<br>4. Click Submit | Form does not submit; External ID field displays an error: 'Must be unique.' | high |
| TC-014 |  | Attempt to Activate client with Activation Date before Submitted On date | Client is in Pending status | 1. Open Client Detail page for the client<br>2. Click Activate<br>3. Enter an Activation Date that is before the Submitted On date<br>4. Click Submit | Form does not submit; Activation Date field displays an error: 'Activation Date must not be before submission date.' | high |
| TC-015 |  | Attempt to Close client with active accounts | Client is in Active status, Client has active accounts | 1. Open Client Detail page for the client<br>2. Click Close<br>3. Fill Closure Reason field<br>4. Click Submit | Form does not submit; Closure Reason field displays an error: 'Cannot close with active accounts.' | high |
| TC-016 |  | Attempt to Transfer Client to the same office | Client is in Active status | 1. Open Client Detail page for the client<br>2. Click Transfer Client<br>3. Select the same office in the Destination Office field<br>4. Click Submit | Form does not submit; Destination Office field displays an error: 'Same office is blocked.' | high |
| TC-017 |  | Attempt to Withdraw client without providing a reason | Client is in Pending status | 1. Open Client Detail page for the client<br>2. Click Withdraw<br>3. Leave the Reason field blank<br>4. Click Submit | Form does not submit; Reason field displays an error: 'This field is required.' | high |
| TC-018 |  | Attempt to Reject client without providing a reason | Client is in Pending status | 1. Open Client Detail page for the client<br>2. Click Reject<br>3. Leave the Reason field blank<br>4. Click Submit | Form does not submit; Reason field displays an error: 'This field is required.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) |  | Submit client with External ID that is unique | User is on Create Client wizard, Step 1 | 1. Enter a unique value in the External ID field<br>2. Fill in all other required fields<br>3. Click Submit | Client is created in Pending status with the provided External ID | medium |
| TC-020 (boundary) |  | Attempt to submit client with duplicate External ID | User is on Create Client wizard, Step 1 | 1. Enter a value in the External ID field that already exists<br>2. Fill in all other required fields<br>3. Click Submit | Form submission is blocked; error message displayed indicating that the External ID must be unique | medium |
| TC-021 (state_edge) | WF-001 | Activate client with Activation Date equal to Submitted On date | Client is in Pending status, User is on Client Detail page | 1. Click Activate<br>2. Enter the same date as Submitted On in the Activation Date field<br>3. Click Submit | Client is activated successfully | medium |
| TC-022 (state_edge) | WF-002 | Attempt to activate client with Activation Date before Submitted On date | Client is in Pending status, User is on Client Detail page | 1. Click Activate<br>2. Enter a date before Submitted On in the Activation Date field<br>3. Click Submit | Form submission is blocked; error message displayed indicating that Activation Date must not be before submission date | medium |
| TC-023 (state_edge) | WF-003 | Transfer client to the same office | Client is in Active status, User is on Client Detail page | 1. Click Transfer Client<br>2. Select the same office in the Destination Office field<br>3. Click Submit | Form submission is blocked; error message displayed indicating that transferring to the same office is blocked | medium |
| TC-024 (input_edge) |  | Enter a very long name in the search field | User is on Clients page | 1. Enter a string longer than 200 characters in the Search field<br>2. Press Enter | Search is executed; either results are shown or an error message is displayed indicating input is too long | low |
| TC-025 (input_edge) |  | Enter special characters in the search field | User is on Clients page | 1. Enter special characters (e.g., @#$%^&*) in the Search field<br>2. Press Enter | Search is executed; either results are shown or an error message is displayed indicating invalid input | low |
| TC-026 (input_edge) |  | Enter value with leading/trailing whitespace in the search field | User is on Clients page | 1. Enter '   John Doe   ' in the Search field<br>2. Press Enter | Leading/trailing whitespace is trimmed; search results display 'John Doe' | low |

---

## Group Management

Total: **20** (positive: 8, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new group successfully | User logged in as <Admin>, User is on the Groups page | 1. Click 'Create New Group' button<br>2. Enter <valid group name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid date> in the Submitted On field<br>5. Click 'Submit' | A success notification is displayed; the group is listed in the Groups table | high |
| TC-002 | WF-002 | Import groups successfully | User logged in as <Admin>, User is on the Groups page | 1. Click 'Import Groups' button<br>2. Upload a <valid groups file> in the Groups Upload panel<br>3. Click 'Upload' | A success notification is displayed; the imported groups are shown in the Groups table | high |
| TC-003 | WF-003 | View group details | User logged in as <Admin>, User is on the Groups page | 1. Click on the 'Group Name' link for a specific group | The Group Detail page displays the group name, account number, status, office, and staff | medium |
| TC-004 | WF-004 | Activate a group successfully | User logged in as <Admin>, User is on the Group Detail page of a group in 'Pending' status | 1. Click 'Activate' button | Status badge updates to 'Active' (green) on the Group Detail page | medium |
| TC-005 | WF-005 | Edit group details successfully | User logged in as <Admin>, User is on the Group Detail page | 1. Click 'Edit' button<br>2. Update <field> with <new value><br>3. Click 'Submit' | A success notification is displayed; the updated details are visible on the Group Detail page | medium |
| TC-006 | WF-006 | Close a group successfully | User logged in as <Admin>, User is on the Group Detail page | 1. Click 'Close' button | Status badge updates to 'Closed' (red) on the Group Detail page | medium |
| TC-007 | WF-007 | Assign staff to a group successfully | User logged in as <Admin>, User is on the Group Detail page | 1. Click 'Assign Staff' button<br>2. Select <staff member> from the list<br>3. Click 'Submit' | A success notification is displayed; the assigned staff member is visible on the Group Detail page | medium |
| TC-008 | WF-008 | Transfer clients successfully | User logged in as <Admin>, User is on the Group Detail page | 1. Click 'Transfer Clients' button<br>2. Select <clients> to transfer<br>3. Click 'Submit' | A success notification is displayed; the transferred clients are no longer listed under the group | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Name field blank and submit the Create Group form |  | 1. Leave the Name field blank<br>2. Fill in the Office and Submitted On fields with valid data<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 |  | Leave the Office field blank and submit the Create Group form |  | 1. Leave the Office field blank<br>2. Fill in the Name and Submitted On fields with valid data<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the Submitted On field blank and submit the Create Group form |  | 1. Leave the Submitted On field blank<br>2. Fill in the Name and Office fields with valid data<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-012 |  | Submit the Create Group form with all required fields empty |  | 1. Leave the Name, Office, and Submitted On fields blank<br>2. Click Submit | Inline validation errors appear on the Name, Office, and Submitted On fields indicating they are required | high |
| TC-013 |  | Attempt to activate a group that is already Active |  | 1. Navigate to a group that is in Active status<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-014 |  | Attempt to close a group that is in Pending status |  | 1. Navigate to a group that is in Pending status<br>2. Click Close | Status remains Pending; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Test group creation with maximum length for Name field |  | 1. Enter a string of maximum allowed length in the Name field<br>2. Enter a valid Office value<br>3. Enter a valid date in Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the maximum length Name | medium |
| TC-016 (boundary) |  | Test group creation with one character less than maximum length for Name field |  | 1. Enter a string of one character less than maximum allowed length in the Name field<br>2. Enter a valid Office value<br>3. Enter a valid date in Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the Name | medium |
| TC-017 (boundary) |  | Test group creation with empty Name field |  | 1. Leave the Name field empty<br>2. Enter a valid Office value<br>3. Enter a valid date in Submitted On field<br>4. Click Submit | Form submission is blocked; inline error displayed for Name field indicating it is required | medium |
| TC-018 (input_edge) |  | Test group creation with special characters in Name field |  | 1. Enter a string with special characters in the Name field<br>2. Enter a valid Office value<br>3. Enter a valid date in Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the Name containing special characters | low |
| TC-019 (input_edge) |  | Test group creation with leading and trailing whitespace in Name field |  | 1. Enter a string with leading and trailing whitespace in the Name field<br>2. Enter a valid Office value<br>3. Enter a valid date in Submitted On field<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-020 (interaction_edge) | WF-001 | Test rapid consecutive state transitions for Active group | Group is in Active state | 1. Click Close action button<br>2. Immediately click Edit action button | Close action succeeds; Edit action is blocked with a visible error indicating state cannot change while closing | medium |

---

## Center Management

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new center successfully | User logged in as <Admin>, On the Centers page | 1. Click 'Create Center' button<br>2. Enter <valid center name> in the Name field<br>3. Enter <valid office name> in the Office field<br>4. Enter <valid date> in the Submitted On field<br>5. Click 'Submit' button | The center is created successfully | high |
| TC-002 | WF-002 | Import centers successfully | User logged in as <Admin>, On the Centers page | 1. Click 'Import Center' button<br>2. Upload a valid template file<br>3. Click 'Submit' button | The centers are imported successfully | high |
| TC-003 | WF-003 | View center details | User logged in as <Admin>, On the Centers page | 1. Click on the center name link in the Name column | The Center Detail page displays the center name, status, office, and staff | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-005 |  | Leave the Office field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-006 |  | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-007 |  | Submit the Create Center form with all required fields empty |  | 1. Leave the Name field blank<br>2. Leave the Office field blank<br>3. Leave the Submitted On field blank<br>4. Click Submit | Form does not submit; Center is not created; error shown on Name, Office, and Submitted On fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Submit Create Center form with maximum length Name | User is on the Create Center form | 1. Enter maximum length string in the Name field<br>2. Enter valid Office in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submits successfully; center is created with the maximum length Name | medium |
| TC-009 (boundary) |  | Submit Create Center form with empty Name field | User is on the Create Center form | 1. Leave Name field empty<br>2. Enter valid Office in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submission is blocked; error shown indicating Name is required | medium |
| TC-010 (input_edge) |  | Submit Create Center form with leading and trailing whitespace in Name field | User is on the Create Center form | 1. Enter '  Center Name  ' in the Name field<br>2. Enter valid Office in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-011 (input_edge) |  | Submit Create Center form with special characters in Name field | User is on the Create Center form | 1. Enter special characters in the Name field<br>2. Enter valid Office in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submission is blocked; specific error shown indicating invalid characters in Name field | low |
| TC-012 (data_edge) |  | Upload file exactly at size limit in Bulk Import Centers page | User is on the Bulk Import Centers page | 1. Upload a file exactly at the size limit in the template-download field<br>2. Click Submit | File upload succeeds with a visible success indicator | medium |
| TC-013 (data_edge) |  | Upload file one byte over size limit in Bulk Import Centers page | User is on the Bulk Import Centers page | 1. Upload a file one byte over the size limit in the template-download field<br>2. Click Submit | File upload is blocked; visible error naming the size constraint is shown | medium |

---

## Loan Products

Total: **23** (positive: 9, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Loan Products page | User logged in as <Role> | 1. Navigate to the Loan Products page | The Loan Products page is displayed with a filter bar and a data table listing all loan products | high |
| TC-002 | WF-002 | Create new loan product | User logged in as <Role> | 1. Click the '+ Create Loan Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to Step 2 | opens 6-step stepper wizard | high |
| TC-003 | WF-002 | Complete Step 1 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 1 | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Click Next to proceed to Step 2 | Step 1 is saved and user proceeds to Step 2 | high |
| TC-004 | WF-002 | Complete Step 2 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 2 | 1. Enter <valid decimal places> in the Decimal Places field<br>2. Enter <valid multiples of rounding> in the Multiples of Rounding field<br>3. Click Next to proceed to Step 3 | Step 2 is saved and user proceeds to Step 3 | high |
| TC-005 | WF-002 | Complete Step 3 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 3 | 1. Enter <valid grace period> in the Grace Period field<br>2. Enter <valid arrears tolerance> in the Arrears Tolerance field<br>3. Click Next to proceed to Step 4 | Step 3 is saved and user proceeds to Step 4 | high |
| TC-006 | WF-002 | Complete Step 4 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 4 | 1. Enter <valid number of repayments> in the Number of Repayments field<br>2. Select 'Months' from the Repaid Every dropdown<br>3. Click Next to proceed to Step 5 | Step 4 is saved and user proceeds to Step 5 | high |
| TC-007 | WF-002 | Complete Step 5 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 5 | 1. Click Next to proceed to Step 6 | Step 5 is saved and user proceeds to Step 6 | high |
| TC-008 | WF-002 | Complete Step 6 of the loan product wizard | User logged in as <Role>, User is on the loan product creation wizard Step 6 | 1. Select 'Cash-based' from the Accounting Method radio options<br>2. Click Submit to finish creating the loan product | The new loan product is created successfully and the user is redirected to the Loan Products page | high |
| TC-009 | WF-001 | View loan product details | User logged in as <Role>, At least one loan product exists | 1. Click on the name of an existing loan product in the data table | opens detail view | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Leave the Product Name field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Leave the Product Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Product_Name field indicating it is required | high |
| TC-011 |  | Leave the Short Name field blank and submit |  | 1. Click on '+ Create Loan Product' button<br>2. Leave the Short Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Short_Name field indicating it is required | high |
| TC-012 |  | Submit with all required fields empty |  | 1. Click on '+ Create Loan Product' button<br>2. Leave all required fields blank<br>3. Click Next | Form does not submit; errors shown on Product_Name and Short_Name fields | high |
| TC-013 |  | Enter a non-numeric value in the Decimal Places field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields<br>3. Enter <non-numeric value> in the Decimal Places field<br>4. Click Next | Inline validation error appears on the Decimal_Places field indicating it must be a number | medium |
| TC-014 |  | Enter a non-numeric value in the Multiples of Rounding field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields<br>3. Enter <non-numeric value> in the Multiples of Rounding field<br>4. Click Next | Inline validation error appears on the Multiples_of_Rounding field indicating it must be a number | medium |
| TC-015 |  | Enter a value below the minimum in the Grace Period field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields<br>3. Enter <amount below minimum> in the Grace_Period field<br>4. Click Next | Inline validation error appears on the Grace_Period field indicating minimum value required | medium |
| TC-016 |  | Enter a value below the minimum in the Arrears Tolerance field |  | 1. Click on '+ Create Loan Product' button<br>2. Fill all required fields<br>3. Enter <amount below minimum> in the Arrears_Tolerance field<br>4. Click Next | Inline validation error appears on the Arrears_Tolerance field indicating minimum value required | medium |
| TC-017 |  | Attempt to select a repayment frequency without filling required fields |  | 1. Click on '+ Create Loan Product' button<br>2. Leave all required fields blank<br>3. Attempt to select a value in the Repaid Every dropdown<br>4. Click Next | Inline validation error appears on the Repaid_Every field indicating it is required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) |  | Enter minimum Principal Amount |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter minimum value in the Principal Amount field<br>4. Fill all other required fields in Step 2<br>5. Click Next | Form submits successfully; Principal Amount is saved with the minimum value | medium |
| TC-019 (boundary) |  | Enter one unit below minimum Principal Amount |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter one unit below minimum value in the Principal Amount field<br>4. Fill all other required fields in Step 2<br>5. Click Next | Inline validation error shown for Principal Amount; error indicates 'Minimum value required' | medium |
| TC-020 (boundary) |  | Enter maximum Number of Repayments |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter maximum value in the Number of Repayments field<br>4. Fill all other required fields in Step 4<br>5. Click Next | Form submits successfully; Number of Repayments is saved with the maximum value | medium |
| TC-021 (boundary) |  | Enter one unit above maximum Number of Repayments |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter one unit above maximum value in the Number of Repayments field<br>4. Fill all other required fields in Step 4<br>5. Click Next | Inline validation error shown for Number of Repayments; error indicates 'Maximum value required' | medium |
| TC-022 (input_edge) |  | Enter very long text in Product Name |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter a very long string (200+ characters) in the Product Name field<br>4. Fill all other required fields in Step 1<br>5. Click Next | Form submits successfully; Product Name is saved with the long string | low |
| TC-023 (input_edge) |  | Enter special characters in Short Name |  | 1. Click '+ Create Loan Product' button<br>2. Fill all required fields in Step 1<br>3. Enter special characters in the Short Name field<br>4. Fill all other required fields in Step 1<br>5. Click Next | Form submits successfully; Short Name is saved with special characters | low |

---

## Savings Products

Total: **22** (positive: 4, negative: 10, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a Savings Product with required fields | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Charges step<br>8. Click Next to proceed to the Accounting step<br>9. Select 'None' for Accounting Method<br>10. Click Submit | A success notification is displayed; the new Savings Product is listed in the data table | high |
| TC-002 |  | Create a Fixed Deposit Product with required fields | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Pre-Closure step<br>8. Click Next to proceed to the Deposit Term step<br>9. Click Next to proceed to the Interest Rate Chart step<br>10. Click Submit | A success notification is displayed; the new Fixed Deposit Product is listed in the data table | high |
| TC-003 |  | Create a Recurring Deposit Product with required fields | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Charges step<br>8. Click Next to proceed to the Accounting step<br>9. Select 'None' for Accounting Method<br>10. Click Submit | A success notification is displayed; the new Recurring Deposit Product is listed in the data table | high |
| TC-004 |  | Create a Savings Product with optional fields filled | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Enter <valid description> in the Description field<br>5. Enter <valid external id> in the External Id field<br>6. Click Next to proceed to the Currency step<br>7. Click Next to proceed to the Terms step<br>8. Click Next to proceed to the Settings step<br>9. Click Next to proceed to the Charges step<br>10. Click Next to proceed to the Accounting step<br>11. Select 'None' for Accounting Method<br>12. Click Submit | A success notification is displayed; the new Savings Product is listed in the data table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Product Name field blank |  | 1. Open the '+ Create Savings Product' wizard<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name field with a valid value<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-006 |  | Leave the Short Name field blank |  | 1. Open the '+ Create Savings Product' wizard<br>2. Fill in the Product Name field with a valid value<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-007 |  | Submit with all required fields empty |  | 1. Open the '+ Create Savings Product' wizard<br>2. Leave the Product Name field blank<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required; Inline validation error appears on the Short Name field indicating it is required | high |
| TC-008 |  | Attempt to submit Minimum Required Balance without checking Enforce Minimum Required Balance |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Enforce Minimum Required Balance checkbox<br>3. Leave the Minimum Required Balance field blank<br>4. Click Next | Inline validation error appears on the Minimum Required Balance field indicating it is required | high |
| TC-009 |  | Attempt to submit Maximum Overdraft Amount without checking Is Overdraft Allowed |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Is Overdraft Allowed checkbox<br>3. Leave the Maximum Overdraft Amount field blank<br>4. Click Next | Inline validation error appears on the Maximum Overdraft Amount field indicating it is required | high |
| TC-010 |  | Attempt to submit Overdraft Interest Rate without checking Is Overdraft Allowed |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Is Overdraft Allowed checkbox<br>3. Leave the Overdraft Interest Rate field blank<br>4. Click Next | Inline validation error appears on the Overdraft Interest Rate field indicating it is required | high |
| TC-011 |  | Attempt to submit Tax Group without checking Enable Withhold Tax |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Enable Withhold Tax checkbox<br>3. Leave the Tax Group field blank<br>4. Click Next | Inline validation error appears on the Tax Group field indicating it is required | high |
| TC-012 |  | Attempt to submit Days to Inactive without checking Enable Dormancy Tracking |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Enable Dormancy Tracking checkbox<br>3. Leave the Days to Inactive field blank<br>4. Click Next | Inline validation error appears on the Days to Inactive field indicating it is required | high |
| TC-013 |  | Attempt to submit Days to Dormancy without checking Enable Dormancy Tracking |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Enable Dormancy Tracking checkbox<br>3. Leave the Days to Dormancy field blank<br>4. Click Next | Inline validation error appears on the Days to Dormancy field indicating it is required | high |
| TC-014 |  | Attempt to submit Days to Escheat without checking Enable Dormancy Tracking |  | 1. Open the '+ Create Savings Product' wizard<br>2. Check the Enable Dormancy Tracking checkbox<br>3. Leave the Days to Escheat field blank<br>4. Click Next | Inline validation error appears on the Days to Escheat field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Enter exactly 0 in the Minimum Opening Balance field |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 4 (Settings)<br>3. Enter '0' in the Minimum Opening Balance field | Form submits successfully; saved record shows Minimum Opening Balance as '0' | medium |
| TC-016 (boundary) |  | Enter exactly 1 in the Minimum Required Balance field after checking Enforce Minimum Required Balance | Enforce Minimum Required Balance checkbox is checked | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 4 (Settings)<br>3. Check Enforce Minimum Required Balance checkbox<br>4. Enter '1' in the Minimum Required Balance field | Form submits successfully; saved record shows Minimum Required Balance as '1' | medium |
| TC-017 (boundary) |  | Enter exactly 1 in the Maximum Deposit Amount field in Deposit Term step |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 6 (Deposit Term)<br>3. Enter '1' in the Maximum Deposit Amount field | Form submits successfully; saved record shows Maximum Deposit Amount as '1' | medium |
| TC-018 (boundary) |  | Add exactly 5 entries to the GL Account Mappings repeating group |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 6 (Accounting)<br>3. Add 5 entries to the GL Account Mappings repeating group | Form submits successfully; 5 entries are displayed in the GL Account Mappings section | medium |
| TC-019 (boundary) |  | Attempt to add 6 entries to the GL Account Mappings repeating group |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 6 (Accounting)<br>3. Add 6 entries to the GL Account Mappings repeating group | Adding the 6th entry is blocked; a visible error message indicates the maximum limit has been reached | medium |
| TC-020 (input_edge) |  | Enter a very long string in the Product Name field |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 1 (Details)<br>3. Enter a string of 250 characters in the Product Name field | Form submits successfully; the saved record shows the Product Name as the entered string or truncated with an indicator | low |
| TC-021 (input_edge) |  | Enter special characters in the Short Name field |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 1 (Details)<br>3. Enter special characters in the Short Name field | Form submits successfully; the saved record shows the Short Name with the entered special characters | low |
| TC-022 (input_edge) |  | Enter leading and trailing whitespace in the Description field |  | 1. Click '+ Create Savings Product' button<br>2. Navigate to Step 1 (Details)<br>3. Enter '   Sample Description   ' in the Description field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Share Products

Total: **16** (positive: 3, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new share product with valid details | User logged in as <Role> | 1. Click '+ Create Share Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Enter <valid description> in the Description field<br>5. Click 'Next' to proceed to the Currency step<br>6. Enter <valid currency> in the Currency field<br>7. Click 'Next' to proceed to the Terms step<br>8. Enter <valid total number of shares> in the Total Number of Shares field<br>9. Enter <valid nominal unit price> in the Nominal Unit Price field<br>10. Click 'Next' to proceed to the Settings step<br>11. Click 'Next' to proceed to the Market Price step<br>12. Click 'Add Row' to add a market price row<br>13. Enter <valid from date> in the From Date field<br>14. Enter <valid share value> in the Share Value field<br>15. Click 'Next' to proceed to the Charges step<br>16. Click 'Next' to proceed to the Accounting step<br>17. Select 'Cash-based' from the Accounting Method radio options<br>18. Click 'Next' to complete the wizard | A success message is displayed; the new share product is listed in the Share Products table | high |
| TC-002 |  | Edit an existing share product | User logged in as <Role>, At least one share product exists in the Share Products table | 1. Click on the Product Name link of the existing share product<br>2. Click 'Edit' action for the selected product<br>3. Modify <valid product name> in the Product Name field<br>4. Modify <valid short name> in the Short Name field<br>5. Modify <valid description> in the Description field<br>6. Click 'Save' to update the product | The Share Products table displays the updated product details with the new values | medium |
| TC-003 |  | Delete an existing share product | User logged in as <Role>, At least one share product exists in the Share Products table | 1. Click on the Product Name link of the existing share product<br>2. Click 'Delete' action for the selected product<br>3. Confirm the deletion | The Share Products table no longer displays the deleted product | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Product Name field blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name and Description fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-005 |  | Leave the Short Name field blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Fill in the Product Name and Description fields<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-006 |  | Leave the Description field blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Fill in the Product Name and Short Name fields<br>3. Leave the Description field blank<br>4. Click Next | Inline validation error appears on the Description field indicating it is required | high |
| TC-007 |  | Leave the Total Number of Shares field blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Fill in the Product Name, Short Name, and Description fields<br>3. Leave the Total Number of Shares field blank<br>4. Click Next | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-008 |  | Leave the Nominal Unit Price field blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Fill in the Product Name, Short Name, Description, and Total Number of Shares fields<br>3. Leave the Nominal Unit Price field blank<br>4. Click Next | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-009 |  | Attempt to submit the Market Price step without filling From Date and Share Value |  | 1. Click on '+ Create Share Product' button<br>2. Fill in all required fields in previous steps<br>3. Click Next to reach the Market Price step<br>4. Leave the From Date and Share Value fields blank<br>5. Click Add | Inline validation error appears on the From Date and Share Value fields indicating they are required | high |
| TC-010 |  | Attempt to access accounting settings without selecting Cash-based |  | 1. Click on '+ Create Share Product' button<br>2. Fill in all required fields in previous steps<br>3. Select 'None' for Accounting Method<br>4. Click Next to reach the Accounting step | GL account mappings fields are not visible; no error shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Add maximum allowed entries to Market Price | User is on the Create Share Product wizard, Step 5 (Market Price) | 1. Add maximum allowed entries to the Market Price table | Form submits successfully with maximum entries displayed in the Market Price table | medium |
| TC-012 (boundary) |  | Attempt to add one more entry to Market Price beyond maximum | User is on the Create Share Product wizard, Step 5 (Market Price) | 1. Add maximum allowed entries to the Market Price table<br>2. Attempt to add one more entry | Attempt to add entry is blocked; an error message is shown indicating maximum entries reached | medium |
| TC-013 (input_edge) |  | Enter long text in Product Name field | User is on the Create Share Product wizard, Step 1 (Details) | 1. Enter a string of 200+ characters in the Product Name field | Input is either accepted or truncated with a visible indicator | low |
| TC-014 (input_edge) |  | Enter special characters in Short Name field | User is on the Create Share Product wizard, Step 1 (Details) | 1. Enter special characters in the Short Name field | Input is accepted or a specific error message is shown | low |
| TC-015 (interaction_edge) |  | Rapidly navigate through wizard steps | User is on the Create Share Product wizard | 1. Complete Step 1<br>2. Immediately attempt to click on Step 3 | Navigation is blocked; user remains on Step 2 until completed | medium |
| TC-016 (state_edge) |  | Select Cash-based accounting method and check GL account mappings | User is on the Create Share Product wizard, Step 7 (Accounting) | 1. Select Cash-based from Accounting Method<br>2. Check visibility of GL account mappings | GL account mappings fields are displayed after selecting Cash-based | medium |

---

## Charges

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new charge definition successfully | User logged in as <Role> | 1. Click '+ Create Charge' to open the creation form<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Enter <Currency> in the Currency field<br>5. Enter <Amount> in the Amount field<br>6. Click 'Submit' | A success notification is displayed; the Charges Table shows the new charge definition | high |
| TC-002 |  | Edit an existing charge definition | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click the link in the Name column of an existing charge<br>2. Click 'Edit' on the charge detail page<br>3. Modify <Charge Name> in the Charge Name field<br>4. Click 'Submit' | The Charges Table shows the updated charge definition with the modified Charge Name | medium |
| TC-003 |  | Delete an existing charge definition | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click the link in the Name column of an existing charge<br>2. Click 'Delete'<br>3. Confirm the deletion | The Charges Table no longer displays the deleted charge definition | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Charge Name blank and submit |  | 1. Leave the Charge Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-005 |  | Leave Charge Applies To blank and submit |  | 1. Leave the Charge Applies To field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-006 |  | Leave Currency blank and submit |  | 1. Leave the Currency field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-007 |  | Leave Amount blank and submit |  | 1. Leave the Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-008 |  | Submit with all required fields empty |  | 1. Leave the Charge Name field blank<br>2. Leave the Charge Applies To field blank<br>3. Leave the Currency field blank<br>4. Leave the Amount field blank<br>5. Click Submit | Form does not submit; Charge Name, Charge Applies To, Currency, and Amount fields display errors indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Enter a valid Charge Name at the minimum length |  | 1. Enter a valid Charge Name in the Charge_Name field | Form submits successfully; entity is created with the Charge Name | medium |
| TC-010 (boundary) |  | Enter a Charge Name with leading/trailing whitespace |  | 1. Enter '   Valid Charge Name   ' in the Charge_Name field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-011 (boundary) |  | Select 'Loan' in Charge Applies To dropdown |  | 1. Select 'Loan' in the Charge_Applies_To dropdown<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; charge definition is created with 'Loan' selected | medium |
| TC-012 (input_edge) |  | Enter a very long Charge Name |  | 1. Enter a string longer than 200 characters in the Charge_Name field | Form is blocked with an error indicating the Charge Name exceeds the maximum length allowed | low |
| TC-013 (input_edge) |  | Enter special characters in Charge Name |  | 1. Enter '@#$%^&*()' in the Charge_Name field | Form is blocked with an error indicating invalid characters in the Charge Name | low |

---

## Floating Rates

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form for Floating Rate | User logged in as <Role> | 1. Click the '+ Create Floating Rate' button | The creation form opens | high |
| TC-002 | WF-001 | Submit valid Floating Rate creation form | User logged in as <Role>, Creation form is open | 1. Enter <valid Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Check the Is Active checkbox<br>4. Click Submit | A success notification is displayed; the Floating Rate Name appears in the Floating Rates Table | high |
| TC-003 | WF-001 | View Floating Rate details | User logged in as <Role>, At least one Floating Rate exists in the table | 1. Click on the Floating Rate Name link in the Floating Rates Table | The detail view shows the full rate history with an Edit option | medium |
| TC-004 | WF-001 | Edit an existing Floating Rate | User logged in as <Role>, At least one Floating Rate exists in the table, Detail view of the Floating Rate is open | 1. Click the Edit option<br>2. Modify <valid Floating Rate Name> in the Floating Rate Name field<br>3. Click Submit | A success notification is displayed; the updated Floating Rate Name appears in the Floating Rates Table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Floating Rate Name field blank and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Click on the '+ Create Floating Rate' button<br>2. Leave all fields empty<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-007 |  | Attempt to create a second base lending rate |  | 1. Click on the '+ Create Floating Rate' button<br>2. Enter <valid name> in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit<br>5. Click on the '+ Create Floating Rate' button again<br>6. Enter <another valid name> in the Floating Rate Name field<br>7. Check the Is Base Lending Rate checkbox<br>8. Click Submit | Error shown: 'Only one base rate can exist at a time' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Attempt to create a floating rate with an empty Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field empty<br>3. Click Submit | Error message displayed indicating 'Floating Rate Name is required' | medium |
| TC-009 (boundary) |  | Attempt to create a second base lending rate |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit<br>5. Click the '+ Create Floating Rate' button again<br>6. Enter another valid Floating Rate Name<br>7. Check the Is Base Lending Rate checkbox<br>8. Click Submit | Error message displayed indicating 'only one base rate can exist at a time' | medium |
| TC-010 (input_edge) |  | Enter a very long Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter a string of 200+ characters in the Floating Rate Name field<br>3. Click Submit | Form submits successfully; Floating Rate Name is displayed correctly in the detail view | low |
| TC-011 (input_edge) |  | Enter special characters in the Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter special characters (e.g., @#$%^&*) in the Floating Rate Name field<br>3. Click Submit | Form submits successfully; Floating Rate Name is displayed correctly in the detail view | low |

---

## Delinquency Management

Total: **16** (positive: 4, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new delinquency range with valid data | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <valid classification> in the Classification field<br>4. Enter <valid minimum age days> in the Minimum Age Days field<br>5. Enter <valid maximum age days> in the Maximum Age Days field<br>6. Click Submit | A success notification is displayed; the new delinquency range appears in the Delinquency Ranges table with the entered Classification, Minimum Age Days, and Maximum Age Days | high |
| TC-002 |  | Create a new delinquency bucket with valid data | User logged in as <Role> | 1. Navigate to the Delinquency Buckets page<br>2. Click on 'Create Delinquency Bucket'<br>3. Enter <valid bucket name> in the Bucket Name field<br>4. Click 'Add Range'<br>5. Enter <valid range name> in the Range Name field<br>6. Enter <valid minimum age days> in the Minimum Age Days field<br>7. Enter <valid maximum age days> in the Maximum Age Days field<br>8. Click 'Add Range' again to add another range<br>9. Enter <valid range name 2> in the Range Name field<br>10. Enter <valid minimum age days 2> in the Minimum Age Days field<br>11. Leave Maximum Age Days field blank<br>12. Click Submit | A success notification is displayed; the new delinquency bucket appears in the Delinquency Buckets table with the entered Bucket Name and associated ranges | high |
| TC-003 |  | Access delinquency range classification link | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on the Classification link for a specific range | The Classification detail page is displayed with relevant information | medium |
| TC-004 |  | Access delinquency bucket name link | User logged in as <Role> | 1. Navigate to the Delinquency Buckets page<br>2. Click on the Bucket Name link for a specific bucket | The Bucket detail page is displayed with relevant information | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Classification field blank and submit the Create Delinquency Range form |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-006 |  | Leave the Minimum Age Days field blank and submit the Create Delinquency Range form |  | 1. Leave the Minimum Age Days field blank<br>2. Fill Classification with a valid value<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-007 |  | Leave the Bucket Name field blank and submit the Create Delinquency Bucket form |  | 1. Leave the Bucket Name field blank<br>2. Fill in the Delinquency Ranges with valid values<br>3. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-008 |  | Submit the Create Delinquency Bucket form with all required fields empty |  | 1. Leave the Bucket Name field blank<br>2. Leave the Range Name field blank in Delinquency Ranges<br>3. Leave Minimum Age Days field blank in Delinquency Ranges<br>4. Click Submit | Form does not submit; Bucket Name and Range Name fields display errors indicating they are required | high |
| TC-009 |  | Enter a non-numeric value in the Minimum Age Days field |  | 1. Fill Classification with a valid value<br>2. Enter <non-numeric value> in the Minimum Age Days field<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it must be a number | medium |
| TC-010 |  | Enter a non-numeric value in the Maximum Age Days field of Delinquency Ranges |  | 1. Fill Bucket Name with a valid value<br>2. Fill in the Range Name with a valid value<br>3. Enter <non-numeric value> in the Maximum Age Days field<br>4. Click Submit | Inline validation error appears on the Maximum Age Days field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Minimum Age Days at lower boundary |  | 1. Enter the minimum allowed value in the Minimum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the minimum value in Minimum Age Days | medium |
| TC-012 (boundary) |  | Minimum Age Days below lower boundary |  | 1. Enter one unit below the minimum allowed value in the Minimum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Minimum Age Days displays an error indicating the value is below the minimum allowed | medium |
| TC-013 (boundary) |  | Maximum Age Days at upper boundary |  | 1. Enter the maximum allowed value in the Maximum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the maximum value in Maximum Age Days | medium |
| TC-014 (boundary) |  | Maximum Age Days above upper boundary |  | 1. Enter one unit above the maximum allowed value in the Maximum Age Days field<br>2. Fill all other required fields<br>3. Click Submit | Maximum Age Days displays an error indicating the value exceeds the maximum allowed | medium |
| TC-015 (boundary) |  | Add maximum allowed entries to Delinquency Ranges |  | 1. Add the maximum allowed entries to the Delinquency Ranges repeating group<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully with maximum allowed entries in Delinquency Ranges | medium |
| TC-016 (boundary) |  | Add one more entry to Delinquency Ranges |  | 1. Add maximum allowed entries + 1 to the Delinquency Ranges repeating group<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; a visible error indicates the maximum number of entries has been exceeded | medium |

---

## Loan Account

Total: **30** (positive: 3, negative: 20, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Complete loan application successfully | User logged in as <Client>, User is on the Client Detail page | 1. Click 'Start Loan Application'<br>2. Select <valid product> from the Product Name dropdown<br>3. Enter <Loan Officer> in the Loan Officer field<br>4. Enter <Loan Purpose> in the Loan Purpose field<br>5. Enter <Fund> in the Fund field<br>6. Enter <valid date> in the Submitted On date field<br>7. Enter <valid date> in the Expected Disbursement Date field<br>8. Enter <valid principal amount> in the Principal field<br>9. Enter <valid number of repayments> in the Number of Repayments field<br>10. Enter <valid frequency> in the Repaid Every field<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Click 'Next' to proceed to Step 2<br>13. Select <Repayment Strategy> in the Repayment Strategy field<br>14. Select <Amortization> in the Amortization field<br>15. Select <Interest Method> in the Interest Method field<br>16. Select <valid interest calculation period> from the Interest Calculation Period dropdown<br>17. Click 'Next' to proceed to Step 3<br>18. Click 'Add Charge' to add additional charges if necessary<br>19. Click 'Next' to proceed to Step 4<br>20. Click 'Add Row' to add collateral items<br>21. Enter <Collateral Type> in the Collateral Type field<br>22. Enter <valid value> in the Value field<br>23. Enter <Description> in the Description field<br>24. Click 'Submit' to complete the application | Loan is created in 'Submitted and Pending Approval' status | high |
| TC-002 |  | Add collateral item successfully | User logged in as <Client>, User is on the Loan Application wizard Step 4 | 1. Click 'Add Row' to add collateral items<br>2. Enter <Collateral Type> in the Collateral Type field<br>3. Enter <valid value> in the Value field<br>4. Enter <Description> in the Description field<br>5. Click 'Submit' to save the collateral item | New collateral item appears in the Collateral section with the entered details | medium |
| TC-003 |  | Submit loan application with all required fields filled | User logged in as <Client>, User is on the Loan Application wizard Step 1 | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On date field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number of repayments> in the Number of Repayments field<br>9. Enter <valid frequency> in the Repaid Every field<br>10. Enter <valid interest rate> in the Interest Rate field<br>11. Click 'Next' to proceed to Step 2<br>12. Select <Repayment Strategy> in the Repayment Strategy field<br>13. Select <Amortization> in the Amortization field<br>14. Select <Interest Method> in the Interest Method field<br>15. Select <valid interest calculation period> from the Interest Calculation Period dropdown<br>16. Click 'Next' to proceed to Step 3<br>17. Click 'Next' to proceed to Step 4<br>18. Click 'Submit' to complete the application | Loan is created in 'Submitted and Pending Approval' status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-005 |  | Leave the Loan Officer field blank and submit |  | 1. Leave the Loan Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-006 |  | Leave the Loan Purpose field blank and submit |  | 1. Leave the Loan Purpose field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Purpose field indicating it is required | high |
| TC-007 |  | Leave the Fund field blank and submit |  | 1. Leave the Fund field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fund field indicating it is required | high |
| TC-008 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-009 |  | Leave the Expected Disbursement Date blank and submit |  | 1. Leave the Expected Disbursement Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it is required | high |
| TC-010 |  | Leave the Principal field blank and submit |  | 1. Leave the Principal field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is required | high |
| TC-011 |  | Leave the Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-012 |  | Leave the Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-013 |  | Leave the Interest Rate field blank and submit |  | 1. Leave the Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-014 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; errors shown on all required fields | high |
| TC-015 |  | Enter an invalid date in the Submitted On field and submit |  | 1. Enter <invalid date format> in the Submitted On field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is not a valid date | medium |
| TC-016 |  | Enter a Principal amount below product minimum and submit |  | 1. Enter <amount below minimum> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is below the minimum required | medium |
| TC-017 |  | Enter a Principal amount above product maximum and submit |  | 1. Enter <amount above maximum> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is above the maximum allowed | medium |
| TC-018 |  | Attempt to approve a loan without filling Approved Amount and submit | Loan status is Pending Approval | 1. Click Approve<br>2. Leave the Approved Amount field blank<br>3. Click Submit | Inline validation error appears on the Approved Amount field indicating it is required | high |
| TC-019 |  | Attempt to disburse a loan without filling Transaction Amount and submit | Loan status is Approved | 1. Click Disburse<br>2. Leave the Transaction Amount field blank<br>3. Click Submit | Inline validation error appears on the Transaction Amount field indicating it is required | high |
| TC-020 |  | Attempt to make a repayment without filling Transaction Amount and submit | Loan status is Active | 1. Click Make Repayment<br>2. Leave the Transaction Amount field blank<br>3. Click Submit | Inline validation error appears on the Transaction Amount field indicating it is required | high |
| TC-021 |  | Attempt to reschedule a loan without filling Reason and submit | Loan status is Active | 1. Click Reschedule<br>2. Leave the Reason field blank<br>3. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-022 |  | Attempt to reschedule a loan without filling Adjusted Due Date and submit | Loan status is Active | 1. Click Reschedule<br>2. Leave the Adjusted Due Date field blank<br>3. Click Submit | Inline validation error appears on the Adjusted Due Date field indicating it is required | high |
| TC-023 |  | Attempt to approve a loan when it is already approved | Loan status is Approved | 1. Click Approve | Status remains Approved; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 (boundary) |  | Submit loan application with Principal at minimum bound | Select a product that defines minimum and maximum for Principal | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter exactly the minimum allowed value in the Principal field<br>4. Click Submit | Form submits successfully; loan is created with Principal set to the minimum value | medium |
| TC-025 (boundary) |  | Submit loan application with Principal just above maximum bound | Select a product that defines minimum and maximum for Principal | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter a value in the Principal field that is one unit above the maximum allowed<br>4. Click Submit | Form submission is blocked; error shown indicating Principal exceeds maximum limit | medium |
| TC-026 (boundary) |  | Submit loan application with Interest Rate at minimum bound | Select a product that defines minimum and maximum for Interest Rate | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter exactly the minimum allowed value in the Interest Rate field<br>4. Click Submit | Form submits successfully; loan is created with Interest Rate set to the minimum value | medium |
| TC-027 (boundary) |  | Submit loan application with Interest Rate just above maximum bound | Select a product that defines minimum and maximum for Interest Rate | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter a value in the Interest Rate field that is one unit above the maximum allowed<br>4. Click Submit | Form submission is blocked; error shown indicating Interest Rate exceeds maximum limit | medium |
| TC-028 (input_edge) |  | Enter a long string in Loan Officer field |  | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter a string longer than 200 characters in the Loan Officer field<br>4. Click Submit | Form submission is blocked; error shown indicating the Loan Officer field exceeds maximum length | low |
| TC-029 (input_edge) |  | Enter special characters in Loan Purpose field |  | 1. Navigate to the Loan Application Wizard<br>2. Fill in all required fields with valid data<br>3. Enter special characters in the Loan Purpose field<br>4. Click Submit | Form submission is blocked; error shown indicating invalid characters in the Loan Purpose field | low |
| TC-030 (interaction_edge) |  | Rapid re-submission after redirect | Successfully submitted a loan application | 1. After submission, press the browser back button<br>2. Verify the Loan Application Wizard is displayed | The Loan Application Wizard is shown blank; no duplicate submission occurs | medium |

---

## Savings Account

Total: **23** (positive: 5, negative: 10, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new savings account successfully | User logged in as <Client>, Client Detail page is open | 1. Select <Product Name> from the Product Name dropdown<br>2. Enter <Field Officer> in the Field Officer field<br>3. Enter <valid date> in the Submitted On field<br>4. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>5. Select <Interest Compounding Period> from the Interest Compounding Period dropdown<br>6. Select <Interest Posting Period> from the Interest Posting Period dropdown<br>7. Select <Interest Calculated Using> from the Interest Calculated Using dropdown<br>8. Select <Days in Year> from the Days in Year dropdown<br>9. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>10. Enter <Lock-in Period> in the Lock-in Period field<br>11. Check the Allow Overdraft checkbox<br>12. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-002 |  | View Transactions tab on Savings Account Detail page | User logged in as <Client>, Savings Account is created and visible | 1. Click on the Transactions tab | Transactions tab displays all deposits, withdrawals, and interest postings with Date, Type, Amount, and Running Balance | medium |
| TC-003 |  | Approve a pending savings account application | User logged in as <Admin>, Savings Account is in Pending status | 1. Click Approve on the Savings Account Actions bar | Savings Account status updates to Approved | high |
| TC-004 |  | Withdraw from an active savings account | User logged in as <Client>, Savings Account is in Active status | 1. Click Withdraw on the Savings Account Actions bar<br>2. Enter <valid date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Click Submit | Withdrawal is processed and account balance is updated accordingly | high |
| TC-005 |  | Deposit into an active savings account | User logged in as <Client>, Savings Account is in Active status | 1. Click Deposit on the Savings Account Actions bar<br>2. Enter <valid date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Click Submit | Deposit is processed and account balance is updated accordingly | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-007 |  | Leave the Field Officer field blank and submit |  | 1. Leave the Field Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Field Officer field indicating it is required | high |
| TC-008 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-009 |  | Leave the Lock-in Period field blank and submit |  | 1. Leave the Lock-in Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Lock-in Period field indicating it is required | high |
| TC-010 |  | Leave the Allow Overdraft checkbox unchecked and submit |  | 1. Leave the Allow Overdraft checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Allow Overdraft field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Form does not submit; errors shown on Product Name, Field Officer, Submitted On, Lock-in Period, and Allow Overdraft fields | high |
| TC-012 |  | Attempt to Withdraw when overdraft is not enabled and withdrawal exceeds available balance | Account is in Active state, Available balance is less than withdrawal amount | 1. Click Withdraw<br>2. Fill Transaction Date and Transaction Amount fields with an amount exceeding available balance<br>3. Click Submit | Form does not submit; error shown indicating withdrawal cannot exceed available balance unless overdraft is enabled | medium |
| TC-013 |  | Attempt to Withdraw when minimum balance is enforced and withdrawal would breach it | Account is in Active state, Withdrawal would breach minimum balance | 1. Click Withdraw<br>2. Fill Transaction Date and Transaction Amount fields with an amount that breaches minimum balance<br>3. Click Submit | Form does not submit; error shown indicating minimum balance must be maintained | medium |
| TC-014 | WF-NNN | Attempt to Approve an account that is not in Pending status | Account is in Approved state | 1. Click Approve | Action is blocked; no transition occurs | medium |
| TC-015 |  | Attempt to Activate an account that is not in Approved status | Account is in Pending state | 1. Click Activate | Action is blocked; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) |  | Enter minimum opening balance | User is on the Savings Account Creation Form | 1. Enter <minimum allowed value> in the Minimum Opening Balance field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with the minimum opening balance | medium |
| TC-017 (boundary) |  | Enter one unit below minimum opening balance | User is on the Savings Account Creation Form | 1. Enter <one unit below minimum> in the Minimum Opening Balance field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message displayed indicating the minimum opening balance requirement | medium |
| TC-018 (boundary) |  | Enter lock-in period of zero | User is on the Savings Account Creation Form | 1. Enter 0 in the Lock-in Period field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with a lock-in period of zero | medium |
| TC-019 (boundary) |  | Enter negative lock-in period | User is on the Savings Account Creation Form | 1. Enter -1 in the Lock-in Period field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message displayed indicating the lock-in period cannot be negative | medium |
| TC-020 (data_edge) |  | Enter today's date in Submitted On field | User is on the Savings Account Creation Form | 1. Enter today's date in the Submitted On field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with today's date in Submitted On | medium |
| TC-021 (data_edge) |  | Enter a far future date in Submitted On field | User is on the Savings Account Creation Form | 1. Enter a far future date in the Submitted On field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with a far future date in Submitted On | medium |
| TC-022 (input_edge) |  | Enter a very long string in Field Officer field | User is on the Savings Account Creation Form | 1. Enter a very long string (200+ characters) in the Field Officer field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message displayed indicating the input exceeds maximum length | low |
| TC-023 (input_edge) |  | Enter special characters in Field Officer field | User is on the Savings Account Creation Form | 1. Enter special characters in the Field Officer field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message displayed indicating invalid characters | low |

---

## Share Account

Total: **21** (positive: 5, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Share Account Application with valid data | User logged in as <Client>, Client has active savings accounts | 1. Select <valid share product> from the Share Product dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid number within bounds> in the Requested Shares field<br>4. Enter <valid date> in the Application Date field<br>5. Select <active savings account> from the Savings Account for Charges dropdown<br>6. Click Submit | Account is created in 'Submitted and Pending Approval' status | high |
| TC-002 |  | Verify Share Account Detail Page displays correct information | User logged in as <Client>, Account is in 'Submitted and Pending Approval' status | 1. Navigate to the Share Account Detail Page | Share account number, product name, client name, status badge, total approved shares, total pending shares, and unit price are displayed | medium |
| TC-003 | WF-001 | Approve Share Account Application | User logged in as <Approver>, Account is in 'Pending' status | 1. Click Approve on the Share Account Actions<br>2. Enter <valid number of approved shares> in the Approved Shares field<br>3. Enter <valid date> in the Approved Date field<br>4. Click Confirm on the Approval dialog | Account status updates to 'Approved' | high |
| TC-004 | WF-002 | Reject Share Account Application | User logged in as <Approver>, Account is in 'Pending' status | 1. Click Reject on the Share Account Actions<br>2. Click Confirm on the Reject dialog | Account status updates to 'Rejected' | high |
| TC-005 | WF-003 | Redeem Shares from Active Share Account | User logged in as <Client>, Account is in 'Active' status, Shares are available for redemption | 1. Click Redeem Shares on the Share Account Actions | Redemption amount calculated as shares multiplied by current unit price and credited to the linked savings account | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-007 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-008 |  | Leave the Requested Shares field blank and submit |  | 1. Leave the Requested Shares field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-009 |  | Leave the Application Date blank and submit |  | 1. Leave the Application Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-010 |  | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave the Share Product field blank<br>2. Leave the Submitted On field blank<br>3. Leave the Requested Shares field blank<br>4. Leave the Application Date field blank<br>5. Leave the Savings Account for Charges field blank<br>6. Click Submit | Form does not submit; error shown on Share Product, Submitted On, Requested Shares, Application Date, and Savings Account for Charges fields | high |
| TC-012 |  | Submit with Requested Shares below product minimum |  | 1. Fill the Share Product field with a valid product<br>2. Fill the Submitted On field with a valid date<br>3. Enter <amount below minimum> in the Requested Shares field<br>4. Fill the Application Date field with a valid date<br>5. Fill the Savings Account for Charges field with a valid account<br>6. Click Submit | Form does not submit; error shown on Requested Shares field indicating it must be bounded by product min/max per client | medium |
| TC-013 |  | Attempt to approve shares when in Active state |  | 1. Navigate to the Share Account in Active state<br>2. Click on Approve | Status remains Active; no transition occurs | medium |
| TC-014 |  | Attempt to activate when in Approved state |  | 1. Navigate to the Share Account in Approved state<br>2. Click on Activate | Status remains Approved; no transition occurs | medium |
| TC-015 |  | Attempt to redeem shares when in Pending state |  | 1. Navigate to the Share Account in Pending state<br>2. Click on Redeem Shares | Status remains Pending; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) |  | Requesting shares at the minimum allowed value | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submits successfully; account is created with the minimum requested shares | medium |
| TC-017 (boundary) |  | Requesting shares just above the maximum allowed value | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter a value above the maximum allowed in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Submission is blocked; an error message is displayed indicating the requested shares exceed the maximum allowed | medium |
| TC-018 (data_edge) |  | Submitting with today's date in Submitted On field | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the number of requested shares within the allowed range<br>3. Enter today's date in the Submitted On field<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submits successfully; account is created with today's date as the submitted date | medium |
| TC-019 (data_edge) |  | Submitting with a past date in Application Date field | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the number of requested shares within the allowed range<br>3. Fill in the Submitted On date<br>4. Enter a date in the Application Date field that is in the past<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Submission is blocked; an error message is displayed indicating the application date cannot be in the past | medium |
| TC-020 (input_edge) |  | Entering a very long External ID | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the number of requested shares within the allowed range<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter a very long string (200+ characters) in the External ID field<br>7. Click Submit | Form submits successfully; External ID is saved correctly or truncated with a visible indicator | low |
| TC-021 (input_edge) |  | Using special characters in External ID | User is on the Share Account Application Form | 1. Select a Share Product from the dropdown<br>2. Enter the number of requested shares within the allowed range<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter special characters in the External ID field<br>7. Click Submit | Form submits successfully; External ID is saved correctly or an error message is displayed | low |

---

## Fixed & Recurring Deposit Accounts

Total: **20** (positive: 5, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a Fixed Deposit Account successfully | User logged in as <Client> | 1. Navigate to the FD Account Creation Form<br>2. Enter <valid deposit amount> in the Deposit Amount field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select 'Transfer to Savings' from the Maturity Instructions dropdown<br>5. Click Submit | A success notification is displayed; the FD Account details are visible in the FD Account Detail page | high |
| TC-002 |  | Create a Recurring Deposit Account successfully | User logged in as <Client> | 1. Navigate to the RD Account Creation Form<br>2. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount field<br>3. Select 'Monthly' from the Deposit Frequency dropdown<br>4. Enter <valid date> in the Expected First Deposit On field<br>5. Click Submit | A success notification is displayed; the RD Account details are visible in the RD Account Detail page | high |
| TC-003 |  | Approve a Fixed Deposit Account | User logged in as <Admin>, FD Account is created | 1. Navigate to the FD Account Detail page<br>2. Click Approve | The FD Account status updates to 'Approved' | medium |
| TC-004 |  | Activate a Recurring Deposit Account | User logged in as <Admin>, RD Account is created | 1. Navigate to the RD Account Detail page<br>2. Click Activate | The RD Account status updates to 'Active' | medium |
| TC-005 |  | View Summary tab in FD and RD Account Detail | User logged in as <Client>, FD and RD Accounts are created | 1. Navigate to the FD Account Detail page<br>2. Click on the Summary tab<br>3. Navigate to the RD Account Detail page<br>4. Click on the Summary tab | The Summary tab displays the correct account details for both FD and RD Accounts | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Deposit Amount blank and submit the FD Account creation form |  | 1. Leave the Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-007 |  | Leave the Deposit Period blank and submit the FD Account creation form |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-008 |  | Leave the Mandatory Deposit Amount blank and submit the RD Account creation form |  | 1. Leave the Mandatory Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mandatory Deposit Amount field indicating it is required | high |
| TC-009 |  | Leave the Expected First Deposit On date blank and submit the RD Account creation form |  | 1. Leave the Expected First Deposit On field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected First Deposit On field indicating it is required | high |
| TC-010 |  | Submit FD Account creation form with a non-numeric value in Deposit Amount |  | 1. Enter <non-numeric value> in the Deposit Amount field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Amount field indicating it must be a number | medium |
| TC-011 |  | Submit RD Account creation form with a non-numeric value in Mandatory Deposit Amount |  | 1. Enter <non-numeric value> in the Mandatory Deposit Amount field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mandatory Deposit Amount field indicating it must be a number | medium |
| TC-012 |  | Submit RD Account creation form with an invalid date in Expected First Deposit On |  | 1. Enter <invalid date> in the Expected First Deposit On field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected First Deposit On field indicating it must be a valid date | medium |
| TC-013 |  | Attempt to Approve an FD account when it is not in an appropriate state |  | 1. Navigate to the FD Account Detail page<br>2. Click Approve | Action is blocked; no change occurs to the FD account status | medium |
| TC-014 |  | Attempt to Activate an RD account when it is not in an appropriate state |  | 1. Navigate to the RD Account Detail page<br>2. Click Activate | Action is blocked; no change occurs to the RD account status | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) |  | Deposit Amount at minimum value |  | 1. Enter <minimum allowed value> in the <Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <minimum allowed value> | medium |
| TC-016 (boundary) |  | Deposit Amount below minimum value |  | 1. Enter <one unit below minimum> in the <Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | <Deposit_Amount> displays an error indicating the value is below the minimum allowed | medium |
| TC-017 (boundary) |  | Deposit Period at minimum value |  | 1. Enter <minimum allowed value> in the <Deposit_Period> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <minimum allowed value> | medium |
| TC-018 (boundary) |  | Deposit Period below minimum value |  | 1. Enter <one unit below minimum> in the <Deposit_Period> field<br>2. Fill all other required fields<br>3. Click Submit | <Deposit_Period> displays an error indicating the value is below the minimum allowed | medium |
| TC-019 (input_edge) |  | Enter long text in dropdown fields |  | 1. Select a value from <Fixed_Deposit_Product> dropdown<br>2. Enter a very long string (200+ characters) in the <Mandatory_Deposit_Amount> field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully or displays an error for the <Mandatory_Deposit_Amount> field | low |
| TC-020 (input_edge) |  | Enter special characters in Mandatory Deposit Amount |  | 1. Enter special characters in the <Mandatory_Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | <Mandatory_Deposit_Amount> displays an error indicating invalid input | low |

---

## Accounting — Chart of Accounts

Total: **16** (positive: 3, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new General Ledger account successfully | User logged in as <Accountant>, User is on the Chart of Accounts page | 1. Click '+ Create GL Account' button<br>2. Select <Account Type> from the Account Type dropdown<br>3. Select <Parent Account> from the Parent Account dropdown<br>4. Enter <unique GL Code> in the GL Code field<br>5. Enter <Account Name> in the Account Name field<br>6. Select <Account Usage> from the Account Usage dropdown<br>7. Check the Manual Entries Allowed checkbox<br>8. Enter <Description> in the Description field<br>9. Select <Tag> from the Tag dropdown<br>10. Click Submit | A success notification is displayed; the new account appears in the Chart of Accounts with the entered GL Code and Account Name | high |
| TC-002 |  | Edit an existing General Ledger account | User logged in as <Accountant>, User is on the Chart of Accounts page, An account with GL Code <existing GL Code> exists | 1. Click on the account name with GL Code <existing GL Code><br>2. Click Edit<br>3. Update the Account Name to <new Account Name><br>4. Click Submit | The account name updates to '<new Account Name>' in the Chart of Accounts | medium |
| TC-003 |  | Delete an existing General Ledger account | User logged in as <Accountant>, User is on the Chart of Accounts page, An account with GL Code <existing GL Code> exists | 1. Click on the account name with GL Code <existing GL Code><br>2. Click Delete<br>3. Confirm the deletion | The account with GL Code <existing GL Code> is no longer present in the Chart of Accounts | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-005 |  | Leave the Parent Account field blank and submit |  | 1. Leave the Parent Account field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Parent Account field indicating it is required | high |
| TC-006 |  | Leave the GL Code field blank and submit |  | 1. Leave the GL Code field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-007 |  | Leave the Account Name field blank and submit |  | 1. Leave the Account Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-008 |  | Leave the Account Usage field blank and submit |  | 1. Leave the Account Usage field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Account Usage field indicating it is required | high |
| TC-009 |  | Leave the Manual Entries Allowed field unchecked and submit |  | 1. Leave the Manual Entries Allowed field unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Manual Entries Allowed field indicating it is required | high |
| TC-010 |  | Leave the Description field blank and submit |  | 1. Leave the Description field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Description field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; error shown on Account Type, Parent Account, GL Code, Account Name, Account Usage, Manual Entries Allowed, and Description fields | high |
| TC-012 |  | Submit with a duplicate GL Code |  | 1. Enter <duplicate GL Code> in the GL Code field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Validation error shown: 'GL Code must be unique' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Attempt to create a GL account with a duplicate GL Code | A GL account with the same GL Code already exists | 1. Navigate to the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter the same GL Code as the existing account<br>4. Click Submit | An error message is displayed indicating that the GL Code must be unique | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Account Name field |  | 1. Navigate to the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter a string of 200+ characters in the Account Name field<br>4. Click Submit | The form submits successfully; the Account Name is saved as entered or truncated with a visible indicator | low |
| TC-015 (input_edge) |  | Enter special characters in the Description field |  | 1. Navigate to the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter special characters (e.g., !@#$%^&*) in the Description field<br>4. Click Submit | The form submits successfully; the Description is saved as entered or an error is shown | low |
| TC-016 (input_edge) |  | Enter a value with leading/trailing whitespace in the Account Name field |  | 1. Navigate to the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter '   Account Name   ' in the Account Name field<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounting — Journal Entries & Closures

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Add a new journal entry with valid details | User logged in as <Accountant>, No existing journal entries | 1. Click '+ Add Journal Entry' button<br>2. Select <Office> from the Office dropdown<br>3. Select <Currency> from the Currency dropdown<br>4. Enter <valid reference number> in the Reference Number field<br>5. Enter <valid date> in the Transaction Date field<br>6. Click 'Add Row' in Entry Lines<br>7. Select <GL Account> from the GL Account dropdown<br>8. Enter <valid amount> in the Amount field<br>9. Click 'Submit' button | A success notification is displayed; the new journal entry appears in the Journal Entries table with the entered details. | high |
| TC-002 |  | Create a closure with valid details | User logged in as <Accountant>, No existing closures | 1. Click '+ Create Closure' button<br>2. Select <Office> from the Office dropdown<br>3. Enter <valid closing date> in the Closing Date field<br>4. Enter <valid comments> in the Comments field<br>5. Click 'Submit' button | A success notification is displayed; the new closure appears in the Closing Entries table with the entered details. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Office field blank and submit the Journal Entry creation form |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-004 |  | Leave the Transaction Date field blank and submit the Journal Entry creation form |  | 1. Leave the Transaction Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-005 |  | Leave the GL Account field blank in an Entry Line and submit the Journal Entry creation form |  | 1. Add an Entry Line<br>2. Leave the GL Account field blank<br>3. Fill all other required fields in the Entry Line<br>4. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-006 |  | Leave the Amount field blank in an Entry Line and submit the Journal Entry creation form |  | 1. Add an Entry Line<br>2. Fill the GL Account field<br>3. Leave the Amount field blank<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-007 |  | Submit the Journal Entry creation form with total debits not equal to total credits |  | 1. Fill all required fields in the Journal Entry creation form<br>2. Add Entry Lines with total debits not equal to total credits<br>3. Click Submit | Validation error shown: 'Total debits must equal total credits' | high |
| TC-008 |  | Attempt to create a closure with a closing date in the past and submit |  | 1. Fill the Office field<br>2. Set the Closing Date to a date in the past<br>3. Click Submit | Form does not submit; error shown on Closing Date indicating it must be a future date | high |
| TC-009 |  | Attempt to create a journal entry for a date on or before the closing date |  | 1. Create a closure with a future closing date<br>2. Attempt to create a journal entry with a Transaction Date on or before the closing date<br>3. Click Submit | Form does not submit; error shown indicating journal entries cannot be posted for dates on or before the closing date | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Total debits equal total credits at the boundary | Journal entry form is open, At least one entry line is added | 1. Enter an amount in the first entry line's Amount field<br>2. Enter the same amount in the second entry line's Amount field<br>3. Click Submit | Form submits successfully; journal entry is created with total debits equal to total credits | medium |
| TC-011 (boundary) |  | Total debits do not equal total credits just past the boundary | Journal entry form is open, At least one entry line is added | 1. Enter an amount in the first entry line's Amount field<br>2. Enter a different amount in the second entry line's Amount field<br>3. Click Submit | Form submission is blocked; error message displays indicating total debits must equal total credits | medium |
| TC-012 (state_edge) |  | Prevent journal entries for dates on or before the closing date | Closure creation form is open, A closure has been created with a closing date | 1. Open the journal entry creation form<br>2. Enter a closing date that is on or before the created closure's closing date in the Transaction Date field<br>3. Click Submit | Form submission is blocked; error message displays indicating journal entries cannot be posted for dates on or before the closing date | medium |
| TC-013 (input_edge) |  | Enter a very long comment | Journal entry form is open | 1. Enter a comment with more than 200 characters in the Comments field<br>2. Click Submit | Form submission is blocked; error message displays indicating comment exceeds maximum length | low |

---

## Accounting Rules & Financial Activity Mappings

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new accounting rule | User logged in as <Role> | 1. Click '+ Create Rule' button<br>2. Enter <valid rule name> in the Rule Name field<br>3. Select <valid office> from the Office dropdown<br>4. Select <valid debit account> from the Debit Account dropdown<br>5. Check the Allow Multiple Debit Entries checkbox<br>6. Select <valid credit account> from the Credit Account dropdown<br>7. Check the Allow Multiple Credit Entries checkbox<br>8. Click 'Create Rule' button | A new accounting rule is created | high |
| TC-002 |  | Create a new financial activity mapping | User logged in as <Role> | 1. Click '+ Create Mapping' button<br>2. Select <valid financial activity> from the Financial Activity dropdown<br>3. Select <valid GL account> from the GL Account dropdown<br>4. Click 'Create Mapping' button | A new financial activity mapping is created | high |
| TC-003 |  | Edit an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule<br>2. Click 'Edit' option<br>3. Update the Rule Name field with <new valid rule name><br>4. Click 'Save' button | The accounting rule is updated with the new rule name | medium |
| TC-004 |  | Delete an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule<br>2. Click 'Delete' option<br>3. Confirm deletion | The accounting rule is removed from the table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Rule Name field blank and submit |  | 1. Leave the Rule_Name field blank<br>2. Fill all other fields with valid data<br>3. Click Create Rule | Inline validation error appears on the Rule_Name field indicating it is required | high |
| TC-006 |  | Leave the Financial Activity field blank and submit |  | 1. Leave the Financial_Activity field blank<br>2. Fill the GL_Account field with valid data<br>3. Click Create Mapping | Inline validation error appears on the Financial_Activity field indicating it is required | high |
| TC-007 |  | Leave the GL Account field blank and submit |  | 1. Fill the Financial_Activity field with valid data<br>2. Leave the GL_Account field blank<br>3. Click Create Mapping | Inline validation error appears on the GL_Account field indicating it is required | high |
| TC-008 |  | Attempt to create a mapping with an already mapped Financial Activity |  | 1. Select an already mapped Financial Activity in the Financial_Activity dropdown<br>2. Select a valid GL Account<br>3. Click Create Mapping | Error shown indicating that the Financial Activity can only be mapped once | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Create Rule with maximum length Rule Name |  | 1. Open the Create Rule form<br>2. Enter a Rule Name with maximum allowed length in the Rule_Name field<br>3. Click Create Rule | Form submits successfully; entity is created with the maximum length Rule Name | medium |
| TC-010 (boundary) |  | Create Mapping with unmapped Financial Activity |  | 1. Open the Create Mapping form<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click Create Mapping | Form submits successfully; entity is created with the selected Financial Activity and GL Account | medium |
| TC-011 (input_edge) |  | Create Rule with leading/trailing whitespace in Rule Name |  | 1. Open the Create Rule form<br>2. Enter '   Example Rule Name   ' in the Rule_Name field<br>3. Click Create Rule | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-012 (input_edge) |  | Create Mapping with special characters in GL Account |  | 1. Open the Create Mapping form<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account containing special characters from the dropdown<br>4. Click Create Mapping | Form submits successfully; entity is created with the selected Financial Activity and GL Account containing special characters | low |

---

## Provisioning

Total: **18** (positive: 4, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new provisioning criteria with valid inputs | User logged in as <Role> | 1. Click '+ Create' to open the Criteria creation form<br>2. Enter <valid criteria name> in the Criteria Name field<br>3. Click 'Add Row' in the Definitions table<br>4. Enter <valid loan product> in the Loan Product field<br>5. Select 'STANDARD' from the Category dropdown<br>6. Enter <valid minimum age> in the Minimum Age field<br>7. Enter <valid maximum age> in the Maximum Age field<br>8. Enter <valid provisioning percentage> in the Provisioning Percentage field<br>9. Select <valid liability account> from the Liability Account dropdown<br>10. Select <valid expense account> from the Expense Account dropdown<br>11. Click 'Submit' to create the provisioning criteria | New row appears in the Provisioning Criteria Table with the entered Criteria Name and Created Date | high |
| TC-002 |  | Generate provisioning entries based on current loan portfolio status | User logged in as <Role>, At least one provisioning criteria exists | 1. Click '+ Create Provisioning Entry'<br>2. Observe the system processing the current loan portfolio status | Generates new provisioning entries based on current loan portfolio status | high |
| TC-003 |  | Review a provisioning entry | User logged in as <Role>, At least one provisioning entry exists | 1. Click 'Review' on an entry in the Provisioning Entries Table | Detailed breakdown by loan product and category is displayed | medium |
| TC-004 |  | Recreate a provisioning entry | User logged in as <Role>, At least one provisioning entry exists | 1. Click 'Recreate' on an entry in the Provisioning Entries Table | The provisioning entry is recreated based on the original criteria | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Criteria Name blank and submit |  | 1. Leave the Criteria_Name field blank<br>2. Fill in all other fields in the Create Criteria Form<br>3. Click Submit | Inline validation error appears on the Criteria_Name field indicating it is required | high |
| TC-006 |  | Leave Minimum Age blank and submit |  | 1. Leave the Minimum_Age field blank in the Definitions table<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Minimum_Age field indicating it is required | high |
| TC-007 |  | Leave Maximum Age blank and submit |  | 1. Leave the Maximum_Age field blank in the Definitions table<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Maximum_Age field indicating it is required | high |
| TC-008 |  | Leave Provisioning Percentage blank and submit |  | 1. Leave the Provisioning_Percentage field blank in the Definitions table<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Provisioning_Percentage field indicating it is required | high |
| TC-009 |  | Leave Liability Account blank and submit |  | 1. Leave the Liability_Account field blank in the Definitions table<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Liability_Account field indicating it is required | high |
| TC-010 |  | Leave Expense Account blank and submit |  | 1. Leave the Expense_Account field blank in the Definitions table<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Expense_Account field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields blank in the Create Criteria Form<br>2. Click Submit | Form does not submit; multiple inline validation errors are shown indicating required fields | high |
| TC-012 |  | Attempt to create provisioning entry without criteria |  | 1. Click on the + Create Provisioning Entry button<br>2. Observe the state of the form | No provisioning criteria are available; the button is disabled or an error message is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Add a Definitions entry with Minimum Age at 0 | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a row to the Definitions table<br>3. Enter a Loan Product in the Loan_Product field<br>4. Select a Category from the dropdown<br>5. Enter 0 in the Minimum_Age field<br>6. Enter a positive number in the Maximum_Age field<br>7. Enter a valid Provisioning_Percentage in the field<br>8. Select valid Liability Account and Expense Account from the dropdowns | Form submits successfully; entry is created with Minimum Age set to 0 | medium |
| TC-014 (boundary) |  | Add a Definitions entry with Maximum Age at 0 | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a row to the Definitions table<br>3. Enter a Loan Product in the Loan_Product field<br>4. Select a Category from the dropdown<br>5. Enter a positive number in the Minimum_Age field<br>6. Enter 0 in the Maximum_Age field<br>7. Enter a valid Provisioning_Percentage in the field<br>8. Select valid Liability Account and Expense Account from the dropdowns | Form submits successfully; entry is created with Maximum Age set to 0 | medium |
| TC-015 (boundary) |  | Add a Definitions entry with Provisioning Percentage at 0 | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a row to the Definitions table<br>3. Enter a Loan Product in the Loan_Product field<br>4. Select a Category from the dropdown<br>5. Enter a valid Minimum_Age in the field<br>6. Enter a valid Maximum_Age in the field<br>7. Enter 0 in the Provisioning_Percentage field<br>8. Select valid Liability Account and Expense Account from the dropdowns | Form submits successfully; entry is created with Provisioning Percentage set to 0 | medium |
| TC-016 (input_edge) |  | Enter a long string in the Criteria Name field | User is on the Create Criteria Form | 1. Enter a string longer than 200 characters in the Criteria_Name field | Field displays an error indicating the input exceeds the maximum length allowed | low |
| TC-017 (input_edge) |  | Enter special characters in the Criteria Name field | User is on the Create Criteria Form | 1. Enter special characters in the Criteria_Name field | Field displays an error indicating invalid characters are not allowed | low |
| TC-018 (interaction_edge) |  | Rapidly submit the Create Criteria Form | User has filled out the Create Criteria Form | 1. Click the Submit button<br>2. Immediately click the Submit button again | Second submission attempt is blocked; only one record appears in the table | medium |

---

## Offices

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form from Offices page | User logged in as <Admin> | 1. Click '+ Create Office' button | The creation form opens | high |
| TC-002 | WF-002 | Successfully create a new office | User logged in as <Admin>, Creation form is open | 1. Enter <valid office name> in the Office Name field<br>2. Select 'Head Office' from the Parent Office dropdown<br>3. Enter <valid date> in the Opened On Date field<br>4. Click Submit | A success notification is displayed; the new office appears in the Offices table | high |
| TC-003 | WF-003 | View office details from the Offices table | User logged in as <Admin>, Offices table is displayed | 1. Click on the Office Name link of an existing office | The Office Detail page shows the office information | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Office Name field blank and submit |  | 1. Open the Create Office form<br>2. Leave the Office Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-005 |  | Leave the Parent Office field blank and submit |  | 1. Open the Create Office form<br>2. Leave the Parent Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-006 |  | Leave the Opened On Date field blank and submit |  | 1. Open the Create Office form<br>2. Leave the Opened On Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-007 |  | Submit the Create Office form with all required fields empty |  | 1. Open the Create Office form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Office Name, Parent Office, and Opened On Date fields display errors indicating they are required | high |
| TC-008 |  | Attempt to create an office with a Parent Office not set to Head Office |  | 1. Open the Create Office form<br>2. Fill the Office Name field with a valid name<br>3. Fill the Parent Office field with a non-root office<br>4. Fill the Opened On Date field with a valid date<br>5. Click Submit | Form does not submit; error shown indicating 'Head Office is the root' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Open date is today |  | 1. Click on '+ Create Office' button<br>2. Enter valid Office Name in the Office_Name field<br>3. Enter valid Parent Office in the Parent_Office field<br>4. Enter today's date in the Opened_On_Date field<br>5. Click Submit | Form submits successfully; new office is created with today's date | medium |
| TC-010 (boundary) |  | Open date is yesterday |  | 1. Click on '+ Create Office' button<br>2. Enter valid Office Name in the Office_Name field<br>3. Enter valid Parent Office in the Parent_Office field<br>4. Enter yesterday's date in the Opened_On_Date field<br>5. Click Submit | Form submits successfully; new office is created with yesterday's date | medium |
| TC-011 (boundary) |  | Open date is far future date |  | 1. Click on '+ Create Office' button<br>2. Enter valid Office Name in the Office_Name field<br>3. Enter valid Parent Office in the Parent_Office field<br>4. Enter a far future date in the Opened_On_Date field<br>5. Click Submit | Form submits successfully; new office is created with the far future date | medium |
| TC-012 (input_edge) |  | Enter long Office Name |  | 1. Click on '+ Create Office' button<br>2. Enter a long string (200+ characters) in the Office_Name field<br>3. Enter valid Parent Office in the Parent_Office field<br>4. Enter today's date in the Opened_On_Date field<br>5. Click Submit | Form submits successfully; new office is created with the long Office Name | low |
| TC-013 (input_edge) |  | Enter special characters in Office Name |  | 1. Click on '+ Create Office' button<br>2. Enter special characters in the Office_Name field<br>3. Enter valid Parent Office in the Parent_Office field<br>4. Enter today's date in the Opened_On_Date field<br>5. Click Submit | Form submits successfully; new office is created with special characters in Office Name | low |

---

## Employees

Total: **13** (positive: 4, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new employee with all required fields | User logged in as <Admin>, User is on the Employees page | 1. Click '+ Create Employee' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Click Submit | A success notification is displayed; the new employee appears in the Employees table with the entered Name and Office | high |
| TC-002 |  | Edit an existing employee's details | User logged in as <Admin>, User is on the Employees page, At least one employee exists | 1. Click the Edit action for the first employee in the Employees table<br>2. Change <valid office> in the Office field<br>3. Change <valid mobile number> in the Mobile Number field<br>4. Click Submit | A success notification is displayed; the updated employee details are visible in the Staff Detail page | medium |
| TC-003 |  | Delete selected employees from the table | User logged in as <Admin>, User is on the Employees page, At least one employee exists | 1. Select the checkbox for the first employee in the Employees table<br>2. Click 'Delete Selected'<br>3. Confirm deletion | The selected employee is no longer present in the Employees table | medium |
| TC-004 |  | Sort employees by Name column | User logged in as <Admin>, User is on the Employees page, At least two employees exist | 1. Click on the Name column header to sort<br>2. Observe the order of employees in the Employees table | Employees are sorted in ascending order by Name | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Office field blank and submit the Create Employee form |  | 1. Leave the Office field blank<br>2. Fill First Name and Last Name fields with valid data<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-006 |  | Leave the First Name field blank and submit the Create Employee form |  | 1. Leave the First Name field blank<br>2. Fill Office and Last Name fields with valid data<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-007 |  | Leave the Last Name field blank and submit the Create Employee form |  | 1. Leave the Last Name field blank<br>2. Fill Office and First Name fields with valid data<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-008 |  | Submit the Create Employee form with all required fields empty |  | 1. Leave the Office, First Name, and Last Name fields blank<br>2. Click Submit | Form does not submit; errors shown on Office, First Name, and Last Name fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Open the Create Employee form<br>2. Enter a string of 200+ characters in the First Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; saved value in the First Name field is either accepted or truncated | low |
| TC-010 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Open the Create Employee form<br>2. Enter special characters (e.g., @#$%^&*) in the Last Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; saved value in the Last Name field displays correctly with special characters | low |
| TC-011 (input_edge) |  | Enter a value with leading and trailing whitespace in the Office field |  | 1. Open the Create Employee form<br>2. Enter '  New York  ' in the Office field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value in the Office field shows 'New York' | low |
| TC-012 (data_edge) |  | Enter today's date in the Joining Date field |  | 1. Open the Create Employee form<br>2. Enter today's date in the Joining Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; Joining Date field displays today's date correctly | medium |
| TC-013 (data_edge) |  | Enter a future date in the Joining Date field |  | 1. Open the Create Employee form<br>2. Enter a date 10 years in the future in the Joining Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; Joining Date field displays the future date correctly | medium |

---

## Teller & Cashier Management

Total: **22** (positive: 5, negative: 11, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new teller with all required fields | User logged in as <Admin>, Teller page is open | 1. Click '+ Create Teller' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid teller name> in the Teller Name field<br>4. Enter <valid start date> in the Start Date field<br>5. Select 'Active' from the Status dropdown<br>6. Click Submit | A success notification is displayed; the Teller Name appears in the Tellers table | high |
| TC-002 |  | View teller details after creating a teller | User logged in as <Admin>, Teller page is open, A teller has been created | 1. Click on the Teller Name link in the Tellers table | The Teller Detail page displays the teller's information and a list of assigned cashiers | high |
| TC-003 |  | Allocate a cashier to a teller | User logged in as <Admin>, Teller Detail page is open, A teller exists | 1. Click '+ Allocate Cashier' button<br>2. Enter <valid staff name> in the Staff field<br>3. Enter <valid start date> in the Start Date field<br>4. Click Submit | A success notification is displayed; the Cashier Name appears in the Cashiers section of the Teller Detail page | high |
| TC-004 |  | Settle cash for a cashier | User logged in as <Admin>, Cashier Detail page is open, A cashier exists | 1. Enter <valid amount> in the Amount field<br>2. Select <valid currency> from the Currency dropdown<br>3. Enter <valid transaction date> in the Transaction Date field<br>4. Click 'Settle Cash' | A success notification is displayed; the Cashier Transactions List updates to show the new settlement entry | high |
| TC-005 |  | View cashier transactions list | User logged in as <Admin>, Cashier Detail page is open, Cashier transactions exist | 1. Navigate to the Cashier Transactions List | The Cashier Transactions List displays all transactions with Date, Type, Amount, and Running Balance columns | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Office field blank in Create Teller form |  | 1. Open the Create Teller form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 |  | Leave the Teller Name field blank in Create Teller form |  | 1. Open the Create Teller form<br>2. Leave the Teller Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Teller Name field indicating it is required | high |
| TC-008 |  | Leave the Start Date field blank in Create Teller form |  | 1. Open the Create Teller form<br>2. Leave the Start Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-009 |  | Submit Create Teller form with all required fields empty |  | 1. Open the Create Teller form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Teller is not created; error shown on Office, Teller Name, and Start Date fields | high |
| TC-010 |  | Leave the Staff field blank in Allocate Cashier form |  | 1. Open the Allocate Cashier form<br>2. Leave the Staff field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Staff field indicating it is required | high |
| TC-011 |  | Leave the Start Date field blank in Allocate Cashier form |  | 1. Open the Allocate Cashier form<br>2. Leave the Start Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-012 |  | Submit Allocate Cashier form with all required fields empty |  | 1. Open the Allocate Cashier form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Cashier is not allocated; error shown on Staff and Start Date fields | high |
| TC-013 |  | Leave the Amount field blank in Settle Cash action |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash action<br>3. Leave the Amount field blank<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-014 |  | Leave the Currency field blank in Settle Cash action |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash action<br>3. Leave the Currency field blank<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-015 |  | Leave the Transaction Date field blank in Settle Cash action |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash action<br>3. Leave the Transaction Date field blank<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-016 |  | Submit Settle Cash action with all required fields empty |  | 1. Open the Cashier Detail page<br>2. Click on Settle Cash action<br>3. Leave all required fields blank<br>4. Click Submit | Form does not submit; Cash is not settled; error shown on Amount, Currency, and Transaction Date fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) |  | Start Date equals End Date | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller Name field<br>3. Enter today's date in the Start Date field<br>4. Enter today's date in the End Date field<br>5. Select Active from the Status dropdown<br>6. Click Submit | Form submits successfully; teller is created with Start Date and End Date both set to today | medium |
| TC-018 (boundary) |  | End Date is one day before Start Date | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller Name field<br>3. Enter today's date in the Start Date field<br>4. Enter yesterday's date in the End Date field<br>5. Select Active from the Status dropdown<br>6. Click Submit | Form is blocked; error displayed indicating End Date must be on or after Start Date | medium |
| TC-019 (boundary) |  | Allocate Cashier with Start Date equals End Date | User is on the Allocate Cashier Form | 1. Enter a valid Staff name in the Staff field<br>2. Enter today's date in the Start Date field<br>3. Enter today's date in the End Date field<br>4. Click Submit | Form submits successfully; cashier is allocated with Start Date and End Date both set to today | medium |
| TC-020 (boundary) |  | End Date is one day before Start Date in Allocate Cashier Form | User is on the Allocate Cashier Form | 1. Enter a valid Staff name in the Staff field<br>2. Enter today's date in the Start Date field<br>3. Enter yesterday's date in the End Date field<br>4. Click Submit | Form is blocked; error displayed indicating End Date must be on or after Start Date | medium |
| TC-021 (input_edge) |  | Long Description in Create Teller Form | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller Name field<br>3. Enter a very long string (200+ characters) in the Description field<br>4. Enter today's date in the Start Date field<br>5. Select Active from the Status dropdown<br>6. Click Submit | Form submits successfully; description is saved correctly or truncated with a visible indicator | low |
| TC-022 (input_edge) |  | Special characters in Teller Name | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter special characters in the Teller Name field<br>3. Enter today's date in the Start Date field<br>4. Select Active from the Status dropdown<br>5. Click Submit | Form is blocked; error displayed indicating invalid characters in Teller Name | low |

---

## Users & Roles

Total: **22** (positive: 4, negative: 12, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new user with valid details | User logged in as <Admin> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <valid office> in the Office field<br>7. Select <staff option> from the Staff dropdown<br>8. Enter <valid password> in the Password field<br>9. Enter <same valid password> in the Repeat Password field<br>10. Select <roles> from the Roles checkboxes<br>11. Check the Override Password Expiry Policy checkbox<br>12. Check the Send Password to Email checkbox<br>13. Click Submit | A success notification is displayed; the new user appears in the Users table with the entered Username | high |
| TC-002 |  | Create a new role with valid details | User logged in as <Admin> | 1. Click '+ Create Role' button<br>2. Enter <valid role name> in the Role Name field<br>3. Enter <optional description> in the Description field<br>4. Click Submit | A success notification is displayed; the new role appears in the Roles table with the entered Role Name | high |
| TC-003 |  | View user details from the Users table | User logged in as <Admin>, At least one user exists in the Users table | 1. Click on the Username link of the first user in the Users table | User detail page displays the selected user's information | medium |
| TC-004 |  | View role details from the Roles table | User logged in as <Admin>, At least one role exists in the Roles table | 1. Click on the Name link of the first role in the Roles table | Role detail page displays the selected role's information | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-006 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-007 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-008 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 |  | Enter an invalid email format in the Email field |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email format | medium |
| TC-010 |  | Leave the Office field blank and submit |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Enter a password that does not meet the policy |  | 1. Enter <password that does not meet policy> in the Password field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it must meet password policy | medium |
| TC-013 |  | Leave the Repeat Password field blank and submit |  | 1. Leave the Repeat Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match Password | high |
| TC-014 |  | Enter a mismatched password in Repeat Password field |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Repeat Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match Password | high |
| TC-015 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Inline validation errors appear on the Username, First Name, Last Name, Email, Office, and Password fields indicating they are required | high |
| TC-016 |  | Submit with a duplicate Username |  | 1. Enter <duplicate username> in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Username field indicating it must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) |  | Username must be unique - existing username | A user with the username 'existing_user' already exists. | 1. Enter 'existing_user' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error message 'Username must be unique' is displayed. | medium |
| TC-018 (boundary) |  | Email must be valid email format - invalid email |  | 1. Enter 'invalid_email_format' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error message 'Email must be valid email format' is displayed. | medium |
| TC-019 (input_edge) |  | Long text in First Name field |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is either accepted or an error is shown indicating the input is too long. | low |
| TC-020 (input_edge) |  | Leading/trailing whitespace in Last Name field |  | 1. Enter '   Smith   ' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |
| TC-021 (interaction_edge) |  | Rapid consecutive state transitions after user creation | User creation form is open. | 1. Fill all required fields with valid data<br>2. Click Submit<br>3. Immediately click Submit again after the first submission | Second submission attempt is blocked; the form remains on the creation page without creating a duplicate user. | medium |
| TC-022 (data_edge) |  | Test today's date and far future date in permissions |  | 1. Attempt to set permissions for today's date<br>2. Attempt to set permissions for a far future date | Both attempts are accepted without errors, indicating date handling is correct. | low |

---

## Reports

Total: **13** (positive: 5, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Run report generates the report as a data table | User logged in as <Role>, User is on the Reports page | 1. Click on a report link to open the parameters form<br>2. Fill in the parameters as needed<br>3. Click 'Run Report' | The report is generated as a data table | high |
| TC-002 |  | View report on screen displays report on screen | User logged in as <Role>, User is on the Reports page | 1. Click on a report link to open the parameters form<br>2. Fill in the parameters as needed<br>3. Click 'View on Screen' | The report is displayed on screen | high |
| TC-003 |  | Export report to Excel exports report to Excel | User logged in as <Role>, User is on the Reports page | 1. Click on a report link to open the parameters form<br>2. Fill in the parameters as needed<br>3. Click 'Export to Excel' | The report is exported to Excel | medium |
| TC-004 |  | Export report to CSV exports report to CSV | User logged in as <Role>, User is on the Reports page | 1. Click on a report link to open the parameters form<br>2. Fill in the parameters as needed<br>3. Click 'Export to CSV' | The report is exported to CSV | medium |
| TC-005 |  | Export report to PDF exports report to PDF | User logged in as <Role>, User is on the Reports page | 1. Click on a report link to open the parameters form<br>2. Fill in the parameters as needed<br>3. Click 'Export to PDF' | The report is exported to PDF | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to run report with all fields empty |  | 1. Open the parameters form for a report<br>2. Leave all fields blank<br>3. Click 'Run Report' | Form does not submit; no report is generated; all fields are highlighted |  |
| TC-007 |  | Attempt to view report on screen with all fields empty |  | 1. Open the parameters form for a report<br>2. Leave all fields blank<br>3. Click 'View on Screen' | Form does not submit; no report is displayed; all fields are highlighted |  |
| TC-008 |  | Attempt to export report to Excel with all fields empty |  | 1. Open the parameters form for a report<br>2. Leave all fields blank<br>3. Click 'Export to Excel' | Form does not submit; no report is exported; all fields are highlighted |  |
| TC-009 |  | Attempt to export report to CSV with all fields empty |  | 1. Open the parameters form for a report<br>2. Leave all fields blank<br>3. Click 'Export to CSV' | Form does not submit; no report is exported; all fields are highlighted |  |
| TC-010 |  | Attempt to export report to PDF with all fields empty |  | 1. Open the parameters form for a report<br>2. Leave all fields blank<br>3. Click 'Export to PDF' | Form does not submit; no report is exported; all fields are highlighted |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long string in the Loan Officer field |  | 1. Open the Reports page<br>2. Click on a report to open the parameters form<br>3. Enter a string of 200+ characters in the Loan Officer field<br>4. Click Run Report | The form submits successfully; the Loan Officer field displays the long string correctly in the report output | low |
| TC-012 (input_edge) |  | Enter special characters in the Currency field |  | 1. Open the Reports page<br>2. Click on a report to open the parameters form<br>3. Enter special characters (e.g., $%^&*) in the Currency field<br>4. Click Run Report | The form submits successfully; the Currency field displays the special characters correctly in the report output | low |
| TC-013 (input_edge) |  | Enter leading and trailing whitespace in the Office field |  | 1. Open the Reports page<br>2. Click on a report to open the parameters form<br>3. Enter '  Office Name  ' (with leading and trailing spaces) in the Office field<br>4. Click Run Report | Leading/trailing whitespace is trimmed; saved value shown in the report output has no extra spaces | low |

---

## Account Transfers & Standing Instructions

Total: **15** (positive: 6, negative: 3, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient for the transfer | 1. Enter <valid From Office> in the From Office field<br>2. Enter <valid From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <valid To Office> in the To Office field<br>5. Enter <valid To Client> in the To Client field<br>6. Enter <valid To Account Type> in the To Account Type field<br>7. Enter <valid transfer amount> in the Transfer Amount field<br>8. Select <valid date> in the Transfer Date field<br>9. Enter <optional description> in the Description field<br>10. Click Submit | The transfer is processed, debiting the source and crediting the destination | high |
| TC-002 |  | Show error when transfer amount exceeds available balance | User logged in as <Role>, Available balance is less than the transfer amount | 1. Enter <valid From Office> in the From Office field<br>2. Enter <valid From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <valid To Office> in the To Office field<br>5. Enter <valid To Client> in the To Client field<br>6. Enter <valid To Account Type> in the To Account Type field<br>7. Enter <amount greater than available balance> in the Transfer Amount field<br>8. Select <valid date> in the Transfer Date field<br>9. Click Submit | An error is shown indicating that the transfer amount exceeds the available balance | high |
| TC-003 |  | Create a standing instruction successfully | User logged in as <Role> | 1. Click '+ Create Standing Instruction'<br>2. Enter <valid Name> in the Name field<br>3. Enter <valid From Account> in the From Account field<br>4. Enter <valid To Account> in the To Account field<br>5. Select 'Fixed' from the Instruction Type dropdown<br>6. Enter <valid amount> in the Amount field<br>7. Select <valid Validity From date> in the Validity From field<br>8. Select <valid Validity Till date> in the Validity Till field<br>9. Select 'Periodic' from the Recurrence Type dropdown<br>10. Click Submit | The standing instruction is created successfully and appears in the Standing Instructions table | high |
| TC-004 |  | Enable a standing instruction | User logged in as <Role>, At least one standing instruction exists in the table | 1. Select the standing instruction to enable<br>2. Click Enable | The selected standing instruction status updates to 'Active' in the Standing Instructions table | medium |
| TC-005 |  | Disable a standing instruction | User logged in as <Role>, At least one standing instruction exists in the table | 1. Select the standing instruction to disable<br>2. Click Disable | The selected standing instruction status updates to 'Disabled' in the Standing Instructions table | medium |
| TC-006 |  | Delete a standing instruction | User logged in as <Role>, At least one standing instruction exists in the table | 1. Select the standing instruction to delete<br>2. Click Delete | The selected standing instruction is removed from the Standing Instructions table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Transfer Amount field left blank |  | 1. Leave the Transfer Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Transfer Amount field displays an error: 'This field is required.' | high |
| TC-008 |  | Transfer Date field left blank |  | 1. Leave the Transfer Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Transfer Date field displays an error: 'This field is required.' | high |
| TC-009 |  | Transfer Amount exceeds available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Transfer Amount field displays an error: 'Amount must not exceed available balance.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Transfer Amount exactly matches available balance | User has sufficient balance in the account | 1. Enter the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-011 (boundary) |  | Transfer Amount exceeds available balance by 1 unit | User has insufficient balance in the account | 1. Enter an amount greater than the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Error is shown indicating that the transfer amount exceeds the available balance | medium |
| TC-012 (state_edge) |  | Transfer Date is set to today |  | 1. Enter today's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-013 (state_edge) |  | Transfer Date is set to yesterday |  | 1. Enter yesterday's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-014 (data_edge) |  | Enter a very long description |  | 1. Enter a string longer than 200 characters in the Description field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is either accepted or the description is truncated with a visible indicator | low |
| TC-015 (input_edge) |  | Enter special characters in the Name field of Create Standing Instruction Form |  | 1. Open Create Standing Instruction Form<br>2. Enter special characters in the Name field<br>3. Click Submit | Form submission is either accepted or a specific error is shown | low |

---

## Tax Management

Total: **18** (positive: 4, negative: 6, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new tax component successfully | User logged in as <Admin>, Tax Components page is open | 1. Click '+ Create Tax Component' button<br>2. Enter <valid tax component name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Enter <valid debit account> in the Debit Account field<br>6. Select 'Liability' from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Enter <valid start date> in the Start Date field<br>9. Click '+ Create Tax Component' button | A success notification is displayed; the Tax Components table shows the new tax component with the entered Name and Percentage | high |
| TC-002 |  | Create a new tax group successfully | User logged in as <Admin>, Tax Groups page is open | 1. Click '+ Create Tax Group' button<br>2. Enter <valid tax group name> in the Name field<br>3. Click 'Add Tax Component' to add a new component<br>4. Enter <valid start date> in the Start Date field<br>5. Enter <valid end date> in the End Date field<br>6. Select 'Income' from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Click '+ Create Tax Group' button | A success notification is displayed; the Tax Groups table shows the new tax group with the entered Name | high |
| TC-003 |  | View tax components in the data table | User logged in as <Admin>, Tax Components page is open | 1. Observe the Tax Components table | The Tax Components table displays columns for Name, Percentage, Debit Account Type, Debit Account, Credit Account Type, Credit Account, and Start Date | medium |
| TC-004 |  | View tax groups in the data table | User logged in as <Admin>, Tax Groups page is open | 1. Observe the Tax Groups table | The Tax Groups table displays columns for Name and Associated Components | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Name field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Name field blank<br>3. Fill in the Percentage field with a valid number<br>4. Select a Debit Account Type<br>5. Fill in the Start Date<br>6. Click + Create Tax Component | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Leave the Percentage field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Percentage field blank<br>3. Fill in the Name field with a valid name<br>4. Select a Debit Account Type<br>5. Fill in the Start Date<br>6. Click + Create Tax Component | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-007 |  | Leave the Start Date field blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Start Date field blank<br>3. Fill in the Name field with a valid name<br>4. Fill in the Percentage field with a valid number<br>5. Select a Debit Account Type<br>6. Click + Create Tax Component | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-008 |  | Leave all required fields blank in Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Leave the Name field blank<br>3. Leave the Percentage field blank<br>4. Leave the Start Date field blank<br>5. Click + Create Tax Component | Form does not submit; error shown on Name, Percentage, and Start Date fields | high |
| TC-009 |  | Leave the Start Date field blank in Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Leave the Name field blank<br>3. Fill in the Start Date field with a valid date<br>4. Click + Create Tax Group | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 |  | Leave all required fields blank in Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Leave the Name field blank<br>3. Click + Create Tax Group | Form does not submit; error shown on Name field | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Enter exactly 0 in the Percentage field | Navigate to Create Tax Component Form | 1. Enter 0 in the Percentage field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submits successfully; entity is created with the Percentage value of 0 | medium |
| TC-012 (boundary) |  | Enter exactly 100 in the Percentage field | Navigate to Create Tax Component Form | 1. Enter 100 in the Percentage field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submits successfully; entity is created with the Percentage value of 100 | medium |
| TC-013 (boundary) |  | Enter 101 in the Percentage field | Navigate to Create Tax Component Form | 1. Enter 101 in the Percentage field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submission is blocked; an error message indicates that the Percentage must be less than or equal to 100 | medium |
| TC-014 (boundary) |  | Add maximum allowed entries to the Tax Components repeating group | Navigate to Create Tax Group Form | 1. Add maximum allowed entries to the Tax Components section<br>2. Click + Create Tax Group | Form submits successfully; all entries are saved | medium |
| TC-015 (boundary) |  | Attempt to add one more entry to the Tax Components repeating group | Navigate to Create Tax Group Form | 1. Add maximum allowed entries to the Tax Components section<br>2. Attempt to add one more entry<br>3. Click + Create Tax Group | Form submission is blocked; an error message indicates that the maximum number of entries has been reached | medium |
| TC-016 (data_edge) |  | Enter today's date in the Start Date field | Navigate to Create Tax Component Form | 1. Enter today's date in the Start Date field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submits successfully; entity is created with today's date in the Start Date field | medium |
| TC-017 (data_edge) |  | Enter a date in the Start Date field that is one day in the past | Navigate to Create Tax Component Form | 1. Enter yesterday's date in the Start Date field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submission is blocked; an error message indicates that the Start Date must not be in the past | medium |
| TC-018 (input_edge) |  | Enter a very long string in the Name field | Navigate to Create Tax Component Form | 1. Enter a string longer than 200 characters in the Name field<br>2. Fill all other required fields<br>3. Click + Create Tax Component | Form submission is blocked; an error message indicates that the Name exceeds the maximum allowed length | low |

---

## Organization Settings

Total: **15** (positive: 6, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the Holiday Creation Form | User logged in as <Admin>, Holidays page is open | 1. Click '+ Create Holiday' button | The holiday creation form is opened | high |
| TC-002 | WF-001 | Create a Holiday Successfully | User logged in as <Admin>, Holiday creation form is open | 1. Enter <valid holiday name> in the Name field<br>2. Enter <valid start date> in the From Date field<br>3. Enter <valid end date> in the To Date field<br>4. Click Submit | The holiday is created and displayed in the Holidays table | high |
| TC-003 | WF-002 | Configure Working Days | User logged in as <Admin>, Working Days page is open | 1. Check the checkbox for Monday<br>2. Check the checkbox for Wednesday<br>3. Click Submit | The selected working days are saved and reflected in the Working Days settings | medium |
| TC-004 | WF-003 | Add a New Payment Type | User logged in as <Admin>, Payment Types page is open | 1. Click '+ Create' button<br>2. Enter <valid payment type name> in the Name field<br>3. Enter <valid description> in the Description field<br>4. Select <Is Cash Payment option> from the dropdown<br>5. Click Submit | The new payment type is added to the dropdown options | high |
| TC-005 | WF-004 | Select Active Currencies | User logged in as <Admin>, Currencies page is open | 1. Select <valid currency> from the list<br>2. Click Submit | The selected currency is marked as active | medium |
| TC-006 | WF-005 | Upload Data for Bulk Import | User logged in as <Admin>, Bulk Import page is open | 1. Click Upload<br>2. Select <valid data file> from the OS dialog<br>3. Click Submit | The data is uploaded successfully and processed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Name field blank in Create Holiday Form |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill in valid dates for From Date and To Date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-008 |  | Leave the From Date field blank in Create Holiday Form |  | 1. Click on '+ Create Holiday'<br>2. Leave the From Date field blank<br>3. Fill in valid values for Name and To Date<br>4. Click Submit | Inline validation error appears on the From_Date field indicating it is required | high |
| TC-009 |  | Leave the To Date field blank in Create Holiday Form |  | 1. Click on '+ Create Holiday'<br>2. Leave the To Date field blank<br>3. Fill in valid values for Name and From Date<br>4. Click Submit | Inline validation error appears on the To_Date field indicating it is required | high |
| TC-010 |  | Submit Create Holiday Form with all required fields empty |  | 1. Click on '+ Create Holiday'<br>2. Leave all required fields (Name, From Date, To Date) blank<br>3. Click Submit | Form does not submit; Holiday is not created; error shown on Name, From_Date, and To_Date fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Create Holiday with From_Date equal to To_Date |  | 1. Click on '+ Create Holiday' button<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Click Submit | Form submits successfully; holiday is created with From_Date and To_Date both set to today's date. | medium |
| TC-012 (boundary) |  | Create Holiday with To_Date one day after From_Date |  | 1. Click on '+ Create Holiday' button<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Click Submit | Form submits successfully; holiday is created with From_Date set to today and To_Date set to tomorrow. | medium |
| TC-013 (input_edge) |  | Enter long text in Name field |  | 1. Click on '+ Create Holiday' button<br>2. Enter a very long string (200+ characters) in the Name field<br>3. Enter a valid date in From_Date<br>4. Enter a valid date in To_Date<br>5. Click Submit | Form submits successfully; Name field accepts long text without error. | low |
| TC-014 (input_edge) |  | Enter special characters in Name field |  | 1. Click on '+ Create Holiday' button<br>2. Enter special characters in the Name field<br>3. Enter a valid date in From_Date<br>4. Enter a valid date in To_Date<br>5. Click Submit | Form submits successfully; Name field accepts special characters without error. | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after creating a holiday |  | 1. Click on '+ Create Holiday' button<br>2. Enter a valid Name in the Name field<br>3. Enter a valid date in From_Date<br>4. Enter a valid date in To_Date<br>5. Click Submit<br>6. Immediately click Submit again after the success message | Second submission attempt is blocked; the form remains blank without creating a duplicate holiday. | medium |

---

## System Administration

Total: **21** (positive: 7, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Edit Scheduler Job to toggle active status | User logged in as <Admin>, Manage Scheduler Jobs page is open | 1. Click Edit on the job 'Apply Annual Fee'<br>2. Toggle the Is Active checkbox to activate the job<br>3. Click Save | The job 'Apply Annual Fee' is now active; the Is Active toggle reflects the change. | high |
| TC-002 |  | Edit Scheduler Job to update CRON expression | User logged in as <Admin>, Manage Scheduler Jobs page is open | 1. Click Edit on the job 'Add Accrual Transactions'<br>2. Enter '0 12 * * *' in the CRON Expression field<br>3. Click Save | The CRON Expression for 'Add Accrual Transactions' is updated to '0 12 * * *'. | high |
| TC-003 |  | Start all scheduled jobs using global toggle | User logged in as <Admin>, Manage Scheduler Jobs page is open | 1. Toggle the Global Toggle checkbox to start all jobs<br>2. Click Confirm | All scheduled jobs are now running; the Global Toggle reflects the active state. | high |
| TC-004 |  | Edit Global Configuration setting | User logged in as <Admin>, Global Configuration page is open | 1. Click Edit on the configuration 'maker-checker'<br>2. Toggle the Enabled checkbox to enable the setting<br>3. Click Save | The configuration 'maker-checker' is now enabled; the Enabled toggle reflects the change. | high |
| TC-005 |  | Edit Manage Codes entry | User logged in as <Admin>, Manage Codes page is open | 1. Click Edit on the code 'Client Type'<br>2. Add a new value 'Corporate'<br>3. Click Save | The code 'Client Type' now includes the value 'Corporate'. | high |
| TC-006 |  | Create new custom data table | User logged in as <Admin>, Manage Data Tables page is open | 1. Enter 'Custom Client Data' in the Data Table Name field<br>2. Select 'm_client' from the Application Table Name dropdown<br>3. Check the Multi Row checkbox<br>4. Click 'Add Column Definition'<br>5. Enter 'Client ID' in the Name field<br>6. Select 'string' from the Type dropdown<br>7. Enter '10' in the Length field<br>8. Check the Is Mandatory checkbox<br>9. Click Save | The custom data table 'Custom Client Data' is created with the specified column definitions. | high |
| TC-007 |  | View Audit Trails with filters | User logged in as <Admin>, Audit Trails page is open | 1. Enter 'Create' in the Action Name search field<br>2. Click Search | The Audit Trails table displays only entries with 'Create' in the Action Name. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the Data Table Name blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Click on Create<br>3. Leave the Data Table Name field blank<br>4. Select an Application Table Name<br>5. Click Submit | Form does not submit; Data Table Name is required and highlighted | high |
| TC-009 |  | Leave the Application Table Name dropdown unselected and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Click on Create<br>3. Enter a valid Data Table Name<br>4. Leave the Application Table Name dropdown unselected<br>5. Click Submit | Form does not submit; Application Table Name is required and highlighted | high |
| TC-010 |  | Leave the Name field in Column Definitions blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Click on Create<br>3. Enter a valid Data Table Name<br>4. Select an Application Table Name<br>5. Check Multi Row<br>6. Leave the Name field in Column Definitions blank<br>7. Click Submit | Form does not submit; Name is required in Column Definitions and highlighted | high |
| TC-011 |  | Attempt to edit a scheduler job without filling CRON Expression |  | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click Edit on a job<br>3. Leave the CRON Expression field blank<br>4. Click Save | Form does not submit; CRON Expression is required and highlighted | high |
| TC-012 |  | Attempt to start/stop scheduler without toggling Global Toggle |  | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click Start/Stop Scheduler<br>3. Leave Global Toggle unchecked<br>4. Click Submit | Form does not submit; Global Toggle is required and highlighted | high |
| TC-013 |  | Leave the Maker ID field blank in Audit Trails View and submit |  | 1. Navigate to the Audit Trails page<br>2. Click View<br>3. Leave the Maker ID field blank<br>4. Click Submit | Form does not submit; Maker ID is required and highlighted | high |
| TC-014 |  | Attempt to view audit trails with invalid date range |  | 1. Navigate to the Audit Trails page<br>2. Enter an invalid date range<br>3. Click Submit | Form does not submit; Date Range is invalid and highlighted | medium |
| TC-015 |  | Attempt to edit Global Configuration without filling Value field |  | 1. Navigate to the Global Configuration page<br>2. Click Edit on a configuration<br>3. Leave the Value field blank<br>4. Click Save | Form does not submit; Value is required and highlighted | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) |  | Add maximum allowed entries to Column Definitions | User is on the Manage Data Tables Create form | 1. Add <maximum allowed entries> rows to the Column Definitions repeating group<br>2. Fill in all required fields for each row<br>3. Click Submit | Form submits successfully; all entries are saved. | medium |
| TC-017 (boundary) |  | Attempt to add one more entry to Column Definitions | User is on the Manage Data Tables Create form | 1. Add <maximum allowed entries> rows to the Column Definitions repeating group<br>2. Attempt to add one more row<br>3. Click Submit | Submission is blocked; an error message indicates the maximum entry limit has been reached. | medium |
| TC-018 (input_edge) |  | Enter a very long Data Table Name | User is on the Manage Data Tables Create form | 1. Enter a string longer than 200 characters in the Data Table Name field<br>2. Fill in all other required fields<br>3. Click Submit | An error message is shown indicating the name exceeds the maximum length. | low |
| TC-019 (input_edge) |  | Enter special characters in the Data Table Name | User is on the Manage Data Tables Create form | 1. Enter special characters in the Data Table Name field<br>2. Fill in all other required fields<br>3. Click Submit | An error message is shown indicating invalid characters in the Data Table Name. | low |
| TC-020 (state_edge) |  | Rapidly toggle the Global Toggle for Start/Stop Scheduler | User is on the Manage Scheduler Jobs page | 1. Toggle the Global Toggle to Start<br>2. Immediately toggle it to Stop | The action succeeds, and the scheduler reflects the last toggle state. | medium |
| TC-021 (data_edge) |  | Test date filter with today's date and yesterday's date | User is on the Audit Trails page | 1. Enter today's date in the Date Range filter<br>2. Click Apply Filter<br>3. Enter yesterday's date in the Date Range filter<br>4. Click Apply Filter | Both filters return results for actions made today and yesterday. | medium |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User logs out successfully | User logged in as <User> | 1. Click <User Profile Icon> to reveal dropdown<br>2. Click 'Log Out' from the dropdown | terminates authenticated session, clears authentication token, redirects to login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access an authenticated page after logout | User is logged in | 1. Click on the User Profile Icon<br>2. Select 'Log Out' | User is redirected to the login page; authenticated session is terminated | high |
| TC-003 |  | Attempt to navigate to an authenticated page without logging in | User is not authenticated | 1. Attempt to access an authenticated page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) |  | Rapid logout attempts | User is logged in and on an authenticated page | 1. Click the User Profile Icon<br>2. Click Log Out<br>3. Immediately click Log Out again | Second logout attempt is blocked; user remains on the login page without additional logout action. | medium |
| TC-005 (interaction_edge) |  | Navigate to authenticated page after logout | User is logged in | 1. Click the User Profile Icon<br>2. Click Log Out<br>3. Attempt to navigate to an authenticated page | User is redirected to the login page. | medium |

---
