# Test Cases — Mifos

Generated: 2026-06-10T19:18:36.388299Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 529 | 164 | 190 | 175 | 273 | 203 | 51 |

## Login

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to Dashboard | high |
| TC-002 | WF-003 | Login with empty required fields | User logged in as <User> | 1. Leave Username field empty<br>2. Leave Password field empty<br>3. Click Login | shows inline validation messages | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-003 | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-004 | WF-003 | Leave the Password field blank and submit |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-005 | WF-002 | Submit with invalid credentials |  | 1. Fill the Username field with <invalid username><br>2. Fill the Password field with <invalid password><br>3. Click Login | Page displays 'Invalid credentials' error message | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-003 | Submit with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | Inline validation messages show for both Username and Password fields | medium |
| TC-007 (boundary) | WF-002 | Submit with invalid credentials |  | 1. Enter an invalid Username in the Username field<br>2. Enter an invalid Password in the Password field<br>3. Click the Login button | Error message shows indicating invalid credentials | medium |
| TC-008 (input_edge) |  | Enter long Username |  | 1. Enter a very long string (200+ characters) in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | System handles the input; either accepts or shows error for exceeding length | low |
| TC-009 (input_edge) |  | Enter special characters in Username |  | 1. Enter special characters (e.g., @#$%^&*) in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | System handles the input; either accepts or shows error for invalid characters | low |

---

## Home Page

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard from Home Page | User logged in as <Role> | 1. Click on the Dashboard button | redirects to dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to access the dashboard without being logged in | User is not authenticated | 1. Navigate to the Home Page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User is logged in and on the Home page | 1. Click the Dashboard button | User is redirected to the dashboard; Home page is not pre-filled upon back navigation | medium |
| TC-004 (input_edge) |  | Enter long text in Search Activity input | User is on the Home page | 1. Enter a string of 200+ characters in the Search Activity input | Input is either accepted or truncated with a visible indicator | low |
| TC-005 (input_edge) |  | Enter special characters in Search Activity input | User is on the Home page | 1. Enter a string with special characters in the Search Activity input | Input is accepted or a specific error is shown | low |

---

## Dashboard

Total: **6** (positive: 1, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard from Home page | User logged in as <Role> | 1. Click the Dashboard button on the Home page | Navigates to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access the Dashboard |  | 1. Attempt to click on the Dashboard button | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapidly click the Dashboard button multiple times | User is on the Home page | 1. Click the Dashboard button<br>2. Immediately click the Dashboard button again | Only one navigation occurs to the Dashboard; no duplicate entries or errors are shown. | medium |
| TC-004 (input_edge) |  | Enter a long search term in the Search Activity field | User is on the Dashboard | 1. Enter a string of 200+ characters in the Search Activity field | The field accepts the input or displays a visible error indicating the input is too long. | low |
| TC-005 (input_edge) |  | Enter special characters in the Search Activity field | User is on the Dashboard | 1. Enter special characters (e.g., @#$%^&*) in the Search Activity field | The field accepts the input or displays a specific error message. | low |
| TC-006 (input_edge) |  | Enter a value with leading and trailing whitespace in the Search Activity field | User is on the Dashboard | 1. Enter '   test search   ' in the Search Activity field | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces. | low |

---

## Global Search

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field | User logged in as <Role> | 1. Click the Search Icon in the top toolbar | opens search input field | high |
| TC-002 | WF-002 | Search with results found | User logged in as <Role>, Search input field is open | 1. Enter <valid search term> in the Search Input field | searches across Clients, Groups, Loans, and Savings accounts | high |
| TC-003 | WF-003 | Display no results message | User logged in as <Role>, Search input field is open | 1. Enter <non-matching search term> in the Search Input field | No results found | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user attempts to access search input |  | 1. Attempt to click on the Search Icon | User is redirected to the login page; search input field is not opened | high |
| TC-005 |  | Search input field submitted with empty input | user is logged in | 1. Click on the Search Icon<br>2. Leave the Search Input blank<br>3. Click Submit | No results found message is displayed; search results dropdown is not shown | high |
| TC-006 |  | Search input with invalid characters | user is logged in | 1. Click on the Search Icon<br>2. Enter <invalid characters> in the Search Input<br>3. Click Submit | No results found message is displayed; search results dropdown is not shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Search with a partial match of maximum length | User is logged in, Search input field is open | 1. Enter a partial match string that is at the maximum length supported by the search input | Search results display matching entities based on the entered partial match | medium |
| TC-008 (boundary) | WF-003 | Search with a string that results in no matches | User is logged in, Search input field is open | 1. Enter a string that is unlikely to match any entities | No results found message is displayed | medium |
| TC-009 (input_edge) |  | Search with special characters | User is logged in, Search input field is open | 1. Enter a string containing special characters (e.g., !@#$%^&*) in the search input | Search results display based on the entered string or an error message is shown | low |
| TC-010 (input_edge) |  | Search with leading and trailing whitespace | User is logged in, Search input field is open | 1. Enter a string with leading and trailing whitespace in the search input | Search results display matching entities without the extra spaces | low |

---

## Client Management

Total: **27** (positive: 9, negative: 10, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Client Details | User logged in as <Role> | 1. Click on the Name link of a client in the Clients table | Client details displayed | high |
| TC-002 | WF-002 | Import Client | User logged in as <Role> | 1. Click on the Import Client button | opens Bulk Import page | high |
| TC-003 | WF-003 | Create Client | User logged in as <Role> | 1. Click on the Create Client button | Client creation wizard opened | high |
| TC-004 | WF-004 | Download Client Excel Template | User logged in as <Role>, User is on the Bulk Import page | 1. Click on the Download Client Excel Template button | downloads template | medium |
| TC-005 | WF-006 | Submit Create Client | User logged in as <Role>, User is on Step 1 of the Create Client wizard | 1. Enter <valid office> in the Office field<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <unique external ID> in the External ID field<br>5. Enter <valid date> in the Submitted On field<br>6. Click Submit | creates client in Pending status | high |
| TC-006 | WF-007 | Activate Client | User logged in as <Role>, Client is in Pending status | 1. Click Activate<br>2. Enter <valid activation date> in the Activation Date field<br>3. Click Confirm on the Activation dialog | Client activated | high |
| TC-007 | WF-008 | Edit Client | User logged in as <Role>, Client is in Pending status | 1. Click Edit | Client details editable | medium |
| TC-008 | WF-009 | Reject Client | User logged in as <Role>, Client is in Pending status | 1. Click Reject<br>2. Enter <valid reason> in the Reason field<br>3. Click Confirm on the Reject dialog | Client rejected | medium |
| TC-009 | WF-010 | Withdraw Client | User logged in as <Role>, Client is in Pending status | 1. Click Withdraw<br>2. Enter <valid reason> in the Reason field<br>3. Click Confirm on the Withdraw dialog | Client withdrawn | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Leave the Office field blank in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the First Name field blank in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-012 |  | Leave the Last Name field blank in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-013 |  | Leave the Submitted On field blank in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Leave the Submitted On field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-014 |  | Submit with all required fields empty in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; multiple validation errors shown on required fields | high |
| TC-015 |  | Submit with non-unique External ID in Create Client wizard |  | 1. Open the Create Client wizard<br>2. Fill all required fields<br>3. Enter a duplicate value in the External ID field<br>4. Click Submit | Inline validation error appears on the External ID field indicating it must be unique | medium |
| TC-016 | WF-011 | Attempt to transfer client to the same office from Active state |  | 1. Open the Client Detail page for an Active client<br>2. Click Transfer Client<br>3. Select the same office in the Destination Office field<br>4. Click Submit | Inline validation error appears on the Destination Office field indicating same office is blocked | medium |
| TC-017 | WF-012 | Attempt to close client with active accounts from Active state |  | 1. Open the Client Detail page for an Active client<br>2. Click Close<br>3. Fill in the Closure Reason field<br>4. Click Submit | Inline validation error appears on the Closure Reason field indicating cannot close with active accounts | medium |
| TC-018 | WF-007 | Attempt to activate client with Activation Date before submission date |  | 1. Open the Client Detail page for a Pending client<br>2. Click Activate<br>3. Enter a date in the Activation Date field that is before the Submitted On date<br>4. Click Submit | Inline validation error appears on the Activation Date field indicating it must not be before submission date | medium |
| TC-019 |  | Attempt to view client details without authentication |  | 1. Attempt to access the Client Detail page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 (boundary) | WF-006 | Submit Create Client with unique External ID | User is on Create Client wizard | 1. Enter a valid value in the Office field<br>2. Enter a valid First Name<br>3. Enter a valid Last Name<br>4. Enter a unique value in the External ID field<br>5. Enter a valid value in the Submitted On field<br>6. Click Submit | Client is created in Pending status | medium |
| TC-021 (boundary) | WF-006 | Submit Create Client with duplicate External ID | User is on Create Client wizard | 1. Enter a valid value in the Office field<br>2. Enter a valid First Name<br>3. Enter a valid Last Name<br>4. Enter a duplicate value in the External ID field<br>5. Enter a valid value in the Submitted On field<br>6. Click Submit | Error shown indicating 'External ID must be unique' | medium |
| TC-022 (boundary) | WF-007 | Activate Client with Activation Date equal to Submitted On | Client is in Pending status | 1. Click Activate<br>2. Enter Activation Date equal to Submitted On date<br>3. Click Submit | Client is activated successfully | medium |
| TC-023 (boundary) | WF-007 | Activate Client with Activation Date before Submitted On | Client is in Pending status | 1. Click Activate<br>2. Enter Activation Date before Submitted On date<br>3. Click Submit | Error shown indicating 'Activation Date must not be before submission date' | medium |
| TC-024 (boundary) | WF-011 | Transfer Client to same office | Client is in Active status | 1. Click Transfer Client<br>2. Select the same office as the current office<br>3. Click Submit | Error shown indicating 'same office is blocked' | medium |
| TC-025 (boundary) | WF-012 | Close Client with active accounts | Client is in Active status and has active accounts | 1. Click Close<br>2. Enter Closure Reason<br>3. Click Submit | Error shown indicating 'cannot close with active accounts' | medium |
| TC-026 (input_edge) |  | Search with long name | User is on Clients page | 1. Enter a very long name (200+ characters) in the search field<br>2. Click Search | Search results display correctly or show a truncation indicator | low |
| TC-027 (input_edge) |  | Search with special characters | User is on Clients page | 1. Enter special characters (e.g., @#$%^&*) in the search field<br>2. Click Search | Search results display correctly or show a specific error | low |

---

## Group Management

Total: **21** (positive: 9, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Group Details | User logged in as <Role>, At least one group exists in the Groups Table | 1. Click on the Group Name of the desired group in the Groups Table | Group details displayed | high |
| TC-002 | WF-003 | Create New Group | User logged in as <Role> | 1. Click 'Create New Group' button<br>2. Enter <valid group name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | creates the group | high |
| TC-003 | WF-002 | Import Groups | User logged in as <Role> | 1. Click 'Import Groups' button<br>2. Click 'Download' button in the Groups Template Panel<br>3. Select a <valid file> in the File Picker<br>4. Click Upload | Groups imported successfully | medium |
| TC-004 | WF-004 | Upload Groups | User logged in as <Role> | 1. Click 'Import Groups' button<br>2. Select a <valid file> in the File Picker<br>3. Click Upload | Groups uploaded successfully | medium |
| TC-005 | WF-005 | Activate Group | User logged in as <Role>, At least one group exists in the Groups Table with status 'Pending' | 1. Click on the Group Name of the desired group in the Groups Table<br>2. Click Activate | Group activated | medium |
| TC-006 | WF-006 | Edit Group | User logged in as <Role>, At least one group exists in the Groups Table | 1. Click on the Group Name of the desired group in the Groups Table<br>2. Click Edit<br>3. Update <field> with <new value><br>4. Click Submit | Group edited | medium |
| TC-007 | WF-007 | Close Group | User logged in as <Role>, At least one group exists in the Groups Table with status 'Active' | 1. Click on the Group Name of the desired group in the Groups Table<br>2. Click Close | Group closed | medium |
| TC-008 | WF-008 | Assign Staff to Group | User logged in as <Role>, At least one group exists in the Groups Table | 1. Click on the Group Name of the desired group in the Groups Table<br>2. Click Assign Staff<br>3. Select <staff member> from the dropdown<br>4. Click Submit | Staff assigned to group | medium |
| TC-009 | WF-009 | Transfer Clients | User logged in as <Role>, At least one group exists in the Groups Table | 1. Click on the Group Name of the desired group in the Groups Table<br>2. Click Transfer Clients<br>3. Select <clients> to transfer<br>4. Click Submit | Clients transferred | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-003 | Leave the Name field blank and submit the Create Group form |  | 1. Leave the Name field blank<br>2. Fill the Office field with a valid value<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-011 | WF-003 | Leave the Office field blank and submit the Create Group form |  | 1. Fill the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-012 | WF-003 | Leave the Submitted On field blank and submit the Create Group form |  | 1. Fill the Name field with a valid value<br>2. Fill the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-013 | WF-004 | Leave the File Picker field blank and attempt to upload groups |  | 1. Leave the File Picker field blank<br>2. Click Upload | Inline validation error appears on the File Picker field indicating it is required | high |
| TC-014 | WF-005 | Attempt to activate a group without meeting the precondition | Group is already active | 1. Click Activate on the Group Detail page | Status remains Active; no transition occurs | medium |
| TC-015 | WF-007 | Attempt to close a group that is already closed | Group is already closed | 1. Click Close on the Group Detail page | Status remains Closed; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-003 | Create group with the minimum required fields filled |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Office field<br>3. Enter a valid value in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum required fields | medium |
| TC-017 (boundary) | WF-003 | Create group with missing required fields |  | 1. Leave the Name field empty<br>2. Leave the Office field empty<br>3. Click Submit | Form submission is blocked; error messages indicate that Name and Office are required | medium |
| TC-018 (boundary) | WF-004 | Upload file at the exact size limit |  | 1. Select a file that is exactly at the size limit for upload in the File Picker<br>2. Click Upload | File upload succeeds; success message is shown | medium |
| TC-019 (boundary) | WF-004 | Upload file exceeding the size limit |  | 1. Select a file that is one byte over the size limit in the File Picker<br>2. Click Upload | File upload is blocked; error message indicates the file exceeds the size limit | medium |
| TC-020 (input_edge) |  | Enter a long string in the Name field |  | 1. Enter a string longer than 200 characters in the Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is either accepted or shows an error indicating the field length limit | low |
| TC-021 (input_edge) |  | Enter special characters in the Office field |  | 1. Enter special characters in the Office field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is either accepted or shows an error for invalid characters | low |

---

## Center Management

Total: **18** (positive: 4, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Center Details | User logged in as <Role>, At least one center exists in the Centers Table | 1. Click on the Name link of the center in the Centers Table | Displays center details | high |
| TC-002 | WF-002 | Import Center | User logged in as <Role> | 1. Click on the 'Import Center' button<br>2. Upload a valid center file in the File Upload field<br>3. Click Submit | Centers imported successfully | high |
| TC-003 | WF-003 | Create Center | User logged in as <Role> | 1. Click on the 'Create Center' button<br>2. Enter <valid center name> in the Name field<br>3. Enter <valid office name> in the Office field<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | creates the center | high |
| TC-004 | WF-004 | Generate Collection Sheet | User logged in as <Role>, At least one group exists under the center | 1. Click on the 'Generate Collection Sheet' button | shows all groups and their clients with loan repayment and savings deposit amounts | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid entry<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the Office field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid entry<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 | WF-003 | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid entry<br>2. Fill in the Office field with a valid entry<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-008 | WF-002 | Leave the File Upload field blank and submit the Bulk Import Centers form |  | 1. Leave the File Upload field blank<br>2. Click Import Center | Inline validation error appears on the File Upload field indicating it is required | high |
| TC-009 |  | Attempt to activate a center that is already active | Center is in Active state | 1. Navigate to the Center Detail Page<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-010 |  | Attempt to close a center that is already closed | Center is in Closed state | 1. Navigate to the Center Detail Page<br>2. Click Close | Status remains Closed; no transition occurs | medium |
| TC-011 |  | Attempt to edit a center that is already closed | Center is in Closed state | 1. Navigate to the Center Detail Page<br>2. Click Edit | Edit action is not available; no edit form is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-003 | Submit Create Center form with minimum required fields filled |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Office field<br>3. Enter a valid value in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum required fields filled | medium |
| TC-013 (boundary) | WF-003 | Submit Create Center form with empty required fields |  | 1. Leave the Name field empty<br>2. Leave the Office field empty<br>3. Click Submit | Form submission is blocked; inline error shown for Name and Office fields indicating they are required | medium |
| TC-014 (boundary) | WF-002 | Upload file exactly at size limit for Bulk Import Centers |  | 1. Click on the File Upload field<br>2. Upload a file that is exactly at the size limit specified<br>3. Click Submit | File upload succeeds with a visible success indicator | medium |
| TC-015 (boundary) | WF-002 | Upload file exceeding size limit for Bulk Import Centers |  | 1. Click on the File Upload field<br>2. Upload a file that is one byte over the size limit<br>3. Click Submit | File upload is blocked; visible error shown indicating the file exceeds the size limit | medium |
| TC-016 (input_edge) |  | Enter long text in Name field |  | 1. Enter a string longer than 200 characters in the Name field<br>2. Fill other required fields<br>3. Click Submit | Form submits successfully; the saved value in the detail page shows the entered long text | low |
| TC-017 (input_edge) |  | Enter special characters in Office field |  | 1. Enter special characters in the Office field<br>2. Fill other required fields<br>3. Click Submit | Form submits successfully; the saved value in the detail page shows the entered special characters | low |
| TC-018 (interaction_edge) |  | Rapid re-submission after redirect from Create Center form |  | 1. Submit the Create Center form successfully<br>2. Press the browser back button<br>3. Click Submit again | The creation form is shown blank; no second entity is created | low |

---

## Loan Products

Total: **19** (positive: 4, negative: 6, edge: 9)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Loan Product Details | User logged in as <Role> | 1. Click on the Name of an existing loan product in the Loan Products Table | opens detail view | high |
| TC-002 | WF-002 | Edit Loan Product | User logged in as <Role> | 1. Click on the Edit option for an existing loan product in the Loan Products Table | opens detail view | high |
| TC-003 | WF-003 | Create New Loan Product | User logged in as <Role> | 1. Click the '+ Create Loan Product' button | opens 6-step stepper wizard | high |
| TC-004 | WF-004 | Complete Loan Product Creation | User logged in as <Role>, User is on the Details step of the Loan Product Stepper Wizard | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Click Next to proceed to the Currency step<br>4. Select <valid currency> from the Currency Selection dropdown<br>5. Enter <valid principal amount> in the Principal Amount field<br>6. Click Next to proceed to the Settings step<br>7. Select <valid amortization method> from the Amortization Method dropdown<br>8. Click Next to proceed to the Terms step<br>9. Enter <valid number of repayments> in the Number of Repayments field<br>10. Click Next to proceed to the Charges step<br>11. Click Next to proceed to the Accounting step<br>12. Select <valid accounting method> from the Accounting Method radio options<br>13. Click Submit to complete the loan product creation | Loan product created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Product Name blank and submit |  | 1. Click on the '+ Create Loan Product' button<br>2. Leave the Product Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the Short Name blank and submit |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill the Product Name field<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-007 | WF-004 | Submit the loan product creation with all required fields empty |  | 1. Click on the '+ Create Loan Product' button<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; loan product is not created; inline validation errors appear on Product Name and Short Name fields indicating they are required | high |
| TC-008 | WF-004 | Enter an invalid date in the Start Date field |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <invalid date format> in the Start Date field<br>4. Click Next | Inline validation error appears on the Start Date field indicating it must be a valid date | medium |
| TC-009 | WF-004 | Enter a Principal Amount below minimum value |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <amount below minimum> in the Principal Amount field<br>4. Click Next | Inline validation error appears on the Principal Amount field indicating it must be at least the minimum value | medium |
| TC-010 | WF-004 | Attempt to create a loan product with a duplicate External Id |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill all required fields with valid data<br>3. Enter <duplicate external id> in the External Id field<br>4. Click Submit | Form does not submit; loan product is not created; error shown indicating External Id must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-003 | Enter minimum value for Principal Amount |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 2<br>4. Enter the minimum allowed value in the Principal Amount field<br>5. Fill in all other required fields | Form submits successfully; loan product is created with the minimum Principal Amount value | medium |
| TC-012 (boundary) | WF-003 | Enter one unit below minimum for Principal Amount |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 2<br>4. Enter one unit below the minimum allowed value in the Principal Amount field<br>5. Fill in all other required fields | Submission is blocked; inline error shown indicating the Principal Amount must be at least the minimum value | medium |
| TC-013 (boundary) | WF-004 | Enter maximum value for Number of Repayments |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 4<br>4. Enter the maximum allowed value in the Number of Repayments field<br>5. Fill in all other required fields | Form submits successfully; loan product is created with the maximum Number of Repayments value | medium |
| TC-014 (boundary) | WF-004 | Enter one unit above maximum for Number of Repayments |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 4<br>4. Enter one unit above the maximum allowed value in the Number of Repayments field<br>5. Fill in all other required fields | Submission is blocked; inline error shown indicating the Number of Repayments must not exceed the maximum value | medium |
| TC-015 (boundary) | WF-004 | Enter maximum value for Nominal Interest Rate |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 4<br>4. Enter the maximum allowed value in the Nominal Interest Rate field<br>5. Fill in all other required fields | Form submits successfully; loan product is created with the maximum Nominal Interest Rate value | medium |
| TC-016 (boundary) | WF-004 | Enter one unit above maximum for Nominal Interest Rate |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in all required fields in Step 1<br>3. Go to Step 4<br>4. Enter one unit above the maximum allowed value in the Nominal Interest Rate field<br>5. Fill in all other required fields | Submission is blocked; inline error shown indicating the Nominal Interest Rate must not exceed the maximum value | medium |
| TC-017 (input_edge) |  | Enter a very long string in Product Name |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in a very long string in the Product Name field<br>3. Fill in all other required fields | Form submits successfully; the saved Product Name displays the long string correctly | low |
| TC-018 (input_edge) |  | Enter special characters in Short Name |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in special characters in the Short Name field<br>3. Fill in all other required fields | Form submits successfully; the saved Short Name displays the special characters correctly | low |
| TC-019 (input_edge) |  | Enter a value with leading/trailing whitespace in Description |  | 1. Click the '+ Create Loan Product' button<br>2. Fill in leading/trailing whitespace in the Description field<br>3. Fill in all other required fields | Leading/trailing whitespace is trimmed; saved Description shows no extra spaces | low |

---

## Savings Products

Total: **22** (positive: 10, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open stepper wizard to create a savings product | User logged in as <Role> | 1. Click the '+ Create Savings Product' button | The stepper wizard opens to Step 1: Details | high |
| TC-002 | WF-002 | View details of a savings product | User logged in as <Role> | 1. Click on a savings product link in the Name column | View details of the savings product | high |
| TC-003 | WF-003 | Open stepper wizard to create a fixed deposit product | User logged in as <Role> | 1. Click the '+ Create Fixed Deposit Product' button | The stepper wizard opens to Step 1: Details | high |
| TC-004 | WF-004 | Open stepper wizard to create a recurring deposit product | User logged in as <Role> | 1. Click the '+ Create Recurring Deposit Product' button | The stepper wizard opens to Step 1: Details | high |
| TC-005 | WF-001 | Complete Step 1 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 1: Details | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Click Next | The stepper wizard advances to Step 2: Currency | high |
| TC-006 | WF-001 | Complete Step 2 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 2: Currency | 1. Select <valid currency> from the Currency dropdown<br>2. Enter <valid decimal places> in the Decimal Places field<br>3. Enter <valid multiples> in the Currency In Multiples Of field<br>4. Click Next | The stepper wizard advances to Step 3: Terms | high |
| TC-007 | WF-001 | Complete Step 3 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 3: Terms | 1. Enter <valid nominal annual interest rate> in the Nominal Annual Interest Rate field<br>2. Select <valid compounding period> from the Interest Compounding Period dropdown<br>3. Select <valid posting period> from the Interest Posting Period dropdown<br>4. Select <valid calculation method> from the Interest Calculated Using dropdown<br>5. Select <valid days in year> from the Days in Year dropdown<br>6. Click Next | The stepper wizard advances to Step 4: Settings | high |
| TC-008 | WF-001 | Complete Step 4 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 4: Settings | 1. Enter <valid minimum opening balance> in the Minimum Opening Balance field<br>2. Enter <valid lock-in period> in the Lock-in Period field<br>3. Check the Apply Withdrawal Fee for Transfers checkbox<br>4. Enter <valid minimum balance for interest calculation> in the Minimum Balance for Interest Calculation field<br>5. Check the Enforce Minimum Required Balance checkbox<br>6. Enter <valid minimum required balance> in the Minimum Required Balance field<br>7. Check the Is Overdraft Allowed checkbox<br>8. Enter <valid maximum overdraft amount> in the Maximum Overdraft Amount field<br>9. Enter <valid overdraft interest rate> in the Overdraft Interest Rate field<br>10. Check the Enable Withhold Tax checkbox<br>11. Select <valid tax group> from the Tax Group dropdown<br>12. Check the Enable Dormancy Tracking checkbox<br>13. Enter <valid days to inactive> in the Days to Inactive field<br>14. Enter <valid days to dormancy> in the Days to Dormancy field<br>15. Enter <valid days to escheat> in the Days to Escheat field<br>16. Click Next | The stepper wizard advances to Step 5: Charges | high |
| TC-009 | WF-001 | Complete Step 5 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 5: Charges | 1. Enter <valid charge> in the Search and Add Charges field<br>2. Click Add Charge<br>3. Click Next | The stepper wizard advances to Step 6: Accounting | high |
| TC-010 | WF-001 | Complete Step 6 of the savings product wizard | User logged in as <Role>, The stepper wizard is open to Step 6: Accounting | 1. Select Cash-based from the Accounting Method radio options<br>2. Enter <valid savings reference> in the Savings Reference field<br>3. Enter <valid savings control> in the Savings Control field<br>4. Enter <valid transfers in suspense> in the Transfers in Suspense field<br>5. Enter <valid interest on savings> in the Interest on Savings field<br>6. Enter <valid income from fees> in the Income from Fees field<br>7. Enter <valid income from penalties> in the Income from Penalties field<br>8. Enter <valid escheat liability> in the Escheat Liability field<br>9. Click Submit | The savings product is created successfully and the stepper wizard closes | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Leave the Product Name field blank and submit |  | 1. Click on '+ Create Savings Product' button<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name field with a valid value<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-012 | WF-001 | Leave the Short Name field blank and submit |  | 1. Click on '+ Create Savings Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-013 | WF-001 | Submit with all required fields empty |  | 1. Click on '+ Create Savings Product' button<br>2. Leave the Product Name field blank<br>3. Leave the Short Name field blank<br>4. Click Next | Form does not submit; Product Name and Short Name fields display errors indicating they are required | high |
| TC-014 |  | Attempt to create a savings product without authentication |  | 1. Navigate to the Savings Products page without logging in<br>2. Click on '+ Create Savings Product' button | User is redirected to the login page | high |
| TC-015 | WF-003 | Attempt to create a fixed deposit product without authentication |  | 1. Navigate to the Savings Products page without logging in<br>2. Click on 'Create Fixed Deposit Product' button | User is redirected to the login page | high |
| TC-016 | WF-004 | Attempt to create a recurring deposit product without authentication |  | 1. Navigate to the Savings Products page without logging in<br>2. Click on 'Create Recurring Deposit Product' button | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-001 | Enter a valid Product Name with exactly 1 character |  | 1. Click on '+ Create Savings Product' button<br>2. Enter 'A' in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; the wizard proceeds to the next step. | medium |
| TC-018 (boundary) | WF-001 | Enter a valid Product Name with exactly 255 characters |  | 1. Click on '+ Create Savings Product' button<br>2. Enter a string of 255 characters in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; the wizard proceeds to the next step. | medium |
| TC-019 (boundary) | WF-001 | Enter a Product Name with 256 characters |  | 1. Click on '+ Create Savings Product' button<br>2. Enter a string of 256 characters in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Form is blocked; an error message indicates that the Product Name exceeds the maximum length. | medium |
| TC-020 (input_edge) | WF-001 | Enter a long string with special characters in the Product Name |  | 1. Click on '+ Create Savings Product' button<br>2. Enter '@#$%^&*()_+' in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; the wizard proceeds to the next step. | low |
| TC-021 (input_edge) | WF-001 | Enter a Product Name with leading and trailing whitespace |  | 1. Click on '+ Create Savings Product' button<br>2. Enter '   Product Name   ' in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces. | low |
| TC-022 (interaction_edge) | WF-001 | Rapidly navigate through the wizard steps after submission |  | 1. Click on '+ Create Savings Product' button<br>2. Fill in all required fields and click Next through all steps<br>3. After reaching the last step, click Back rapidly multiple times | User is redirected to the previous step without losing any entered data. | medium |

---

## Share Products

Total: **26** (positive: 11, negative: 7, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Share Product Creation Wizard | User logged in as <Role> | 1. Click the '+ Create Share Product' button | opens 7-step stepper wizard | high |
| TC-002 | WF-004 | Complete Step 1 - Details | User logged in as <Role>, User is in the Share Product Creation Wizard | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Enter <valid description> in the Description field<br>4. Click Next | Step 2 loaded | high |
| TC-003 | WF-005 | Complete Step 2 - Currency | User logged in as <Role>, User is in Step 2 of the Share Product Creation Wizard | 1. Enter <valid currency> in the Currency field<br>2. Enter <valid decimal places> in the Decimal Places field<br>3. Enter <valid multiples> in the Currency In Multiples Of field<br>4. Click Next | Step 3 loaded | high |
| TC-004 | WF-006 | Complete Step 3 - Terms | User logged in as <Role>, User is in Step 3 of the Share Product Creation Wizard | 1. Enter <valid total number of shares> in the Total Number of Shares field<br>2. Enter <valid shares to be issued> in the Shares to be Issued field<br>3. Enter <valid nominal unit price> in the Nominal Unit Price field<br>4. Click Next | Step 4 loaded | high |
| TC-005 | WF-007 | Complete Step 4 - Settings | User logged in as <Role>, User is in Step 4 of the Share Product Creation Wizard | 1. Check the Allow Dividends for Inactive Clients checkbox<br>2. Enter <valid minimum shares per client> in the Minimum Shares per Client field<br>3. Enter <valid maximum shares per client> in the Maximum Shares per Client field<br>4. Click Next | Step 5 loaded | high |
| TC-006 | WF-008 | Complete Step 5 - Market Price | User logged in as <Role>, User is in Step 5 of the Share Product Creation Wizard | 1. Click 'Add Row' in the Market Price section<br>2. Enter <valid from date> in the From Date field<br>3. Enter <valid share value> in the Share Value field<br>4. Click Next | Step 6 loaded | high |
| TC-007 | WF-009 | Complete Step 6 - Charges | User logged in as <Role>, User is in Step 6 of the Share Product Creation Wizard | 1. Enter <valid search term> in the Charges search field<br>2. Click Next | Step 7 loaded | high |
| TC-008 | WF-010 | Complete Step 7 - Accounting with None | User logged in as <Role>, User is in Step 7 of the Share Product Creation Wizard | 1. Select 'None' for Accounting Method<br>2. Click Finish | Share product created successfully | high |
| TC-009 | WF-011 | Complete Step 7 - Accounting with Cash-based | User logged in as <Role>, User is in Step 7 of the Share Product Creation Wizard | 1. Select 'Cash-based' for Accounting Method<br>2. Click 'Add Row' in the GL Account Mappings section<br>3. Enter <valid share reference> in the Share Reference field<br>4. Click Finish | Share product created successfully | high |
| TC-010 | WF-002 | Edit Product | User logged in as <Role>, User is on the Share Products page | 1. Click on the Product Name link for an existing product<br>2. Click the Edit button<br>3. Verify the product details are opened for editing | Product details opened for editing | medium |
| TC-011 | WF-003 | Delete Product | User logged in as <Role>, User is on the Share Products page | 1. Click on the Product Name link for an existing product<br>2. Click the Delete button<br>3. Confirm deletion | Product deleted successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Leave Product Name blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name and Description fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-013 | WF-001 | Leave Short Name blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in the Product Name and Description fields<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-014 | WF-001 | Leave Description blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in the Product Name and Short Name fields<br>3. Leave the Description field blank<br>4. Click Next | Inline validation error appears on the Description field indicating it is required | high |
| TC-015 | WF-004 | Leave Total Number of Shares blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in the Product Name, Short Name, and Description fields<br>3. Click Next<br>4. Leave the Total Number of Shares field blank<br>5. Fill in Nominal Unit Price<br>6. Click Next | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-016 | WF-004 | Leave Nominal Unit Price blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in the Product Name, Short Name, and Description fields<br>3. Click Next<br>4. Fill in Total Number of Shares<br>5. Leave the Nominal Unit Price field blank<br>6. Click Next | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-017 | WF-010 | Attempt to finish step 7 without selecting Accounting Method |  | 1. Click '+ Create Share Product' button<br>2. Fill in all required fields in steps 1 to 6<br>3. Click Next<br>4. Leave Accounting Method unselected<br>5. Click Finish | Inline validation error appears on the Accounting Method field indicating it is required | high |
| TC-018 | WF-011 | Attempt to finish step 7 with Cash-based without filling GL Account Mappings |  | 1. Click '+ Create Share Product' button<br>2. Fill in all required fields in steps 1 to 6<br>3. Click Next<br>4. Select Cash-based for Accounting Method<br>5. Leave all GL Account Mappings fields blank<br>6. Click Finish | Form does not submit; Share product is not created; error shown on GL Account Mappings fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-004 | Enter minimum allowed value for Total Number of Shares | User is on Step 3 - Terms of the wizard | 1. Enter <minimum allowed value> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Step 4 loads successfully; Total Number of Shares is set to <minimum allowed value> | medium |
| TC-020 (boundary) | WF-004 | Enter one unit below minimum for Total Number of Shares | User is on Step 3 - Terms of the wizard | 1. Enter <one unit below minimum> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Step 4 is blocked; error message displayed indicating the value is below the minimum allowed | medium |
| TC-021 (boundary) | WF-006 | Enter maximum allowed value for Nominal Unit Price | User is on Step 3 - Terms of the wizard | 1. Enter <maximum allowed value> in the Nominal Unit Price field<br>2. Fill all other required fields<br>3. Click Next | Step 4 loads successfully; Nominal Unit Price is set to <maximum allowed value> | medium |
| TC-022 (boundary) | WF-006 | Enter one unit over maximum for Nominal Unit Price | User is on Step 3 - Terms of the wizard | 1. Enter <one unit over maximum> in the Nominal Unit Price field<br>2. Fill all other required fields<br>3. Click Next | Step 4 is blocked; error message displayed indicating the value exceeds the maximum allowed | medium |
| TC-023 (boundary) | WF-008 | Add maximum allowed Market Price rows | User is on Step 5 - Market Price of the wizard | 1. Add <maximum allowed rows> to the Market Price table<br>2. Click Next | Step 6 loads successfully; all <maximum allowed rows> are displayed in the Market Price table | medium |
| TC-024 (boundary) | WF-008 | Attempt to add one more Market Price row beyond maximum | User is on Step 5 - Market Price of the wizard | 1. Add <maximum allowed rows> to the Market Price table<br>2. Attempt to add one more row<br>3. Click Next | Step 6 is blocked; error message displayed indicating the maximum number of rows has been reached | medium |
| TC-025 (interaction_edge) | WF-011 | Select Cash-based and fill GL account mappings | User is on Step 7 - Accounting of the wizard | 1. Select Cash-based for Accounting Method<br>2. Fill all GL account mapping fields with valid data<br>3. Click Finish | Share product created successfully; all GL account mappings are saved | medium |
| TC-026 (interaction_edge) | WF-011 | Select None and complete the wizard | User is on Step 7 - Accounting of the wizard | 1. Select None for Accounting Method<br>2. Click Finish | Share product created successfully; no GL account mappings are required | medium |

---

## Charges

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new charge successfully | User logged in as <Role> | 1. Click the '+ Create Charge' button<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Enter <Currency> in the Currency field<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <Amount> in the Amount field<br>8. Click Submit | A success notification is displayed; the charge definition is created and visible in the Charges table | high |
| TC-002 | WF-002 | Edit an existing charge successfully | User logged in as <Role>, At least one charge exists in the Charges table | 1. Click the Edit action on an existing charge<br>2. Modify <Charge Name> in the Charge Name field<br>3. Click Submit | A success notification is displayed; the charge definition is updated and visible in the Charges table | medium |
| TC-003 | WF-003 | Delete an existing charge successfully | User logged in as <Role>, At least one charge exists in the Charges table | 1. Click the Delete action on an existing charge<br>2. Confirm the deletion | The charge is deleted; it no longer appears in the Charges table | medium |

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
| TC-009 (boundary) | WF-001 | Enter minimum valid Charge Name |  | 1. Click the '+ Create Charge' button<br>2. Enter minimum allowed value in the Charge Name field<br>3. Select 'Loan' in the Charge Applies To dropdown<br>4. Enter valid Currency<br>5. Select a Charge Time Type<br>6. Select a Charge Calculation Type<br>7. Enter minimum allowed value in the Amount field<br>8. Click Submit | Form submits successfully; charge definition is created with the minimum Charge Name | medium |
| TC-010 (boundary) | WF-001 | Enter maximum allowed value in Amount field |  | 1. Click the '+ Create Charge' button<br>2. Enter valid Charge Name<br>3. Select 'Loan' in the Charge Applies To dropdown<br>4. Enter valid Currency<br>5. Select a Charge Time Type<br>6. Select a Charge Calculation Type<br>7. Enter maximum allowed value in the Amount field<br>8. Click Submit | Form submits successfully; charge definition is created with the maximum Amount | medium |
| TC-011 (boundary) | WF-001 | Enter one unit below minimum Amount |  | 1. Click the '+ Create Charge' button<br>2. Enter valid Charge Name<br>3. Select 'Loan' in the Charge Applies To dropdown<br>4. Enter valid Currency<br>5. Select a Charge Time Type<br>6. Select a Charge Calculation Type<br>7. Enter one unit below minimum value in the Amount field<br>8. Click Submit | Submission is blocked; inline error shown indicating the Amount is below the minimum allowed | medium |
| TC-012 (input_edge) | WF-001 | Enter a very long Charge Name |  | 1. Click the '+ Create Charge' button<br>2. Enter a string longer than 200 characters in the Charge Name field<br>3. Select 'Loan' in the Charge Applies To dropdown<br>4. Enter valid Currency<br>5. Select a Charge Time Type<br>6. Select a Charge Calculation Type<br>7. Enter valid value in the Amount field<br>8. Click Submit | Form submits successfully; Charge Name is either accepted or truncated with a visible indicator | low |
| TC-013 (input_edge) | WF-001 | Enter Charge Name with special characters |  | 1. Click the '+ Create Charge' button<br>2. Enter special characters in the Charge Name field<br>3. Select 'Loan' in the Charge Applies To dropdown<br>4. Enter valid Currency<br>5. Select a Charge Time Type<br>6. Select a Charge Calculation Type<br>7. Enter valid value in the Amount field<br>8. Click Submit | Form submits successfully; Charge Name with special characters is accepted | low |

---

## Floating Rates

Total: **15** (positive: 3, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form for Floating Rate | User logged in as <Role> | 1. Click the '+ Create Floating Rate' button | The creation form is opened | high |
| TC-002 | WF-001 | Create a new Floating Rate with valid data | User logged in as <Role>, Creation form is open | 1. Enter <Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Click 'Add Row' in the Rate Periods table<br>4. Enter <From Date> in the From Date field of the new row<br>5. Enter <Interest Rate> in the Interest Rate field of the new row<br>6. Click Save | The new floating rate is displayed in the Floating Rates table | high |
| TC-003 | WF-002 | Edit an existing Floating Rate | User logged in as <Role>, Floating Rates table is displayed | 1. Click on the Floating Rate Name link of an existing floating rate<br>2. Click the Edit button | Edit mode activated for the selected floating rate | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Floating Rate Name blank and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-005 | WF-001 | Submit the form with all required fields empty |  | 1. Click on the '+ Create Floating Rate' button<br>2. Leave all fields empty<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-006 | WF-001 | Select multiple base lending rates and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Check the Is Base Lending Rate checkbox<br>4. Check another Is Base Lending Rate checkbox in a different row<br>5. Click Submit | Inline validation error appears indicating 'only one base rate can exist at a time' | medium |
| TC-007 | WF-001 | Leave the From Date blank in Rate Periods and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Add a Rate Period<br>4. Leave the From Date field blank<br>5. Click Submit | Inline validation error appears on the From Date field indicating it is required | high |
| TC-008 | WF-001 | Enter a non-numeric value in the Interest Rate field |  | 1. Click on the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name<br>3. Add a Rate Period<br>4. Enter <non-numeric value> in the Interest Rate field<br>5. Click Submit | Inline validation error appears on the Interest Rate field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Add maximum allowed entries to Rate Periods | User is on the Create Floating Rate form | 1. Add the maximum allowed entries to the Rate Periods table | Form submits successfully; all entries are saved in the Rate Periods table | medium |
| TC-010 (boundary) | WF-001 | Attempt to add one more entry to Rate Periods | User is on the Create Floating Rate form with maximum entries in Rate Periods | 1. Attempt to add one more entry to the Rate Periods table | Adding the entry is blocked; a visible error is shown indicating the maximum limit has been reached | medium |
| TC-011 (boundary) | WF-001 | Enter today's date in From Date field | User is on the Create Floating Rate form | 1. Enter today's date in the From Date field of a Rate Period<br>2. Fill in the Interest Rate field<br>3. Click Submit | Form submits successfully; the Rate Period entry is saved with today's date | medium |
| TC-012 (boundary) | WF-001 | Enter yesterday's date in From Date field | User is on the Create Floating Rate form | 1. Enter yesterday's date in the From Date field of a Rate Period<br>2. Fill in the Interest Rate field<br>3. Click Submit | Form submits successfully; the Rate Period entry is saved with yesterday's date | medium |
| TC-013 (input_edge) | WF-001 | Enter a very long Floating Rate Name | User is on the Create Floating Rate form | 1. Enter a string longer than 200 characters in the Floating Rate Name field | The input is either accepted or truncated with a visible indicator | low |
| TC-014 (input_edge) | WF-001 | Enter special characters in Floating Rate Name | User is on the Create Floating Rate form | 1. Enter special characters (e.g., !@#$%^&*) in the Floating Rate Name field | The input is accepted or an error is shown indicating invalid characters | low |
| TC-015 (input_edge) | WF-001 | Enter leading and trailing whitespace in Floating Rate Name | User is on the Create Floating Rate form | 1. Enter '  Test Rate  ' (with spaces) in the Floating Rate Name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Delinquency Management

Total: **16** (positive: 5, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a Delinquency Range without Maximum Age Days | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <valid classification> in the Classification field<br>4. Enter <valid minimum age days> in the Minimum Age Days field<br>5. Click Submit | Delinquency range created; success message shown | high |
| TC-002 | WF-002 | Create a Delinquency Range with Maximum Age Days | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <valid classification> in the Classification field<br>4. Enter <valid minimum age days> in the Minimum Age Days field<br>5. Enter <valid maximum age days> in the Maximum Age Days field<br>6. Click Submit | Delinquency range created; success message shown | high |
| TC-003 | WF-003 | View Delinquency Range Classification | User logged in as <Role>, At least one delinquency range exists | 1. Navigate to the Delinquency Ranges page<br>2. Click on the Classification link for a delinquency range | Navigated to Delinquency Range details | medium |
| TC-004 | WF-004 | Create a Delinquency Bucket | User logged in as <Role> | 1. Navigate to the Delinquency Buckets page<br>2. Click on 'Create Delinquency Bucket'<br>3. Enter <valid bucket name> in the Bucket Name field<br>4. Click 'Add Range' to add a delinquency range<br>5. Enter <valid range name> in the Range Name field<br>6. Enter <valid days> in the Days field<br>7. Click Submit | Delinquency bucket created; success message shown | high |
| TC-005 | WF-005 | View Delinquency Bucket Name | User logged in as <Role>, At least one delinquency bucket exists | 1. Navigate to the Delinquency Buckets page<br>2. Click on the Bucket Name link for a delinquency bucket | Navigated to Delinquency Bucket details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Classification field blank |  | 1. Open the Create Delinquency Range form<br>2. Leave the Classification field blank<br>3. Fill in the Minimum Age Days field with a valid number<br>4. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-007 |  | Leave the Minimum Age Days field blank |  | 1. Open the Create Delinquency Range form<br>2. Leave the Minimum Age Days field blank<br>3. Fill in the Classification field with a valid value<br>4. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-008 |  | Leave the Bucket Name field blank |  | 1. Open the Create Delinquency Bucket form<br>2. Leave the Bucket Name field blank<br>3. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-009 |  | Leave the Range Name field blank in Delinquency Ranges |  | 1. Open the Create Delinquency Bucket form<br>2. Add a delinquency range<br>3. Leave the Range Name field blank<br>4. Fill in the Days field with a valid value<br>5. Click Submit | Inline validation error appears on the Range Name field indicating it is required | high |
| TC-010 |  | Leave the Days field blank in Delinquency Ranges |  | 1. Open the Create Delinquency Bucket form<br>2. Add a delinquency range<br>3. Fill in the Range Name field with a valid value<br>4. Leave the Days field blank<br>5. Click Submit | Inline validation error appears on the Days field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Minimum Age Days at minimum value |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field<br>3. Click Submit | Form submits successfully; delinquency range created with Minimum Age Days set to <minimum allowed value> | medium |
| TC-012 (boundary) | WF-001 | Minimum Age Days below minimum value |  | 1. Enter <one unit below minimum> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field<br>3. Click Submit | <Minimum_Age_Days> displays an error indicating the value is below the minimum allowed | medium |
| TC-013 (boundary) | WF-002 | Maximum Age Days at boundary |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Enter <maximum allowed value> in the <Maximum_Age_Days> field<br>3. Fill in the <Classification> field<br>4. Click Submit | Form submits successfully; delinquency range created with Maximum Age Days set to <maximum allowed value> | medium |
| TC-014 (boundary) | WF-002 | Maximum Age Days above boundary |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Enter <one unit above maximum> in the <Maximum_Age_Days> field<br>3. Fill in the <Classification> field<br>4. Click Submit | <Maximum_Age_Days> displays an error indicating the value exceeds the maximum allowed | medium |
| TC-015 (boundary) | WF-004 | Repeating group maximum entries |  | 1. Add <maximum allowed entries> rows to the <Delinquency_Ranges> repeating group<br>2. Fill in the <Bucket_Name> field<br>3. Click Submit | Form submits successfully; delinquency bucket created with <maximum allowed entries> ranges | medium |
| TC-016 (boundary) | WF-004 | Repeating group exceeding maximum entries |  | 1. Add <maximum allowed entries + 1> rows to the <Delinquency_Ranges> repeating group<br>2. Fill in the <Bucket_Name> field<br>3. Click Submit | Form is blocked; visible error shown indicating the maximum number of entries has been exceeded | medium |

---

## Loan Account

Total: **33** (positive: 8, negative: 18, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application with valid details | User logged in as <Client>, Loan Application form is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On date field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number of repayments> in the Number of Repayments field<br>9. Select <frequency> from the Repaid Every dropdown<br>10. Select <unit> from the Repaid Every dropdown<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Click Submit | Loan is created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Loan Application | User logged in as <Loan Officer>, Loan application is in Pending Approval status | 1. Click Approve<br>2. Enter <valid date> in the Approved On Date field<br>3. Enter <valid approved amount> in the Approved Amount field<br>4. Enter <valid date> in the Expected Disbursement Date field<br>5. Click Submit on the approval dialog | Loan application is approved | high |
| TC-003 | WF-003 | Reject Loan Application | User logged in as <Loan Officer>, Loan application is in Pending Approval status | 1. Click Reject<br>2. Confirm rejection | Loan application is rejected | medium |
| TC-004 | WF-004 | Withdraw Loan Application | User logged in as <Client>, Loan application is in Pending Approval status | 1. Click Withdraw<br>2. Confirm withdrawal | Loan application is withdrawn | medium |
| TC-005 | WF-006 | Disburse Loan | User logged in as <Loan Officer>, Loan application is in Approved status | 1. Click Disburse<br>2. Enter <valid date> in the Disbursed On Date field<br>3. Enter <valid transaction amount> in the Transaction Amount field<br>4. Select <Payment Type> from the dropdown<br>5. Click Submit | Loan is disbursed | high |
| TC-006 | WF-008 | Make Repayment | User logged in as <Client>, Loan application is Active | 1. Click Make Repayment<br>2. Enter <valid date> in the Transaction Date field<br>3. Verify Transaction Amount is pre-filled with amount due<br>4. Select <Payment Type> from the dropdown<br>5. Click Submit | Repayment is made | high |
| TC-007 | WF-009 | Waive Interest on Active Loan | User logged in as <Loan Officer>, Loan application is Active | 1. Click Waive Interest<br>2. Confirm interest waiver | Interest is waived | medium |
| TC-008 | WF-011 | Close Loan | User logged in as <Loan Officer>, Loan application is Active | 1. Click Close<br>2. Confirm closure | Loan is closed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-010 |  | Leave the Loan Officer field blank and submit |  | 1. Leave the Loan Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-011 |  | Leave the Loan Purpose field blank and submit |  | 1. Leave the Loan Purpose field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Purpose field indicating it is required | high |
| TC-012 |  | Leave the Fund field blank and submit |  | 1. Leave the Fund field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fund field indicating it is required | high |
| TC-013 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-014 |  | Leave the Expected Disbursement Date blank and submit |  | 1. Leave the Expected Disbursement Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it is required | high |
| TC-015 |  | Leave the Principal field blank and submit |  | 1. Leave the Principal field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is required | high |
| TC-016 |  | Leave the Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-017 |  | Leave the Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-018 |  | Leave the Interest Rate field blank and submit |  | 1. Leave the Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-019 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; error shown on all required fields | high |
| TC-020 |  | Submit with Principal below minimum bound |  | 1. Enter <amount below minimum> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it must be within product min/max | medium |
| TC-021 |  | Submit with Interest Rate above maximum bound |  | 1. Enter <amount exceeding maximum> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it must be within product min/max | medium |
| TC-022 | WF-001 | Attempt to submit loan application without selecting a product |  | 1. Leave the Product Name dropdown blank<br>2. Click Submit | Form does not submit; error shown on Product Name field | high |
| TC-023 | WF-002 | Attempt to approve loan application when status is not Pending Approval |  | 1. Attempt to approve loan application while in Approved state<br>2. Click Approve | Status remains Approved; no transition occurs | high |
| TC-024 | WF-003 | Attempt to reject loan application when status is not Pending Approval |  | 1. Attempt to reject loan application while in Approved state<br>2. Click Reject | Status remains Approved; no transition occurs | high |
| TC-025 | WF-004 | Attempt to withdraw loan application when status is not Pending Approval |  | 1. Attempt to withdraw loan application while in Approved state<br>2. Click Withdraw | Status remains Approved; no transition occurs | high |
| TC-026 | WF-005 | Attempt to delete loan application when status is not Pending Approval |  | 1. Attempt to delete loan application while in Approved state<br>2. Click Delete | Status remains Approved; no transition occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 (boundary) | WF-001 | Submit Loan Application with Principal at minimum value | User is on the Loan Application wizard, Step 1. | 1. Select a Product Name from the dropdown.<br>2. Enter a Loan Officer.<br>3. Enter a Loan Purpose.<br>4. Enter a Fund.<br>5. Enter today's date in the Submitted On field.<br>6. Enter today's date in the Expected Disbursement Date field.<br>7. Enter the minimum allowed Principal amount.<br>8. Enter a valid Number of Repayments.<br>9. Select a Repaid Every frequency and unit.<br>10. Enter the minimum allowed Interest Rate.<br>11. Click Submit. | Form submits successfully; loan is created in Submitted and Pending Approval status. | medium |
| TC-028 (boundary) | WF-001 | Submit Loan Application with Principal just below minimum value | User is on the Loan Application wizard, Step 1. | 1. Select a Product Name from the dropdown.<br>2. Enter a Loan Officer.<br>3. Enter a Loan Purpose.<br>4. Enter a Fund.<br>5. Enter today's date in the Submitted On field.<br>6. Enter today's date in the Expected Disbursement Date field.<br>7. Enter the minimum allowed Principal amount minus one.<br>8. Enter a valid Number of Repayments.<br>9. Select a Repaid Every frequency and unit.<br>10. Enter the minimum allowed Interest Rate.<br>11. Click Submit. | Form submission is blocked; error displayed indicating the Principal amount is below the minimum allowed. | medium |
| TC-029 (boundary) | WF-001 | Submit Loan Application with Interest Rate at maximum value | User is on the Loan Application wizard, Step 1. | 1. Select a Product Name from the dropdown.<br>2. Enter a Loan Officer.<br>3. Enter a Loan Purpose.<br>4. Enter a Fund.<br>5. Enter today's date in the Submitted On field.<br>6. Enter today's date in the Expected Disbursement Date field.<br>7. Enter a valid Principal amount.<br>8. Enter a valid Number of Repayments.<br>9. Select a Repaid Every frequency and unit.<br>10. Enter the maximum allowed Interest Rate.<br>11. Click Submit. | Form submits successfully; loan is created in Submitted and Pending Approval status. | medium |
| TC-030 (boundary) | WF-001 | Submit Loan Application with Interest Rate just above maximum value | User is on the Loan Application wizard, Step 1. | 1. Select a Product Name from the dropdown.<br>2. Enter a Loan Officer.<br>3. Enter a Loan Purpose.<br>4. Enter a Fund.<br>5. Enter today's date in the Submitted On field.<br>6. Enter today's date in the Expected Disbursement Date field.<br>7. Enter a valid Principal amount.<br>8. Enter a valid Number of Repayments.<br>9. Select a Repaid Every frequency and unit.<br>10. Enter the maximum allowed Interest Rate plus one.<br>11. Click Submit. | Form submission is blocked; error displayed indicating the Interest Rate exceeds the maximum allowed. | medium |
| TC-031 (state_edge) | WF-002 | Rapid approval of loan application | Loan application is in Pending Approval status. | 1. Click Approve.<br>2. Fill in the Approved On Date, Approved Amount, and Expected Disbursement Date.<br>3. Click Submit.<br>4. Immediately click Approve again. | Second approval attempt is blocked; only one approval is processed. | medium |
| TC-032 (state_edge) | WF-008 | Make repayment with Transaction Amount at due amount | Loan is in Active status. | 1. Click Make Repayment.<br>2. Enter today's date in the Transaction Date field.<br>3. Enter the amount due in the Transaction Amount field.<br>4. Select a Payment Type.<br>5. Click Submit. | Repayment is processed successfully; loan status updates if fully settled. | medium |
| TC-033 (state_edge) | WF-008 | Make repayment with Transaction Amount exceeding due amount | Loan is in Active status. | 1. Click Make Repayment.<br>2. Enter today's date in the Transaction Date field.<br>3. Enter an amount greater than the due amount in the Transaction Amount field.<br>4. Select a Payment Type.<br>5. Click Submit. | Repayment is processed successfully; loan status updates to Closed if fully settled. | medium |

---

## Savings Account

Total: **29** (positive: 14, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Savings Account Creation Form | User logged in as <Role> | 1. Navigate to the Savings Account Creation Form<br>2. Select <Product Name> from the Product Name dropdown<br>3. Enter <Field Officer> in the Field Officer field<br>4. Enter <date> in the Submitted On field<br>5. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>6. Select <Interest Compounding Period> from the Interest Compounding Period dropdown<br>7. Select <Interest Posting Period> from the Interest Posting Period dropdown<br>8. Select <Interest Calculated Using> from the Interest Calculated Using dropdown<br>9. Select <Days in Year> from the Days in Year dropdown<br>10. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>11. Enter <Lock-in Period> in the Lock-in Period field<br>12. Check the Allow Overdraft checkbox if applicable<br>13. Click 'Add Row' in the Charges section<br>14. Enter <Charge Description> in the Charge Description field<br>15. Enter <Charge Amount> in the Charge Amount field<br>16. Click 'Submit' | Account is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-002 | Approve Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Approve on the Savings Account Detail page | Account is approved | high |
| TC-003 | WF-003 | Reject Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Reject on the Savings Account Detail page | Account is rejected | high |
| TC-004 | WF-004 | Withdraw Application for Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Withdraw Application on the Savings Account Detail page | Application is withdrawn | high |
| TC-005 | WF-005 | Activate Approved Savings Account | User logged in as <Role>, Account is in Approved status | 1. Click Activate on the Savings Account Detail page | Account is activated | high |
| TC-006 | WF-006 | Undo Approval for Approved Savings Account | User logged in as <Role>, Account is in Approved status | 1. Click Undo Approval on the Savings Account Detail page | Approval is undone | high |
| TC-007 | WF-007 | Deposit into Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Deposit on the Savings Account Detail page<br>2. Enter <date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Enter <Payment Details> in the Payment Details field<br>6. Click Submit | Account is credited | high |
| TC-008 | WF-008 | Withdraw from Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Withdraw on the Savings Account Detail page<br>2. Enter <date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Enter <Payment Details> in the Payment Details field<br>6. Click Submit | Account is debited | high |
| TC-009 | WF-009 | Post Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Post Interest on the Savings Account Detail page | Interest is posted | high |
| TC-010 | WF-010 | Calculate Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Calculate Interest on the Savings Account Detail page | Interest is calculated | high |
| TC-011 | WF-011 | Close Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Close on the Savings Account Detail page | Account is closed | high |
| TC-012 | WF-012 | Block Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Account on the Savings Account Detail page | Account is blocked | high |
| TC-013 | WF-013 | Block Debit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Debit on the Savings Account Detail page | Debit is blocked | high |
| TC-014 | WF-014 | Block Credit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Credit on the Savings Account Detail page | Credit is blocked | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 | WF-001 | Submit Savings Account Creation Form with all fields empty |  | 1. Leave the Product Name dropdown blank<br>2. Leave the Field Officer field blank<br>3. Leave the Submitted On date blank<br>4. Leave the Nominal Annual Interest Rate field blank<br>5. Leave the Interest Compounding Period dropdown blank<br>6. Leave the Interest Posting Period dropdown blank<br>7. Leave the Interest Calculated Using dropdown blank<br>8. Leave the Days in Year dropdown blank<br>9. Leave the Minimum Opening Balance field blank<br>10. Leave the Lock-in Period field blank<br>11. Leave the Allow Overdraft checkbox unchecked<br>12. Leave the Charges section empty<br>13. Click Submit | Form does not submit; error shown on all required fields | high |
| TC-016 | WF-008 | Withdraw from Active Savings Account exceeding available balance without overdraft enabled | Account is in Active state, Available balance is <amount> | 1. Click Withdraw<br>2. Enter <Transaction_Date> in the Transaction Date field<br>3. Enter <amount exceeding available balance> in the Transaction Amount field<br>4. Click Submit | Form does not submit; error shown indicating withdrawal cannot exceed available balance unless overdraft is enabled | high |
| TC-017 | WF-008 | Withdraw from Active Savings Account breaching minimum balance | Account is in Active state, Minimum balance is enforced, Available balance is <amount>, Withdrawal amount would breach minimum balance | 1. Click Withdraw<br>2. Enter <Transaction_Date> in the Transaction Date field<br>3. Enter <amount breaching minimum balance> in the Transaction Amount field<br>4. Click Submit | Form does not submit; error shown indicating minimum balance must be enforced | high |
| TC-018 | WF-002 | Approve Pending Savings Account when account is not in Pending state | Account is in Approved state | 1. Click Approve | Action is blocked; no approval occurs | high |
| TC-019 | WF-003 | Reject Pending Savings Account when account is not in Pending state | Account is in Approved state | 1. Click Reject | Action is blocked; no rejection occurs | high |
| TC-020 | WF-004 | Withdraw Application for Pending Savings Account when account is not in Pending state | Account is in Approved state | 1. Click Withdraw Application | Action is blocked; no withdrawal occurs | high |
| TC-021 | WF-005 | Activate Approved Savings Account when account is not in Approved state | Account is in Active state | 1. Click Activate | Action is blocked; no activation occurs | high |
| TC-022 | WF-006 | Undo Approval for Approved Savings Account when account is not in Approved state | Account is in Active state | 1. Click Undo Approval | Action is blocked; no undo occurs | high |
| TC-023 | WF-011 | Close Active Savings Account when account is not in Active state | Account is in Approved state | 1. Click Close | Action is blocked; no closure occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 (boundary) | WF-001 | Submit Savings Account Creation Form with minimum opening balance |  | 1. Select a product from the Product Name dropdown<br>2. Fill in the Field Officer field<br>3. Enter today's date in the Submitted On field<br>4. Enter the minimum opening balance in the Minimum Opening Balance field<br>5. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-025 (boundary) | WF-001 | Submit Savings Account Creation Form with opening balance below minimum |  | 1. Select a product from the Product Name dropdown<br>2. Fill in the Field Officer field<br>3. Enter today's date in the Submitted On field<br>4. Enter an amount below the minimum opening balance in the Minimum Opening Balance field<br>5. Click Submit | Submission is blocked; an error message indicates the opening balance is below the minimum required | medium |
| TC-026 (boundary) | WF-008 | Withdraw from Active Savings Account exceeding available balance without overdraft | Account is in Active status and has a balance of $100 | 1. Click Withdraw on the Active account<br>2. Enter today's date in the Transaction Date field<br>3. Enter $150 in the Transaction Amount field<br>4. Click Submit | Submission is blocked; an error message indicates the withdrawal exceeds available balance and overdraft is not enabled | medium |
| TC-027 (boundary) | WF-008 | Withdraw from Active Savings Account breaching minimum balance | Account is in Active status with a balance of $100 and minimum balance enforced at $50 | 1. Click Withdraw on the Active account<br>2. Enter today's date in the Transaction Date field<br>3. Enter $60 in the Transaction Amount field<br>4. Click Submit | Submission is blocked; an error message indicates the withdrawal would breach the minimum balance requirement | medium |
| TC-028 (input_edge) |  | Enter long text in the Field Officer field |  | 1. Select a product from the Product Name dropdown<br>2. Enter a very long string (over 200 characters) in the Field Officer field<br>3. Click Submit | Submission is blocked; an error message indicates the input exceeds the maximum allowed length | low |
| TC-029 (input_edge) |  | Enter special characters in the Charge Description field |  | 1. Select a product from the Product Name dropdown<br>2. Click to add a new charge in the Charges section<br>3. Enter special characters in the Charge Description field<br>4. Click Submit | Submission is blocked; an error message indicates invalid characters in the Charge Description field | low |

---

## Share Account

Total: **24** (positive: 8, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application with valid data | User logged in as <Role>, Client has active savings accounts | 1. Select <valid share product> from the Share Product dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid number of shares within bounds> in the Requested Shares field<br>4. Enter <valid date> in the Application Date field<br>5. Select <active savings account> from the Savings Account for Charges dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Share Account with valid data | User logged in as <Role>, Share Account is in Pending status | 1. Enter <valid number of approved shares> in the Approved Shares field<br>2. Enter <valid date> in the Approved Date field<br>3. Click Approve | Approval process completed | high |
| TC-003 | WF-003 | Reject Share Account | User logged in as <Role>, Share Account is in Pending status | 1. Click Reject | Rejection process completed | high |
| TC-004 | WF-004 | Activate Share Account | User logged in as <Role>, Share Account is in Approved status | 1. Click Activate | Account activated | high |
| TC-005 | WF-005 | Undo Approval of Share Account | User logged in as <Role>, Share Account is in Approved status | 1. Click Undo Approval | Approval undone | high |
| TC-006 | WF-006 | Apply Additional Shares to Share Account | User logged in as <Role>, Share Account is in Active status | 1. Click Apply Additional Shares<br>2. Enter <valid number of additional shares> in the field<br>3. Click Submit | Additional shares applied | high |
| TC-007 | WF-007 | Redeem Shares from Share Account | User logged in as <Role>, Share Account is in Active status | 1. Click Redeem Shares | Redemption amount calculated as shares multiplied by current unit price and credited to the linked savings account | high |
| TC-008 | WF-008 | Close Share Account | User logged in as <Role>, Share Account is in Active status | 1. Click Close | Account closed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-010 | WF-001 | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 | WF-001 | Leave the Requested Shares blank and submit |  | 1. Leave the Requested Shares blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-012 | WF-001 | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-013 | WF-001 | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-014 | WF-002 | Attempt to approve a share account without filling Approved Shares and Approved Date | entity_state == Pending | 1. Click Approve<br>2. Leave the Approved Shares blank<br>3. Leave the Approved Date blank<br>4. Click Submit | Inline validation error appears on the Approved Shares field indicating it is required; Inline validation error appears on the Approved Date field indicating it is required | high |
| TC-015 | WF-002 | Attempt to approve a share account with Approved Shares exceeding the maximum limit | entity_state == Pending | 1. Click Approve<br>2. Enter <amount exceeding maximum limit> in the Approved Shares field<br>3. Enter a valid date in the Approved Date field<br>4. Click Submit | Form does not submit; Approved Shares is highlighted; error shown on Approved Shares field indicating it must be within the product min/max | medium |
| TC-016 | WF-004 | Attempt to activate a share account while in Pending state | entity_state == Pending | 1. Click Activate | Form does not submit; no action is taken; error shown indicating activation is not allowed while in Pending state | high |
| TC-017 | WF-006 | Attempt to apply additional shares while in Pending state | entity_state == Pending | 1. Click Apply Additional Shares | Form does not submit; no action is taken; error shown indicating additional shares cannot be applied while in Pending state | high |
| TC-018 | WF-007 | Attempt to redeem shares while in Pending state | entity_state == Pending | 1. Click Redeem Shares | Form does not submit; no action is taken; error shown indicating shares cannot be redeemed while in Pending state | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-001 | Submit application with requested shares at minimum allowed value | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Enter today's date in the Submitted On field<br>3. Enter the minimum allowed value in the Requested Shares field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | medium |
| TC-020 (boundary) | WF-001 | Submit application with requested shares exceeding maximum allowed value | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Enter today's date in the Submitted On field<br>3. Enter a value greater than the maximum allowed in the Requested Shares field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Submission is blocked; error message displayed indicating requested shares exceed maximum allowed | medium |
| TC-021 (state_edge) | WF-002 | Rapidly approve a pending share account application | User is on the Share Account Detail page with a Pending status | 1. Click Approve<br>2. Enter the approved shares value in the Approved Shares field<br>3. Enter today's date in the Approved Date field<br>4. Click Approve again immediately after the first approval | Second approval attempt is blocked; only one approval is processed | medium |
| TC-022 (state_edge) | WF-007 | Redeem shares with maximum shares allowed | User is on the Share Account Detail page with Active status | 1. Click Redeem Shares<br>2. Enter the maximum shares allowed for redemption<br>3. Click Redeem Shares | Redemption amount is calculated and credited to the linked savings account | medium |
| TC-023 (input_edge) |  | Enter a very long External ID | User is on the Share Account Application form | 1. Enter a string longer than 200 characters in the External ID field | Field accepts the input or shows an error indicating the limit | low |
| TC-024 (input_edge) |  | Enter special characters in the External ID field | User is on the Share Account Application form | 1. Enter special characters in the External ID field | Input is accepted or shows a specific error message | low |

---

## Fixed & Recurring Deposit Accounts

Total: **28** (positive: 11, negative: 10, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Fixed Deposit Account with valid details | User logged in as <Role> | 1. Navigate to the FD Account Creation Form<br>2. Select <Fixed Deposit Product> from the Fixed Deposit Product dropdown<br>3. Enter <valid deposit amount> in the Deposit Amount field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <Deposit Period Unit> from the Deposit Period Unit dropdown<br>6. Select <Maturity Instructions> from the Maturity Instructions dropdown<br>7. Click Submit | Fixed Deposit account created successfully | high |
| TC-002 | WF-002 | Create Recurring Deposit Account with valid details | User logged in as <Role> | 1. Navigate to the RD Account Creation Form<br>2. Select <Recurring Deposit Product> from the Recurring Deposit Product dropdown<br>3. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <Deposit Frequency> from the Deposit Frequency dropdown<br>6. Enter <valid date> in the Expected First Deposit On field<br>7. Click Submit | Recurring Deposit account created successfully | high |
| TC-003 | WF-003 | Approve Fixed Deposit Account | User logged in as <Role>, FD Account is created and pending approval | 1. Navigate to the FD Account Detail Page<br>2. Click Approve | Fixed Deposit account approved | medium |
| TC-004 | WF-004 | Activate Fixed Deposit Account | User logged in as <Role>, FD Account is approved | 1. Navigate to the FD Account Detail Page<br>2. Click Activate | Fixed Deposit account activated | medium |
| TC-005 | WF-005 | Premature Close Fixed Deposit Account | User logged in as <Role>, FD Account is active | 1. Navigate to the FD Account Detail Page<br>2. Click Premature Close | Fixed Deposit account closed prematurely | medium |
| TC-006 | WF-006 | Close Fixed Deposit Account on Maturity | User logged in as <Role>, FD Account is matured | 1. Navigate to the FD Account Detail Page<br>2. Click Close on Maturity | Fixed Deposit account closed on maturity | medium |
| TC-007 | WF-007 | Approve Recurring Deposit Account | User logged in as <Role>, RD Account is created and pending approval | 1. Navigate to the RD Account Detail Page<br>2. Click Approve | Recurring Deposit account approved | medium |
| TC-008 | WF-008 | Activate Recurring Deposit Account | User logged in as <Role>, RD Account is approved | 1. Navigate to the RD Account Detail Page<br>2. Click Activate | Recurring Deposit account activated | medium |
| TC-009 | WF-009 | Deposit into Recurring Deposit Account | User logged in as <Role>, RD Account is active | 1. Navigate to the RD Account Detail Page<br>2. Click Deposit | Deposit made into Recurring Deposit account | medium |
| TC-010 | WF-010 | Premature Close Recurring Deposit Account | User logged in as <Role>, RD Account is active | 1. Navigate to the RD Account Detail Page<br>2. Click Premature Close | Recurring Deposit account closed prematurely | medium |
| TC-011 | WF-011 | Close Recurring Deposit Account on Maturity | User logged in as <Role>, RD Account is matured | 1. Navigate to the RD Account Detail Page<br>2. Click Close on Maturity | Recurring Deposit account closed on maturity | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Leave the Deposit Amount blank and submit |  | 1. Leave the Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-013 | WF-001 | Leave the Deposit Period blank and submit |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-014 | WF-002 | Leave the Mandatory Deposit Amount blank and submit |  | 1. Leave the Mandatory Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mandatory Deposit Amount field indicating it is required | high |
| TC-015 | WF-002 | Leave the Expected First Deposit On date blank and submit |  | 1. Leave the Expected First Deposit On field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected First Deposit On field indicating it is required | high |
| TC-016 | WF-003 | Attempt to approve a Fixed Deposit account without meeting preconditions |  | 1. Click Approve on the Fixed Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |
| TC-017 | WF-007 | Attempt to approve a Recurring Deposit account without meeting preconditions |  | 1. Click Approve on the Recurring Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |
| TC-018 | WF-005 | Attempt to prematurely close a Fixed Deposit account when it is not eligible |  | 1. Click Premature Close on the Fixed Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |
| TC-019 | WF-010 | Attempt to prematurely close a Recurring Deposit account when it is not eligible |  | 1. Click Premature Close on the Recurring Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |
| TC-020 | WF-006 | Attempt to close a Fixed Deposit account on maturity when it is not eligible |  | 1. Click Close on Maturity on the Fixed Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |
| TC-021 | WF-011 | Attempt to close a Recurring Deposit account on maturity when it is not eligible |  | 1. Click Close on Maturity on the Recurring Deposit Account Detail page | Status remains unchanged; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (boundary) | WF-001 | Test minimum valid Deposit Amount for Fixed Deposit |  | 1. Enter <minimum allowed value> in the <Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Fixed Deposit account is created with the <minimum allowed value> | medium |
| TC-023 (boundary) | WF-001 | Test Deposit Amount below minimum for Fixed Deposit |  | 1. Enter <one unit below minimum> in the <Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | <Deposit_Amount> displays an error indicating the value is below the minimum allowed | medium |
| TC-024 (boundary) | WF-002 | Test minimum valid Mandatory Deposit Amount for Recurring Deposit |  | 1. Enter <minimum allowed value> in the <Mandatory_Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Recurring Deposit account is created with the <minimum allowed value> | medium |
| TC-025 (boundary) | WF-002 | Test Mandatory Deposit Amount below minimum for Recurring Deposit |  | 1. Enter <one unit below minimum> in the <Mandatory_Deposit_Amount> field<br>2. Fill all other required fields<br>3. Click Submit | <Mandatory_Deposit_Amount> displays an error indicating the value is below the minimum allowed | medium |
| TC-026 (data_edge) | WF-002 | Test Expected First Deposit On date with today's date |  | 1. Enter today's date in the <Expected_First_Deposit_On> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Recurring Deposit account is created with today's date as the first deposit date | medium |
| TC-027 (data_edge) | WF-002 | Test Expected First Deposit On date with yesterday's date |  | 1. Enter yesterday's date in the <Expected_First_Deposit_On> field<br>2. Fill all other required fields<br>3. Click Submit | <Expected_First_Deposit_On> displays an error indicating the date cannot be in the past | medium |
| TC-028 (data_edge) | WF-002 | Test Expected First Deposit On date with a far future date |  | 1. Enter a far future date in the <Expected_First_Deposit_On> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Recurring Deposit account is created with the far future date as the first deposit date | medium |

---

## Accounting — Chart of Accounts

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit GL Account | User logged in as <Role>, An existing GL Account is available | 1. Click on the Account Name of the GL Account to open its detail view<br>2. Click on the Edit option | GL Account details opened for editing | high |
| TC-002 | WF-002 | Delete GL Account | User logged in as <Role>, An existing GL Account is available | 1. Click on the Account Name of the GL Account to open its detail view<br>2. Click on the Delete option<br>3. Confirm the deletion | GL Account deleted successfully | high |
| TC-003 | WF-003 | Open Create GL Account Form | User logged in as <Role> | 1. Click on the + Create GL Account button | opens the creation form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Leave the Account Type dropdown blank and submit |  | 1. Click on '+ Create GL Account' button<br>2. Leave the Account Type field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-005 | WF-003 | Leave the GL Code field blank and submit |  | 1. Click on '+ Create GL Account' button<br>2. Leave the GL Code field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-006 | WF-003 | Leave the Account Name field blank and submit |  | 1. Click on '+ Create GL Account' button<br>2. Leave the Account Name field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-007 | WF-003 | Submit with all required fields empty |  | 1. Click on '+ Create GL Account' button<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; errors shown on Account Type, GL Code, and Account Name fields | high |
| TC-008 | WF-003 | Enter a duplicate GL Code and submit |  | 1. Click on '+ Create GL Account' button<br>2. Enter <duplicate GL Code> in the GL Code field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Error shown: 'GL Code must be unique' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-003 | Attempt to create a GL Account with a duplicate GL Code | A GL Account with the same GL Code already exists | 1. Click the '+ Create GL Account' button<br>2. Fill in the form with the same GL Code as the existing account<br>3. Fill in all other required fields with valid data<br>4. Click Submit | Form submission is blocked; an error message displays indicating 'GL Code must be unique' | medium |
| TC-010 (input_edge) | WF-003 | Enter a very long Account Name |  | 1. Click the '+ Create GL Account' button<br>2. Fill in the form with a valid Account Type<br>3. Enter a long string (200+ characters) in the Account Name field<br>4. Fill in all other required fields with valid data<br>5. Click Submit | Form submission is either accepted or an error message indicates the length constraint for the Account Name | low |
| TC-011 (input_edge) | WF-003 | Enter special characters in the Description field |  | 1. Click the '+ Create GL Account' button<br>2. Fill in the form with a valid Account Type<br>3. Enter special characters (e.g., !@#$%^&*()) in the Description field<br>4. Fill in all other required fields with valid data<br>5. Click Submit | Form submission is accepted, and the Description field displays the entered special characters correctly | low |
| TC-012 (input_edge) | WF-003 | Enter leading and trailing whitespace in the Account Name |  | 1. Click the '+ Create GL Account' button<br>2. Fill in the form with a valid Account Type<br>3. Enter '   Account Name   ' in the Account Name field<br>4. Fill in all other required fields with valid data<br>5. Click Submit | Leading and trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Accounting — Journal Entries & Closures

Total: **16** (positive: 4, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add Journal Entry with valid data | User logged in as <Role> | 1. Click '+ Add Journal Entry' button<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid reference number> in the Reference Number field<br>5. Enter <valid transaction date> in the Transaction Date field<br>6. Click 'Add Row' to add an entry line<br>7. Select <valid GL account> from the GL Account dropdown in the entry line<br>8. Enter <valid amount> in the Amount field of the entry line<br>9. Click 'Add Row' to add another entry line<br>10. Select <valid GL account> from the GL Account dropdown in the second entry line<br>11. Enter <valid amount> in the Amount field of the second entry line<br>12. Click Submit | A success notification is displayed; the Journal entry created. | high |
| TC-002 | WF-002 | Add Journal Entry with validation error on total debits and credits | User logged in as <Role> | 1. Click '+ Add Journal Entry' button<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click 'Add Row' to add an entry line<br>6. Select <valid GL account> from the GL Account dropdown in the entry line<br>7. Enter <valid amount> in the Amount field of the entry line<br>8. Click Submit | Validation error; total debits must equal total credits | high |
| TC-003 | WF-003 | Create Closure with valid data | User logged in as <Role> | 1. Click '+ Create Closure' button<br>2. Select <valid office> from the Office dropdown<br>3. Enter <valid closing date> in the Closing Date field<br>4. Enter <valid comments> in the Comments field<br>5. Click Submit | A success notification is displayed; the Closure created. | high |
| TC-004 | WF-004 | Create Closure that prevents journal entries for closing date | User logged in as <Role> | 1. Click '+ Create Closure' button<br>2. Select <valid office> from the Office dropdown<br>3. Enter <valid closing date> in the Closing Date field<br>4. Click Submit | A success notification is displayed; journal entries are prevented for dates on or before the closing date. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Office dropdown blank and submit the Add Journal Entry form |  | 1. Open the Add Journal Entry form<br>2. Leave the Office field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-006 |  | Leave the Transaction Date field blank and submit the Add Journal Entry form |  | 1. Open the Add Journal Entry form<br>2. Leave the Transaction Date field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-007 |  | Leave the GL Account field blank in an Entry Line and submit the Add Journal Entry form |  | 1. Open the Add Journal Entry form<br>2. Add an Entry Line<br>3. Leave the GL Account field blank<br>4. Fill the Amount field with a valid number<br>5. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-008 |  | Leave the Amount field blank in an Entry Line and submit the Add Journal Entry form |  | 1. Open the Add Journal Entry form<br>2. Add an Entry Line<br>3. Fill the GL Account field with a valid selection<br>4. Leave the Amount field blank<br>5. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-009 | WF-002 | Submit the Add Journal Entry form with total debits not equal to total credits |  | 1. Open the Add Journal Entry form<br>2. Fill in valid data for all required fields<br>3. Add Entry Lines with total debits not equal to total credits<br>4. Click Submit | Validation error; total debits must equal total credits | high |
| TC-010 |  | Leave the Office dropdown blank and submit the Create Closure form |  | 1. Open the Create Closure form<br>2. Leave the Office field blank<br>3. Fill the Closing Date field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the Closing Date field blank and submit the Create Closure form |  | 1. Open the Create Closure form<br>2. Leave the Closing Date field blank<br>3. Fill the Office field with a valid selection<br>4. Click Submit | Inline validation error appears on the Closing Date field indicating it is required | high |
| TC-012 | WF-004 | Create a closure for a date that allows journal entries |  | 1. Open the Create Closure form<br>2. Fill in valid data for all required fields with a Closing Date in the future<br>3. Click Submit | Closure created; journal entries are still allowed for dates on or before the closing date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-002 | Total debits equal total credits (boundary case) | User has filled in all required fields in the Add Journal Entry Form | 1. Enter a valid amount in the first Entry Line's Amount field<br>2. Enter the same amount in the second Entry Line's Amount field<br>3. Click Submit | Form submits successfully; journal entry created with total debits equal to total credits | medium |
| TC-014 (boundary) | WF-002 | Total debits less than total credits (boundary case) | User has filled in all required fields in the Add Journal Entry Form | 1. Enter a valid amount in the first Entry Line's Amount field<br>2. Enter a smaller amount in the second Entry Line's Amount field<br>3. Click Submit | Validation error; total debits must equal total credits | medium |
| TC-015 (boundary) | WF-004 | Closing date prevents journal entries on or before the date | User has created a closure with a specified closing date | 1. Attempt to add a journal entry with a Transaction Date equal to the Closing Date<br>2. Click Submit | Submission is blocked; journal entries are prevented for dates on or before the closing date | medium |
| TC-016 (boundary) | WF-004 | Closing date allows journal entries after the date | User has created a closure with a specified closing date | 1. Attempt to add a journal entry with a Transaction Date after the Closing Date<br>2. Click Submit | Form submits successfully; journal entry created for date after the closing date | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new accounting rule | User logged in as <Role> | 1. Click '+ Create Rule' to open the creation form<br>2. Select 'Office 1' from the Office dropdown<br>3. Enter <valid rule name> in the Rule Name field<br>4. Select 'GL Account 1' from the Debit Tags/Debit Account dropdown<br>5. Check the Allow Multiple Debit Entries checkbox<br>6. Select 'GL Account 2' from the Credit Tags/Credit Account dropdown<br>7. Check the Allow Multiple Credit Entries checkbox<br>8. Click '+ Create Rule' to submit the form | A new accounting rule is created | high |
| TC-002 | WF-002 | Edit an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click 'Edit' to open the editing form<br>3. Change the Rule Name to <new valid rule name><br>4. Click 'Save' to update the rule | Rule details updated | medium |
| TC-003 | WF-003 | Delete an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click 'Delete' to remove the rule<br>3. Confirm the deletion | Rule deleted | medium |
| TC-004 | WF-004 | Create a new financial activity mapping | User logged in as <Role> | 1. Click '+ Create Mapping' to open the creation form<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select 'GL Account 1' from the GL Account dropdown<br>4. Click '+ Create Mapping' to submit the form | A new financial activity mapping is created | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Rule Name field blank and submit the Create Rule form |  | 1. Click on '+ Create Rule'<br>2. Leave the Rule Name field blank<br>3. Select any option in the Office dropdown<br>4. Click '+ Create Rule' | Inline validation error appears on the Rule Name field indicating it is required | high |
| TC-006 | WF-004 | Attempt to create a financial activity mapping with a duplicate financial activity |  | 1. Click on '+ Create Mapping'<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select any option in the GL Account dropdown<br>4. Click '+ Create Mapping'<br>5. Click on '+ Create Mapping' again<br>6. Select 'Asset Transfer' from the Financial Activity dropdown again<br>7. Select any option in the GL Account dropdown<br>8. Click '+ Create Mapping' | Form does not submit; error shown indicating 'each financial activity can only be mapped once' | high |
| TC-007 |  | Attempt to create a rule with all fields empty |  | 1. Click on '+ Create Rule'<br>2. Leave all fields empty<br>3. Click '+ Create Rule' | Inline validation error appears on the Rule Name field indicating it is required; form does not submit | high |
| TC-008 |  | Attempt to create a mapping with all fields empty |  | 1. Click on '+ Create Mapping'<br>2. Leave all fields empty<br>3. Click '+ Create Mapping' | Form does not submit; error shown on Financial Activity and GL Account fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-004 | Attempt to map a financial activity that is already mapped | At least one financial activity is already mapped | 1. Open the Create Mapping form<br>2. Select a financial activity that is already mapped in the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click + Create Mapping | Form submission is blocked; an error message indicates that each financial activity can only be mapped once. | medium |
| TC-010 (boundary) | WF-004 | Create mapping with a financial activity that has not been mapped yet | No financial activities are mapped yet | 1. Open the Create Mapping form<br>2. Select a financial activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click + Create Mapping | Form submits successfully; a new financial activity mapping is created. | medium |
| TC-011 (boundary) | WF-001 | Create rule with minimum required fields filled | User is on the Create Rule form | 1. Select an Office from the dropdown<br>2. Enter a valid Rule Name in the Rule_Name field<br>3. Select a Debit Account from the dropdown<br>4. Select a Credit Account from the dropdown<br>5. Click + Create Rule | Form submits successfully; a new accounting rule is created. | medium |
| TC-012 (boundary) | WF-001 | Create rule with no Rule Name entered | User is on the Create Rule form | 1. Select an Office from the dropdown<br>2. Leave the Rule_Name field empty<br>3. Select a Debit Account from the dropdown<br>4. Select a Credit Account from the dropdown<br>5. Click + Create Rule | Form submission is blocked; an error message indicates that Rule Name is required. | medium |

---

## Provisioning

Total: **15** (positive: 5, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Create Criteria Form | User logged in as <Role> | 1. Click '+ Create' button | The creation form is opened | high |
| TC-002 | WF-002 | Create Provisioning Entry | User logged in as <Role>, Criteria are defined in the system | 1. Click '+ Create Provisioning Entry' button | New provisioning entries are generated based on the current loan portfolio status | high |
| TC-003 | WF-003 | Review Provisioning Entry | User logged in as <Role>, Provisioning entries exist in the system | 1. Click 'Review' on a provisioning entry | A detailed breakdown by loan product and category is shown | medium |
| TC-004 | WF-004 | Recreate Provisioning Entry | User logged in as <Role>, Provisioning entries exist in the system | 1. Click 'Recreate' on a provisioning entry | The provisioning entry is recreated | medium |
| TC-005 | WF-005 | View Criteria Name | User logged in as <Role>, Criteria exist in the system | 1. Click on a 'Criteria Name' link in the table | Navigates to criteria details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave Criteria Name blank and submit |  | 1. Open the Create Criteria Form<br>2. Leave the Criteria Name field blank<br>3. Click + Create | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Open the Create Criteria Form<br>2. Leave all required fields in the Definitions table blank<br>3. Click + Create | Inline validation error appears on the Criteria Name field indicating it is required; form does not submit | high |
| TC-008 | WF-002 | Attempt to create provisioning entry without criteria defined |  | 1. Click + Create Provisioning Entry | Status remains unchanged; no provisioning entries are created; error shown indicating criteria must be defined | high |
| TC-009 | WF-005 | Attempt to view Criteria Name without having defined criteria |  | 1. Click on Criteria Name link | Status remains unchanged; no navigation occurs; error shown indicating criteria must be defined | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Add minimum number of definitions | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add exactly 1 row to the Definitions table<br>3. Fill all required fields in the Definitions row | Form submits successfully; entity is created with the minimum number of definitions | medium |
| TC-011 (boundary) | WF-001 | Attempt to add one more definition than allowed | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add 2 rows to the Definitions table (one more than the minimum)<br>3. Fill all required fields in both Definitions rows | Form submission is blocked; a visible error indicates that at least one definition is required | medium |
| TC-012 (input_edge) | WF-001 | Enter long text in Criteria Name | User is on the Create Criteria Form | 1. Enter a string of 200+ characters in the Criteria_Name field | Field accepts the input; Criteria Name is displayed correctly on the detail page | low |
| TC-013 (input_edge) | WF-001 | Enter special characters in Criteria Name | User is on the Create Criteria Form | 1. Enter special characters in the Criteria_Name field | Field accepts the input; Criteria Name is displayed correctly on the detail page | low |
| TC-014 (boundary) | WF-002 | Create provisioning entry with valid criteria | User has created valid provisioning criteria | 1. Click on the + Create Provisioning Entry button | New provisioning entries are generated successfully based on the current loan portfolio status | medium |
| TC-015 (input_edge) | WF-002 | Rapidly create provisioning entries | User has created valid provisioning criteria | 1. Click on the + Create Provisioning Entry button<br>2. Immediately click the + Create Provisioning Entry button again | The second entry creation is blocked; a message indicates that entries are being processed | low |

---

## Offices

Total: **14** (positive: 3, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the Create Office form | User logged in as <Role> | 1. Click the '+ Create Office' button | The creation form opens | high |
| TC-002 | WF-001 | Create a new office with valid details | User logged in as <Role>, The creation form is open | 1. Enter <valid office name> in the Office Name field<br>2. Select <valid head office> from the Parent Office dropdown<br>3. Enter <valid date> in the Opened On Date field<br>4. Click Submit | The office is created and displayed in the offices table | high |
| TC-003 | WF-002 | Edit an existing office | User logged in as <Role>, Offices table is displayed | 1. Click the Edit action for an existing office | The office detail page opens | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Office Name field blank |  | 1. Click the '+ Create Office' button<br>2. Leave the Office Name field blank<br>3. Fill in the Parent Office and Opened On Date fields<br>4. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Parent Office field blank |  | 1. Click the '+ Create Office' button<br>2. Leave the Parent Office field blank<br>3. Fill in the Office Name and Opened On Date fields<br>4. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-006 | WF-001 | Leave the Opened On Date field blank |  | 1. Click the '+ Create Office' button<br>2. Fill in the Office Name and Parent Office fields<br>3. Leave the Opened On Date field blank<br>4. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Click the '+ Create Office' button<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Office Name, Parent Office, and Opened On Date fields are highlighted with validation errors | high |
| TC-008 | WF-001 | Select a non-Head Office as Parent Office when creating a root office |  | 1. Click the '+ Create Office' button<br>2. Fill in the Office Name field<br>3. Select a non-Head Office for the Parent Office<br>4. Fill in the Opened On Date field<br>5. Click Submit | Inline validation error appears on the Parent Office field indicating it must be Head Office if root | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter valid opening date |  | 1. Click the '+ Create Office' button<br>2. Enter today's date in the 'Opened On Date' field<br>3. Fill 'Office Name' and 'Parent Office' fields with valid data<br>4. Click Submit | Form submits successfully; office is created with today's date | medium |
| TC-010 (boundary) | WF-001 | Enter yesterday's date as opening date |  | 1. Click the '+ Create Office' button<br>2. Enter yesterday's date in the 'Opened On Date' field<br>3. Fill 'Office Name' and 'Parent Office' fields with valid data<br>4. Click Submit | Form submits successfully; office is created with yesterday's date | medium |
| TC-011 (boundary) | WF-001 | Enter a future date as opening date |  | 1. Click the '+ Create Office' button<br>2. Enter a date next year in the 'Opened On Date' field<br>3. Fill 'Office Name' and 'Parent Office' fields with valid data<br>4. Click Submit | Form submits successfully; office is created with future date | medium |
| TC-012 (boundary) | WF-001 | Enter invalid parent office |  | 1. Click the '+ Create Office' button<br>2. Enter valid data in 'Office Name' field<br>3. Enter a non-Head Office in the 'Parent Office' field<br>4. Enter today's date in the 'Opened On Date' field<br>5. Click Submit | Form submission is blocked; error message indicates 'must be Head Office if root' | medium |
| TC-013 (input_edge) |  | Enter long office name |  | 1. Click the '+ Create Office' button<br>2. Enter a string longer than 200 characters in the 'Office Name' field<br>3. Fill 'Parent Office' with valid data<br>4. Enter today's date in the 'Opened On Date' field<br>5. Click Submit | Form submission is blocked; error message indicates 'Office Name is too long' | low |
| TC-014 (input_edge) |  | Enter special characters in office name |  | 1. Click the '+ Create Office' button<br>2. Enter special characters in the 'Office Name' field<br>3. Fill 'Parent Office' with valid data<br>4. Enter today's date in the 'Opened On Date' field<br>5. Click Submit | Form submission is blocked; error message indicates 'Invalid characters in Office Name' | low |

---

## Employees

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Create Employee Form | User logged in as <Role> | 1. Click the '+ Create Employee' button | The creation form opens | high |
| TC-002 | WF-002 | Edit Employee Information | User logged in as <Role>, Employee is listed in the Employees table | 1. Click the Name link of the employee to edit<br>2. Click the Edit button | Employee information updated | high |
| TC-003 | WF-001 | Submit Create Employee Form with Required Fields | User logged in as <Role>, Creation form is open | 1. Enter <Office> in the Office field<br>2. Enter <First Name> in the First Name field<br>3. Enter <Last Name> in the Last Name field<br>4. Click Submit | The employee is added to the Employees table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Office field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Fill in First Name and Last Name with valid values<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-005 | WF-001 | Leave the First Name field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Fill in Office and Last Name with valid values<br>3. Leave the First Name field blank<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-006 | WF-001 | Leave the Last Name field blank and submit the Create Employee form |  | 1. Click on the '+ Create Employee' button<br>2. Fill in Office and First Name with valid values<br>3. Leave the Last Name field blank<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-007 | WF-001 | Submit the Create Employee form with all required fields empty |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office, First Name, and Last Name fields blank<br>3. Click Submit | Form does not submit; error shown on Office, First Name, and Last Name fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Joining Date is today's date |  | 1. Click on the '+ Create Employee' button<br>2. Enter today's date in the Joining Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; employee is created with today's date as Joining Date | medium |
| TC-009 (boundary) | WF-001 | Joining Date is yesterday's date |  | 1. Click on the '+ Create Employee' button<br>2. Enter yesterday's date in the Joining Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; employee is created with yesterday's date as Joining Date | medium |
| TC-010 (boundary) | WF-001 | Joining Date is a far future date |  | 1. Click on the '+ Create Employee' button<br>2. Enter a date 10 years in the future in the Joining Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; employee is created with a future date as Joining Date | medium |
| TC-011 (data_edge) | WF-001 | Enter a very long name in First Name field |  | 1. Click on the '+ Create Employee' button<br>2. Enter a string of 200+ characters in the First Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; employee is created with the long First Name | low |
| TC-012 (input_edge) | WF-001 | Enter special characters in Last Name field |  | 1. Click on the '+ Create Employee' button<br>2. Enter special characters in the Last Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; employee is created with special characters in Last Name | low |
| TC-013 (input_edge) | WF-001 | Enter leading/trailing whitespace in Office field |  | 1. Click on the '+ Create Employee' button<br>2. Enter '   Office Name   ' in the Office field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Teller & Cashier Management

Total: **23** (positive: 6, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new Teller | User logged in as <Role> | 1. Click '+ Create Teller' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid teller name> in the Teller Name field<br>4. Enter <valid start date> in the Start Date field<br>5. Select 'Active' from the Status dropdown<br>6. Click Submit | Teller created; success message shown | high |
| TC-002 | WF-002 | View Teller details | User logged in as <Role>, At least one teller exists | 1. Click on the Teller Name of the first teller in the Tellers table | Teller details displayed | high |
| TC-003 | WF-003 | Edit Teller details | User logged in as <Role>, At least one teller exists | 1. Click on the Teller Name of the first teller in the Tellers table<br>2. Click Edit button<br>3. Update <valid teller name> in the Teller Name field<br>4. Click Submit | Teller details updated; success message shown | high |
| TC-004 | WF-004 | Allocate a Cashier | User logged in as <Role>, At least one teller exists | 1. Click on the Teller Name of the first teller in the Tellers table<br>2. Click '+ Allocate Cashier' button<br>3. Enter <valid staff> in the Staff field<br>4. Enter <valid start date> in the Start Date field<br>5. Click Submit | Cashier allocation form opened | high |
| TC-005 | WF-005 | Allocate Cash from the vault | User logged in as <Role>, Cashier Detail page is open | 1. Click Allocate Cash Button | Cash added from the vault | medium |
| TC-006 | WF-006 | Settle Cash to the vault | User logged in as <Role>, Cashier Detail page is open | 1. Enter <valid amount> in the Amount field<br>2. Enter <valid currency> in the Currency field<br>3. Enter <valid transaction date> in the Transaction Date field<br>4. Click Settle Cash Button | Cash returned to the vault | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Office field blank and submit the Create Teller form |  | 1. Leave the Office field blank<br>2. Fill in the Teller Name, Start Date, and all other fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-008 |  | Leave the Teller Name field blank and submit the Create Teller form |  | 1. Leave the Teller Name field blank<br>2. Fill in the Office, Start Date, and all other fields<br>3. Click Submit | Inline validation error appears on the Teller Name field indicating it is required | high |
| TC-009 |  | Leave the Start Date field blank and submit the Create Teller form |  | 1. Leave the Start Date field blank<br>2. Fill in the Office, Teller Name, and all other fields<br>3. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 |  | Submit the Create Teller form with all required fields empty |  | 1. Leave the Office, Teller Name, and Start Date fields blank<br>2. Click Submit | Form does not submit; error shown on Office, Teller Name, and Start Date fields indicating they are required | high |
| TC-011 |  | Attempt to allocate a cashier without filling the Staff field |  | 1. Click on the + Allocate Cashier button<br>2. Leave the Staff field blank<br>3. Fill in the Start Date and all other fields<br>4. Click Submit | Inline validation error appears on the Staff field indicating it is required | high |
| TC-012 |  | Attempt to settle cash without filling the Amount, Currency, and Transaction Date fields |  | 1. Click on the Settle Cash Button<br>2. Leave the Amount, Currency, and Transaction Date fields blank<br>3. Click Submit | Form does not submit; error shown on Amount, Currency, and Transaction Date fields indicating they are required | high |
| TC-013 | WF-001 | Attempt to create a new teller with a duplicate Teller Name |  | 1. Fill in the Office, Teller Name (same as existing teller), Start Date, and all other fields<br>2. Click Submit | Form does not submit; error shown indicating Teller Name must be unique | medium |
| TC-014 | WF-006 | Attempt to settle cash with an Amount less than or equal to zero |  | 1. Click on the Settle Cash Button<br>2. Enter <amount less than or equal to zero> in the Amount field<br>3. Fill in the Currency and Transaction Date fields<br>4. Click Submit | Form does not submit; error shown on Amount field indicating it must be greater than zero | medium |
| TC-015 | WF-004 | Attempt to allocate a cashier with an End Date before the Start Date |  | 1. Click on the + Allocate Cashier button<br>2. Fill in the Staff, Start Date (e.g., <today's date>), and End Date (e.g., <yesterday's date>)<br>3. Click Submit | Form does not submit; error shown indicating End Date must be after Start Date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-001 | Create a Teller with Start Date set to today |  | 1. Click '+ Create Teller'<br>2. Enter a valid Office in the Office field<br>3. Enter a valid Teller Name in the Teller Name field<br>4. Enter today's date in the Start Date field<br>5. Click Submit | Form submits successfully; teller is created with today's Start Date | medium |
| TC-017 (boundary) | WF-001 | Create a Teller with Start Date set to tomorrow |  | 1. Click '+ Create Teller'<br>2. Enter a valid Office in the Office field<br>3. Enter a valid Teller Name in the Teller Name field<br>4. Enter tomorrow's date in the Start Date field<br>5. Click Submit | Form submits successfully; teller is created with tomorrow's Start Date | medium |
| TC-018 (boundary) | WF-001 | Create a Teller with End Date set to today |  | 1. Click '+ Create Teller'<br>2. Enter a valid Office in the Office field<br>3. Enter a valid Teller Name in the Teller Name field<br>4. Enter today's date in the Start Date field<br>5. Enter today's date in the End Date field<br>6. Click Submit | Form submits successfully; teller is created with today's End Date | medium |
| TC-019 (boundary) | WF-001 | Create a Teller with End Date set to yesterday |  | 1. Click '+ Create Teller'<br>2. Enter a valid Office in the Office field<br>3. Enter a valid Teller Name in the Teller Name field<br>4. Enter today's date in the Start Date field<br>5. Enter yesterday's date in the End Date field<br>6. Click Submit | Form is blocked; error shown indicating 'End Date must not be before Start Date' | medium |
| TC-020 (boundary) | WF-004 | Allocate a Cashier with Start Date set to today |  | 1. Click '+ Allocate Cashier'<br>2. Enter a valid Staff name in the Staff field<br>3. Enter today's date in the Start Date field<br>4. Click Submit | Form submits successfully; cashier is allocated with today's Start Date | medium |
| TC-021 (boundary) | WF-004 | Allocate a Cashier with Start Date set to tomorrow |  | 1. Click '+ Allocate Cashier'<br>2. Enter a valid Staff name in the Staff field<br>3. Enter tomorrow's date in the Start Date field<br>4. Click Submit | Form submits successfully; cashier is allocated with tomorrow's Start Date | medium |
| TC-022 (boundary) | WF-006 | Settle Cash with Amount equal to zero |  | 1. Click 'Settle Cash'<br>2. Enter '0' in the Amount field<br>3. Enter a valid Currency in the Currency field<br>4. Enter today's date in the Transaction Date field<br>5. Click Submit | Form submits successfully; cash is settled with an Amount of 0 | medium |
| TC-023 (boundary) | WF-006 | Settle Cash with Amount set to a negative value |  | 1. Click 'Settle Cash'<br>2. Enter '-1' in the Amount field<br>3. Enter a valid Currency in the Currency field<br>4. Enter today's date in the Transaction Date field<br>5. Click Submit | Form is blocked; error shown indicating 'Amount must be greater than zero' | medium |

---

## Users & Roles

Total: **21** (positive: 5, negative: 11, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new user with valid details | User logged in as <Role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <valid password> in the Repeat Password field<br>9. Click Submit | User created; success message shown | high |
| TC-002 | WF-002 | Create a user with a non-unique username | User logged in as <Role>, A user with username '<existing username>' exists | 1. Click '+ Create User' button<br>2. Enter '<existing username>' in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <valid password> in the Repeat Password field<br>9. Click Submit | User created; success message shown | high |
| TC-003 | WF-003 | Create a user with valid email format | User logged in as <Role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter '<invalid email>' in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <valid password> in the Repeat Password field<br>9. Click Submit | User created; success message shown | high |
| TC-004 | WF-004 | Create a new role with valid details | User logged in as <Role> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Enter <description> in the Description field<br>4. Click Submit | Role created; success message shown | high |
| TC-005 | WF-005 | View user details | User logged in as <Role>, A user with username '<existing username>' exists | 1. Click on the Username '<existing username>' in the Users Table | User details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-007 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-008 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-009 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-010 |  | Leave the Office field blank |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Enter a non-unique Username |  | 1. Enter <non-unique username> in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Error shown: 'Username must be unique' | high |
| TC-013 |  | Enter an invalid Email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Email field indicating it is not a valid email format | high |
| TC-014 |  | Enter a Password that does not meet policy |  | 1. Enter <password not meeting policy> in the Password field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Password field indicating it must meet password policy | high |
| TC-015 |  | Enter mismatched Password and Repeat Password |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Repeat Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match | high |
| TC-016 |  | Attempt to create a user without filling any required fields |  | 1. Leave all required fields blank<br>2. Click Submit | Form does not submit; multiple inline validation errors shown for all required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-002 | Create User with unique Username at boundary |  | 1. Enter a Username that is exactly the same as an existing Username<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message indicates that the Username must be unique. | medium |
| TC-018 (boundary) | WF-003 | Create User with valid Email format at boundary |  | 1. Enter an Email that is exactly valid according to email format<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; user is created with the provided Email. | medium |
| TC-019 (input_edge) |  | Create User with long Username |  | 1. Enter a Username that is a very long string (200+ characters)<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message indicates that the Username exceeds maximum length. | low |
| TC-020 (input_edge) |  | Create User with special characters in First Name |  | 1. Enter special characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message indicates invalid characters in the First Name field. | low |
| TC-021 (interaction_edge) |  | Rapid re-submission after successful user creation | A user has just been successfully created | 1. Click the browser back button after the success message<br>2. Click the Create User button again | The creation form is shown blank and not pre-filled with the previous user's data. | low |

---

## Reports

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Report with Parameters Form | User logged in as <Role> | 1. Click on the Name link of a report in the Reports table | The parameters form for the selected report is displayed | high |
| TC-002 | WF-002 | Run Report and Display Results | User logged in as <Role>, Parameters form is displayed | 1. Fill in any parameters if necessary<br>2. Click the 'Run Report' button | Displays report with sorting and pagination | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to open report parameters form without required fields |  | 1. Click on a report link to open the parameters form | Parameters form displays with all fields available for input; no required fields are enforced |  |
| TC-004 | WF-002 | Attempt to run report without selecting output options |  | 1. Open a report parameters form<br>2. Leave all fields blank<br>3. Click 'Run Report' | Form does not submit; report is not generated; no error shown as all fields are optional |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) | WF-001 | Enter long text in the parameters form fields | User is on the Reports page, User clicks on a report to open the parameters form | 1. Enter a long string (200+ characters) in the Office field<br>2. Enter a long string (200+ characters) in the Branch field<br>3. Enter a long string (200+ characters) in the Currency field<br>4. Enter a long string (200+ characters) in the Loan Product field<br>5. Enter a long string (200+ characters) in the Loan Officer field | Each field displays an error indicating that the input exceeds the maximum length allowed | low |
| TC-006 (input_edge) | WF-002 | Enter special characters in the parameters form fields | User is on the Reports page, User clicks on a report to open the parameters form | 1. Enter special characters in the Office field<br>2. Enter special characters in the Branch field<br>3. Enter special characters in the Currency field<br>4. Enter special characters in the Loan Product field<br>5. Enter special characters in the Loan Officer field | Each field displays an error indicating invalid characters are not accepted | low |
| TC-007 (input_edge) | WF-002 | Enter whitespace in the parameters form fields | User is on the Reports page, User clicks on a report to open the parameters form | 1. Enter leading and trailing whitespace in the Office field<br>2. Enter leading and trailing whitespace in the Branch field<br>3. Enter leading and trailing whitespace in the Currency field<br>4. Enter leading and trailing whitespace in the Loan Product field<br>5. Enter leading and trailing whitespace in the Loan Officer field | Leading/trailing whitespace is trimmed; saved values shown in the detail page have no extra spaces | low |
| TC-008 (data_edge) | WF-002 | Test pagination with maximum rows | User is on the Reports page, User generates a report with maximum rows | 1. Click the Run Report button<br>2. Observe the generated report | The report displays with pagination showing the maximum number of rows allowed | medium |

---

## Account Transfers & Standing Instructions

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient for the transfer amount | 1. Enter <From Office> in the From Office field<br>2. Enter <From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <From Account> in the From Account field<br>5. Enter <To Office> in the To Office field<br>6. Enter <To Client> in the To Client field<br>7. Select 'Loan Account' from the To Account Type dropdown<br>8. Enter <To Account> in the To Account field<br>9. Enter <valid transfer amount> in the Transfer Amount field<br>10. Select <valid date> in the Transfer Date field<br>11. Enter <Description> in the Description field<br>12. Click Submit | processes the transfer, debiting the source and crediting the destination | high |
| TC-002 | WF-002 | Enable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Enable on the standing instruction row | Standing instruction enabled | medium |
| TC-003 | WF-003 | Disable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Disable on the standing instruction row | Standing instruction disabled | medium |
| TC-004 | WF-004 | Delete a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Delete on the standing instruction row<br>2. Confirm deletion | Standing instruction deleted | medium |
| TC-005 | WF-005 | Create a new standing instruction | User logged in as <Role> | 1. Click '+ Create Standing Instruction'<br>2. Enter <Name> in the Name field<br>3. Enter <From Account> in the From Account field<br>4. Enter <To Account> in the To Account field<br>5. Select <Transfer Type> in the Transfer Type field<br>6. Enter <Priority> in the Priority field<br>7. Select 'Fixed' from the Instruction Type dropdown<br>8. Enter <valid amount> in the Amount field<br>9. Select <valid date> in the Validity From field<br>10. Select <valid date> in the Validity Till field<br>11. Select 'Periodic' from the Recurrence Type dropdown<br>12. Enter <Recurrence Frequency> in the Recurrence Frequency field<br>13. Enter <Recurrence Interval> in the Recurrence Interval field<br>14. Click Create | creates a new standing instruction | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Submit Account Transfer with Transfer Amount exceeding available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Enter a valid <date> in the Transfer Date field<br>3. Click Submit | Form does not submit; error shown on Transfer Amount field indicating 'Transfer amount must not exceed available balance' | high |
| TC-007 | WF-001 | Submit Account Transfer with blank Transfer Amount and Transfer Date |  | 1. Leave the Transfer Amount field blank<br>2. Leave the Transfer Date field blank<br>3. Click Submit | Form does not submit; error shown on Transfer Amount field indicating it is required; error shown on Transfer Date field indicating it is required | high |
| TC-008 | WF-005 | Create Standing Instruction with blank Name field |  | 1. Leave the Name field blank<br>2. Click Create | Form does not submit; error shown on Name field indicating it is required | high |
| TC-009 | WF-002 | Enable Standing Instruction when no standing instructions exist |  | 1. Attempt to enable a standing instruction that does not exist | Action is blocked; no standing instruction is enabled | medium |
| TC-010 | WF-004 | Delete Standing Instruction when no standing instructions exist |  | 1. Attempt to delete a standing instruction that does not exist | Action is blocked; no standing instruction is deleted | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Transfer amount equals available balance | User has an available balance equal to the transfer amount | 1. Select 'From Account Type' as 'Savings Account'<br>2. Enter the 'Transfer Amount' equal to the available balance<br>3. Enter the 'Transfer Date'<br>4. Click 'Submit' | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-012 (boundary) | WF-001 | Transfer amount exceeds available balance | User has an available balance | 1. Select 'From Account Type' as 'Savings Account'<br>2. Enter the 'Transfer Amount' greater than the available balance<br>3. Enter the 'Transfer Date'<br>4. Click 'Submit' | Error shown indicating the transfer amount exceeds the available balance | medium |
| TC-013 (boundary) | WF-005 | Validity From date equals Validity Till date |  | 1. Click '+ Create Standing Instruction'<br>2. Enter a name in the 'Name' field<br>3. Enter the 'Validity From' date<br>4. Enter the same date in the 'Validity Till' field<br>5. Click 'Create' | Standing instruction is created successfully with the same start and end date | medium |
| TC-014 (boundary) | WF-005 | Validity From date is one day before Validity Till date |  | 1. Click '+ Create Standing Instruction'<br>2. Enter a name in the 'Name' field<br>3. Enter today's date in the 'Validity From' field<br>4. Enter tomorrow's date in the 'Validity Till' field<br>5. Click 'Create' | Standing instruction is created successfully with Validity From and Validity Till dates correctly set | medium |

---

## Tax Management

Total: **17** (positive: 4, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-002 | Create a new tax component successfully | User logged in as <Role> | 1. Click '+ Create Tax Component' button<br>2. Enter <valid name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Enter <valid debit account> in the Debit Account field<br>6. Select 'Income' from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Enter <valid start date> in the Start Date field<br>9. Click Create | A success notification is displayed; the tax component is visible in the Tax Components table | high |
| TC-002 | WF-001 | View tax component details | User logged in as <Role>, At least one tax component exists | 1. Click the Name link of the first tax component in the Tax Components table | View tax component details | medium |
| TC-003 | WF-004 | Create a new tax group successfully | User logged in as <Role> | 1. Click '+ Create Tax Group' button<br>2. Enter <valid name> in the Name field<br>3. Click 'Add Row' in the Tax Components section<br>4. Enter <valid start date> in the Start Date field of the new row<br>5. Click Create | A success notification is displayed; the tax group is visible in the Tax Groups table | high |
| TC-004 | WF-003 | View tax group details | User logged in as <Role>, At least one tax group exists | 1. Click the Name link of the first tax group in the Tax Groups table | View tax group details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-002 | Leave the Name field blank and submit the Create Tax Component form |  | 1. Leave the Name field blank<br>2. Fill Percentage with a valid value<br>3. Select a Debit Account Type<br>4. Fill Start Date with a valid date<br>5. Click Create | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 | WF-002 | Leave the Percentage field blank and submit the Create Tax Component form |  | 1. Fill Name with a valid value<br>2. Leave the Percentage field blank<br>3. Select a Debit Account Type<br>4. Fill Start Date with a valid date<br>5. Click Create | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-007 | WF-002 | Leave the Start Date field blank and submit the Create Tax Component form |  | 1. Fill Name with a valid value<br>2. Fill Percentage with a valid value<br>3. Select a Debit Account Type<br>4. Leave the Start Date field blank<br>5. Click Create | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-008 | WF-004 | Leave the Name field blank and submit the Create Tax Group form |  | 1. Leave the Name field blank<br>2. Click Create | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-004 | Leave the Start Date field blank in the Tax Components section and submit the Create Tax Group form |  | 1. Fill Name with a valid value<br>2. Add a Tax Component with Start Date left blank<br>3. Click Create | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 |  | Attempt to access the Create Tax Component form without authentication |  | 1. Navigate to the Create Tax Component page | User is redirected to the login page | high |
| TC-011 |  | Attempt to access the Create Tax Group form without authentication |  | 1. Navigate to the Create Tax Group page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-002 | Create Tax Component with minimum required Percentage |  | 1. Open the Create Tax Component form<br>2. Enter the minimum allowed value in the Percentage field<br>3. Fill all other required fields<br>4. Click Create | Form submits successfully; entity is created with the minimum allowed Percentage | medium |
| TC-013 (boundary) | WF-002 | Create Tax Component with Percentage just below minimum |  | 1. Open the Create Tax Component form<br>2. Enter one unit below the minimum allowed value in the Percentage field<br>3. Fill all other required fields<br>4. Click Create | Percentage field displays an error indicating the value is below the minimum allowed | medium |
| TC-014 (boundary) | WF-004 | Create Tax Group with exactly one Tax Component |  | 1. Open the Create Tax Group form<br>2. Add exactly one Tax Component with a valid Start_Date<br>3. Fill the Name field<br>4. Click Create | Form submits successfully; tax group is created with one Tax Component | medium |
| TC-015 (boundary) | WF-004 | Create Tax Group with more than maximum allowed Tax Components |  | 1. Open the Create Tax Group form<br>2. Add maximum allowed Tax Components plus one<br>3. Fill the Name field<br>4. Click Create | Adding Tax Components is blocked; only the maximum allowed entries appear in the group | medium |
| TC-016 (input_edge) |  | Enter long text in Name field of Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Enter a string longer than 200 characters in the Name field<br>3. Fill all other required fields<br>4. Click Create | Form submission is either accepted or truncated with a visible indicator | low |
| TC-017 (input_edge) |  | Enter special characters in Name field of Create Tax Component form |  | 1. Open the Create Tax Component form<br>2. Enter special characters in the Name field<br>3. Fill all other required fields<br>4. Click Create | Form submission is either accepted or a specific error is shown | low |

---

## Organization Settings

Total: **17** (positive: 5, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Holiday Creation Form | User logged in as <Admin> | 1. Navigate to the Holidays page<br>2. Click '+ Create Holiday' | opens holiday creation form | high |
| TC-002 | WF-002 | Open Fund Creation Form | User logged in as <Admin> | 1. Navigate to the Funds page<br>2. Click 'Create Fund' | opens fund creation form | high |
| TC-003 | WF-003 | Add New Payment Type | User logged in as <Admin>, Payment Types page is open | 1. Click '+ Create' on the Payment Types page<br>2. Fill in the required fields<br>3. Submit the form | adds new payment type | high |
| TC-004 | WF-004 | Download Bulk Import Template | User logged in as <Admin>, Bulk Import page is open | 1. Click 'Download_Template' button | downloads import template | medium |
| TC-005 | WF-005 | Upload Bulk Import Data | User logged in as <Admin>, Bulk Import page is open | 1. Click 'Upload_Interface' button<br>2. Select a <valid file> to upload<br>3. Confirm the upload | data imported successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave the Name field blank when creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill in valid From Date and To Date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-007 | WF-001 | Leave all required fields blank when creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name, From Date, and To Date fields blank<br>3. Click Submit | Form does not submit; error shown on Name field, From Date field, and To Date field indicating they are required | high |
| TC-008 | WF-005 | Leave the Upload Interface blank when uploading bulk import data |  | 1. Click on Upload_Interface<br>2. Leave the Upload Interface blank<br>3. Click Submit | Inline validation error appears on the Upload Interface field indicating it is required | high |
| TC-009 | WF-003 | Attempt to create a payment type without filling required fields |  | 1. Click on '+ Create'<br>2. Leave the Name field blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 |  | Attempt to access the Organization Settings without authentication |  | 1. Navigate to the Organization Settings page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Create Holiday with From_Date equal to To_Date |  | 1. Click on '+ Create Holiday'<br>2. Enter 'Holiday Name' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Click Submit | Form submits successfully; holiday is created with From_Date and To_Date set to today's date | medium |
| TC-012 (boundary) | WF-001 | Create Holiday with From_Date one day before To_Date |  | 1. Click on '+ Create Holiday'<br>2. Enter 'Holiday Name' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Click Submit | Form submits successfully; holiday is created with From_Date and To_Date set correctly | medium |
| TC-013 (boundary) | WF-001 | Create Holiday with From_Date after To_Date |  | 1. Click on '+ Create Holiday'<br>2. Enter 'Holiday Name' in the Name field<br>3. Enter tomorrow's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Click Submit | Form is blocked; error message displayed indicating From_Date must be before To_Date | medium |
| TC-014 (boundary) | WF-005 | Upload Bulk Import Data with file at exact size limit |  | 1. Navigate to Bulk Import Page<br>2. Click on Upload_Interface<br>3. Select a file that is exactly at the size limit<br>4. Click Upload | Data imported successfully; confirmation message displayed | medium |
| TC-015 (boundary) | WF-005 | Upload Bulk Import Data with file over size limit |  | 1. Navigate to Bulk Import Page<br>2. Click on Upload_Interface<br>3. Select a file that is one byte over the size limit<br>4. Click Upload | Upload is blocked; error message displayed indicating file size exceeds limit | medium |
| TC-016 (input_edge) |  | Enter long text in Name field |  | 1. Click on '+ Create Holiday'<br>2. Enter a string longer than 200 characters in the Name field<br>3. Click Submit | Form is blocked; error message displayed indicating Name exceeds maximum length | low |
| TC-017 (input_edge) |  | Enter special characters in Name field |  | 1. Click on '+ Create Holiday'<br>2. Enter special characters (e.g., @#$%^&*) in the Name field<br>3. Click Submit | Form is blocked; error message displayed indicating invalid characters in Name | low |

---

## System Administration

Total: **21** (positive: 8, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Toggle Active Job | User logged in as <Role>, Job 'Apply Annual Fee' is listed in the Manage Scheduler Jobs table | 1. Click the toggle for 'Apply Annual Fee' job | Job status toggled successfully | high |
| TC-002 | WF-002 | Edit CRON Expression for Job | User logged in as <Role>, Job 'Add Accrual Transactions' is listed in the Manage Scheduler Jobs table | 1. Click the edit icon for 'Add Accrual Transactions'<br>2. Enter '<valid CRON expression>' in the CRON Expression field<br>3. Click Save | CRON expression updated successfully | high |
| TC-003 | WF-003 | Start/Stop Scheduler | User logged in as <Role> | 1. Click the Start/Stop Scheduler toggle | Scheduler status toggled successfully | high |
| TC-004 | WF-004 | Edit Configuration | User logged in as <Role>, Configuration 'maker-checker' is listed in the Global Configuration table | 1. Click the edit icon for 'maker-checker'<br>2. Change the Value field to '<new value>'<br>3. Click Save | Configuration updated successfully | high |
| TC-005 | WF-005 | Open Code Values | User logged in as <Role>, Code 'Client Type' is listed in the Manage Codes table | 1. Click on 'Client Type' to open its values | Code values displayed successfully | high |
| TC-006 | WF-006 | Create Data Table | User logged in as <Role> | 1. Navigate to Manage Data Tables<br>2. Enter '<Data Table Name>' in the Data Table Name field<br>3. Select '<Application Table Name>' from the dropdown<br>4. Check the Multi Row checkbox<br>5. Click 'Add Row' to define column<br>6. Enter '<Column Name>' in the Name field<br>7. Select '<Type>' from the Type dropdown<br>8. Enter '<Length>' in the Length field<br>9. Check Is Mandatory checkbox<br>10. Check Is Unique checkbox<br>11. Click Submit | Data table created successfully | high |
| TC-007 | WF-007 | Approve Audit Trail Entry | User logged in as <Role>, maker-checker is enabled, An entry is pending approval in the Audit Trails table | 1. Click Approve for the pending audit trail entry | Audit trail entry approved successfully | high |
| TC-008 | WF-008 | Reject Audit Trail Entry | User logged in as <Role>, maker-checker is enabled, An entry is pending rejection in the Audit Trails table | 1. Click Reject for the pending audit trail entry | Audit trail entry rejected successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Job_Name field blank when toggling active status |  | 1. Navigate to Manage Scheduler Jobs<br>2. Click on Toggle Active for a job<br>3. Leave the Job_Name field blank<br>4. Click Submit | Inline validation error appears on the Job_Name field indicating it is required | high |
| TC-010 |  | Leave the CRON_Expression field blank when editing a job |  | 1. Navigate to Manage Scheduler Jobs<br>2. Click on Edit CRON Expression for a job<br>3. Leave the CRON_Expression field blank<br>4. Click Submit | Inline validation error appears on the CRON_Expression field indicating it is required | high |
| TC-011 |  | Attempt to approve an audit trail entry when maker-checker is not enabled |  | 1. Navigate to Audit Trails<br>2. Click on Approve for a pending entry | Action is blocked; no approval occurs; the Approve button is not visible | high |
| TC-012 |  | Attempt to reject an audit trail entry when maker-checker is not enabled |  | 1. Navigate to Audit Trails<br>2. Click on Reject for a pending entry | Action is blocked; no rejection occurs; the Reject button is not visible | high |
| TC-013 |  | Leave the Data_Table_Name field blank when creating a data table |  | 1. Navigate to Manage Data Tables<br>2. Click on Create Data Table<br>3. Leave the Data_Table_Name field blank<br>4. Click Submit | Inline validation error appears on the Data_Table_Name field indicating it is required | high |
| TC-014 |  | Leave the Application_Table_Name dropdown unselected when creating a data table |  | 1. Navigate to Manage Data Tables<br>2. Click on Create Data Table<br>3. Leave the Application_Table_Name dropdown unselected<br>4. Click Submit | Inline validation error appears on the Application_Table_Name field indicating it is required | high |
| TC-015 |  | Attempt to toggle the scheduler when it is already stopped |  | 1. Navigate to Manage Scheduler Jobs<br>2. Click on Start/Stop Scheduler<br>3. Confirm the scheduler is currently stopped | Action is blocked; the scheduler remains stopped; no toggle occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (interaction_edge) | WF-001 | Rapid toggle of job active status | Job exists in the Manage Scheduler Jobs table | 1. Click the toggle for the job to set it to active<br>2. Immediately click the toggle again to set it to inactive | Job status toggled successfully; the job reflects the last toggle state in the table | medium |
| TC-017 (boundary) | WF-002 | Edit CRON Expression with valid edge case | Job exists in the Manage Scheduler Jobs table | 1. Click Edit for the job<br>2. Enter a valid CRON expression at the boundary of acceptable format<br>3. Click Submit | CRON expression updated successfully; the new expression is displayed in the table | medium |
| TC-018 (interaction_edge) | WF-003 | Rapid start/stop of the scheduler | Scheduler is currently running | 1. Click Start/Stop Scheduler to stop the scheduler<br>2. Immediately click Start/Stop Scheduler again to start the scheduler | Scheduler status toggled successfully; the scheduler reflects the last toggle state | medium |
| TC-019 (boundary) | WF-004 | Edit configuration with boundary value | Configuration exists in the Global Configuration table | 1. Click Edit for the configuration<br>2. Enter a boundary value in the Value field<br>3. Click Submit | Configuration updated successfully; the new value is displayed in the table | medium |
| TC-020 (boundary) | WF-006 | Create data table with maximum column definitions | User is on the Manage Data Tables page | 1. Enter a Data Table Name<br>2. Select an Application Table Name<br>3. Check Multi Row checkbox<br>4. Add maximum allowed entries in Column Definitions<br>5. Click Submit | Data table created successfully; the new table appears in the list | medium |
| TC-021 (interaction_edge) | WF-007 | Rapid approve/reject of audit trail entry | Audit trail entry exists and maker-checker is enabled | 1. Click Approve for the audit trail entry<br>2. Immediately click Reject for the same entry | The action reflects the last click; the entry is either approved or rejected based on the last action taken | medium |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User is redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out without being authenticated | User is not authenticated | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User remains on the current page; no session is terminated; user is not redirected to the login page | high |
| TC-003 |  | Attempt to access an authenticated page after logout | User is logged out | 1. Attempt to navigate to an authenticated page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in and on an authenticated page | 1. Click on the User Profile Icon<br>2. Select 'Log Out'<br>3. Immediately click on the User Profile Icon again<br>4. Select 'Log Out' again | Second logout attempt is blocked; user remains on the login page without any session termination error. | medium |
| TC-005 (interaction_edge) |  | Navigation after logout | User has logged out successfully | 1. Attempt to navigate to an authenticated page | User is redirected to the login page. | medium |

---
