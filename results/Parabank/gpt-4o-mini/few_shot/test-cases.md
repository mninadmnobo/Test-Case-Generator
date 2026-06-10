# Test Cases — 

Generated:   
Model:   

## Parabank

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Successful login with valid credentials | User has a registered account with valid email and password | 1. Navigate to the login page<br>2. Enter valid Email/Username in the input field<br>3. Enter valid Password in the input field<br>4. Click the Sign In button | Page shows 'Signed in successfully.' and redirects to Accounts Overview | high |
| P-002 |  | Successful account registration with valid details | User is on the registration page | 1. Fill in First Name, Last Name, Street Address, City, State, ZIP Code, Phone Number, Social Security Number, Username, Password, and Confirm Password with valid data<br>2. Click the Register button | Page shows 'Account created successfully — please sign in.' and redirects to the login page | high |
| P-003 |  | Open a Checking account with valid initial deposit | User logged in, A funding account with sufficient balance exists | 1. Navigate to Open New Account<br>2. Select Checking account type<br>3. Enter 25 in the Initial Deposit Amount field<br>4. Select a funding account from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Checking account appears | high |
| P-004 |  | Transfer funds between two internal ParaBank accounts | User logged in, At least two Checking or Savings accounts exist with sufficient balance | 1. Navigate to Transfer Funds from the left-hand menu<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter <transfer amount> in the Transfer Amount field<br>4. Select <source account> from the Source Account dropdown<br>5. Select <destination account> from the destination dropdown<br>6. Click Transfer | Page shows 'Transfer completed successfully.' with a transaction ID; navigating to Accounts Overview shows the source account balance decreased and the destination account balance increased by the transfer amount | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Attempt login with invalid credentials | User is on the login page | 1. Enter invalid Email/Username in the input field<br>2. Enter invalid Password in the input field<br>3. Click the Sign In button | An error message 'Incorrect email or password. Please try again.' is displayed; password field is cleared | high |
| N-002 |  | Attempt registration with invalid email format | User is on the registration page | 1. Fill in First Name, Last Name, Street Address, City, State, ZIP Code, Phone Number, Social Security Number, and an invalid email format in the Username field<br>2. Enter valid Password and Confirm Password<br>3. Click the Register button | An error message indicating invalid email format is displayed | high |
| N-003 |  | Attempt to open a Checking account with insufficient initial deposit | User logged in, A funding account with insufficient balance exists | 1. Navigate to Open New Account<br>2. Select Checking account type<br>3. Enter an amount less than 25 in the Initial Deposit Amount field<br>4. Select a funding account from the Funding Source Account dropdown<br>5. Click Open Account | An error message indicating insufficient deposit amount is displayed | high |
| N-004 |  | Attempt a fund transfer with an amount exceeding the source account balance | User logged in, A Checking or Savings account exists with a known balance | 1. Navigate to Transfer Funds<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter an amount greater than the source account balance<br>4. Select the source and a destination account<br>5. Click Transfer | An error message 'Insufficient funds' is displayed; no transfer is processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Login with email at maximum length | User has a registered account with maximum length email | 1. Navigate to the login page<br>2. Enter an email with maximum allowed length in the Email/Username field<br>3. Enter valid Password in the input field<br>4. Click the Sign In button | Page shows 'Signed in successfully.' and redirects to Accounts Overview | medium |
| E-002 |  | Registration with maximum length for First Name and Last Name | User is on the registration page | 1. Fill in First Name and Last Name with maximum allowed length<br>2. Fill in valid Street Address, City, State, ZIP Code, Phone Number, Social Security Number, Username, Password, and Confirm Password<br>3. Click the Register button | Page shows 'Account created successfully — please sign in.' and redirects to the login page | medium |
| E-003 |  | Open a Savings account with the exact minimum deposit amount | User logged in, A funding account with at least $100 exists | 1. Navigate to Open New Account<br>2. Select Savings account type<br>3. Enter exactly 100 in the Initial Deposit Amount field<br>4. Select a funding account from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Savings account appears | medium |
| E-004 |  | Transfer funds with a transfer amount of zero | User logged in, At least two Checking or Savings accounts exist | 1. Navigate to Transfer Funds<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter 0 in the Transfer Amount field<br>4. Select <source account> from the Source Account dropdown<br>5. Select <destination account> from the destination dropdown<br>6. Click Transfer | An error message indicating that the transfer amount must be greater than zero is displayed | medium |

---
