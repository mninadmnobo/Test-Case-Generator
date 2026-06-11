# Test Cases — Mifos

Generated: 2026-06-09T09:26:36.635437Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 550 | 171 | 209 | 170 | 277 | 226 | 47 |

## Login

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User Role>, User is on the Login page | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | User is redirected to Dashboard | high |
| TC-002 | WF-002 | Login with empty required fields | User logged in as <User Role>, User is on the Login page | 1. Click Login | shows inline validation messages | medium |
| TC-003 | WF-003 | Login with invalid credentials | User logged in as <User Role>, User is on the Login page | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | shows error message | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-002 | Attempt to login with empty Username and Password fields |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Inline validation messages show for Username and Password fields indicating they are required | high |
| TC-005 | WF-003 | Attempt to login with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Page displays 'shows error message' indicating invalid credentials | high |
| TC-006 |  | Attempt to login with only the Username field filled |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Login | Inline validation messages show for Password field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Attempt login with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | Inline validation messages are shown for both Username and Password fields | medium |
| TC-008 (boundary) | WF-003 | Attempt login with a valid Username and invalid Password |  | 1. Enter a valid Username in the Username field<br>2. Enter an invalid Password in the Password field<br>3. Click the Login button | Error message shows indicating invalid credentials | medium |
| TC-009 (input_edge) |  | Enter a very long Username |  | 1. Enter a string longer than 255 characters in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | Form submission is blocked; inline validation message indicates the Username is too long | low |
| TC-010 (input_edge) |  | Enter special characters in the Username |  | 1. Enter special characters in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | Form submission is blocked; inline validation message indicates invalid characters in the Username | low |

---

