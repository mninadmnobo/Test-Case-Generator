# Test Cases — Mifos

Generated: 2026-06-09T09:30:17.303693Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 525 | 156 | 204 | 165 | 248 | 225 | 52 |

## Login

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User>, Required fields must be filled | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | redirects to Dashboard | high |
| TC-002 | WF-002 | Login with empty required fields | User logged in as <User> | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | shows inline validation messages | high |
| TC-003 | WF-003 | Login with invalid credentials | User logged in as <User>, Required fields must be filled | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | shows error message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to login with empty Username field |  | 1. Leave the Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Username field indicating it cannot be empty | high |
| TC-005 |  | Attempt to login with empty Password field |  | 1. Fill the Username field with a valid username<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it cannot be empty | high |
| TC-006 | WF-002 | Attempt to login with all required fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Form does not submit; inline validation messages show for both Username and Password fields | high |
| TC-007 | WF-003 | Attempt to login with invalid credentials |  | 1. Fill the Username field with an invalid username<br>2. Fill the Password field with an invalid password<br>3. Click Login | Page displays 'shows error message' and the form does not submit | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Attempt to submit the form with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | Inline validation messages show for empty required fields | medium |
| TC-009 (boundary) | WF-003 | Attempt to login with a valid Username but invalid Password | Username field is filled with a valid username | 1. Enter a valid Username in the Username field<br>2. Enter an invalid Password in the Password field<br>3. Click the Login button | Error message shows indicating invalid credentials | medium |
| TC-010 (input_edge) |  | Enter a very long string in the Username field |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | Form submission is blocked; inline validation message shows | low |
| TC-011 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter special characters (e.g., @#$%^&) in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | Form submission is blocked; inline validation message shows | low |

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
| TC-002 | WF-001 | Attempt to access dashboard without being logged in | User is not authenticated | 1. Navigate to the Home Page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully logged in | 1. Click the Dashboard button<br>2. Immediately press the browser back button | User is redirected to the dashboard without a second entity being created; the dashboard is displayed blank. | medium |
| TC-004 (input_edge) |  | Long text in Search Activity input | Home page is displayed | 1. Enter a string of 200+ characters in the Search Activity input field | Search Activity input field accepts the input without error, or truncates the input with a visible indicator. | low |
| TC-005 (input_edge) |  | Special characters in Search Activity input | Home page is displayed | 1. Enter a string containing special characters (e.g., !@#$%^&*) in the Search Activity input field | Search Activity input field accepts the input without error, or displays a specific error message. | low |

---

## Dashboard

Total: **6** (positive: 1, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access the Dashboard from the Home page | User logged in as <Role> | 1. Click on the 'Dashboard' button on the Home page | Navigates to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access the Dashboard |  | 1. Navigate to the Dashboard link | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Access Dashboard from Home page | User is on the Home page | 1. Click on the 'Dashboard' button | Navigates to the Dashboard page successfully | medium |
| TC-004 (input_edge) |  | Enter long text in Search Activity field | User is on the Dashboard page | 1. Enter a string of 200+ characters in the 'Search Activity' field | The input is accepted or truncated with a visible indicator | low |
| TC-005 (input_edge) |  | Enter special characters in Search Activity field | User is on the Dashboard page | 1. Enter special characters (e.g., !@#$%^&*) in the 'Search Activity' field | The input is accepted or a specific error is shown | low |
| TC-006 (input_edge) |  | Enter value with leading/trailing whitespace in Search Activity field | User is on the Dashboard page | 1. Enter '   test input   ' in the 'Search Activity' field | Leading/trailing whitespace is trimmed; saved value shown has no extra spaces | low |

---

## Global Search

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field | User logged in as <Role> | 1. Click the Search Icon in the top toolbar | opens search input field | high |
| TC-002 | WF-002 | Search with results found | User logged in as <Role>, Search input field is open | 1. Enter <valid search term> in the Search Input field | searches across Clients, Groups, Loans, and Savings accounts | high |
| TC-003 | WF-003 | Display no results message | User logged in as <Role>, Search input field is open | 1. Enter <non-matching search term> in the Search Input field | No results found | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Unauthenticated user attempts to open search input field |  | 1. Attempt to click on the Search Icon | User is redirected to the login page; search input field does not open | high |
| TC-005 |  | Search input field submitted with empty input | user is logged in | 1. Click on the Search Icon<br>2. Leave the Search_Input field blank<br>3. Click Submit | No results found message is displayed; search results dropdown does not appear | high |
| TC-006 |  | Search input field submitted with invalid input format | user is logged in | 1. Click on the Search Icon<br>2. Enter <invalid search term> in the Search_Input field<br>3. Click Submit | No results found message is displayed; search results dropdown does not appear | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Search with partial match at the boundary of entity name | User is logged in | 1. Click on the Search Icon<br>2. Enter a partial entity name that is exactly at the boundary of matching<br>3. Observe the Search Results dropdown | Search results display entities that match the partial input; dropdown shows relevant results | medium |
| TC-008 (boundary) | WF-003 | Search with input that has no matches | User is logged in | 1. Click on the Search Icon<br>2. Enter a search term that does not match any entity<br>3. Observe the No Results Message | No results found message is displayed | medium |
| TC-009 (input_edge) |  | Search input with special characters | User is logged in | 1. Click on the Search Icon<br>2. Enter a search term with special characters (e.g., @, #, $)<br>3. Observe the Search Results dropdown | Search results display entities that match the input with special characters; dropdown shows relevant results | low |
| TC-010 (input_edge) |  | Search input with leading and trailing whitespace | User is logged in | 1. Click on the Search Icon<br>2. Enter a search term with leading and trailing spaces<br>3. Observe the Search Results dropdown | Leading and trailing whitespace is trimmed; search results display correctly based on the trimmed input | low |

---

## Client Management

Total: **27** (positive: 10, negative: 10, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Import Client opens Bulk Import page | User logged in as <Role> | 1. Click Import Client button | opens Bulk Import page | high |
| TC-002 | WF-002 | Create Client submits the wizard and creates client in Pending status | User logged in as <Role> | 1. Click Create Client button<br>2. Enter <Office> in the Office field<br>3. Enter <First Name> in the First Name field<br>4. Enter <Last Name> in the Last Name field<br>5. Enter <Submitted On> in the Submitted On field<br>6. Click Submit | creates client in Pending status | high |
| TC-003 | WF-003 | View Client Details displays client details | User logged in as <Role>, Client exists in the Clients Table | 1. Click on the Name link of the client in the Clients Table | displays client details | medium |
| TC-004 | WF-004 | Activate Client activates the client | User logged in as <Role>, Client is in Pending status | 1. Click Activate button<br>2. Enter <Activation Date> in the Activation Date field<br>3. Click Confirm on the Activation dialog | activates client | medium |
| TC-005 | WF-005 | Edit Client opens client edit form | User logged in as <Role>, Client exists in the Clients Table | 1. Click Edit button on the Client Detail page | opens client edit form | medium |
| TC-006 | WF-006 | Reject Client rejects the client | User logged in as <Role>, Client is in Pending status | 1. Click Reject button<br>2. Enter <Reason> in the Reason field<br>3. Click Confirm on the Reject dialog | rejects client | medium |
| TC-007 | WF-007 | Withdraw Client withdraws the client | User logged in as <Role>, Client is in Pending status | 1. Click Withdraw button<br>2. Enter <Reason> in the Reason field<br>3. Click Confirm on the Withdraw dialog | withdraws client | medium |
| TC-008 | WF-008 | Transfer Client transfers the client | User logged in as <Role>, Client is in Active status | 1. Click Transfer Client button<br>2. Enter <Destination Office> in the Destination Office field<br>3. Click Confirm on the Transfer dialog | transfers client | medium |
| TC-009 | WF-009 | Close Client closes the client | User logged in as <Role>, Client is in Active status | 1. Click Close button<br>2. Enter <Closure Reason> in the Closure Reason field<br>3. Click Confirm on the Close dialog | closes client | medium |
| TC-010 | WF-010 | Reactivate Client reactivates the client | User logged in as <Role>, Client is in Closed status | 1. Click Reactivate button | reactivates client | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-002 | Leave the Office field blank and submit the Create Client form |  | 1. Leave the Office field blank<br>2. Fill in First Name, Last Name, and Submitted On fields with valid data<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-012 | WF-002 | Leave the First Name field blank and submit the Create Client form |  | 1. Leave the First Name field blank<br>2. Fill in Office, Last Name, and Submitted On fields with valid data<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-013 | WF-002 | Leave the Last Name field blank and submit the Create Client form |  | 1. Leave the Last Name field blank<br>2. Fill in Office, First Name, and Submitted On fields with valid data<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-014 | WF-002 | Leave the Submitted On field blank and submit the Create Client form |  | 1. Leave the Submitted On field blank<br>2. Fill in Office, First Name, and Last Name fields with valid data<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-015 | WF-002 | Submit the Create Client form with all required fields empty |  | 1. Leave the Office, First Name, Last Name, and Submitted On fields blank<br>2. Click Submit | Form does not submit; Client is not created; errors shown on Office, First Name, Last Name, and Submitted On fields | high |
| TC-016 | WF-006 | Submit the Reject action without filling the Reason field | Status == Pending | 1. Click Reject<br>2. Leave the Reason field blank<br>3. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-017 | WF-007 | Submit the Withdraw action without filling the Reason field | Status == Pending | 1. Click Withdraw<br>2. Leave the Reason field blank<br>3. Click Submit | Inline validation error appears on the Reason field indicating it is required | high |
| TC-018 | WF-004 | Attempt to activate a client without filling the Activation Date field | Status == Pending | 1. Click Activate<br>2. Leave the Activation Date field blank<br>3. Click Submit | Inline validation error appears on the Activation Date field indicating it is required | high |
| TC-019 | WF-008 | Attempt to transfer a client to the same office | Status == Active | 1. Click Transfer Client<br>2. Select the same office as current office<br>3. Click Submit | Inline validation error appears indicating 'same office is blocked' | medium |
| TC-020 | WF-009 | Attempt to close a client with active accounts | Status == Active | 1. Click Close<br>2. Fill in Closure Reason field with valid data<br>3. Click Submit | Inline validation error appears indicating 'cannot close with active accounts' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-002 | Submit with Submitted On date equal to today | User is on the Create Client Wizard Step 1 | 1. Enter valid values for all required fields<br>2. Set Submitted On to today's date<br>3. Click Submit | Client is created in Pending status | medium |
| TC-022 (boundary) | WF-004 | Activate client with Activation Date equal to Submitted On date | Client is in Pending status, User is on Client Detail Page | 1. Click Activate<br>2. Set Activation Date to the Submitted On date<br>3. Click Confirm | Client is activated successfully | medium |
| TC-023 (boundary) | WF-004 | Attempt to activate client with Activation Date before Submitted On date | Client is in Pending status, User is on Client Detail Page | 1. Click Activate<br>2. Set Activation Date to one day before Submitted On date<br>3. Click Confirm | Activation is blocked; error message displayed indicating 'Activation Date must not be before submission date' | medium |
| TC-024 (boundary) | WF-008 | Transfer client to same office | Client is in Active status, User is on Client Detail Page | 1. Click Transfer Client<br>2. Set Destination Office to the same office as current<br>3. Click Confirm | Transfer is blocked; error message displayed indicating 'same office is blocked' | medium |
| TC-025 (input_edge) |  | Enter a very long name in the Client Name field | User is on the Create Client Wizard Step 1 | 1. Enter a name longer than 200 characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; Client Name is truncated or an error message is shown | low |
| TC-026 (input_edge) |  | Enter special characters in the External ID field | User is on the Create Client Wizard Step 1 | 1. Enter special characters in the External ID field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully or an error message is shown indicating invalid characters | low |
| TC-027 (input_edge) |  | Enter a value with leading/trailing whitespace in the First Name field | User is on the Create Client Wizard Step 1 | 1. Enter '   John   ' in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Group Management

Total: **23** (positive: 9, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Group Details | User logged in as <Role>, At least one group exists in the Groups Table | 1. Click on the Group Name link in the Groups Table | Group details displayed | high |
| TC-002 | WF-003 | Create New Group | User logged in as <Role> | 1. Click on 'Create New Group' button<br>2. Enter <valid group name> in the Name field<br>3. Enter <valid office> in the Office field<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | creates the group | high |
| TC-003 | WF-004 | Upload Groups | User logged in as <Role>, Navigated to the Bulk Import Groups page | 1. Click on the File Picker to select a valid file<br>2. Click Upload | Groups uploaded successfully | high |
| TC-004 | WF-005 | Activate Group | User logged in as <Role>, Group is in 'Pending' status | 1. Click Activate on the Group Detail page | Group activated | medium |
| TC-005 | WF-006 | Edit Group | User logged in as <Role>, Group exists | 1. Click Edit on the Group Detail page<br>2. Modify <field> with <new value><br>3. Click Submit | Group edited | medium |
| TC-006 | WF-007 | Close Group | User logged in as <Role>, Group is active | 1. Click Close on the Group Detail page | Group closed | medium |
| TC-007 | WF-008 | Assign Staff to Group | User logged in as <Role>, Group exists | 1. Click Assign Staff on the Group Detail page<br>2. Select <staff member> from the dropdown<br>3. Click Submit | Staff assigned to group | medium |
| TC-008 | WF-009 | Transfer Clients | User logged in as <Role>, Group exists | 1. Click Transfer Clients on the Group Detail page<br>2. Select <clients> to transfer<br>3. Click Submit | Clients transferred | medium |
| TC-009 | WF-010 | Generate Collection Sheet | User logged in as <Role>, Group exists | 1. Click Generate Collection Sheet button | Collection sheet generated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-003 | Leave the Name field blank and submit the Create Group form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-011 | WF-003 | Leave the Office field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-012 | WF-003 | Leave the Submitted On field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-013 | WF-004 | Leave the File Picker blank and attempt to upload groups |  | 1. Leave the File Picker blank<br>2. Click Upload | Inline validation error appears on the File Picker field indicating it is required | high |
| TC-014 | WF-005 | Attempt to activate a group that is already active |  | 1. Navigate to the Group Detail page of an active group<br>2. Click Activate | Status remains Active; no transition occurs; error shown indicating the group is already active | medium |
| TC-015 | WF-007 | Attempt to close a group that is already closed |  | 1. Navigate to the Group Detail page of a closed group<br>2. Click Close | Status remains Closed; no transition occurs; error shown indicating the group is already closed | medium |
| TC-016 | WF-008 | Attempt to assign staff to a group that has no staff assigned |  | 1. Navigate to the Group Detail page of a group with no staff assigned<br>2. Click Assign Staff | No staff assigned; action is blocked; error shown indicating no staff can be assigned | medium |
| TC-017 | WF-009 | Attempt to transfer clients from a group with no clients |  | 1. Navigate to the Group Detail page of a group with no clients<br>2. Click Transfer Clients | No clients transferred; action is blocked; error shown indicating no clients to transfer | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-003 | Create group with minimum length name |  | 1. Enter the minimum allowed length in the Name field<br>2. Fill in the required Office field<br>3. Fill in the required Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum length name | medium |
| TC-019 (boundary) | WF-003 | Create group with one character less than minimum length name |  | 1. Enter one character less than the minimum allowed length in the Name field<br>2. Fill in the required Office field<br>3. Fill in the required Submitted On field<br>4. Click Submit | Name field displays an error indicating the value is below the minimum allowed | medium |
| TC-020 (boundary) | WF-004 | Upload file at exact size limit |  | 1. Select a file exactly at the size limit in the File Picker<br>2. Click Upload | File uploads successfully; confirmation message displayed | medium |
| TC-021 (boundary) | WF-004 | Upload file one byte over size limit |  | 1. Select a file one byte over the size limit in the File Picker<br>2. Click Upload | Upload is blocked; error message shown indicating file exceeds size limit | medium |
| TC-022 (input_edge) |  | Enter long text in Name field |  | 1. Enter a very long string (200+ characters) in the Name field<br>2. Fill in the required Office field<br>3. Fill in the required Submitted On field<br>4. Click Submit | Form submits successfully; saved value shows the long string in the detail page | low |
| TC-023 (input_edge) |  | Enter special characters in Name field |  | 1. Enter special characters (e.g., @#$%^&*) in the Name field<br>2. Fill in the required Office field<br>3. Fill in the required Submitted On field<br>4. Click Submit | Form submits successfully; saved value shows the special characters in the detail page | low |

---

## Center Management

Total: **20** (positive: 7, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-003 | Create a new center with valid details | User logged in as <Role> | 1. Click 'Create Center' button<br>2. Enter <valid center name> in the Name field<br>3. Enter <valid office name> in the Office field<br>4. Enter <valid submission date> in the Submitted On field<br>5. Click Submit | The center is created successfully | high |
| TC-002 | WF-002 | Import centers using a valid file | User logged in as <Role> | 1. Click 'Import Center' button<br>2. Upload a <valid file> in the File Upload field<br>3. Click Submit | Centers imported successfully | high |
| TC-003 | WF-001 | View center details | User logged in as <Role>, At least one center exists | 1. Click on the center's Name link in the Centers table | View center details | medium |
| TC-004 | WF-004 | Activate a center | User logged in as <Role>, Center is in 'Inactive' status | 1. Click on the center's Name link in the Centers table<br>2. Click Activate button | Center activated | medium |
| TC-005 | WF-005 | Edit center details | User logged in as <Role>, Center exists | 1. Click on the center's Name link in the Centers table<br>2. Click Edit button<br>3. Update <valid center name> in the Name field<br>4. Click Submit | Center details updated | medium |
| TC-006 | WF-006 | Close a center | User logged in as <Role>, Center is active | 1. Click on the center's Name link in the Centers table<br>2. Click Close button | Center closed | medium |
| TC-007 | WF-007 | Assign staff to a center | User logged in as <Role>, Center exists | 1. Click on the center's Name link in the Centers table<br>2. Click Assign Staff button | Staff assigned to center | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-003 | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-003 | Leave the Office field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-010 | WF-003 | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 | WF-002 | Leave the File Upload field blank and submit the Bulk Import Centers form |  | 1. Leave the File Upload field blank<br>2. Click Import Center | Inline validation error appears on the File Upload field indicating it is required | high |
| TC-012 | WF-004 | Attempt to activate a center that is already active |  | 1. Navigate to the Center Detail page of an active center<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-013 | WF-006 | Attempt to close a center that is already closed |  | 1. Navigate to the Center Detail page of a closed center<br>2. Click Close | Status remains Closed; no transition occurs | medium |
| TC-014 | WF-007 | Attempt to assign staff to a center that has no staff assigned |  | 1. Navigate to the Center Detail page of a center with no staff assigned<br>2. Click Assign Staff | No staff assigned; action is blocked | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-003 | Submit Create Center form with required fields at minimum length |  | 1. Enter minimum allowed value in the Name field<br>2. Enter minimum allowed value in the Office field<br>3. Enter minimum allowed value in the Submitted On field<br>4. Click Submit | Form submits successfully; center is created with the minimum values | medium |
| TC-016 (boundary) | WF-003 | Submit Create Center form with required fields below minimum length |  | 1. Enter one character below minimum length in the Name field<br>2. Enter one character below minimum length in the Office field<br>3. Enter valid date in the Submitted On field<br>4. Click Submit | Submission is blocked; error shown for Name and Office fields indicating minimum length not met | medium |
| TC-017 (boundary) | WF-002 | Upload file at exact size limit for Bulk Import Centers |  | 1. Upload a file exactly at the size limit in the File Upload field<br>2. Click Submit | File uploads successfully; import process begins with a visible success indicator | medium |
| TC-018 (boundary) | WF-002 | Upload file over size limit for Bulk Import Centers |  | 1. Upload a file one byte over the size limit in the File Upload field<br>2. Click Submit | Submission is blocked; error shown indicating file exceeds size limit | medium |
| TC-019 (input_edge) |  | Enter long text in Name field |  | 1. Enter a string of 200+ characters in the Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; center is created with the long Name value | low |
| TC-020 (input_edge) |  | Enter special characters in Office field |  | 1. Enter special characters in the Office field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; center is created with the special characters in the Office field | low |

---

## Loan Products

Total: **17** (positive: 4, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Loan Product Details | User logged in as <Role> | 1. Click on an existing product name in the Loan Products Table | opens detail view | high |
| TC-002 | WF-002 | Edit Loan Product | User logged in as <Role> | 1. Click on the Edit option for an existing product in the Loan Products Table | opens detail view | high |
| TC-003 | WF-003 | Create New Loan Product | User logged in as <Role> | 1. Click the '+ Create Loan Product' button | opens 6-step stepper wizard | high |
| TC-004 | WF-004 | Complete Loan Product Creation | User logged in as <Role>, User is on the 6-step stepper wizard | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Click Next to proceed to Step 2<br>4. Select <valid currency> from the Currency Selection dropdown<br>5. Enter <valid principal amount> in the Principal Amount field<br>6. Click Next to proceed to Step 3<br>7. Select <valid amortization method> from the Amortization Method dropdown<br>8. Select <valid interest method> from the Interest Method dropdown<br>9. Click Next to proceed to Step 4<br>10. Enter <valid number of repayments> in the Number of Repayments field<br>11. Select <valid repayment frequency> from the Repaid Every dropdown<br>12. Enter <valid nominal interest rate> in the Nominal Interest Rate field<br>13. Click Next to proceed to Step 5<br>14. Search and add <valid charge> in the Search and Add Charges field<br>15. Click Next to proceed to Step 6<br>16. Select <valid accounting method> from the Accounting Method radio options<br>17. If accounting method is not 'None', select <valid GL account mapping> from the GL Account Mappings dropdown<br>18. Click Submit to create the loan product | Loan product created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Product Name field blank and submit |  | 1. Click on the '+ Create Loan Product' button<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name field with a valid value<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the Short Name field blank and submit |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-007 | WF-004 | Submit the Loan Product creation with all required fields empty |  | 1. Click on the '+ Create Loan Product' button<br>2. Click Next on the Details step without filling any fields<br>3. Click Next on the Currency step<br>4. Click Next on the Settings step<br>5. Click Next on the Terms step<br>6. Click Next on the Charges step<br>7. Click Next on the Accounting step<br>8. Click Submit | Form does not submit; Loan product is not created; error shown on Product Name and Short Name fields | high |
| TC-008 | WF-003 | Enter an invalid date in the Start Date field |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Fill in the Short Name field with a valid value<br>4. Enter <invalid date format> in the Start Date field<br>5. Click Next | Inline validation error appears on the Start Date field indicating it must be a valid date | medium |
| TC-009 | WF-003 | Enter a Principal Amount below the minimum required value |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Fill in the Short Name field with a valid value<br>4. Click Next to the Currency step<br>5. Enter <amount below minimum> in the Principal Amount field<br>6. Click Next | Inline validation error appears on the Principal Amount field indicating Minimum value required | medium |
| TC-010 | WF-003 | Enter a Number of Repayments below the minimum required value |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Fill in the Short Name field with a valid value<br>4. Click Next to the Terms step<br>5. Enter <number below minimum> in the Number of Repayments field<br>6. Click Next | Inline validation error appears on the Number of Repayments field indicating Minimum value required | medium |
| TC-011 | WF-003 | Attempt to select GL Account Mappings without selecting Accounting Method |  | 1. Click on the '+ Create Loan Product' button<br>2. Fill in the Product Name field with a valid value<br>3. Fill in the Short Name field with a valid value<br>4. Click Next to the Accounting step<br>5. Attempt to select a GL Account Mapping | GL Account Mappings field is not visible; no action can be taken | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-003 | Enter minimum Principal Amount | User is on the Create Loan Product wizard | 1. Fill in all required fields in Step 1<br>2. Enter the minimum allowed value in the Principal Amount field in Step 2<br>3. Complete all other required fields<br>4. Click Submit | Loan product is created successfully with the minimum Principal Amount | medium |
| TC-013 (boundary) | WF-003 | Enter one unit below minimum Principal Amount | User is on the Create Loan Product wizard | 1. Fill in all required fields in Step 1<br>2. Enter one unit below the minimum allowed value in the Principal Amount field in Step 2<br>3. Complete all other required fields<br>4. Click Submit | Form submission is blocked; inline error displays for Principal Amount indicating it is below the minimum required value | medium |
| TC-014 (boundary) | WF-004 | Enter maximum Number of Repayments | User is on the Create Loan Product wizard | 1. Fill in all required fields in Step 1<br>2. Enter the maximum allowed value in the Number of Repayments field in Step 4<br>3. Complete all other required fields<br>4. Click Submit | Loan product is created successfully with the maximum Number of Repayments | medium |
| TC-015 (boundary) | WF-004 | Enter one unit above maximum Number of Repayments | User is on the Create Loan Product wizard | 1. Fill in all required fields in Step 1<br>2. Enter one unit above the maximum allowed value in the Number of Repayments field in Step 4<br>3. Complete all other required fields<br>4. Click Submit | Form submission is blocked; inline error displays for Number of Repayments indicating it exceeds the maximum allowed value | medium |
| TC-016 (input_edge) | WF-003 | Enter a very long Product Name | User is on the Create Loan Product wizard | 1. Enter a string longer than 200 characters in the Product Name field in Step 1<br>2. Fill in all other required fields<br>3. Click Submit | Form submission is blocked; inline error displays for Product Name indicating it exceeds the maximum length allowed | low |
| TC-017 (input_edge) | WF-003 | Enter special characters in Short Name | User is on the Create Loan Product wizard | 1. Enter special characters in the Short Name field in Step 1<br>2. Fill in all other required fields<br>3. Click Submit | Form submission is blocked; inline error displays for Short Name indicating invalid characters | low |

---

## Savings Products

Total: **19** (positive: 5, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the Create Savings Product stepper wizard | User logged in as <Role> | 1. Click '+ Create Savings Product' button | opens stepper wizard | high |
| TC-002 | WF-002 | View details of a savings product | User logged in as <Role> | 1. Click on a savings product link in the Name column<br>2. Observe the details of the savings product | View details of the savings product | medium |
| TC-003 | WF-003 | Edit a savings product | User logged in as <Role> | 1. Click on the Edit action for a savings product<br>2. Make changes to the product fields<br>3. Click Save | Edit the savings product | medium |
| TC-004 | WF-004 | Create a Fixed Deposit Product | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Fill in the required fields in the Details step<br>3. Proceed through the steps to complete the Fixed Deposit Product creation | opens stepper wizard | high |
| TC-005 | WF-005 | Create a Recurring Deposit Product | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Fill in the required fields in the Details step<br>3. Proceed through the steps to complete the Recurring Deposit Product creation | opens stepper wizard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave Product Name blank and submit |  | 1. Click on '+ Create Savings Product'<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name field with valid data<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-007 | WF-001 | Leave Short Name blank and submit |  | 1. Click on '+ Create Savings Product'<br>2. Fill in the Product Name field with valid data<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-008 | WF-001 | Leave all required fields blank and submit |  | 1. Click on '+ Create Savings Product'<br>2. Leave the Product Name field blank<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required; Inline validation error appears on the Short Name field indicating it is required | high |
| TC-009 | WF-001 | Attempt to create a savings product without filling required fields in the wizard |  | 1. Click on '+ Create Savings Product'<br>2. Click Next without filling any fields | Inline validation error appears on the Product Name field indicating it is required; Inline validation error appears on the Short Name field indicating it is required | high |
| TC-010 | WF-001 | Attempt to create a savings product with invalid data in numeric fields |  | 1. Click on '+ Create Savings Product'<br>2. Fill in the Product Name field with valid data<br>3. Fill in the Short Name field with valid data<br>4. Fill in the Nominal Annual Interest Rate field with <non-numeric input><br>5. Click Next | Inline validation error appears on the Nominal Annual Interest Rate field indicating it must be a number | medium |
| TC-011 | WF-001 | Attempt to create a savings product with invalid currency format |  | 1. Click on '+ Create Savings Product'<br>2. Fill in the Product Name field with valid data<br>3. Fill in the Short Name field with valid data<br>4. Click Next without filling any currency fields | No currency fields are filled; proceed to next step without errors | medium |
| TC-012 | WF-004 | Attempt to create a Fixed Deposit Product without filling required fields in the wizard |  | 1. Click on '+ Create Savings Product'<br>2. Click Next without filling any fields for Fixed Deposit Product | Inline validation error appears on the required fields for Fixed Deposit Product | high |
| TC-013 | WF-005 | Attempt to create a Recurring Deposit Product without filling required fields in the wizard |  | 1. Click on '+ Create Savings Product'<br>2. Click Next without filling any fields for Recurring Deposit Product | Inline validation error appears on the required fields for Recurring Deposit Product | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Minimum value for Minimum Required Balance |  | 1. Click '+ Create Savings Product'<br>2. Fill in 'Product Name' with valid data<br>3. Fill in 'Short Name' with valid data<br>4. Enter exactly <minimum value> in the 'Minimum Required Balance' field<br>5. Complete all other required fields<br>6. Click Submit | Form submits successfully; entity is created with the <minimum value> | medium |
| TC-015 (boundary) | WF-001 | One unit below minimum for Minimum Required Balance |  | 1. Click '+ Create Savings Product'<br>2. Fill in 'Product Name' with valid data<br>3. Fill in 'Short Name' with valid data<br>4. Enter <one unit below minimum> in the 'Minimum Required Balance' field<br>5. Complete all other required fields<br>6. Click Submit | 'Minimum Required Balance' displays an error indicating the value is below the minimum allowed | medium |
| TC-016 (boundary) | WF-001 | Maximum value for Maximum Overdraft Amount |  | 1. Click '+ Create Savings Product'<br>2. Fill in 'Product Name' with valid data<br>3. Fill in 'Short Name' with valid data<br>4. Enter exactly <maximum value> in the 'Maximum Overdraft Amount' field<br>5. Complete all other required fields<br>6. Click Submit | Form submits successfully; entity is created with the <maximum value> | medium |
| TC-017 (boundary) | WF-001 | One unit above maximum for Maximum Overdraft Amount |  | 1. Click '+ Create Savings Product'<br>2. Fill in 'Product Name' with valid data<br>3. Fill in 'Short Name' with valid data<br>4. Enter <one unit above maximum> in the 'Maximum Overdraft Amount' field<br>5. Complete all other required fields<br>6. Click Submit | 'Maximum Overdraft Amount' displays an error indicating the value exceeds the maximum allowed | medium |
| TC-018 (input_edge) | WF-001 | Long text in Product Name |  | 1. Click '+ Create Savings Product'<br>2. Enter a string of 200+ characters in the 'Product Name' field<br>3. Fill in 'Short Name' with valid data<br>4. Complete all other required fields<br>5. Click Submit | Form submits successfully; entity is created with the long Product Name | low |
| TC-019 (input_edge) | WF-001 | Leading/trailing whitespace in Short Name |  | 1. Click '+ Create Savings Product'<br>2. Enter '   Short Name   ' in the 'Short Name' field<br>3. Fill in 'Product Name' with valid data<br>4. Complete all other required fields<br>5. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Share Products

Total: **24** (positive: 7, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Create Share Product Wizard | User logged in as <Role> | 1. Click the '+ Create Share Product' button | opens 7-step stepper wizard | high |
| TC-002 | WF-002 | Edit Product Details | User logged in as <Role>, At least one product exists in the Share Products table | 1. Click on the Product Name link of the existing product<br>2. Click the 'Edit' option | Product details updated | medium |
| TC-003 | WF-003 | Delete Product | User logged in as <Role>, At least one product exists in the Share Products table | 1. Click on the Product Name link of the existing product<br>2. Click the 'Delete' option | Product deleted | medium |
| TC-004 | WF-001 | Complete Create Share Product Wizard - Step 1 | User logged in as <Role>, User has opened the 7-step stepper wizard | 1. Enter <valid product name> in the Product Name field<br>2. Enter <valid short name> in the Short Name field<br>3. Enter <valid description> in the Description field<br>4. Click 'Next' to proceed to Step 2 | Step 2 (Currency) is visible | high |
| TC-005 | WF-001 | Complete Create Share Product Wizard - Step 3 | User logged in as <Role>, User has completed Step 1 of the wizard | 1. Enter <valid total number of shares> in the Total Number of Shares field<br>2. Enter <valid nominal unit price> in the Nominal Unit Price field<br>3. Click 'Next' to proceed to Step 4 | Step 4 (Settings) is visible | high |
| TC-006 | WF-001 | Complete Create Share Product Wizard - Step 5 | User logged in as <Role>, User has completed Step 4 of the wizard | 1. Click 'Add Row' in the Market Price section<br>2. Enter <valid from date> in the From Date field<br>3. Enter <valid share value> in the Share Value field<br>4. Click 'Next' to proceed to Step 6 | Step 6 (Charges) is visible | high |
| TC-007 | WF-001 | Complete Create Share Product Wizard - Step 7 | User logged in as <Role>, User has completed Step 6 of the wizard | 1. Select 'Cash-based' from the Accounting Method radio options<br>2. Enter <valid share reference> in the Share Reference field<br>3. Click 'Finish' to complete the wizard | A success notification is displayed; the product is listed in the Share Products table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Leave Product Name blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Leave the Product Name field blank<br>3. Fill in Short Name and Description fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-009 | WF-001 | Leave Short Name blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name and Description fields<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-010 | WF-001 | Leave Description blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name and Short Name fields<br>3. Leave the Description field blank<br>4. Click Next | Inline validation error appears on the Description field indicating it is required | high |
| TC-011 | WF-001 | Leave Total Number of Shares blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name, Short Name, and Description fields<br>3. Leave the Total Number of Shares field blank<br>4. Click Next | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-012 | WF-001 | Leave Nominal Unit Price blank and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name, Short Name, Description, and Total Number of Shares fields<br>3. Leave the Nominal Unit Price field blank<br>4. Click Next | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-013 | WF-001 | Leave From Date blank in Market Price and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name, Short Name, Description, Total Number of Shares, and Nominal Unit Price fields<br>3. Add a Market Price row with Share Value filled and leave From Date blank<br>4. Click Next | Inline validation error appears on the From Date field indicating it is required | high |
| TC-014 | WF-001 | Leave Share Value blank in Market Price and submit |  | 1. Click '+ Create Share Product' button<br>2. Fill in Product Name, Short Name, Description, Total Number of Shares, and Nominal Unit Price fields<br>3. Add a Market Price row with From Date filled and leave Share Value blank<br>4. Click Next | Inline validation error appears on the Share Value field indicating it is required | high |
| TC-015 | WF-002 | Attempt to edit product without permission |  | 1. Attempt to click on the Edit action for a product | User is blocked from editing the product due to insufficient permissions | medium |
| TC-016 | WF-003 | Attempt to delete product without permission |  | 1. Attempt to click on the Delete action for a product | User is blocked from deleting the product due to insufficient permissions | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-001 | Enter minimum required Total Number of Shares | User is on the Create Share Product wizard | 1. Enter <minimum allowed value> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | Form submits successfully; user proceeds to the next step of the wizard. | medium |
| TC-018 (boundary) | WF-001 | Enter one less than required Total Number of Shares | User is on the Create Share Product wizard | 1. Enter <one unit below minimum> in the Total Number of Shares field<br>2. Fill all other required fields<br>3. Click Next | An error message is displayed indicating that Total Number of Shares is required. | medium |
| TC-019 (boundary) | WF-001 | Add maximum allowed rows to Market Price repeating group | User is on the Create Share Product wizard, step 5 | 1. Add <maximum allowed entries> rows to the Market Price table<br>2. Fill in all required fields for each row<br>3. Click Next | Form submits successfully; user proceeds to the next step of the wizard. | medium |
| TC-020 (boundary) | WF-001 | Attempt to add one more row to Market Price repeating group | User is on the Create Share Product wizard, step 5 | 1. Add <maximum allowed entries> rows to the Market Price table<br>2. Attempt to add one more row<br>3. Click Next | An error message is displayed indicating that the maximum number of entries has been reached. | medium |
| TC-021 (data_edge) | WF-001 | Enter today's date in From Date field | User is on the Create Share Product wizard, step 5 | 1. Enter today's date in the From Date field<br>2. Enter a valid Share Value<br>3. Click Add | Row is added successfully to the Market Price table with today's date. | medium |
| TC-022 (data_edge) | WF-001 | Enter a far future date in From Date field | User is on the Create Share Product wizard, step 5 | 1. Enter a far future date in the From Date field<br>2. Enter a valid Share Value<br>3. Click Add | Row is added successfully to the Market Price table with the far future date. | medium |
| TC-023 (data_edge) | WF-001 | Enter a date one day before today's date in From Date field | User is on the Create Share Product wizard, step 5 | 1. Enter yesterday's date in the From Date field<br>2. Enter a valid Share Value<br>3. Click Add | Row is added successfully to the Market Price table with yesterday's date. | medium |
| TC-024 (input_edge) | WF-001 | Enter a very long string in Product Name field | User is on the Create Share Product wizard | 1. Enter a string longer than 200 characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Next | An error message is displayed indicating that the input exceeds the maximum allowed length. | low |

---

## Charges

Total: **14** (positive: 3, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-003 | Create a new charge successfully | User logged in as <Role> | 1. Click the '+ Create Charge' button<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Enter <Currency> in the Currency field<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <Amount> in the Amount field<br>8. Click Submit | Charge definition is created | high |
| TC-002 | WF-001 | Edit an existing charge | User logged in as <Role>, At least one charge exists in the Charges table | 1. Click the Name link of an existing charge in the Charges table<br>2. Click the Edit button<br>3. Modify <Charge Name> in the Charge Name field<br>4. Click Submit | Charge definition is updated | medium |
| TC-003 | WF-002 | Delete an existing charge | User logged in as <Role>, At least one charge exists in the Charges table | 1. Click the Delete button for an existing charge in the Charges table<br>2. Confirm the deletion | Charge deleted; success message shown | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Leave Charge Name blank and submit |  | 1. Leave the Charge Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-005 | WF-003 | Leave Charge Applies To blank and submit |  | 1. Leave the Charge Applies To field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-006 | WF-003 | Leave Currency blank and submit |  | 1. Leave the Currency field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-007 | WF-003 | Leave Amount blank and submit |  | 1. Leave the Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-008 | WF-003 | Enter invalid value in Charge Applies To dropdown and submit |  | 1. Select an invalid option in the Charge Applies To field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Charge Applies To field indicating it must be a valid option | medium |
| TC-009 | WF-003 | Enter negative value in Amount field and submit |  | 1. Enter <negative amount> in the Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Amount is not created; error shown on Amount field indicating it must be a positive value | medium |
| TC-010 | WF-002 | Attempt to delete a charge without confirmation |  | 1. Click Delete on an existing charge<br>2. Do not confirm the deletion | Charge remains unchanged; no deletion occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-003 | Enter minimum allowed value in Amount field | User is on the Create Charge form | 1. Enter <minimum allowed value> in the Amount field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; charge definition is created with the <minimum allowed value> in the Amount field | medium |
| TC-012 (boundary) | WF-003 | Enter one unit above maximum in Amount field | User is on the Create Charge form | 1. Enter <one unit above maximum> in the Amount field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Submission is blocked; error message displayed indicating the amount exceeds the maximum allowed | medium |
| TC-013 (input_edge) |  | Enter a very long string in Charge Name field | User is on the Create Charge form | 1. Enter a string of 200+ characters in the Charge Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error message displayed indicating the Charge Name exceeds maximum length | low |
| TC-014 (input_edge) |  | Enter special characters in Currency field | User is on the Create Charge form | 1. Enter special characters in the Currency field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Submission is blocked; error message displayed indicating invalid characters in Currency field | low |

---

## Floating Rates

Total: **14** (positive: 4, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Floating Rate Details | User logged in as <Role> | 1. Click on the Floating Rate Name link in the Floating Rates Table | Displays full rate history | high |
| TC-002 | WF-002 | Edit Floating Rate | User logged in as <Role> | 1. Click on the Edit action for a Floating Rate in the Floating Rates Table | Opens edit form for the floating rate | high |
| TC-003 | WF-003 | Create Floating Rate | User logged in as <Role> | 1. Click the '+ Create Floating Rate' button | opens creation form | high |
| TC-004 | WF-003 | Submit Floating Rate Creation Form | User logged in as <Role>, Creation form is open | 1. Enter <Floating Rate Name> in the Floating Rate Name field<br>2. Check the Is Base Lending Rate checkbox<br>3. Check the Is Active checkbox<br>4. Click 'Add Row' in the Rate Periods table<br>5. Enter <From Date> in the From Date field of the new row<br>6. Enter <Interest Rate> in the Interest Rate field of the new row<br>7. Check the Is Differential Rate checkbox in the new row<br>8. Click Submit | The Floating Rates Table updates to show the new floating rate with the entered details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Floating Rate Name field blank and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the From Date field blank in Rate Periods and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Add a row in Rate Periods<br>3. Leave the From Date field blank<br>4. Fill in the Interest Rate field with a valid number<br>5. Click Submit | Inline validation error appears on the From Date field indicating it is required | high |
| TC-007 | WF-003 | Leave the Interest Rate field blank in Rate Periods and submit |  | 1. Click on the '+ Create Floating Rate' button<br>2. Add a row in Rate Periods<br>3. Fill in the From Date field with a valid date<br>4. Leave the Interest Rate field blank<br>5. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-008 | WF-003 | Attempt to create a second base lending rate |  | 1. Click on the '+ Create Floating Rate' button<br>2. Fill in the Floating Rate Name field with a valid name<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit<br>5. Click on the '+ Create Floating Rate' button again<br>6. Fill in another Floating Rate Name field with a valid name<br>7. Check the Is Base Lending Rate checkbox<br>8. Click Submit | Form does not submit; error shown indicating 'only one base rate can exist at a time' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-003 | Enter a valid Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name in the Floating Rate Name field | Form submits successfully; entity is created with the valid Floating Rate Name | medium |
| TC-010 (boundary) | WF-003 | Attempt to create a base lending rate when one already exists | A base lending rate already exists | 1. Click the '+ Create Floating Rate' button<br>2. Enter a valid Floating Rate Name in the Floating Rate Name field<br>3. Check the Is Base Lending Rate checkbox<br>4. Click Submit | Submission is blocked; an error message indicates that only one base rate can exist at a time | medium |
| TC-011 (boundary) | WF-003 | Add maximum allowed entries to Rate Periods |  | 1. Click the '+ Create Floating Rate' button<br>2. Add maximum allowed entries to the Rate Periods table<br>3. Click Submit | Form submits successfully; all entries are saved | medium |
| TC-012 (boundary) | WF-003 | Attempt to add one more entry than allowed in Rate Periods |  | 1. Click the '+ Create Floating Rate' button<br>2. Add maximum allowed entries to the Rate Periods table<br>3. Attempt to add one more entry<br>4. Click Submit | Submission is blocked; an error message indicates the maximum number of entries has been exceeded | medium |
| TC-013 (input_edge) |  | Enter a very long Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter a very long string (200+ characters) in the Floating Rate Name field | The input is either accepted or truncated with a visible indicator | low |
| TC-014 (input_edge) |  | Enter special characters in the Floating Rate Name |  | 1. Click the '+ Create Floating Rate' button<br>2. Enter special characters in the Floating Rate Name field | The input is either accepted or a specific error is shown | low |

---

## Delinquency Management

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a delinquency range with required fields | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <Classification> in the Classification field<br>4. Enter <valid number> in the Minimum Age Days field<br>5. Click Submit | Delinquency range created; success message shown | high |
| TC-002 | WF-002 | Create a delinquency range with optional Maximum Age Days | User logged in as <Role> | 1. Navigate to the Delinquency Ranges page<br>2. Click on 'Create Delinquency Range'<br>3. Enter <Classification> in the Classification field<br>4. Enter <valid number> in the Minimum Age Days field<br>5. Leave the Maximum Age Days field blank<br>6. Click Submit | Delinquency range created; success message shown | high |
| TC-003 | WF-003 | Access delinquency range classification details | User logged in as <Role>, At least one delinquency range exists | 1. Navigate to the Delinquency Ranges page<br>2. Click on the Classification link for the first delinquency range | Navigated to classification details | medium |
| TC-004 | WF-004 | Create a delinquency bucket with required fields | User logged in as <Role> | 1. Navigate to the Delinquency Buckets page<br>2. Click on 'Create Delinquency Bucket'<br>3. Enter <Bucket Name> in the Bucket Name field<br>4. Click Submit | Delinquency bucket created; success message shown | high |
| TC-005 | WF-005 | Access delinquency bucket name details | User logged in as <Role>, At least one delinquency bucket exists | 1. Navigate to the Delinquency Buckets page<br>2. Click on the Bucket Name link for the first delinquency bucket | Navigated to bucket details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave the Classification field blank |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-007 | WF-001 | Leave the Minimum Age Days field blank |  | 1. Leave the Minimum Age Days field blank<br>2. Fill Classification with a valid value<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-008 | WF-002 | Leave the Classification field blank for optional Maximum Age Days |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Leave Maximum Age Days blank<br>4. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-009 | WF-004 | Leave the Bucket Name field blank |  | 1. Leave the Bucket Name field blank<br>2. Fill in the Delinquency Ranges with valid values<br>3. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-010 | WF-004 | Leave the Range Name field blank in Delinquency Ranges |  | 1. Fill Bucket Name with a valid value<br>2. Leave the Range Name field blank in Delinquency Ranges<br>3. Fill Days with a valid value<br>4. Click Submit | Inline validation error appears on the Range Name field indicating it is required | high |
| TC-011 | WF-004 | Leave the Days field blank in Delinquency Ranges |  | 1. Fill Bucket Name with a valid value<br>2. Fill Range Name with a valid value in Delinquency Ranges<br>3. Leave the Days field blank<br>4. Click Submit | Inline validation error appears on the Days field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Minimum Age Days at minimum value |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field with valid data<br>3. Click Submit | Form submits successfully; delinquency range created with the <minimum allowed value> | medium |
| TC-013 (boundary) | WF-001 | Minimum Age Days just below minimum value |  | 1. Enter <one unit below minimum> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field with valid data<br>3. Click Submit | <Minimum_Age_Days> displays an error indicating the value is below the minimum allowed | medium |
| TC-014 (boundary) | WF-002 | Maximum Age Days left blank |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field with valid data<br>3. Leave <Maximum_Age_Days> blank<br>4. Click Submit | Form submits successfully; delinquency range created with no upper limit on age days | medium |
| TC-015 (boundary) | WF-002 | Maximum Age Days at maximum value |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field with valid data<br>3. Enter <maximum allowed value> in the <Maximum_Age_Days> field<br>4. Click Submit | Form submits successfully; delinquency range created with <maximum allowed value> | medium |
| TC-016 (boundary) | WF-002 | Maximum Age Days just above maximum value |  | 1. Enter <minimum allowed value> in the <Minimum_Age_Days> field<br>2. Fill in the <Classification> field with valid data<br>3. Enter <one unit above maximum> in the <Maximum_Age_Days> field<br>4. Click Submit | <Maximum_Age_Days> displays an error indicating the value exceeds the maximum allowed | medium |
| TC-017 (interaction_edge) | WF-004 | Repeating group: add then remove all |  | 1. Click to add a new delinquency range in the <Delinquency_Ranges> repeating group<br>2. Fill in all required fields for the first range<br>3. Click to add another delinquency range<br>4. Fill in all required fields for the second range<br>5. Remove all added delinquency ranges<br>6. Click Submit | Form submits successfully; no delinquency ranges are required, and the submission is accepted | medium |

---

## Loan Account

Total: **26** (positive: 2, negative: 18, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application with valid details | User logged in as <Client>, Loan Application Wizard is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number of repayments> in the Number of Repayments field<br>9. Select <frequency> from the Repaid Every dropdown<br>10. Select <unit> from the Repaid Every dropdown<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Click Submit | Loan is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-001 | Submit Loan Application with collateral items | User logged in as <Client>, Loan Application Wizard is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number of repayments> in the Number of Repayments field<br>9. Select <frequency> from the Repaid Every dropdown<br>10. Select <unit> from the Repaid Every dropdown<br>11. Enter <valid interest rate> in the Interest Rate field<br>12. Click 'Add Charge' to add additional charges<br>13. Click 'Add Row' to add collateral items<br>14. Enter <Collateral Type> in the Collateral Type field<br>15. Enter <valid value> in the Value field<br>16. Click Submit | Loan is created in 'Submitted and Pending Approval' status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-004 |  | Leave the Loan Officer field blank and submit |  | 1. Leave the Loan Officer field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Officer field indicating it is required | high |
| TC-005 |  | Leave the Loan Purpose field blank and submit |  | 1. Leave the Loan Purpose field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Purpose field indicating it is required | high |
| TC-006 |  | Leave the Fund field blank and submit |  | 1. Leave the Fund field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fund field indicating it is required | high |
| TC-007 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-008 |  | Leave the Expected Disbursement Date blank and submit |  | 1. Leave the Expected Disbursement Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it is required | high |
| TC-009 |  | Leave the Principal field blank and submit |  | 1. Leave the Principal field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is required | high |
| TC-010 |  | Leave the Number of Repayments field blank and submit |  | 1. Leave the Number of Repayments field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it is required | high |
| TC-011 |  | Leave the Repaid Every field blank and submit |  | 1. Leave the Repaid Every field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-012 |  | Leave the Interest Rate field blank and submit |  | 1. Leave the Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is required | high |
| TC-013 |  | Leave all required fields blank and submit |  | 1. Leave all required fields blank<br>2. Click Submit | Inline validation error appears on the Product Name, Loan Officer, Loan Purpose, Fund, Submitted On, Expected Disbursement Date, Principal, Number of Repayments, Repaid Every, and Interest Rate fields indicating they are required | high |
| TC-014 |  | Enter an invalid date in the Submitted On field and submit |  | 1. Enter <invalid date format> in the Submitted On field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it must be a valid date | medium |
| TC-015 |  | Enter an invalid date in the Expected Disbursement Date field and submit |  | 1. Enter <invalid date format> in the Expected Disbursement Date field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Expected Disbursement Date field indicating it must be a valid date | medium |
| TC-016 |  | Enter a Principal amount below the minimum bound and submit |  | 1. Enter <amount below minimum> in the Principal field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Principal field indicating it is bounded by product min/max | medium |
| TC-017 |  | Enter an Interest Rate above the maximum bound and submit |  | 1. Enter <amount exceeding maximum> in the Interest Rate field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline validation error appears on the Interest Rate field indicating it is bounded by product min/max | medium |
| TC-018 | WF-001 | Attempt to submit the loan application without filling required fields |  | 1. Leave required fields blank<br>2. Click Submit | Form does not submit; loan is not created; inline validation errors are shown on all required fields | high |
| TC-019 |  | Attempt to approve a loan while it is not in Pending Approval state |  | 1. Navigate to the Loan Detail page<br>2. Attempt to click Approve while the loan is in Approved state | No Approve action button is visible; user cannot approve the loan | medium |
| TC-020 |  | Attempt to make a repayment while the loan is not in Active state |  | 1. Navigate to the Loan Detail page<br>2. Attempt to click Make Repayment while the loan is in Pending Approval state | No Make Repayment action button is visible; user cannot make a repayment | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Enter minimum Principal amount | User is on Step 1 of the Loan Application Wizard | 1. Select a Product Name from the dropdown<br>2. Fill in Loan Officer, Loan Purpose, Fund fields<br>3. Enter the minimum Principal amount in the Principal field<br>4. Fill in Number of Repayments and Repaid Every fields<br>5. Enter the minimum Interest Rate in the Interest Rate field<br>6. Fill in Submitted On and Expected Disbursement Date fields<br>7. Click Submit | Form submits successfully; loan is created with the minimum Principal amount | medium |
| TC-022 (boundary) | WF-001 | Enter maximum Principal amount | User is on Step 1 of the Loan Application Wizard | 1. Select a Product Name from the dropdown<br>2. Fill in Loan Officer, Loan Purpose, Fund fields<br>3. Enter the maximum Principal amount in the Principal field<br>4. Fill in Number of Repayments and Repaid Every fields<br>5. Enter the maximum Interest Rate in the Interest Rate field<br>6. Fill in Submitted On and Expected Disbursement Date fields<br>7. Click Submit | Form submits successfully; loan is created with the maximum Principal amount | medium |
| TC-023 (boundary) | WF-001 | Enter Principal amount just above maximum | User is on Step 1 of the Loan Application Wizard | 1. Select a Product Name from the dropdown<br>2. Fill in Loan Officer, Loan Purpose, Fund fields<br>3. Enter an amount just above the maximum in the Principal field<br>4. Fill in Number of Repayments and Repaid Every fields<br>5. Enter the maximum Interest Rate in the Interest Rate field<br>6. Fill in Submitted On and Expected Disbursement Date fields<br>7. Click Submit | Form is blocked; error message displayed indicating the Principal amount exceeds the maximum allowed | medium |
| TC-024 (boundary) | WF-001 | Enter Interest Rate just above maximum | User is on Step 1 of the Loan Application Wizard | 1. Select a Product Name from the dropdown<br>2. Fill in Loan Officer, Loan Purpose, Fund fields<br>3. Enter the maximum Principal amount in the Principal field<br>4. Fill in Number of Repayments and Repaid Every fields<br>5. Enter an Interest Rate just above the maximum in the Interest Rate field<br>6. Fill in Submitted On and Expected Disbursement Date fields<br>7. Click Submit | Form is blocked; error message displayed indicating the Interest Rate exceeds the maximum allowed | medium |
| TC-025 (input_edge) |  | Enter a very long description in Collateral items | User is on Step 4 of the Loan Application Wizard | 1. Click 'Add Charge' button<br>2. Enter a very long string (200+ characters) in the Description field<br>3. Fill in Collateral Type and Value fields<br>4. Click Submit | Form submits successfully; the long description is saved correctly in the detail page | low |
| TC-026 (input_edge) |  | Enter special characters in Loan Officer field | User is on Step 1 of the Loan Application Wizard | 1. Select a Product Name from the dropdown<br>2. Enter special characters in the Loan Officer field<br>3. Fill in Loan Purpose, Fund fields<br>4. Enter the minimum Principal amount in the Principal field<br>5. Fill in Number of Repayments and Repaid Every fields<br>6. Enter the minimum Interest Rate in the Interest Rate field<br>7. Fill in Submitted On and Expected Disbursement Date fields<br>8. Click Submit | Form is blocked; error message displayed indicating invalid characters in the Loan Officer field | low |

---

## Savings Account

Total: **29** (positive: 14, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Savings Account Creation Form | User logged in as <Role> | 1. Open the Savings Account Creation Form<br>2. Select <valid product name> from the Product Name dropdown<br>3. Enter <valid date> in the Submitted On field<br>4. Enter <valid minimum opening balance> in the Minimum Opening Balance field<br>5. Click Submit | Account is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-002 | Approve Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Approve on the Savings Account Detail page | Account status updates to 'Approved' | high |
| TC-003 | WF-003 | Reject Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Reject on the Savings Account Detail page | Application is rejected | high |
| TC-004 | WF-004 | Withdraw Application for Pending Savings Account | User logged in as <Role>, Account is in Pending status | 1. Click Withdraw Application on the Savings Account Detail page | Application is withdrawn | high |
| TC-005 | WF-005 | Activate Approved Savings Account | User logged in as <Role>, Account is in Approved status | 1. Click Activate on the Savings Account Detail page | Account is activated | high |
| TC-006 | WF-006 | Undo Approval for Approved Savings Account | User logged in as <Role>, Account is in Approved status | 1. Click Undo Approval on the Savings Account Detail page | Approval is undone | high |
| TC-007 | WF-007 | Deposit into Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Deposit on the Savings Account Detail page<br>2. Enter <valid transaction date> in the Transaction Date field<br>3. Enter <valid transaction amount> in the Transaction Amount field<br>4. Select <valid payment type> from the Payment Type dropdown<br>5. Click Submit | Account is credited with the deposit | high |
| TC-008 | WF-008 | Withdraw from Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Withdraw on the Savings Account Detail page<br>2. Enter <valid transaction date> in the Transaction Date field<br>3. Enter <valid transaction amount> in the Transaction Amount field<br>4. Select <valid payment type> from the Payment Type dropdown<br>5. Click Submit | Account is debited with the withdrawal | high |
| TC-009 | WF-009 | Post Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Post Interest on the Savings Account Detail page | Interest is posted to the account | high |
| TC-010 | WF-010 | Calculate Interest for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Calculate Interest on the Savings Account Detail page | Interest is calculated | high |
| TC-011 | WF-011 | Close Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Close on the Savings Account Detail page | Account is closed | high |
| TC-012 | WF-012 | Block Account for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Account on the Savings Account Detail page | Account is blocked | high |
| TC-013 | WF-013 | Block Debit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Debit on the Savings Account Detail page | Debit is blocked | high |
| TC-014 | WF-014 | Block Credit for Active Savings Account | User logged in as <Role>, Account is in Active status | 1. Click Block Credit on the Savings Account Detail page | Credit is blocked | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Leave the Product Name dropdown blank and submit |  | 1. Leave the Product Name dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-016 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-017 |  | Leave the Minimum Opening Balance blank and submit |  | 1. Leave the Minimum Opening Balance blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Minimum Opening Balance field indicating it is required | high |
| TC-018 |  | Submit with all required fields empty |  | 1. Leave the Product Name dropdown blank<br>2. Leave the Submitted On date blank<br>3. Leave the Minimum Opening Balance blank<br>4. Click Submit | Form does not submit; errors shown on Product Name, Submitted On, and Minimum Opening Balance fields | high |
| TC-019 | WF-002 | Attempt to approve a Pending account when it is already Approved |  | 1. Navigate to the Approved Savings Account<br>2. Click Approve | Status remains Approved; no transition occurs | high |
| TC-020 | WF-008 | Withdraw from Active account exceeding available balance without overdraft enabled |  | 1. Navigate to the Active Savings Account<br>2. Fill in the Transaction Date<br>3. Enter <amount exceeding available balance> in the Transaction Amount field<br>4. Select a Payment Type<br>5. Click Withdraw | Form does not submit; error shown indicating withdrawal cannot exceed available balance unless overdraft is enabled | medium |
| TC-021 | WF-008 | Withdraw from Active account that would breach minimum balance |  | 1. Navigate to the Active Savings Account<br>2. Fill in the Transaction Date<br>3. Enter <amount that breaches minimum balance> in the Transaction Amount field<br>4. Select a Payment Type<br>5. Click Withdraw | Form does not submit; error shown indicating minimum balance must be enforced | medium |
| TC-022 | WF-011 | Attempt to close an account that is already closed |  | 1. Navigate to the Closed Savings Account<br>2. Click Close | Status remains Closed; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 (boundary) | WF-001 | Submit Savings Account Creation Form with Minimum Opening Balance |  | 1. Select a product from the Product Name dropdown<br>2. Enter today's date in the Submitted On field<br>3. Enter the minimum allowed value in the Minimum Opening Balance field<br>4. Click Submit | Form submits successfully; account is created in 'Submitted and Pending Approval' status | medium |
| TC-024 (boundary) | WF-001 | Submit Savings Account Creation Form with Minimum Opening Balance - Below Minimum |  | 1. Select a product from the Product Name dropdown<br>2. Enter today's date in the Submitted On field<br>3. Enter one unit below the minimum allowed value in the Minimum Opening Balance field<br>4. Click Submit | Form submission is blocked; error message displayed indicating the minimum opening balance requirement | medium |
| TC-025 (boundary) | WF-008 | Withdraw from Active Savings Account Exceeding Available Balance | Account is in Active status with a balance of $100 | 1. Navigate to the Withdraw action for the Active Savings Account<br>2. Enter today's date in the Transaction Date field<br>3. Enter $150 in the Transaction Amount field<br>4. Select 'Cash' in the Payment Type dropdown<br>5. Click Submit | Form submission is blocked; error message displayed indicating withdrawal cannot exceed available balance unless overdraft is enabled | medium |
| TC-026 (boundary) | WF-008 | Withdraw from Active Savings Account Breaching Minimum Balance | Account is in Active status with a balance of $100 and minimum balance enforced | 1. Navigate to the Withdraw action for the Active Savings Account<br>2. Enter today's date in the Transaction Date field<br>3. Enter $90 in the Transaction Amount field<br>4. Select 'Cash' in the Payment Type dropdown<br>5. Click Submit | Form submission is blocked; error message displayed indicating minimum balance must be enforced | medium |
| TC-027 (input_edge) |  | Enter long text in Charge Description |  | 1. Navigate to the Charges section of the Savings Account Creation Form<br>2. Enter a very long string (200+ characters) in the Charge Description field | Field accepts the input; saved value is displayed correctly in the detail page or an error is shown if truncated | low |
| TC-028 (input_edge) |  | Enter special characters in Charge Description |  | 1. Navigate to the Charges section of the Savings Account Creation Form<br>2. Enter special characters (e.g., !@#$%^&*) in the Charge Description field | Field accepts the input; saved value is displayed correctly in the detail page or a specific error is shown | low |
| TC-029 (interaction_edge) |  | Rapid consecutive state transitions for Active Savings Account | Account is in Active status | 1. Click Deposit action<br>2. Immediately click Withdraw action | Both actions are processed successfully or the expected blocking message is shown per spec | medium |

---

## Share Account

Total: **23** (positive: 8, negative: 10, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application | User logged in as <Role>, Client has active savings accounts available | 1. Select <valid share product> from the Share Product dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid number within bounds> in the Requested Shares field<br>4. Enter <valid date> in the Application Date field<br>5. Select <active savings account> from the Savings Account for Charges dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Share Account | User logged in as <Role>, Share account is in Pending status | 1. Enter <valid number of approved shares> in the Approved Shares field<br>2. Enter <valid date> in the Approved Date field<br>3. Click Approve | Approval process initiated | high |
| TC-003 | WF-003 | Reject Share Account | User logged in as <Role>, Share account is in Pending status | 1. Click Reject | Rejection process initiated | high |
| TC-004 | WF-004 | Activate Share Account | User logged in as <Role>, Share account is in Approved status | 1. Click Activate | Account activated | high |
| TC-005 | WF-005 | Undo Approval of Share Account | User logged in as <Role>, Share account is in Approved status | 1. Click Undo Approval | Approval undone | medium |
| TC-006 | WF-006 | Apply Additional Shares | User logged in as <Role>, Share account is in Active status | 1. Click Apply Additional Shares | Additional shares applied | medium |
| TC-007 | WF-007 | Redeem Shares | User logged in as <Role>, Share account is in Active status | 1. Click Redeem Shares | Redemption amount calculated as shares multiplied by current unit price and credited to the linked savings account | medium |
| TC-008 | WF-008 | Close Share Account | User logged in as <Role>, Share account is in Active status | 1. Click Close | Account closed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-010 |  | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 |  | Leave the Requested Shares field blank and submit |  | 1. Leave the Requested Shares field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-012 |  | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-013 |  | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-014 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Submit | Form does not submit; error shown on Share Product, Submitted On, Requested Shares, Application Date, and Savings Account for Charges fields | high |
| TC-015 |  | Submit Requested Shares exceeding product min/max |  | 1. Fill the Requested Shares field with <amount exceeding product max><br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; error shown on Requested Shares field indicating it is bounded by product min/max per client | medium |
| TC-016 | WF-002 | Approve Share Account when state is not Pending |  | 1. Attempt to approve a share account in Approved state<br>2. Click Approve | Status remains Approved; no transition occurs; Approve action is not available | medium |
| TC-017 | WF-004 | Activate Share Account when state is not Approved |  | 1. Attempt to activate a share account in Pending state<br>2. Click Activate | Status remains Pending; no transition occurs; Activate action is not available | medium |
| TC-018 | WF-006 | Apply Additional Shares when state is not Active |  | 1. Attempt to apply additional shares when the account is in Approved state<br>2. Click Apply Additional Shares | Status remains Approved; no transition occurs; Apply Additional Shares action is not available | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-001 | Requested Shares at minimum value | Share Product is selected with a defined minimum for Requested Shares | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed value in the Requested Shares field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-020 (boundary) | WF-001 | Requested Shares above maximum value | Share Product is selected with a defined maximum for Requested Shares | 1. Select a Share Product from the dropdown<br>2. Enter a value greater than the maximum allowed in the Requested Shares field<br>3. Fill all other required fields<br>4. Click Submit | Submission is blocked; an error message indicates the Requested Shares exceed the maximum allowed | medium |
| TC-021 (data_edge) | WF-001 | Application Date set to today |  | 1. Select a Share Product from the dropdown<br>2. Enter today's date in the Application Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-022 (data_edge) | WF-001 | Application Date set to yesterday |  | 1. Select a Share Product from the dropdown<br>2. Enter yesterday's date in the Application Date field<br>3. Fill all other required fields<br>4. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-023 (state_edge) | WF-002 | Rapid approval action on Pending state | Share Account is in Pending state | 1. Click Approve<br>2. Immediately click Approve again | First approval action succeeds; second approval action is blocked with a message indicating approval already in progress | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **31** (positive: 11, negative: 14, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a Fixed Deposit Account successfully | User logged in as <Role> | 1. Open the Fixed Deposit Account Creation Form<br>2. Select <valid fixed deposit product> from the Fixed Deposit Product dropdown<br>3. Enter <valid deposit amount> in the Deposit Amount field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <valid deposit period unit> from the Deposit Period Unit dropdown<br>6. Select <valid maturity instruction> from the Maturity Instructions dropdown<br>7. Click Submit | Fixed Deposit account created successfully | high |
| TC-002 | WF-002 | Create a Recurring Deposit Account successfully | User logged in as <Role> | 1. Open the Recurring Deposit Account Creation Form<br>2. Select <valid recurring deposit product> from the Recurring Deposit Product dropdown<br>3. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount field<br>4. Enter <valid deposit period> in the Deposit Period field<br>5. Select <valid deposit frequency> from the Deposit Frequency dropdown<br>6. Enter <valid expected first deposit date> in the Expected First Deposit On field<br>7. Click Submit | Recurring Deposit account created successfully | high |
| TC-003 | WF-003 | Approve a Fixed Deposit Account successfully | User logged in as <Role>, Fixed Deposit account is created | 1. Open the FD Account Detail Page<br>2. Click Approve | Fixed Deposit account approved | medium |
| TC-004 | WF-004 | Activate a Fixed Deposit Account successfully | User logged in as <Role>, Fixed Deposit account is created and approved | 1. Open the FD Account Detail Page<br>2. Click Activate | Fixed Deposit account activated | medium |
| TC-005 | WF-005 | Close a Fixed Deposit Account prematurely | User logged in as <Role>, Fixed Deposit account is activated | 1. Open the FD Account Detail Page<br>2. Click Premature Close | Fixed Deposit account closed prematurely | medium |
| TC-006 | WF-006 | Close a Fixed Deposit Account on maturity | User logged in as <Role>, Fixed Deposit account is activated | 1. Open the FD Account Detail Page<br>2. Click Close on Maturity | Fixed Deposit account closed on maturity | medium |
| TC-007 | WF-007 | Approve a Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit account is created | 1. Open the RD Account Detail Page<br>2. Click Approve | Recurring Deposit account approved | medium |
| TC-008 | WF-008 | Activate a Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit account is created and approved | 1. Open the RD Account Detail Page<br>2. Click Activate | Recurring Deposit account activated | medium |
| TC-009 | WF-009 | Deposit into a Recurring Deposit Account successfully | User logged in as <Role>, Recurring Deposit account is activated | 1. Open the RD Account Detail Page<br>2. Click Deposit | Deposit made into Recurring Deposit account | medium |
| TC-010 | WF-010 | Close a Recurring Deposit Account prematurely | User logged in as <Role>, Recurring Deposit account is activated | 1. Open the RD Account Detail Page<br>2. Click Premature Close | Recurring Deposit account closed prematurely | medium |
| TC-011 | WF-011 | Close a Recurring Deposit Account on maturity | User logged in as <Role>, Recurring Deposit account is activated | 1. Open the RD Account Detail Page<br>2. Click Close on Maturity | Recurring Deposit account closed on maturity | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Leave Fixed Deposit Product dropdown blank and submit |  | 1. Leave the Fixed Deposit Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Fixed Deposit Product field indicating it is required | high |
| TC-013 | WF-001 | Leave Deposit Amount blank and submit |  | 1. Leave the Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Amount field indicating it is required | high |
| TC-014 | WF-001 | Leave Deposit Period blank and submit |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-015 | WF-001 | Leave Deposit Period Unit dropdown blank and submit |  | 1. Leave the Deposit Period Unit dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period Unit field indicating it is required | high |
| TC-016 | WF-001 | Leave Maturity Instructions dropdown blank and submit |  | 1. Leave the Maturity Instructions dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Maturity Instructions field indicating it is required | high |
| TC-017 | WF-002 | Leave Recurring Deposit Product dropdown blank and submit |  | 1. Leave the Recurring Deposit Product dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Recurring Deposit Product field indicating it is required | high |
| TC-018 | WF-002 | Leave Mandatory Deposit Amount blank and submit |  | 1. Leave the Mandatory Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mandatory Deposit Amount field indicating it is required | high |
| TC-019 | WF-002 | Leave Deposit Period blank and submit |  | 1. Leave the Deposit Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Period field indicating it is required | high |
| TC-020 | WF-002 | Leave Deposit Frequency dropdown blank and submit |  | 1. Leave the Deposit Frequency dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Deposit Frequency field indicating it is required | high |
| TC-021 | WF-002 | Leave Expected First Deposit On date blank and submit |  | 1. Leave the Expected First Deposit On field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Expected First Deposit On field indicating it is required | high |
| TC-022 | WF-003 | Attempt to approve Fixed Deposit Account without required state |  | 1. Navigate to the Fixed Deposit Account Detail Page<br>2. Click Approve | Status remains unapproved; no transition occurs | medium |
| TC-023 | WF-004 | Attempt to activate Fixed Deposit Account without required state |  | 1. Navigate to the Fixed Deposit Account Detail Page<br>2. Click Activate | Status remains inactive; no transition occurs | medium |
| TC-024 | WF-010 | Attempt to prematurely close Recurring Deposit Account without required state |  | 1. Navigate to the Recurring Deposit Account Detail Page<br>2. Click Premature Close | Status remains open; no transition occurs | medium |
| TC-025 | WF-011 | Attempt to close Recurring Deposit Account on maturity without required state |  | 1. Navigate to the Recurring Deposit Account Detail Page<br>2. Click Close on Maturity | Status remains open; no transition occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 (boundary) | WF-001 | Test Fixed Deposit Deposit Amount at minimum boundary |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter the minimum allowed Deposit Amount in the Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select a Deposit Period Unit from the dropdown<br>5. Select Maturity Instructions from the dropdown<br>6. Click Submit | Form submits successfully; Fixed Deposit account is created with the minimum Deposit Amount | medium |
| TC-027 (boundary) | WF-001 | Test Fixed Deposit Deposit Amount just below minimum boundary |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter one unit below the minimum allowed Deposit Amount in the Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select a Deposit Period Unit from the dropdown<br>5. Select Maturity Instructions from the dropdown<br>6. Click Submit | Form submission is blocked; an error message is shown indicating the Deposit Amount is below the minimum allowed | medium |
| TC-028 (boundary) | WF-002 | Test Recurring Deposit Mandatory Deposit Amount at minimum boundary |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter the minimum allowed Mandatory Deposit Amount in the Mandatory Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select a Deposit Frequency from the dropdown<br>5. Enter a valid Expected First Deposit On date<br>6. Click Submit | Form submits successfully; Recurring Deposit account is created with the minimum Mandatory Deposit Amount | medium |
| TC-029 (boundary) | WF-002 | Test Recurring Deposit Mandatory Deposit Amount just below minimum boundary |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter one unit below the minimum allowed Mandatory Deposit Amount in the Mandatory Deposit Amount field<br>3. Enter a valid Deposit Period in the Deposit Period field<br>4. Select a Deposit Frequency from the dropdown<br>5. Enter a valid Expected First Deposit On date<br>6. Click Submit | Form submission is blocked; an error message is shown indicating the Mandatory Deposit Amount is below the minimum allowed | medium |
| TC-030 (boundary) | WF-009 | Test Deposit into Recurring Deposit Account with zero deposit |  | 1. Navigate to the Recurring Deposit Account Detail Page<br>2. Click on the Deposit action button<br>3. Enter '0' in the deposit amount field<br>4. Click Submit | Form submission is blocked; an error message is shown indicating that the deposit amount cannot be zero | medium |
| TC-031 (boundary) | WF-009 | Test Deposit into Recurring Deposit Account with valid maximum deposit amount |  | 1. Navigate to the Recurring Deposit Account Detail Page<br>2. Click on the Deposit action button<br>3. Enter the maximum allowed deposit amount in the deposit amount field<br>4. Click Submit | Form submits successfully; deposit is made into the Recurring Deposit account with the maximum allowed deposit amount | medium |

---

## Accounting — Chart of Accounts

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit GL Account details | User logged in as <Role>, At least one GL Account exists | 1. Click on the account name of an existing GL Account | GL Account details opened for editing | high |
| TC-002 | WF-002 | Delete a GL Account | User logged in as <Role>, At least one GL Account exists | 1. Click on the three-dot menu of an existing GL Account<br>2. Select 'Delete' from the options<br>3. Confirm the deletion | GL Account deleted successfully | high |
| TC-003 | WF-003 | Open Create GL Account form | User logged in as <Role> | 1. Click '+ Create GL Account' button | opens the creation form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Leave the Account Type field blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the Account Type field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-005 | WF-003 | Leave the GL Code field blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the GL Code field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the GL Code field indicating it is required | high |
| TC-006 | WF-003 | Leave the Account Name field blank and submit |  | 1. Click on '+ Create GL Account'<br>2. Leave the Account Name field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Account Name field indicating it is required | high |
| TC-007 | WF-003 | Submit with duplicate GL Code |  | 1. Click on '+ Create GL Account'<br>2. Enter <duplicate GL Code> in the GL Code field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form does not submit; GL Code is not unique; error shown on GL Code field | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-003 | Attempt to create a GL Account with a duplicate GL Code | A GL Account with the same GL Code already exists | 1. Click the '+ Create GL Account' button<br>2. Fill in all required fields with valid data<br>3. Enter the duplicate GL Code in the GL Code field<br>4. Click Submit | Form submission is blocked; an error message displays indicating the GL Code must be unique | medium |
| TC-009 (input_edge) | WF-003 | Enter a very long Account Name |  | 1. Click the '+ Create GL Account' button<br>2. Fill in all required fields with valid data<br>3. Enter a string of 200+ characters in the Account Name field<br>4. Click Submit | Form submission is blocked; an error message displays indicating the Account Name is too long | low |
| TC-010 (input_edge) | WF-003 | Enter special characters in the Description field |  | 1. Click the '+ Create GL Account' button<br>2. Fill in all required fields with valid data<br>3. Enter special characters in the Description field<br>4. Click Submit | Form submits successfully; the Description field displays the entered special characters correctly | low |
| TC-011 (input_edge) | WF-003 | Enter a GL Code with leading/trailing whitespace |  | 1. Click the '+ Create GL Account' button<br>2. Fill in all required fields with valid data<br>3. Enter a GL Code with leading and trailing spaces<br>4. Click Submit | GL Code is trimmed; saved record shows the GL Code without whitespace | low |

---

## Accounting — Journal Entries & Closures

Total: **15** (positive: 4, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Journal Entry Creation Form | User logged in as <Role> | 1. Click '+ Add Journal Entry' | The creation form is opened | high |
| TC-002 | WF-002 | Open Closure Creation Form | User logged in as <Role> | 1. Click '+ Create Closure' | The closure form is opened | high |
| TC-003 | WF-001 | Add Journal Entry with Valid Data | User logged in as <Role> | 1. Click '+ Add Journal Entry'<br>2. Enter <Office> in the Office field<br>3. Enter <Currency> in the Currency field<br>4. Enter <valid date> in the Transaction Date field<br>5. Click 'Add Row' in the Entry Lines section<br>6. Select <GL Account> from the GL Account dropdown in the new row<br>7. Enter <valid amount> in the Amount field in the new row<br>8. Click Submit | The total debits and credits are validated; the entry is added successfully. | high |
| TC-004 | WF-002 | Create Closure with Valid Data | User logged in as <Role> | 1. Click '+ Create Closure'<br>2. Enter <Office> in the Office field<br>3. Enter <valid closing date> in the Closing Date field<br>4. Click Submit | The closure is created successfully; journal entries cannot be posted for dates on or before the closing date. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Office field blank |  | 1. Click on '+ Add Journal Entry'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Office field displays an error: 'This field is required.' | high |
| TC-006 | WF-001 | Leave the Transaction Date field blank |  | 1. Click on '+ Add Journal Entry'<br>2. Fill all other required fields<br>3. Leave the Transaction Date field blank<br>4. Click Submit | Form does not submit; Transaction Date field displays an error: 'This field is required.' | high |
| TC-007 | WF-001 | Add entry lines with missing GL Account |  | 1. Click on '+ Add Journal Entry'<br>2. Fill all required fields<br>3. Click 'Add Row' without selecting a GL Account<br>4. Leave the Amount field blank<br>5. Click Submit | Form does not submit; GL Account field displays an error: 'This field is required.'; Amount field displays an error: 'This field is required.' | high |
| TC-008 | WF-001 | Total debits do not equal total credits |  | 1. Click on '+ Add Journal Entry'<br>2. Fill all required fields with valid data<br>3. Add entry lines with total debits not equal to total credits<br>4. Click Submit | Form does not submit; displays an error: 'Total debits must equal total credits.' | high |
| TC-009 | WF-002 | Leave the Office field blank in Create Closure form |  | 1. Click on '+ Create Closure'<br>2. Leave the Office field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Office field displays an error: 'This field is required.' | high |
| TC-010 | WF-002 | Leave the Closing Date field blank in Create Closure form |  | 1. Click on '+ Create Closure'<br>2. Fill all other required fields<br>3. Leave the Closing Date field blank<br>4. Click Submit | Form does not submit; Closing Date field displays an error: 'This field is required.' | high |
| TC-011 | WF-002 | Attempt to create closure with journal entries posted on or before the closing date |  | 1. Click on '+ Create Closure'<br>2. Fill in the Office and Closing Date fields with a date that has journal entries posted<br>3. Click Submit | Form does not submit; displays an error: 'Cannot create closure; journal entries exist for this date or earlier.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Total debits equal total credits exactly | User is on the Add Journal Entry Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Currency in the Currency field<br>3. Enter a valid Transaction Date in the Transaction Date field<br>4. Add 1 row to Entry Lines with a GL Account and a debit amount of 100<br>5. Add another row to Entry Lines with a GL Account and a credit amount of 100<br>6. Click Submit | Form submits successfully; journal entry is created with total debits equal to total credits. | medium |
| TC-013 (boundary) | WF-001 | Total debits exceed total credits by 1 | User is on the Add Journal Entry Form | 1. Enter a valid Office in the Office field<br>2. Enter a valid Currency in the Currency field<br>3. Enter a valid Transaction Date in the Transaction Date field<br>4. Add 1 row to Entry Lines with a GL Account and a debit amount of 100<br>5. Add another row to Entry Lines with a GL Account and a credit amount of 99<br>6. Click Submit | Submission is blocked; error message displayed indicating total debits must equal total credits. | medium |
| TC-014 (boundary) | WF-002 | Closing date equals transaction date | User is on the Create Closure Form | 1. Enter a valid Office in the Office field<br>2. Enter today's date in the Closing Date field<br>3. Click Submit | Form submits successfully; closure is created with the closing date set to today. | medium |
| TC-015 (boundary) | WF-002 | Closing date is one day before transaction date | User is on the Create Closure Form | 1. Enter a valid Office in the Office field<br>2. Enter yesterday's date in the Closing Date field<br>3. Click Submit | Submission is blocked; error message displayed indicating journal entries cannot be posted for dates on or before the closing date. | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new accounting rule | User logged in as <Role> | 1. Click '+ Create Rule' to open the creation form<br>2. Enter <valid rule name> in the Rule Name field<br>3. Select 'All Offices' from the Office dropdown<br>4. Click '+ Create Rule' to submit the form | A success notification is displayed; the new accounting rule is visible in the Accounting Rules Table | high |
| TC-002 | WF-002 | Edit an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click 'Edit' to open the edit form<br>3. Modify the Rule Name to <new valid rule name><br>4. Click 'Save' to submit the changes | A success notification is displayed; the accounting rule details are updated in the Accounting Rules Table | medium |
| TC-003 | WF-003 | Delete an existing accounting rule | User logged in as <Role>, At least one accounting rule exists | 1. Click on the Rule Name of the existing rule to open its detail view<br>2. Click 'Delete' to remove the rule<br>3. Confirm the deletion | A success notification is displayed; the accounting rule is no longer present in the Accounting Rules Table | medium |
| TC-004 | WF-004 | Create a new financial activity mapping | User logged in as <Role> | 1. Click '+ Create Mapping' to open the creation form<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select <valid GL account> from the GL Account dropdown<br>4. Click '+ Create Mapping' to submit the form | A success notification is displayed; the new financial activity mapping is visible in the Financial Activity Mappings Table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave Rule Name field blank and submit |  | 1. Open the Create Rule Form<br>2. Leave the Rule Name field blank<br>3. Click + Create Rule | Inline validation error appears on the Rule Name field indicating it is required | high |
| TC-006 | WF-004 | Leave Financial Activity field blank and submit |  | 1. Open the Create Mapping Form<br>2. Leave the Financial Activity field blank<br>3. Click + Create Mapping | Inline validation error appears on the Financial Activity field indicating it is required | high |
| TC-007 | WF-004 | Submit with duplicate Financial Activity mapping |  | 1. Open the Create Mapping Form<br>2. Select <existing financial activity> in the Financial Activity field<br>3. Select <valid GL account> in the GL Account field<br>4. Click + Create Mapping | Form does not submit; error shown indicating 'each financial activity can only be mapped once' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-004 | Create Financial Activity Mapping with duplicate financial activity | Financial Activity 'Asset Transfer' is already mapped | 1. Click '+ Create Mapping'<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select a GL Account from the GL Account dropdown<br>4. Click Submit | Form submission is blocked; error message displays 'each financial activity can only be mapped once' | medium |
| TC-009 (boundary) | WF-001 | Create Accounting Rule with empty Rule Name |  | 1. Click '+ Create Rule'<br>2. Leave the Rule Name field empty<br>3. Click Submit | Form submission is blocked; error message indicates 'Rule Name is required' | medium |
| TC-010 (input_edge) |  | Create Accounting Rule with long Rule Name |  | 1. Click '+ Create Rule'<br>2. Enter a long string of characters (200+ characters) in the Rule Name field<br>3. Click Submit | Form submission is either accepted or displays an error indicating the input exceeds the maximum allowed length | low |
| TC-011 (input_edge) |  | Create Mapping with special characters in GL Account |  | 1. Click '+ Create Mapping'<br>2. Select a Financial Activity<br>3. Enter special characters in the GL Account field<br>4. Click Submit | Form submission is either accepted or displays an error indicating invalid characters in the GL Account | low |

---

## Provisioning

Total: **21** (positive: 5, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form for new provisioning criteria | User logged in as <role> | 1. Click '+ Create' button | opens creation form | high |
| TC-002 | WF-002 | Generate new provisioning entries | User logged in as <role>, Provisioning criteria are configured | 1. Click '+ Create Provisioning Entry' button | generates new provisioning entries | high |
| TC-003 | WF-003 | Review provisioning entry details | User logged in as <role>, Provisioning entries exist | 1. Click 'Review' on a provisioning entry | shows detailed breakdown by loan product and category | medium |
| TC-004 | WF-004 | Recreate a provisioning entry | User logged in as <role>, Provisioning entries exist | 1. Click 'Recreate' on a provisioning entry | recreates the provisioning entry | medium |
| TC-005 | WF-005 | View criteria details | User logged in as <role>, Provisioning criteria exist | 1. Click on 'Criteria Name' link in the criteria table | navigates to criteria details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave the Criteria Name field blank and submit |  | 1. Click on '+ Create'<br>2. Leave the Criteria Name field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-007 | WF-001 | Submit the form with all required fields empty |  | 1. Click on '+ Create'<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Criteria Name field is highlighted; error shown on Criteria Name field | high |
| TC-008 | WF-001 | Leave the Loan Product field blank in Definitions and submit |  | 1. Click on '+ Create'<br>2. Fill the Criteria Name field with valid data<br>3. Add a row in the Definitions table<br>4. Leave the Loan Product field blank<br>5. Fill all other required fields in the Definitions row with valid data<br>6. Click Submit | Inline validation error appears on the Loan Product field indicating it is required | high |
| TC-009 | WF-001 | Leave the Category field blank in Definitions and submit |  | 1. Click on '+ Create'<br>2. Fill the Criteria Name field with valid data<br>3. Add a row in the Definitions table<br>4. Leave the Category field blank<br>5. Fill all other required fields in the Definitions row with valid data<br>6. Click Submit | Inline validation error appears on the Category field indicating it is required | high |
| TC-010 | WF-001 | Enter a negative value in Minimum Age field |  | 1. Click on '+ Create'<br>2. Fill the Criteria Name field with valid data<br>3. Add a row in the Definitions table<br>4. Enter <negative value> in the Minimum Age field<br>5. Fill all other required fields in the Definitions row with valid data<br>6. Click Submit | Inline validation error appears on the Minimum Age field indicating it must be a positive number | medium |
| TC-011 | WF-001 | Enter a value in Maximum Age field less than Minimum Age |  | 1. Click on '+ Create'<br>2. Fill the Criteria Name field with valid data<br>3. Add a row in the Definitions table<br>4. Enter <value> in the Minimum Age field<br>5. Enter <value less than Minimum Age> in the Maximum Age field<br>6. Fill all other required fields in the Definitions row with valid data<br>7. Click Submit | Inline validation error appears on the Maximum Age field indicating it must be greater than Minimum Age | medium |
| TC-012 | WF-001 | Leave the Provisioning Percentage field blank in Definitions and submit |  | 1. Click on '+ Create'<br>2. Fill the Criteria Name field with valid data<br>3. Add a row in the Definitions table<br>4. Leave the Provisioning Percentage field blank<br>5. Fill all other required fields in the Definitions row with valid data<br>6. Click Submit | Inline validation error appears on the Provisioning Percentage field indicating it is required | high |
| TC-013 | WF-002 | Attempt to create provisioning entry without valid criteria |  | 1. Click on '+ Create Provisioning Entry'<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; error shown on all required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Minimum Age at threshold | User is on the Create Criteria Form | 1. Enter a value of 1 in the Minimum Age field<br>2. Fill all other required fields<br>3. Click + Create | Form submits successfully; entity is created with Minimum Age set to 1 | medium |
| TC-015 (boundary) | WF-001 | Maximum Age just above threshold | User is on the Create Criteria Form | 1. Enter a value of 1 in the Maximum Age field<br>2. Fill all other required fields<br>3. Click + Create | Form submits successfully; entity is created with Maximum Age set to 1 | medium |
| TC-016 (boundary) | WF-001 | Provisioning Percentage at threshold | User is on the Create Criteria Form | 1. Enter a value of 0 in the Provisioning Percentage field<br>2. Fill all other required fields<br>3. Click + Create | Form submits successfully; entity is created with Provisioning Percentage set to 0 | medium |
| TC-017 (boundary) | WF-001 | Adding maximum allowed entries to Definitions | User is on the Create Criteria Form | 1. Add 1 row to the Definitions table<br>2. Fill all required fields in that row<br>3. Click + Create | Form submits successfully; entity is created with 1 entry in Definitions | medium |
| TC-018 (boundary) | WF-001 | Exceeding maximum allowed entries in Definitions | User is on the Create Criteria Form | 1. Add 2 rows to the Definitions table<br>2. Fill all required fields in both rows<br>3. Click + Create | Form is blocked; a visible error indicates that only 1 entry is allowed | medium |
| TC-019 (input_edge) |  | Long text in Criteria Name | User is on the Create Criteria Form | 1. Enter a string of 200+ characters in the Criteria Name field<br>2. Fill all other required fields<br>3. Click + Create | Form submits successfully; Criteria Name is saved as entered | low |
| TC-020 (input_edge) |  | Special characters in Criteria Name | User is on the Create Criteria Form | 1. Enter special characters in the Criteria Name field<br>2. Fill all other required fields<br>3. Click + Create | Form submits successfully; Criteria Name is saved as entered | low |
| TC-021 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully created a criteria | 1. Press the browser back button after submission<br>2. Observe the form state | Creation form is shown blank (not pre-filled) | low |

---

## Offices

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open the Create Office form | User logged in as <Role> | 1. Click the '+ Create Office' button | The creation form opens | high |
| TC-002 | WF-001 | Create a new office with valid details | User logged in as <Role>, The creation form is open | 1. Enter <valid office name> in the Office Name field<br>2. Select <valid parent office> in the Parent Office dropdown<br>3. Enter <valid opening date> in the Opened On Date field<br>4. Enter <optional external ID> in the External ID field<br>5. Click Submit | The new office is created and displayed in the offices table | high |
| TC-003 | WF-002 | Edit an office's details | User logged in as <Role>, An office exists in the offices table | 1. Click the Office Name link of the office to edit<br>2. Click the Edit button<br>3. Modify <field> with <new value><br>4. Click Submit | Office information updated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Office Name field blank and submit |  | 1. Click on the '+ Create Office' button<br>2. Leave the Office Name field blank<br>3. Fill in the Parent Office field with a valid value<br>4. Fill in the Opened On Date field with a valid date<br>5. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Parent Office field blank and submit |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name field with a valid value<br>3. Leave the Parent Office field blank<br>4. Fill in the Opened On Date field with a valid date<br>5. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-006 | WF-001 | Leave the Opened On Date field blank and submit |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name field with a valid value<br>3. Fill in the Parent Office field with a valid value<br>4. Leave the Opened On Date field blank<br>5. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Click on the '+ Create Office' button<br>2. Leave the Office Name field blank<br>3. Leave the Parent Office field blank<br>4. Leave the Opened On Date field blank<br>5. Click Submit | Form does not submit; Office Name, Parent Office, and Opened On Date fields display errors indicating they are required | high |
| TC-008 | WF-001 | Submit with Parent Office not being Head Office when root |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name field with a valid value<br>3. Fill in the Parent Office field with a non-Head Office value<br>4. Fill in the Opened On Date field with a valid date<br>5. Click Submit | Inline validation error appears on the Parent Office field indicating it must be Head Office if root | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Open a new office with a valid opening date |  | 1. Click on the '+ Create Office' button<br>2. Enter today's date in the 'Opened On Date' field<br>3. Fill in 'Office Name' and 'Parent Office' with valid values<br>4. Click Submit | Form submits successfully; office is created with today's date as the opening date | medium |
| TC-010 (boundary) | WF-001 | Open a new office with an opening date in the past |  | 1. Click on the '+ Create Office' button<br>2. Enter a date one day before today in the 'Opened On Date' field<br>3. Fill in 'Office Name' and 'Parent Office' with valid values<br>4. Click Submit | Form submits successfully; office is created with the past date as the opening date | medium |
| TC-011 (boundary) | WF-001 | Open a new office with an invalid opening date |  | 1. Click on the '+ Create Office' button<br>2. Enter a date in the future in the 'Opened On Date' field<br>3. Fill in 'Office Name' and 'Parent Office' with valid values<br>4. Click Submit | Form is blocked; an error message indicates that the opening date cannot be in the future | medium |
| TC-012 (input_edge) | WF-001 | Enter a very long office name |  | 1. Click on the '+ Create Office' button<br>2. Enter a string of 200+ characters in the 'Office Name' field<br>3. Fill in 'Parent Office' with a valid value<br>4. Enter today's date in the 'Opened On Date' field<br>5. Click Submit | Form submits successfully; the office name is saved correctly in the detail page | low |
| TC-013 (input_edge) | WF-001 | Enter special characters in the office name |  | 1. Click on the '+ Create Office' button<br>2. Enter special characters in the 'Office Name' field<br>3. Fill in 'Parent Office' with a valid value<br>4. Enter today's date in the 'Opened On Date' field<br>5. Click Submit | Form submits successfully; the office name is saved correctly in the detail page | low |

---

## Employees

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View employee details | User logged in as <Role>, Employee is listed in the Employees table | 1. Click on the Name link of the employee | Employee details displayed | high |
| TC-002 | WF-002 | Edit employee details | User logged in as <Role>, Employee is listed in the Employees table | 1. Click on the Edit action for the employee | Employee edit form opened | high |
| TC-003 | WF-003 | Create a new employee | User logged in as <Role> | 1. Click the + Create Employee button<br>2. Enter <Office> in the Office field<br>3. Enter <First Name> in the First Name field<br>4. Enter <Last Name> in the Last Name field<br>5. Click Submit | opens creation form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Leave the Office field blank and submit the form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Fill in First Name and Last Name with valid values<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-005 | WF-003 | Leave the First Name field blank and submit the form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the First Name field blank<br>3. Fill in Office and Last Name with valid values<br>4. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-006 | WF-003 | Leave the Last Name field blank and submit the form |  | 1. Click on the '+ Create Employee' button<br>2. Leave the Last Name field blank<br>3. Fill in Office and First Name with valid values<br>4. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-007 |  | Attempt to view employee details without proper authentication |  | 1. Attempt to access the employee details page without logging in | User is redirected to the login page | high |
| TC-008 |  | Attempt to edit employee details without proper authentication |  | 1. Attempt to access the edit employee details page without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-003 | Submit the creation form with today's date in Joining Date field |  | 1. Click on the '+ Create Employee' button<br>2. Enter a valid Office<br>3. Enter a valid First Name<br>4. Enter a valid Last Name<br>5. Enter today's date in the Joining Date field<br>6. Click Submit | Form submits successfully; employee is created with today's date in the Joining Date field | medium |
| TC-010 (boundary) | WF-003 | Submit the creation form with a Joining Date that is one day in the past |  | 1. Click on the '+ Create Employee' button<br>2. Enter a valid Office<br>3. Enter a valid First Name<br>4. Enter a valid Last Name<br>5. Enter a date that is one day before today in the Joining Date field<br>6. Click Submit | Form submits successfully; employee is created with the past date in the Joining Date field | medium |
| TC-011 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Click on the '+ Create Employee' button<br>2. Enter a valid Office<br>3. Enter a long string (200+ characters) in the First Name field<br>4. Enter a valid Last Name<br>5. Click Submit | Form submission is blocked; an error message indicates the First Name exceeds the maximum length | low |
| TC-012 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Click on the '+ Create Employee' button<br>2. Enter a valid Office<br>3. Enter a valid First Name<br>4. Enter special characters in the Last Name field<br>5. Click Submit | Form submission is blocked; an error message indicates the Last Name contains invalid characters | low |

---

## Teller & Cashier Management

Total: **21** (positive: 6, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open creation form for a new Teller | User logged in as <Role> | 1. Click '+ Create Teller' | Creation form opens | high |
| TC-002 | WF-002 | View details of a Teller | User logged in as <Role> | 1. Click on the Teller Name link | Teller detail view opens | high |
| TC-003 | WF-003 | Open edit form for a Teller | User logged in as <Role> | 1. Click 'Edit' on the Teller Detail page | Edit form opens | medium |
| TC-004 | WF-004 | Open allocation form for a new Cashier | User logged in as <Role>, Teller Detail page is open | 1. Click '+ Allocate Cashier' | Allocation form opens | high |
| TC-005 | WF-005 | Add cash from the vault | User logged in as <Role>, Cashier Detail page is open | 1. Click 'Allocate Cash' | Cash is added from the vault | medium |
| TC-006 | WF-006 | Return cash to the vault | User logged in as <Role>, Cashier Detail page is open | 1. Click 'Settle Cash' | Cash is returned to the vault | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Leave the Office field blank and submit the Create Teller form |  | 1. Click on '+ Create Teller'<br>2. Leave the Office field blank<br>3. Fill in the Teller Name, Start Date, and all other fields<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-008 | WF-001 | Leave the Teller Name field blank and submit the Create Teller form |  | 1. Click on '+ Create Teller'<br>2. Fill in the Office, Start Date, and all other fields<br>3. Leave the Teller Name field blank<br>4. Click Submit | Inline validation error appears on the Teller Name field indicating it is required | high |
| TC-009 | WF-001 | Leave the Start Date field blank and submit the Create Teller form |  | 1. Click on '+ Create Teller'<br>2. Fill in the Office, Teller Name, and all other fields<br>3. Leave the Start Date field blank<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 | WF-004 | Leave the Staff field blank and submit the Allocate Cashier form |  | 1. Click on '+ Allocate Cashier'<br>2. Leave the Staff field blank<br>3. Fill in the Start Date and all other fields<br>4. Click Submit | Inline validation error appears on the Staff field indicating it is required | high |
| TC-011 | WF-004 | Leave the Start Date field blank and submit the Allocate Cashier form |  | 1. Click on '+ Allocate Cashier'<br>2. Fill in the Staff and all other fields<br>3. Leave the Start Date field blank<br>4. Click Submit | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-012 | WF-006 | Leave the Amount field blank and submit the Settle Cash form |  | 1. Click on 'Settle Cash'<br>2. Leave the Amount field blank<br>3. Fill in the Currency and Transaction Date fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-013 | WF-006 | Leave the Currency field blank and submit the Settle Cash form |  | 1. Click on 'Settle Cash'<br>2. Fill in the Amount and Transaction Date fields<br>3. Leave the Currency field blank<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-014 | WF-006 | Leave the Transaction Date field blank and submit the Settle Cash form |  | 1. Click on 'Settle Cash'<br>2. Fill in the Amount and Currency fields<br>3. Leave the Transaction Date field blank<br>4. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-001 | Create Teller with valid Start Date |  | 1. Click + Create Teller<br>2. Fill in the Office field with a valid entry<br>3. Enter a valid Teller Name<br>4. Enter a valid Start Date (today's date)<br>5. Click Submit | Form submits successfully; teller is created with today's date as Start Date | medium |
| TC-016 (boundary) | WF-001 | Create Teller with End Date before Start Date |  | 1. Click + Create Teller<br>2. Fill in the Office field with a valid entry<br>3. Enter a valid Teller Name<br>4. Enter a valid Start Date (tomorrow's date)<br>5. Enter an End Date (today's date)<br>6. Click Submit | Form submission is blocked; error shown indicating End Date must be after Start Date | medium |
| TC-017 (boundary) | WF-004 | Allocate Cashier with valid Start Date |  | 1. Click + Allocate Cashier<br>2. Fill in the Staff field with a valid entry<br>3. Enter a valid Start Date (today's date)<br>4. Click Submit | Form submits successfully; cashier is allocated with today's date as Start Date | medium |
| TC-018 (boundary) | WF-006 | Settle Cash with valid Transaction Date |  | 1. Click Settle Cash<br>2. Enter a valid Amount<br>3. Enter a valid Currency<br>4. Enter Transaction Date (today's date)<br>5. Click Submit | Cash is settled successfully with today's date as Transaction Date | medium |
| TC-019 (boundary) | WF-006 | Settle Cash with Transaction Date in the future |  | 1. Click Settle Cash<br>2. Enter a valid Amount<br>3. Enter a valid Currency<br>4. Enter Transaction Date (a future date)<br>5. Click Submit | Form submission is blocked; error shown indicating Transaction Date must not be in the future | medium |
| TC-020 (input_edge) |  | Enter long text in Description field |  | 1. Click + Create Teller<br>2. Fill in the Office field with a valid entry<br>3. Enter a valid Teller Name<br>4. Enter a long string (200+ characters) in the Description field<br>5. Enter a valid Start Date (today's date)<br>6. Click Submit | Form submits successfully; description is saved correctly without truncation | low |
| TC-021 (input_edge) |  | Enter special characters in Teller Name |  | 1. Click + Create Teller<br>2. Fill in the Office field with a valid entry<br>3. Enter special characters in the Teller Name field<br>4. Enter a valid Start Date (today's date)<br>5. Click Submit | Form submission is blocked; error shown indicating invalid characters in Teller Name | low |

---

## Users & Roles

Total: **20** (positive: 5, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new user with all required fields filled | User logged in as <Role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <same valid password> in the Repeat Password field<br>9. Click Submit | User created successfully | high |
| TC-002 | WF-002 | Create a new user with staff linked | User logged in as <Role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Select <staff> from the Staff dropdown<br>8. Enter <valid password> in the Password field<br>9. Enter <same valid password> in the Repeat Password field<br>10. Click Submit | User created successfully | high |
| TC-003 | WF-003 | View user details from the users table | User logged in as <Role> | 1. Click on the Username link of an existing user | User details displayed | medium |
| TC-004 | WF-004 | Create a new role with a name | User logged in as <Role> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Click Submit | Role created successfully | high |
| TC-005 | WF-005 | Manage permissions for a role | User logged in as <Role>, Role exists | 1. Navigate to the Permissions page for the role<br>2. Check 'Manage Users' permission<br>3. Click Save Permissions | Permissions updated successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it is required | high |
| TC-007 | WF-001 | Leave First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-008 | WF-001 | Leave Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-009 | WF-001 | Leave Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-010 | WF-001 | Leave Office field blank |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 | WF-001 | Enter invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email format | medium |
| TC-012 | WF-001 | Leave Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-013 | WF-001 | Enter mismatched passwords |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Repeat Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Repeat Password field indicating it must match Password | medium |
| TC-014 | WF-001 | Submit with duplicate Username |  | 1. Enter <duplicate username> in the Username field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Username field indicating it must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-001 | Username must be unique | User with the same Username already exists | 1. Enter the existing Username in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown: 'Username must be unique' | medium |
| TC-016 (boundary) | WF-001 | Email must be valid format |  | 1. Enter an invalid email format in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown: 'Email must be valid email format' | medium |
| TC-017 (boundary) | WF-001 | Password must meet password policy |  | 1. Enter a password that does not meet the password policy in the Password field<br>2. Enter the same password in the Repeat Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form submission is blocked; error shown: 'Password must meet password policy' | medium |
| TC-018 (boundary) | WF-001 | Repeat Password must match Password |  | 1. Enter a valid password in the Password field<br>2. Enter a different password in the Repeat Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form submission is blocked; error shown: 'Repeat Password must match Password' | medium |
| TC-019 (input_edge) |  | Enter long text in Username field |  | 1. Enter a very long string (200+ characters) in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating the Username is too long or accepted with truncation visible | low |
| TC-020 (input_edge) |  | Enter special characters in First Name field |  | 1. Enter special characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating invalid characters or accepted with the value saved | low |

---

## Reports

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Report with Parameters Form | User logged in as <role> | 1. Click on the report 'Loans Awaiting Disbursal' | Parameters form displayed for report selection | high |
| TC-002 | WF-002 | Run Report - View on Screen | User logged in as <role>, Parameters form displayed for report selection | 1. Fill in the parameters as needed<br>2. Click 'Run Report'<br>3. Click 'View on Screen' | generates report as data table | high |
| TC-003 | WF-003 | Run Report - Export to Excel | User logged in as <role>, Parameters form displayed for report selection | 1. Fill in the parameters as needed<br>2. Click 'Run Report'<br>3. Click 'Export to Excel' | generates report as data table | high |
| TC-004 | WF-004 | Run Report - Export to CSV | User logged in as <role>, Parameters form displayed for report selection | 1. Fill in the parameters as needed<br>2. Click 'Run Report'<br>3. Click 'Export to CSV' | generates report as data table | high |
| TC-005 | WF-005 | Run Report - Export to PDF | User logged in as <role>, Parameters form displayed for report selection | 1. Fill in the parameters as needed<br>2. Click 'Run Report'<br>3. Click 'Export to PDF' | generates report as data table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to open report parameters form |  | 1. Click on a report link | Parameters form is displayed with all fields empty; no validation errors shown | medium |
| TC-007 | WF-002 | Attempt to run report without parameters |  | 1. Click on a report link<br>2. Leave all parameters empty<br>3. Click 'View on Screen' | Form does not submit; report is not generated; no errors shown | high |
| TC-008 | WF-003 | Attempt to run report without parameters for Excel export |  | 1. Click on a report link<br>2. Leave all parameters empty<br>3. Click 'Export to Excel' | Form does not submit; report is not generated; no errors shown | high |
| TC-009 | WF-004 | Attempt to run report without parameters for CSV export |  | 1. Click on a report link<br>2. Leave all parameters empty<br>3. Click 'Export to CSV' | Form does not submit; report is not generated; no errors shown | high |
| TC-010 | WF-005 | Attempt to run report without parameters for PDF export |  | 1. Click on a report link<br>2. Leave all parameters empty<br>3. Click 'Export to PDF' | Form does not submit; report is not generated; no errors shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Open Report with all parameters filled with maximum length text |  | 1. Click on a report link to open the Parameters Form<br>2. Enter a very long string (200+ characters) in the Office field<br>3. Enter a very long string (200+ characters) in the Branch field<br>4. Enter a very long string (200+ characters) in the Currency field<br>5. Enter a very long string (200+ characters) in the Loan Product field<br>6. Enter a very long string (200+ characters) in the Loan Officer field<br>7. Select an option from the Fund dropdown<br>8. Click Run Report | Report is generated successfully; visible confirmation of report generation appears | medium |
| TC-012 (input_edge) | WF-002 | Run report with leading and trailing whitespace in parameters |  | 1. Click on a report link to open the Parameters Form<br>2. Enter '   OfficeName   ' in the Office field<br>3. Enter '   BranchName   ' in the Branch field<br>4. Select an option from the Fund dropdown<br>5. Click Run Report | Leading/trailing whitespace is trimmed; report is generated with 'OfficeName' and 'BranchName' | low |
| TC-013 (input_edge) | WF-003 | Run report with special characters in parameters |  | 1. Click on a report link to open the Parameters Form<br>2. Enter '@#$%^&*()' in the Office field<br>3. Enter '@#$%^&*()' in the Branch field<br>4. Select an option from the Fund dropdown<br>5. Click Run Report | Report is generated successfully; visible confirmation of report generation appears | low |
| TC-014 (input_edge) | WF-004 | Run report with zero as a parameter value |  | 1. Click on a report link to open the Parameters Form<br>2. Enter '0' in the Loan Product field<br>3. Select an option from the Fund dropdown<br>4. Click Run Report | Report is generated successfully; visible confirmation of report generation appears | low |

---

## Account Transfers & Standing Instructions

Total: **15** (positive: 5, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient for the transfer | 1. Enter <valid From Office> in the From Office field<br>2. Enter <valid From Client> in the From Client field<br>3. Select 'Savings Account' from the From Account Type dropdown<br>4. Enter <valid From Account> in the From Account field<br>5. Enter <valid To Office> in the To Office field<br>6. Enter <valid To Client> in the To Client field<br>7. Select 'Loan Account' from the To Account Type dropdown<br>8. Enter <valid To Account> in the To Account field<br>9. Enter <valid Transfer Amount> in the Transfer Amount field<br>10. Enter <valid Transfer Date> in the Transfer Date field<br>11. Enter <optional Description> in the Description field<br>12. Click Submit | processes the transfer, debiting the source and crediting the destination | high |
| TC-002 | WF-005 | Create a standing instruction successfully | User logged in as <Role> | 1. Click '+ Create Standing Instruction'<br>2. Enter <valid Name> in the Name field<br>3. Enter <valid From Account> in the From Account field<br>4. Enter <valid To Account> in the To Account field<br>5. Select <valid Transfer Type> in the Transfer Type field<br>6. Enter <valid Priority> in the Priority field<br>7. Select 'Fixed' from the Instruction Type dropdown<br>8. Enter <valid Amount> in the Amount field<br>9. Enter <valid Validity From> in the Validity From field<br>10. Enter <valid Validity Till> in the Validity Till field<br>11. Select 'Periodic' from the Recurrence Type dropdown<br>12. Enter <valid Recurrence Frequency> in the Recurrence Frequency field<br>13. Enter <valid Recurrence Interval> in the Recurrence Interval field<br>14. Click Create | creates standing instruction | high |
| TC-003 | WF-002 | Enable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Enable on the first standing instruction in the table | Standing instruction enabled | medium |
| TC-004 | WF-003 | Disable a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Disable on the first standing instruction in the table | Standing instruction disabled | medium |
| TC-005 | WF-004 | Delete a standing instruction | User logged in as <Role>, At least one standing instruction exists | 1. Click Delete on the first standing instruction in the table<br>2. Confirm deletion | Standing instruction deleted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to submit account transfer with transfer amount exceeding available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Enter <valid date> in the Transfer Date field<br>3. Click Submit | Form does not submit; error shown on Transfer Amount field indicating 'Transfer amount must not exceed available balance' | high |
| TC-007 | WF-001 | Attempt to submit account transfer with blank transfer date |  | 1. Enter <valid amount> in the Transfer Amount field<br>2. Leave the Transfer Date field blank<br>3. Click Submit | Form does not submit; inline validation error appears on the Transfer Date field indicating it is required | high |
| TC-008 | WF-005 | Attempt to create standing instruction with blank name field |  | 1. Leave the Name field blank<br>2. Click Create | Form does not submit; inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-002 | Attempt to enable standing instruction when it is already enabled |  | 1. Select an already enabled standing instruction<br>2. Click Enable | No action occurs; standing instruction remains enabled | medium |
| TC-010 | WF-003 | Attempt to disable standing instruction when it is already disabled |  | 1. Select an already disabled standing instruction<br>2. Click Disable | No action occurs; standing instruction remains disabled | medium |
| TC-011 | WF-004 | Attempt to delete standing instruction when it is already deleted |  | 1. Select an already deleted standing instruction<br>2. Click Delete | No action occurs; standing instruction remains deleted | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Transfer Amount exactly equals available balance | User has an available balance equal to the transfer amount | 1. Fill the From Account field with a valid account<br>2. Fill the To Account field with a valid account<br>3. Enter the Transfer Amount equal to the available balance<br>4. Enter a valid Transfer Date<br>5. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-013 (boundary) | WF-001 | Transfer Amount exceeds available balance by one unit | User has an available balance | 1. Fill the From Account field with a valid account<br>2. Fill the To Account field with a valid account<br>3. Enter the Transfer Amount greater than the available balance by one unit<br>4. Enter a valid Transfer Date<br>5. Click Submit | Error is shown indicating the transfer amount exceeds the available balance | medium |
| TC-014 (boundary) | WF-005 | Validity From date equals Validity Till date | User is on the Create Standing Instruction Form | 1. Fill in the Name field with a valid name<br>2. Enter a Validity From date<br>3. Enter the same date in Validity Till<br>4. Click Create | Standing instruction is created successfully with the same Validity From and Till date | medium |
| TC-015 (boundary) | WF-005 | Validity From date is one day before Validity Till date | User is on the Create Standing Instruction Form | 1. Fill in the Name field with a valid name<br>2. Enter a Validity From date<br>3. Enter a Validity Till date that is one day after Validity From<br>4. Click Create | Standing instruction is created successfully with Validity From and Till dates correctly set | medium |

---

## Tax Management

Total: **16** (positive: 4, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new tax component successfully | User logged in as <Role> | 1. Click '+ Create Tax Component'<br>2. Enter <valid name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Select 'Income' from the Credit Account Type dropdown<br>6. Enter <valid date> in the Start Date field<br>7. Click '+ Create Tax Component' to submit the form | A success notification is displayed; the Tax Components Table shows the new tax component with the entered Name and Percentage | high |
| TC-002 | WF-002 | View tax component details | User logged in as <Role>, At least one tax component exists | 1. Click the Name link of the tax component in the Tax Components Table | Tax component details displayed | medium |
| TC-003 | WF-003 | Create a new tax group successfully | User logged in as <Role> | 1. Click '+ Create Tax Group'<br>2. Enter <valid name> in the Name field<br>3. Click 'Add Tax Component'<br>4. Enter <valid start date> in the Start Date field for the new component<br>5. Click '+ Create Tax Group' to submit the form | A success notification is displayed; the Tax Groups Table shows the new tax group with the entered Name | high |
| TC-004 | WF-004 | View tax group details | User logged in as <Role>, At least one tax group exists | 1. Click the Name link of the tax group in the Tax Groups Table | Tax group details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Name field blank and submit |  | 1. Leave the Name field blank<br>2. Fill Percentage with a valid value<br>3. Select a Debit Account Type<br>4. Fill Debit Account with a valid value<br>5. Select a Credit Account Type<br>6. Fill Credit Account with a valid value<br>7. Fill Start Date with a valid date<br>8. Click + Create Tax Component | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 | WF-001 | Leave the Percentage field blank and submit |  | 1. Fill Name with a valid value<br>2. Leave the Percentage field blank<br>3. Select a Debit Account Type<br>4. Fill Debit Account with a valid value<br>5. Select a Credit Account Type<br>6. Fill Credit Account with a valid value<br>7. Fill Start Date with a valid date<br>8. Click + Create Tax Component | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-007 | WF-001 | Leave the Start Date field blank and submit |  | 1. Fill Name with a valid value<br>2. Fill Percentage with a valid value<br>3. Select a Debit Account Type<br>4. Fill Debit Account with a valid value<br>5. Select a Credit Account Type<br>6. Fill Credit Account with a valid value<br>7. Leave the Start Date field blank<br>8. Click + Create Tax Component | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-008 | WF-003 | Leave the Name field blank and submit in Create Tax Group Form |  | 1. Leave the Name field blank<br>2. Click + Create Tax Group | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-003 | Submit Create Tax Group Form with all fields empty |  | 1. Leave the Name field blank<br>2. Click + Create Tax Group | Inline validation error appears on the Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Create Tax Component with minimum Percentage value |  | 1. Open the Create Tax Component form<br>2. Enter minimum allowed value in the Percentage field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; tax component is created with the minimum Percentage value | medium |
| TC-011 (boundary) | WF-001 | Create Tax Component with invalid Percentage value |  | 1. Open the Create Tax Component form<br>2. Enter one unit below minimum allowed value in the Percentage field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submission is blocked; error shown indicating the Percentage is below the minimum allowed | medium |
| TC-012 (boundary) | WF-001 | Create Tax Component with valid Start_Date |  | 1. Open the Create Tax Component form<br>2. Set Start_Date to today's date<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; tax component is created with today's Start_Date | medium |
| TC-013 (boundary) | WF-001 | Create Tax Group with maximum Tax Components |  | 1. Open the Create Tax Group form<br>2. Add maximum allowed Tax Components to the Tax Components section<br>3. Fill all required fields<br>4. Click + Create Tax Group | Form submits successfully; tax group is created with maximum Tax Components | medium |
| TC-014 (boundary) | WF-001 | Create Tax Group exceeding maximum Tax Components |  | 1. Open the Create Tax Group form<br>2. Add maximum allowed Tax Components + 1 to the Tax Components section<br>3. Fill all required fields<br>4. Click + Create Tax Group | Form submission is blocked; error shown indicating the maximum number of Tax Components has been exceeded | medium |
| TC-015 (input_edge) | WF-001 | Create Tax Component with long Name |  | 1. Open the Create Tax Component form<br>2. Enter a very long string (200+ characters) in the Name field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; Name field displays the long string correctly | low |
| TC-016 (input_edge) | WF-001 | Create Tax Component with special characters in Name |  | 1. Open the Create Tax Component form<br>2. Enter special characters in the Name field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; Name field accepts special characters | low |

---

## Organization Settings

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Holiday Creation Form | User logged in as <Role> | 1. Click '+ Create Holiday' button | opens the holiday creation form | high |
| TC-002 | WF-002 | Open Fund Creation Form | User logged in as <Role> | 1. Click 'Create Fund' button | opens the fund creation form | high |
| TC-003 | WF-003 | Add New Payment Type | User logged in as <Role> | 1. Click '+ Create' button | adds new payment type | high |
| TC-004 | WF-004 | Download Bulk Import Template | User logged in as <Role> | 1. Click 'Download_Template' button | downloads template | high |
| TC-005 | WF-005 | Upload Bulk Import Data | User logged in as <Role> | 1. Click 'Upload_Interface' button<br>2. Select a <valid file> to upload | data imported successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Leave the Name field blank while creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill in valid From Date and To Date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-007 | WF-001 | Leave all required fields blank while creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Leave the From Date field blank<br>4. Leave the To Date field blank<br>5. Click Submit | Form does not submit; Holiday is not created; inline validation errors appear on the Name, From Date, and To Date fields indicating they are required | high |
| TC-008 | WF-001 | Enter an invalid date format in the From Date field |  | 1. Click on '+ Create Holiday'<br>2. Enter <invalid date format> in the From Date field<br>3. Fill in valid Name and To Date<br>4. Click Submit | Inline validation error appears on the From Date field indicating it must be a valid date | medium |
| TC-009 | WF-001 | Enter a To Date that is before the From Date |  | 1. Click on '+ Create Holiday'<br>2. Enter a valid Name in the Name field<br>3. Enter <future date> in the From Date field<br>4. Enter <past date> in the To Date field<br>5. Click Submit | Inline validation error appears indicating 'To Date must be after From Date' | medium |
| TC-010 | WF-005 | Leave the Upload Interface blank while uploading bulk import data |  | 1. Click on 'Upload_Interface'<br>2. Leave the Upload Interface blank<br>3. Click Submit | Inline validation error appears on the Upload Interface field indicating it is required | high |
| TC-011 | WF-005 | Attempt to upload a file that exceeds the allowed size limit |  | 1. Click on 'Upload_Interface'<br>2. Upload a file that exceeds the maximum size limit<br>3. Click Submit | Inline validation error appears indicating 'File size exceeds the maximum limit' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Create Holiday with From_Date equal to To_Date |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field | Form submits successfully; holiday is created with From_Date equal to To_Date | medium |
| TC-013 (boundary) | WF-001 | Create Holiday with To_Date before From_Date |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter tomorrow's date in the From_Date field<br>4. Enter today's date in the To_Date field | Form submission is blocked; error displayed indicating To_Date cannot be before From_Date | medium |
| TC-014 (boundary) | WF-005 | Upload Bulk Import Data with file at exact size limit |  | 1. Click Upload_Interface<br>2. Select a file exactly at the size limit for upload | File upload succeeds; success message displayed | medium |
| TC-015 (boundary) | WF-005 | Upload Bulk Import Data with file over size limit |  | 1. Click Upload_Interface<br>2. Select a file one byte over the size limit for upload | File upload is blocked; error displayed indicating file exceeds size limit | medium |
| TC-016 (input_edge) |  | Enter long text in Name field |  | 1. Click + Create Holiday<br>2. Enter a string longer than 200 characters in the Name field | Form submission is blocked; error displayed indicating Name exceeds maximum length | low |
| TC-017 (input_edge) |  | Enter special characters in Description field |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Enter special characters in the Description field | Form submits successfully; holiday is created with special characters in Description | low |

---

## System Administration

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Toggle Start/Stop Scheduler | User logged in as <Role> | 1. Toggle the Start/Stop Scheduler checkbox | Scheduler state updated | high |
| TC-002 | WF-002 | Open Code Values | User logged in as <Role> | 1. Click on the Open_Code_Values action for a code | Code values displayed for editing | medium |
| TC-003 | WF-003 | Create a new Data Table | User logged in as <Role> | 1. Navigate to Manage Data Tables<br>2. Enter <Data Table Name> in the Data Table Name field<br>3. Select <Application Table Name> from the dropdown<br>4. Check the Multi Row checkbox<br>5. Click 'Add Row' in Column Definitions<br>6. Enter <Column Name> in the new row's Name field<br>7. Select <Type> from the Type dropdown<br>8. Enter <Length> in the Length field<br>9. Check the Is Mandatory checkbox<br>10. Check the Is Unique checkbox<br>11. Click Submit | Data table created successfully | high |
| TC-004 | WF-004 | Approve an Audit Trail entry | User logged in as <Role>, maker-checker is enabled | 1. Click Approve on a pending Audit Trail entry | Audit trail approved | high |
| TC-005 | WF-005 | Reject an Audit Trail entry | User logged in as <Role>, maker-checker is enabled | 1. Click Reject on a pending Audit Trail entry | Audit trail rejected | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Data Table Name field blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Leave the Data Table Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Data Table Name field displays an error: 'This field is required' | high |
| TC-007 |  | Leave the Application Table Name dropdown unselected and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Leave the Application Table Name dropdown unselected<br>3. Fill all other required fields<br>4. Click Submit | Form does not submit; Application Table Name field displays an error: 'This field is required' | high |
| TC-008 |  | Leave the Name field in Column Definitions blank and submit |  | 1. Navigate to the Manage Data Tables page<br>2. Fill all required fields except for the Name field in Column Definitions<br>3. Click Submit | Form does not submit; Name field displays an error: 'This field is required' | high |
| TC-009 |  | Attempt to approve an audit trail when maker-checker is not enabled |  | 1. Navigate to the Audit Trails page<br>2. Attempt to click Approve on a pending audit trail | Action is blocked; Approve button is not visible | high |
| TC-010 |  | Attempt to reject an audit trail when maker-checker is not enabled |  | 1. Navigate to the Audit Trails page<br>2. Attempt to click Reject on a pending audit trail | Action is blocked; Reject button is not visible | high |
| TC-011 | WF-001 | Attempt to toggle Start/Stop Scheduler when no jobs are scheduled |  | 1. Navigate to the Manage Scheduler Jobs page<br>2. Click the Start/Stop Scheduler toggle | Action is blocked; Scheduler state remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Toggle Start/Stop Scheduler with active jobs | At least one job is active | 1. Click the Start/Stop Scheduler toggle | Scheduler state updated; all active jobs are now stopped | medium |
| TC-013 (boundary) | WF-001 | Toggle Start/Stop Scheduler with no active jobs | No jobs are active | 1. Click the Start/Stop Scheduler toggle | Scheduler state updated; no jobs to stop | medium |
| TC-014 (boundary) | WF-003 | Create Data Table with maximum column definitions | No existing data tables | 1. Enter a valid Data Table Name<br>2. Select an Application Table Name<br>3. Check the Multi Row checkbox<br>4. Add maximum allowed column definitions<br>5. Click Submit | Data table created successfully with maximum column definitions | medium |
| TC-015 (boundary) | WF-003 | Create Data Table exceeding maximum column definitions | No existing data tables | 1. Enter a valid Data Table Name<br>2. Select an Application Table Name<br>3. Check the Multi Row checkbox<br>4. Add maximum allowed column definitions plus one<br>5. Click Submit | Form submission is blocked; error shown indicating maximum column definitions exceeded | medium |
| TC-016 (state_edge) | WF-004 | Rapid consecutive approval of audit trails | Maker-checker is enabled, At least one audit trail is pending approval | 1. Click Approve on the first pending audit trail<br>2. Immediately click Approve on the second pending audit trail | First approval succeeds; second approval is blocked with a message indicating it cannot be approved again until the first is processed | medium |
| TC-017 (state_edge) | WF-005 | Rapid consecutive rejection of audit trails | Maker-checker is enabled, At least one audit trail is pending rejection | 1. Click Reject on the first pending audit trail<br>2. Immediately click Reject on the second pending audit trail | First rejection succeeds; second rejection is blocked with a message indicating it cannot be rejected again until the first is processed | medium |

---

## Logout

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click on 'Log Out' | User is redirected to the login page after terminating the authenticated session and clearing the authentication token | high |
| TC-002 | WF-002 | User navigates to Profile Settings | User logged in as <Role> | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click on 'Profile Settings' | User is navigated to the Profile Settings page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to log out while already logged out | User is not authenticated | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User remains on the current page; no session is terminated; no redirection occurs. | high |
| TC-004 |  | Attempt to access authenticated page after logout | User is logged out | 1. Attempt to navigate to an authenticated page | Redirects to the login page; access to the authenticated page is blocked. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click 'Log Out'<br>3. Immediately click 'Log Out' again before the redirect completes | Second logout attempt is blocked; user remains on the login page without a second session termination | medium |
| TC-006 (input_edge) |  | Attempt to access authenticated page after logout | User is logged in and has logged out | 1. Click on the User Profile Icon to reveal the dropdown<br>2. Click 'Log Out'<br>3. Attempt to navigate to an authenticated page | User is redirected to the login page; no authenticated access is granted | medium |

---
