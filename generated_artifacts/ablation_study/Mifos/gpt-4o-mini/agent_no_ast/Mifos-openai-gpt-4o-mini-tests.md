# Test Cases — Mifos

Generated: 2026-06-10T19:10:41.530776Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 405 | 126 | 154 | 125 | 226 | 119 | 54 |

## Login

Total: **9** (positive: 2, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <User> | 1. Select 'default' from the Tenant dropdown<br>2. Enter <valid username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Check the Remember me checkbox<br>5. Click the Login button | Redirect to the Dashboard | high |
| TC-002 | WF-003 | Empty required fields validation | User logged in as <User> | 1. Click the Login button without filling any fields | Inline validation messages shown | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-003 | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill in the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-004 | WF-003 | Leave the Password field blank and submit |  | 1. Fill in the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-005 | WF-003 | Leave all required fields empty and submit |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Form does not submit; inline validation errors appear on the Username and Password fields indicating they are required | high |
| TC-006 | WF-002 | Submit with invalid credentials |  | 1. Fill in the Username field with <invalid username><br>2. Fill in the Password field with <invalid password><br>3. Click Login | Error message displayed: 'Incorrect username or password.' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Fill in the Password field<br>3. Click Login | Inline validation message shown indicating the username exceeds the maximum length | low |
| TC-008 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter special characters (e.g., @#$%^&*) in the Username field<br>2. Fill in the Password field<br>3. Click Login | Inline validation message shown indicating the username contains invalid characters | low |
| TC-009 (input_edge) |  | Enter leading and trailing whitespace in the Username field |  | 1. Enter '   username   ' in the Username field<br>2. Fill in the Password field<br>3. Click Login | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Home Page

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display welcome message and search input on home page | User logged in as <User> | 1. Observe the home page | The home page displays 'Welcome, mifos!' and a 'Search Activity' input field. | high |
| TC-002 |  | Access dashboard from home page | User logged in as <User> | 1. Click on the 'Dashboard' button | User is redirected to the dashboard view. | medium |
| TC-003 |  | Display system version information on home page | User logged in as <User> | 1. Observe the bottom of the home page | System version information for Mifos and Fineract is displayed. | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user attempts to access the Home page |  | 1. Attempt to access the Home page without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the Search Activity input field | User is logged in and on the Home page | 1. Enter a string of 200+ characters in the 'Search Activity' input field | Input is either accepted or truncated with a visible indicator | low |
| TC-006 (input_edge) |  | Enter special characters in the Search Activity input field | User is logged in and on the Home page | 1. Enter special characters (e.g., @#$%^&*) in the 'Search Activity' input field | Input is accepted or a specific error is shown | low |
| TC-007 (input_edge) |  | Enter a value with leading and trailing whitespace in the Search Activity input field | User is logged in and on the Home page | 1. Enter '   search term   ' in the 'Search Activity' input field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Dashboard

Total: **6** (positive: 2, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Access Dashboard and verify components | User logged in as <User Role> | 1. Click the 'Dashboard' button on the Home page | The 'Search Activity' field is visible at the top; the 'Client Trends' chart displays with legends for 'New Clients' and 'Closed Clients'; summary cards for 'Amount Pending / Disbursed' and 'Amount Collected' are displayed |  |
| TC-002 |  | Verify no data message in summary cards | User logged in as <User Role>, No data is available for the selected office | 1. Click the 'Dashboard' button on the Home page | The summary cards display 'No Data' for both 'Amount Pending / Disbursed' and 'Amount Collected' |  |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user attempts to access the Dashboard |  | 1. Navigate to the Dashboard URL | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Enter a very long search term in the Search Activity field | User is on the Dashboard page | 1. Enter a string of 200+ characters in the 'Search Activity' field<br>2. Click the search button | The system accepts the input and displays a loading indicator or an error message indicating input length if it exceeds limits. | low |
| TC-005 (input_edge) |  | Enter special characters in the Search Activity field | User is on the Dashboard page | 1. Enter a string containing special characters (e.g., @#$%^&*) in the 'Search Activity' field<br>2. Click the search button | The system handles the input and displays either the relevant results or an error message indicating invalid characters. | low |
| TC-006 (input_edge) |  | Enter whitespace in the Search Activity field | User is on the Dashboard page | 1. Enter a string with leading and trailing spaces in the 'Search Activity' field<br>2. Click the search button | Leading/trailing whitespace is trimmed; the search term displayed in the results has no extra spaces. | low |

---

## Global Search

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search with matching results | User logged in as <Role> | 1. Click the search icon in the top toolbar<br>2. Enter <search term> in the search input field<br>3. Select a matching result from the dropdown | Navigates to the corresponding detail page | high |
| TC-002 | WF-002 | Search with no results | User logged in as <Role> | 1. Click the search icon in the top toolbar<br>2. Enter <non-matching search term> in the search input field | No results found message displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to search with an empty input field |  | 1. Click on the search icon in the top toolbar<br>2. Leave the search input field blank<br>3. Click the search button | No results found message is displayed | high |
| TC-004 | WF-002 | Search for a non-existent entity |  | 1. Click on the search icon in the top toolbar<br>2. Enter <non-existent entity> in the search input field<br>3. Click the search button | No results found message is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) | WF-001 | Search with long input string | User is logged in, User is on any page | 1. Click on the search icon in the top toolbar<br>2. Enter a string longer than 200 characters in the search input field | Search input is accepted; results are displayed or truncated appropriately. | low |
| TC-006 (input_edge) | WF-001 | Search with special characters | User is logged in, User is on any page | 1. Click on the search icon in the top toolbar<br>2. Enter a string containing special characters (e.g., @#$%^&*) in the search input field | Search input is accepted; results are displayed or a specific error message is shown. | low |
| TC-007 (input_edge) | WF-002 | Search with leading and trailing whitespace | User is logged in, User is on any page | 1. Click on the search icon in the top toolbar<br>2. Enter a search term with leading and trailing spaces in the search input field | Leading/trailing whitespace is trimmed; 'No results found' message is displayed if no matches exist. | low |

---

## Client Management

Total: **25** (positive: 10, negative: 10, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Import Client | User logged in as <role> | 1. Click 'Import Client' button<br>2. Verify redirection to Bulk Import page | Redirects to Bulk Import page | high |
| TC-002 | WF-002 | Create Client | User logged in as <role> | 1. Click 'Create Client' button<br>2. Enter <Office> in the Office field<br>3. Enter <First Name> in the First Name field<br>4. Enter <Last Name> in the Last Name field<br>5. Enter <Submitted On> in the Submitted On field<br>6. Click 'Submit' button | Client created in Pending status | high |
| TC-003 | WF-003 | View Client Details | User logged in as <role>, Client exists in Pending status | 1. Click on the client name link in the data table | Client details displayed | medium |
| TC-004 | WF-004 | Edit Client | User logged in as <role>, Client exists in Pending status | 1. Click on the client name link in the data table<br>2. Click 'Edit' button<br>3. Update <Field> with <New Value><br>4. Click 'Submit' button | Client details updated | medium |
| TC-005 | WF-005 | Reject Client | User logged in as <role>, Client exists in Pending status | 1. Click on the client name link in the data table<br>2. Click 'Reject' button<br>3. Enter <reason> in the reason field<br>4. Click 'Confirm' on the Reject dialog | Client rejected with reason | medium |
| TC-006 | WF-006 | Withdraw Client | User logged in as <role>, Client exists in Pending status | 1. Click on the client name link in the data table<br>2. Click 'Withdraw' button<br>3. Enter <reason> in the reason field<br>4. Click 'Confirm' on the Withdraw dialog | Client withdrawn with reason | medium |
| TC-007 | WF-007 | Activate Client | User logged in as <role>, Client exists in Pending status | 1. Click on the client name link in the data table<br>2. Click 'Activate' button<br>3. Enter <Activation Date> in the Activation Date field<br>4. Click 'Confirm' on the Activate dialog | Client activated | medium |
| TC-008 | WF-008 | Transfer Client | User logged in as <role>, Client exists in Active status | 1. Click on the client name link in the data table<br>2. Click 'Transfer Client' button<br>3. Select <destination office> from the dropdown<br>4. Click 'Submit' button | Client transferred to new office | medium |
| TC-009 | WF-009 | Close Client | User logged in as <role>, Client exists in Active status | 1. Click on the client name link in the data table<br>2. Click 'Close' button<br>3. Enter <closure reason> in the reason field<br>4. Click 'Confirm' on the Close dialog | Client closed with reason | medium |
| TC-010 | WF-010 | Reactivate Client | User logged in as <role>, Client exists in Closed status | 1. Click on the client name link in the data table<br>2. Click 'Reactivate' button<br>3. Click 'Confirm' on the Reactivate dialog | Client reactivated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-002 | Leave the required Office field blank when creating a client |  | 1. Open the Create Client form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-012 | WF-002 | Leave the required First Name field blank when creating a client |  | 1. Open the Create Client form<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-013 | WF-002 | Leave the required Last Name field blank when creating a client |  | 1. Open the Create Client form<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-014 | WF-002 | Leave the required Submitted On field blank when creating a client |  | 1. Open the Create Client form<br>2. Leave the Submitted On field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-015 | WF-005 | Attempt to reject a client without providing a reason | Client is in Pending status | 1. Open the Client Detail page for a Pending client<br>2. Click Reject<br>3. Leave the Reason field blank<br>4. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-016 | WF-006 | Attempt to withdraw a client without providing a reason | Client is in Pending status | 1. Open the Client Detail page for a Pending client<br>2. Click Withdraw<br>3. Leave the Reason field blank<br>4. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-017 | WF-007 | Attempt to activate a client without providing an Activation Date | Client is in Pending status | 1. Open the Client Detail page for a Pending client<br>2. Click Activate<br>3. Leave the Activation Date field blank<br>4. Click Submit | Inline validation error appears on the Activation Date field indicating it is required | high |
| TC-018 | WF-008 | Attempt to transfer a client to the same office | Client is in Active status | 1. Open the Client Detail page for an Active client<br>2. Click Transfer Client<br>3. Select the same office as the current office<br>4. Click Submit | Status remains Active; no transition occurs; error shown indicating transfer to the same office is blocked | high |
| TC-019 | WF-009 | Attempt to close a client without providing a closure reason | Client is in Active status | 1. Open the Client Detail page for an Active client<br>2. Click Close<br>3. Leave the Closure Reason field blank<br>4. Click Submit | Inline validation error appears on the Closure Reason field indicating it is required | high |
| TC-020 | WF-010 | Attempt to reactivate a client that is already active | Client is in Active status | 1. Open the Client Detail page for an Active client<br>2. Click Reactivate<br>3. Click Submit | Status remains Active; no transition occurs; error shown indicating client cannot be reactivated while active | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-002 | Submit Create Client form with required fields filled at their minimum valid lengths | User is on the Create Client form | 1. Enter minimum valid length in the First Name field<br>2. Enter minimum valid length in the Last Name field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Client is created in Pending status. | medium |
| TC-022 (boundary) | WF-002 | Submit Create Client form with required fields filled at their maximum valid lengths | User is on the Create Client form | 1. Enter maximum valid length in the First Name field<br>2. Enter maximum valid length in the Last Name field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Client is created in Pending status. | medium |
| TC-023 (boundary) | WF-002 | Submit Create Client form with duplicate External ID | User is on the Create Client form, An existing client has the same External ID | 1. Enter duplicate External ID in the External ID field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Error message displayed indicating External ID must be unique. | medium |
| TC-024 (boundary) | WF-007 | Activate Client with Activation Date set to submission date | User is on the Client Detail page for a Pending client | 1. Enter today's date in the Activation Date field<br>2. Click Activate | Client is activated successfully. | medium |
| TC-025 (boundary) | WF-007 | Activate Client with Activation Date set to one day before submission date | User is on the Client Detail page for a Pending client | 1. Enter yesterday's date in the Activation Date field<br>2. Click Activate | Error message displayed indicating Activation Date must not be before submission date. | medium |

---

## Group Management

Total: **22** (positive: 7, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new group successfully | User logged in as <role> | 1. Click 'Create Group' button<br>2. Enter <valid group name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid staff> in the Staff field<br>5. Enter <valid date> in the Submitted On field<br>6. Check the Active checkbox<br>7. Enter <valid external id> in the External Id field<br>8. Click 'Add Clients' and select <existing client><br>9. Click 'Submit' | A success notification is displayed; the page shows 'Group created successfully' | high |
| TC-002 | WF-002 | Bulk import groups successfully | User logged in as <role> | 1. Click 'Bulk Import Groups' button<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid staff> from the Staff dropdown<br>4. Click 'Download' to get the Groups Template<br>5. Upload a valid groups file in the Groups Upload panel<br>6. Click 'Upload' | A success notification is displayed; the page shows 'Groups imported successfully' | high |
| TC-003 | WF-003 | Activate a group successfully | User logged in as <role>, Group is in 'Pending' status | 1. Click the group name link to open the Group Detail page<br>2. Click 'Activate' button | A success notification is displayed; the page shows 'Group activated successfully' | high |
| TC-004 | WF-004 | Edit a group successfully | User logged in as <role>, Group is in 'Active' status | 1. Click the group name link to open the Group Detail page<br>2. Click 'Edit' button<br>3. Update the Name field with <new valid group name><br>4. Click 'Submit' | A success notification is displayed; the page shows 'Group details updated successfully' | high |
| TC-005 | WF-005 | Close a group successfully | User logged in as <role>, Group is in 'Active' status | 1. Click the group name link to open the Group Detail page<br>2. Click 'Close' button | A success notification is displayed; the page shows 'Group closed successfully' | high |
| TC-006 | WF-006 | Assign staff to a group successfully | User logged in as <role>, Group is in 'Active' status | 1. Click the group name link to open the Group Detail page<br>2. Click 'Assign Staff' button<br>3. Select <valid staff> from the staff list<br>4. Click 'Submit' | A success notification is displayed; the page shows 'Staff assigned successfully' | high |
| TC-007 | WF-007 | Transfer clients from a group successfully | User logged in as <role>, Group is in 'Active' status | 1. Click the group name link to open the Group Detail page<br>2. Click 'Transfer Clients' button<br>3. Select <valid client> from the list<br>4. Click 'Submit' | A success notification is displayed; the page shows 'Clients transferred successfully' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Leave the Name field blank when creating a new group |  | 1. Open the Create Group form<br>2. Leave the Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-001 | Leave the Office field blank when creating a new group |  | 1. Open the Create Group form<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-010 | WF-001 | Leave the Submitted On field blank when creating a new group |  | 1. Open the Create Group form<br>2. Leave the Submitted On field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 | WF-002 | Attempt to upload a file without selecting a file in the Bulk Import Groups page |  | 1. Open the Bulk Import Groups page<br>2. Leave the file picker blank<br>3. Click Upload | Inline validation error appears indicating a file must be selected | high |
| TC-012 | WF-003 | Attempt to activate a group when it is already active |  | 1. Open the Group Detail page for an active group<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-013 | WF-004 | Attempt to edit a group without making any changes |  | 1. Open the Group Detail page<br>2. Click Edit<br>3. Click Submit without making any changes | Status remains unchanged; no updates occur | medium |
| TC-014 | WF-005 | Attempt to close a group that is already closed |  | 1. Open the Group Detail page for a closed group<br>2. Click Close | Status remains Closed; no transition occurs | medium |
| TC-015 | WF-006 | Attempt to assign staff to a group without selecting any staff |  | 1. Open the Group Detail page<br>2. Click Assign Staff<br>3. Leave the staff selection blank<br>4. Click Submit | Inline validation error appears indicating staff must be selected | high |
| TC-016 | WF-007 | Attempt to transfer clients from a group without selecting any clients |  | 1. Open the Group Detail page<br>2. Click Transfer Clients<br>3. Leave the client selection blank<br>4. Click Submit | Inline validation error appears indicating clients must be selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-001 | Create a new group with minimum required fields | User is on the Create Group form | 1. Enter minimum valid value in the Name field<br>2. Select an Office from the dropdown<br>3. Enter a valid date in the Submitted On field<br>4. Click the Submit button | Form submits successfully; group is created with the minimum required fields | medium |
| TC-018 (boundary) | WF-001 | Create a new group with maximum length Name | User is on the Create Group form | 1. Enter maximum length string in the Name field<br>2. Select an Office from the dropdown<br>3. Enter a valid date in the Submitted On field<br>4. Click the Submit button | Form submits successfully; group is created with the maximum length Name | medium |
| TC-019 (boundary) | WF-002 | Bulk import groups with file at exact size limit | User is on the Bulk Import Groups page | 1. Select a file that is exactly at the size limit for upload<br>2. Click the Upload button | Groups imported successfully; visible success indicator shown | medium |
| TC-020 (boundary) | WF-002 | Bulk import groups with file over size limit | User is on the Bulk Import Groups page | 1. Select a file that exceeds the size limit for upload<br>2. Click the Upload button | Upload is blocked; visible error indicating the file exceeds the size limit | medium |
| TC-021 (state_edge) | WF-003 | Rapid consecutive activation of a group | User is on the Group Detail page of an inactive group | 1. Click the Activate button<br>2. Immediately click the Activate button again | First activation succeeds; second activation is blocked with a message indicating the group is already active | medium |
| TC-022 (state_edge) | WF-005 | Rapid consecutive closing of a group | User is on the Group Detail page of an active group | 1. Click the Close button<br>2. Immediately click the Close button again | First closing succeeds; second closing is blocked with a message indicating the group is already closed | medium |

---

## Center Management

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Import Centers successfully | User logged in as <role> | 1. Click 'Import Center' button<br>2. Select a <valid file type> for upload<br>3. Click 'Submit' to import | A success notification is displayed; 'Centers imported successfully' is shown | high |
| TC-002 | WF-002 | Create Center successfully | User logged in as <role> | 1. Click 'Create Center' button<br>2. Enter <valid center name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid external id> in the External Id field<br>5. Check the Active checkbox<br>6. Click 'Submit' | A success notification is displayed; 'Center created successfully' is shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-004 | WF-002 | Leave the Office field blank and submit the Create Center form |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-005 | WF-002 | Leave the Submitted On field blank and submit the Create Center form |  | 1. Leave the Submitted On field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-006 |  | Unauthenticated user attempts to access the Create Center form |  | 1. Navigate to the Create Center page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Submit with minimum required Name length | User is on the Create Center form | 1. Enter a single character in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating the Name must be at least 2 characters long | medium |
| TC-008 (boundary) | WF-002 | Submit with maximum required Name length | User is on the Create Center form | 1. Enter the maximum allowed length string in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; center is created with the maximum length Name | medium |
| TC-009 (input_edge) |  | Submit with leading and trailing whitespace in Name | User is on the Create Center form | 1. Enter '  Center Name  ' in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown on the detail page has no extra spaces | low |
| TC-010 (input_edge) |  | Submit with special characters in Name | User is on the Create Center form | 1. Enter '!@#$%^&*()' in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating invalid characters in the Name field | low |

---

## Loan Products

Total: **19** (positive: 8, negative: 3, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Navigate to Step 1 of the loan product creation wizard | User logged in as <role> | 1. Click '+ Create Loan Product' button | Navigated to Step 1 of the loan product creation wizard | high |
| TC-002 | WF-002 | Navigate to Step 2 of the loan product creation wizard | User logged in as <role>, Navigated to Step 1 of the loan product creation wizard | 1. Fill in required fields in Step 1<br>2. Click 'Next' button | Navigated to Step 2 of the loan product creation wizard | high |
| TC-003 | WF-003 | Navigate to Step 3 of the loan product creation wizard | User logged in as <role>, Navigated to Step 2 of the loan product creation wizard | 1. Fill in required fields in Step 2<br>2. Click 'Next' button | Navigated to Step 3 of the loan product creation wizard | high |
| TC-004 | WF-004 | Navigate to Step 4 of the loan product creation wizard | User logged in as <role>, Navigated to Step 3 of the loan product creation wizard | 1. Fill in required fields in Step 3<br>2. Click 'Next' button | Navigated to Step 4 of the loan product creation wizard | high |
| TC-005 | WF-005 | Navigate to Step 5 of the loan product creation wizard | User logged in as <role>, Navigated to Step 4 of the loan product creation wizard | 1. Fill in required fields in Step 4<br>2. Click 'Next' button | Navigated to Step 5 of the loan product creation wizard | high |
| TC-006 | WF-006 | Navigate to Step 6 of the loan product creation wizard | User logged in as <role>, Navigated to Step 5 of the loan product creation wizard | 1. Fill in required fields in Step 5<br>2. Click 'Next' button | Navigated to Step 6 of the loan product creation wizard | high |
| TC-007 | WF-007 | Open detail view of the selected loan product | User logged in as <role>, Loan products are listed in the data table | 1. Click on the Name link of an existing loan product | Opened detail view of the selected loan product | high |
| TC-008 | WF-008 | Open edit interface for the selected loan product | User logged in as <role>, Opened detail view of the selected loan product | 1. Click 'Edit' button | Opened edit interface for the selected loan product | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Product Name field blank and submit |  | 1. Click on '+ Create Loan Product'<br>2. Leave the Product Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-010 | WF-001 | Leave the Short Name field blank and submit |  | 1. Click on '+ Create Loan Product'<br>2. Leave the Short Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-011 | WF-001 | Submit with all required fields empty |  | 1. Click on '+ Create Loan Product'<br>2. Leave all required fields empty<br>3. Click Next | Form does not submit; error shown on Product Name and Short Name fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Product Name minimum length | User is on the Create Loan Product Step 1 wizard | 1. Enter a single character in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Inline validation error displays: 'Product Name must be at least 2 characters long' | medium |
| TC-013 (boundary) | WF-001 | Product Name maximum length | User is on the Create Loan Product Step 1 wizard | 1. Enter a string of 255 characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the maximum length Product Name | medium |
| TC-014 (boundary) | WF-002 | Principal Amount minimum value | User is on the Create Loan Product Step 2 wizard | 1. Enter the minimum Principal Amount in the field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the minimum Principal Amount | medium |
| TC-015 (boundary) | WF-002 | Principal Amount maximum value | User is on the Create Loan Product Step 2 wizard | 1. Enter the maximum Principal Amount in the field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the maximum Principal Amount | medium |
| TC-016 (boundary) | WF-003 | Number of Repayments minimum value | User is on the Create Loan Product Step 4 wizard | 1. Enter the minimum Number of Repayments<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the minimum Number of Repayments | medium |
| TC-017 (boundary) | WF-003 | Number of Repayments maximum value | User is on the Create Loan Product Step 4 wizard | 1. Enter the maximum Number of Repayments<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; entity is created with the maximum Number of Repayments | medium |
| TC-018 (input_edge) |  | Enter long text in Description field | User is on the Create Loan Product Step 1 wizard | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; Description is saved as entered without truncation | low |
| TC-019 (input_edge) |  | Enter special characters in Product Name | User is on the Create Loan Product Step 1 wizard | 1. Enter special characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; Product Name is saved as entered | low |

---

## Savings Products

Total: **8** (positive: 1, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new Savings Product with all required fields filled | User logged in as <Admin>, User is on the Savings Products page | 1. Click '+ Create Savings Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click 'Next' to proceed to Step 2<br>5. Select <Currency> from the Currency dropdown<br>6. Enter <Decimal Places> in the Decimal Places field<br>7. Enter <Currency In Multiples Of> in the Currency In Multiples Of field<br>8. Click 'Next' to proceed to Step 3<br>9. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>10. Select <Interest Compounding Period> from the Interest Compounding Period dropdown<br>11. Select <Interest Posting Period> from the Interest Posting Period dropdown<br>12. Select <Interest Calculated Using> from the Interest Calculated Using dropdown<br>13. Select <Days in Year> from the Days in Year dropdown<br>14. Click 'Next' to proceed to Step 4<br>15. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>16. Enter <Lock-in Period> in the Lock-in Period field<br>17. Check the Apply Withdrawal Fee for Transfers checkbox<br>18. Enter <Minimum Balance for Interest Calculation> in the Minimum Balance for Interest Calculation field<br>19. Check the Enforce Minimum Required Balance checkbox<br>20. Enter <Minimum Required Balance> in the Minimum Required Balance field<br>21. Check the Is Overdraft Allowed checkbox<br>22. Enter <Maximum Overdraft Amount> in the Maximum Overdraft Amount field<br>23. Enter <Overdraft Interest Rate> in the Overdraft Interest Rate field<br>24. Check the Enable Withhold Tax checkbox<br>25. Select <Tax Group> from the Tax Group dropdown<br>26. Check the Enable Dormancy Tracking checkbox<br>27. Enter <Days to Inactive> in the Days to Inactive field<br>28. Enter <Days to Dormancy> in the Days to Dormancy field<br>29. Enter <Days to Escheat> in the Days to Escheat field<br>30. Click 'Next' to proceed to Step 5<br>31. Search and add predefined charges as needed<br>32. Click 'Next' to proceed to Step 6<br>33. Select <None or Cash-based> radio button<br>34. If Cash-based is selected, fill in GL account mappings as required<br>35. Click 'Finish' to complete the creation of the Savings Product | A success message is displayed; the new Savings Product appears in the data table with the entered Product Name and Short Name | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave Product Name blank and submit |  | 1. Click '+ Create Savings Product' button<br>2. Leave the Product Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-003 |  | Leave Short Name blank and submit |  | 1. Click '+ Create Savings Product' button<br>2. Leave the Short Name field blank<br>3. Fill all other required fields<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-004 |  | Submit with all required fields empty |  | 1. Click '+ Create Savings Product' button<br>2. Leave all required fields blank<br>3. Click Next | Form does not submit; errors shown on Product Name and Short Name fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the Product Name field | User is on the Create Savings Product wizard | 1. Navigate to Step 1 (Details)<br>2. Enter a string of 200+ characters in the Product Name field | Product Name field displays an error indicating the input exceeds the maximum length | low |
| TC-006 (input_edge) |  | Enter special characters in the Short Name field | User is on the Create Savings Product wizard | 1. Navigate to Step 1 (Details)<br>2. Enter special characters in the Short Name field | Short Name field displays an error indicating invalid characters | low |
| TC-007 (input_edge) |  | Enter leading and trailing whitespace in the Description field | User is on the Create Savings Product wizard | 1. Navigate to Step 1 (Details)<br>2. Enter '   Sample Description   ' in the Description field | Description field is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-008 (input_edge) |  | Enter zero in the Minimum Opening Balance field | User is on the Create Savings Product wizard | 1. Navigate to Step 4 (Settings)<br>2. Enter '0' in the Minimum Opening Balance field | Form submits successfully and saved record displays '0' in the Minimum Opening Balance field | medium |

---

## Share Products

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Share Product creation wizard | User logged in as <role> | 1. Click '+ Create Share Product' button | Share product creation wizard opened | high |
| TC-002 | WF-002 | Open existing product for editing | User logged in as <role>, At least one product exists | 1. Click on the Product Name link of an existing product | Product details opened for editing | high |
| TC-003 | WF-003 | Delete existing product | User logged in as <role>, At least one product exists | 1. Click on the Product Name link of an existing product<br>2. Click 'Delete' option | Product deleted successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Product Name blank and submit |  | 1. Click on '+ Create Share Product' button<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name and Description fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-005 | WF-001 | Leave all required fields empty and submit |  | 1. Click on '+ Create Share Product' button<br>2. Leave the Product Name, Short Name, Description, Total Number of Shares, and Nominal/Unit Price fields blank<br>3. Click Next | Inline validation errors appear on the Product Name, Short Name, Description, Total Number of Shares, and Nominal/Unit Price fields indicating they are required | high |
| TC-006 | WF-001 | Enter invalid format in Total Number of Shares |  | 1. Click on '+ Create Share Product' button<br>2. Fill in the Product Name, Short Name, and Description fields<br>3. Enter <non-numeric value> in the Total Number of Shares field<br>4. Click Next | Inline validation error appears on the Total Number of Shares field indicating it must be a number | medium |
| TC-007 | WF-001 | Attempt to create a share product without filling required fields in the Accounting step |  | 1. Click on '+ Create Share Product' button<br>2. Fill in all required fields up to Step 6<br>3. Leave the Accounting radio button blank<br>4. Click Next | Inline validation error appears indicating that a selection must be made for Accounting | high |
| TC-008 | WF-003 | Attempt to delete a product without confirmation |  | 1. Click on an existing product<br>2. Click on Delete | No product is deleted; confirmation dialog is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter minimum allowed value for Total Number of Shares | User is on Step 3 of the Create Share Product wizard | 1. Enter <minimum allowed value> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; Total Number of Shares is saved with the minimum allowed value | medium |
| TC-010 (boundary) | WF-001 | Enter one unit below minimum for Total Number of Shares | User is on Step 3 of the Create Share Product wizard | 1. Enter <one unit below minimum> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Total Number of Shares displays an error indicating the value is below the minimum allowed | medium |
| TC-011 (input_edge) | WF-001 | Enter a very long string in the Description field | User is on Step 1 of the Create Share Product wizard | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields<br>3. Click Next | Description field accepts the input; saved value shows the full string or is truncated with a visible indicator | low |
| TC-012 (input_edge) | WF-001 | Enter special characters in the Product Name field | User is on Step 1 of the Create Share Product wizard | 1. Enter special characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | Product Name field accepts the input; saved value shows the correct string with special characters | low |

---

## Charges

Total: **10** (positive: 2, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new charge successfully | User logged in as <role> | 1. Click '+ Create Charge' button<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Select <Currency> from the Currency dropdown<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <Amount> in the Amount field<br>8. Check the Is Penalty checkbox<br>9. Check the Is Active checkbox<br>10. Select <Tax Group> from the Tax Group dropdown<br>11. Select 'Regular' from the Payment Mode dropdown<br>12. Click Submit | Charge definition created | high |
| TC-002 | WF-004 | View charge details successfully | User logged in as <role> | 1. Click on the Charge Name link for an existing charge | Charge details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave Charge Name blank and submit |  | 1. Click '+ Create Charge'<br>2. Leave the Charge Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-004 | WF-001 | Leave Charge Applies To blank and submit |  | 1. Click '+ Create Charge'<br>2. Leave the Charge Applies To field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-005 | WF-001 | Leave Currency blank and submit |  | 1. Click '+ Create Charge'<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-006 | WF-001 | Leave Amount blank and submit |  | 1. Click '+ Create Charge'<br>2. Leave the Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Click '+ Create Charge'<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Charge Name, Charge Applies To, Currency, and Amount fields are highlighted with validation errors | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter a Charge Name with maximum allowed length |  | 1. Click '+ Create Charge' button<br>2. Enter maximum allowed length string in the Charge Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; charge definition is created with the maximum length Charge Name | medium |
| TC-009 (input_edge) | WF-001 | Enter Charge Name with leading and trailing whitespace |  | 1. Click '+ Create Charge' button<br>2. Enter '   Charge Name   ' in the Charge Name field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved Charge Name on detail page shows 'Charge Name' | low |
| TC-010 (input_edge) | WF-001 | Enter Charge Name with special characters |  | 1. Click '+ Create Charge' button<br>2. Enter 'Charge@Name#2023!' in the Charge Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; charge definition is created with the Charge Name 'Charge@Name#2023!' | low |

---

## Floating Rates

Total: **9** (positive: 4, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display Floating Rates data table | User logged in as <Role> | 1. Navigate to the Floating Rates page | The data table displays columns for Floating Rate Name, Is Base Lending Rate, Is Active, and Created By | high |
| TC-002 |  | Open creation form for Floating Rate | User logged in as <Role> | 1. Click the '+ Create Floating Rate' button | The creation form for Floating Rate is displayed with fields for Floating Rate Name, Is Base Lending Rate, Is Active, and Rate Periods table | high |
| TC-003 |  | Create a new Floating Rate with valid data | User logged in as <Role>, Creation form is open | 1. Enter <Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Check the Is Active checkbox<br>4. Click 'Add Row' in the Rate Periods table<br>5. Enter <From Date> in the From Date field<br>6. Enter <Interest Rate> in the Interest Rate field<br>7. Check the Is Differential Rate checkbox<br>8. Click 'Submit' to create the Floating Rate | A success notification is displayed; the new Floating Rate appears in the data table with the entered details | high |
| TC-004 |  | Add multiple Rate Periods to a Floating Rate | User logged in as <Role>, Creation form is open | 1. Enter <Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Check the Is Active checkbox<br>4. Click 'Add Row' in the Rate Periods table<br>5. Enter <From Date 1> in the From Date field<br>6. Enter <Interest Rate 1> in the Interest Rate field<br>7. Click 'Add Row' in the Rate Periods table<br>8. Enter <From Date 2> in the From Date field<br>9. Enter <Interest Rate 2> in the Interest Rate field<br>10. Click 'Submit' to create the Floating Rate | A success notification is displayed; the new Floating Rate appears in the data table with multiple rate periods defined | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Floating Rate Name field blank and submit |  | 1. Click on '+ Create Floating Rate'<br>2. Leave the Floating Rate Name field blank<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-006 |  | Attempt to create a second base lending rate |  | 1. Click on '+ Create Floating Rate'<br>2. Fill the Floating Rate Name field with '<valid name>'<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit | Error shown indicating that only one base rate can exist at a time; the Floating Rate is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long Floating Rate Name | User is on the Create Floating Rate form | 1. Enter a string of 200+ characters in the Floating Rate Name field | Field displays an error indicating the name is too long or is truncated to fit the maximum allowed length | low |
| TC-008 (input_edge) |  | Enter special characters in Floating Rate Name | User is on the Create Floating Rate form | 1. Enter special characters (e.g., @#$%^&*) in the Floating Rate Name field | Field displays an error indicating invalid characters or accepts the input without error | low |
| TC-009 (input_edge) |  | Enter Floating Rate Name with leading/trailing whitespace | User is on the Create Floating Rate form | 1. Enter '   Rate Name   ' in the Floating Rate Name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Delinquency Management

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new Delinquency Range | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <Classification> in the Classification field<br>4. Enter <Minimum Age Days> in the Minimum Age Days field<br>5. Leave Maximum Age Days field blank<br>6. Click Submit | Delinquency range created; success message shown | high |
| TC-002 | WF-002 | Create a new Delinquency Bucket | User logged in as <Role> | 1. Navigate to the Delinquency Buckets page<br>2. Click on 'Create Delinquency Bucket'<br>3. Enter <Bucket Name> in the Bucket Name field<br>4. Click 'Add Range'<br>5. Enter '1' in the Minimum Age Days field<br>6. Enter '29' in the Maximum Age Days field<br>7. Click 'Add Range'<br>8. Enter '30' in the Minimum Age Days field<br>9. Enter '59' in the Maximum Age Days field<br>10. Click 'Add Range'<br>11. Enter '60' in the Minimum Age Days field<br>12. Leave Maximum Age Days field blank<br>13. Click Submit | Delinquency bucket created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave Classification field blank and submit |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-004 | WF-001 | Submit Create Delinquency Range form with all required fields empty |  | 1. Leave the Classification field blank<br>2. Leave the Minimum Age Days field blank<br>3. Click Submit | Form does not submit; Classification field displays an error: 'Must be a valid value'; Minimum Age Days field displays an error: 'Must be a valid number' | high |
| TC-005 | WF-002 | Leave Bucket Name field blank and submit |  | 1. Leave the Bucket Name field blank<br>2. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-006 | WF-002 | Submit Create Delinquency Bucket form with all required fields empty |  | 1. Leave the Bucket Name field blank<br>2. Click Submit | Form does not submit; Bucket Name field displays an error: 'Must be a valid value' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Minimum Age Days at lower boundary |  | 1. Enter exactly 0 in the Minimum Age Days field<br>2. Fill in the Classification field<br>3. Click Submit | Form submits successfully; delinquency range created with Minimum Age Days set to 0 | medium |
| TC-008 (boundary) | WF-001 | Minimum Age Days below lower boundary |  | 1. Enter -1 in the Minimum Age Days field<br>2. Fill in the Classification field<br>3. Click Submit | Form submission is blocked; error message displayed indicating Minimum Age Days must be 0 or greater | medium |
| TC-009 (boundary) | WF-001 | Maximum Age Days with no value |  | 1. Enter a value in the Minimum Age Days field<br>2. Fill in the Classification field<br>3. Leave the Maximum Age Days field blank<br>4. Click Submit | Form submits successfully; delinquency range created with Maximum Age Days applying to all days beyond the Minimum Age Days | medium |
| TC-010 (input_edge) | WF-002 | Long Bucket Name |  | 1. Enter a string of 200 characters in the Bucket Name field<br>2. Click Submit | Form submits successfully; delinquency bucket created with the long Bucket Name displayed correctly | low |

---

## Loan Account

Total: **17** (positive: 1, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application from Step 1 to Step 4 | User logged in as <Loan Officer>, Client Detail page is open | 1. Click 'Start Loan Application' button<br>2. Select <Product Name> from the Product Name dropdown<br>3. Enter <Loan Officer> in the Loan Officer field<br>4. Select <Loan Purpose> from the Loan Purpose dropdown<br>5. Select <Fund> from the Fund dropdown<br>6. Enter <valid date> in the Submitted On date field<br>7. Enter <valid date> in the Expected Disbursement Date field<br>8. Enter <valid principal amount> in the Principal field<br>9. Enter <valid number of repayments> in the Number of Repayments field<br>10. Select <frequency> from the Repaid Every dropdown<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Enter <External ID> in the External ID field<br>13. Click 'Next' to proceed to Step 2<br>14. Select <Repayment Strategy> from the Repayment Strategy dropdown<br>15. Select <Amortization> from the Amortization dropdown<br>16. Select <Interest Method> from the Interest Method dropdown<br>17. Select <Interest Calculation Period> from the Interest Calculation Period dropdown<br>18. Enter <valid grace period> in the Grace Period field<br>19. Click 'Next' to proceed to Step 3<br>20. Click 'Add Charge' button<br>21. Enter <Charge Name> in the Charge Name field<br>22. Enter <valid charge amount> in the Charge Amount field<br>23. Click 'Next' to proceed to Step 4<br>24. Click 'Add Collateral' button<br>25. Select <Collateral Type> from the Collateral Type dropdown<br>26. Enter <valid collateral value> in the Value field<br>27. Enter <Collateral Description> in the Description field<br>28. Click 'Submit' to create the loan | Loan created in 'Submitted and Pending Approval' status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave all required fields blank in Loan Application form |  | 1. Leave the Product Name dropdown blank<br>2. Leave the Loan Officer field blank<br>3. Leave the Loan Purpose field blank<br>4. Leave the Fund field blank<br>5. Leave the Submitted On date blank<br>6. Leave the Expected Disbursement Date blank<br>7. Leave the Principal field blank<br>8. Leave the Number of Repayments field blank<br>9. Leave the Repaid Every frequency field blank<br>10. Leave the Repaid Every unit field blank<br>11. Leave the Interest Rate field blank<br>12. Leave the External ID field blank<br>13. Click Submit | Form does not submit; error shown on all required fields indicating they are required | high |
| TC-003 | WF-001 | Submit Loan Application with invalid Principal amount |  | 1. Select a Product Name from the dropdown<br>2. Fill in the Loan Officer field<br>3. Fill in the Loan Purpose field<br>4. Fill in the Fund field<br>5. Fill in the Submitted On date<br>6. Fill in the Expected Disbursement Date<br>7. Enter <amount below minimum> in the Principal field<br>8. Fill in the Number of Repayments field<br>9. Fill in the Repaid Every frequency field<br>10. Fill in the Repaid Every unit field<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Fill in the External ID field<br>13. Click Submit | Form does not submit; error shown on Principal field indicating it must be within product min/max | high |
| TC-004 | WF-002 | Attempt to approve loan application when status is not Pending Approval | Loan application is in Approved status | 1. Click Approve | Action is blocked; no approval dialog appears; current status remains Approved | high |
| TC-005 | WF-003 | Attempt to reject loan application when status is not Pending Approval | Loan application is in Approved status | 1. Click Reject | Action is blocked; no rejection dialog appears; current status remains Approved | high |
| TC-006 | WF-004 | Attempt to withdraw loan application when status is not Pending Approval | Loan application is in Approved status | 1. Click Withdraw | Action is blocked; no withdrawal dialog appears; current status remains Approved | high |
| TC-007 | WF-005 | Attempt to disburse loan when status is not Approved | Loan application is in Pending Approval status | 1. Click Disburse | Action is blocked; no disbursement form appears; current status remains Pending Approval | high |
| TC-008 | WF-006 | Attempt to make repayment when status is not Active | Loan application is in Approved status | 1. Click Make Repayment | Action is blocked; no repayment form appears; current status remains Approved | high |
| TC-009 | WF-007 | Attempt to close loan when status is not Active | Loan application is in Approved status | 1. Click Close | Action is blocked; no closure confirmation appears; current status remains Approved | high |
| TC-010 | WF-008 | Attempt to prepay loan when status is not Active | Loan application is in Approved status | 1. Click Prepay Loan | Action is blocked; no prepayment form appears; current status remains Approved | high |
| TC-011 | WF-009 | Attempt to charge off loan when status is not Active | Loan application is in Approved status | 1. Click Charge Off | Action is blocked; no charge off confirmation appears; current status remains Approved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Submit Loan Application with Principal at minimum value | User is on Step 1 of the Loan Application wizard | 1. Select a Product Name from the dropdown<br>2. Enter Loan Officer<br>3. Enter Loan Purpose<br>4. Enter Fund<br>5. Set Submitted On date to today<br>6. Set Expected Disbursement Date to tomorrow<br>7. Enter Principal at the minimum allowed value<br>8. Enter Number of Repayments<br>9. Select Repaid Every frequency<br>10. Enter Interest Rate at the minimum allowed value<br>11. Enter External ID<br>12. Click Submit | Loan is created in 'Submitted and Pending Approval' status | medium |
| TC-013 (boundary) | WF-001 | Submit Loan Application with Principal just below minimum value | User is on Step 1 of the Loan Application wizard | 1. Select a Product Name from the dropdown<br>2. Enter Loan Officer<br>3. Enter Loan Purpose<br>4. Enter Fund<br>5. Set Submitted On date to today<br>6. Set Expected Disbursement Date to tomorrow<br>7. Enter Principal just below the minimum allowed value<br>8. Enter Number of Repayments<br>9. Select Repaid Every frequency<br>10. Enter Interest Rate at the minimum allowed value<br>11. Enter External ID<br>12. Click Submit | Form submission is blocked; error message displayed indicating the Principal must meet the minimum value | medium |
| TC-014 (boundary) | WF-001 | Submit Loan Application with Interest Rate at maximum value | User is on Step 1 of the Loan Application wizard | 1. Select a Product Name from the dropdown<br>2. Enter Loan Officer<br>3. Enter Loan Purpose<br>4. Enter Fund<br>5. Set Submitted On date to today<br>6. Set Expected Disbursement Date to tomorrow<br>7. Enter Principal at the minimum allowed value<br>8. Enter Number of Repayments<br>9. Select Repaid Every frequency<br>10. Enter Interest Rate at the maximum allowed value<br>11. Enter External ID<br>12. Click Submit | Loan is created in 'Submitted and Pending Approval' status | medium |
| TC-015 (boundary) | WF-001 | Submit Loan Application with Interest Rate just above maximum value | User is on Step 1 of the Loan Application wizard | 1. Select a Product Name from the dropdown<br>2. Enter Loan Officer<br>3. Enter Loan Purpose<br>4. Enter Fund<br>5. Set Submitted On date to today<br>6. Set Expected Disbursement Date to tomorrow<br>7. Enter Principal at the minimum allowed value<br>8. Enter Number of Repayments<br>9. Select Repaid Every frequency<br>10. Enter Interest Rate just above the maximum allowed value<br>11. Enter External ID<br>12. Click Submit | Form submission is blocked; error message displayed indicating the Interest Rate exceeds the maximum allowed value | medium |
| TC-016 (input_edge) |  | Enter long description in Collateral Description field | User is on Step 4 of the Loan Application wizard | 1. Click 'Add Charge'<br>2. Enter Collateral Type<br>3. Enter Value<br>4. Enter a long description (over 200 characters) in the Description field<br>5. Click Submit | Form submission is blocked; error message displayed indicating the Description exceeds maximum length | low |
| TC-017 (input_edge) |  | Enter special characters in External ID field | User is on Step 1 of the Loan Application wizard | 1. Select a Product Name from the dropdown<br>2. Enter Loan Officer<br>3. Enter Loan Purpose<br>4. Enter Fund<br>5. Set Submitted On date to today<br>6. Set Expected Disbursement Date to tomorrow<br>7. Enter Principal at the minimum allowed value<br>8. Enter Number of Repayments<br>9. Select Repaid Every frequency<br>10. Enter Interest Rate at the minimum allowed value<br>11. Enter External ID with special characters<br>12. Click Submit | Form submission is blocked; error message displayed indicating invalid characters in External ID | low |

---

## Savings Account

Total: **11** (positive: 1, negative: 10, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit new savings account creation form | User logged in as <Role>, Client Detail page is open | 1. Select <Product Name> from the Product Name dropdown<br>2. Enter <Field Officer> in the Field Officer field<br>3. Select <Submitted On date> from the date picker<br>4. Enter <Nominal Annual Interest Rate> in the Nominal Annual Interest Rate field<br>5. Select <Interest Compounding Period> from the dropdown<br>6. Select <Interest Posting Period> from the dropdown<br>7. Select <Interest Calculated Using> from the dropdown<br>8. Enter <Days in Year> in the Days in Year field<br>9. Enter <Minimum Opening Balance> in the Minimum Opening Balance field<br>10. Enter <Lock-in Period> in the Lock-in Period field<br>11. Check the Allow Overdraft checkbox<br>12. Click 'Submit' | Account created in 'Submitted and Pending Approval' status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit savings account creation form with all required fields empty |  | 1. Leave the Product Name dropdown blank<br>2. Leave the Field Officer field blank<br>3. Leave the Submitted On date blank<br>4. Leave the Nominal Annual Interest Rate field blank<br>5. Leave the Interest Compounding Period dropdown blank<br>6. Leave the Interest Posting Period dropdown blank<br>7. Leave the Interest Calculated Using dropdown blank<br>8. Leave the Days in Year dropdown blank<br>9. Leave the Minimum Opening Balance field blank<br>10. Leave the Lock-in Period field blank<br>11. Leave the Allow Overdraft checkbox unchecked<br>12. Click Submit | Form does not submit; all required fields are highlighted with inline validation errors indicating they are required | high |
| TC-003 | WF-001 | Submit savings account creation form with invalid email format |  | 1. Select a product from the Product Name dropdown<br>2. Fill in the Field Officer field with <invalid email format><br>3. Fill in the Submitted On date with a valid date<br>4. Fill in the Nominal Annual Interest Rate field with a valid number<br>5. Fill in the Interest Compounding Period dropdown with a valid selection<br>6. Fill in the Interest Posting Period dropdown with a valid selection<br>7. Fill in the Interest Calculated Using dropdown with a valid selection<br>8. Fill in the Days in Year dropdown with a valid selection<br>9. Fill in the Minimum Opening Balance field with a valid number<br>10. Fill in the Lock-in Period field with a valid number<br>11. Leave the Allow Overdraft checkbox unchecked<br>12. Click Submit | Inline validation error appears on the Field Officer field indicating 'Must be a valid email address' | medium |
| TC-004 | WF-002 | Attempt to approve a savings account application that is not in 'Submitted and Pending Approval' status |  | 1. Attempt to approve a savings account application that is in 'Active' status<br>2. Click Approve | Action is blocked; no approval occurs and the account status remains 'Active' | high |
| TC-005 | WF-003 | Attempt to reject a savings account application that is not in 'Submitted and Pending Approval' status |  | 1. Attempt to reject a savings account application that is in 'Approved' status<br>2. Click Reject | Action is blocked; no rejection occurs and the account status remains 'Approved' | high |
| TC-006 | WF-004 | Attempt to withdraw a savings account application that is not in 'Submitted and Pending Approval' status |  | 1. Attempt to withdraw a savings account application that is in 'Approved' status<br>2. Click Withdraw Application | Action is blocked; no withdrawal occurs and the account status remains 'Approved' | high |
| TC-007 | WF-005 | Attempt to activate a savings account that is not in 'Approved' status |  | 1. Attempt to activate a savings account that is in 'Submitted and Pending Approval' status<br>2. Click Activate | Action is blocked; no activation occurs and the account status remains 'Submitted and Pending Approval' | high |
| TC-008 | WF-006 | Attempt to undo approval of a savings account that is not in 'Approved' status |  | 1. Attempt to undo approval of a savings account that is in 'Active' status<br>2. Click Undo Approval | Action is blocked; no undo occurs and the account status remains 'Active' | high |
| TC-009 | WF-007 | Attempt to deposit into a savings account that is not in 'Active' status |  | 1. Attempt to deposit into a savings account that is in 'Submitted and Pending Approval' status<br>2. Click Deposit | Action is blocked; no deposit occurs and the account status remains 'Submitted and Pending Approval' | high |
| TC-010 | WF-008 | Attempt to withdraw from a savings account that is not in 'Active' status |  | 1. Attempt to withdraw from a savings account that is in 'Approved' status<br>2. Click Withdraw | Action is blocked; no withdrawal occurs and the account status remains 'Approved' | high |
| TC-011 | WF-011 | Attempt to close a savings account that is not in 'Active' status |  | 1. Attempt to close a savings account that is in 'Approved' status<br>2. Click Close | Action is blocked; no closure occurs and the account status remains 'Approved' | high |

---

## Share Account

Total: **24** (positive: 8, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application | User logged in as <role>, Client is selected on the Client Detail page | 1. Select <share product> from the Share Product dropdown<br>2. Enter <submitted on date> in the Submitted On field<br>3. Enter <requested shares> in the Requested Shares field<br>4. Enter <application date> in the Application Date field<br>5. Select <active savings account> from the Savings Account for Charges dropdown<br>6. Enter <external ID> in the External ID field<br>7. Fill in the Charges section as required<br>8. Click Submit | Account created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-002 | Approve Pending Share Account | User logged in as <role>, Share account is in 'Submitted and Pending Approval' status | 1. Click Approve on the Share Account Detail page<br>2. Enter <approved shares> in the Approved Shares field<br>3. Enter <approved date> in the Approved Date field<br>4. Click Confirm on the Approval dialog | Share account approved with Approved Shares and Approved Date | high |
| TC-003 | WF-003 | Reject Pending Share Account | User logged in as <role>, Share account is in 'Submitted and Pending Approval' status | 1. Click Reject on the Share Account Detail page<br>2. Click Confirm on the Reject dialog | Share account rejected | high |
| TC-004 | WF-004 | Activate Approved Share Account | User logged in as <role>, Share account is in 'Approved' status | 1. Click Activate on the Share Account Detail page<br>2. Click Confirm on the Activation dialog | Share account activated | high |
| TC-005 | WF-005 | Undo Approval of Share Account | User logged in as <role>, Share account is in 'Approved' status | 1. Click Undo Approval on the Share Account Detail page<br>2. Click Confirm on the Undo Approval dialog | Share account approval undone | high |
| TC-006 | WF-006 | Apply Additional Shares to Active Share Account | User logged in as <role>, Share account is in 'Active' status | 1. Click Apply Additional Shares on the Share Account Detail page<br>2. Enter <additional shares> in the Additional Shares field<br>3. Click Confirm on the Apply Additional Shares dialog | Additional shares applied | high |
| TC-007 | WF-007 | Redeem Shares from Active Share Account | User logged in as <role>, Share account is in 'Active' status | 1. Click Redeem Shares on the Share Account Detail page<br>2. Enter <shares to redeem> in the Shares to Redeem field<br>3. Click Confirm on the Redeem Shares dialog | Redemption amount credited to linked savings account | high |
| TC-008 | WF-008 | Close Active Share Account | User logged in as <role>, Share account is in 'Active' status | 1. Click Close on the Share Account Detail page<br>2. Click Confirm on the Close dialog | Share account closed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Share Product field displays an error: 'This field is required' | high |
| TC-010 | WF-001 | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Submitted On field displays an error: 'This field is required' | high |
| TC-011 | WF-001 | Leave the Requested Shares blank and submit |  | 1. Leave the Requested Shares blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Requested Shares field displays an error: 'This field is required' | high |
| TC-012 | WF-001 | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application Date field displays an error: 'This field is required' | high |
| TC-013 | WF-001 | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Savings Account for Charges field displays an error: 'This field is required' | high |
| TC-014 | WF-002 | Attempt to approve a share account that is not in Pending status | Share account is in Approved status | 1. Navigate to the Share Account Detail page<br>2. Click Approve | Form does not submit; status remains Approved; no transition occurs | high |
| TC-015 | WF-003 | Attempt to reject a share account that is not in Pending status | Share account is in Approved status | 1. Navigate to the Share Account Detail page<br>2. Click Reject | Form does not submit; status remains Approved; no transition occurs | high |
| TC-016 | WF-004 | Attempt to activate a share account that is not in Approved status | Share account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page<br>2. Click Activate | Form does not submit; status remains Submitted and Pending Approval; no transition occurs | high |
| TC-017 | WF-005 | Attempt to undo approval of a share account that is not in Approved status | Share account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page<br>2. Click Undo Approval | Form does not submit; status remains Submitted and Pending Approval; no transition occurs | high |
| TC-018 | WF-006 | Attempt to apply additional shares to a share account that is not in Active status | Share account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page<br>2. Click Apply Additional Shares | Form does not submit; status remains Submitted and Pending Approval; no transition occurs | high |
| TC-019 | WF-007 | Attempt to redeem shares from a share account that is not in Active status | Share account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page<br>2. Click Redeem Shares | Form does not submit; status remains Submitted and Pending Approval; no transition occurs | high |
| TC-020 | WF-008 | Attempt to close a share account that is not in Active status | Share account is in Submitted and Pending Approval status | 1. Navigate to the Share Account Detail page<br>2. Click Close | Form does not submit; status remains Submitted and Pending Approval; no transition occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Submit Share Account Application with minimum requested shares | Client has a valid share product with a minimum requested shares constraint | 1. Select a share product from the Share Product dropdown<br>2. Enter the Submitted On date<br>3. Enter the minimum requested shares in the Requested Shares field<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter an External ID<br>7. Click Submit | Share account is created in 'Submitted and Pending Approval' status | medium |
| TC-022 (boundary) | WF-001 | Submit Share Account Application with maximum requested shares | Client has a valid share product with a maximum requested shares constraint | 1. Select a share product from the Share Product dropdown<br>2. Enter the Submitted On date<br>3. Enter the maximum requested shares in the Requested Shares field<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter an External ID<br>7. Click Submit | Share account is created in 'Submitted and Pending Approval' status | medium |
| TC-023 (boundary) | WF-001 | Submit Share Account Application with one less than minimum requested shares | Client has a valid share product with a minimum requested shares constraint | 1. Select a share product from the Share Product dropdown<br>2. Enter the Submitted On date<br>3. Enter one less than the minimum requested shares in the Requested Shares field<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter an External ID<br>7. Click Submit | Submission is blocked; error message displayed indicating insufficient shares | medium |
| TC-024 (boundary) | WF-001 | Submit Share Account Application with one more than maximum requested shares | Client has a valid share product with a maximum requested shares constraint | 1. Select a share product from the Share Product dropdown<br>2. Enter the Submitted On date<br>3. Enter one more than the maximum requested shares in the Requested Shares field<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Enter an External ID<br>7. Click Submit | Submission is blocked; error message displayed indicating too many shares requested | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **21** (positive: 11, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Fixed Deposit Account successfully | User logged in as <Role>, Client Detail page is open | 1. Select <Fixed Deposit Product> from the Fixed Deposit Product dropdown<br>2. Enter <valid deposit amount> in the Deposit Amount field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select <Maturity Instructions> from the Maturity Instructions dropdown<br>5. Click Submit | Fixed Deposit Account created successfully | high |
| TC-002 | WF-002 | Create Recurring Deposit Account successfully | User logged in as <Role>, Client Detail page is open | 1. Select <Recurring Deposit Product> from the Recurring Deposit Product dropdown<br>2. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount per installment field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select <Deposit Frequency> from the Deposit Frequency dropdown<br>5. Enter <valid expected first deposit date> in the Expected First Deposit On field<br>6. Click Submit | Recurring Deposit Account created successfully | high |
| TC-003 | WF-003 | Approve Fixed Deposit Account successfully | User logged in as <Role>, Fixed Deposit Account Detail page is open | 1. Click Approve | Fixed Deposit Account approved | medium |
| TC-004 | WF-004 | Activate Fixed Deposit Account successfully | User logged in as <Role>, Fixed Deposit Account Detail page is open | 1. Click Activate | Fixed Deposit Account activated | medium |
| TC-005 | WF-005 | Premature Close Fixed Deposit Account successfully | User logged in as <Role>, Fixed Deposit Account Detail page is open | 1. Click Premature Close | Fixed Deposit Account closed prematurely | medium |
| TC-006 | WF-006 | Close Fixed Deposit Account on Maturity successfully | User logged in as <Role>, Fixed Deposit Account Detail page is open | 1. Click Close on Maturity | Fixed Deposit Account closed on maturity | medium |
| TC-007 | WF-007 | Approve Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit Account Detail page is open | 1. Click Approve | Recurring Deposit Account approved | medium |
| TC-008 | WF-008 | Activate Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit Account Detail page is open | 1. Click Activate | Recurring Deposit Account activated | medium |
| TC-009 | WF-009 | Deposit to Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit Account Detail page is open | 1. Click Deposit | Deposit made to Recurring Deposit Account | medium |
| TC-010 | WF-010 | Premature Close Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit Account Detail page is open | 1. Click Premature Close | Recurring Deposit Account closed prematurely | medium |
| TC-011 | WF-011 | Close Recurring Deposit Account on Maturity successfully | User logged in as <Role>, Recurring Deposit Account Detail page is open | 1. Click Close on Maturity | Recurring Deposit Account closed on maturity | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Leave the Deposit Amount blank when creating a Fixed Deposit Account |  | 1. Navigate to the Fixed Deposit Account creation form<br>2. Leave the Deposit Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-013 | WF-002 | Leave the Mandatory Deposit Amount blank when creating a Recurring Deposit Account |  | 1. Navigate to the Recurring Deposit Account creation form<br>2. Leave the Mandatory Deposit Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Mandatory Deposit Amount field indicating it is required | high |
| TC-014 | WF-003 | Attempt to approve a Fixed Deposit Account without meeting preconditions | The Fixed Deposit Account is not created | 1. Navigate to the Fixed Deposit Account detail page<br>2. Click Approve | Status remains 'Pending'; no transition occurs | high |
| TC-015 | WF-004 | Attempt to activate a Fixed Deposit Account without meeting preconditions | The Fixed Deposit Account is not created | 1. Navigate to the Fixed Deposit Account detail page<br>2. Click Activate | Status remains 'Pending'; no transition occurs | high |
| TC-016 | WF-007 | Attempt to approve a Recurring Deposit Account without meeting preconditions | The Recurring Deposit Account is not created | 1. Navigate to the Recurring Deposit Account detail page<br>2. Click Approve | Status remains 'Pending'; no transition occurs | high |
| TC-017 | WF-008 | Attempt to activate a Recurring Deposit Account without meeting preconditions | The Recurring Deposit Account is not created | 1. Navigate to the Recurring Deposit Account detail page<br>2. Click Activate | Status remains 'Pending'; no transition occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-001 | Submit Fixed Deposit Account creation form with minimum deposit amount |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter the minimum allowed Deposit Amount in the Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select Maturity Instructions from the dropdown<br>5. Click Submit | Form submits successfully; Fixed Deposit Account created with the minimum deposit amount | medium |
| TC-019 (boundary) | WF-001 | Submit Fixed Deposit Account creation form with one unit below minimum deposit amount |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter one unit below the minimum allowed Deposit Amount in the Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select Maturity Instructions from the dropdown<br>5. Click Submit | Form submission is blocked; an error message is shown indicating the deposit amount is below the minimum allowed | medium |
| TC-020 (boundary) | WF-002 | Submit Recurring Deposit Account creation form with minimum mandatory deposit amount |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter the minimum allowed Mandatory Deposit Amount per installment in the Mandatory Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select Deposit Frequency from the dropdown<br>5. Enter a valid Expected First Deposit On date<br>6. Click Submit | Form submits successfully; Recurring Deposit Account created with the minimum mandatory deposit amount | medium |
| TC-021 (boundary) | WF-002 | Submit Recurring Deposit Account creation form with one unit below minimum mandatory deposit amount |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter one unit below the minimum allowed Mandatory Deposit Amount per installment in the Mandatory Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select Deposit Frequency from the dropdown<br>5. Enter a valid Expected First Deposit On date<br>6. Click Submit | Form submission is blocked; an error message is shown indicating the mandatory deposit amount is below the minimum allowed | medium |

---

## Accounting — Chart of Accounts

Total: **11** (positive: 3, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new GL Account | User logged in as <Role> | 1. Click '+ Create GL Account'<br>2. Select <Account Type> from the Account Type dropdown<br>3. Select <Parent Account> from the Parent Account dropdown<br>4. Enter <unique GL Code> in the GL Code field<br>5. Enter <Account Name> in the Account Name field<br>6. Select <Account Usage> from the Account Usage dropdown<br>7. Check the Manual Entries Allowed checkbox<br>8. Enter <Description> in the Description field<br>9. Select <Tag> from the Tag dropdown<br>10. Click Submit | A success notification is displayed; the page shows 'GL Account created successfully' | high |
| TC-002 | WF-002 | Edit an existing GL Account | User logged in as <Role>, An existing GL Account is available | 1. Click on the <Account Name> of the existing GL Account<br>2. Click Edit<br>3. Update <Account Name> in the Account Name field<br>4. Click Submit | A success notification is displayed; the page shows 'GL Account updated successfully' | high |
| TC-003 | WF-003 | Delete an existing GL Account | User logged in as <Role>, An existing GL Account is available | 1. Click on the <Account Name> of the existing GL Account<br>2. Click Delete<br>3. Click Confirm on the Delete dialog | A success notification is displayed; the page shows 'GL Account deleted successfully' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Account Type blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the Account Type field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-005 | WF-001 | Leave GL Code blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the GL Code field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-006 | WF-001 | Leave Account Name blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the Account Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Click on '+ Create GL Account'<br>2. Leave the Account Type, GL Code, and Account Name fields blank<br>3. Click Submit | Form does not submit; errors shown on Account Type, GL Code, and Account Name fields indicating they are required | high |
| TC-008 | WF-001 | Submit with duplicate GL Code |  | 1. Click on '+ Create GL Account'<br>2. Enter <duplicate GL Code> in the GL Code field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Error shown indicating 'GL Code must be unique' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Create GL Account with duplicate GL Code | Existing GL Account with GL Code '1001' | 1. Click '+ Create GL Account'<br>2. Enter '1001' in the GL Code field<br>3. Fill all other required fields<br>4. Click Submit | Form submission is blocked; error message 'GL Code must be unique' is displayed. | medium |
| TC-010 (input_edge) | WF-001 | Create GL Account with long Description |  | 1. Click '+ Create GL Account'<br>2. Fill all required fields with valid data<br>3. Enter a long string (200+ characters) in the Description field<br>4. Click Submit | Form submits successfully; the long description is saved and displayed correctly in the detail view. | low |
| TC-011 (input_edge) | WF-001 | Create GL Account with special characters in Account Name |  | 1. Click '+ Create GL Account'<br>2. Enter '@ccountName!' in the Account Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; the account is created with special characters in the name. | low |

---

## Accounting — Journal Entries & Closures

Total: **13** (positive: 3, negative: 7, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Add a new Journal Entry with valid details | User logged in as <Accountant> | 1. Click '+ Add Journal Entry' button<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <reference number> in the Reference Number field<br>5. Enter <valid transaction date> in the Transaction Date field<br>6. Select <payment type> from the Payment Type dropdown<br>7. Enter <payment detail> in the Payment Detail field<br>8. Click 'Add Row' to add an entry line<br>9. Select <valid GL account> from the GL Account dropdown in the new row<br>10. Enter <valid amount> in the Amount field of the new row<br>11. Enter <comments> in the Comments field<br>12. Click 'Submit' button | A success notification is displayed; the new journal entry appears in the data table with the correct details. | high |
| TC-002 |  | Filter Journal Entries by Office | User logged in as <Accountant> | 1. Enter <valid office> in the Office filter<br>2. Click 'Apply Filters' button | The data table displays only journal entries for <valid office>; unrelated entries are no longer visible. | medium |
| TC-003 |  | Create a Closure with valid details | User logged in as <Accountant> | 1. Click '+ Create Closure' button<br>2. Select <valid office> from the Office dropdown<br>3. Enter <valid closing date> in the Closing Date field<br>4. Enter <comments> in the Comments field<br>5. Click 'Submit' button | A success notification is displayed; the new closure appears in the Closing Entries table with the correct details. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Office field blank when adding a journal entry |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-005 |  | Leave the Currency field blank when adding a journal entry |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-006 |  | Leave the Transaction Date field blank when adding a journal entry |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Transaction Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-007 |  | Submit journal entry with total debits not equal to total credits |  | 1. Click on '+ Add Journal Entry'<br>2. Fill in the Office, Currency, and Transaction Date fields<br>3. Add a debit line with an Amount of <amount><br>4. Add a credit line with an Amount of <different amount><br>5. Click Submit | Validation error appears indicating total debits must equal total credits | high |
| TC-008 |  | Leave the Office field blank when creating a closure |  | 1. Click on '+ Create Closure'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-009 |  | Leave the Closing Date field blank when creating a closure |  | 1. Click on '+ Create Closure'<br>2. Leave the Closing Date field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Closing Date field indicating it is required | high |
| TC-010 |  | Attempt to post journal entries for dates on or before the closing date |  | 1. Click on '+ Create Closure'<br>2. Fill in the Office and Closing Date fields with a future date<br>3. Click Submit<br>4. Attempt to post a journal entry with a Transaction Date on or before the closing date | Error is displayed indicating journal entries cannot be posted for dates on or before the closing date | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long comment in the Comments field | User is on the Journal Entries creation form | 1. Enter a string of 200+ characters in the Comments field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked with an error indicating the comment exceeds the maximum length | low |
| TC-012 (input_edge) |  | Enter special characters in the Reference Number field | User is on the Journal Entries creation form | 1. Enter special characters in the Reference Number field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked with an error indicating invalid characters in the Reference Number field | low |
| TC-013 (input_edge) |  | Enter a value with leading/trailing whitespace in the Office field | User is on the Journal Entries creation form | 1. Enter '  Office Name  ' in the Office field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Accounting Rules & Financial Activity Mappings

Total: **16** (positive: 6, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new accounting rule | User logged in as <Role> | 1. Click '+ Create Rule' button<br>2. Select <Office> from the Office dropdown<br>3. Enter <Rule Name> in the Rule Name field<br>4. Select <Debit Account> from the Debit Account dropdown<br>5. Check the 'Allow Multiple Debit Entries' checkbox<br>6. Select <Credit Account> from the Credit Account dropdown<br>7. Check the 'Allow Multiple Credit Entries' checkbox<br>8. Click 'Submit' button | A success message is shown; the new rule appears in the Accounting Rules table | high |
| TC-002 | WF-002 | View accounting rule details | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name link in the Accounting Rules table | Rule details are displayed | high |
| TC-003 | WF-003 | Edit an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name link in the Accounting Rules table<br>2. Click 'Edit' button<br>3. Update <Rule Name> in the Rule Name field<br>4. Click 'Submit' button | A success message is shown; the updated rule appears in the Accounting Rules table | medium |
| TC-004 | WF-004 | Delete an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name link in the Accounting Rules table<br>2. Click 'Delete' button<br>3. Confirm deletion | A success message is shown; the rule no longer appears in the Accounting Rules table | medium |
| TC-005 | WF-005 | Create a new financial activity mapping | User logged in as <Role> | 1. Click '+ Create Mapping' button<br>2. Select <Financial Activity> from the Financial Activity dropdown<br>3. Select <GL Account> from the GL Account dropdown<br>4. Click 'Submit' button | A success message is shown; the new mapping appears in the Financial Activity Mappings table | high |
| TC-006 | WF-006 | View financial activity mapping details | User logged in as <Role>, At least one financial activity mapping exists | 1. Click on the Financial Activity link in the Financial Activity Mappings table | Mapping details are displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Leave the Rule Name field blank when creating a new accounting rule |  | 1. Click on '+ Create Rule'<br>2. Leave the Rule Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Rule Name field indicating it is required | high |
| TC-008 | WF-005 | Leave the Financial Activity field blank when creating a new mapping |  | 1. Click on '+ Create Mapping'<br>2. Leave the Financial Activity field blank<br>3. Select a GL Account<br>4. Click Submit | Inline validation error appears on the Financial Activity field indicating it is required | high |
| TC-009 | WF-005 | Attempt to create a financial activity mapping for an already mapped activity |  | 1. Click on '+ Create Mapping'<br>2. Select an already mapped Financial Activity<br>3. Select a GL Account<br>4. Click Submit | Error message displayed: 'This financial activity is already mapped to a GL account.'; mapping is not created | medium |
| TC-010 | WF-003 | Attempt to edit an accounting rule without filling required fields |  | 1. Click on an existing rule to view its details<br>2. Click on Edit Rule<br>3. Leave the Rule Name field blank<br>4. Click Submit | Inline validation error appears on the Rule Name field indicating it is required; rule is not updated | high |
| TC-011 | WF-004 | Attempt to delete an accounting rule without proper authorization |  | 1. Click on an existing rule to view its details<br>2. Click on Delete Rule | Error message displayed: 'You do not have permission to delete this rule.'; rule remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Create Accounting Rule with minimum required fields |  | 1. Click '+ Create Rule'<br>2. Select an Office from the dropdown<br>3. Enter a valid Rule Name<br>4. Select a Debit Account<br>5. Select a Credit Account<br>6. Click Submit | Form submits successfully; entity is created with the minimum required fields | medium |
| TC-013 (boundary) | WF-001 | Create Accounting Rule with maximum length Rule Name |  | 1. Click '+ Create Rule'<br>2. Select an Office from the dropdown<br>3. Enter a Rule Name with maximum allowed length<br>4. Select a Debit Account<br>5. Select a Credit Account<br>6. Click Submit | Form submits successfully; entity is created with the maximum length Rule Name | medium |
| TC-014 (boundary) | WF-001 | Create Accounting Rule with empty Rule Name |  | 1. Click '+ Create Rule'<br>2. Select an Office from the dropdown<br>3. Leave Rule Name blank<br>4. Select a Debit Account<br>5. Select a Credit Account<br>6. Click Submit | Form submission is blocked; an error message indicates that Rule Name is required | medium |
| TC-015 (boundary) | WF-005 | Create Financial Activity Mapping with duplicate Financial Activity |  | 1. Click '+ Create Mapping'<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account from the dropdown<br>4. Click Submit<br>5. Click '+ Create Mapping' again<br>6. Select the same Financial Activity from the dropdown<br>7. Select a different GL Account from the dropdown<br>8. Click Submit | Form submission is blocked; an error message indicates that the Financial Activity can only be mapped once | medium |
| TC-016 (input_edge) | WF-005 | Create Financial Activity Mapping with long GL Account name |  | 1. Click '+ Create Mapping'<br>2. Select a Financial Activity from the dropdown<br>3. Select a GL Account with a long name<br>4. Click Submit | Form submits successfully; mapping is created with the long GL Account name | low |

---

## Provisioning

Total: **14** (positive: 4, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the creation form for provisioning criteria | User logged in as <role> | 1. Click '+ Create' button | Creation form opened | high |
| TC-002 | WF-002 | Generate new provisioning entries based on current loan portfolio status | User logged in as <role> | 1. Click '+ Create Provisioning Entry' button | New provisioning entries generated based on current loan portfolio status | high |
| TC-003 | WF-003 | Review a provisioning entry | User logged in as <role>, At least one provisioning entry exists | 1. Click on the action button to review an entry | Detailed breakdown by loan product and category shown | medium |
| TC-004 | WF-004 | Recreate a provisioning entry | User logged in as <role>, At least one provisioning entry exists | 1. Click on the action button to recreate an entry | Provisioning entry recreated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave Criteria Name blank and submit the creation form |  | 1. Click on the '+ Create' button to open the creation form<br>2. Leave the Criteria Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-006 | WF-002 | Attempt to create provisioning entry without meeting preconditions | No existing provisioning criteria configured | 1. Click on the '+ Create Provisioning Entry' button | Form does not submit; no provisioning entries are generated; error shown indicating that provisioning criteria must be configured | high |
| TC-007 | WF-003 | Attempt to review a provisioning entry without any existing entries | No existing provisioning entries | 1. Click on the 'Review' button for a provisioning entry | No entries are displayed; error shown indicating that there are no provisioning entries to review | medium |
| TC-008 | WF-004 | Attempt to recreate a provisioning entry that does not exist | No existing provisioning entries to recreate | 1. Click on the 'Recreate' button for a provisioning entry | No entry is recreated; error shown indicating that the provisioning entry does not exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Add maximum allowed rows to Definitions table | User is on the Create Criteria form | 1. Add maximum allowed rows to the Definitions table<br>2. Fill in all required fields<br>3. Click Save | Form submits successfully; all rows are saved in the Definitions table | medium |
| TC-010 (boundary) | WF-001 | Attempt to add one more row to Definitions table beyond maximum | User is on the Create Criteria form with maximum rows added | 1. Attempt to add one more row to the Definitions table | Addition is blocked; visible error message indicates maximum row limit reached | medium |
| TC-011 (state_edge) | WF-002 | Generate provisioning entries with edge case criteria | User has created criteria with edge values in Minimum Age and Maximum Age | 1. Click + Create Provisioning Entry<br>2. Confirm generation of entries | New provisioning entries are generated based on criteria; entries reflect edge case values correctly | medium |
| TC-012 (state_edge) | WF-002 | Rapidly generate provisioning entries after previous generation | User has just generated provisioning entries | 1. Immediately click + Create Provisioning Entry again | System handles the request without errors; new entries are generated based on current criteria | medium |
| TC-013 (input_edge) |  | Enter long text in Criteria Name field | User is on the Create Criteria form | 1. Enter a very long string (200+ characters) in the Criteria Name field | Form submission is blocked; visible error message indicates the name exceeds the maximum allowed length | low |
| TC-014 (input_edge) |  | Enter special characters in Criteria Name field | User is on the Create Criteria form | 1. Enter special characters in the Criteria Name field | Form submission is blocked; visible error message indicates invalid characters in the Criteria Name | low |

---

## Offices

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new office successfully | User logged in as <role> | 1. Click '+ Create Office' button<br>2. Enter <Office Name> in the Office Name field<br>3. Select <Parent Office> from the Parent Office dropdown<br>4. Enter <Opened On Date> in the Opened On Date field<br>5. Enter <External ID> in the External ID field<br>6. Click Submit | Office created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the Office Name field blank |  | 1. Click on the '+ Create Office' button<br>2. Leave the Office Name field blank<br>3. Fill in the Parent Office, Opened On Date, and External ID fields<br>4. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-003 | WF-001 | Leave the Parent Office field blank |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name, Opened On Date, and External ID fields<br>3. Leave the Parent Office field blank<br>4. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-004 | WF-001 | Leave the Opened On Date field blank |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name, Parent Office, and External ID fields<br>3. Leave the Opened On Date field blank<br>4. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-005 | WF-001 | Submit with all required fields empty |  | 1. Click on the '+ Create Office' button<br>2. Leave the Office Name, Parent Office, Opened On Date, and External ID fields blank<br>3. Click Submit | Form does not submit; Office is not created; inline validation errors appear on the Office Name, Parent Office, and Opened On Date fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Create office with maximum length Office Name |  | 1. Click on '+ Create Office' button<br>2. Enter maximum allowed length string in the Office Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; entity is created with the maximum length Office Name | medium |
| TC-007 (boundary) | WF-001 | Create office with empty Office Name |  | 1. Click on '+ Create Office' button<br>2. Leave Office Name field empty<br>3. Fill all other required fields<br>4. Click Submit | Inline error shown indicating 'Office Name is required' | medium |
| TC-008 (input_edge) | WF-001 | Create office with special characters in Office Name |  | 1. Click on '+ Create Office' button<br>2. Enter special characters in the Office Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; entity is created with the Office Name containing special characters | low |
| TC-009 (input_edge) | WF-001 | Create office with leading/trailing whitespace in Office Name |  | 1. Click on '+ Create Office' button<br>2. Enter leading and trailing spaces in the Office Name field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Employees

Total: **10** (positive: 3, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form for a new employee | User logged in as <Role> | 1. Click '+ Create Employee' button | Creation form opened | high |
| TC-002 | WF-002 | View employee details | User logged in as <Role> | 1. Click on the Name link of an employee in the data table | Employee details displayed | high |
| TC-003 | WF-003 | Open edit form for an employee | User logged in as <Role>, Employee details are displayed | 1. Click 'Edit' option on the employee detail page | Employee edit form opened | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to create an employee with required fields empty |  | 1. Click on '+ Create Employee'<br>2. Leave the Office field blank<br>3. Leave the First Name field blank<br>4. Leave the Last Name field blank<br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required'; First Name field displays an error: 'This field is required'; Last Name field displays an error: 'This field is required' | high |
| TC-005 | WF-001 | Attempt to create an employee with only required fields empty |  | 1. Click on '+ Create Employee'<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; Office field displays an error: 'This field is required'; First Name field displays an error: 'This field is required'; Last Name field displays an error: 'This field is required' | high |
| TC-006 |  | Attempt to access employee details without authentication |  | 1. Attempt to click on a Name link for an employee | User is redirected to the login page | high |
| TC-007 | WF-003 | Attempt to edit an employee without authentication |  | 1. Attempt to click on Edit for an employee | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) | WF-001 | Enter long text in First Name field | User is on the Create Employee form | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates the input exceeds the maximum allowed length for the First Name field. | low |
| TC-009 (input_edge) | WF-001 | Enter special characters in Last Name field | User is on the Create Employee form | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates that special characters are not allowed in the Last Name field. | low |
| TC-010 (input_edge) | WF-001 | Enter leading/trailing whitespace in Mobile Number field | User is on the Create Employee form | 1. Enter leading and trailing whitespace in the Mobile Number field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; the saved value shown in the detail page has no extra spaces. | low |

---

## Teller & Cashier Management

Total: **13** (positive: 5, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new teller successfully | User logged in as <role> | 1. Click '+ Create Teller'<br>2. Enter <Office> in the Office field<br>3. Enter <Teller Name> in the Teller Name field<br>4. Enter <Description> in the Description field<br>5. Enter <Start Date> in the Start Date field<br>6. Click Submit | Teller created; success message shown | high |
| TC-002 | WF-002 | Edit an existing teller successfully | User logged in as <role>, Teller exists | 1. Click on the Teller Name link<br>2. Click Edit<br>3. Update <Teller Name> in the Teller Name field<br>4. Click Save | Teller details updated; success message shown | high |
| TC-003 | WF-003 | Allocate a cashier successfully | User logged in as <role>, Teller exists | 1. Click on the Teller Name link<br>2. Click '+ Allocate Cashier'<br>3. Enter <Staff> in the Staff field<br>4. Enter <Start Date> in the Start Date field<br>5. Enter <End Date> in the End Date field<br>6. Check the Is Full Day checkbox<br>7. Enter <Description> in the Description field<br>8. Click Submit | Cashier allocated; success message shown | high |
| TC-004 | WF-004 | Allocate cash successfully | User logged in as <role>, Cashier exists | 1. Click on the Cashier Name link<br>2. Click Allocate Cash<br>3. Enter <Amount> in the Amount field<br>4. Select <Currency> from the Currency dropdown<br>5. Enter <Transaction Date> in the Transaction Date field<br>6. Click Submit | Cash allocated; success message shown | high |
| TC-005 | WF-005 | Settle cash successfully | User logged in as <role>, Cashier exists | 1. Click on the Cashier Name link<br>2. Click Settle Cash<br>3. Enter <Amount> in the Amount field<br>4. Select <Currency> from the Currency dropdown<br>5. Enter <Transaction Date> in the Transaction Date field<br>6. Click Submit | Cash settled; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave required fields blank when creating a Teller |  | 1. Click on '+ Create Teller'<br>2. Leave the Office field blank<br>3. Leave the Teller Name field blank<br>4. Leave the Start Date field blank<br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required'; Teller Name field displays an error: 'This field is required'; Start Date field displays an error: 'This field is required' | high |
| TC-007 | WF-003 | Leave required fields blank when allocating a Cashier |  | 1. Click on '+ Allocate Cashier'<br>2. Leave the Staff field blank<br>3. Leave the Start Date field blank<br>4. Click Submit | Form does not submit; Staff field displays an error: 'This field is required'; Start Date field displays an error: 'This field is required' | high |
| TC-008 | WF-005 | Attempt to settle cash without required fields |  | 1. Click on 'Settle Cash'<br>2. Leave the Amount field blank<br>3. Leave the Currency field blank<br>4. Leave the Transaction Date field blank<br>5. Click Submit | Form does not submit; Amount field displays an error: 'This field is required'; Currency field displays an error: 'This field is required'; Transaction Date field displays an error: 'This field is required' | high |
| TC-009 |  | Unauthenticated user attempts to access the Tellers page |  | 1. Navigate to the Tellers page without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) | WF-001 | Enter a very long Teller Name | User is on the Create Teller form | 1. Enter a string of 200+ characters in the Teller Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Teller created with the long name displayed on the detail page | low |
| TC-011 (input_edge) | WF-001 | Enter special characters in the Description field | User is on the Create Teller form | 1. Enter special characters in the Description field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Teller created with special characters displayed in the Description | low |
| TC-012 (input_edge) | WF-003 | Enter a very long Description for Cashier allocation | User is on the Allocate Cashier form | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Cashier allocated with the long description displayed on the detail page | low |
| TC-013 (input_edge) | WF-005 | Enter leading/trailing whitespace in the Amount field | User is on the Settle Cash form | 1. Enter ' 100 ' in the Amount field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Users & Roles

Total: **18** (positive: 2, negative: 9, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new user successfully | User logged in as <Admin>, No existing user with the same Username | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Select <office> from the Office dropdown<br>7. Enter <valid password> in the Password field<br>8. Enter <same valid password> in the Repeat Password field<br>9. Select <role> from the Roles checkboxes<br>10. Check the Override Password Expiry Policy checkbox<br>11. Check the Send Password to Email checkbox<br>12. Click 'Submit' button | User created successfully | high |
| TC-002 | WF-002 | Create a new role successfully | User logged in as <Admin> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Enter <role description> in the Description field<br>4. Click 'Submit' button | Role created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to create user with blank Username field |  | 1. Click on '+ Create User'<br>2. Leave the Username field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-004 | WF-001 | Attempt to create user with blank First Name field |  | 1. Click on '+ Create User'<br>2. Leave the First Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-005 | WF-001 | Attempt to create user with blank Last Name field |  | 1. Click on '+ Create User'<br>2. Leave the Last Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-006 | WF-001 | Attempt to create user with blank Email field |  | 1. Click on '+ Create User'<br>2. Leave the Email field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 | WF-001 | Attempt to create user with invalid Email format |  | 1. Click on '+ Create User'<br>2. Enter <invalid email format> in the Email field<br>3. Fill all other required fields<br>4. Click Submit | Email field displays an error: 'Must be a valid email address' | medium |
| TC-008 | WF-001 | Attempt to create user with blank Password field |  | 1. Click on '+ Create User'<br>2. Leave the Password field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-009 | WF-001 | Attempt to create user with mismatched Password and Repeat Password fields |  | 1. Click on '+ Create User'<br>2. Fill in the Password field<br>3. Fill in a different value in the Repeat Password field<br>4. Fill all other required fields<br>5. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match | medium |
| TC-010 | WF-002 | Attempt to create role with blank Role Name field |  | 1. Click on '+ Create Role'<br>2. Leave the Role Name field blank<br>3. Fill in the Description field<br>4. Click Submit | Inline validation error appears on the Role Name field indicating it is required | high |
| TC-011 | WF-002 | Attempt to create role with blank Description field |  | 1. Click on '+ Create Role'<br>2. Fill in the Role Name field<br>3. Leave the Description field blank<br>4. Click Submit | Inline validation error appears on the Description field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Enter a unique Username that meets the minimum character requirement |  | 1. Click '+ Create User'<br>2. Enter a unique Username that meets the minimum character requirement in the Username field<br>3. Fill in all other required fields<br>4. Click Submit | Form submits successfully; user is created with the specified Username | medium |
| TC-013 (boundary) | WF-001 | Enter a Username that is not unique |  | 1. Click '+ Create User'<br>2. Enter a Username that already exists in the system<br>3. Fill in all other required fields<br>4. Click Submit | Inline error displayed indicating 'Username must be unique' | medium |
| TC-014 (boundary) | WF-001 | Enter an invalid email format |  | 1. Click '+ Create User'<br>2. Enter a valid Username<br>3. Enter an invalid email format in the Email field<br>4. Fill in all other required fields<br>5. Click Submit | Inline error displayed indicating 'Email format is invalid' | medium |
| TC-015 (boundary) | WF-001 | Enter a password that does not meet the password policy |  | 1. Click '+ Create User'<br>2. Enter a valid Username<br>3. Enter a valid email<br>4. Enter a password that does not meet the password policy in the Password field<br>5. Fill in all other required fields<br>6. Click Submit | Inline error displayed indicating 'Password does not meet policy requirements' | medium |
| TC-016 (boundary) | WF-001 | Enter a password and repeat password that do not match |  | 1. Click '+ Create User'<br>2. Enter a valid Username<br>3. Enter a valid email<br>4. Enter a valid password in the Password field<br>5. Enter a different password in the Repeat Password field<br>6. Fill in all other required fields<br>7. Click Submit | Inline error displayed indicating 'Passwords do not match' | medium |
| TC-017 (boundary) | WF-002 | Enter a Role Name that meets the minimum character requirement |  | 1. Click '+ Create Role'<br>2. Enter a Role Name that meets the minimum character requirement<br>3. Fill in the Description field<br>4. Click Submit | Form submits successfully; role is created with the specified Role Name | medium |
| TC-018 (boundary) | WF-002 | Enter a Role Name that is not unique |  | 1. Click '+ Create Role'<br>2. Enter a Role Name that already exists in the system<br>3. Fill in the Description field<br>4. Click Submit | Inline error displayed indicating 'Role Name must be unique' | medium |

---

## Reports

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View report parameters form | User logged in as <role> | 1. Click on the report 'Loans Awaiting Disbursal'<br>2. Fill in the parameters form with valid selections for Office, Branch, Currency, Loan Product, Date Range, Loan Officer, and Fund<br>3. Click 'Run Report' | Report generated as a data table | high |
| TC-002 | WF-002 | Export report to Excel | User logged in as <role>, Report generated as a data table | 1. Click on the report 'Active Loans Summary'<br>2. Fill in the parameters form with valid selections<br>3. Click 'Run Report'<br>4. Click 'Export to Excel' | Report exported to Excel file | medium |
| TC-003 | WF-003 | Export report to CSV | User logged in as <role>, Report generated as a data table | 1. Click on the report 'Active Loans Details'<br>2. Fill in the parameters form with valid selections<br>3. Click 'Run Report'<br>4. Click 'Export to CSV' | Report exported to CSV file | medium |
| TC-004 | WF-004 | Export report to PDF | User logged in as <role>, Report generated as a data table | 1. Click on the report 'Portfolio at Risk'<br>2. Fill in the parameters form with valid selections<br>3. Click 'Run Report'<br>4. Click 'Export to PDF' | Report exported to PDF file | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to run report without filling required parameters |  | 1. Click on a report to open the parameters form<br>2. Leave all parameter fields blank<br>3. Click 'Run Report' | Form does not submit; error shown on all required fields |  |
| TC-006 | WF-002 | Attempt to export report to Excel without selecting parameters |  | 1. Click on a report to open the parameters form<br>2. Leave all parameter fields blank<br>3. Click 'Export to Excel' | Form does not submit; error shown on all required fields |  |
| TC-007 | WF-003 | Attempt to export report to CSV without selecting parameters |  | 1. Click on a report to open the parameters form<br>2. Leave all parameter fields blank<br>3. Click 'Export to CSV' | Form does not submit; error shown on all required fields |  |
| TC-008 | WF-004 | Attempt to export report to PDF without selecting parameters |  | 1. Click on a report to open the parameters form<br>2. Leave all parameter fields blank<br>3. Click 'Export to PDF' | Form does not submit; error shown on all required fields |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (interaction_edge) | WF-001 | Rapid submission of report parameters | User is on the Reports page | 1. Click on a report to open the parameters form<br>2. Fill in all required fields with valid data<br>3. Click 'Run Report'<br>4. Immediately click 'Run Report' again | Second submission attempt is blocked; the report is generated only once and displayed as a data table | medium |
| TC-010 (interaction_edge) | WF-002 | Export report to Excel after generating | User has generated a report | 1. Click 'Export to Excel' | Report is successfully exported to an Excel file with a visible success indicator | medium |
| TC-011 (interaction_edge) | WF-003 | Export report to CSV after generating | User has generated a report | 1. Click 'Export to CSV' | Report is successfully exported to a CSV file with a visible success indicator | medium |
| TC-012 (interaction_edge) | WF-004 | Export report to PDF after generating | User has generated a report | 1. Click 'Export to PDF' | Report is successfully exported to a PDF file with a visible success indicator | medium |

---

## Account Transfers & Standing Instructions

Total: **12** (positive: 5, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient | 1. Enter <From Office> in the From Office field<br>2. Enter <From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Select <From Account> from the From Account dropdown<br>5. Enter <To Office> in the To Office field<br>6. Enter <To Client> in the To Client field<br>7. Select 'Loan Account' from the To Account Type dropdown<br>8. Select <To Account> from the To Account dropdown<br>9. Enter <valid transfer amount> in the Transfer Amount field<br>10. Select <valid transfer date> in the Transfer Date field<br>11. Enter <description> in the Description field<br>12. Click Submit | Transfer processed, debiting source and crediting destination | high |
| TC-002 | WF-002 | Create a standing instruction | User logged in as <Role> | 1. Click + Create Standing Instruction<br>2. Enter <Name> in the Name field<br>3. Select <From Account> in the From Account field<br>4. Select <To Account> in the To Account field<br>5. Select <Transfer Type> from the Transfer Type dropdown<br>6. Enter <priority> in the Priority field<br>7. Select <Instruction Type> from the Instruction Type dropdown<br>8. Enter <valid amount> in the Amount field<br>9. Select <valid from date> in the Validity From field<br>10. Select <valid till date> in the Validity Till field<br>11. Select <Recurrence Type> from the Recurrence Type dropdown<br>12. Enter <recurrence frequency> in the Recurrence Frequency field<br>13. Enter <recurrence interval> in the Recurrence Interval field<br>14. Click Submit | Standing instruction created | high |
| TC-003 | WF-003 | Enable a standing instruction | User logged in as <Role>, Standing instruction is in Disabled status | 1. Locate the standing instruction in the data table<br>2. Click Enable | Standing instruction enabled | medium |
| TC-004 | WF-004 | Disable a standing instruction | User logged in as <Role>, Standing instruction is in Active status | 1. Locate the standing instruction in the data table<br>2. Click Disable | Standing instruction disabled | medium |
| TC-005 | WF-005 | Delete a standing instruction | User logged in as <Role>, Standing instruction exists | 1. Locate the standing instruction in the data table<br>2. Click Delete | Standing instruction deleted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave Transfer Amount blank and submit |  | 1. Leave the Transfer Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-007 | WF-001 | Enter amount exceeding available balance and submit |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; error shown indicating transfer amount exceeds available balance | high |
| TC-008 | WF-002 | Leave Name blank and submit Standing Instruction |  | 1. Leave the Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Transfer amount exactly equal to available balance | User has an account with a known balance | 1. Enter the From Office and From Client fields<br>2. Select the From Account Type as Savings Account<br>3. Choose the From Account with the exact available balance<br>4. Enter the To Office and To Client fields<br>5. Select the To Account Type as Savings Account<br>6. Choose the To Account<br>7. Enter the Transfer Amount equal to the available balance<br>8. Select the Transfer Date<br>9. Fill in the Description<br>10. Click Submit | Transfer processed, debiting source and crediting destination | medium |
| TC-010 (boundary) | WF-001 | Transfer amount exceeds available balance | User has an account with a known balance | 1. Enter the From Office and From Client fields<br>2. Select the From Account Type as Savings Account<br>3. Choose the From Account with the known balance<br>4. Enter the Transfer Amount greater than the available balance<br>5. Select the Transfer Date<br>6. Fill in the Description<br>7. Click Submit | Error shown indicating transfer amount exceeds available balance | medium |
| TC-011 (input_edge) | WF-002 | Create standing instruction with very long name |  | 1. Click + Create Standing Instruction<br>2. Enter a Name with 200+ characters<br>3. Fill in the From and To account fields<br>4. Select Transfer Type and Priority<br>5. Select Instruction Type and enter Amount<br>6. Fill Validity From and Till dates<br>7. Select Recurrence Type, Frequency, and Interval<br>8. Click Submit | Form submits successfully; standing instruction created with the long name | low |
| TC-012 (input_edge) | WF-002 | Create standing instruction with special characters in name |  | 1. Click + Create Standing Instruction<br>2. Enter a Name with special characters (e.g., @#$%^&*)<br>3. Fill in the From and To account fields<br>4. Select Transfer Type and Priority<br>5. Select Instruction Type and enter Amount<br>6. Fill Validity From and Till dates<br>7. Select Recurrence Type, Frequency, and Interval<br>8. Click Submit | Form submits successfully; standing instruction created with the name containing special characters | low |

---

## Tax Management

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create a new Tax Component successfully | User logged in as <Role> | 1. Click '+ Create Tax Component' button<br>2. Enter <valid name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select <valid Debit Account Type> from the Debit Account Type dropdown<br>5. Select <valid Debit Account> from the Debit Account dropdown<br>6. Select <valid Credit Account Type> from the Credit Account Type dropdown<br>7. Select <valid Credit Account> from the Credit Account dropdown<br>8. Enter <valid start date> in the Start Date field<br>9. Click Submit | A success notification is displayed; the new Tax Component appears in the data table with the entered Name and Percentage | high |
| TC-002 |  | Create a new Tax Group successfully | User logged in as <Role> | 1. Click '+ Create Tax Group' button<br>2. Enter <valid name> in the Name field<br>3. Click 'Add Component' button<br>4. Enter <valid component name> in the Name field<br>5. Enter <valid start date> in the Start Date field<br>6. Enter <valid end date> in the End Date field<br>7. Click Submit | A success notification is displayed; the new Tax Group appears in the data table with the entered Name and associated components | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to create a Tax Component with required fields blank |  | 1. Click on '+ Create Tax Component'<br>2. Leave the Name field blank<br>3. Leave the Percentage field blank<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required; Inline validation error appears on the Percentage field indicating it is required | high |
| TC-004 |  | Attempt to create a Tax Group with required fields blank |  | 1. Click on '+ Create Tax Group'<br>2. Leave the Name field blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long name in the Name field |  | 1. Click on '+ Create Tax Component' button<br>2. Enter a string of 200+ characters in the Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; entity is created with the long name | low |
| TC-006 (input_edge) |  | Enter special characters in the Name field |  | 1. Click on '+ Create Tax Component' button<br>2. Enter special characters in the Name field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; entity is created with the special characters in the name | low |
| TC-007 (input_edge) |  | Enter leading and trailing whitespace in the Name field |  | 1. Click on '+ Create Tax Component' button<br>2. Enter '   Tax Component Name   ' in the Name field<br>3. Fill all other required fields<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Organization Settings

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new holiday successfully | User logged in as <Admin>, User is on the Holidays page | 1. Click '+ Create Holiday' button<br>2. Enter <valid holiday name> in the Name field<br>3. Select <valid start date> in the From Date field<br>4. Select <valid end date> in the To Date field<br>5. Select <valid rescheduling type> from the Rescheduling Type dropdown<br>6. Enter <optional description> in the Description field<br>7. Select applicable offices from the Offices multi-select<br>8. Click Submit | Holiday created; success message shown | high |
| TC-002 | WF-002 | Create a new fund successfully | User logged in as <Admin>, User is on the Funds page | 1. Click 'Create Fund' button<br>2. Enter <valid fund name> in the Fund Name field<br>3. Enter <valid external ID> in the External ID field<br>4. Click Submit | Fund created; success message shown | high |
| TC-003 | WF-003 | Create a new payment type successfully | User logged in as <Admin>, User is on the Payment Types page | 1. Click '+ Create' button<br>2. Enter <valid payment type name> in the Name field<br>3. Enter <valid description> in the Description field<br>4. Select <is cash payment> in the Is Cash Payment checkbox<br>5. Enter <valid position> in the Position field<br>6. Click Submit | Payment type created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave all required fields blank when creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Leave the From Date field blank<br>4. Leave the To Date field blank<br>5. Click Submit | Form does not submit; Name, From Date, and To Date fields are highlighted with inline validation errors indicating they are required | high |
| TC-005 | WF-002 | Leave all required fields blank when creating a fund |  | 1. Click on 'Create Fund'<br>2. Leave the Fund Name field blank<br>3. Leave the External ID field blank<br>4. Click Submit | Form does not submit; Fund Name and External ID fields are highlighted with inline validation errors indicating they are required | high |
| TC-006 | WF-003 | Leave all required fields blank when creating a payment type |  | 1. Click on '+ Create'<br>2. Leave the Name field blank<br>3. Click Submit | Form does not submit; Name field is highlighted with inline validation error indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Enter the same date for From Date and To Date | User is on the Create Holiday form | 1. Enter a valid holiday name in the Name field<br>2. Enter today's date in the From Date field<br>3. Enter today's date in the To Date field<br>4. Fill other required fields<br>5. Click Submit | Holiday is created successfully; success message shown. | medium |
| TC-008 (boundary) | WF-001 | Enter a past date for From Date | User is on the Create Holiday form | 1. Enter a valid holiday name in the Name field<br>2. Enter a date from yesterday in the From Date field<br>3. Enter a future date in the To Date field<br>4. Fill other required fields<br>5. Click Submit | Form submission is blocked; error message displayed indicating From Date cannot be in the past. | medium |
| TC-009 (boundary) | WF-002 | Enter maximum length for Fund Name | User is on the Create Fund form | 1. Enter a fund name with maximum allowed characters in the Fund Name field<br>2. Enter a valid External ID<br>3. Click Create | Fund is created successfully; success message shown. | medium |
| TC-010 (boundary) | WF-002 | Enter an empty External ID | User is on the Create Fund form | 1. Enter a valid fund name in the Fund Name field<br>2. Leave the External ID field empty<br>3. Click Create | Form submission is blocked; error message displayed indicating External ID is required. | medium |

---

## System Administration

Total: **27** (positive: 14, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Toggle job active status | User logged in as <Role>, Job 'Apply Annual Fee' is currently active | 1. Navigate to the Manage Scheduler Jobs page<br>2. Toggle the Is Active switch for 'Apply Annual Fee' job | Job status updated | high |
| TC-002 | WF-002 | Edit CRON expression for a job | User logged in as <Role>, Job 'Add Accrual Transactions' is displayed | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click on the Edit button for 'Add Accrual Transactions'<br>3. Enter '<valid CRON expression>' in the CRON Expression field<br>4. Click Save | CRON expression updated | high |
| TC-003 | WF-003 | Start all scheduled jobs | User logged in as <Role>, Global Start/Stop toggle is in the Stop position | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click the Start button for the global scheduler toggle | All jobs started | high |
| TC-004 | WF-004 | Stop all scheduled jobs | User logged in as <Role>, Global Start/Stop toggle is in the Start position | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click the Stop button for the global scheduler toggle | All jobs stopped | high |
| TC-005 | WF-005 | Toggle feature flag enabled status | User logged in as <Role>, Feature flag 'maker-checker' is currently enabled | 1. Navigate to the Global Configuration page<br>2. Toggle the Enabled switch for 'maker-checker' | Feature flag status updated | high |
| TC-006 | WF-006 | Add new code entry | User logged in as <Role>, Manage Codes page is displayed | 1. Click the Add button on the Manage Codes page<br>2. Enter '<valid code name>' in the Name field<br>3. Toggle Is System Defined checkbox<br>4. Click Add | Code entry added | high |
| TC-007 | WF-007 | Edit existing code entry | User logged in as <Role>, Code entry 'Gender' is displayed | 1. Navigate to the Manage Codes page<br>2. Click on the Edit button for 'Gender'<br>3. Change the Value field to '<new value>'<br>4. Click Save | Code entry updated | high |
| TC-008 | WF-008 | Deactivate code entry | User logged in as <Role>, Code entry 'Client Type' is displayed | 1. Navigate to the Manage Codes page<br>2. Click on the Deactivate button for 'Client Type' | Code entry deactivated | high |
| TC-009 | WF-009 | Create custom data table | User logged in as <Role>, Manage Data Tables page is displayed | 1. Click the Create button on the Manage Data Tables page<br>2. Enter '<Data Table Name>' in the Data Table Name field<br>3. Select '<Application Table Name>' from the dropdown<br>4. Check Multi Row checkbox<br>5. Click Create | Custom data table created | high |
| TC-010 | WF-010 | Add column to custom data table | User logged in as <Role>, Custom data table 'm_client' is displayed | 1. Navigate to the Manage Data Tables page<br>2. Click on 'm_client'<br>3. Click the Add Column button<br>4. Enter '<Column Name>' in the Name field<br>5. Select '<Type>' from the Type dropdown<br>6. Click Add Column | Column added to data table | high |
| TC-011 | WF-011 | Edit column in custom data table | User logged in as <Role>, Column 'Name' in custom data table 'm_client' is displayed | 1. Navigate to the Manage Data Tables page<br>2. Click on 'm_client'<br>3. Click on the Edit button for 'Name' column<br>4. Change the Length field to '<new length>'<br>5. Click Save Column | Column updated in data table | high |
| TC-012 | WF-012 | Deactivate column in custom data table | User logged in as <Role>, Column 'Is Active' in custom data table 'm_client' is displayed | 1. Navigate to the Manage Data Tables page<br>2. Click on 'm_client'<br>3. Click on the Deactivate Column button for 'Is Active' | Column deactivated in data table | high |
| TC-013 | WF-013 | Approve pending action | User logged in as <Role>, Maker-checker is enabled, Pending action is displayed | 1. Navigate to the Audit Trails page<br>2. Click on the Approve button for the pending action | Action approved | high |
| TC-014 | WF-014 | Reject pending action | User logged in as <Role>, Maker-checker is enabled, Pending action is displayed | 1. Navigate to the Audit Trails page<br>2. Click on the Reject button for the pending action | Action rejected | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Leave the Data Table Name blank when creating a custom data table |  | 1. Navigate to Create custom data table<br>2. Leave the Data Table Name blank<br>3. Fill all other required fields<br>4. Click Create | Form does not submit; Data Table Name is not provided; error shown on Data Table Name field indicating it is required | high |
| TC-016 |  | Leave the Application Table Name dropdown unselected when creating a custom data table |  | 1. Navigate to Create custom data table<br>2. Select Data Table Name<br>3. Leave the Application Table Name dropdown unselected<br>4. Click Create | Form does not submit; Application Table Name is not selected; error shown on Application Table Name field indicating it is required | high |
| TC-017 |  | Attempt to toggle job active/inactive without required permissions |  | 1. Attempt to toggle the active status of a job without proper role permissions | Action is blocked; user is not allowed to toggle job status | high |
| TC-018 |  | Attempt to start all scheduled jobs without required permissions |  | 1. Attempt to start all scheduled jobs without proper role permissions | Action is blocked; user is not allowed to start jobs | high |
| TC-019 |  | Attempt to edit CRON expression for a job without required permissions |  | 1. Attempt to edit the CRON expression for a job without proper role permissions | Action is blocked; user is not allowed to edit CRON expression | high |
| TC-020 |  | Attempt to approve a pending action when maker-checker is not enabled |  | 1. Attempt to approve a pending action when maker-checker is disabled | Action is blocked; user cannot approve without maker-checker enabled | high |
| TC-021 |  | Attempt to reject a pending action when maker-checker is not enabled |  | 1. Attempt to reject a pending action when maker-checker is disabled | Action is blocked; user cannot reject without maker-checker enabled | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (interaction_edge) | WF-001 | Rapid toggle of job active/inactive | User is on the Manage Scheduler Jobs page | 1. Toggle a job's active status to inactive<br>2. Immediately toggle the same job's active status back to active | Job status updated successfully; the job remains active | medium |
| TC-023 (boundary | interaction_edge) | WF-002 | Edit CRON expression with boundary values | User is on the Manage Scheduler Jobs page, A job is selected | 1. Click to edit the CRON expression<br>2. Enter a valid CRON expression that is at the maximum length allowed<br>3. Click Save | CRON expression updated successfully; the new expression is displayed | medium |
| TC-024 (boundary | interaction_edge) | WF-002 | Edit CRON expression with invalid format | User is on the Manage Scheduler Jobs page, A job is selected | 1. Click to edit the CRON expression<br>2. Enter an invalid CRON expression<br>3. Click Save | Error message displayed indicating invalid CRON expression format | medium |
| TC-025 (interaction_edge) | WF-003 | Start all scheduled jobs rapidly | User is on the Manage Scheduler Jobs page | 1. Click Start to begin all scheduled jobs<br>2. Immediately click Start again | All jobs started successfully; no duplicate start action is performed | medium |
| TC-026 (interaction_edge) | WF-004 | Stop all scheduled jobs rapidly | User is on the Manage Scheduler Jobs page | 1. Click Stop to halt all scheduled jobs<br>2. Immediately click Stop again | All jobs stopped successfully; no duplicate stop action is performed | medium |
| TC-027 (interaction_edge) | WF-013 | Rapid approval of pending action | User is on the Audit Trails page, maker-checker is enabled | 1. Click Approve on a pending action<br>2. Immediately click Approve again on the same action | Action approved successfully; no duplicate approval is processed | medium |

---

## Logout

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User logs out successfully | User logged in as <Authenticated User> | 1. Click the user profile icon in the top-right corner<br>2. Click 'Log Out' from the dropdown | User is redirected to the login page | high |
| TC-002 |  | Attempt to access authenticated page after logout | User logged in as <Authenticated User>, User has logged out | 1. Attempt to navigate to an authenticated page | User is redirected to the login page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to access an authenticated page after logout | User is logged in | 1. Click on the user profile icon<br>2. Select 'Log Out'<br>3. Attempt to navigate to an authenticated page | User is redirected to the login page | high |
| TC-004 |  | Attempt to access the logout function without being authenticated | User is not logged in | 1. Attempt to click on the user profile icon | Logout option is not visible or accessible | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Attempt to log out while rapidly clicking the logout button multiple times | User is logged in and on a page with the user profile icon visible | 1. Click the user profile icon in the top-right corner<br>2. Click 'Log Out' rapidly multiple times | Only one logout action is processed; user is redirected to the login page without multiple sessions being created. | low |
| TC-006 (input_edge) |  | Attempt to navigate to an authenticated page after logging out | User is logged in, User has logged out | 1. Click the user profile icon in the top-right corner<br>2. Click 'Log Out'<br>3. Attempt to navigate to an authenticated page | User is redirected to the login page upon attempting to access the authenticated page. | low |

---
