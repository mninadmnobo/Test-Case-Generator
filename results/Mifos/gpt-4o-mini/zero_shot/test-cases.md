# Test Cases — 

Generated:   
Model:   

## Mifos

Total: **10** (positive: 3, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful login with valid credentials | User is on the login page, User has valid credentials | 1. Select a tenant from the dropdown<br>2. Enter a valid username<br>3. Enter a valid password<br>4. Click the Login button | User is redirected to the Dashboard page | high |
| TC005 |  | Access Dashboard after successful login | User is logged in and on the Home page | 1. Click the Dashboard button | User is redirected to the Dashboard page displaying client trends and summary cards | high |
| TC008 |  | Create a new client successfully | User is logged in, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in all required fields in the multi-step wizard<br>3. Click Submit | New client is created and displayed in the client list with Pending status | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Login attempt with invalid credentials | User is on the login page | 1. Select a tenant from the dropdown<br>2. Enter an invalid username<br>3. Enter an invalid password<br>4. Click the Login button | An error message is displayed indicating invalid credentials | high |
| TC003 |  | Login attempt with empty required fields | User is on the login page | 1. Leave the username and password fields empty<br>2. Click the Login button | Inline validation messages are displayed for empty fields | high |
| TC006 |  | Global search with no input | User is logged in | 1. Click the global search icon<br>2. Leave the search input empty<br>3. Press Enter | No results found message is displayed | medium |
| TC009 |  | Create a new client with missing required fields | User is logged in, User is on the Clients page | 1. Click the Create Client button<br>2. Leave required fields empty<br>3. Click Submit | Inline validation messages are displayed for missing required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC004 |  | Login attempt with maximum length username and password | User is on the login page | 1. Enter a username with maximum allowed length<br>2. Enter a password with maximum allowed length<br>3. Click the Login button | User is redirected to the Dashboard page if credentials are valid | medium |
| TC007 |  | Global search with special characters | User is logged in | 1. Click the global search icon<br>2. Enter special characters in the search input<br>3. Press Enter | No results found message is displayed or appropriate handling of special characters | medium |
| TC010 |  | Create a new client with maximum length fields | User is logged in, User is on the Clients page | 1. Click the Create Client button<br>2. Fill in all fields with maximum allowed length<br>3. Click Submit | New client is created successfully if all validations pass | medium |

---
