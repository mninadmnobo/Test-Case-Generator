# Test Cases — 

Generated:   
Model:   

## Mifos

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Login with valid credentials | User is on the login page, User has valid username and password | 1. Select 'default' from the Tenant dropdown<br>2. Enter valid <username> in the Username field<br>3. Enter valid <password> in the Password field<br>4. Click the Login button | User is redirected to the Home page with a welcome message | high |
| P-002 |  | Create a new client with valid details | User logged in as Admin, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in all required fields in the Create Client form<br>3. Click Submit | A new client is created and appears in the Clients list with Pending status | high |
| P-003 |  | Activate a Pending client with a valid activation date | User logged in as Admin, A client exists in Pending status | 1. Navigate to the Client Detail page of a Pending client<br>2. Click the Activate button<br>3. Enter <valid activation date> in the Activation Date field<br>4. Click Submit | Client status badge updates to 'Active' (green chip) on the Client Detail page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Login with invalid credentials | User is on the login page | 1. Select 'default' from the Tenant dropdown<br>2. Enter invalid <username> in the Username field<br>3. Enter invalid <password> in the Password field<br>4. Click the Login button | An error message is displayed indicating invalid credentials | high |
| N-002 |  | Create a new client with missing required fields | User logged in as Admin, User is on the Clients page | 1. Click the Create Client button<br>2. Leave the First Name and Last Name fields empty<br>3. Click Submit | Inline validation messages appear indicating required fields are missing | high |
| N-003 |  | Attempt to activate a Pending client with an invalid activation date | User logged in as Admin, A client exists in Pending status | 1. Navigate to the Client Detail page of a Pending client<br>2. Click the Activate button<br>3. Enter <invalid activation date> in the Activation Date field<br>4. Click Submit | An error message is displayed indicating the activation date is invalid | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Login with empty fields | User is on the login page | 1. Select 'default' from the Tenant dropdown<br>2. Leave the Username field empty<br>3. Leave the Password field empty<br>4. Click the Login button | Inline validation messages appear indicating required fields are empty | high |
| E-002 |  | Create a new client with maximum length fields | User logged in as Admin, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in the First Name and Last Name fields with maximum allowed characters<br>3. Click Submit | A new client is created successfully with maximum length names | medium |
| E-003 |  | Activate a Pending client with an activation date before submission date | User logged in as Admin, A client exists in Pending status | 1. Navigate to the Client Detail page of a Pending client<br>2. Click the Activate button<br>3. Enter a date that is before the submission date in the Activation Date field<br>4. Click Submit | An error message is displayed indicating the activation date cannot be before the submission date | high |

---