## Home Page

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard from Home Page | User logged in as <Role> | 1. Click on the Dashboard button | redirects to dashboard | high |
| TC-002 | WF-002 | Search Activities on Home Page | User logged in as <Role> | 1. Enter <search term> in the Search Activity input field<br>2. Press Enter | Search results displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to access the dashboard without being logged in | User is not authenticated | 1. Navigate to the Home Page | User is redirected to the login page | high |
| TC-004 |  | Attempt to search activities without any input |  | 1. Leave the Search Activity field blank<br>2. Click Search | No search results displayed; Search Activity field is highlighted | medium |
| TC-005 | WF-001 | Attempt to access the dashboard without being logged in | User is not authenticated | 1. Click the Dashboard button | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) | WF-002 | Search Activity with long text input | User is on the Home Page | 1. Enter a very long string (200+ characters) in the Search Activity input field | Search Activity input field displays an error indicating the input is too long | low |
| TC-007 (input_edge) |  | Search Activity with special characters | User is on the Home Page | 1. Enter special characters (e.g., @#$%^&*) in the Search Activity input field | Search Activity input field displays an error indicating invalid characters | low |
| TC-008 (input_edge) |  | Search Activity with leading and trailing whitespace | User is on the Home Page | 1. Enter a string with leading and trailing spaces in the Search Activity input field | Leading/trailing whitespace is trimmed; saved value shown in the Search Activity input field has no extra spaces | low |

---

## Dashboard

Total: **11** (positive: 5, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard | User logged in as <role> | 1. Click on the 'Dashboard' button on the Home page | Dashboard is displayed with search and charts | high |
| TC-002 | WF-002 | Display Amount Pending / Disbursed with Data | User logged in as <role>, Data is available for Amount Pending / Disbursed | 1. Access the Dashboard | Amount Pending / Disbursed card shows data | medium |
| TC-003 | WF-003 | Display Amount Collected with Data | User logged in as <role>, Data is available for Amount Collected | 1. Access the Dashboard | Amount Collected card shows data | medium |
| TC-004 | WF-004 | Display Amount Pending / Disbursed with No Data | User logged in as <role>, No data is available for Amount Pending / Disbursed | 1. Access the Dashboard | Amount Pending / Disbursed card shows No Data | medium |
| TC-005 | WF-005 | Display Amount Collected with No Data | User logged in as <role>, No data is available for Amount Collected | 1. Access the Dashboard | Amount Collected card shows No Data | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-004 | Attempt to display Amount Pending / Disbursed with no data available |  | 1. Access the Dashboard<br>2. Ensure no data is available for Amount Pending / Disbursed | Amount Pending / Disbursed card shows 'No Data' | high |
| TC-007 | WF-005 | Attempt to display Amount Collected with no data available |  | 1. Access the Dashboard<br>2. Ensure no data is available for Amount Collected | Amount Collected card shows 'No Data' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Display Amount Pending / Disbursed with data available | User is on the Dashboard, Data is available for Amount Pending / Disbursed | 1. Access the Dashboard<br>2. Ensure data is available for Amount Pending / Disbursed | Amount Pending / Disbursed card shows data | medium |
| TC-009 (boundary) | WF-004 | Display Amount Pending / Disbursed with no data | User is on the Dashboard, No data is available for Amount Pending / Disbursed | 1. Access the Dashboard<br>2. Ensure no data is available for Amount Pending / Disbursed | Amount Pending / Disbursed card shows No Data | medium |
| TC-010 (boundary) | WF-003 | Display Amount Collected with data available | User is on the Dashboard, Data is available for Amount Collected | 1. Access the Dashboard<br>2. Ensure data is available for Amount Collected | Amount Collected card shows data | medium |
| TC-011 (boundary) | WF-005 | Display Amount Collected with no data | User is on the Dashboard, No data is available for Amount Collected | 1. Access the Dashboard<br>2. Ensure no data is available for Amount Collected | Amount Collected card shows No Data | medium |

---

## Global Search

Total: **12** (positive: 4, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field | User logged in as <Role> | 1. Click the Search Icon in the top toolbar | The search input field is opened | high |
| TC-002 | WF-002 | Search with results | User logged in as <Role>, Search input field is open | 1. Enter <valid search term> in the Search Input field | Searches across Clients, Groups, Loans, and Savings accounts | high |
| TC-003 | WF-003 | Select search result | User logged in as <Role>, Search input field is open, Results are available | 1. Enter <valid search term> in the Search Input field<br>2. Select a result from the Search Results dropdown | Navigates to the corresponding detail page | high |
| TC-004 | WF-004 | No results found | User logged in as <Role>, Search input field is open | 1. Enter <invalid search term> in the Search Input field | No results found | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Unauthenticated user attempts to open search input field |  | 1. Attempt to click on the Search Icon | User is redirected to the login page; search input field does not open | high |
| TC-006 | WF-004 | Search with no results available |  | 1. Click on the Search Icon<br>2. Enter <any search term> in the Search Input<br>3. Submit the search | Search Results dropdown displays 'No results found' | high |
| TC-007 |  | Search with invalid input format |  | 1. Click on the Search Icon<br>2. Enter <invalid search term> in the Search Input<br>3. Submit the search | Search Results dropdown displays 'No results found' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Search with partial match at the edge of valid input | User is logged in | 1. Click on the Search Icon<br>2. Enter a partial string that matches the beginning of a valid entity name | Search results dropdown displays matching entities grouped by entity type | medium |
| TC-009 (boundary) | WF-002 | Search with case sensitivity edge case | User is logged in | 1. Click on the Search Icon<br>2. Enter a string in a different case than the stored entity names | Search results dropdown displays matching entities regardless of case | medium |
| TC-010 (boundary) | WF-004 | Search with no results edge case | User is logged in | 1. Click on the Search Icon<br>2. Enter a string that does not match any entity | Search results dropdown shows 'No results found' message | medium |
| TC-011 (input_edge) |  | Search with long input string | User is logged in | 1. Click on the Search Icon<br>2. Enter a very long string (200+ characters) in the search input | Search input accepts the long string; either results are returned or a message indicates no results | low |
| TC-012 (input_edge) |  | Search with special characters | User is logged in | 1. Click on the Search Icon<br>2. Enter a string with special characters (e.g., @#$%^&*) | Search input accepts the special characters; either results are returned or a message indicates no results | low |

---

## Client Management

Total: **31** (positive: 14, negative: 10, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Import Client opens Bulk Import page | User logged in as <Role> | 1. Click Import Client button | opens Bulk Import page | high |
| TC-002 | WF-002 | Create Client submits the form successfully | User logged in as <Role> | 1. Click Create Client button<br>2. Enter <Office> in the Office field<br>3. Enter <First Name> in the First Name field<br>4. Enter <Last Name> in the Last Name field<br>5. Enter <External ID> in the External ID field<br>6. Enter <Submitted On> in the Submitted On field<br>7. Click Submit | creates client in Pending status | high |
| TC-003 | WF-003 | Activate Client changes status to Active | User logged in as <Role>, Client is in Pending status | 1. Click on the client name to view details<br>2. Click Activate button<br>3. Enter <Activation Date> in the Activation Date field<br>4. Click Confirm on the Activation dialog | Client activated | medium |
| TC-004 | WF-004 | Edit Client updates details successfully | User logged in as <Role>, Client is in Pending status | 1. Click on the client name to view details<br>2. Click Edit button<br>3. Update <Field> with <New Value><br>4. Click Save | Client details updated | medium |
| TC-005 | WF-005 | Reject Client successfully | User logged in as <Role>, Client is in Pending status | 1. Click on the client name to view details<br>2. Click Reject button<br>3. Enter <Reason> in the Reason field<br>4. Click Confirm on the Reject dialog | Client rejected | medium |
| TC-006 | WF-006 | Withdraw Client successfully | User logged in as <Role>, Client is in Pending status | 1. Click on the client name to view details<br>2. Click Withdraw button<br>3. Enter <Reason> in the Reason field<br>4. Click Confirm on the Withdraw dialog | Client withdrawn | medium |
| TC-007 | WF-007 | Edit Client (Active) updates details successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click Edit button<br>3. Update <Field> with <New Value><br>4. Click Save | Client details updated | medium |
| TC-008 | WF-008 | Transfer Client to another office successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click Transfer Client button<br>3. Enter <Destination Office> in the Destination Office field<br>4. Click Confirm on the Transfer dialog | Client transferred | medium |
| TC-009 | WF-009 | Close Client successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click Close button<br>3. Enter <Closure Reason> in the Closure Reason field<br>4. Click Confirm on the Close dialog | Client closed | medium |
| TC-010 | WF-010 | Add Charge to Client successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click Add Charge button<br>3. Enter <Charge Details> in the Charge field<br>4. Click Confirm on the Add Charge dialog | Charge added | medium |
| TC-011 | WF-011 | Create New Loan for Client successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click New Loan button<br>3. Enter <Loan Details> in the Loan field<br>4. Click Confirm on the New Loan dialog | Loan created | medium |
| TC-012 | WF-012 | Create New Savings Account for Client successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click New Savings button<br>3. Enter <Savings Details> in the Savings field<br>4. Click Confirm on the New Savings dialog | Savings account created | medium |
| TC-013 | WF-013 | Create New Share Account for Client successfully | User logged in as <Role>, Client is in Active status | 1. Click on the client name to view details<br>2. Click New Share Account button<br>3. Enter <Share Account Details> in the Share Account field<br>4. Click Confirm on the New Share Account dialog | Share account created | medium |
| TC-014 | WF-014 | Reactivate Client successfully | User logged in as <Role>, Client is in Closed status | 1. Click on the client name to view details<br>2. Click Reactivate button<br>3. Click Confirm on the Reactivate dialog | Client reactivated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 | WF-002 | Leave the required Office field blank while creating a client |  | 1. Open the Create Client wizard<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-016 | WF-002 | Leave the required First Name field blank while creating a client |  | 1. Open the Create Client wizard<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-017 | WF-002 | Leave the required Last Name field blank while creating a client |  | 1. Open the Create Client wizard<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-018 | WF-002 | Leave the required External ID field blank while creating a client |  | 1. Open the Create Client wizard<br>2. Leave the External ID field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the External ID field indicating it is required | high |
| TC-019 | WF-003 | Attempt to activate a client with Activation Date before submission date | Client is in Pending status | 1. Open the Client Detail page for the client<br>2. Click Activate<br>3. Enter an Activation Date that is before the Submitted On date<br>4. Click Submit | Inline validation error appears on the Activation Date field indicating it must not be before submission date | high |
| TC-020 | WF-005 | Leave the required Reason field blank while rejecting a client | Client is in Pending status | 1. Open the Client Detail page for the client<br>2. Click Reject<br>3. Leave the Reason field blank<br>4. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-021 | WF-006 | Leave the required Reason field blank while withdrawing a client | Client is in Pending status | 1. Open the Client Detail page for the client<br>2. Click Withdraw<br>3. Leave the Reason field blank<br>4. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-022 | WF-008 | Attempt to transfer a client to the same office | Client is in Active status | 1. Open the Client Detail page for the client<br>2. Click Transfer Client<br>3. Select the same office as the current office<br>4. Click Submit | Inline validation error appears on the Destination Office field indicating same office is blocked | high |
| TC-023 | WF-009 | Attempt to close a client with active accounts | Client is in Active status | 1. Open the Client Detail page for the client<br>2. Click Close<br>3. Fill in the Closure Reason<br>4. Click Submit | Inline validation error appears on the Closure Reason field indicating cannot close with active accounts | high |
| TC-024 |  | Unauthenticated user attempts to access the Create Client page |  | 1. Navigate to the Create Client page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 (boundary) | WF-003 | Activation Date is exactly the same as Submission Date | A client is in Pending status with a known submission date | 1. Navigate to the Client Detail page of the pending client<br>2. Click on the Activate button<br>3. Enter the Activation Date as the same date as Submitted On<br>4. Click Submit | Client is activated successfully; status changes to Active | medium |
| TC-026 (boundary) | WF-003 | Activation Date is one day before Submission Date | A client is in Pending status with a known submission date | 1. Navigate to the Client Detail page of the pending client<br>2. Click on the Activate button<br>3. Enter the Activation Date as one day before Submitted On<br>4. Click Submit | Action is blocked; error shown indicating 'Activation Date must not be before submission date' | medium |
| TC-027 (boundary) | WF-008 | Transfer Client to the same office | A client is in Active status and is associated with an office | 1. Navigate to the Client Detail page of the active client<br>2. Click on the Transfer Client button<br>3. Select the same office as the current office<br>4. Click Submit | Action is blocked; error shown indicating 'same office is blocked' | medium |
| TC-028 (boundary) | WF-009 | Close Client with active accounts | A client is in Active status with an active account | 1. Navigate to the Client Detail page of the active client<br>2. Click on the Close button<br>3. Enter a Closure Reason<br>4. Click Submit | Action is blocked; error shown indicating 'cannot close with active accounts' | medium |
| TC-029 (input_edge) |  | Enter a very long name in the search field |  | 1. Go to the Clients page<br>2. Enter a string of 200+ characters in the search field<br>3. Click Search | Search results display as per system handling of long strings; may be truncated or show an error | low |
| TC-030 (input_edge) |  | Enter special characters in the search field |  | 1. Go to the Clients page<br>2. Enter special characters (e.g., !@#$%^&*) in the search field<br>3. Click Search | Search results display as per system handling of special characters; may show an error or return no results | low |
| TC-031 (input_edge) |  | Enter leading and trailing whitespace in the search field |  | 1. Go to the Clients page<br>2. Enter a name with leading and trailing spaces in the search field<br>3. Click Search | Search results display trimmed value; leading/trailing whitespace is removed | low |

---

## Group Management

Total: **22** (positive: 8, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-004 | Create a new group successfully | User logged in as <Role> | 1. Click 'Create New Group' button<br>2. Enter <valid group name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | creates the group | high |
| TC-002 | WF-003 | Initiate group import process | User logged in as <Role> | 1. Click 'Import Groups' button | Import process initiated | medium |
| TC-003 | WF-002 | Bulk import groups successfully | User logged in as <Role> | 1. Click 'Bulk Import Groups' button<br>2. Select <valid file> using the File Picker<br>3. Click Upload | Groups imported successfully | high |
| TC-004 | WF-005 | Activate a group successfully | User logged in as <Role>, Group is in 'Pending' status | 1. Click Activate button | Group activated | medium |
| TC-005 | WF-006 | Edit group details successfully | User logged in as <Role>, Group is in 'Active' status | 1. Click Edit button<br>2. Change <field> to <new value><br>3. Click Submit | Group details edited | medium |
| TC-006 | WF-007 | Close a group successfully | User logged in as <Role>, Group is in 'Active' status | 1. Click Close button | Group closed | medium |
| TC-007 | WF-008 | Assign staff to a group successfully | User logged in as <Role>, Group is in 'Active' status | 1. Click Assign Staff button<br>2. Select <valid staff member> from the dropdown<br>3. Click Submit | Staff assigned to group | medium |
| TC-008 | WF-009 | Transfer clients from a group successfully | User logged in as <Role>, Group is in 'Active' status | 1. Click Transfer Clients button<br>2. Select <valid clients> to transfer<br>3. Click Submit | Clients transferred from group | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-004 | Leave the Name field blank and submit |  | 1. Leave the Name field blank<br>2. Fill the Office field with a valid value<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 | WF-004 | Leave the Office field blank and submit |  | 1. Fill the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 | WF-004 | Leave the Submitted On field blank and submit |  | 1. Fill the Name field with a valid value<br>2. Fill the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-012 | WF-002 | Leave the File Picker field blank and upload |  | 1. Leave the File Picker field blank<br>2. Click Upload | Inline validation error appears on the File Picker field indicating it is required | high |
| TC-013 | WF-005 | Attempt to activate a group without required fields filled |  | 1. Open the Group Detail page<br>2. Click Activate | No action occurs; the group remains inactive | medium |
| TC-014 | WF-007 | Attempt to close a group without required fields filled |  | 1. Open the Group Detail page<br>2. Click Close | No action occurs; the group remains open | medium |
| TC-015 | WF-008 | Attempt to assign staff without required fields filled |  | 1. Open the Group Detail page<br>2. Click Assign Staff | No action occurs; staff remains unassigned | medium |
| TC-016 | WF-009 | Attempt to transfer clients from a group without required fields filled |  | 1. Open the Group Detail page<br>2. Click Transfer Clients | No action occurs; clients remain in the group | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-004 | Submit group creation form with maximum length name | User is on the Create Group form | 1. Enter maximum length string in the Name field<br>2. Enter valid Office value<br>3. Enter valid Submitted On date<br>4. Click Submit | Form submits successfully; entity is created with the maximum length name | medium |
| TC-018 (boundary) | WF-004 | Submit group creation form with one character less than minimum length name | User is on the Create Group form | 1. Enter one character less than minimum length in the Name field<br>2. Enter valid Office value<br>3. Enter valid Submitted On date<br>4. Click Submit | Submission is blocked; inline error shown indicating the name is too short | medium |
| TC-019 (boundary) | WF-002 | Upload file exactly at size limit for bulk import | User is on the Bulk Import Groups page | 1. Select a file exactly at the size limit in the File Picker<br>2. Click Upload | File uploads successfully; import process initiated | medium |
| TC-020 (boundary) | WF-002 | Upload file one byte over the size limit for bulk import | User is on the Bulk Import Groups page | 1. Select a file one byte over the size limit in the File Picker<br>2. Click Upload | Submission is blocked; visible error shown indicating the file exceeds the size limit | medium |
| TC-021 (input_edge) |  | Enter a very long string in the Name field | User is on the Create Group form | 1. Enter a very long string (200+ characters) in the Name field<br>2. Enter valid Office value<br>3. Enter valid Submitted On date<br>4. Click Submit | Form submission is blocked; inline error shown indicating the name is too long | low |
| TC-022 (input_edge) |  | Enter special characters in the Office field | User is on the Create Group form | 1. Enter special characters in the Office field<br>2. Enter valid Name<br>3. Enter valid Submitted On date<br>4. Click Submit | Submission is blocked; inline error shown indicating invalid characters in the Office field | low |

---

## Center Management

Total: **18** (positive: 4, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Center Details | User logged in as <role> | 1. Navigate to the Centers page<br>2. Click on the Name link of a center | Displays center details | high |
| TC-002 | WF-002 | Import Centers | User logged in as <role>, User is on the Bulk Import Centers page | 1. Click 'Upload' to select a valid file<br>2. Select a <valid file type> from the OS dialog<br>3. Click 'Submit' to import centers | Centers imported successfully | high |
| TC-003 | WF-003 | Create Center | User logged in as <role>, User is on the Create Center form | 1. Enter <valid center name> in the Name field<br>2. Enter <valid office name> in the Office field<br>3. Enter <valid date> in the Submitted On field<br>4. Click 'Submit' | creates the center | high |
| TC-004 | WF-004 | Generate Collection Sheet | User logged in as <role>, User is on the Center Detail page | 1. Click on the Collection Sheet Feature button | generates a sheet showing all groups and their clients | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill the Office field with a valid value<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the Office field blank and submit the Create Center form |  | 1. Fill the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 | WF-003 | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill the Name field with a valid value<br>2. Fill the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-008 | WF-002 | Leave the file upload field blank and submit the Bulk Import Centers form |  | 1. Leave the file upload field blank<br>2. Click Import Center | Inline validation error appears on the file_upload field indicating it is required | high |
| TC-009 | WF-004 | Attempt to generate a collection sheet without any groups |  | 1. Navigate to the Center Detail page<br>2. Click on the Collection Sheet Feature | Status remains unchanged; no sheet is generated; error message displayed indicating no groups available | medium |
| TC-010 |  | Attempt to view center details without proper authentication |  | 1. Attempt to access the Center Detail page without logging in | User is redirected to the login page | high |
| TC-011 | WF-003 | Attempt to create a center with an invalid date format in the Submitted On field |  | 1. Fill the Name field with a valid value<br>2. Fill the Office field with a valid value<br>3. Enter <invalid date format> in the Submitted On field<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it must be a valid date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-003 | Submit Create Center form with minimum required fields filled |  | 1. Enter valid value in the Name field<br>2. Enter valid value in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum required fields filled | medium |
| TC-013 (boundary) | WF-003 | Submit Create Center form with missing required fields |  | 1. Leave Name field empty<br>2. Leave Office field empty<br>3. Click Submit | Form submission is blocked; inline error shown indicating required fields are missing | medium |
| TC-014 (boundary) | WF-002 | Upload file for Bulk Import Centers at exact size limit |  | 1. Upload a file that meets the size requirements for import<br>2. Click Import Center | File upload succeeds; centers imported successfully | medium |
| TC-015 (boundary) | WF-002 | Upload file for Bulk Import Centers exceeding size limit |  | 1. Upload a file that exceeds the size limit for import<br>2. Click Import Center | File upload is blocked; visible error shown naming the size constraint | medium |
| TC-016 (input_edge) |  | Enter long text in Name field |  | 1. Enter a string of 200+ characters in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; saved value in the detail page shows the long text correctly | low |
| TC-017 (input_edge) |  | Enter special characters in Office field |  | 1. Enter special characters in the Office field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; saved value in the detail page shows the special characters correctly | low |
| TC-018 (input_edge) |  | Enter value with leading/trailing whitespace in Name field |  | 1. Enter '   Center Name   ' in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Loan Products

Total: **25** (positive: 8, negative: 10, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Loan Product Details | User logged in as <Role> | 1. Click on an existing product name in the Loan Products Table | opens detail view | high |
| TC-002 | WF-002 | Edit Loan Product | User logged in as <Role> | 1. Click on an existing product name in the Loan Products Table<br>2. Click on the Edit option | opens edit interface | high |
| TC-003 | WF-003 | Create Loan Product - Step 1 Submit | User logged in as <Role>, Create Loan Product button is visible | 1. Click on the + Create Loan Product button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click Next | proceeds to Step 2 | high |
| TC-004 | WF-004 | Create Loan Product - Step 2 Submit | User logged in as <Role>, Create Loan Product button is visible, Step 1 is completed | 1. Select <Currency> from the Currency dropdown<br>2. Enter <Principal Amount> in the Principal Amount field<br>3. Click Next | proceeds to Step 3 | high |
| TC-005 | WF-005 | Create Loan Product - Step 3 Submit | User logged in as <Role>, Create Loan Product button is visible, Step 2 is completed | 1. Select <Amortization Method> from the Amortization Method dropdown<br>2. Select <Interest Method> from the Interest Method dropdown<br>3. Click Next | proceeds to Step 4 | high |
| TC-006 | WF-006 | Create Loan Product - Step 4 Submit | User logged in as <Role>, Create Loan Product button is visible, Step 3 is completed | 1. Enter <Number of Repayments> in the Number of Repayments field<br>2. Select <Repaid Every> from the Repaid Every dropdown<br>3. Enter <Nominal Interest Rate> in the Nominal Interest Rate field<br>4. Click Next | proceeds to Step 5 | high |
| TC-007 | WF-007 | Create Loan Product - Step 5 Submit | User logged in as <Role>, Create Loan Product button is visible, Step 4 is completed | 1. Select <Predefined Charges> from the predefined charges interface<br>2. Click Next | proceeds to Step 6 | high |
| TC-008 | WF-008 | Create Loan Product - Step 6 Submit | User logged in as <Role>, Create Loan Product button is visible, Step 5 is completed | 1. Select <Accounting Method> from the Accounting Method radio options<br>2. Click Submit | Loan product created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-003 | Leave Product Name field blank and submit |  | 1. Leave the Product Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-010 | WF-003 | Leave Short Name field blank and submit |  | 1. Leave the Short Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-011 | WF-004 | Leave Currency field blank and submit |  | 1. Leave the Currency field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-012 | WF-004 | Submit with all required fields empty in Step 2 |  | 1. Leave the Currency field blank<br>2. Leave the Principal Amount field blank<br>3. Click Submit | Inline validation error appears on the Currency field indicating it is required; Inline validation error appears on the Principal Amount field indicating it is required | high |
| TC-013 | WF-006 | Leave Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-014 | WF-006 | Leave Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-015 | WF-008 | Leave Accounting Method field blank and submit |  | 1. Leave the Accounting Method field blank<br>2. Click Submit | Inline validation error appears on the Accounting Method field indicating it is required | high |
| TC-016 | WF-008 | Select 'None' for Accounting Method and submit |  | 1. Select 'None' for Accounting Method<br>2. Click Submit | GL account dropdown mappings are not visible; Loan product is not created | medium |
| TC-017 | WF-008 | Enter Principal Amount below minimum and submit |  | 1. Enter <amount below minimum> in the Principal Amount field<br>2. Click Submit | Inline validation error appears on the Principal Amount field indicating minimum value required | medium |
| TC-018 | WF-008 | Enter Number of Repayments below minimum and submit |  | 1. Enter <amount below minimum> in the Number of Repayments field<br>2. Click Submit | Inline validation error appears on the Number of Repayments field indicating minimum value required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-003 | Submit Step 1 with minimum required values | User is on Step 1 of the Create Loan Product wizard | 1. Enter minimum allowed value in the Product_Name field<br>2. Enter minimum allowed value in the Short_Name field<br>3. Click Submit | Form submits successfully; proceeds to Step 2 | medium |
| TC-020 (boundary) | WF-003 | Submit Step 1 with one required field missing | User is on Step 1 of the Create Loan Product wizard | 1. Enter minimum allowed value in the Product_Name field<br>2. Leave Short_Name field empty<br>3. Click Submit | Inline validation error shown for Short_Name field; submission is blocked | medium |
| TC-021 (boundary) | WF-004 | Submit Step 2 with Principal Amount at maximum value | User is on Step 2 of the Create Loan Product wizard | 1. Select a Currency<br>2. Enter maximum allowed value in the Principal_Amount field<br>3. Click Submit | Form submits successfully; proceeds to Step 3 | medium |
| TC-022 (boundary) | WF-004 | Submit Step 2 with Principal Amount exceeding maximum value | User is on Step 2 of the Create Loan Product wizard | 1. Select a Currency<br>2. Enter one unit above the maximum allowed value in the Principal_Amount field<br>3. Click Submit | Inline validation error shown for Principal_Amount field; submission is blocked | medium |
| TC-023 (boundary) | WF-006 | Submit Step 4 with Number of Repayments at minimum value | User is on Step 4 of the Create Loan Product wizard | 1. Enter minimum allowed value in the Number_of_Repayments field<br>2. Select Repaid Every frequency<br>3. Enter minimum allowed value in the Nominal_Interest_Rate field<br>4. Click Submit | Form submits successfully; proceeds to Step 5 | medium |
| TC-024 (boundary) | WF-006 | Submit Step 4 with Nominal Interest Rate exceeding maximum value | User is on Step 4 of the Create Loan Product wizard | 1. Enter minimum allowed value in the Number_of_Repayments field<br>2. Select Repaid Every frequency<br>3. Enter one unit above the maximum allowed value in the Nominal_Interest_Rate field<br>4. Click Submit | Inline validation error shown for Nominal_Interest_Rate field; submission is blocked | medium |
| TC-025 (interaction_edge) | WF-008 | Rapid submission after creating a loan product | User has just successfully created a loan product | 1. Click the browser back button<br>2. Click Submit again | User is redirected to the detail page without a second entity being created | low |

---

## Savings Products

Total: **20** (positive: 9, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Savings Product Details | User logged in as <Role>, At least one savings product exists | 1. Click on the Name link of a savings product in the data table | View details of the savings product | high |
| TC-002 | WF-002 | Edit Savings Product | User logged in as <Role>, At least one savings product exists | 1. Click on the Edit action of a savings product in the data table | Edit the savings product details | high |
| TC-003 | WF-003 | Create a New Savings Product | User logged in as <Role> | 1. Click the '+ Create Savings Product' button | opens stepper wizard | high |
| TC-004 | WF-004 | Submit Details Step in Savings Product Stepper | User logged in as <Role>, User is on the Details step of the Savings Product Stepper | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Click Submit | Proceed to Currency step | high |
| TC-005 | WF-005 | Submit Currency Step in Savings Product Stepper | User logged in as <Role>, User is on the Currency step of the Savings Product Stepper | 1. Click Submit | Proceed to Terms step | medium |
| TC-006 | WF-006 | Submit Terms Step in Savings Product Stepper | User logged in as <Role>, User is on the Terms step of the Savings Product Stepper | 1. Click Submit | Proceed to Settings step | medium |
| TC-007 | WF-007 | Submit Settings Step in Savings Product Stepper | User logged in as <Role>, User is on the Settings step of the Savings Product Stepper | 1. Click Submit | Proceed to Charges step | medium |
| TC-008 | WF-008 | Submit Charges Step in Savings Product Stepper | User logged in as <Role>, User is on the Charges step of the Savings Product Stepper | 1. Click Submit | Proceed to Accounting step | medium |
| TC-009 | WF-009 | Submit Accounting Step in Savings Product Stepper | User logged in as <Role>, User is on the Accounting step of the Savings Product Stepper | 1. Click Submit | Savings product created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-003 | Attempt to create a savings product with required fields empty |  | 1. Leave the Product Name field blank<br>2. Leave the Short Name field blank<br>3. Click Submit | Form does not submit; Product Name field displays an error: 'This field is required'; Short Name field displays an error: 'This field is required' | high |
| TC-011 | WF-004 | Submit Details Step with required fields empty |  | 1. Click Submit on the Details step without filling any required fields | Form does not submit; Product Name field displays an error: 'This field is required'; Short Name field displays an error: 'This field is required' | high |
| TC-012 | WF-009 | Attempt to submit Accounting Step without selecting Accounting Method |  | 1. Click Submit on the Accounting step without selecting an Accounting Method | Form does not submit; Accounting Method field displays an error: 'This field is required' | high |
| TC-013 | WF-011 | Submit Deposit Term Step with Minimum Deposit Term empty |  | 1. Leave the Minimum Deposit Term field blank<br>2. Leave the Maximum Deposit Term field blank<br>3. Click Submit | Form does not submit; Minimum Deposit Term field displays an error: 'This field is required'; Maximum Deposit Term field displays an error: 'This field is required' | high |
| TC-014 | WF-013 | Submit Additional Features Step with required fields empty |  | 1. Leave the Mandatory Recommended Deposit Amount field blank<br>2. Leave the Is Mandatory Deposit field unchecked<br>3. Leave the Allow Withdrawal field unchecked<br>4. Leave the Adjust Advance Towards Future Payments field unchecked<br>5. Click Submit | Form does not submit; Mandatory Recommended Deposit Amount field displays an error: 'This field is required'; Is Mandatory Deposit field displays an error: 'This field is required'; Allow Withdrawal field displays an error: 'This field is required'; Adjust Advance Towards Future Payments field displays an error: 'This field is required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-004 | Submit Details Step with minimum character length for Product Name | User is on the Details step of the Savings Product Stepper | 1. Enter exactly 1 character in the Product Name field<br>2. Enter a valid Short Name<br>3. Click Submit | Form submits successfully; proceeds to Currency step | medium |
| TC-016 (boundary) | WF-004 | Submit Details Step with one character less than minimum for Product Name | User is on the Details step of the Savings Product Stepper | 1. Enter 0 characters in the Product Name field<br>2. Enter a valid Short Name<br>3. Click Submit | Submission is blocked; error message displayed for Product Name being required | medium |
| TC-017 (boundary) | WF-011 | Submit Deposit Term Step with Minimum Deposit Term equal to Maximum Deposit Term | User is on the Deposit Term step of the Fixed Deposit Products Stepper | 1. Enter the same value for Minimum Deposit Term and Maximum Deposit Term<br>2. Enter a valid Minimum Deposit Amount<br>3. Click Submit | Form submits successfully; proceeds to Interest Rate Chart step | medium |
| TC-018 (boundary) | WF-011 | Submit Deposit Term Step with Minimum Deposit Term one less than Maximum Deposit Term | User is on the Deposit Term step of the Fixed Deposit Products Stepper | 1. Enter a value for Minimum Deposit Term that is one less than the Maximum Deposit Term<br>2. Enter a valid Minimum Deposit Amount<br>3. Click Submit | Form submits successfully; proceeds to Interest Rate Chart step | medium |
| TC-019 (boundary) | WF-008 | Submit Charges Step with maximum allowed entries in Charges | User is on the Charges step of the Savings Product Stepper | 1. Add maximum allowed entries to the Charges field<br>2. Click Submit | Form submits successfully; proceeds to Accounting step | medium |
| TC-020 (boundary) | WF-008 | Submit Charges Step with one more entry than maximum allowed in Charges | User is on the Charges step of the Savings Product Stepper | 1. Add maximum allowed entries + 1 to the Charges field<br>2. Click Submit | Submission is blocked; error message displayed indicating maximum entries exceeded | medium |

---

## Share Products

Total: **25** (positive: 10, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Product Details | User logged in as <Role> | 1. Click on the Product Name in the Share Products Table | Product details displayed | high |
| TC-002 | WF-002 | Edit Product | User logged in as <Role>, Product exists in the Share Products Table | 1. Click on the Edit action for the selected product | Product edit form displayed | high |
| TC-003 | WF-003 | Delete Product | User logged in as <Role>, Product exists in the Share Products Table | 1. Click on the Delete action for the selected product<br>2. Confirm deletion | Product deleted successfully | high |
| TC-004 | WF-004 | Create Share Product - Step 1 | User logged in as <Role> | 1. Click the '+ Create Share Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Enter <valid description> in the Description field | Proceed to Step 2 | high |
| TC-005 | WF-005 | Create Share Product - Step 2 | User logged in as <Role>, Step 1 completed successfully | 1. Select <valid currency> from the Currency dropdown<br>2. Enter <valid number> in the Decimal Places field<br>3. Enter <valid number> in the Currency In Multiples Of field | Proceed to Step 3 | high |
| TC-006 | WF-006 | Create Share Product - Step 3 | User logged in as <Role>, Step 2 completed successfully | 1. Enter <valid number> in the Total Number of Shares field<br>2. Enter <valid number> in the Nominal Unit Price field | Proceed to Step 4 | high |
| TC-007 | WF-007 | Create Share Product - Step 4 | User logged in as <Role>, Step 3 completed successfully | 1. Check the Allow Dividends for Inactive Clients checkbox<br>2. Enter <valid number> in the Minimum Shares per Client field | Proceed to Step 5 | high |
| TC-008 | WF-008 | Create Share Product - Step 5 | User logged in as <Role>, Step 4 completed successfully | 1. Click 'Add Row' in the Market Price table<br>2. Enter <valid date> in the From Date field<br>3. Enter <valid number> in the Share Value field | Proceed to Step 6 | high |
| TC-009 | WF-009 | Create Share Product - Step 6 | User logged in as <Role>, Step 5 completed successfully | 1. Enter <valid charges> in the Charges field | Proceed to Step 7 | high |
| TC-010 | WF-010 | Create Share Product - Step 7 | User logged in as <Role>, Step 6 completed successfully | 1. Select 'Cash-based' from the Accounting Method radio options<br>2. Enter <valid share reference> in the Share Reference field | Share product created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-004 | Leave the Product Name field blank and submit |  | 1. Leave the Product Name field blank<br>2. Fill the Short Name field with a valid value<br>3. Fill the Description field with a valid value<br>4. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-012 | WF-004 | Leave the Short Name field blank and submit |  | 1. Leave the Short Name field blank<br>2. Fill the Product Name field with a valid value<br>3. Fill the Description field with a valid value<br>4. Click Submit | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-013 | WF-004 | Leave the Description field blank and submit |  | 1. Leave the Description field blank<br>2. Fill the Product Name field with a valid value<br>3. Fill the Short Name field with a valid value<br>4. Click Submit | Inline validation error appears on the Description field indicating it is required | high |
| TC-014 | WF-006 | Leave the Total Number of Shares field blank and submit |  | 1. Fill the Total Number of Shares field with an empty value<br>2. Fill the Shares to be Issued field with a valid value<br>3. Fill the Nominal Unit Price field with a valid value<br>4. Click Submit | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-015 | WF-006 | Leave the Nominal Unit Price field blank and submit |  | 1. Fill the Nominal Unit Price field with an empty value<br>2. Fill the Total Number of Shares field with a valid value<br>3. Fill the Shares to be Issued field with a valid value<br>4. Click Submit | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-016 | WF-010 | Attempt to create a share product without filling any required fields |  | 1. Click on the Create Share Product button<br>2. Leave all required fields blank in Step 1<br>3. Click Submit | Form does not submit; Share product is not created; error shown on Product Name, Short Name, and Description fields | high |
| TC-017 | WF-010 | Attempt to create a share product with invalid Total Number of Shares |  | 1. Click on the Create Share Product button<br>2. Fill the Product Name field with a valid value<br>3. Fill the Short Name field with a valid value<br>4. Fill the Description field with a valid value<br>5. Enter <non-numeric value> in the Total Number of Shares field<br>6. Fill the Nominal Unit Price field with a valid value<br>7. Click Submit | Inline validation error appears on the Total Number of Shares field indicating it must be a number | medium |
| TC-018 | WF-010 | Attempt to create a share product with invalid Nominal Unit Price |  | 1. Click on the Create Share Product button<br>2. Fill the Product Name field with a valid value<br>3. Fill the Short Name field with a valid value<br>4. Fill the Description field with a valid value<br>5. Fill the Total Number of Shares field with a valid value<br>6. Enter <non-numeric value> in the Nominal Unit Price field<br>7. Click Submit | Inline validation error appears on the Nominal Unit Price field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-004 | Enter valid Product Name, Short Name, and Description |  | 1. Enter valid value in the Product Name field<br>2. Enter valid value in the Short Name field<br>3. Enter valid value in the Description field<br>4. Click Submit | Form submits successfully; proceeds to Step 2 | medium |
| TC-020 (boundary) | WF-004 | Enter empty Product Name, Short Name, and Description |  | 1. Leave Product Name field empty<br>2. Leave Short Name field empty<br>3. Leave Description field empty<br>4. Click Submit | Form is blocked; inline errors shown for required fields | medium |
| TC-021 (boundary) | WF-006 | Enter valid Total Number of Shares and Nominal Unit Price |  | 1. Enter valid value in the Total Number of Shares field<br>2. Enter valid value in the Nominal Unit Price field<br>3. Click Submit | Form submits successfully; proceeds to Step 4 | medium |
| TC-022 (boundary) | WF-006 | Enter zero in Total Number of Shares |  | 1. Enter 0 in the Total Number of Shares field<br>2. Enter valid value in the Nominal Unit Price field<br>3. Click Submit | Form is blocked; inline error shown indicating Total Number of Shares must be greater than zero | medium |
| TC-023 (interaction_edge) | WF-010 | Rapidly submit the final step after successful creation | Successfully completed all previous steps | 1. Click Submit on Step 7<br>2. Immediately click Submit again | Second submission attempt is blocked; user remains on the final step with a message indicating the product has already been created | low |
| TC-024 (input_edge) |  | Enter a very long string in Product Name |  | 1. Enter a string of 200+ characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; saved value shows the long string correctly | low |
| TC-025 (input_edge) |  | Enter special characters in Short Name |  | 1. Enter special characters in the Short Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; saved value shows special characters correctly | low |

---

## Charges

Total: **15** (positive: 3, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Charge Creation Form with valid data | User logged in as <Role> | 1. Click '+ Create Charge' button<br>2. Enter <valid charge name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Enter <valid currency> in the Currency field<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <valid amount> in the Amount field<br>8. Click Submit | A success notification is displayed; the Charges Table shows the new charge definition | high |
| TC-002 | WF-002 | Edit Charge details | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click on the Name link of an existing charge in the Charges Table<br>2. Click Edit<br>3. Modify <field> with <new value><br>4. Click Submit | Charge details opened for editing | medium |
| TC-003 | WF-003 | Delete Charge | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click on the Name link of an existing charge in the Charges Table<br>2. Click Delete<br>3. Confirm deletion | Charge deleted successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Charge Name blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Charge Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Charge Applies To blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Charge Applies To field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-006 | WF-001 | Leave Currency blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-007 | WF-001 | Leave Charge Time Type blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Charge Time Type field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Time Type field indicating it is required | high |
| TC-008 | WF-001 | Leave Charge Calculation Type blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Charge Calculation Type field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Calculation Type field indicating it is required | high |
| TC-009 | WF-001 | Leave Amount blank and submit |  | 1. Open the Charge Creation Form<br>2. Leave the Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-010 | WF-001 | Submit with all required fields empty |  | 1. Open the Charge Creation Form<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Charge Name, Charge Applies To, Currency, Charge Time Type, Charge Calculation Type, and Amount fields display errors indicating they are required | high |
| TC-011 | WF-001 | Select an invalid option in Charge Applies To |  | 1. Open the Charge Creation Form<br>2. Select an invalid option in the Charge Applies To field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form does not submit; Charge Applies To field displays an error indicating the selected option is invalid | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Submit Charge Creation Form with minimum valid Amount | User is on the Charge Creation Form | 1. Enter a valid Charge Name in the Charge_Name field<br>2. Select a valid option from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a valid option from the Charge_Time_Type dropdown<br>5. Select a valid option from the Charge_Calculation_Type dropdown<br>6. Enter exactly <minimum valid Amount> in the Amount field<br>7. Click Submit | Form submits successfully; charge definition is created with the <minimum valid Amount> | medium |
| TC-013 (boundary) | WF-001 | Submit Charge Creation Form with Amount below minimum | User is on the Charge Creation Form | 1. Enter a valid Charge Name in the Charge_Name field<br>2. Select a valid option from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a valid option from the Charge_Time_Type dropdown<br>5. Select a valid option from the Charge_Calculation_Type dropdown<br>6. Enter <one unit below minimum valid Amount> in the Amount field<br>7. Click Submit | Submission is blocked; error message displayed indicating that the Amount is below the minimum allowed | medium |
| TC-014 (input_edge) | WF-001 | Submit Charge Creation Form with long Charge Name | User is on the Charge Creation Form | 1. Enter a very long string (200+ characters) in the Charge_Name field<br>2. Select a valid option from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a valid option from the Charge_Time_Type dropdown<br>5. Select a valid option from the Charge_Calculation_Type dropdown<br>6. Enter a valid Amount in the Amount field<br>7. Click Submit | Form submits successfully; charge definition is created with the long Charge Name | low |
| TC-015 (input_edge) | WF-001 | Submit Charge Creation Form with special characters in Charge Name | User is on the Charge Creation Form | 1. Enter special characters in the Charge_Name field<br>2. Select a valid option from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a valid option from the Charge_Time_Type dropdown<br>5. Select a valid option from the Charge_Calculation_Type dropdown<br>6. Enter a valid Amount in the Amount field<br>7. Click Submit | Form submits successfully; charge definition is created with the Charge Name containing special characters | low |

---

## Floating Rates

Total: **12** (positive: 2, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new floating rate with valid details | User logged in as <Role> | 1. Click '+ Create Floating Rate' button<br>2. Enter <Floating Rate Name> in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Check the Is Active checkbox<br>5. Click 'Add Row' in the Rate Periods table<br>6. Enter <From Date> in the From Date field of the new row<br>7. Enter <Interest Rate> in the Interest Rate field of the new row<br>8. Click Submit | Floating rate created; success message shown | high |
| TC-002 | WF-002 | Edit an existing floating rate | User logged in as <Role>, At least one floating rate exists | 1. Click on the Floating Rate Name link of the existing floating rate<br>2. Click the Edit button<br>3. Modify the <Floating Rate Name> in the Floating Rate Name field<br>4. Uncheck the Is Base Lending Rate checkbox<br>5. Click Submit | Floating rate edited; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Floating Rate Name blank and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-004 | WF-001 | Submit the form with all required fields empty |  | 1. Click on '+ Create Floating Rate' button<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Floating Rate Name field displays an error: 'This field is required' | high |
| TC-005 | WF-001 | Select multiple base lending rates and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Check the Is Base Lending Rate checkbox<br>3. Check another Is Base Lending Rate checkbox for a different rate<br>4. Click Submit | Form does not submit; error shown indicating 'only one base rate can exist at a time' | high |
| TC-006 | WF-001 | Leave the From Date blank in Rate Periods and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Add a Rate Period<br>3. Leave the From Date field blank<br>4. Click Submit | Inline validation error appears on the From Date field indicating it is required | high |
| TC-007 | WF-001 | Enter a non-numeric value in the Interest Rate field |  | 1. Click on '+ Create Floating Rate' button<br>2. Add a Rate Period<br>3. Enter <non-numeric value> in the Interest Rate field<br>4. Click Submit | Inline validation error appears on the Interest Rate field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Add maximum allowed entries to Rate Periods | User is on the Create Floating Rate form | 1. Add the maximum allowed entries to the Rate Periods table | Form submits successfully; all entries are saved in the Rate Periods table | medium |
| TC-009 (boundary) | WF-001 | Attempt to add one more entry to Rate Periods beyond the maximum | User has added the maximum allowed entries to the Rate Periods table | 1. Attempt to add one more entry to the Rate Periods table | Submission is blocked; visible error indicating maximum entries reached | medium |
| TC-010 (input_edge) |  | Enter a very long Floating Rate Name | User is on the Create Floating Rate form | 1. Enter a string longer than 200 characters in the Floating Rate Name field | Input is either accepted or truncated with a visible indicator | low |
| TC-011 (input_edge) |  | Enter special characters in Floating Rate Name | User is on the Create Floating Rate form | 1. Enter special characters (e.g., @#$%^&*) in the Floating Rate Name field | Input is either accepted or a specific error shown | low |
| TC-012 (interaction_edge) |  | Rapid re-submission after successful creation | User has successfully created a Floating Rate | 1. Press the browser back button after the success message<br>2. Verify the Create Floating Rate form is shown blank | The Create Floating Rate form is shown blank; no duplicate entity is created | medium |

---

## Delinquency Management

Total: **15** (positive: 4, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Create Delinquency Range Form with valid data | User logged in as <Role> | 1. Navigate to Create Delinquency Range form<br>2. Enter <valid classification> in the Classification field<br>3. Enter <valid number> in the Minimum Age Days field<br>4. Enter <valid number> in the Maximum Age Days field<br>5. Click Submit | Delinquency range created; success message shown | high |
| TC-002 | WF-002 | Submit Create Delinquency Bucket Form with valid data | User logged in as <Role> | 1. Navigate to Create Delinquency Bucket form<br>2. Enter <valid bucket name> in the Bucket Name field<br>3. Click 'Add Range'<br>4. Enter <valid range description> in the Range Description field<br>5. Enter <valid number> in the Days field<br>6. Click 'Add Range' again<br>7. Enter <valid range description> in the Range Description field<br>8. Enter <valid number> in the Days field<br>9. Click Submit | Delinquency bucket created; success message shown | high |
| TC-003 | WF-003 | View Classification details in Delinquency Ranges | User logged in as <Role>, Delinquency Ranges page is open | 1. Click on the Classification link in the Delinquency Ranges table | Classification details displayed | medium |
| TC-004 | WF-004 | View Bucket details in Delinquency Buckets | User logged in as <Role>, Delinquency Buckets page is open | 1. Click on the Bucket Name link in the Delinquency Buckets table | Bucket details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave Classification field blank and submit |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-006 | WF-001 | Leave Minimum Age Days field blank and submit |  | 1. Leave the Minimum Age Days field blank<br>2. Fill Classification with a valid value<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-007 | WF-002 | Leave Bucket Name field blank and submit |  | 1. Leave the Bucket Name field blank<br>2. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-008 | WF-002 | Leave Range Description field blank and submit in delinquency ranges |  | 1. Click to add a delinquency range<br>2. Leave the Range Description field blank<br>3. Fill Days with a valid value<br>4. Click Submit | Inline validation error appears on the Range Description field indicating it is required | high |
| TC-009 | WF-002 | Leave Days field blank and submit in delinquency ranges |  | 1. Click to add a delinquency range<br>2. Fill Range Description with a valid value<br>3. Leave the Days field blank<br>4. Click Submit | Inline validation error appears on the Days field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Minimum Age Days at lower boundary |  | 1. Enter <minimum allowed value> in the Minimum Age Days field<br>2. Fill Classification field with valid value<br>3. Click Submit | Form submits successfully; delinquency range created with Minimum Age Days set to <minimum allowed value> | medium |
| TC-011 (boundary) | WF-001 | Minimum Age Days below lower boundary |  | 1. Enter <one unit below minimum> in the Minimum Age Days field<br>2. Fill Classification field with valid value<br>3. Click Submit | Submission is blocked; error shown indicating the value is below the minimum allowed | medium |
| TC-012 (boundary) | WF-001 | Maximum Age Days at upper boundary |  | 1. Enter <maximum allowed value> in the Maximum Age Days field<br>2. Fill Classification field with valid value<br>3. Fill Minimum Age Days field with valid value<br>4. Click Submit | Form submits successfully; delinquency range created with Maximum Age Days set to <maximum allowed value> | medium |
| TC-013 (boundary) | WF-001 | Maximum Age Days above upper boundary |  | 1. Enter <one unit above maximum> in the Maximum Age Days field<br>2. Fill Classification field with valid value<br>3. Fill Minimum Age Days field with valid value<br>4. Click Submit | Submission is blocked; error shown indicating the value exceeds the maximum allowed | medium |
| TC-014 (boundary) | WF-002 | Repeating group: add maximum number of delinquency ranges |  | 1. Fill Bucket Name field with valid value<br>2. Add <maximum allowed entries> delinquency ranges<br>3. Click Submit | Form submits successfully; delinquency bucket created with <maximum allowed entries> delinquency ranges | medium |
| TC-015 (boundary) | WF-002 | Repeating group: add one more delinquency range than allowed |  | 1. Fill Bucket Name field with valid value<br>2. Add <maximum allowed entries + 1> delinquency ranges<br>3. Click Submit | Submission is blocked; error shown indicating the maximum number of delinquency ranges has been exceeded | medium |

---

## Loan Account

Total: **31** (positive: 7, negative: 17, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application with valid details | User logged in as <Client> | 1. Click on 'Apply for Loan' from the Client Detail page<br>2. Select <valid product> from the Product Name dropdown<br>3. Enter <Loan Officer> in the Loan Officer field<br>4. Enter <Loan Purpose> in the Loan Purpose field<br>5. Enter <Fund> in the Fund field<br>6. Enter <valid date> in the Submitted On date field<br>7. Enter <valid date> in the Expected Disbursement Date field<br>8. Enter <valid principal amount> in the Principal field<br>9. Enter <valid number of repayments> in the Number of Repayments field<br>10. Enter <valid frequency> in the Repaid Every field<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Click 'Next' to proceed to Step 2<br>13. Select <valid repayment strategy> in the Repayment Strategy field<br>14. Select <valid amortization> in the Amortization field<br>15. Select <valid interest method> in the Interest Method field<br>16. Select <valid interest calculation period> from the Interest Calculation Period dropdown<br>17. Click 'Next' to proceed to Step 3<br>18. Click 'Add Charge' to add any additional charges<br>19. Click 'Next' to proceed to Step 4<br>20. Click 'Add Row' to add collateral items<br>21. Enter <valid collateral type> in the Collateral Type field<br>22. Enter <valid value> in the Value field<br>23. Click 'Submit' to finalize the loan application | Loan is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-002 | Approve Loan Application | User logged in as <Loan Officer>, Loan application is in 'Pending Approval' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Approve' on the Loan Detail Actions bar<br>3. Enter <valid date> in the Approved On Date field<br>4. Enter <valid approved amount> in the Approved Amount field<br>5. Enter <valid date> in the Expected Disbursement Date field<br>6. Click 'Confirm' on the approval dialog | Loan approved and ready for disbursement | high |
| TC-003 | WF-003 | Reject Loan Application | User logged in as <Loan Officer>, Loan application is in 'Pending Approval' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Reject' on the Loan Detail Actions bar<br>3. Click 'Confirm' on the rejection dialog | Loan application rejected | high |
| TC-004 | WF-004 | Withdraw Loan Application | User logged in as <Loan Officer>, Loan application is in 'Pending Approval' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Withdraw' on the Loan Detail Actions bar<br>3. Click 'Confirm' on the withdrawal dialog | Loan application withdrawn | high |
| TC-005 | WF-005 | Delete Loan Application | User logged in as <Loan Officer>, Loan application is in 'Pending Approval' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Delete' on the Loan Detail Actions bar<br>3. Click 'Confirm' on the deletion dialog | Loan application deleted | high |
| TC-006 | WF-006 | Disburse Loan | User logged in as <Loan Officer>, Loan application is in 'Approved' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Disburse' on the Loan Detail Actions bar<br>3. Enter <valid date> in the Disbursed On Date field<br>4. Enter <valid transaction amount> in the Transaction Amount field<br>5. Select <valid payment type> from the Payment Type dropdown<br>6. Click 'Confirm' on the disbursement dialog | Loan disbursed to client | high |
| TC-007 | WF-007 | Undo Loan Approval | User logged in as <Loan Officer>, Loan application is in 'Approved' status | 1. Navigate to the Loan Detail page of the application<br>2. Click 'Undo Approval' on the Loan Detail Actions bar<br>3. Click 'Confirm' on the undo approval dialog | Loan approval undone | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-009 |  | Leave the Loan Officer field blank and submit |  | 1. Leave the Loan Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-010 |  | Leave the Loan Purpose field blank and submit |  | 1. Leave the Loan Purpose field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Purpose field indicating it is required | high |
| TC-011 |  | Leave the Fund field blank and submit |  | 1. Leave the Fund field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fund field indicating it is required | high |
| TC-012 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-013 |  | Leave the Expected Disbursement Date blank and submit |  | 1. Leave the Expected Disbursement Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it is required | high |
| TC-014 |  | Leave the Principal field blank and submit |  | 1. Leave the Principal field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is required | high |
| TC-015 |  | Leave the Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-016 |  | Leave the Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-017 |  | Leave the Interest Rate field blank and submit |  | 1. Leave the Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-018 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; error shown on all required fields | high |
| TC-019 |  | Submit with Principal below minimum bound |  | 1. Enter <amount below minimum> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is bounded by product min/max | medium |
| TC-020 |  | Submit with Interest Rate above maximum bound |  | 1. Enter <amount exceeding maximum> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is bounded by product min/max | medium |
| TC-021 | WF-002 | Attempt to approve a loan application that is not in Pending Approval state |  | 1. Navigate to the Loan Detail page of a loan in Approved state<br>2. Click Approve | Status remains Approved; no transition occurs; error shown indicating action not allowed | medium |
| TC-022 | WF-003 | Attempt to reject a loan application that is not in Pending Approval state |  | 1. Navigate to the Loan Detail page of a loan in Approved state<br>2. Click Reject | Status remains Approved; no transition occurs; error shown indicating action not allowed | medium |
| TC-023 | WF-004 | Attempt to withdraw a loan application that is not in Pending Approval state |  | 1. Navigate to the Loan Detail page of a loan in Approved state<br>2. Click Withdraw | Status remains Approved; no transition occurs; error shown indicating action not allowed | medium |
| TC-024 | WF-005 | Attempt to delete a loan application that is not in Pending Approval state |  | 1. Navigate to the Loan Detail page of a loan in Approved state<br>2. Click Delete | Status remains Approved; no transition occurs; error shown indicating action not allowed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 (boundary) | WF-001 | Submit loan application with Principal at minimum product value | All required fields are filled correctly | 1. Enter <minimum product value> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created with Principal at minimum value | medium |
| TC-026 (boundary) | WF-001 | Submit loan application with Principal just above maximum product value | All required fields are filled correctly | 1. Enter <maximum product value + 1> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating Principal exceeds maximum allowed value | medium |
| TC-027 (boundary) | WF-001 | Submit loan application with Interest Rate at minimum product value | All required fields are filled correctly | 1. Enter <minimum product value> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created with Interest Rate at minimum value | medium |
| TC-028 (boundary) | WF-001 | Submit loan application with Interest Rate just above maximum product value | All required fields are filled correctly | 1. Enter <maximum product value + 1> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating Interest Rate exceeds maximum allowed value | medium |
| TC-029 (input_edge) |  | Enter long text in Loan Officer field | Loan application form is open | 1. Enter a long string of 200+ characters in the Loan Officer field | Field accepts input; Loan Officer field displays the long text correctly | low |
| TC-030 (input_edge) |  | Enter special characters in Loan Purpose field | Loan application form is open | 1. Enter special characters in the Loan Purpose field | Field accepts input; Loan Purpose field displays the special characters correctly | low |
| TC-031 (interaction_edge) |  | Rapid re-submission after successful loan application submission | Loan application is successfully submitted | 1. Click the browser back button<br>2. Observe the loan application form | Loan application form is shown blank; no second entity is created | low |

---

## Savings Account

Total: **35** (positive: 13, negative: 15, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Savings Account Creation Form | User logged in as <Role> | 1. Select <Product Name> from the Product Name dropdown<br>2. Enter <Field Officer> in the Field Officer field<br>3. Enter <valid date> in the Submitted On field<br>4. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>5. Select <Interest Compounding Period> from the Interest Compounding Period dropdown<br>6. Select <Interest Posting Period> from the Interest Posting Period dropdown<br>7. Select <Interest Calculated Using> from the Interest Calculated Using dropdown<br>8. Select <Days in Year> from the Days in Year dropdown<br>9. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>10. Enter <Lock-in Period> in the Lock-in Period field<br>11. Check the Allow Overdraft checkbox if applicable<br>12. Click 'Add Charge' in the Charges section<br>13. Enter <Charge Description> in the Charge Description field<br>14. Enter <Charge Amount> in the Charge Amount field<br>15. Click 'Submit' to create the account | Account is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-002 | Approve Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click 'Approve' on the Savings Account Actions | Account approved | high |
| TC-003 | WF-003 | Reject Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click 'Reject' on the Savings Account Actions | Account rejected | high |
| TC-004 | WF-004 | Withdraw Application for Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click 'Withdraw Application' on the Savings Account Actions | Application withdrawn | high |
| TC-005 | WF-005 | Activate Approved Savings Account | User logged in as <Role>, Account is in Approved status | 1. Click 'Activate' on the Savings Account Actions | Account activated | high |
| TC-006 | WF-007 | Deposit into Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Deposit' on the Savings Account Actions<br>2. Enter <valid date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Enter <Payment Details> if applicable<br>6. Click 'Submit' to deposit | Account credited | high |
| TC-007 | WF-008 | Withdraw from Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Withdraw' on the Savings Account Actions<br>2. Enter <valid date> in the Transaction Date field<br>3. Enter <Transaction Amount> in the Transaction Amount field<br>4. Select <Payment Type> from the Payment Type dropdown<br>5. Enter <Payment Details> if applicable<br>6. Click 'Submit' to withdraw | Account debited | high |
| TC-008 | WF-009 | Post Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Post Interest' on the Savings Account Actions | Interest posted | high |
| TC-009 | WF-010 | Calculate Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Calculate Interest' on the Savings Account Actions | Interest calculated | high |
| TC-010 | WF-011 | Close Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Close' on the Savings Account Actions | Account closed | high |
| TC-011 | WF-012 | Block Account for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Block Account' on the Savings Account Actions | Account blocked | high |
| TC-012 | WF-013 | Block Debit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Block Debit' on the Savings Account Actions | Debit blocked | high |
| TC-013 | WF-014 | Block Credit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click 'Block Credit' on the Savings Account Actions | Credit blocked | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-015 |  | Leave the Field Officer field blank and submit |  | 1. Leave the Field Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Field Officer field indicating it is required | high |
| TC-016 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-017 |  | Leave the Nominal Annual Interest Rate blank and submit |  | 1. Leave the Nominal Annual Interest Rate blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Nominal Annual Interest Rate field indicating it is required | high |
| TC-018 |  | Leave the Interest Compounding Period blank and submit |  | 1. Leave the Interest Compounding Period blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Compounding Period field indicating it is required | high |
| TC-019 |  | Leave the Interest Posting Period blank and submit |  | 1. Leave the Interest Posting Period blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Posting Period field indicating it is required | high |
| TC-020 |  | Leave the Interest Calculated Using blank and submit |  | 1. Leave the Interest Calculated Using blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Calculated Using field indicating it is required | high |
| TC-021 |  | Leave the Days in Year blank and submit |  | 1. Leave the Days in Year blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Days in Year field indicating it is required | high |
| TC-022 |  | Leave the Minimum Opening Balance blank and submit |  | 1. Leave the Minimum Opening Balance blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Minimum Opening Balance field indicating it is required | high |
| TC-023 |  | Leave the Lock-in Period blank and submit |  | 1. Leave the Lock-in Period blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Lock-in Period field indicating it is required | high |
| TC-024 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Form does not submit; multiple inline validation errors are shown indicating required fields | high |
| TC-025 | WF-008 | Attempt to withdraw from Active Savings Account exceeding available balance without overdraft enabled |  | 1. Open Withdraw dialog<br>2. Fill Transaction Date with <valid date><br>3. Fill Transaction Amount with <amount exceeding available balance><br>4. Select Payment Type as Cash<br>5. Click Submit | Form does not submit; error shown indicating withdrawal cannot exceed available balance unless overdraft is enabled | medium |
| TC-026 | WF-008 | Attempt to withdraw from Active Savings Account breaching minimum balance |  | 1. Open Withdraw dialog<br>2. Fill Transaction Date with <valid date><br>3. Fill Transaction Amount with <amount breaching minimum balance><br>4. Select Payment Type as Cash<br>5. Click Submit | Form does not submit; error shown indicating minimum balance must be enforced | medium |
| TC-027 | WF-001 | Attempt to submit Savings Account Creation Form without logging in |  | 1. Attempt to access Savings Account Creation Form without authentication | User is redirected to the login page | high |
| TC-028 | WF-002 | Attempt to approve a Pending Savings Account without the correct role |  | 1. Attempt to approve a Pending Savings Account as a user without approval permissions | User is blocked from approving the account; action is not visible | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 (boundary) | WF-001 | Submit Savings Account Creation Form with Minimum Opening Balance |  | 1. Select a product from the Product Name dropdown<br>2. Fill in the Field Officer<br>3. Enter today's date in the Submitted On field<br>4. Enter the minimum allowed value in the Minimum Opening Balance field<br>5. Fill in all other required fields<br>6. Click Submit | Form submits successfully; account is created with the minimum opening balance | medium |
| TC-030 (boundary) | WF-001 | Submit Savings Account Creation Form with Minimum Opening Balance - Below Minimum |  | 1. Select a product from the Product Name dropdown<br>2. Fill in the Field Officer<br>3. Enter today's date in the Submitted On field<br>4. Enter one unit below the minimum allowed value in the Minimum Opening Balance field<br>5. Fill in all other required fields<br>6. Click Submit | Form submission is blocked; error message shown for Minimum Opening Balance | medium |
| TC-031 (boundary) | WF-008 | Withdraw from Active Savings Account Exceeding Available Balance |  | 1. Navigate to the Active Savings Account<br>2. Click on Withdraw<br>3. Enter today's date in the Transaction Date field<br>4. Enter an amount greater than the available balance in the Transaction Amount field<br>5. Select a Payment Type<br>6. Click Submit | Withdrawal is blocked; error message shown indicating the withdrawal exceeds available balance | medium |
| TC-032 (boundary) | WF-008 | Withdraw from Active Savings Account at Minimum Balance |  | 1. Navigate to the Active Savings Account<br>2. Click on Withdraw<br>3. Enter today's date in the Transaction Date field<br>4. Enter an amount that equals the available balance minus the minimum balance in the Transaction Amount field<br>5. Select a Payment Type<br>6. Click Submit | Form submits successfully; account is debited without breaching minimum balance | medium |
| TC-033 (input_edge) |  | Enter Long Text in Charge Description |  | 1. Navigate to the Charges section of the Savings Account Creation Form<br>2. Add a new charge<br>3. Enter a long string (200+ characters) in the Charge Description field | Charge Description field accepts the long string without error or is truncated with a visible indicator | low |
| TC-034 (input_edge) |  | Enter Special Characters in Field Officer |  | 1. Navigate to the Savings Account Creation Form<br>2. Enter special characters (e.g., @#$%^&*) in the Field Officer field | Field Officer field accepts special characters without error or shows a specific error message | low |
| TC-035 (input_edge) |  | Enter Leading and Trailing Whitespace in Minimum Opening Balance |  | 1. Navigate to the Savings Account Creation Form<br>2. Enter leading and trailing spaces in the Minimum Opening Balance field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Share Account

Total: **23** (positive: 8, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application | User logged in as <Role>, Client has active savings accounts | 1. Select <Share Product> from the Share Product dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid number of shares> in the Requested Shares field<br>4. Enter <valid date> in the Application Date field<br>5. Select <Savings Account> from the Savings Account for Charges dropdown<br>6. Click Submit | Account created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Pending Share Account | User logged in as <Role>, Share account is in Pending status | 1. Enter <valid number of approved shares> in the Approved Shares field<br>2. Enter <valid date> in the Approved Date field<br>3. Click Approve | Approval process completed | high |
| TC-003 | WF-003 | Reject Pending Share Account | User logged in as <Role>, Share account is in Pending status | 1. Click Reject | Rejection process completed | high |
| TC-004 | WF-004 | Activate Approved Share Account | User logged in as <Role>, Share account is in Approved status | 1. Click Activate | Account activated | high |
| TC-005 | WF-005 | Undo Approval of Share Account | User logged in as <Role>, Share account is in Approved status | 1. Click Undo Approval | Approval undone | high |
| TC-006 | WF-006 | Apply Additional Shares to Active Share Account | User logged in as <Role>, Share account is in Active status | 1. Click Apply Additional Shares | Additional shares applied | high |
| TC-007 | WF-007 | Redeem Shares from Active Share Account | User logged in as <Role>, Share account is in Active status | 1. Click Redeem Shares | Redemption amount calculated as shares multiplied by current unit price and credited to the linked savings account | high |
| TC-008 | WF-008 | Close Active Share Account | User logged in as <Role>, Share account is in Active status | 1. Click Close | Account closed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-010 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 |  | Leave the Requested Shares field blank and submit |  | 1. Leave the Requested Shares field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-012 |  | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-013 |  | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-014 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Form does not submit; errors shown on Share Product, Submitted On, Requested Shares, Application Date, and Savings Account for Charges fields | high |
| TC-015 | WF-002 | Attempt to approve a pending share account without filling required fields | Account is in Pending state | 1. Click Approve<br>2. Leave Approved Shares and Approved Date fields blank<br>3. Click Submit | Inline validation error appears on the Approved Shares field indicating it is required; form does not submit | high |
| TC-016 | WF-004 | Attempt to activate an approved share account without any action | Account is in Approved state | 1. Click Activate | No action occurs; the account remains in Approved state | medium |
| TC-017 | WF-006 | Attempt to apply additional shares while account is not in Active state | Account is in Pending state | 1. Click Apply Additional Shares | No action occurs; the account remains in Pending state | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-001 | Submit application with requested shares at minimum limit | User has selected a Share Product with a defined minimum for Requested Shares | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed Requested Shares in the Requested Shares field<br>3. Enter today's date in the Submitted On field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | medium |
| TC-019 (boundary) | WF-001 | Submit application with requested shares at maximum limit | User has selected a Share Product with a defined maximum for Requested Shares | 1. Select a Share Product from the dropdown<br>2. Enter the maximum allowed Requested Shares in the Requested Shares field<br>3. Enter today's date in the Submitted On field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | medium |
| TC-020 (boundary) | WF-001 | Submit application with requested shares one unit over maximum limit | User has selected a Share Product with a defined maximum for Requested Shares | 1. Select a Share Product from the dropdown<br>2. Enter one unit over the maximum allowed Requested Shares in the Requested Shares field<br>3. Enter today's date in the Submitted On field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Submission is blocked; error shown indicating the Requested Shares exceed the maximum limit | medium |
| TC-021 (data_edge) | WF-001 | Submit application with Submitted On date set to yesterday |  | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed Requested Shares in the Requested Shares field<br>3. Enter yesterday's date in the Submitted On field<br>4. Enter today's date in the Application Date field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | medium |
| TC-022 (state_edge) | WF-002 | Rapidly approve a pending share account twice | Share account is in Pending status | 1. Click Approve on the pending share account<br>2. Enter the approved shares in the Approved Shares field<br>3. Enter today's date in the Approved Date field<br>4. Click Approve again immediately after the first approval | Second approval attempt is blocked; error shown indicating the account is already approved | medium |
| TC-023 (state_edge) | WF-007 | Redeem shares with a calculated redemption amount | Share account is in Active status with shares available to redeem | 1. Click Redeem Shares on the active share account<br>2. Enter the number of shares to redeem<br>3. Click Redeem | Redemption amount is calculated and credited to the linked savings account | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **23** (positive: 11, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Fixed Deposit Account Creation Form | User logged in as <Role> | 1. Open the Fixed Deposit Account Creation Form<br>2. Enter <valid deposit amount> in the Deposit Amount field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select <valid unit> from the Deposit Period Unit dropdown<br>5. Select <valid maturity instruction> from the Maturity Instructions dropdown<br>6. Click Submit | Page shows 'FD Account created successfully' | high |
| TC-002 | WF-002 | Submit Recurring Deposit Account Creation Form | User logged in as <Role> | 1. Open the Recurring Deposit Account Creation Form<br>2. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount Per Installment field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select <valid unit> from the Deposit Period Unit dropdown<br>5. Select <valid deposit frequency> from the Deposit Frequency dropdown<br>6. Enter <valid date> in the Expected First Deposit On field<br>7. Click Submit | Page shows 'RD Account created successfully' | high |
| TC-003 | WF-003 | Approve Fixed Deposit Account | User logged in as <Role>, FD Account is created and visible on the detail page | 1. Click Approve on the FD Account Detail Page | Page shows 'FD Account approved' | medium |
| TC-004 | WF-004 | Activate Fixed Deposit Account | User logged in as <Role>, FD Account is approved and visible on the detail page | 1. Click Activate on the FD Account Detail Page | Page shows 'FD Account activated' | medium |
| TC-005 | WF-005 | Premature Close Fixed Deposit Account | User logged in as <Role>, FD Account is activated and visible on the detail page | 1. Click Premature Close on the FD Account Detail Page | Page shows 'FD Account closed prematurely' | medium |
| TC-006 | WF-006 | Close Fixed Deposit Account on Maturity | User logged in as <Role>, FD Account is matured and visible on the detail page | 1. Click Close on Maturity on the FD Account Detail Page | Page shows 'FD Account closed on maturity' | medium |
| TC-007 | WF-007 | Approve Recurring Deposit Account | User logged in as <Role>, RD Account is created and visible on the detail page | 1. Click Approve on the RD Account Detail Page | Page shows 'RD Account approved' | medium |
| TC-008 | WF-008 | Activate Recurring Deposit Account | User logged in as <Role>, RD Account is approved and visible on the detail page | 1. Click Activate on the RD Account Detail Page | Page shows 'RD Account activated' | medium |
| TC-009 | WF-009 | Deposit into Recurring Deposit Account | User logged in as <Role>, RD Account is activated and visible on the detail page | 1. Click Deposit on the RD Account Detail Page | Page shows 'Deposit made into RD Account' | medium |
| TC-010 | WF-010 | Premature Close Recurring Deposit Account | User logged in as <Role>, RD Account is activated and visible on the detail page | 1. Click Premature Close on the RD Account Detail Page | Page shows 'RD Account closed prematurely' | medium |
| TC-011 | WF-011 | Close Recurring Deposit Account on Maturity | User logged in as <Role>, RD Account is matured and visible on the detail page | 1. Click Close on Maturity on the RD Account Detail Page | Page shows 'RD Account closed on maturity' | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Leave the Deposit Amount field blank and submit the Fixed Deposit Account Creation Form |  | 1. Leave the Deposit Amount field blank<br>2. Fill Deposit Period with a valid number<br>3. Select a valid Deposit Period Unit<br>4. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-013 | WF-001 | Leave all required fields empty and submit the Fixed Deposit Account Creation Form |  | 1. Leave the Deposit Amount field blank<br>2. Leave the Deposit Period field blank<br>3. Leave the Deposit Period Unit field blank<br>4. Click Submit | Form does not submit; Deposit Amount, Deposit Period, and Deposit Period Unit fields are highlighted with required errors | high |
| TC-014 | WF-002 | Leave the Mandatory Deposit Amount Per Installment field blank and submit the Recurring Deposit Account Creation Form |  | 1. Leave the Mandatory Deposit Amount Per Installment field blank<br>2. Fill Deposit Period with a valid number<br>3. Select a valid Deposit Period Unit<br>4. Select a valid Expected First Deposit On date<br>5. Click Submit | Inline validation error appears on the Mandatory Deposit Amount Per Installment field indicating it is required | high |
| TC-015 | WF-002 | Leave all required fields empty and submit the Recurring Deposit Account Creation Form |  | 1. Leave the Mandatory Deposit Amount Per Installment field blank<br>2. Leave the Deposit Period field blank<br>3. Leave the Deposit Period Unit field blank<br>4. Leave the Expected First Deposit On field blank<br>5. Click Submit | Form does not submit; Mandatory Deposit Amount Per Installment, Deposit Period, Deposit Period Unit, and Expected First Deposit On fields are highlighted with required errors | high |
| TC-016 | WF-003 | Attempt to Approve Fixed Deposit Account when it is not in a state that allows approval | The Fixed Deposit Account is already approved | 1. Navigate to the FD Account Detail Page<br>2. Click Approve | Status remains approved; no transition occurs; error shown indicating the account is already approved | medium |
| TC-017 | WF-008 | Attempt to Activate Recurring Deposit Account when it is not in a state that allows activation | The Recurring Deposit Account is already activated | 1. Navigate to the RD Account Detail Page<br>2. Click Activate | Status remains activated; no transition occurs; error shown indicating the account is already activated | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-001 | Submit Fixed Deposit Account Creation Form with minimum Deposit Amount |  | 1. Select a value from the Fixed Deposit Product dropdown<br>2. Enter the minimum allowed value in the Deposit Amount field<br>3. Enter a valid Deposit Period<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Maturity Instructions dropdown<br>6. Click Submit | Form submits successfully; FD Account is created with the minimum Deposit Amount | medium |
| TC-019 (boundary) | WF-001 | Submit Fixed Deposit Account Creation Form with Deposit Amount below minimum |  | 1. Select a value from the Fixed Deposit Product dropdown<br>2. Enter one unit below the minimum allowed value in the Deposit Amount field<br>3. Enter a valid Deposit Period<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Maturity Instructions dropdown<br>6. Click Submit | Submission is blocked; error shown indicating the Deposit Amount is below the minimum allowed | medium |
| TC-020 (boundary) | WF-002 | Submit Recurring Deposit Account Creation Form with minimum Mandatory Deposit Amount per Installment |  | 1. Select a value from the Recurring Deposit Product dropdown<br>2. Enter the minimum allowed value in the Mandatory Deposit Amount Per Installment field<br>3. Enter a valid Deposit Period<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Deposit Frequency dropdown<br>6. Enter a valid Expected First Deposit On date<br>7. Click Submit | Form submits successfully; RD Account is created with the minimum Mandatory Deposit Amount per Installment | medium |
| TC-021 (boundary) | WF-002 | Submit Recurring Deposit Account Creation Form with Mandatory Deposit Amount per Installment below minimum |  | 1. Select a value from the Recurring Deposit Product dropdown<br>2. Enter one unit below the minimum allowed value in the Mandatory Deposit Amount Per Installment field<br>3. Enter a valid Deposit Period<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Deposit Frequency dropdown<br>6. Enter a valid Expected First Deposit On date<br>7. Click Submit | Submission is blocked; error shown indicating the Mandatory Deposit Amount per Installment is below the minimum allowed | medium |
| TC-022 (data_edge) | WF-001 | Submit Fixed Deposit Account Creation Form with Deposit Period of zero |  | 1. Select a value from the Fixed Deposit Product dropdown<br>2. Enter a valid Deposit Amount<br>3. Enter 0 in the Deposit Period field<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Maturity Instructions dropdown<br>6. Click Submit | Submission is blocked; error shown indicating the Deposit Period cannot be zero | medium |
| TC-023 (data_edge) | WF-002 | Submit Recurring Deposit Account Creation Form with Expected First Deposit On date in the past |  | 1. Select a value from the Recurring Deposit Product dropdown<br>2. Enter a valid Mandatory Deposit Amount Per Installment<br>3. Enter a valid Deposit Period<br>4. Select a unit from the Deposit Period Unit dropdown<br>5. Select a value from the Deposit Frequency dropdown<br>6. Enter a date that is in the past in the Expected First Deposit On field<br>7. Click Submit | Submission is blocked; error shown indicating the Expected First Deposit On date cannot be in the past | medium |

---

## Accounting — Chart of Accounts

Total: **13** (positive: 4, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View GL Account details | User logged in as <role> | 1. Click on an account name in the Chart of Accounts table | Account details displayed | high |
| TC-002 | WF-002 | Edit GL Account | User logged in as <role> | 1. Click on an account name in the Chart of Accounts table<br>2. Click the Edit button | Edit form displayed | high |
| TC-003 | WF-003 | Delete GL Account | User logged in as <role> | 1. Click on an account name in the Chart of Accounts table<br>2. Click the Delete button<br>3. Confirm deletion | Account deleted; success message shown | high |
| TC-004 | WF-004 | Create a new GL Account | User logged in as <role> | 1. Click the '+ Create GL Account' button<br>2. Select <Account Type> from the dropdown<br>3. Enter <unique GL Code> in the GL Code field<br>4. Enter <Account Name> in the Account Name field<br>5. Select <Account Usage> from the dropdown<br>6. Check the Manual Entries Allowed checkbox if applicable<br>7. Enter <Description> in the Description field<br>8. Select <Tag> from the dropdown<br>9. Click Submit | GL Account created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-004 | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-006 | WF-004 | Leave the GL Code field blank and submit |  | 1. Leave the GL Code field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-007 | WF-004 | Leave the Account Name field blank and submit |  | 1. Leave the Account Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-008 | WF-004 | Leave the Description field blank and submit |  | 1. Leave the Description field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Description field indicating it is required | high |
| TC-009 | WF-004 | Submit with a duplicate GL Code |  | 1. Fill all required fields with valid data<br>2. Enter a duplicate value in the GL Code field<br>3. Click Submit | Form does not submit; error shown on GL Code field indicating 'GL Code must be unique' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-004 | Create GL Account with unique GL Code |  | 1. Open the Create GL Account form<br>2. Select a value from the Account Type dropdown<br>3. Enter a unique GL Code in the GL_Code field<br>4. Enter a valid Account Name in the Account_Name field<br>5. Enter a valid Description in the Description field<br>6. Click Submit | GL Account created; success message shown | medium |
| TC-011 (boundary) | WF-004 | Create GL Account with duplicate GL Code | A GL Account with the same GL Code already exists | 1. Open the Create GL Account form<br>2. Select a value from the Account Type dropdown<br>3. Enter the same GL Code as the existing account in the GL_Code field<br>4. Enter a valid Account Name in the Account_Name field<br>5. Enter a valid Description in the Description field<br>6. Click Submit | Validation error shown indicating GL Code must be unique | medium |
| TC-012 (input_edge) |  | Create GL Account with long Description |  | 1. Open the Create GL Account form<br>2. Select a value from the Account Type dropdown<br>3. Enter a unique GL Code in the GL_Code field<br>4. Enter a valid Account Name in the Account_Name field<br>5. Enter a long Description exceeding 200 characters in the Description field<br>6. Click Submit | Form submits successfully; Description is accepted or truncated with a visible indicator | low |
| TC-013 (input_edge) |  | Create GL Account with special characters in Account Name |  | 1. Open the Create GL Account form<br>2. Select a value from the Account Type dropdown<br>3. Enter a unique GL Code in the GL_Code field<br>4. Enter special characters in the Account_Name field<br>5. Enter a valid Description in the Description field<br>6. Click Submit | Form submits successfully; Account Name is accepted or specific error shown | low |

---

## Accounting — Journal Entries & Closures

Total: **14** (positive: 2, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid journal entry | User logged in as <Role>, Total debits equal total credits in the entry lines | 1. Click '+ Add Journal Entry' to open the form<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid reference number> in the Reference Number field<br>5. Select <valid date> in the Transaction Date field<br>6. Click 'Add Row' to add an entry line<br>7. Select <valid GL account> from the GL Account dropdown in the entry line<br>8. Enter <valid amount> in the Amount field of the entry line<br>9. Click 'Submit' to submit the journal entry | A success notification is displayed; the journal entry is listed in the Journal Entries Table | high |
| TC-002 | WF-002 | Create a valid closure | User logged in as <Role> | 1. Click '+ Create Closure' to open the closure form<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid date> in the Closing Date field<br>4. Enter <valid comments> in the Comments field<br>5. Click 'Submit' to create the closure | A success notification is displayed; the closure is listed in the Closing Entries Table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Office field blank and submit the journal entry form |  | 1. Open the Add Journal Entry form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-004 | WF-001 | Leave the Transaction Date field blank and submit the journal entry form |  | 1. Open the Add Journal Entry form<br>2. Leave the Transaction Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-005 | WF-001 | Leave the GL Account field blank in the Entry Lines and submit the journal entry form |  | 1. Open the Add Journal Entry form<br>2. Add a row in Entry Lines<br>3. Leave the GL Account field blank<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-006 | WF-001 | Leave the Amount field blank in the Entry Lines and submit the journal entry form |  | 1. Open the Add Journal Entry form<br>2. Add a row in Entry Lines<br>3. Leave the Amount field blank<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-007 | WF-001 | Submit journal entry with total debits not equal to total credits |  | 1. Open the Add Journal Entry form<br>2. Fill in all required fields with valid data<br>3. Add entry lines where total debits do not equal total credits<br>4. Click Submit | Validation error appears indicating 'Total debits must equal total credits' | high |
| TC-008 | WF-002 | Leave the Office field blank and submit the create closure form |  | 1. Open the Create Closure form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-009 | WF-002 | Leave the Closing Date field blank and submit the create closure form |  | 1. Open the Create Closure form<br>2. Leave the Closing Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Closing Date field indicating it is required | high |
| TC-010 | WF-002 | Attempt to create closure with journal entries posted for the closing date |  | 1. Open the Create Closure form<br>2. Fill in all required fields with a Closing Date that has journal entries posted on or before that date<br>3. Click Submit | Validation error appears indicating 'journal entries cannot be posted for dates on or before the closing date' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Total debits exactly equal total credits | Form is filled with valid data | 1. Add a journal entry with debit amount of <X><br>2. Add a journal entry with credit amount of <X><br>3. Click Submit | Form submits successfully; journal entry is created | medium |
| TC-012 (boundary) | WF-001 | Total debits exceed total credits by one unit | Form is filled with valid data | 1. Add a journal entry with debit amount of <X><br>2. Add a journal entry with credit amount of <X-1><br>3. Click Submit | Submission is blocked; error shown indicating 'Total debits must equal total credits' | medium |
| TC-013 (boundary) | WF-002 | Closing date equals transaction date | No journal entries posted for the closing date | 1. Fill in the Office field<br>2. Set Closing Date to today's date<br>3. Click + Create Closure | Form submits successfully; closure is created | medium |
| TC-014 (boundary) | WF-002 | Closing date is one day before transaction date | No journal entries posted for the closing date | 1. Fill in the Office field<br>2. Set Closing Date to yesterday's date<br>3. Click + Create Closure | Submission is blocked; error shown indicating 'journal entries cannot be posted for dates on or before the closing date' | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **16** (positive: 5, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-003 | Create a new accounting rule successfully | User logged in as <Role> | 1. Click '+ Create Rule' to open the creation form<br>2. Enter <valid rule name> in the Rule Name field<br>3. Select <valid office> from the Office dropdown<br>4. Select <valid debit account> from the Debit Tags Account multi-select<br>5. Check the Allow Multiple Debit Entries checkbox<br>6. Select <valid credit account> from the Credit Tags Account dropdown<br>7. Check the Allow Multiple Credit Entries checkbox<br>8. Click Submit | A success notification is displayed; the Accounting rule created successfully. | high |
| TC-002 | WF-001 | Edit an existing accounting rule successfully | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click Edit<br>3. Update the Rule Name field with <new valid rule name><br>4. Click Submit | A success notification is displayed; Rule details updated. | high |
| TC-003 | WF-002 | Delete an existing accounting rule successfully | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click Delete<br>3. Confirm the deletion | A success notification is displayed; Rule deleted successfully. | high |
| TC-004 | WF-004 | Create a new financial activity mapping successfully | User logged in as <Role> | 1. Click '+ Create Mapping' to open the creation form<br>2. Select <valid financial activity> from the Financial Activity dropdown<br>3. Select <valid GL account> from the GL Account dropdown<br>4. Click Submit | A success notification is displayed; Financial activity mapping created successfully. | high |
| TC-005 | WF-005 | Link to financial activity details successfully | User logged in as <Role>, At least one financial activity mapping exists | 1. Click on the Financial Activity of the existing mapping | Navigated to financial activity details. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-003 | Leave the Rule Name field blank and submit |  | 1. Open the Create Rule form<br>2. Leave the Rule Name field blank<br>3. Click Submit | Inline validation error appears on the Rule Name field indicating it is required | high |
| TC-007 | WF-004 | Leave the Financial Activity field blank and submit |  | 1. Open the Create Mapping form<br>2. Leave the Financial Activity field blank<br>3. Click Submit | Inline validation error appears on the Financial Activity field indicating it is required | high |
| TC-008 | WF-004 | Leave the GL Account field blank and submit |  | 1. Open the Create Mapping form<br>2. Leave the GL Account field blank<br>3. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-009 |  | Attempt to create a mapping with a duplicate financial activity |  | 1. Open the Create Mapping form<br>2. Select a Financial Activity that is already mapped<br>3. Select a GL Account<br>4. Click Submit | Error message displayed indicating that the financial activity can only be mapped once | medium |
| TC-010 | WF-002 | Attempt to delete a rule that does not exist |  | 1. Attempt to delete a rule by selecting a non-existent rule<br>2. Click Delete | Error message displayed indicating that the rule does not exist | medium |
| TC-011 | WF-001 | Attempt to edit a rule that does not exist |  | 1. Attempt to edit a rule by selecting a non-existent rule<br>2. Click Edit | Error message displayed indicating that the rule does not exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-003 | Create accounting rule with exactly one character in Rule Name |  | 1. Open Create Rule Form<br>2. Enter 'A' in the Rule Name field<br>3. Click Submit | Form submits successfully; entity is created with the Rule Name 'A' | medium |
| TC-013 (boundary) | WF-003 | Create accounting rule with exactly 255 characters in Rule Name |  | 1. Open Create Rule Form<br>2. Enter a string of 255 characters in the Rule Name field<br>3. Click Submit | Form submits successfully; entity is created with the Rule Name of 255 characters | medium |
| TC-014 (boundary) | WF-003 | Create accounting rule with 256 characters in Rule Name |  | 1. Open Create Rule Form<br>2. Enter a string of 256 characters in the Rule Name field<br>3. Click Submit | Submission is blocked; error message displayed indicating maximum length exceeded | medium |
| TC-015 (boundary) | WF-004 | Create financial activity mapping with a valid financial activity and GL account |  | 1. Open Create Mapping Form<br>2. Select a valid Financial Activity from the dropdown<br>3. Select a valid GL Account from the dropdown<br>4. Click Submit | Form submits successfully; financial activity mapping is created | medium |
| TC-016 (boundary) | WF-004 | Create financial activity mapping with the same financial activity twice |  | 1. Open Create Mapping Form<br>2. Select a financial activity that has already been mapped<br>3. Select a valid GL Account from the dropdown<br>4. Click Submit | Submission is blocked; error message displayed indicating financial activity can only be mapped once | medium |

---

## Provisioning

Total: **18** (positive: 5, negative: 6, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create new provisioning criteria | User logged in as <Role> | 1. Click '+ Create' to open the Create Criteria form<br>2. Enter <Criteria Name> in the Criteria Name field<br>3. Click 'Add Row' in the Definitions table<br>4. Enter <Loan_Product> in the Loan Product field<br>5. Select 'STANDARD' from the Category dropdown<br>6. Enter <valid number> in the Minimum Age field<br>7. Enter <valid number> in the Maximum Age field<br>8. Enter <valid percentage> in the Provisioning Percentage field<br>9. Select <Liability Account> from the Liability Account dropdown<br>10. Select <Expense Account> from the Expense Account dropdown<br>11. Click '+ Create' to submit the form | The table displays the new provisioning criteria with the entered Criteria Name | high |
| TC-002 | WF-002 | View provisioning criteria | User logged in as <Role>, At least one provisioning criteria exists | 1. Click on the Criteria Name link in the Provisioning Criteria Table | Criteria details displayed | medium |
| TC-003 | WF-003 | Create new provisioning entry | User logged in as <Role>, Provisioning criteria is configured | 1. Click '+ Create Provisioning Entry'<br>2. Confirm the action | Generates new provisioning entries based on current loan portfolio status | high |
| TC-004 | WF-004 | Review provisioning entry | User logged in as <Role>, At least one provisioning entry exists | 1. Click 'Review' on a provisioning entry in the Provisioning Entries Table | Detailed breakdown by loan product and category displayed | medium |
| TC-005 | WF-005 | Recreate provisioning entry | User logged in as <Role>, At least one provisioning entry exists | 1. Click 'Recreate' on a provisioning entry in the Provisioning Entries Table<br>2. Confirm the action | Provisioning entry recreated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave Criteria Name blank and submit |  | 1. Leave the Criteria_Name field blank<br>2. Fill all other required fields in Definitions with valid data<br>3. Click + Create | Inline validation error appears on the Criteria_Name field indicating it is required | high |
| TC-007 | WF-001 | Leave all required fields in Definitions blank and submit |  | 1. Leave the Criteria_Name field blank<br>2. Leave all fields in Definitions blank<br>3. Click + Create | Inline validation error appears on the Criteria_Name field indicating it is required; Form does not submit; no provisioning criteria is created | high |
| TC-008 | WF-001 | Submit with invalid Minimum Age value |  | 1. Enter valid Criteria_Name<br>2. Add a Definitions row<br>3. Enter <invalid non-numeric value> in Minimum_Age field<br>4. Fill all other required fields with valid data<br>5. Click + Create | Inline validation error appears on the Minimum_Age field indicating it must be a number | medium |
| TC-009 | WF-001 | Submit with Minimum Age greater than Maximum Age |  | 1. Enter valid Criteria_Name<br>2. Add a Definitions row<br>3. Enter <value greater than maximum> in Minimum_Age field<br>4. Enter <valid value> in Maximum_Age field<br>5. Fill all other required fields with valid data<br>6. Click + Create | Inline validation error appears indicating Minimum_Age must be less than Maximum_Age | medium |
| TC-010 | WF-001 | Submit with invalid Provisioning Percentage value |  | 1. Enter valid Criteria_Name<br>2. Add a Definitions row<br>3. Enter <invalid non-numeric value> in Provisioning_Percentage field<br>4. Fill all other required fields with valid data<br>5. Click + Create | Inline validation error appears on the Provisioning_Percentage field indicating it must be a number | medium |
| TC-011 | WF-003 | Attempt to create provisioning entry without criteria defined |  | 1. Click + Create Provisioning Entry | Form does not submit; no provisioning entries are created; error shown indicating criteria must be defined | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Minimum Age boundary test | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a new row in the Definitions table<br>3. Enter a valid Loan Product in the Loan_Product field<br>4. Select a valid Category from the dropdown<br>5. Enter exactly 1 in the Minimum_Age field<br>6. Enter a valid value in the Maximum_Age field<br>7. Enter a valid value in the Provisioning_Percentage field<br>8. Select valid Liability Account from the dropdown<br>9. Select valid Expense Account from the dropdown<br>10. Click + Create | New provisioning criteria is created successfully with Minimum_Age set to 1 | medium |
| TC-013 (boundary) | WF-001 | Maximum Age boundary test | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a new row in the Definitions table<br>3. Enter a valid Loan Product in the Loan_Product field<br>4. Select a valid Category from the dropdown<br>5. Enter a valid value in the Minimum_Age field<br>6. Enter exactly 1 in the Maximum_Age field<br>7. Enter a valid value in the Provisioning_Percentage field<br>8. Select valid Liability Account from the dropdown<br>9. Select valid Expense Account from the dropdown<br>10. Click + Create | New provisioning criteria is created successfully with Maximum_Age set to 1 | medium |
| TC-014 (boundary) | WF-001 | Provisioning Percentage boundary test | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a new row in the Definitions table<br>3. Enter a valid Loan Product in the Loan_Product field<br>4. Select a valid Category from the dropdown<br>5. Enter a valid value in the Minimum_Age field<br>6. Enter a valid value in the Maximum_Age field<br>7. Enter exactly 0 in the Provisioning_Percentage field<br>8. Select valid Liability Account from the dropdown<br>9. Select valid Expense Account from the dropdown<br>10. Click + Create | New provisioning criteria is created successfully with Provisioning_Percentage set to 0 | medium |
| TC-015 (boundary) | WF-001 | Adding maximum number of definitions | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add 10 rows in the Definitions table<br>3. Fill in all required fields for each row<br>4. Click + Create | New provisioning criteria is created successfully with 10 definitions | medium |
| TC-016 (boundary) | WF-001 | Attempt to add one more definition than allowed | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add 10 rows in the Definitions table<br>3. Fill in all required fields for each row<br>4. Attempt to add one more row<br>5. Click + Create | Submission is blocked; error shown indicating maximum number of definitions exceeded | medium |
| TC-017 (input_edge) |  | Long text in Criteria Name field | User is on the Create Criteria Form | 1. Enter a string of 250 characters in the Criteria_Name field<br>2. Click + Create | Form submits successfully; Criteria_Name displays the full 250 characters in the detail view | low |
| TC-018 (input_edge) |  | Special characters in Loan Product field | User is on the Create Criteria Form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a new row in the Definitions table<br>3. Enter special characters in the Loan_Product field<br>4. Select a valid Category from the dropdown<br>5. Enter a valid value in the Minimum_Age field<br>6. Enter a valid value in the Maximum_Age field<br>7. Enter a valid value in the Provisioning_Percentage field<br>8. Select valid Liability Account from the dropdown<br>9. Select valid Expense Account from the dropdown<br>10. Click + Create | Submission is blocked; error shown indicating invalid characters in Loan_Product field | low |

---

## Offices

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Office Details | User logged in as <Role> | 1. Click on the Office Name link in the Offices table | Office details displayed | high |
| TC-002 | WF-002 | Edit Office | User logged in as <Role> | 1. Click on the Edit button for an office in the Offices table | Edit form displayed | high |
| TC-003 | WF-003 | Create Office | User logged in as <Role> | 1. Click on the '+ Create Office' button<br>2. Enter <valid office name> in the Office Name field<br>3. Select 'Head Office' from the Parent Office dropdown<br>4. Enter <valid date> in the Opened On Date field<br>5. Enter <valid external ID> in the External ID field<br>6. Click Submit | Office created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Attempt to create office with Office Name blank |  | 1. Leave the Office Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-005 | WF-003 | Attempt to create office with Parent Office blank |  | 1. Leave the Parent Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-006 | WF-003 | Attempt to create office with Opened On Date blank |  | 1. Leave the Opened On Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-007 | WF-003 | Attempt to create office with External ID blank |  | 1. Leave the External ID field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the External ID field indicating it is required | high |
| TC-008 | WF-003 | Attempt to create office with invalid Parent Office |  | 1. Enter <invalid Parent Office> in the Parent Office field<br>2. Fill all other required fields<br>3. Click Submit | Error shown indicating 'Head Office is the root' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-003 | Open date is set to today |  | 1. Enter a valid value in the Office Name field<br>2. Enter a valid value in the Parent Office field<br>3. Enter today's date in the Opened On Date field<br>4. Enter a valid value in the External ID field<br>5. Click Submit | Form submits successfully; office is created with today's date in the Opened On Date field | medium |
| TC-010 (boundary) | WF-003 | Open date is set to yesterday |  | 1. Enter a valid value in the Office Name field<br>2. Enter a valid value in the Parent Office field<br>3. Enter yesterday's date in the Opened On Date field<br>4. Enter a valid value in the External ID field<br>5. Click Submit | Form submits successfully; office is created with yesterday's date in the Opened On Date field | medium |
| TC-011 (boundary) | WF-003 | Open date is set to a far future date |  | 1. Enter a valid value in the Office Name field<br>2. Enter a valid value in the Parent Office field<br>3. Enter a far future date in the Opened On Date field<br>4. Enter a valid value in the External ID field<br>5. Click Submit | Form submits successfully; office is created with the far future date in the Opened On Date field | medium |
| TC-012 (input_edge) | WF-003 | Enter a long string in Office Name |  | 1. Enter a string longer than 200 characters in the Office Name field<br>2. Enter a valid value in the Parent Office field<br>3. Enter today's date in the Opened On Date field<br>4. Enter a valid value in the External ID field<br>5. Click Submit | Form submission is blocked; an error message is shown indicating the Office Name exceeds the maximum length | low |
| TC-013 (input_edge) | WF-003 | Enter special characters in External ID |  | 1. Enter a valid value in the Office Name field<br>2. Enter a valid value in the Parent Office field<br>3. Enter today's date in the Opened On Date field<br>4. Enter special characters in the External ID field<br>5. Click Submit | Form submission is blocked; an error message is shown indicating invalid characters in the External ID field | low |

---

## Employees

Total: **14** (positive: 4, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Employee Details | User logged in as <Role>, Employee is listed in the Employees table | 1. Click the Name link of the employee in the Employees table | Employee details displayed | high |
| TC-002 | WF-002 | Edit Employee Details | User logged in as <Role>, Employee is listed in the Employees table | 1. Click the Edit action for the employee in the Employees table | Employee edit form displayed | high |
| TC-003 | WF-003 | Create New Employee | User logged in as <Role> | 1. Click the + Create Employee button | opens creation form | high |
| TC-004 | WF-003 | Submit New Employee Creation | User logged in as <Role>, Creation form is open | 1. Enter <Office> in the Office field<br>2. Enter <First Name> in the First Name field<br>3. Enter <Last Name> in the Last Name field<br>4. Click Submit | A new employee is added to the Employees table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Attempt to create a new employee with required fields empty |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Leave the First Name field blank<br>4. Leave the Last Name field blank<br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required'; First Name field displays an error: 'This field is required'; Last Name field displays an error: 'This field is required' | high |
| TC-006 |  | Attempt to create a new employee with Office field empty |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Fill in the First Name field with '<valid first name>'<br>4. Fill in the Last Name field with '<valid last name>'<br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required' | high |
| TC-007 |  | Attempt to create a new employee with First Name field empty |  | 1. Click on the '+ Create Employee' button<br>2. Fill in the Office field with '<valid office>'<br>3. Leave the First Name field blank<br>4. Fill in the Last Name field with '<valid last name>'<br>5. Click Submit | Form does not submit; First Name field displays an error: 'This field is required' | high |
| TC-008 |  | Attempt to create a new employee with Last Name field empty |  | 1. Click on the '+ Create Employee' button<br>2. Fill in the Office field with '<valid office>'<br>3. Fill in the First Name field with '<valid first name>'<br>4. Leave the Last Name field blank<br>5. Click Submit | Form does not submit; Last Name field displays an error: 'This field is required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-003 | Joining Date is today | User is on the Create Employee form | 1. Enter today's date in the Joining Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; employee record is created with today's date in Joining Date field | medium |
| TC-010 (boundary) | WF-003 | Joining Date is yesterday | User is on the Create Employee form | 1. Enter yesterday's date in the Joining Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; employee record is created with yesterday's date in Joining Date field | medium |
| TC-011 (boundary) | WF-003 | Joining Date is far future date | User is on the Create Employee form | 1. Enter a far future date in the Joining Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; employee record is created with the far future date in Joining Date field | medium |
| TC-012 (input_edge) |  | Enter long text in First Name field | User is on the Create Employee form | 1. Enter a string longer than 200 characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates the First Name exceeds the maximum length | low |
| TC-013 (input_edge) |  | Enter special characters in Last Name field | User is on the Create Employee form | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates invalid characters in the Last Name field | low |
| TC-014 (input_edge) |  | Enter value with leading/trailing whitespace in Office field | User is on the Create Employee form | 1. Enter '   Office Name   ' in the Office field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shows 'Office Name' on detail page | low |

---

## Teller & Cashier Management

Total: **20** (positive: 5, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Create Teller Form | User logged in as <Role> | 1. Click '+ Create Teller' button | Creation form opens | high |
| TC-002 | WF-002 | Submit Create Teller Form | User logged in as <Role>, Creation form is open | 1. Enter <valid office> in the Office field<br>2. Enter <valid teller name> in the Teller Name field<br>3. Enter <valid start date> in the Start Date field<br>4. Click Submit | Teller created; success message shown | high |
| TC-003 | WF-003 | Open Edit Teller Form | User logged in as <Role>, Teller Detail page is open | 1. Click Edit button | Edit form opens | medium |
| TC-004 | WF-004 | Allocate Cashier | User logged in as <Role>, Cashier Detail page is open | 1. Click '+ Allocate Cashier' button<br>2. Enter <valid staff> in the Staff field<br>3. Enter <valid start date> in the Start Date field<br>4. Click Allocate Cash | adds cash from the vault | high |
| TC-005 | WF-005 | Settle Cash | User logged in as <Role>, Cashier Detail page is open | 1. Click Settle Cash button<br>2. Enter <valid amount> in the Amount field<br>3. Enter <valid currency> in the Currency field<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click Settle Cash | returns cash to the vault | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Office field blank in Create Teller Form |  | 1. Click on '+ Create Teller'<br>2. Leave the Office field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 |  | Leave the Teller Name field blank in Create Teller Form |  | 1. Click on '+ Create Teller'<br>2. Leave the Teller Name field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Teller Name field indicating it is required | high |
| TC-008 |  | Leave the Start Date field blank in Create Teller Form |  | 1. Click on '+ Create Teller'<br>2. Leave the Start Date field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-009 |  | Leave Staff field blank in Allocate Cashier Form |  | 1. Click on '+ Allocate Cashier'<br>2. Leave the Staff field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Staff field indicating it is required | high |
| TC-010 |  | Leave Start Date field blank in Allocate Cashier Form |  | 1. Click on '+ Allocate Cashier'<br>2. Leave the Start Date field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-011 |  | Submit Create Teller Form with all required fields empty |  | 1. Click on '+ Create Teller'<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; error shown on Office, Teller Name, and Start Date fields | high |
| TC-012 | WF-005 | Submit Settle Cash with Amount field blank |  | 1. Click on 'Settle Cash'<br>2. Leave the Amount field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-013 | WF-005 | Submit Settle Cash with Currency field blank |  | 1. Click on 'Settle Cash'<br>2. Leave the Currency field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-014 | WF-005 | Submit Settle Cash with Transaction Date field blank |  | 1. Click on 'Settle Cash'<br>2. Leave the Transaction Date field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-002 | Create Teller with valid Start Date | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller_Name field<br>3. Enter today's date in the Start_Date field<br>4. Click Submit | Form submits successfully; teller is created with today's date as Start Date | medium |
| TC-016 (boundary) | WF-002 | Create Teller with Start Date in the past | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller_Name field<br>3. Enter yesterday's date in the Start_Date field<br>4. Click Submit | Form is blocked; error message displayed indicating Start Date cannot be in the past | medium |
| TC-017 (boundary) | WF-002 | Create Teller with valid End Date | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller_Name field<br>3. Enter today's date in the Start_Date field<br>4. Enter a date in the far future in the End_Date field<br>5. Click Submit | Form submits successfully; teller is created with the far future date as End Date | medium |
| TC-018 (boundary) | WF-002 | Create Teller without required fields | User is on the Create Teller Form | 1. Leave the Office field empty<br>2. Leave the Teller_Name field empty<br>3. Click Submit | Form is blocked; error messages displayed indicating required fields must be filled | medium |
| TC-019 (input_edge) |  | Enter long text in Description field | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Teller Name in the Teller_Name field<br>3. Enter a long text (over 200 characters) in the Description field<br>4. Enter today's date in the Start_Date field<br>5. Click Submit | Form submits successfully; saved Description shows the long text without truncation | low |
| TC-020 (input_edge) |  | Enter special characters in Teller Name | User is on the Create Teller Form | 1. Enter a valid Office in the Office field<br>2. Enter special characters in the Teller_Name field<br>3. Enter today's date in the Start_Date field<br>4. Click Submit | Form submits successfully; Teller Name is saved with special characters | low |

---

## Users & Roles

Total: **21** (positive: 4, negative: 11, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View User Details | User logged in as <role>, User exists in the Users table | 1. Click on the Username link in the Users table | User details displayed | high |
| TC-002 | WF-002 | Create User | User logged in as <role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <same valid password> in the Repeat Password field<br>9. Click Submit | User created; success message shown | high |
| TC-003 | WF-003 | Create Role | User logged in as <role> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Enter <description> in the Description field<br>4. Click Submit | Role created; success message shown | high |
| TC-004 | WF-004 | View Role Details | User logged in as <role>, Role exists in the Roles table | 1. Click on the Role Name link in the Roles table | Role details displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-002 | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-006 | WF-002 | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-007 | WF-002 | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-008 | WF-002 | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 | WF-002 | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email format | medium |
| TC-010 | WF-002 | Leave the Office field blank and submit |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 | WF-002 | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 | WF-002 | Enter a password that does not meet policy and submit |  | 1. Enter <password that does not meet policy> in the Password field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it must meet password policy | medium |
| TC-013 | WF-002 | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Repeat Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match Password | medium |
| TC-014 | WF-003 | Leave the Role Name field blank and submit |  | 1. Leave the Role Name field blank<br>2. Click Submit | Inline validation error appears on the Role Name field indicating it is required | high |
| TC-015 |  | Attempt to access the Users page without authentication |  | 1. Navigate to the Users page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-002 | Username input at minimum uniqueness constraint | Existing user with username 'testuser' | 1. Enter 'testuser' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating 'Username must be unique' | medium |
| TC-017 (boundary) | WF-002 | Email input at valid format boundary |  | 1. Enter 'user@example.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; user is created with the email 'user@example.com' | medium |
| TC-018 (boundary) | WF-002 | Password input at password policy boundary |  | 1. Enter a password that meets the policy criteria in the Password field<br>2. Enter the same password in the Repeat Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form submits successfully; user is created with the specified password | medium |
| TC-019 (boundary) | WF-002 | Password mismatch between Password and Repeat Password |  | 1. Enter 'Password123!' in the Password field<br>2. Enter 'Password123' in the Repeat Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form submission is blocked; error shown indicating 'Passwords do not match' | medium |
| TC-020 (boundary) | WF-003 | Role Name input at uniqueness constraint | Existing role with name 'Admin' | 1. Enter 'Admin' in the Role_Name field<br>2. Click Submit | Form submission is blocked; error shown indicating 'Role Name must be unique' | medium |
| TC-021 (input_edge) |  | Long text in Description field for role creation |  | 1. Enter a long description (over 200 characters) in the Description field<br>2. Fill the Role_Name field with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating 'Description exceeds maximum length' | low |

---

## Reports

Total: **13** (positive: 5, negative: 2, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Report Parameters for 'Loans Awaiting Disbursal' | User logged in as <Role> | 1. Click on the report 'Loans Awaiting Disbursal' in the Reports table | Parameters form displayed for the selected report | high |
| TC-002 | WF-002 | Run Report with output option 'View on Screen' | User logged in as <Role>, Parameters form for 'Loans Awaiting Disbursal' is open | 1. Select <valid office> from the Office dropdown<br>2. Click 'Run Report' button<br>3. Select 'view on screen' from output options | Report generated and displayed on screen | high |
| TC-003 | WF-002 | Run Report with output option 'Export to Excel' | User logged in as <Role>, Parameters form for 'Loans Awaiting Disbursal' is open | 1. Select <valid office> from the Office dropdown<br>2. Click 'Run Report' button<br>3. Select 'export to Excel' from output options | Report generated and exported to Excel | medium |
| TC-004 | WF-002 | Run Report with output option 'Export to CSV' | User logged in as <Role>, Parameters form for 'Loans Awaiting Disbursal' is open | 1. Select <valid office> from the Office dropdown<br>2. Click 'Run Report' button<br>3. Select 'export to CSV' from output options | Report generated and exported to CSV | medium |
| TC-005 | WF-002 | Run Report with output option 'Export to PDF' | User logged in as <Role>, Parameters form for 'Loans Awaiting Disbursal' is open | 1. Select <valid office> from the Office dropdown<br>2. Click 'Run Report' button<br>3. Select 'export to PDF' from output options | Report generated and exported to PDF | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to submit report parameters with Office field blank |  | 1. Open Report Parameters for a specific report<br>2. Leave the Office field blank<br>3. Click Run Report | Inline validation error appears on the Office field indicating it is required | high |
| TC-007 | WF-002 | Attempt to run report with no output option selected |  | 1. Open Report Parameters for a specific report<br>2. Select a valid Office<br>3. Click Run Report without selecting any output option | Form does not submit; no report is generated; error shown indicating an output option must be selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Select the first option in the Office dropdown | User is on the Reports page, User has opened the Report Parameters form | 1. Click on the Office dropdown<br>2. Select the first available option | The Office field is populated with the first option; no error is shown. | medium |
| TC-009 (boundary) | WF-001 | Select the last option in the Office dropdown | User is on the Reports page, User has opened the Report Parameters form | 1. Click on the Office dropdown<br>2. Select the last available option | The Office field is populated with the last option; no error is shown. | medium |
| TC-010 (boundary) | WF-002 | Select a valid output option for exporting | User has filled required fields in Report Parameters, User is ready to run the report | 1. Click on the Run Report button<br>2. Choose 'export to Excel' as the output option | The report is generated and exported to Excel successfully. | medium |
| TC-011 (boundary) | WF-002 | Select an invalid output option for exporting | User has filled required fields in Report Parameters, User is ready to run the report | 1. Click on the Run Report button<br>2. Choose an unsupported output option | An error message is displayed indicating the output option is not supported. | medium |
| TC-012 (input_edge) |  | Enter a very long string in the Date Range field | User is on the Reports page, User has opened the Report Parameters form | 1. Click on the Date Range field<br>2. Enter a string longer than 200 characters | The input is either truncated or an error message is shown indicating the input is too long. | low |
| TC-013 (input_edge) |  | Enter special characters in the Loan Officer field | User is on the Reports page, User has opened the Report Parameters form | 1. Click on the Loan Officer dropdown<br>2. Enter special characters like @#$%^&* | An error message is displayed indicating invalid characters. | low |

---

## Account Transfers & Standing Instructions

Total: **16** (positive: 4, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid account transfer | User logged in as <Role>, Sufficient balance in the source account | 1. Enter <valid From Office> in the From Office field<br>2. Enter <valid From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <valid From Account> in the From Account field<br>5. Enter <valid To Office> in the To Office field<br>6. Enter <valid To Client> in the To Client field<br>7. Select 'Loan Account' from the To Account Type dropdown<br>8. Enter <valid To Account> in the To Account field<br>9. Enter <valid Transfer Amount> in the Transfer Amount field<br>10. Enter <valid Transfer Date> in the Transfer Date field<br>11. Enter <optional Description> in the Description field<br>12. Click Submit | processes the transfer, debiting the source and crediting the destination | high |
| TC-002 | WF-002 | Enable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Enable on the standing instruction row | Standing instruction enabled | medium |
| TC-003 | WF-003 | Disable a standing instruction | User logged in as <Role>, At least one standing instruction is enabled | 1. Click Disable on the standing instruction row | Standing instruction disabled | medium |
| TC-004 | WF-004 | Delete a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Delete on the standing instruction row | Standing instruction deleted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Transfer Amount is left blank |  | 1. Leave the Transfer Amount field blank<br>2. Fill in a valid Transfer Date<br>3. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-006 | WF-001 | Transfer Amount exceeds available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Fill in a valid Transfer Date<br>3. Click Submit | Form does not submit; error shown: 'Transfer amount exceeds available balance' | high |
| TC-007 | WF-002 | Attempt to enable standing instruction without proper permissions |  | 1. Attempt to click Enable on a standing instruction | Action is blocked; no change occurs to the standing instruction status | medium |
| TC-008 | WF-003 | Attempt to disable standing instruction without proper permissions |  | 1. Attempt to click Disable on a standing instruction | Action is blocked; no change occurs to the standing instruction status | medium |
| TC-009 | WF-004 | Attempt to delete standing instruction without proper permissions |  | 1. Attempt to click Delete on a standing instruction | Action is blocked; standing instruction is not deleted | medium |
| TC-010 |  | Name field left blank in Create Standing Instruction form |  | 1. Leave the Name field blank<br>2. Fill in valid From Account and To Account fields<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Transfer amount equals available balance | User has an account with a known balance | 1. Enter the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-012 (boundary) | WF-001 | Transfer amount exceeds available balance | User has an account with a known balance | 1. Enter an amount greater than the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Error is shown indicating that the transfer amount exceeds the available balance | medium |
| TC-013 (data_edge) | WF-001 | Transfer date is today |  | 1. Enter today's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-014 (data_edge) | WF-001 | Transfer date is in the past |  | 1. Enter a date in the Transfer Date field that is yesterday<br>2. Fill all other required fields<br>3. Click Submit | Error is shown indicating that the transfer date cannot be in the past | medium |
| TC-015 (interaction_edge) | WF-002 | Enable standing instruction after creation | At least one standing instruction exists | 1. Click the Enable action for a standing instruction<br>2. Observe the action status | Standing instruction is enabled successfully | medium |
| TC-016 (interaction_edge) | WF-004 | Delete standing instruction | At least one standing instruction exists | 1. Click the Delete action for a standing instruction<br>2. Confirm the deletion | Standing instruction is deleted successfully | medium |

---

## Tax Management

Total: **18** (positive: 6, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new tax component successfully | User logged in as <Role> | 1. Click '+ Create Tax Component' button<br>2. Enter <valid tax component name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Enter <valid debit account> in the Debit Account field<br>6. Select 'Liability' from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Enter <valid start date> in the Start Date field<br>9. Click Save | A success notification is displayed; the tax component details are visible in the Tax Components table | high |
| TC-002 | WF-002 | Create a new tax group successfully | User logged in as <Role> | 1. Click '+ Create Tax Group' button<br>2. Enter <valid tax group name> in the Name field<br>3. Click 'Add Tax Component' to add a component<br>4. Enter <valid start date> in the Start Date field of the component<br>5. Enter <valid end date> in the End Date field of the component<br>6. Click Save | A success notification is displayed; the tax group details are visible in the Tax Groups table | high |
| TC-003 | WF-003 | View tax component details | User logged in as <Role>, At least one tax component exists | 1. Click on the Name link of an existing tax component in the Tax Components table | Tax component details displayed | medium |
| TC-004 | WF-004 | Delete selected tax components | User logged in as <Role>, At least one tax component exists | 1. Select one or more tax components in the Tax Components table<br>2. Click 'Delete Selected' | Selected tax components deleted | medium |
| TC-005 | WF-005 | View tax group details | User logged in as <Role>, At least one tax group exists | 1. Click on the Name link of an existing tax group in the Tax Groups table | Tax group details displayed | medium |
| TC-006 | WF-006 | Delete selected tax groups | User logged in as <Role>, At least one tax group exists | 1. Select one or more tax groups in the Tax Groups table<br>2. Click 'Delete Selected' | Selected tax groups deleted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Leave the Name field blank and submit the Create Tax Component form |  | 1. Leave the Name field blank<br>2. Fill in the Percentage field with a valid number<br>3. Select a Debit Account Type<br>4. Fill in the Start Date<br>5. Click Save | Inline validation error appears on the Name field indicating it is required | high |
| TC-008 | WF-001 | Leave the Percentage field blank and submit the Create Tax Component form |  | 1. Fill in the Name field with a valid name<br>2. Leave the Percentage field blank<br>3. Select a Debit Account Type<br>4. Fill in the Start Date<br>5. Click Save | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-009 | WF-001 | Leave the Start Date field blank and submit the Create Tax Component form |  | 1. Fill in the Name field with a valid name<br>2. Fill in the Percentage field with a valid number<br>3. Select a Debit Account Type<br>4. Leave the Start Date field blank<br>5. Click Save | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 | WF-002 | Leave the Name field blank and submit the Create Tax Group form |  | 1. Leave the Name field blank<br>2. Click Save | Inline validation error appears on the Name field indicating it is required | high |
| TC-011 | WF-002 | Leave the Start Date field blank in Tax Components and submit the Create Tax Group form |  | 1. Fill in the Name field with a valid name<br>2. Add a Tax Component with Start Date left blank<br>3. Click Save | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-012 | WF-002 | Leave the End Date field blank in Tax Components and submit the Create Tax Group form |  | 1. Fill in the Name field with a valid name<br>2. Add a Tax Component with End Date left blank<br>3. Click Save | Inline validation error appears on the End Date field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Add a tax component with minimum percentage | User is on the Create Tax Component form | 1. Enter a valid Name in the Name field<br>2. Enter 0 in the Percentage field<br>3. Select a Debit Account Type from the dropdown<br>4. Enter a valid Debit Account<br>5. Select a Credit Account Type from the dropdown<br>6. Enter a valid Credit Account<br>7. Enter a valid Start Date | Form submits successfully; entity is created with the Percentage of 0 | medium |
| TC-014 (boundary) | WF-001 | Add a tax component with percentage just above maximum limit | User is on the Create Tax Component form | 1. Enter a valid Name in the Name field<br>2. Enter 101 in the Percentage field<br>3. Select a Debit Account Type from the dropdown<br>4. Enter a valid Debit Account<br>5. Select a Credit Account Type from the dropdown<br>6. Enter a valid Credit Account<br>7. Enter a valid Start Date | Form submission is blocked; an error message indicates that the Percentage exceeds the maximum allowed value | medium |
| TC-015 (boundary) | WF-002 | Add a tax group with maximum allowed components | User is on the Create Tax Group form | 1. Enter a valid Name in the Name field<br>2. Add maximum allowed entries in the Tax Components section<br>3. For each component, enter valid Start Dates and End Dates | Form submits successfully; tax group is created with maximum allowed components | medium |
| TC-016 (boundary) | WF-002 | Attempt to add one more tax component than allowed | User is on the Create Tax Group form | 1. Enter a valid Name in the Name field<br>2. Add maximum allowed entries in the Tax Components section<br>3. Attempt to add one more component | Adding the component is blocked; an error message indicates that the maximum number of components has been reached | medium |
| TC-017 (input_edge) |  | Enter long text in Name field | User is on the Create Tax Component form | 1. Enter a string of 200+ characters in the Name field<br>2. Fill all other required fields with valid data | Form submission is either accepted or an error message indicates that the Name exceeds the maximum length | low |
| TC-018 (input_edge) |  | Enter special characters in Name field | User is on the Create Tax Component form | 1. Enter a string with special characters in the Name field<br>2. Fill all other required fields with valid data | Form submission is either accepted or an error message indicates invalid characters in the Name field | low |

---

## Organization Settings

Total: **16** (positive: 3, negative: 8, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new holiday successfully | User logged in as <Admin> | 1. Navigate to the Holidays page<br>2. Click '+ Create Holiday'<br>3. Enter <Holiday Name> in the Name field<br>4. Select <valid start date> in the From Date field<br>5. Select <valid end date> in the To Date field<br>6. Select <valid rescheduled date> in the Repayments Rescheduled To field<br>7. Select <valid rescheduling type> from the Rescheduling Type dropdown<br>8. (Optional) Enter <description> in the Description field<br>9. (Optional) Select applicable offices from the Applicable Offices multi-select<br>10. Click 'Submit' | Holiday created; success message shown | high |
| TC-002 | WF-002 | Create a new fund successfully | User logged in as <Admin> | 1. Navigate to the Funds page<br>2. Click 'Create Fund'<br>3. Click 'Submit' | Fund created; success message shown | high |
| TC-003 | WF-003 | Create a new payment type successfully | User logged in as <Admin> | 1. Navigate to the Payment Types page<br>2. Click '+ Create'<br>3. Click 'Submit' | Payment type created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to create a holiday with the Name field blank |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-005 | WF-001 | Attempt to create a holiday with the From_Date field blank |  | 1. Click on '+ Create Holiday'<br>2. Leave the From_Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the From_Date field indicating it is required | high |
| TC-006 | WF-001 | Attempt to create a holiday with the To_Date field blank |  | 1. Click on '+ Create Holiday'<br>2. Leave the To_Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the To_Date field indicating it is required | high |
| TC-007 | WF-001 | Attempt to create a holiday with the Repayments_Rescheduled_To field blank |  | 1. Click on '+ Create Holiday'<br>2. Leave the Repayments_Rescheduled_To field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Repayments_Rescheduled_To field indicating it is required | high |
| TC-008 | WF-001 | Attempt to create a holiday with the Rescheduling_Type field blank |  | 1. Click on '+ Create Holiday'<br>2. Leave the Rescheduling_Type field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Rescheduling_Type field indicating it is required | high |
| TC-009 | WF-001 | Attempt to create a holiday with all required fields blank |  | 1. Click on '+ Create Holiday'<br>2. Leave all required fields blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required; Inline validation error appears on the From_Date field indicating it is required; Inline validation error appears on the To_Date field indicating it is required; Inline validation error appears on the Repayments_Rescheduled_To field indicating it is required; Inline validation error appears on the Rescheduling_Type field indicating it is required | high |
| TC-010 | WF-002 | Attempt to create a fund without any fields filled |  | 1. Click on 'Create Fund'<br>2. Leave all fields blank<br>3. Click Submit | Form does not submit; no fund is created; error shown | high |
| TC-011 | WF-003 | Attempt to create a payment type without any fields filled |  | 1. Click on '+ Create'<br>2. Leave all fields blank<br>3. Click Submit | Form does not submit; no payment type is created; error shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Create holiday with From_Date equal to To_Date |  | 1. Click + Create Holiday<br>2. Enter 'New Year' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Enter a future date in the Repayments_Rescheduled_To field<br>6. Select a Rescheduling_Type from the dropdown<br>7. Click Submit | Form submits successfully; holiday created with From_Date and To_Date set to today's date | medium |
| TC-013 (boundary) | WF-001 | Create holiday with From_Date one day before To_Date |  | 1. Click + Create Holiday<br>2. Enter 'Holiday' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Enter a future date in the Repayments_Rescheduled_To field<br>6. Select a Rescheduling_Type from the dropdown<br>7. Click Submit | Form submits successfully; holiday created with From_Date set to today and To_Date set to tomorrow | medium |
| TC-014 (boundary) | WF-001 | Create holiday with Repayments_Rescheduled_To before From_Date |  | 1. Click + Create Holiday<br>2. Enter 'Invalid Holiday' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Enter yesterday's date in the Repayments_Rescheduled_To field<br>6. Select a Rescheduling_Type from the dropdown<br>7. Click Submit | Submission is blocked; error shown indicating that Repayments_Rescheduled_To must be on or after From_Date | medium |
| TC-015 (input_edge) |  | Enter long text in Name field |  | 1. Click + Create Holiday<br>2. Enter a string of 200 characters in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Enter a future date in the Repayments_Rescheduled_To field<br>6. Select a Rescheduling_Type from the dropdown<br>7. Click Submit | Form submits successfully; holiday created with the long Name value displayed correctly | low |
| TC-016 (input_edge) |  | Enter special characters in Name field |  | 1. Click + Create Holiday<br>2. Enter '!@#$%^&*()' in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Enter a future date in the Repayments_Rescheduled_To field<br>6. Select a Rescheduling_Type from the dropdown<br>7. Click Submit | Form submits successfully; holiday created with special characters in the Name field displayed correctly | low |

---

## System Administration

Total: **17** (positive: 5, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Toggle Start/Stop Scheduler | User logged in as <Admin>, Scheduler is currently running | 1. Click the Start/Stop Scheduler toggle | Scheduler state toggled | high |
| TC-002 | WF-002 | Submit Manage Data Tables form | User logged in as <Admin> | 1. Navigate to Manage Data Tables page<br>2. Enter <Data Table Name> in the Data Table Name field<br>3. Select 'm_client' from the Application Table Name dropdown<br>4. Uncheck Multi Row checkbox<br>5. Click Submit | Data table created | high |
| TC-003 | WF-003 | Submit Manage Data Tables form with Multi Row | User logged in as <Admin> | 1. Navigate to Manage Data Tables page<br>2. Enter <Data Table Name> in the Data Table Name field<br>3. Select 'm_group' from the Application Table Name dropdown<br>4. Check Multi Row checkbox<br>5. Click Submit | Data table created | high |
| TC-004 | WF-004 | Approve pending action in Audit Trails | User logged in as <Checker>, maker-checker is enabled, There is a pending action in Audit Trails | 1. Navigate to Audit Trails page<br>2. Click Approve on the pending action | Action approved | high |
| TC-005 | WF-005 | Reject pending action in Audit Trails | User logged in as <Checker>, maker-checker is enabled, There is a pending action in Audit Trails | 1. Navigate to Audit Trails page<br>2. Click Reject on the pending action | Action rejected | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Data Table Name blank and submit |  | 1. Leave the Data Table Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Data Table Name field indicating it is required | high |
| TC-007 |  | Leave the Application Table Name dropdown unselected and submit |  | 1. Leave the Application Table Name dropdown unselected<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Table Name field indicating it is required | high |
| TC-008 |  | Leave the Name field in Column Definitions blank and submit |  | 1. Click to add a new column definition<br>2. Leave the Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 |  | Toggle Start/Stop Scheduler when scheduler is already stopped | Scheduler is currently stopped | 1. Click the Start/Stop Scheduler toggle | Scheduler state remains stopped; no change occurs | medium |
| TC-010 |  | Submit Manage Data Tables form with invalid Length value |  | 1. Fill the Data Table Name field<br>2. Select an Application Table Name<br>3. Click to add a new column definition<br>4. Fill the Name field<br>5. Fill the Type field<br>6. Enter <invalid length> in the Length field<br>7. Click Submit | Inline validation error appears on the Length field indicating it must be a valid number | medium |
| TC-011 |  | Attempt to approve a pending action when maker-checker is not enabled | maker-checker is not enabled | 1. Navigate to the Audit Trails page<br>2. Attempt to click the Approve button for a pending action | Approve button is not visible; action cannot be approved | medium |
| TC-012 |  | Attempt to reject a pending action when maker-checker is not enabled | maker-checker is not enabled | 1. Navigate to the Audit Trails page<br>2. Attempt to click the Reject button for a pending action | Reject button is not visible; action cannot be rejected | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapid toggle of Start/Stop Scheduler | Scheduler is currently running | 1. Click the Start/Stop Scheduler toggle<br>2. Immediately click the Start/Stop Scheduler toggle again | Scheduler state toggled successfully; the toggle reflects the latest state change. | medium |
| TC-014 (boundary) | WF-002 | Submit Manage Data Tables form with maximum column definitions | All required fields are filled, Column Definitions has maximum allowed entries | 1. Enter valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Check the Multi Row checkbox<br>4. Add maximum allowed entries to Column Definitions<br>5. Click Submit | Form submits successfully; data table is created with all column definitions. | medium |
| TC-015 (boundary) | WF-002 | Submit Manage Data Tables form with one extra column definition | All required fields are filled, Column Definitions has maximum allowed entries | 1. Enter valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Check the Multi Row checkbox<br>4. Add maximum allowed entries to Column Definitions<br>5. Attempt to add one more entry to Column Definitions<br>6. Click Submit | Submission is blocked; visible error indicates that the maximum number of column definitions has been exceeded. | medium |
| TC-016 (interaction_edge) | WF-004 | Rapid approval of pending actions in Audit Trails | Maker-checker is enabled, There are pending actions to approve | 1. Click Approve on a pending action<br>2. Immediately click Approve on another pending action | First action is approved; the second approval attempt is blocked with a message indicating that actions cannot be approved in quick succession. | medium |
| TC-017 (interaction_edge) | WF-005 | Rapid rejection of pending actions in Audit Trails | Maker-checker is enabled, There are pending actions to reject | 1. Click Reject on a pending action<br>2. Immediately click Reject on another pending action | First action is rejected; the second rejection attempt is blocked with a message indicating that actions cannot be rejected in quick succession. | medium |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully from the user profile dropdown | User logged in as <Role> | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click on 'Log Out' from the dropdown | User is redirected to the login page after the session is terminated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | User is not authenticated | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User remains on the current page; no session is terminated; user is not redirected to the login page | high |
| TC-003 |  | Attempt to access an authenticated page after logout | User is logged in, User has successfully logged out | 1. Attempt to navigate to an authenticated page | User is redirected to the login page; access to the authenticated page is blocked | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click 'Log Out'<br>3. Immediately click 'Log Out' again | Second logout attempt is blocked; user is redirected to the login page without logging out again | medium |
| TC-005 (input_edge) |  | Attempt to navigate to an authenticated page after logout | User is logged in, User has logged out | 1. Navigate to an authenticated page | User is redirected to the login page | medium |

---
