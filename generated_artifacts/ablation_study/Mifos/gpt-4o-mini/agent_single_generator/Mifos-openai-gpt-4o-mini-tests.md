# Test Cases — Mifos

Generated: 2026-06-09T09:49:13.866149Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 336 | 162 | 121 | 53 | 206 | 122 | 8 |

## Login

Total: **9** (positive: 3, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User is on the Login page, User has valid credentials | 1. Enter valid Username<br>2. Enter valid Password<br>3. Click on Login button | User is redirected to the Dashboard | high |
| TC-006 | WF-001 | Login with valid credentials and Remember me checked | User is on the Login page, User has valid credentials | 1. Enter valid Username<br>2. Enter valid Password<br>3. Check Remember me checkbox<br>4. Click on Login button | User is redirected to the Dashboard with Remember me option set | medium |
| TC-007 | WF-002 | Initiate password recovery | User is on the Login page | 1. Click on Forgot Password? link | Password recovery process is initiated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Login with empty Username and Password | User is on the Login page | 1. Leave Username field empty<br>2. Leave Password field empty<br>3. Click on Login button | Inline validation messages for empty required fields are displayed | high |
| TC-003 | WF-001 | Login with invalid credentials | User is on the Login page, User has invalid credentials | 1. Enter invalid Username<br>2. Enter invalid Password<br>3. Click on Login button | Error message indicating invalid credentials is displayed | high |
| TC-004 | WF-001 | Login with valid Username and empty Password | User is on the Login page | 1. Enter valid Username<br>2. Leave Password field empty<br>3. Click on Login button | Inline validation message for empty Password is displayed | medium |
| TC-005 | WF-001 | Login with empty Username and valid Password | User is on the Login page | 1. Leave Username field empty<br>2. Enter valid Password<br>3. Click on Login button | Inline validation message for empty Username is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Login with maximum length Username and Password | User is on the Login page | 1. Enter maximum length Username<br>2. Enter maximum length Password<br>3. Click on Login button | User is redirected to the Dashboard if credentials are valid | low |
| TC-009 | WF-001 | Login with minimum length Username and Password | User is on the Login page | 1. Enter minimum length Username<br>2. Enter minimum length Password<br>3. Click on Login button | User is redirected to the Dashboard if credentials are valid | low |

---

## Home Page

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard Successfully | User logged in as User, Home page is displayed | 1. Click on the Dashboard button | User is redirected to the dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Dashboard Button Disabled When Not Logged In | User not logged in, Home page is displayed | 1. Attempt to click on the Dashboard button | Dashboard button is disabled and no action is taken | high |
| TC-004 | WF-001 | Search Activity Input Field with Special Characters | User logged in as User, Home page is displayed | 1. Enter special characters in the Search Activity input field | Validation error is shown for invalid input | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Search Activity Input Field Limit | User logged in as User, Home page is displayed | 1. Enter 255 characters in the Search Activity input field | Input is accepted without errors | medium |

---

## Dashboard

Total: **7** (positive: 3, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Dashboard successfully | User logged in as Admin, User is on the Home page | 1. Click on the 'Dashboard' button | Dashboard is displayed with search activity field and client trends chart | high |
| TC-006 | WF-001 | Client Trends chart displays correctly | User logged in as Admin, User is on the Dashboard | 1. Observe the 'Client Trends' chart | Client Trends chart is displayed with 'New Clients' and 'Closed Clients' legends | medium |
| TC-007 | WF-001 | Summary cards display 'No Data' | User logged in as Admin, User is on the Dashboard with no data available | 1. Observe the summary cards | Summary cards display 'No Data' for both 'Amount Pending / Disbursed' and 'Amount Collected' | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Access Dashboard without being logged in | User is not logged in | 1. Click on the 'Dashboard' button | User is prompted to log in before accessing the Dashboard | high |
| TC-003 | WF-001 | Access Dashboard from an invalid page | User logged in as User, User is on an invalid page | 1. Click on the 'Dashboard' button | User is redirected to the Home page | medium |
| TC-005 | WF-001 | Search Activity field with no input | User logged in as Admin, User is on the Dashboard | 1. Leave the 'Search Activity' field empty<br>2. Attempt to search | Error message displayed indicating that input is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Search Activity field with maximum characters | User logged in as Admin, User is on the Dashboard | 1. Enter 255 characters in the 'Search Activity' field | Search Activity field accepts the input without errors | medium |

---

## Global Search

Total: **8** (positive: 5, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field successfully | User logged in as regular user | 1. Click on the search icon in the top toolbar | Search input field opens | high |
| TC-002 | WF-002 | Search with valid input and results found | User logged in as regular user, Search input field is open | 1. Type 'John' in the search input<br>2. Observe the search results | Search results are displayed for Clients, Groups, Loans, and Savings accounts containing 'John' | high |
| TC-003 | WF-003 | Display no results message when no matches found | User logged in as regular user, Search input field is open | 1. Type 'xyz123' in the search input<br>2. Observe the search results | No results found message is displayed | medium |
| TC-006 | WF-002 | Search with partial matching | User logged in as regular user, Search input field is open | 1. Type 'Jo' in the search input<br>2. Observe the search results | Search results are displayed for Clients, Groups, Loans, and Savings accounts containing 'Jo' | high |
| TC-007 | WF-002 | Search case insensitivity | User logged in as regular user, Search input field is open | 1. Type 'john' in the search input<br>2. Observe the search results | Search results are displayed for Clients, Groups, Loans, and Savings accounts containing 'John' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-002 | Search with invalid input | User logged in as regular user, Search input field is open | 1. Type special characters '!@#$%' in the search input | No results found message is displayed | medium |
| TC-005 | WF-002 | Search with empty input | User logged in as regular user, Search input field is open | 1. Leave the search input empty and press enter | No results found message is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-003 | No results message visibility | User logged in as regular user, Search input field is open | 1. Type a very long string that exceeds typical entity names in the search input | No results found message is displayed | medium |

---

## Client Management

Total: **20** (positive: 10, negative: 8, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Import Client opens Bulk Import page | User logged in as Admin | 1. Navigate to Clients page<br>2. Click on Import Client button | Bulk Import page opens | high |
| TC-002 | WF-002 | Create Client wizard opens | User logged in as Admin | 1. Navigate to Clients page<br>2. Click on Create Client button | Create Client wizard opens | high |
| TC-003 | WF-003 | Download Client Template downloads Excel template | User logged in as Admin, On Bulk Import page | 1. Click on Download Template button | Client Excel template downloads | medium |
| TC-004 | WF-004 | Upload Client File uploads file successfully | User logged in as Admin, On Bulk Import page | 1. Click on Upload File<br>2. Select a valid client file<br>3. Click on Upload | File uploads successfully | high |
| TC-005 | WF-005 | Submit Create Client wizard creates client | User logged in as Admin, On Create Client wizard | 1. Fill in required fields<br>2. Click on Submit | Client is created in Pending status | high |
| TC-006 | WF-006 | Activate Pending Client with valid Activation Date | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Enter valid Activation Date<br>3. Click on Activate | Client is activated | high |
| TC-007 | WF-007 | Edit Pending Client | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Click on Edit button<br>3. Make changes<br>4. Click on Save | Client details are updated | medium |
| TC-008 | WF-008 | Reject Pending Client with reason | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Click on Reject button<br>3. Enter reason<br>4. Click on Confirm | Client is rejected | medium |
| TC-009 | WF-009 | Withdraw Pending Client with reason | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Click on Withdraw button<br>3. Enter reason<br>4. Click on Confirm | Client is withdrawn | medium |
| TC-010 | WF-010 | Reactivate Closed Client | User logged in as Admin, Client is in Closed status | 1. Navigate to Client Detail page<br>2. Click on Reactivate button | Client is reactivated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Import Client button is disabled when no file is uploaded | User logged in as Admin, On Bulk Import page | 1. Click on Import Client button without uploading a file | Import Client button is disabled | high |
| TC-012 | WF-005 | Submit Create Client wizard without required fields | User logged in as Admin, On Create Client wizard | 1. Leave required fields empty<br>2. Click on Submit | Error message displayed for required fields | high |
| TC-013 | WF-006 | Activate Pending Client with Activation Date before submission date | User logged in as Admin, Client is in Pending status, Activation Date is before submission date | 1. Navigate to Client Detail page<br>2. Enter Activation Date before submission date<br>3. Click on Activate | Error message displayed for invalid Activation Date | high |
| TC-014 | WF-008 | Reject Client without providing a reason | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Click on Reject button<br>3. Leave reason empty<br>4. Click on Confirm | Error message displayed for missing reason | high |
| TC-015 | WF-009 | Withdraw Client without providing a reason | User logged in as Admin, Client is in Pending status | 1. Navigate to Client Detail page<br>2. Click on Withdraw button<br>3. Leave reason empty<br>4. Click on Confirm | Error message displayed for missing reason | high |
| TC-016 | WF-005 | Submit Create Client wizard with duplicate External ID | User logged in as Admin, On Create Client wizard | 1. Fill in required fields with existing External ID<br>2. Click on Submit | Error message displayed for duplicate External ID | high |
| TC-017 | WF-005 | Submit Create Client wizard with future Submitted On date | User logged in as Admin, On Create Client wizard | 1. Fill in required fields with future Submitted On date<br>2. Click on Submit | Error message displayed for future Submitted On date | high |
| TC-018 | WF-005 | Submit Create Client wizard without filling any fields | User logged in as Admin, On Create Client wizard | 1. Click on Submit without filling any fields | Error message displayed for required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 | WF-005 | Create Client wizard with maximum character limits | User logged in as Admin, On Create Client wizard | 1. Fill in fields with maximum allowed characters<br>2. Click on Submit | Client is created successfully with maximum character limits | medium |
| TC-020 | WF-005 | Create Client wizard with minimum character limits | User logged in as Admin, On Create Client wizard | 1. Fill in fields with minimum allowed characters<br>2. Click on Submit | Client is created successfully with minimum character limits | medium |

---

## Group Management

Total: **20** (positive: 9, negative: 8, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Group Details with valid group | User logged in as Admin, Group exists in the system | 1. Navigate to Groups page<br>2. Click on the group name link | Displays group details including name, account number, status, office, and staff | high |
| TC-002 | WF-002 | Create a new group with valid data | User logged in as Admin, On Create Group form | 1. Fill in Name, Office, Submitted On<br>2. Click Submit | Creates the group and displays success message | high |
| TC-003 | WF-003 | Bulk import groups with valid file | User logged in as Admin, On Bulk Import Groups page | 1. Select a valid file to upload<br>2. Click Upload | Import history table updated with new import entry | medium |
| TC-004 | WF-004 | Activate a group | User logged in as Admin, Group is in Pending status | 1. Navigate to Group Detail page<br>2. Click Activate | Group activated and status updated to Active | high |
| TC-005 | WF-005 | Edit group details successfully | User logged in as Admin, Group exists | 1. Navigate to Group Detail page<br>2. Click Edit<br>3. Modify details<br>4. Click Save | Group details updated successfully | medium |
| TC-006 | WF-006 | Close a group | User logged in as Admin, Group is Active | 1. Navigate to Group Detail page<br>2. Click Close | Group closed and status updated to Closed | medium |
| TC-007 | WF-007 | Assign staff to a group | User logged in as Admin, Group exists | 1. Navigate to Group Detail page<br>2. Click Assign Staff<br>3. Select staff<br>4. Click Assign | Staff assigned to group successfully | medium |
| TC-008 | WF-008 | Transfer clients from a group | User logged in as Admin, Group has clients | 1. Navigate to Group Detail page<br>2. Click Transfer Clients<br>3. Select clients<br>4. Click Transfer | Clients transferred successfully | medium |
| TC-009 | WF-009 | Generate collection sheet | User logged in as Admin, Group has clients | 1. Navigate to Group Detail page<br>2. Click Generate Collection Sheet | Generates a sheet showing all group clients with loan repayment amounts due and savings deposit amounts for batch data entry | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-002 | Create a new group without required fields | User logged in as Admin, On Create Group form | 1. Leave Name and Office fields blank<br>2. Click Submit | Displays validation error messages for required fields | high |
| TC-011 | WF-003 | Bulk import groups with invalid file format | User logged in as Admin, On Bulk Import Groups page | 1. Select an invalid file format<br>2. Click Upload | Displays error message for invalid file format | high |
| TC-012 | WF-004 | Activate a group that is already active | User logged in as Admin, Group is already Active | 1. Navigate to Group Detail page<br>2. Click Activate | Displays message indicating the group is already active | medium |
| TC-013 | WF-005 | Edit group with invalid data | User logged in as Admin, Group exists | 1. Navigate to Group Detail page<br>2. Click Edit<br>3. Enter invalid data<br>4. Click Save | Displays validation error messages | medium |
| TC-014 | WF-006 | Close a group that is already closed | User logged in as Admin, Group is already Closed | 1. Navigate to Group Detail page<br>2. Click Close | Displays message indicating the group is already closed | medium |
| TC-015 | WF-007 | Assign staff to a group without selecting staff | User logged in as Admin, Group exists | 1. Navigate to Group Detail page<br>2. Click Assign Staff<br>3. Leave staff selection empty<br>4. Click Assign | Displays validation error message for staff selection | medium |
| TC-016 | WF-008 | Transfer clients from a group with no clients | User logged in as Admin, Group has no clients | 1. Navigate to Group Detail page<br>2. Click Transfer Clients | Displays message indicating no clients to transfer | medium |
| TC-017 | WF-009 | Generate collection sheet for a group with no clients | User logged in as Admin, Group has no clients | 1. Navigate to Group Detail page<br>2. Click Generate Collection Sheet | Displays message indicating no clients available for the collection sheet | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 | WF-002 | Create a new group with maximum character limit in Name | User logged in as Admin, On Create Group form | 1. Fill in Name with maximum characters allowed<br>2. Fill in Office, Submitted On<br>3. Click Submit | Creates the group successfully with maximum character limit | medium |
| TC-019 | WF-003 | Bulk import groups with a large file size | User logged in as Admin, On Bulk Import Groups page | 1. Select a large valid file to upload<br>2. Click Upload | Import history table updated with new import entry | medium |
| TC-020 | WF-004 | Activate a group with maximum allowed clients | User logged in as Admin, Group has maximum clients | 1. Navigate to Group Detail page<br>2. Click Activate | Group activated successfully with maximum clients | medium |

---

## Center Management

Total: **13** (positive: 7, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Center Details with valid center name | User logged in as Admin, Center exists in the system | 1. Navigate to the Centers page<br>2. Click on the center name link | Displays center details including name, status, office, and staff | high |
| TC-002 | WF-002 | Import Centers with valid file | User logged in as Admin, Valid import file is prepared | 1. Navigate to the Bulk Import Centers page<br>2. Upload the valid file<br>3. Click Submit | Imports centers successfully | high |
| TC-003 | WF-003 | Create Center with all required fields filled | User logged in as Admin | 1. Navigate to the Create Center form<br>2. Fill in Name, Office, Submitted On<br>3. Click Submit | Creates the center successfully | high |
| TC-004 | WF-004 | Activate Center when center is active | User logged in as Admin, Center is in Active state | 1. Navigate to the Center Detail page<br>2. Click Activate | Center activated successfully | medium |
| TC-005 | WF-005 | Edit Center with valid changes | User logged in as Admin, Center is in Active state | 1. Navigate to the Center Detail page<br>2. Click Edit<br>3. Make changes<br>4. Click Submit | Center edited successfully | medium |
| TC-006 | WF-006 | Close Center when center is active | User logged in as Admin, Center is in Active state | 1. Navigate to the Center Detail page<br>2. Click Close | Center closed successfully | medium |
| TC-007 | WF-007 | Assign Staff to Center when center is active | User logged in as Admin, Center is in Active state | 1. Navigate to the Center Detail page<br>2. Click Assign Staff<br>3. Select staff member<br>4. Click Submit | Staff assigned to center successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-003 | Create Center with missing required fields | User logged in as Admin | 1. Navigate to the Create Center form<br>2. Leave Name and Office blank<br>3. Click Submit | Error message indicating required fields are missing | high |
| TC-009 | WF-002 | Import Centers with invalid file format | User logged in as Admin, Invalid import file is prepared | 1. Navigate to the Bulk Import Centers page<br>2. Upload the invalid file<br>3. Click Submit | Error message indicating invalid file format | high |
| TC-010 | WF-004 | Activate Center when center is inactive | User logged in as Admin, Center is in Inactive state | 1. Navigate to the Center Detail page<br>2. Click Activate | Error message indicating center cannot be activated | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-003 | Create Center with long name exceeding character limit | User logged in as Admin | 1. Navigate to the Create Center form<br>2. Enter a name longer than the maximum allowed characters<br>3. Click Submit | Error message indicating name exceeds character limit | medium |
| TC-012 | WF-003 | Create Center with future date in Submitted On field | User logged in as Admin | 1. Navigate to the Create Center form<br>2. Fill in Name, Office, and Submitted On with a future date<br>3. Click Submit | Error message indicating submitted date cannot be in the future | medium |
| TC-013 | WF-002 | Import Centers with empty file upload | User logged in as Admin | 1. Navigate to the Bulk Import Centers page<br>2. Leave file upload empty<br>3. Click Submit | Error message indicating file upload is required | high |

---

## Loan Products

Total: **13** (positive: 8, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Loan Product Details | User logged in as <Role>, At least one loan product exists | 1. Navigate to Loan Products page<br>2. Click on the Name of the loan product | Loan product details displayed | high |
| TC-002 | WF-002 | Edit Loan Product | User logged in as <Role>, User has access to edit loan products | 1. Navigate to Loan Products page<br>2. Click on the Edit option of a loan product | Loan product edit form displayed | high |
| TC-003 | WF-003 | Create Loan Product - Valid Step 1 Submission | User logged in as <Role>, User is on the Create Loan Product wizard | 1. Fill in Product Name and Short Name<br>2. Click Next | Step 2 of the wizard displayed | high |
| TC-005 | WF-004 | Create Loan Product - Valid Step 2 Submission | User logged in as <Role>, User completed Step 1 successfully | 1. Fill in Principal Amount with valid value<br>2. Click Next | Step 3 of the wizard displayed | high |
| TC-007 | WF-005 | Create Loan Product - Valid Step 3 Submission | User logged in as <Role>, User completed Step 2 successfully | 1. Fill in Grace Period and Arrears Tolerance with valid values<br>2. Click Next | Step 4 of the wizard displayed | high |
| TC-008 | WF-006 | Create Loan Product - Valid Step 4 Submission | User logged in as <Role>, User completed Step 3 successfully | 1. Fill in Number of Repayments with valid value<br>2. Select Repaid Every frequency<br>3. Fill in Nominal Interest Rate<br>4. Click Next | Step 5 of the wizard displayed | high |
| TC-009 | WF-007 | Create Loan Product - Valid Step 5 Submission | User logged in as <Role>, User completed Step 4 successfully | 1. Click Next | Step 6 of the wizard displayed | high |
| TC-010 | WF-008 | Create Loan Product - Valid Step 6 Submission | User logged in as <Role>, User completed Step 5 successfully | 1. Select Accounting Method<br>2. Click Submit | Loan product created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Create Loan Product - Missing Required Fields | User logged in as <Role>, User is on the Create Loan Product wizard | 1. Leave Product Name and Short Name empty<br>2. Click Next | Inline validation errors displayed for required fields | high |
| TC-006 | WF-004 | Create Loan Product - Invalid Principal Amount | User logged in as <Role>, User completed Step 1 successfully | 1. Fill in Principal Amount with invalid value (e.g., negative)<br>2. Click Next | Validation error displayed for Principal Amount | high |
| TC-013 | WF-008 | Create Loan Product - Step 6 Accounting Method Validation | User logged in as <Role>, User completed Step 5 successfully | 1. Select 'None' as Accounting Method<br>2. Click Submit | GL Account Mappings dropdown should not be visible, and loan product created; success message shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-003 | Create Loan Product - Step 1 Boundary Test | User logged in as <Role>, User is on the Create Loan Product wizard | 1. Fill in Product Name with maximum character limit<br>2. Fill in Short Name with maximum character limit<br>3. Click Next | Step 2 of the wizard displayed | medium |
| TC-012 | WF-005 | Create Loan Product - Step 4 Boundary Test | User logged in as <Role>, User completed Step 3 successfully | 1. Fill in Number of Repayments with minimum value<br>2. Click Next | Step 5 of the wizard displayed | medium |

---

## Savings Products

Total: **7** (positive: 3, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Savings Product with valid details | User logged in as Admin, On the Savings Products page | 1. Click on '+ Create Savings Product' button<br>2. Fill in 'Product Name' with 'High Yield Savings'<br>3. Fill in 'Short Name' with 'HY Savings'<br>4. Click 'Submit' | Savings product created; success message shown | high |
| TC-004 | WF-002 | Create Fixed Deposit Product with valid details | User logged in as Admin, On the Fixed Deposit Products page | 1. Click on '+ Create Fixed Deposit Product' button<br>2. Fill in 'Product Name' with 'Fixed Deposit 1 Year'<br>3. Fill in 'Short Name' with 'FD 1Y'<br>4. Click 'Submit' | Fixed deposit product created; success message shown | high |
| TC-006 | WF-003 | Create Recurring Deposit Product with valid details | User logged in as Admin, On the Recurring Deposit Products page | 1. Click on '+ Create Recurring Deposit Product' button<br>2. Fill in 'Product Name' with 'Recurring Deposit 6 Months'<br>3. Fill in 'Short Name' with 'RD 6M'<br>4. Click 'Submit' | Recurring deposit product created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create Savings Product without Product Name | User logged in as Admin, On the Savings Products page | 1. Click on '+ Create Savings Product' button<br>2. Leave 'Product Name' empty<br>3. Fill in 'Short Name' with 'HY Savings'<br>4. Click 'Submit' | Error message displayed indicating 'Product Name is required' | high |
| TC-005 | WF-002 | Create Fixed Deposit Product without Short Name | User logged in as Admin, On the Fixed Deposit Products page | 1. Click on '+ Create Fixed Deposit Product' button<br>2. Fill in 'Product Name' with 'Fixed Deposit 1 Year'<br>3. Leave 'Short Name' empty<br>4. Click 'Submit' | Error message displayed indicating 'Short Name is required' | high |
| TC-007 | WF-003 | Create Recurring Deposit Product with negative Minimum Opening Balance | User logged in as Admin, On the Recurring Deposit Products page | 1. Click on '+ Create Recurring Deposit Product' button<br>2. Fill in 'Product Name' with 'Recurring Deposit 6 Months'<br>3. Fill in 'Short Name' with 'RD 6M'<br>4. Set 'Minimum Opening Balance' to '-100'<br>5. Click 'Submit' | Error message displayed indicating 'Minimum Opening Balance cannot be negative' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Create Savings Product with very long Short Name | User logged in as Admin, On the Savings Products page | 1. Click on '+ Create Savings Product' button<br>2. Fill in 'Product Name' with 'High Yield Savings'<br>3. Fill in 'Short Name' with 'This is a very long short name that exceeds the limit'<br>4. Click 'Submit' | Error message displayed indicating 'Short Name exceeds maximum length' | medium |

---

## Share Products

Total: **20** (positive: 11, negative: 6, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit existing product successfully | User logged in as Admin, Product exists in the Share Products table | 1. Click on the Product Name link in the Share Products table<br>2. Click on the Edit button | Product details opened for editing | high |
| TC-002 | WF-002 | Delete existing product successfully | User logged in as Admin, Product exists in the Share Products table | 1. Click on the Product Name link in the Share Products table<br>2. Click on the Delete button<br>3. Confirm deletion | Product deleted successfully | high |
| TC-003 | WF-003 | Create new share product successfully | User logged in as Admin | 1. Click on the + Create Share Product button | Opens 7-step stepper wizard | high |
| TC-004 | WF-004 | Submit Details step with valid data | User is on the Details step of the wizard | 1. Enter valid Product Name<br>2. Enter valid Short Name<br>3. Enter valid Description<br>4. Click Next | Currency step displayed | medium |
| TC-005 | WF-005 | Submit Currency step with valid data | User is on the Currency step of the wizard | 1. Enter valid Currency<br>2. Enter valid Decimal Places<br>3. Enter valid Currency In Multiples Of<br>4. Click Next | Terms step displayed | medium |
| TC-006 | WF-006 | Submit Terms step with valid data | User is on the Terms step of the wizard | 1. Enter valid Total Number of Shares<br>2. Enter valid Nominal Unit Price<br>3. Click Next | Settings step displayed | medium |
| TC-007 | WF-007 | Submit Settings step with valid data | User is on the Settings step of the wizard | 1. Enter valid Minimum Shares per Client<br>2. Click Next | Market Price step displayed | medium |
| TC-008 | WF-008 | Submit Market Price step with valid data | User is on the Market Price step of the wizard | 1. Enter valid From Date<br>2. Enter valid Share Value<br>3. Click Next | Charges step displayed | medium |
| TC-009 | WF-009 | Submit Charges step successfully | User is on the Charges step of the wizard | 1. Click Next | Accounting step displayed | medium |
| TC-010 | WF-010 | Submit Accounting step with None method | User is on the Accounting step of the wizard, Accounting_Method is None | 1. Click Finish | Share product created successfully | high |
| TC-011 | WF-011 | Submit Accounting step with Cash-based method | User is on the Accounting step of the wizard, Accounting_Method is Cash-based | 1. Click Finish | Share product created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-004 | Submit Details step with missing Product Name | User is on the Details step of the wizard | 1. Leave Product Name empty<br>2. Enter valid Short Name<br>3. Enter valid Description<br>4. Click Next | Error message displayed for missing Product Name | high |
| TC-013 | WF-006 | Submit Terms step with invalid Total Number of Shares | User is on the Terms step of the wizard | 1. Enter invalid Total Number of Shares (e.g., negative value)<br>2. Click Next | Error message displayed for invalid Total Number of Shares | high |
| TC-014 | WF-007 | Submit Settings step with invalid Minimum Shares per Client | User is on the Settings step of the wizard | 1. Enter invalid Minimum Shares per Client (e.g., negative value)<br>2. Click Next | Error message displayed for invalid Minimum Shares per Client | high |
| TC-015 | WF-008 | Submit Market Price step with invalid From Date | User is on the Market Price step of the wizard | 1. Enter invalid From Date (e.g., future date)<br>2. Enter valid Share Value<br>3. Click Next | Error message displayed for invalid From Date | high |
| TC-016 | WF-010 | Submit Accounting step without selecting a method | User is on the Accounting step of the wizard | 1. Leave Accounting Method unselected<br>2. Click Finish | Error message displayed for unselected Accounting Method | high |
| TC-017 | WF-001 | Edit product that does not exist | User logged in as Admin | 1. Attempt to edit a non-existent product | Error message displayed for product not found | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 | WF-003 | Create share product with maximum character limit for Product Name | User logged in as Admin | 1. Click on the + Create Share Product button<br>2. Enter a Product Name with maximum allowed characters<br>3. Enter valid Short Name<br>4. Enter valid Description<br>5. Click Next | Currency step displayed | medium |
| TC-019 | WF-005 | Submit Currency step with maximum decimal places | User is on the Currency step of the wizard | 1. Enter valid Currency<br>2. Enter maximum allowed Decimal Places<br>3. Click Next | Terms step displayed | medium |
| TC-020 | WF-006 | Submit Terms step with maximum shares | User is on the Terms step of the wizard | 1. Enter maximum allowed Total Number of Shares<br>2. Enter valid Nominal Unit Price<br>3. Click Next | Settings step displayed | medium |

---

## Charges

Total: **7** (positive: 3, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create charge with valid inputs | User logged in as Admin, User is on the Charges page | 1. Click on '+ Create Charge' button<br>2. Fill in 'Charge Name' with 'Service Fee'<br>3. Select 'Charge Applies To' as 'Loan'<br>4. Enter 'Currency' as 'USD'<br>5. Select 'Charge Time Type' as 'Disbursement'<br>6. Select 'Charge Calculation Type' as 'Flat'<br>7. Enter 'Amount' as '100'<br>8. Click on 'Submit' button | Charge definition created successfully and displayed in the Charges table | high |
| TC-004 | WF-002 | Edit existing charge successfully | User logged in as Admin, User is on the Charges page, At least one charge exists | 1. Click on the charge link to open its detail view<br>2. Click on 'Edit' button<br>3. Change 'Charge Name' to 'Updated Service Fee'<br>4. Click on 'Submit' button | Charge details updated successfully and reflected in the Charges table | high |
| TC-005 | WF-003 | Delete existing charge | User logged in as Admin, User is on the Charges page, At least one charge exists | 1. Click on the charge link to open its detail view<br>2. Click on 'Delete' button<br>3. Confirm deletion | Charge deleted successfully and no longer appears in the Charges table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create charge with missing required fields | User logged in as Admin, User is on the Charges page | 1. Click on '+ Create Charge' button<br>2. Leave 'Charge Name' empty<br>3. Select 'Charge Applies To' as 'Client'<br>4. Enter 'Currency' as 'USD'<br>5. Click on 'Submit' button | Error message displayed indicating 'Charge Name is required' | high |
| TC-003 | WF-001 | Create charge with invalid amount | User logged in as Admin, User is on the Charges page | 1. Click on '+ Create Charge' button<br>2. Fill in 'Charge Name' with 'Service Fee'<br>3. Select 'Charge Applies To' as 'Loan'<br>4. Enter 'Currency' as 'USD'<br>5. Select 'Charge Time Type' as 'Disbursement'<br>6. Select 'Charge Calculation Type' as 'Flat'<br>7. Enter 'Amount' as '-50'<br>8. Click on 'Submit' button | Error message displayed indicating 'Amount must be a positive value' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Create charge with maximum character length for Charge Name | User logged in as Admin, User is on the Charges page | 1. Click on '+ Create Charge' button<br>2. Fill in 'Charge Name' with a string of 255 characters<br>3. Select 'Charge Applies To' as 'Savings Account'<br>4. Enter 'Currency' as 'USD'<br>5. Click on 'Submit' button | Charge definition created successfully with maximum character length | medium |
| TC-007 | WF-001 | Create charge with zero amount | User logged in as Admin, User is on the Charges page | 1. Click on '+ Create Charge' button<br>2. Fill in 'Charge Name' with 'Service Fee'<br>3. Select 'Charge Applies To' as 'Loan'<br>4. Enter 'Currency' as 'USD'<br>5. Select 'Charge Time Type' as 'Disbursement'<br>6. Select 'Charge Calculation Type' as 'Flat'<br>7. Enter 'Amount' as '0'<br>8. Click on 'Submit' button | Error message displayed indicating 'Amount must be greater than zero' | medium |

---

## Floating Rates

Total: **8** (positive: 2, negative: 5, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Floating Rate with valid data | User logged in as Admin, User is on the Floating Rates page | 1. Click on '+ Create Floating Rate' button<br>2. Fill in 'Floating Rate Name' with a valid name<br>3. Check 'Is Base Lending Rate'<br>4. Check 'Is Active'<br>5. Add a Rate Period with 'From Date' and 'Interest Rate'<br>6. Click 'Submit' | Floating rate created; success message shown | high |
| TC-005 | WF-002 | Edit Floating Rate with valid data | User logged in as Admin, User is on the Floating Rates page, At least one floating rate exists | 1. Click on the 'Edit' link for an existing floating rate<br>2. Change the 'Floating Rate Name'<br>3. Click 'Submit' | Floating rate details updated; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create Floating Rate without Floating Rate Name | User logged in as Admin, User is on the Floating Rates page | 1. Click on '+ Create Floating Rate' button<br>2. Leave 'Floating Rate Name' empty<br>3. Click 'Submit' | Error message indicating 'Floating Rate Name' is required | high |
| TC-003 | WF-001 | Create multiple Base Lending Rates | User logged in as Admin, User is on the Floating Rates page | 1. Click on '+ Create Floating Rate' button<br>2. Fill in 'Floating Rate Name' with a valid name<br>3. Check 'Is Base Lending Rate'<br>4. Click 'Submit'<br>5. Click on '+ Create Floating Rate' button again<br>6. Fill in 'Floating Rate Name' with another valid name<br>7. Check 'Is Base Lending Rate'<br>8. Click 'Submit' | Error message indicating only one base rate can exist at a time | high |
| TC-006 | WF-002 | Edit Floating Rate to empty name | User logged in as Admin, User is on the Floating Rates page, At least one floating rate exists | 1. Click on the 'Edit' link for an existing floating rate<br>2. Clear the 'Floating Rate Name'<br>3. Click 'Submit' | Error message indicating 'Floating Rate Name' is required | high |
| TC-007 | WF-002 | Edit Floating Rate to set multiple Base Lending Rates | User logged in as Admin, User is on the Floating Rates page, At least one floating rate exists | 1. Click on the 'Edit' link for an existing floating rate<br>2. Check 'Is Base Lending Rate'<br>3. Click 'Submit'<br>4. Click on '+ Create Floating Rate' button<br>5. Fill in 'Floating Rate Name' with another valid name<br>6. Check 'Is Base Lending Rate'<br>7. Click 'Submit' | Error message indicating only one base rate can exist at a time | high |
| TC-008 | WF-002 | Edit Floating Rate with invalid Interest Rate | User logged in as Admin, User is on the Floating Rates page, At least one floating rate exists | 1. Click on the 'Edit' link for an existing floating rate<br>2. Change the 'Interest Rate' to a non-numeric value<br>3. Click 'Submit' | Error message indicating 'Interest Rate' must be a number | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Create Floating Rate with future date in Rate Period | User logged in as Admin, User is on the Floating Rates page | 1. Click on '+ Create Floating Rate' button<br>2. Fill in 'Floating Rate Name' with a valid name<br>3. Check 'Is Active'<br>4. Add a Rate Period with 'From Date' set to a future date<br>5. Fill in 'Interest Rate'<br>6. Click 'Submit' | Floating rate created; success message shown, but future date warning is displayed | medium |

---

## Delinquency Management

Total: **8** (positive: 4, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successfully create a delinquency range with valid inputs | User logged in as Admin, On Create Delinquency Range Form page | 1. Enter 'Low Risk' in Classification field<br>2. Enter '1' in Minimum Age Days field<br>3. Enter '30' in Maximum Age Days field<br>4. Click on Submit button | Delinquency range created; success message shown | high |
| TC-004 | WF-002 | Successfully create a delinquency bucket with valid inputs | User logged in as Admin, On Create Delinquency Bucket Form page | 1. Enter 'Default Bucket' in Bucket Name field<br>2. Add a delinquency range with Range Name '1-29 days' and Days '29'<br>3. Click on Submit button | Delinquency bucket created; success message shown | high |
| TC-007 | WF-003 | View classification details in delinquency ranges | User logged in as Admin, On Delinquency Ranges page | 1. Click on Classification link for a specific range | Classification details displayed | medium |
| TC-008 | WF-004 | View bucket details in delinquency buckets | User logged in as Admin, On Delinquency Buckets page | 1. Click on Bucket Name link for a specific bucket | Bucket details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Fail to create a delinquency range with missing required fields | User logged in as Admin, On Create Delinquency Range Form page | 1. Leave Classification field blank<br>2. Enter '1' in Minimum Age Days field<br>3. Click on Submit button | Error message displayed indicating Classification is required | high |
| TC-005 | WF-002 | Fail to create a delinquency bucket with missing required fields | User logged in as Admin, On Create Delinquency Bucket Form page | 1. Leave Bucket Name field blank<br>2. Click on Submit button | Error message displayed indicating Bucket Name is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Create a delinquency range with only Minimum Age Days filled | User logged in as Admin, On Create Delinquency Range Form page | 1. Enter 'Medium Risk' in Classification field<br>2. Enter '15' in Minimum Age Days field<br>3. Leave Maximum Age Days field blank<br>4. Click on Submit button | Delinquency range created; success message shown | medium |
| TC-006 | WF-002 | Create a delinquency bucket with only Bucket Name filled | User logged in as Admin, On Create Delinquency Bucket Form page | 1. Enter 'Test Bucket' in Bucket Name field<br>2. Leave Delinquency Ranges section empty<br>3. Click on Submit button | Delinquency bucket created; success message shown | medium |

---

## Loan Account

Total: **17** (positive: 11, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit loan application with valid details | User logged in as Loan Officer, Client details are available | 1. Navigate to Loan Application Wizard.<br>2. Fill in all required fields in Step 1 with valid data.<br>3. Proceed to Step 2 and fill in all required fields.<br>4. Proceed to Step 3 and review inherited charges.<br>5. Proceed to Step 4 and add collateral items if necessary.<br>6. Click on 'Submit'. | Loan is created in 'Submitted and Pending Approval' status. | high |
| TC-004 | WF-002 | Approve loan application with valid details | User logged in as Loan Officer, Loan application is in 'Pending Approval' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Approve'.<br>3. Fill in all required fields in the approval dialog.<br>4. Click on 'Confirm'. | Loan application is approved and status is updated to 'Approved'. | high |
| TC-005 | WF-002 | Reject loan application | User logged in as Loan Officer, Loan application is in 'Pending Approval' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Reject'. | Loan application is rejected. | medium |
| TC-006 | WF-003 | Withdraw loan application | User logged in as Loan Officer, Loan application is in 'Pending Approval' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Withdraw'. | Loan application is withdrawn. | medium |
| TC-007 | WF-006 | Disburse loan with valid details | User logged in as Loan Officer, Loan application is in 'Approved' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Disburse'.<br>3. Fill in all required fields in the disbursement form.<br>4. Click on 'Confirm'. | Loan is disbursed. | high |
| TC-008 | WF-008 | Make repayment with valid details | User logged in as Client, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Make Repayment'.<br>3. Fill in all required fields in the repayment form.<br>4. Click on 'Confirm'. | Repayment is made successfully. | high |
| TC-010 | WF-012 | Reschedule loan with valid details | User logged in as Loan Officer, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Reschedule'.<br>3. Fill in all required fields in the reschedule form.<br>4. Click on 'Confirm'. | Loan is rescheduled successfully. | medium |
| TC-012 | WF-013 | Prepay loan with valid details | User logged in as Client, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Prepay Loan'.<br>3. Fill in all required fields in the prepayment form.<br>4. Click on 'Confirm'. | Loan is prepaid successfully. | high |
| TC-013 | WF-014 | Foreclose loan with valid details | User logged in as Loan Officer, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Foreclose'.<br>3. Fill in all required fields in the foreclosure form.<br>4. Click on 'Confirm'. | Loan is foreclosed successfully. | medium |
| TC-014 | WF-015 | Charge off loan with valid details | User logged in as Loan Officer, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Charge Off'.<br>3. Fill in all required fields in the charge-off form.<br>4. Click on 'Confirm'. | Loan is charged off successfully. | medium |
| TC-015 | WF-016 | Assign loan officer with valid details | User logged in as Loan Officer, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Assign Loan Officer'.<br>3. Select a loan officer from the dropdown.<br>4. Click on 'Confirm'. | Loan officer is assigned successfully. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit loan application with missing required fields | User logged in as Loan Officer, Client details are available | 1. Navigate to Loan Application Wizard.<br>2. Fill in some required fields in Step 1 but leave one or more required fields empty.<br>3. Click on 'Submit'. | Error message indicating required fields must be filled. | high |
| TC-003 | WF-001 | Submit loan application with invalid Principal amount | User logged in as Loan Officer, Client details are available | 1. Navigate to Loan Application Wizard.<br>2. Fill in all required fields in Step 1 with valid data except for Principal which is set below minimum.<br>3. Click on 'Submit'. | Error message indicating Principal amount is invalid. | high |
| TC-009 | WF-008 | Make repayment with invalid amount | User logged in as Client, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Make Repayment'.<br>3. Enter an amount greater than the total due.<br>4. Click on 'Confirm'. | Error message indicating repayment amount exceeds total due. | high |
| TC-011 | WF-012 | Reschedule loan with invalid date | User logged in as Loan Officer, Loan application is in 'Active' status | 1. Navigate to Loan Detail Page.<br>2. Click on 'Reschedule'.<br>3. Enter an invalid date for Adjusted Due Date.<br>4. Click on 'Confirm'. | Error message indicating the date is invalid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 | WF-001 | Submit loan application with maximum character limits | User logged in as Loan Officer, Client details are available | 1. Navigate to Loan Application Wizard.<br>2. Fill in all required fields in Step 1 with maximum character limits.<br>3. Proceed to Step 2 and fill in all required fields.<br>4. Proceed to Step 3 and review inherited charges.<br>5. Proceed to Step 4 and add collateral items if necessary.<br>6. Click on 'Submit'. | Loan is created in 'Submitted and Pending Approval' status. | low |
| TC-017 | WF-001 | Submit loan application with boundary date values | User logged in as Loan Officer, Client details are available | 1. Navigate to Loan Application Wizard.<br>2. Fill in all required fields in Step 1 with valid data including boundary dates.<br>3. Proceed to Step 2 and fill in all required fields.<br>4. Proceed to Step 3 and review inherited charges.<br>5. Proceed to Step 4 and add collateral items if necessary.<br>6. Click on 'Submit'. | Loan is created in 'Submitted and Pending Approval' status. | low |

---

## Savings Account

Total: **10** (positive: 7, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Savings Account Creation with valid data | User logged in as Client Manager, Client details are filled in | 1. Select a product from the Product Name dropdown<br>2. Fill in the Nominal Annual Interest Rate<br>3. Select Interest Compounding Period<br>4. Select Interest Posting Period<br>5. Select Interest Calculated Using<br>6. Select Days in Year<br>7. Enter Minimum Opening Balance<br>8. Enter Lock-in Period<br>9. Check Allow Overdraft if applicable<br>10. Add Charges if applicable<br>11. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-003 | WF-002 | Approve Pending Savings Account | User logged in as Approver, Account is in Pending status | 1. Navigate to the Pending Accounts<br>2. Select the account to approve<br>3. Click Approve | Account status changes to Approved | high |
| TC-004 | WF-003 | Reject Pending Savings Account | User logged in as Approver, Account is in Pending status | 1. Navigate to the Pending Accounts<br>2. Select the account to reject<br>3. Click Reject | Account status changes to Rejected | high |
| TC-005 | WF-007 | Deposit into Active Savings Account with valid data | User logged in as Account Holder, Account is Active | 1. Navigate to the Active Account<br>2. Click Deposit<br>3. Fill in Transaction Date<br>4. Enter Transaction Amount<br>5. Select Payment Type<br>6. Click Submit | Amount credited to account | high |
| TC-008 | WF-015 | No actions available for Dormant Savings Account | User logged in as Account Holder, Account is Dormant | 1. Navigate to the Dormant Account | No action buttons are displayed | medium |
| TC-009 | WF-016 | No actions available for Closed Savings Account | User logged in as Account Holder, Account is Closed | 1. Navigate to the Closed Account | No action buttons are displayed | medium |
| TC-010 | WF-017 | No actions available for Blocked Savings Account | User logged in as Account Holder, Account is Blocked | 1. Navigate to the Blocked Account | No action buttons are displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit Savings Account Creation with missing required fields | User logged in as Client Manager, Client details are filled in | 1. Leave Nominal Annual Interest Rate blank<br>2. Click Submit | Error message displayed indicating required fields must be filled | high |
| TC-006 | WF-008 | Withdraw from Active Savings Account exceeding available balance | User logged in as Account Holder, Account is Active, Available balance is less than withdrawal amount | 1. Navigate to the Active Account<br>2. Click Withdraw<br>3. Fill in Transaction Date<br>4. Enter Transaction Amount greater than available balance<br>5. Select Payment Type<br>6. Click Submit | Error message displayed indicating withdrawal exceeds available balance | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-008 | Withdraw from Active Savings Account with minimum balance enforcement | User logged in as Account Holder, Account is Active, Available balance is equal to minimum balance | 1. Navigate to the Active Account<br>2. Click Withdraw<br>3. Fill in Transaction Date<br>4. Enter Transaction Amount equal to available balance<br>5. Select Payment Type<br>6. Click Submit | Error message displayed indicating withdrawal cannot breach minimum balance | high |

---

## Share Account

Total: **13** (positive: 8, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application with valid data | User logged in as Client, User has valid active savings account | 1. Navigate to Share Account Application Form<br>2. Select a valid Share Product from the dropdown<br>3. Enter a valid Submitted On date<br>4. Enter a valid number of Requested Shares within the min/max limit<br>5. Enter a valid Application Date<br>6. Select a valid Savings Account for Charges<br>7. Click on Submit | Account is created in Submitted and Pending Approval status | high |
| TC-004 | WF-002 | Approve Pending Share Account with valid data | User logged in as Manager, Share Account is in Pending status | 1. Navigate to Share Account Detail Page<br>2. Click on Approve button<br>3. Enter valid Approved Shares<br>4. Enter valid Approved Date<br>5. Click on Confirm | Approval process completed successfully | high |
| TC-006 | WF-003 | Reject Pending Share Account | User logged in as Manager, Share Account is in Pending status | 1. Navigate to Share Account Detail Page<br>2. Click on Reject button<br>3. Confirm rejection | Rejection process completed successfully | high |
| TC-007 | WF-004 | Activate Approved Share Account | User logged in as Manager, Share Account is in Approved status | 1. Navigate to Share Account Detail Page<br>2. Click on Activate button | Account activated successfully | high |
| TC-008 | WF-005 | Undo Approval of Share Account | User logged in as Manager, Share Account is in Approved status | 1. Navigate to Share Account Detail Page<br>2. Click on Undo Approval button<br>3. Confirm undo approval | Approval undone successfully | medium |
| TC-009 | WF-006 | Apply Additional Shares to Active Share Account | User logged in as Client, Share Account is in Active status | 1. Navigate to Share Account Detail Page<br>2. Click on Apply Additional Shares button<br>3. Enter valid number of Additional Shares<br>4. Click on Confirm | Additional shares applied successfully | high |
| TC-010 | WF-007 | Redeem Shares from Active Share Account | User logged in as Client, Share Account is in Active status | 1. Navigate to Share Account Detail Page<br>2. Click on Redeem Shares button<br>3. Enter valid number of Shares to redeem<br>4. Click on Confirm | Redemption amount calculated and credited to linked savings account | high |
| TC-011 | WF-008 | Close Active Share Account | User logged in as Client, Share Account is in Active status | 1. Navigate to Share Account Detail Page<br>2. Click on Close button<br>3. Confirm closure | Account closed successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit Share Account Application with missing required fields | User logged in as Client | 1. Navigate to Share Account Application Form<br>2. Leave Share Product dropdown empty<br>3. Leave Submitted On date empty<br>4. Leave Requested Shares empty<br>5. Leave Application Date empty<br>6. Leave Savings Account for Charges empty<br>7. Click on Submit | Error messages displayed for all required fields | high |
| TC-003 | WF-001 | Submit Share Account Application with invalid Requested Shares | User logged in as Client, User has valid active savings account | 1. Navigate to Share Account Application Form<br>2. Select a valid Share Product from the dropdown<br>3. Enter a valid Submitted On date<br>4. Enter an invalid number of Requested Shares (below min limit)<br>5. Enter a valid Application Date<br>6. Select a valid Savings Account for Charges<br>7. Click on Submit | Error message displayed indicating Requested Shares are below the minimum limit | medium |
| TC-005 | WF-002 | Approve Pending Share Account with missing Approved Shares | User logged in as Manager, Share Account is in Pending status | 1. Navigate to Share Account Detail Page<br>2. Click on Approve button<br>3. Leave Approved Shares empty<br>4. Enter valid Approved Date<br>5. Click on Confirm | Error message displayed for missing Approved Shares | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Submit Share Account Application with maximum Requested Shares | User logged in as Client, User has valid active savings account | 1. Navigate to Share Account Application Form<br>2. Select a valid Share Product from the dropdown<br>3. Enter a valid Submitted On date<br>4. Enter maximum number of Requested Shares<br>5. Enter a valid Application Date<br>6. Select a valid Savings Account for Charges<br>7. Click on Submit | Account is created in Submitted and Pending Approval status | high |
| TC-013 | WF-001 | Submit Share Account Application with minimum Requested Shares | User logged in as Client, User has valid active savings account | 1. Navigate to Share Account Application Form<br>2. Select a valid Share Product from the dropdown<br>3. Enter a valid Submitted On date<br>4. Enter minimum number of Requested Shares<br>5. Enter a valid Application Date<br>6. Select a valid Savings Account for Charges<br>7. Click on Submit | Account is created in Submitted and Pending Approval status | high |

---

## Fixed & Recurring Deposit Accounts

Total: **18** (positive: 11, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Fixed Deposit Account with valid inputs | User logged in as Manager, User on Client Detail page | 1. Select Fixed Deposit Product from dropdown<br>2. Enter valid Deposit Amount<br>3. Enter valid Deposit Period<br>4. Select Deposit Period Unit<br>5. Select Maturity Instructions<br>6. Click Submit | Fixed Deposit account created successfully | high |
| TC-002 | WF-002 | Create Recurring Deposit Account with valid inputs | User logged in as Manager, User on Client Detail page | 1. Select Recurring Deposit Product from dropdown<br>2. Enter valid Mandatory Deposit Amount Per Installment<br>3. Enter valid Deposit Period<br>4. Select Deposit Frequency<br>5. Enter Expected First Deposit On date<br>6. Click Submit | Recurring Deposit account created successfully | high |
| TC-003 | WF-003 | Approve Fixed Deposit Account with valid inputs | User logged in as Manager, User on FD Account Detail Page | 1. Click Approve button | Fixed Deposit account approved | high |
| TC-004 | WF-004 | Activate Fixed Deposit Account | User logged in as Manager, User on FD Account Detail Page | 1. Click Activate button | Fixed Deposit account activated | high |
| TC-005 | WF-005 | Premature Close Fixed Deposit Account | User logged in as Manager, User on FD Account Detail Page | 1. Click Premature Close button | Fixed Deposit account closed prematurely | medium |
| TC-006 | WF-006 | Close Fixed Deposit Account on Maturity | User logged in as Manager, User on FD Account Detail Page | 1. Click Close on Maturity button | Fixed Deposit account closed on maturity | medium |
| TC-007 | WF-007 | Approve Recurring Deposit Account with valid inputs | User logged in as Manager, User on RD Account Detail Page | 1. Click Approve button | Recurring Deposit account approved | high |
| TC-008 | WF-008 | Activate Recurring Deposit Account | User logged in as Manager, User on RD Account Detail Page | 1. Click Activate button | Recurring Deposit account activated | high |
| TC-009 | WF-009 | Deposit into Recurring Deposit Account | User logged in as Manager, User on RD Account Detail Page | 1. Click Deposit button | Deposit made into Recurring Deposit account | medium |
| TC-010 | WF-010 | Premature Close Recurring Deposit Account | User logged in as Manager, User on RD Account Detail Page | 1. Click Premature Close button | Recurring Deposit account closed prematurely | medium |
| TC-011 | WF-011 | Close Recurring Deposit Account on Maturity | User logged in as Manager, User on RD Account Detail Page | 1. Click Close on Maturity button | Recurring Deposit account closed on maturity | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Create Fixed Deposit Account with invalid Deposit Amount | User logged in as Manager, User on Client Detail page | 1. Select Fixed Deposit Product from dropdown<br>2. Enter invalid Deposit Amount (e.g., negative value)<br>3. Enter valid Deposit Period<br>4. Select Deposit Period Unit<br>5. Click Submit | Error message displayed for invalid Deposit Amount | high |
| TC-013 | WF-002 | Create Recurring Deposit Account with invalid Expected First Deposit On date | User logged in as Manager, User on Client Detail page | 1. Select Recurring Deposit Product from dropdown<br>2. Enter valid Mandatory Deposit Amount Per Installment<br>3. Enter valid Deposit Period<br>4. Select Deposit Frequency<br>5. Enter invalid Expected First Deposit On date (e.g., past date)<br>6. Click Submit | Error message displayed for invalid Expected First Deposit On date | high |
| TC-014 | WF-001 | Create Fixed Deposit Account with missing required fields | User logged in as Manager, User on Client Detail page | 1. Click Submit without filling required fields | Error message displayed for missing required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 | WF-001 | Create Fixed Deposit Account with maximum Deposit Amount | User logged in as Manager, User on Client Detail page | 1. Select Fixed Deposit Product from dropdown<br>2. Enter maximum valid Deposit Amount<br>3. Enter valid Deposit Period<br>4. Select Deposit Period Unit<br>5. Click Submit | Fixed Deposit account created successfully | medium |
| TC-016 | WF-002 | Create Recurring Deposit Account with maximum Mandatory Deposit Amount Per Installment | User logged in as Manager, User on Client Detail page | 1. Select Recurring Deposit Product from dropdown<br>2. Enter maximum valid Mandatory Deposit Amount Per Installment<br>3. Enter valid Deposit Period<br>4. Select Deposit Frequency<br>5. Enter Expected First Deposit On date<br>6. Click Submit | Recurring Deposit account created successfully | medium |
| TC-017 | WF-001 | Create Fixed Deposit Account with Deposit Period of zero | User logged in as Manager, User on Client Detail page | 1. Select Fixed Deposit Product from dropdown<br>2. Enter valid Deposit Amount<br>3. Enter Deposit Period as 0<br>4. Select Deposit Period Unit<br>5. Click Submit | Error message displayed for invalid Deposit Period | high |
| TC-018 | WF-002 | Create Recurring Deposit Account with Deposit Period of zero | User logged in as Manager, User on Client Detail page | 1. Select Recurring Deposit Product from dropdown<br>2. Enter valid Mandatory Deposit Amount Per Installment<br>3. Enter Deposit Period as 0<br>4. Select Deposit Frequency<br>5. Enter Expected First Deposit On date<br>6. Click Submit | Error message displayed for invalid Deposit Period | high |

---

## Accounting — Chart of Accounts

Total: **8** (positive: 3, negative: 4, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create GL Account with valid data | User logged in as Accountant, User is on the Chart of Accounts page | 1. Click on '+ Create GL Account' button<br>2. Fill in Account Type, Parent Account, GL Code, Account Name, and Account Usage<br>3. Click on 'Submit' button | GL Account created successfully and displayed in the Chart of Accounts | high |
| TC-005 | WF-002 | Edit existing GL Account with valid data | User logged in as Accountant, User is on the Chart of Accounts page, An existing GL Account is available | 1. Click on the Account Name of the existing GL Account<br>2. Click on 'Edit' button<br>3. Modify the necessary fields<br>4. Click on 'Save' button | Account details updated successfully | high |
| TC-007 | WF-003 | Delete existing GL Account | User logged in as Accountant, User is on the Chart of Accounts page, An existing GL Account is available | 1. Click on the Account Name of the existing GL Account<br>2. Click on 'Delete' button<br>3. Confirm deletion | Account deleted successfully and no longer visible in the Chart of Accounts | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create GL Account with duplicate GL Code | User logged in as Accountant, User is on the Chart of Accounts page | 1. Click on '+ Create GL Account' button<br>2. Fill in Account Type, Parent Account, existing GL Code, Account Name, and Account Usage<br>3. Click on 'Submit' button | Validation error indicating GL Code must be unique | high |
| TC-003 | WF-001 | Create GL Account without required fields | User logged in as Accountant, User is on the Chart of Accounts page | 1. Click on '+ Create GL Account' button<br>2. Leave required fields empty<br>3. Click on 'Submit' button | Validation errors for all required fields | high |
| TC-006 | WF-002 | Edit existing GL Account with invalid data | User logged in as Accountant, User is on the Chart of Accounts page, An existing GL Account is available | 1. Click on the Account Name of the existing GL Account<br>2. Click on 'Edit' button<br>3. Change GL Code to an existing GL Code<br>4. Click on 'Save' button | Validation error indicating GL Code must be unique | high |
| TC-008 | WF-003 | Delete non-existing GL Account | User logged in as Accountant, User is on the Chart of Accounts page | 1. Attempt to delete a GL Account that does not exist<br>2. Confirm deletion | Error message indicating the account does not exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Create GL Account with maximum character length | User logged in as Accountant, User is on the Chart of Accounts page | 1. Click on '+ Create GL Account' button<br>2. Fill in Account Type, Parent Account, GL Code, Account Name with maximum allowed characters<br>3. Click on 'Submit' button | GL Account created successfully with maximum character length | medium |

---

## Accounting — Journal Entries & Closures

Total: **9** (positive: 3, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successfully submit a journal entry with valid data | User logged in as Accountant, User is on the Journal Entries page | 1. Click on '+ Add Journal Entry' button<br>2. Fill in required fields: Office, Currency, Transaction Date<br>3. Add at least one entry line with GL Account and Amount<br>4. Ensure total debits equal total credits<br>5. Click on 'Submit' button | Journal entry created; success message shown | high |
| TC-004 | WF-001 | Filter journal entries by Office and GL Account | User logged in as Accountant, User is on the Journal Entries page | 1. Use filter bar to select an Office<br>2. Use filter bar to select a GL Account<br>3. Click on 'Apply Filters' button | Journal entries table updates to show filtered results | medium |
| TC-005 | WF-002 | Successfully submit a closure with valid data | User logged in as Accountant, User is on the Closing Entries page | 1. Click on '+ Create Closure' button<br>2. Fill in required fields: Office, Closing Date<br>3. Click on 'Submit' button | Closure created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to submit a journal entry with missing required fields | User logged in as Accountant, User is on the Journal Entries page | 1. Click on '+ Add Journal Entry' button<br>2. Leave required fields empty<br>3. Click on 'Submit' button | Validation errors displayed for missing required fields | high |
| TC-003 | WF-001 | Submit a journal entry with total debits not equal to total credits | User logged in as Accountant, User is on the Journal Entries page | 1. Click on '+ Add Journal Entry' button<br>2. Fill in required fields: Office, Currency, Transaction Date<br>3. Add entry lines with GL Account and Amount where total debits do not equal total credits<br>4. Click on 'Submit' button | Validation error displayed stating total debits must equal total credits | high |
| TC-006 | WF-002 | Attempt to submit a closure with missing required fields | User logged in as Accountant, User is on the Closing Entries page | 1. Click on '+ Create Closure' button<br>2. Leave required fields empty<br>3. Click on 'Submit' button | Validation errors displayed for missing required fields | high |
| TC-007 | WF-002 | Attempt to create a closure with a date that allows journal entries | User logged in as Accountant, User is on the Closing Entries page | 1. Click on '+ Create Closure' button<br>2. Fill in required fields: Office, Closing Date (set to a future date)<br>3. Click on 'Submit' button | Closure created; success message shown, journal entries can still be posted | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Check journal entry creation with maximum character limits | User logged in as Accountant, User is on the Journal Entries page | 1. Click on '+ Add Journal Entry' button<br>2. Fill in required fields: Office, Currency, Transaction Date<br>3. Add entry lines with maximum character limits for GL Account and Amount<br>4. Ensure total debits equal total credits<br>5. Click on 'Submit' button | Journal entry created; success message shown | medium |
| TC-009 | WF-001 | Check journal entry creation with zero and negative amounts | User logged in as Accountant, User is on the Journal Entries page | 1. Click on '+ Add Journal Entry' button<br>2. Fill in required fields: Office, Currency, Transaction Date<br>3. Add entry lines with GL Account and Amount set to zero and negative values<br>4. Ensure total debits equal total credits<br>5. Click on 'Submit' button | Validation error displayed for zero and negative amounts | high |

---

## Accounting Rules & Financial Activity Mappings

Total: **8** (positive: 4, negative: 4, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a valid accounting rule | User logged in as Accountant, User on Accounting Rules page | 1. Click on '+ Create Rule' button<br>2. Select 'Office 1' from the Office dropdown<br>3. Enter 'Test Rule' in the Rule Name field<br>4. Select 'GL Account 1' from the Debit Tags/Debit Account dropdown<br>5. Check 'Allow Multiple Debit Entries'<br>6. Select 'GL Account 2' from the Credit Tags/Credit Account dropdown<br>7. Check 'Allow Multiple Credit Entries'<br>8. Click 'Submit' | Assignment created; success message shown | high |
| TC-004 | WF-002 | Edit an existing accounting rule | User logged in as Accountant, User on Accounting Rules page, At least one rule exists | 1. Click on the rule link to view details<br>2. Click 'Edit'<br>3. Change 'Rule Name' to 'Updated Rule'<br>4. Click 'Submit' | Rule details updated; success message shown | high |
| TC-005 | WF-003 | Delete an existing accounting rule | User logged in as Accountant, User on Accounting Rules page, At least one rule exists | 1. Click on the rule link to view details<br>2. Click 'Delete'<br>3. Confirm deletion | Rule deleted; success message shown | high |
| TC-006 | WF-004 | Create a valid financial activity mapping | User logged in as Accountant, User on Financial Activity Mappings page | 1. Click on '+ Create Mapping' button<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select 'GL Account 1' from the GL Account dropdown<br>4. Click 'Create Mapping' | Mapping created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create accounting rule without Rule Name | User logged in as Accountant, User on Accounting Rules page | 1. Click on '+ Create Rule' button<br>2. Select 'Office 1' from the Office dropdown<br>3. Leave the Rule Name field empty<br>4. Select 'GL Account 1' from the Debit Tags/Debit Account dropdown<br>5. Click 'Submit' | Error message indicating Rule Name is required | high |
| TC-003 | WF-001 | Create accounting rule with invalid office selection | User logged in as Accountant, User on Accounting Rules page | 1. Click on '+ Create Rule' button<br>2. Select blank from the Office dropdown<br>3. Enter 'Test Rule' in the Rule Name field<br>4. Select 'GL Account 1' from the Debit Tags/Debit Account dropdown<br>5. Click 'Submit' | Success message shown; rule created applicable to all offices | medium |
| TC-007 | WF-004 | Create financial activity mapping with already mapped activity | User logged in as Accountant, User on Financial Activity Mappings page, Mapping for 'Asset Transfer' already exists | 1. Click on '+ Create Mapping' button<br>2. Select 'Asset Transfer' from the Financial Activity dropdown<br>3. Select 'GL Account 1' from the GL Account dropdown<br>4. Click 'Create Mapping' | Error message indicating financial activity is already mapped | high |
| TC-008 | WF-004 | Create financial activity mapping with invalid selection | User logged in as Accountant, User on Financial Activity Mappings page | 1. Click on '+ Create Mapping' button<br>2. Select blank from the Financial Activity dropdown<br>3. Select 'GL Account 1' from the GL Account dropdown<br>4. Click 'Create Mapping' | Error message indicating financial activity selection is required | high |

---

## Provisioning

Total: **8** (positive: 5, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Provisioning Criteria with valid data | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click on '+ Create' button<br>2. Fill in 'Criteria Name' with 'Test Criteria'<br>3. Add a row in Definitions with valid data for all required fields<br>4. Click on 'Submit' | New provisioning criteria 'Test Criteria' is created and displayed in the criteria table | high |
| TC-005 | WF-002 | Create Provisioning Entry with valid data | User logged in as Admin, User is on the Provisioning Entries page | 1. Click on '+ Create Provisioning Entry' button<br>2. Confirm the creation of provisioning entries based on current loan portfolio status | New provisioning entries are generated and displayed in the entries table | high |
| TC-006 | WF-003 | Review Provisioning Entry | User logged in as Admin, User is on the Provisioning Entries page, At least one entry exists | 1. Click on 'Review' action for the first entry in the table | Detailed breakdown by loan product and category is displayed | medium |
| TC-007 | WF-004 | Recreate Provisioning Entry | User logged in as Admin, User is on the Provisioning Entries page, At least one entry exists | 1. Click on 'Recreate' action for the first entry in the table<br>2. Confirm the recreation of the entry | Provisioning entry is recreated successfully and displayed in the entries table | medium |
| TC-008 | WF-005 | View Criteria Name details | User logged in as Admin, User is on the Provisioning Criteria page, At least one criteria exists | 1. Click on the 'Criteria Name' link for the first criteria in the table | User is navigated to the criteria details page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create Provisioning Criteria with missing Criteria Name | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click on '+ Create' button<br>2. Leave 'Criteria Name' empty<br>3. Add a row in Definitions with valid data for all required fields<br>4. Click on 'Submit' | Error message displayed indicating 'Criteria Name is required' | high |
| TC-003 | WF-001 | Create Provisioning Criteria with invalid Minimum Age | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click on '+ Create' button<br>2. Fill in 'Criteria Name' with 'Test Criteria'<br>3. Add a row in Definitions with 'Minimum Age' set to -1<br>4. Click on 'Submit' | Error message displayed indicating 'Minimum Age must be a positive number' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Create Provisioning Criteria with maximum rows in Definitions | User logged in as Admin, User is on the Provisioning Criteria page | 1. Click on '+ Create' button<br>2. Fill in 'Criteria Name' with 'Test Criteria'<br>3. Add 10 rows in Definitions with valid data for all required fields<br>4. Click on 'Submit' | New provisioning criteria 'Test Criteria' is created with 10 definitions and displayed in the criteria table | medium |

---

## Offices

Total: **7** (positive: 2, negative: 4, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create office with valid details | User logged in as Admin, User is on the Offices page | 1. Click on '+ Create Office' button<br>2. Fill in 'Office Name' with 'New Office'<br>3. Select 'Parent Office' as 'Head Office'<br>4. Enter 'Opened On Date' as '2023-10-01'<br>5. Enter 'External ID' as 'EO-123'<br>6. Click on 'Submit' button | Office created successfully message is displayed | high |
| TC-006 | WF-002 | View office detail after creation | User logged in as Admin, An office 'New Office' has been created | 1. Click on 'Office Name' link for 'New Office' | Office details for 'New Office' are displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create office with missing Office Name | User logged in as Admin, User is on the Offices page | 1. Click on '+ Create Office' button<br>2. Leave 'Office Name' blank<br>3. Select 'Parent Office' as 'Head Office'<br>4. Enter 'Opened On Date' as '2023-10-01'<br>5. Enter 'External ID' as 'EO-123'<br>6. Click on 'Submit' button | Error message indicating 'Office Name is required' is displayed | high |
| TC-003 | WF-001 | Create office with invalid Opened On Date | User logged in as Admin, User is on the Offices page | 1. Click on '+ Create Office' button<br>2. Fill in 'Office Name' with 'New Office'<br>3. Select 'Parent Office' as 'Head Office'<br>4. Enter 'Opened On Date' as 'invalid-date'<br>5. Enter 'External ID' as 'EO-123'<br>6. Click on 'Submit' button | Error message indicating 'Opened On Date is invalid' is displayed | high |
| TC-004 | WF-001 | Create office with missing Parent Office | User logged in as Admin, User is on the Offices page | 1. Click on '+ Create Office' button<br>2. Fill in 'Office Name' with 'New Office'<br>3. Leave 'Parent Office' blank<br>4. Enter 'Opened On Date' as '2023-10-01'<br>5. Enter 'External ID' as 'EO-123'<br>6. Click on 'Submit' button | Error message indicating 'Parent Office is required' is displayed | high |
| TC-007 | WF-002 | View office detail for non-existing office | User logged in as Admin, User is on the Offices page | 1. Attempt to access 'Office Name' link for a non-existing office | Error message indicating 'Office not found' is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Create office with maximum length External ID | User logged in as Admin, User is on the Offices page | 1. Click on '+ Create Office' button<br>2. Fill in 'Office Name' with 'New Office'<br>3. Select 'Parent Office' as 'Head Office'<br>4. Enter 'Opened On Date' as '2023-10-01'<br>5. Enter 'External ID' with 255 characters<br>6. Click on 'Submit' button | Office created successfully message is displayed | medium |

---

## Employees

Total: **9** (positive: 3, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View employee details successfully | User logged in as HR, Employee exists in the table | 1. Navigate to Employees page<br>2. Click on the employee's Name link | Employee details displayed | high |
| TC-003 | WF-002 | Edit employee details successfully | User logged in as HR, Employee exists in the table | 1. Navigate to Employees page<br>2. Click on the Edit action for the employee | Employee edit form displayed | high |
| TC-005 | WF-003 | Create new employee successfully | User logged in as HR | 1. Navigate to Employees page<br>2. Click on the + Create Employee button<br>3. Fill in required fields<br>4. Submit the form | New employee created and displayed in the table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | View employee details when employee does not exist | User logged in as HR, Employee does not exist | 1. Navigate to Employees page<br>2. Attempt to click on a non-existent employee's Name link | Error message displayed: Employee not found | high |
| TC-004 | WF-002 | Edit employee details with invalid data | User logged in as HR, Employee exists in the table | 1. Navigate to Employees page<br>2. Click on the Edit action for the employee<br>3. Leave required fields empty<br>4. Attempt to submit the form | Validation errors displayed for required fields | high |
| TC-006 | WF-003 | Create new employee with missing required fields | User logged in as HR | 1. Navigate to Employees page<br>2. Click on the + Create Employee button<br>3. Leave required fields empty<br>4. Attempt to submit the form | Validation errors displayed for required fields | high |
| TC-007 | WF-003 | Create new employee with invalid mobile number | User logged in as HR | 1. Navigate to Employees page<br>2. Click on the + Create Employee button<br>3. Fill in valid required fields and an invalid mobile number<br>4. Submit the form | Validation error displayed for mobile number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-003 | Create new employee with maximum character limits | User logged in as HR | 1. Navigate to Employees page<br>2. Click on the + Create Employee button<br>3. Fill in required fields with maximum characters<br>4. Submit the form | New employee created successfully with maximum character limits | medium |
| TC-009 | WF-003 | Create new employee with future joining date | User logged in as HR | 1. Navigate to Employees page<br>2. Click on the + Create Employee button<br>3. Fill in required fields and set Joining Date to a future date<br>4. Submit the form | New employee created successfully with future joining date | medium |

---

## Teller & Cashier Management

Total: **10** (positive: 3, negative: 5, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Teller with valid data | User logged in as Manager, On the Tellers page | 1. Click on '+ Create Teller' button<br>2. Fill in 'Office' with valid office name<br>3. Fill in 'Teller Name' with valid name<br>4. Fill in 'Start Date' with a valid date<br>5. Click 'Submit' | Teller created; success message shown | high |
| TC-005 | WF-002 | Allocate Cashier with valid data | User logged in as Manager, On the Teller Detail page | 1. Click on '+ Allocate Cashier' button<br>2. Fill in 'Staff' with valid staff name<br>3. Fill in 'Start Date' with a valid date<br>4. Click 'Allocate Cash' | Cashier allocated; success message shown | high |
| TC-009 | WF-003 | View Teller Details successfully | User logged in as Manager, On the Tellers page | 1. Click on a Teller Name link<br>2. Observe the Teller Detail page | Teller details displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create Teller with missing required fields | User logged in as Manager, On the Tellers page | 1. Click on '+ Create Teller' button<br>2. Leave 'Office' and 'Teller Name' blank<br>3. Click 'Submit' | Error message shown for required fields | high |
| TC-003 | WF-001 | Create Teller with invalid date format | User logged in as Manager, On the Tellers page | 1. Click on '+ Create Teller' button<br>2. Fill in 'Office' with valid office name<br>3. Fill in 'Teller Name' with valid name<br>4. Fill in 'Start Date' with invalid date format<br>5. Click 'Submit' | Error message shown for invalid date format | medium |
| TC-006 | WF-002 | Allocate Cashier with missing required fields | User logged in as Manager, On the Teller Detail page | 1. Click on '+ Allocate Cashier' button<br>2. Leave 'Staff' and 'Start Date' blank<br>3. Click 'Allocate Cash' | Error message shown for required fields | high |
| TC-007 | WF-002 | Allocate Cashier with invalid date format | User logged in as Manager, On the Teller Detail page | 1. Click on '+ Allocate Cashier' button<br>2. Fill in 'Staff' with valid staff name<br>3. Fill in 'Start Date' with invalid date format<br>4. Click 'Allocate Cash' | Error message shown for invalid date format | medium |
| TC-010 | WF-003 | View Teller Details for non-existent Teller | User logged in as Manager, On the Tellers page | 1. Attempt to access Teller Detail page via invalid URL | Error message shown for Teller not found | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Create Teller with future Start Date | User logged in as Manager, On the Tellers page | 1. Click on '+ Create Teller' button<br>2. Fill in 'Office' with valid office name<br>3. Fill in 'Teller Name' with valid name<br>4. Fill in 'Start Date' with a date in the future<br>5. Click 'Submit' | Teller created; success message shown | low |
| TC-008 | WF-002 | Allocate Cashier with future Start Date | User logged in as Manager, On the Teller Detail page | 1. Click on '+ Allocate Cashier' button<br>2. Fill in 'Staff' with valid staff name<br>3. Fill in 'Start Date' with a date in the future<br>4. Click 'Allocate Cash' | Cashier allocated; success message shown | low |

---

## Users & Roles

Total: **8** (positive: 3, negative: 4, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View User Details | User logged in as Admin, User exists in the Users table | 1. Navigate to Users page<br>2. Click on the Username link of the user | User details are displayed correctly | high |
| TC-002 | WF-002 | Create User with valid data | User logged in as Admin, No existing user with the same username | 1. Navigate to Users page<br>2. Click on '+ Create User' button<br>3. Fill in all required fields with valid data<br>4. Click on Submit | User created; success message shown | high |
| TC-006 | WF-003 | Create Role with valid data | User logged in as Admin | 1. Navigate to Roles page<br>2. Click on '+ Create Role' button<br>3. Fill in Role Name and Description<br>4. Click on Submit | Role created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Create User with duplicate username | User logged in as Admin, User already exists with the same username | 1. Navigate to Users page<br>2. Click on '+ Create User' button<br>3. Fill in all required fields with duplicate username<br>4. Click on Submit | Error message displayed indicating username must be unique | high |
| TC-004 | WF-002 | Create User with invalid email format | User logged in as Admin | 1. Navigate to Users page<br>2. Click on '+ Create User' button<br>3. Fill in all required fields with invalid email format<br>4. Click on Submit | Error message displayed indicating invalid email format | medium |
| TC-005 | WF-002 | Create User with mismatched passwords | User logged in as Admin | 1. Navigate to Users page<br>2. Click on '+ Create User' button<br>3. Fill in all required fields with mismatched passwords<br>4. Click on Submit | Error message displayed indicating passwords must match | medium |
| TC-007 | WF-003 | Create Role with missing Role Name | User logged in as Admin | 1. Navigate to Roles page<br>2. Click on '+ Create Role' button<br>3. Leave Role Name empty<br>4. Click on Submit | Error message displayed indicating Role Name is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-003 | Create Role with long Role Name | User logged in as Admin | 1. Navigate to Roles page<br>2. Click on '+ Create Role' button<br>3. Fill in Role Name with maximum allowed characters<br>4. Click on Submit | Role created; success message shown | medium |

---

## Reports

Total: **9** (positive: 5, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open report with all parameters filled | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Fill in all parameters in the Parameters Form<br>3. Click on the Run Report button | The report is generated as a data table with sorting and pagination | high |
| TC-002 | WF-002 | Open report with output option View on Screen | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Select 'View on Screen' from Output Options<br>3. Click on the Run Report button | The report is displayed on the screen as a data table with sorting and pagination | high |
| TC-003 | WF-003 | Open report with output option Export to Excel | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Select 'Export to Excel' from Output Options<br>3. Click on the Run Report button | The report is downloaded as an Excel file | high |
| TC-004 | WF-004 | Open report with output option Export to CSV | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Select 'Export to CSV' from Output Options<br>3. Click on the Run Report button | The report is downloaded as a CSV file | high |
| TC-005 | WF-005 | Open report with output option Export to PDF | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Select 'Export to PDF' from Output Options<br>3. Click on the Run Report button | The report is downloaded as a PDF file | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Open report with no parameters filled | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Leave all parameters empty<br>3. Click on the Run Report button | An error message is displayed indicating that parameters are required | high |
| TC-007 | WF-001 | Open report with invalid parameter values | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Enter invalid values in the parameters<br>3. Click on the Run Report button | An error message is displayed indicating invalid parameter values | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Open report with maximum character limit in parameters | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Fill in parameters with maximum allowed characters<br>3. Click on the Run Report button | The report is generated successfully as a data table with sorting and pagination | medium |
| TC-009 | WF-001 | Open report with empty date range | User logged in as Report Viewer, User is on the Reports page | 1. Click on a report link from the Reports page<br>2. Leave the Date Range parameter empty<br>3. Click on the Run Report button | The report is generated with the default date range applied | medium |

---

## Account Transfers & Standing Instructions

Total: **10** (positive: 5, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid account transfer | User logged in as Account Holder, User has sufficient balance | 1. Fill in From Account Type as Savings Account<br>2. Select From Account<br>3. Fill in To Account Type as Loan Account<br>4. Select To Account<br>5. Enter valid Transfer Amount<br>6. Select Transfer Date<br>7. Click Submit | Transfer is processed, source account debited and destination account credited | high |
| TC-004 | WF-005 | Create standing instruction with all fields valid | User logged in as Account Holder | 1. Click on '+ Create Standing Instruction'<br>2. Fill in Name<br>3. Select From Account<br>4. Select To Account<br>5. Select Instruction Type as Fixed<br>6. Enter Amount<br>7. Select Validity From and Till dates<br>8. Click Create | New standing instruction is created successfully | high |
| TC-006 | WF-002 | Enable a standing instruction | User logged in as Account Holder, At least one standing instruction exists | 1. Navigate to Standing Instructions Table<br>2. Click Enable on a standing instruction row | Standing instruction is enabled successfully | medium |
| TC-007 | WF-003 | Disable a standing instruction | User logged in as Account Holder, At least one standing instruction exists | 1. Navigate to Standing Instructions Table<br>2. Click Disable on a standing instruction row | Standing instruction is disabled successfully | medium |
| TC-008 | WF-004 | Delete a standing instruction | User logged in as Account Holder, At least one standing instruction exists | 1. Navigate to Standing Instructions Table<br>2. Click Delete on a standing instruction row<br>3. Confirm deletion | Standing instruction is deleted successfully | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit account transfer with amount exceeding balance | User logged in as Account Holder, User has insufficient balance | 1. Fill in From Account Type as Savings Account<br>2. Select From Account<br>3. Fill in To Account Type as Loan Account<br>4. Select To Account<br>5. Enter Transfer Amount exceeding available balance<br>6. Select Transfer Date<br>7. Click Submit | Error message displayed: 'Transfer amount exceeds available balance' | high |
| TC-003 | WF-001 | Submit account transfer with missing transfer date | User logged in as Account Holder, User has sufficient balance | 1. Fill in From Account Type as Savings Account<br>2. Select From Account<br>3. Fill in To Account Type as Loan Account<br>4. Select To Account<br>5. Enter valid Transfer Amount<br>6. Leave Transfer Date blank<br>7. Click Submit | Error message displayed: 'Transfer Date is required' | high |
| TC-005 | WF-005 | Create standing instruction without required name | User logged in as Account Holder | 1. Click on '+ Create Standing Instruction'<br>2. Leave Name blank<br>3. Select From Account<br>4. Select To Account<br>5. Select Instruction Type as Fixed<br>6. Enter Amount<br>7. Select Validity From and Till dates<br>8. Click Create | Error message displayed: 'Name is required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Submit account transfer with future date | User logged in as Account Holder, User has sufficient balance | 1. Fill in From Account Type as Savings Account<br>2. Select From Account<br>3. Fill in To Account Type as Loan Account<br>4. Select To Account<br>5. Enter valid Transfer Amount<br>6. Select a future Transfer Date<br>7. Click Submit | Transfer is scheduled successfully for the future date | medium |
| TC-010 | WF-001 | Submit account transfer with zero amount | User logged in as Account Holder, User has sufficient balance | 1. Fill in From Account Type as Savings Account<br>2. Select From Account<br>3. Fill in To Account Type as Loan Account<br>4. Select To Account<br>5. Enter Transfer Amount as 0<br>6. Select Transfer Date<br>7. Click Submit | Error message displayed: 'Transfer amount must be greater than zero' | medium |

---

## Tax Management

Total: **10** (positive: 4, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Tax Components | User logged in as Admin, Tax Components exist in the database | 1. Navigate to Tax Components page<br>2. Click on a Tax Component link | Tax Component details are displayed correctly | high |
| TC-002 | WF-002 | Create Tax Component with valid data | User logged in as Admin | 1. Click on '+ Create Tax Component' button<br>2. Fill in valid Name, Percentage, Start Date<br>3. Click Submit | Tax component created; success message shown | high |
| TC-006 | WF-003 | View Tax Groups | User logged in as Admin, Tax Groups exist in the database | 1. Navigate to Tax Groups page<br>2. Click on a Tax Group link | Tax Group details are displayed correctly | high |
| TC-007 | WF-004 | Create Tax Group with valid data | User logged in as Admin | 1. Click on '+ Create Tax Group' button<br>2. Fill in valid Name<br>3. Add Tax Components with valid Start Date and End Date<br>4. Click Submit | Tax group created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Create Tax Component with missing required fields | User logged in as Admin | 1. Click on '+ Create Tax Component' button<br>2. Leave Name and Percentage empty<br>3. Click Submit | Error message indicating required fields are missing | high |
| TC-004 | WF-002 | Create Tax Component with invalid Percentage | User logged in as Admin | 1. Click on '+ Create Tax Component' button<br>2. Fill in valid Name, invalid Percentage (e.g., -5)<br>3. Click Submit | Error message indicating invalid Percentage | medium |
| TC-008 | WF-004 | Create Tax Group with missing required Name | User logged in as Admin | 1. Click on '+ Create Tax Group' button<br>2. Leave Name empty<br>3. Click Submit | Error message indicating Name is required | high |
| TC-009 | WF-004 | Create Tax Group with invalid Start Date | User logged in as Admin | 1. Click on '+ Create Tax Group' button<br>2. Fill in valid Name<br>3. Add Tax Components with invalid Start Date (e.g., future date)<br>4. Click Submit | Error message indicating invalid Start Date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-002 | Create Tax Component with maximum length Name | User logged in as Admin | 1. Click on '+ Create Tax Component' button<br>2. Fill in Name with maximum allowed characters<br>3. Fill in valid Percentage and Start Date<br>4. Click Submit | Tax component created; success message shown | medium |
| TC-010 | WF-004 | Create Tax Group with maximum length Name | User logged in as Admin | 1. Click on '+ Create Tax Group' button<br>2. Fill in Name with maximum allowed characters<br>3. Click Submit | Tax group created; success message shown | medium |

---

## Organization Settings

Total: **11** (positive: 5, negative: 6, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a holiday with valid details | User logged in as Admin, On Holidays Page | 1. Click on '+ Create Holiday'<br>2. Fill in 'Name' with 'New Year'<br>3. Set 'From_Date' to '2023-01-01'<br>4. Set 'To_Date' to '2023-01-01'<br>5. Click 'Submit' | A new holiday 'New Year' is created and displayed in the holidays table | high |
| TC-004 | WF-002 | Submit working days configuration with all days selected | User logged in as Admin, On Working Days Page | 1. Check all days from Monday to Sunday<br>2. Select a value from 'Repayment_Rescheduling'<br>3. Click 'Submit' | Working days updated successfully message is displayed | medium |
| TC-006 | WF-003 | Bulk import data with valid file | User logged in as Admin, On Bulk Import Page | 1. Click on 'Download_Template' to get the template<br>2. Fill the template with valid data<br>3. Upload the filled template<br>4. Click 'Submit' | Data imported successfully message is displayed | high |
| TC-008 | WF-004 | Create a fund with valid details | User logged in as Admin, On Funds Page | 1. Click on 'Create Fund'<br>2. Fill in 'Fund_Name' with 'Emergency Fund'<br>3. Click 'Create Fund' | Fund 'Emergency Fund' is created successfully | high |
| TC-010 | WF-005 | Create a payment type with valid details | User logged in as Admin, On Payment Types Page | 1. Click on '+ Create'<br>2. Fill in 'Payment_Type_Name' with 'Credit Card'<br>3. Click '+ Create' | Payment type 'Credit Card' is created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Create a holiday with missing required fields | User logged in as Admin, On Holidays Page | 1. Click on '+ Create Holiday'<br>2. Leave 'Name' empty<br>3. Set 'From_Date' to '2023-01-01'<br>4. Set 'To_Date' to '2023-01-01'<br>5. Click 'Submit' | An error message indicating 'Name is required' is displayed | high |
| TC-003 | WF-001 | Create a holiday with invalid date range | User logged in as Admin, On Holidays Page | 1. Click on '+ Create Holiday'<br>2. Fill in 'Name' with 'Invalid Holiday'<br>3. Set 'From_Date' to '2023-01-02'<br>4. Set 'To_Date' to '2023-01-01'<br>5. Click 'Submit' | An error message indicating 'To Date must be after From Date' is displayed | high |
| TC-005 | WF-002 | Submit working days configuration without selecting any days | User logged in as Admin, On Working Days Page | 1. Leave all days unchecked<br>2. Select a value from 'Repayment_Rescheduling'<br>3. Click 'Submit' | An error message indicating 'At least one working day must be selected' is displayed | high |
| TC-007 | WF-003 | Bulk import data with invalid file format | User logged in as Admin, On Bulk Import Page | 1. Upload a file that is not in the required format<br>2. Click 'Submit' | An error message indicating 'Invalid file format' is displayed | high |
| TC-009 | WF-004 | Create a fund without Fund Name | User logged in as Admin, On Funds Page | 1. Click on 'Create Fund'<br>2. Leave 'Fund_Name' empty<br>3. Click 'Create Fund' | An error message indicating 'Fund Name is required' is displayed | high |
| TC-011 | WF-005 | Create a payment type without Payment Type Name | User logged in as Admin, On Payment Types Page | 1. Click on '+ Create'<br>2. Leave 'Payment_Type_Name' empty<br>3. Click '+ Create' | An error message indicating 'Payment Type Name is required' is displayed | high |

---

## System Administration

Total: **23** (positive: 10, negative: 10, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit Scheduler Job with valid data | User logged in as Admin, Scheduler job exists | 1. Navigate to Manage Scheduler Jobs<br>2. Click Edit on the desired job<br>3. Update Job Name and CRON Expression<br>4. Save changes | Scheduler job edited successfully | high |
| TC-002 | WF-002 | Delete Scheduler Job | User logged in as Admin, Scheduler job exists | 1. Navigate to Manage Scheduler Jobs<br>2. Click Delete on the desired job<br>3. Confirm deletion | Scheduler job deleted successfully | high |
| TC-003 | WF-003 | Start Scheduler | User logged in as Admin | 1. Navigate to Manage Scheduler Jobs<br>2. Toggle Start/Stop Scheduler to Start | Scheduler state toggled successfully | high |
| TC-004 | WF-004 | Edit Global Configuration with valid data | User logged in as Admin, Global configuration exists | 1. Navigate to Global Configuration<br>2. Click Edit on the desired configuration<br>3. Update Enabled status<br>4. Save changes | Global configuration edited successfully | high |
| TC-005 | WF-005 | Delete Global Configuration | User logged in as Admin, Global configuration exists | 1. Navigate to Global Configuration<br>2. Click Delete on the desired configuration<br>3. Confirm deletion | Global configuration deleted successfully | high |
| TC-006 | WF-006 | Edit Code with valid data | User logged in as Admin, Code exists | 1. Navigate to Manage Codes<br>2. Click Edit on the desired code<br>3. Update Name<br>4. Save changes | Code edited successfully | high |
| TC-007 | WF-007 | Deactivate Code | User logged in as Admin, Code exists | 1. Navigate to Manage Codes<br>2. Click Deactivate on the desired code<br>3. Confirm deactivation | Code deactivated successfully | high |
| TC-008 | WF-008 | Submit Manage Data Tables with valid data | User logged in as Admin | 1. Navigate to Manage Data Tables<br>2. Fill in Data Table Name and select Application Table Name<br>3. Add column definitions<br>4. Submit | Data table created successfully | high |
| TC-009 | WF-009 | Approve Audit Trail Entry | User logged in as Admin, Audit trail entry exists with Pending status | 1. Navigate to Audit Trails<br>2. Click Approve on the pending entry | Audit trail entry approved successfully | high |
| TC-010 | WF-010 | Reject Audit Trail Entry | User logged in as Admin, Audit trail entry exists with Pending status | 1. Navigate to Audit Trails<br>2. Click Reject on the pending entry | Audit trail entry rejected successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Edit Scheduler Job with invalid data | User logged in as Admin, Scheduler job exists | 1. Navigate to Manage Scheduler Jobs<br>2. Click Edit on the desired job<br>3. Leave Job Name empty<br>4. Save changes | Error message displayed for invalid Job Name | high |
| TC-012 | WF-002 | Delete non-existent Scheduler Job | User logged in as Admin | 1. Navigate to Manage Scheduler Jobs<br>2. Attempt to click Delete on a non-existent job | Error message displayed for job not found | high |
| TC-013 | WF-003 | Toggle Start/Stop Scheduler when already stopped | User logged in as Admin, Scheduler is currently stopped | 1. Navigate to Manage Scheduler Jobs<br>2. Toggle Start/Stop Scheduler to Start | Scheduler state toggled successfully | medium |
| TC-014 | WF-004 | Edit Global Configuration with invalid data | User logged in as Admin, Global configuration exists | 1. Navigate to Global Configuration<br>2. Click Edit on the desired configuration<br>3. Leave Configuration Name empty<br>4. Save changes | Error message displayed for invalid Configuration Name | high |
| TC-015 | WF-005 | Delete non-existent Global Configuration | User logged in as Admin | 1. Navigate to Global Configuration<br>2. Attempt to click Delete on a non-existent configuration | Error message displayed for configuration not found | high |
| TC-016 | WF-006 | Edit Code with invalid data | User logged in as Admin, Code exists | 1. Navigate to Manage Codes<br>2. Click Edit on the desired code<br>3. Leave Name empty<br>4. Save changes | Error message displayed for invalid Code Name | high |
| TC-017 | WF-007 | Deactivate non-existent Code | User logged in as Admin | 1. Navigate to Manage Codes<br>2. Attempt to click Deactivate on a non-existent code | Error message displayed for code not found | high |
| TC-018 | WF-008 | Submit Manage Data Tables with missing required fields | User logged in as Admin | 1. Navigate to Manage Data Tables<br>2. Leave Data Table Name empty<br>3. Submit | Error message displayed for missing required fields | high |
| TC-019 | WF-009 | Approve already approved Audit Trail Entry | User logged in as Admin, Audit trail entry exists with Approved status | 1. Navigate to Audit Trails<br>2. Click Approve on the approved entry | Error message displayed for entry already approved | high |
| TC-020 | WF-010 | Reject already rejected Audit Trail Entry | User logged in as Admin, Audit trail entry exists with Rejected status | 1. Navigate to Audit Trails<br>2. Click Reject on the rejected entry | Error message displayed for entry already rejected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 | WF-008 | Submit Manage Data Tables with maximum length for Name | User logged in as Admin | 1. Navigate to Manage Data Tables<br>2. Fill in Data Table Name with maximum allowed characters<br>3. Submit | Data table created successfully | medium |
| TC-022 | WF-008 | Submit Manage Data Tables with minimum length for Length field | User logged in as Admin | 1. Navigate to Manage Data Tables<br>2. Fill in Data Table Name and set Length to 1<br>3. Submit | Data table created successfully | medium |
| TC-023 | WF-008 | Submit Manage Data Tables with maximum length for Length field | User logged in as Admin | 1. Navigate to Manage Data Tables<br>2. Fill in Data Table Name and set Length to maximum allowed value<br>3. Submit | Data table created successfully | medium |

---

## Logout

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as regular user, User is on the dashboard | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User is logged out, session is terminated, authentication token is cleared, and redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | User attempts to access authenticated page after logout | User logged out, User tries to access a protected page | 1. Attempt to navigate to a protected page | User is redirected to the login page | high |
| TC-003 | WF-001 | User clicks on 'Log Out' without being logged in | User is not logged in | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | No action is taken, and the user remains on the current page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | User logs out and tries to access the login page | User logged out | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown<br>3. Attempt to navigate to the login page | User is successfully redirected to the login page without errors | low |

---
