# Test Cases — Parabank

Generated: 2026-06-10T20:09:51.903382Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 163 | 25 | 81 | 57 | 96 | 48 | 19 |

## Login

Total: **10** (positive: 1, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User is on the Login page, User logged in as <Role> | 1. Enter <valid email> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Sign In button | Page shows 'Signed in successfully.' and redirects to the Accounts Overview page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email/Username field blank and submit |  | 1. Leave the Email/Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Sign In | Inline validation error appears on the Email/Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Enter <valid email format> in the Email/Username field<br>2. Leave the Password field blank<br>3. Click Sign In | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click Sign In | Form does not submit; error shown on Email/Username field | medium |
| TC-005 |  | Enter a password that does not meet complexity requirements and submit |  | 1. Enter <valid email format> in the Email/Username field<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Form does not submit; error shown on Password field | medium |
| TC-006 | WF-002 | Attempt to log in with incorrect credentials |  | 1. Enter <valid email format> in the Email/Username field<br>2. Enter <incorrect password> in the Password field<br>3. Click Sign In | Page displays 'Incorrect email or password. Please try again.' and the Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Enter exactly 8 characters in the Password field |  | 1. Enter a valid email format in the Email/Username field<br>2. Enter exactly 8 characters (including uppercase, lowercase, number, and special character) in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-008 (boundary) |  | Enter 7 characters in the Password field |  | 1. Enter a valid email format in the Email/Username field<br>2. Enter 7 characters (including uppercase, lowercase, number, and special character) in the Password field<br>3. Click Sign In | Form submission is blocked; error message 'Incorrect email or password. Please try again.' is shown. | medium |
| TC-009 (input_edge) |  | Enter a valid email with leading and trailing spaces |  | 1. Enter '   user@example.com   ' in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Leading/trailing whitespace is trimmed; user is redirected to the Accounts Overview page. | low |
| TC-010 (input_edge) |  | Enter a valid email with special characters |  | 1. Enter 'user+test@example.com' in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | low |

---

## Register

Total: **24** (positive: 1, negative: 17, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Register with valid inputs | User logged in as <Role> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <Street Address> in the Street Address field<br>4. Enter <City> in the City field<br>5. Select <State> from the State dropdown<br>6. Enter <ZIP Code> in the ZIP Code field<br>7. Enter <Phone Number> in the Phone Number field<br>8. Enter <SSN> in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <Password> in the Password field<br>11. Enter <Password> in the Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the First Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Street Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field unselected |  | 1. Leave the State field unselected<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-009 |  | Leave the Social Security Number field blank |  | 1. Leave the Social Security Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social Security Number field indicating it is required | high |
| TC-010 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it is required | high |
| TC-011 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Leave the Confirm Password field blank |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-013 | WF-002 | Enter an invalid Username format |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | high |
| TC-014 | WF-003 | Enter an invalid Phone Number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | high |
| TC-015 | WF-004 | Enter an invalid ZIP Code format |  | 1. Enter <invalid zip code format> in the ZIP Code field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | high |
| TC-016 | WF-005 | Enter an invalid SSN format |  | 1. Enter <invalid ssn format> in the Social Security Number field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | high |
| TC-017 | WF-006 | Enter a short Password |  | 1. Enter <short password> in the Password field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | high |
| TC-018 | WF-007 | Enter mismatched Password and Confirm Password |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Register | Specific field-level errors are displayed for correction | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) |  | Enter exactly 8 characters in the Password field |  | 1. Enter 'abcdefgh' in the Password field<br>2. Enter 'abcdefgh' in the Confirm Password field<br>3. Fill all other required fields<br>4. Click Register | Account created successfully — please sign in | medium |
| TC-020 (boundary) |  | Enter a valid 5-digit ZIP Code |  | 1. Enter '12345' in the ZIP Code field<br>2. Fill all other required fields<br>3. Click Register | Account created successfully — please sign in | medium |
| TC-021 (boundary) |  | Enter a valid 5+4 ZIP Code format |  | 1. Enter '12345-6789' in the ZIP Code field<br>2. Fill all other required fields<br>3. Click Register | Account created successfully — please sign in | medium |
| TC-022 (input_edge) |  | Enter a very long First Name |  | 1. Enter 'JohnJacobJingleheimerSchmidt' in the First Name field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | low |
| TC-023 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter 'user@name!example.com' in the Username field<br>2. Fill all other required fields<br>3. Click Register | Specific field-level errors are displayed for correction | low |
| TC-024 (input_edge) |  | Enter leading/trailing whitespace in the Username field |  | 1. Enter '   user@example.com   ' in the Username field<br>2. Fill all other required fields<br>3. Click Register | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounts Overview

Total: **10** (positive: 5, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display welcome message and accounts table | User logged in as <User> | 1. Navigate to the Accounts Overview dashboard | The dashboard displays a welcome message with the user's name and a table of all customer accounts. | high |
| TC-002 |  | Display account details in the table | User logged in as <User> | 1. Navigate to the Accounts Overview dashboard | The table shows rows with Account Number, Account Type, Current Balance, Account Status, and Open Date. | high |
| TC-003 |  | Display masked account numbers | User logged in as <User> | 1. Navigate to the Accounts Overview dashboard | Account numbers are masked, showing only the last 4 digits as ****5001. | medium |
| TC-004 |  | Display total balance in footer | User logged in as <User> | 1. Navigate to the Accounts Overview dashboard | The footer row displays the total balance across all accounts. | medium |
| TC-005 |  | Order accounts by creation date | User logged in as <User> | 1. Navigate to the Accounts Overview dashboard | Rows are ordered by account creation date (earliest first). | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Unauthenticated user attempts to access the dashboard |  | 1. Navigate to the Accounts Overview page | User is redirected to the login page | high |
| TC-007 |  | Click on Account Number link which is not implemented |  | 1. Navigate to the Accounts Overview page<br>2. Click on the Account Number link | No action occurs; the link does not lead to any details | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long welcome message |  | 1. Enter a welcome message with 200+ characters in the welcome message field | The welcome message is truncated or an error is shown indicating the message is too long | low |
| TC-009 (input_edge) |  | Enter special characters in the account type |  | 1. Enter special characters in the Account Type field | An error is shown indicating invalid characters in the Account Type field | low |
| TC-010 (input_edge) |  | Enter whitespace in the account number |  | 1. Enter leading and trailing whitespace in the Account Number field | The Account Number is trimmed and displayed without extra spaces in the table | low |

---

## Open New Account

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Checking Account with valid deposit | User logged in as <role> | 1. Select 'Checking' from the account type selection cards<br>2. Enter '25' in the Initial Deposit Amount field<br>3. Select a valid funding source account from the Funding Source Account dropdown<br>4. Click 'Open Account' button | Page shows 'Account opened successfully!' and redirects to accounts overview | high |
| TC-002 | WF-002 | Open Savings Account with valid deposit | User logged in as <role> | 1. Select 'Savings' from the account type selection cards<br>2. Enter '100' in the Initial Deposit Amount field<br>3. Select a valid funding source account from the Funding Source Account dropdown<br>4. Click 'Open Account' button | Page shows 'Account opened successfully!' and redirects to accounts overview | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Initial Deposit Amount field blank and submit |  | 1. Select an account type (Checking or Savings)<br>2. Leave the Initial Deposit Amount field blank<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-004 |  | Enter a deposit amount below the minimum for Checking account and submit |  | 1. Select Checking as the account type<br>2. Enter <amount below minimum> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 | high |
| TC-005 |  | Enter a deposit amount below the minimum for Savings account and submit |  | 1. Select Savings as the account type<br>2. Enter <amount below minimum> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 | high |
| TC-006 |  | Select a Funding Source Account with insufficient balance and submit |  | 1. Select Checking as the account type<br>2. Enter $25 in the Initial Deposit Amount field<br>3. Select a Funding Source Account with insufficient balance<br>4. Click Open Account | Inline validation error appears indicating insufficient balance in the selected Funding Source Account | high |
| TC-007 |  | Leave the account type unselected and submit |  | 1. Leave the account type unselected<br>2. Enter $25 in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears indicating that an account type must be selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Open Checking Account with minimum deposit | User is on the Open New Account page, User selects Checking account type | 1. Enter $25 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-009 (boundary) | WF-001 | Open Checking Account with deposit just below minimum | User is on the Open New Account page, User selects Checking account type | 1. Enter $24.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Real-time validation error displays: 'Deposit must be at least $25.' | medium |
| TC-010 (boundary) | WF-002 | Open Savings Account with minimum deposit | User is on the Open New Account page, User selects Savings account type | 1. Enter $100 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-011 (boundary) | WF-002 | Open Savings Account with deposit just below minimum | User is on the Open New Account page, User selects Savings account type | 1. Enter $99.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Real-time validation error displays: 'Deposit must be at least $100.' | medium |

---

## Transfer Funds

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Transfer from My ParaBank Account | User logged in as <Role>, User has sufficient funds in their Checking or Savings account | 1. Select 'My ParaBank Account' as the transfer type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select <valid source account> from the Source Account dropdown<br>4. Click Submit | Transfer completed successfully. | high |
| TC-002 | WF-002 | Transfer from External Account | User logged in as <Role>, User has sufficient funds in their Checking or Savings account | 1. Select 'External Account' as the transfer type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select <valid source account> from the Source Account dropdown<br>4. Enter <valid external account number> in the Account Number field<br>5. Confirm <valid external account number> in the Confirm Account Number field<br>6. Click Submit | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to submit the transfer form with the Transfer Amount field blank |  | 1. Leave the Transfer Amount field blank<br>2. Select a Source Account<br>3. Choose a transfer type<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-004 |  | Attempt to submit the transfer form with insufficient funds |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Select a Source Account with insufficient funds<br>3. Choose a transfer type<br>4. Click Submit | Error displayed: 'Insufficient funds' | high |
| TC-005 |  | Attempt to submit an external transfer with mismatched account numbers |  | 1. Select External Account as the transfer type<br>2. Enter <valid external account number> in the Account Number field<br>3. Enter <different account number> in the Confirm Account Number field<br>4. Enter <valid amount> in the Transfer Amount field<br>5. Click Submit | Error displayed: 'Account numbers do not match.' | high |
| TC-006 |  | Attempt to submit the transfer form with all fields empty |  | 1. Leave the Transfer Amount field blank<br>2. Leave the Source Account dropdown unselected<br>3. Leave the transfer type unselected<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required; Source Account field is highlighted as required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Transfer amount at minimum threshold | User has sufficient funds in the source account | 1. Select 'My ParaBank Account' as the transfer type<br>2. Enter the minimum transfer amount in the Transfer Amount field<br>3. Select a source account from the dropdown<br>4. Select a destination account<br>5. Click Submit | Transfer completed successfully. Transaction ID is displayed. | medium |
| TC-008 (boundary) | WF-001 | Transfer amount just above minimum threshold | User has sufficient funds in the source account | 1. Select 'My ParaBank Account' as the transfer type<br>2. Enter an amount just above the minimum transfer amount in the Transfer Amount field<br>3. Select a source account from the dropdown<br>4. Select a destination account<br>5. Click Submit | Transfer completed successfully. Transaction ID is displayed. | medium |
| TC-009 (boundary) | WF-001 | Transfer amount just below minimum threshold | User has sufficient funds in the source account | 1. Select 'My ParaBank Account' as the transfer type<br>2. Enter an amount just below the minimum transfer amount in the Transfer Amount field<br>3. Select a source account from the dropdown<br>4. Select a destination account<br>5. Click Submit | Transfer is blocked; error message 'Transfer amount is below the minimum required.' is displayed. | medium |
| TC-010 (boundary) | WF-002 | Account number mismatch for external transfer | User selects external transfer type | 1. Select 'External Account' as the transfer type<br>2. Enter an account number in the Account Number field<br>3. Enter a different account number in the Confirm Account Number field<br>4. Enter a valid transfer amount<br>5. Click Submit | Transfer is blocked; error message 'Account numbers do not match.' is displayed. | medium |
| TC-011 (boundary) | WF-002 | Insufficient funds for transfer | User selects external transfer type, User has insufficient funds | 1. Select 'External Account' as the transfer type<br>2. Enter a valid account number in the Account Number field<br>3. Enter the transfer amount that exceeds available funds<br>4. Click Submit | Transfer is blocked; error message 'Insufficient funds' is displayed. | medium |

---

## Payments

Total: **9** (positive: 1, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with valid details | User logged in as <role>, Sufficient funds are available | 1. Enter <Payee Name> in the Payee Name field<br>2. Enter <Street Address> in the Street Address field<br>3. Enter <City> in the City field<br>4. Select <State> from the State dropdown<br>5. Enter <ZIP Code> in the ZIP Code field<br>6. Enter <Phone Number> in the Phone Number field<br>7. Enter <Payee Account Number> in the Payee Account Number field<br>8. Enter <Payee Account Number> in the Confirm Account Number field<br>9. Enter <Payment Amount> in the Payment Amount field<br>10. Select <Source Account> from the Source Account dropdown<br>11. Click Pay | Payment submitted successfully with a reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Payee Name field blank and submit |  | 1. Leave the Payee Name field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee Name field indicating it is required | high |
| TC-003 |  | Leave the Payment Amount field blank and submit |  | 1. Leave the Payment Amount field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payment Amount field indicating it is required | high |
| TC-004 |  | Enter <invalid format> in the Phone Number field and submit |  | 1. Enter <invalid format> in the Phone Number field<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Phone Number field indicating it must be a valid phone number | medium |
| TC-005 |  | Enter <amount exceeding available balance> in the Payment Amount field and submit |  | 1. Enter <amount exceeding available balance> in the Payment Amount field<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |
| TC-006 |  | Enter mismatched values in Payee Account Number and Confirm Account Number fields and submit |  | 1. Enter <valid account number> in the Payee Account Number field<br>2. Enter <different account number> in the Confirm Account Number field<br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears indicating 'Account numbers do not match' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long Payee Name |  | 1. Enter a string of 200+ characters in the Payee Name field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Form submits successfully; Payee Name is displayed correctly on the confirmation page. | low |
| TC-008 (input_edge) |  | Enter special characters in Street Address |  | 1. Enter special characters in the Street Address field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Form submits successfully; Street Address is displayed correctly on the confirmation page. | low |
| TC-009 (input_edge) |  | Enter value with leading/trailing whitespace in Phone Number |  | 1. Enter '   123-456-7890   ' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Leading/trailing whitespace is trimmed; saved value shown on the confirmation page has no extra spaces. | low |

---

## Request Loan

Total: **17** (positive: 3, negative: 5, edge: 9)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Request a Personal Loan | User logged in as <Role> | 1. Select 'Personal' from the loan type cards<br>2. Enter 10000 in the Loan Amount field<br>3. Enter 1000 in the Down Payment Amount field<br>4. Select a valid account from the Collateral Account dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-002 | WF-002 | Request an Auto Loan | User logged in as <Role> | 1. Select 'Auto' from the loan type cards<br>2. Enter 20000 in the Loan Amount field<br>3. Enter 2000 in the Down Payment Amount field<br>4. Select a valid account from the Collateral Account dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-003 | WF-003 | Request a Home Loan | User logged in as <Role> | 1. Select 'Home' from the loan type cards<br>2. Enter 100000 in the Loan Amount field<br>3. Enter 20000 in the Down Payment Amount field<br>4. Select a valid account from the Collateral Account dropdown<br>5. Click Submit | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Loan Amount field blank and submit |  | 1. Select Personal Loan type<br>2. Leave the Loan Amount field blank<br>3. Fill Down Payment Amount and Collateral Account<br>4. Click Submit | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Enter Down Payment Amount greater than Loan Amount |  | 1. Select Auto Loan type<br>2. Enter <amount greater than Loan Amount> in the Loan Amount field<br>3. Enter <amount greater than Loan Amount> in the Down Payment Amount field<br>4. Fill Collateral Account<br>5. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it must be less than Loan Amount | high |
| TC-006 |  | Enter insufficient collateral funds |  | 1. Select Home Loan type<br>2. Enter <amount within Home Loan range> in the Loan Amount field<br>3. Enter <amount less than 20% of Loan Amount> in the Down Payment Amount field<br>4. Fill Collateral Account with insufficient funds<br>5. Click Submit | Loan is not approved; error shown indicating 'Inadequate collateral value' | high |
| TC-007 |  | Enter a Loan Amount below minimum for Personal Loan |  | 1. Select Personal Loan type<br>2. Enter <amount below $1,000> in the Loan Amount field<br>3. Fill Down Payment Amount and Collateral Account<br>4. Click Submit | Inline validation error appears on the Loan Amount field indicating it must be at least $1,000 | high |
| TC-008 |  | Enter a Loan Amount above maximum for Auto Loan |  | 1. Select Auto Loan type<br>2. Enter <amount above $75,000> in the Loan Amount field<br>3. Fill Down Payment Amount and Collateral Account<br>4. Click Submit | Inline validation error appears on the Loan Amount field indicating it must not exceed $75,000 | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Test minimum loan amount for Personal loan | User selects Personal loan type | 1. Enter $1,000 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-010 (boundary) | WF-001 | Test maximum loan amount for Personal loan | User selects Personal loan type | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-011 (boundary) | WF-001 | Test loan amount exceeding maximum for Personal loan | User selects Personal loan type | 1. Enter $50,001 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan request is blocked; error shown for exceeding maximum loan amount. | medium |
| TC-012 (boundary) | WF-002 | Test minimum loan amount for Auto loan | User selects Auto loan type | 1. Enter $5,000 in the Loan Amount field<br>2. Enter $500 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-013 (boundary) | WF-002 | Test maximum loan amount for Auto loan | User selects Auto loan type | 1. Enter $75,000 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-014 (boundary) | WF-002 | Test loan amount exceeding maximum for Auto loan | User selects Auto loan type | 1. Enter $75,001 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan request is blocked; error shown for exceeding maximum loan amount. | medium |
| TC-015 (boundary) | WF-003 | Test minimum loan amount for Home loan | User selects Home loan type | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $10,000 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-016 (boundary) | WF-003 | Test maximum loan amount for Home loan | User selects Home loan type | 1. Enter $500,000 in the Loan Amount field<br>2. Enter $100,000 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-017 (boundary) | WF-003 | Test loan amount exceeding maximum for Home loan | User selects Home loan type | 1. Enter $500,001 in the Loan Amount field<br>2. Enter $100,000 in the Down Payment Amount field<br>3. Select a collateral account<br>4. Click Submit | Loan request is blocked; error shown for exceeding maximum loan amount. | medium |

---

## Update Contact Info

Total: **12** (positive: 1, negative: 8, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit profile update with valid data | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click the Update Profile button | Profile updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the First Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Street Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the ZIP Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Inline validation error appears on the First Name, Last Name, Street Address, City, State, ZIP Code, and Phone Number fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields<br>3. Click Update Profile | Inline error shown indicating the First Name exceeds the maximum allowed length. | low |
| TC-011 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter special characters (e.g., @#$%) in the Last Name field<br>2. Fill all other required fields<br>3. Click Update Profile | Inline error shown indicating invalid characters in the Last Name field. | low |
| TC-012 (input_edge) |  | Enter a phone number with leading/trailing whitespace |  | 1. Enter '   123-456-7890   ' in the Phone Number field<br>2. Fill all other required fields<br>3. Click Update Profile | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Manage Cards

Total: **14** (positive: 2, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Request a new card with valid details | User logged in as <Role> | 1. Select <Card Type> from the Card Type dropdown<br>2. Select <Account to Link> from the Account dropdown<br>3. Enter a complete Shipping Address in the Shipping Address field<br>4. Click Request Card | Card request submitted successfully. Tracking ID shown. | high |
| TC-002 | WF-002 | Update card controls with valid details | User logged in as <Role> | 1. Select <Existing Card> from the Select Existing Card dropdown<br>2. Enter <New Spending Limit> in the New Spending Limit field<br>3. Enter <optional dates> in the Travel Notice fields<br>4. Select <Card Status> from the Card Status dropdown<br>5. Click Update Controls | Card controls updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Card Type field blank and submit |  | 1. Leave the Card Type field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Card Type field indicating it is required | high |
| TC-004 |  | Leave the Account to Link field blank and submit |  | 1. Leave the Account to Link field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-005 |  | Leave the Shipping Address field blank and submit |  | 1. Leave the Shipping Address field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating it is required | high |
| TC-006 |  | Submit the card request form with all fields empty |  | 1. Leave all fields in the card request form blank<br>2. Click Request Card | Inline validation error appears on the Card Type, Account to Link, and Shipping Address fields indicating they are required | high |
| TC-007 |  | Enter a non-numeric value in the New Spending Limit field and submit |  | 1. Enter <non-numeric value> in the New Spending Limit field<br>2. Fill all other required fields<br>3. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating it must be a number | medium |
| TC-008 |  | Enter an invalid date range in the Travel Notice fields and submit |  | 1. Enter <end date before start date> in the Travel Notice fields<br>2. Fill all other required fields<br>3. Click Update Controls | Inline validation error appears on the Travel Notice fields indicating the end date must be after the start date | medium |
| TC-009 |  | Select an invalid Card Status transition and submit |  | 1. Select <current status> in the Select Existing Card dropdown<br>2. Select <invalid status> in the Card Status field<br>3. Fill all other required fields<br>4. Click Update Controls | Inline validation error appears on the Card Status field indicating the status transition is not allowed | medium |
| TC-010 |  | Attempt to update controls without filling required fields |  | 1. Open the Update Controls form<br>2. Leave all required fields blank<br>3. Click Update Controls | Inline validation error appears on the required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Submit card request with incomplete address | User is on the Manage Cards page | 1. Select 'Debit' as Card Type<br>2. Select an Account to Link<br>3. Leave Shipping Address blank<br>4. Click 'Request Card' | Form submission is blocked; inline error shows 'Shipping Address is required.' | medium |
| TC-012 (boundary) | WF-002 | Update controls with spending limit at policy maximum | User is on the Manage Cards page, User has an existing card | 1. Select an Existing Card from the dropdown<br>2. Enter the maximum allowed New Spending Limit<br>3. Click 'Update Controls' | Card controls updated successfully. | medium |
| TC-013 (boundary) | WF-002 | Update controls with spending limit above policy maximum | User is on the Manage Cards page, User has an existing card | 1. Select an Existing Card from the dropdown<br>2. Enter a New Spending Limit above the maximum allowed<br>3. Click 'Update Controls' | Form submission is blocked; inline error shows 'Spending limit exceeds policy maximum.' | medium |
| TC-014 (boundary) | WF-002 | Update controls with invalid travel notice dates | User is on the Manage Cards page, User has an existing card | 1. Select an Existing Card from the dropdown<br>2. Enter New Spending Limit<br>3. Enter a Travel Notice start date in the past<br>4. Click 'Update Controls' | Form submission is blocked; inline error shows 'Travel notice start date cannot be in the past.' | medium |

---

## Investments

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Execute a successful trade | User logged in as <Investor>, Sufficient buying power is available | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '10' in the Quantity field<br>3. Select <Funding Account> from the Funding Account dropdown<br>4. Click 'Execute Trade' | Trade executed successfully. Order ID is displayed. | high |
| TC-002 |  | Create a successful recurring investment plan | User logged in as <Investor>, Sufficient balance in the funding account | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Weekly' from the Frequency dropdown<br>4. Enter a future date in the Start Date field<br>5. Select <Funding Account> from the Funding Account dropdown<br>6. Click 'Create Plan' | Plan created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Quantity field blank and submit the trade funds form |  | 1. Leave the Quantity field blank<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-004 |  | Enter a negative value in the Quantity field and submit the trade funds form |  | 1. Enter <negative quantity> in the Quantity field<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it must be greater than zero | high |
| TC-005 |  | Select a funding account with insufficient balance and submit the recurring investment plan form |  | 1. Fill all fields in the recurring investment plan form<br>2. Select a funding account with insufficient balance<br>3. Click Create Plan | Inline validation error appears on the Funding Account field indicating insufficient balance | high |
| TC-006 |  | Enter a past date in the Start Date field and submit the recurring investment plan form |  | 1. Enter <past date> in the Start Date field<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Start Date field indicating 'Start date must be in the future' | high |
| TC-007 |  | Submit the trade funds form with all fields empty |  | 1. Leave all fields in the trade funds form blank<br>2. Click Execute Trade | Inline validation errors appear on the Action, Fund Symbol, Quantity, and Funding Account fields indicating they are required | high |
| TC-008 |  | Enter an invalid Fund Symbol in the trade funds form and submit |  | 1. Enter <invalid fund symbol> in the Fund Symbol field<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating it does not exist | high |
| TC-009 |  | Enter a contribution amount below the minimum in the recurring investment plan form and submit |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it must meet the minimum | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Check trade quantity at minimum valid boundary | User has sufficient buying power | 1. Select 'Buy' in the Action field<br>2. Enter a valid Fund Symbol in the Fund Symbol field<br>3. Enter '1' in the Quantity field<br>4. Select a Funding Account from the dropdown<br>5. Click 'Execute Trade' | Trade executed successfully. with an order ID displayed | medium |
| TC-011 (boundary) |  | Check trade quantity below minimum valid boundary | User has sufficient buying power | 1. Select 'Buy' in the Action field<br>2. Enter a valid Fund Symbol in the Fund Symbol field<br>3. Enter '0' in the Quantity field<br>4. Select a Funding Account from the dropdown<br>5. Click 'Execute Trade' | Inline error displayed indicating quantity must be greater than zero | medium |
| TC-012 (boundary) |  | Check recurring investment plan start date in the future | User has sufficient funding account balance | 1. Enter a valid Fund Symbol in the Fund Symbol field<br>2. Enter a valid contribution amount meeting the minimum<br>3. Select 'Weekly' in the Frequency field<br>4. Enter tomorrow's date in the Start Date field<br>5. Select a Funding Account from the dropdown<br>6. Click 'Create Plan' | Plan created successfully. | medium |
| TC-013 (boundary) |  | Check recurring investment plan start date not in the future | User has sufficient funding account balance | 1. Enter a valid Fund Symbol in the Fund Symbol field<br>2. Enter a valid contribution amount meeting the minimum<br>3. Select 'Weekly' in the Frequency field<br>4. Enter yesterday's date in the Start Date field<br>5. Select a Funding Account from the dropdown<br>6. Click 'Create Plan' | Inline error displayed indicating 'Start date must be in the future' | medium |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate statement with valid date range | User logged in as <role> | 1. Enter <valid month-and-year or custom date range> in the Statement Period field<br>2. Select <valid account> from the Account dropdown<br>3. Click Generate Statement | Statement generated successfully. | high |
| TC-002 | WF-003 | Save e-statement preference with valid email | User logged in as <role> | 1. Check the checkbox for paperless statements<br>2. Enter <valid email address> in the Email Address field<br>3. Click Save Preference | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Check the checkbox for paperless statements<br>3. Click Save Preference | Email Address field displays an error: 'Email address is required' | high |
| TC-004 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email Address field<br>2. Check the checkbox for paperless statements<br>3. Click Save Preference | Email Address field displays an error: 'Must be a valid email address' | high |
| TC-005 |  | Leave the Statement Period field blank and submit |  | 1. Leave the Statement Period field blank<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Statement Period field displays an error: 'Statement period is required' | high |
| TC-006 |  | Attempt to generate statement with invalid date range |  | 1. Enter <invalid date range> in the Statement Period field<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Unable to generate statement — please try again later. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Generate statement with end date equal to start date |  | 1. Select a month-and-year for the Statement Period.<br>2. Enter the same date for both start and end date.<br>3. Select an Account from the dropdown.<br>4. Click Generate Statement. | Statement generated successfully. | medium |
| TC-008 (boundary) | WF-002 | Generate statement with end date one day before start date |  | 1. Select a month-and-year for the Statement Period.<br>2. Enter an end date that is one day before the start date.<br>3. Select an Account from the dropdown.<br>4. Click Generate Statement. | Unable to generate statement — please try again later. | medium |
| TC-009 (input_edge) | WF-003 | Save e-statement preference with email containing special characters |  | 1. Enter an email address with special characters (e.g., 'user@domain!com') in the Email Address field.<br>2. Check the checkbox for paperless statements.<br>3. Click Save Preference. | Email field highlighted with guidance. | low |
| TC-010 (input_edge) | WF-004 | Save e-statement preference with email address at maximum length |  | 1. Enter an email address with maximum allowed length in the Email Address field.<br>2. Check the checkbox for paperless statements.<br>3. Click Save Preference. | e-Statement preference updated. | low |

---

## Security Settings

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Change Password with valid inputs | User logged in as <role> | 1. Navigate to the Security Settings page<br>2. Enter <valid current password> in the Current Password field<br>3. Enter <valid new password> in the New Password field<br>4. Enter <valid new password> in the Confirm New Password field<br>5. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Current Password field blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 |  | Leave the New Password field blank and submit |  | 1. Enter a valid Current Password<br>2. Leave the New Password field blank<br>3. Fill Confirm New Password with a valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 |  | Leave the Confirm New Password field blank and submit |  | 1. Enter a valid Current Password<br>2. Fill New Password with a valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 |  | Enter a weak New Password and submit |  | 1. Enter a valid Current Password<br>2. Enter <weak password> in the New Password field<br>3. Fill Confirm New Password with the same weak password<br>4. Click Change Password | Validation errors highlight the appropriate fields; New Password field displays an error: 'Password does not meet strong-password policy' | high |
| TC-006 |  | Enter non-matching New Password and Confirm New Password and submit |  | 1. Enter a valid Current Password<br>2. Enter <valid new password> in the New Password field<br>3. Enter <different password> in the Confirm New Password field<br>4. Click Change Password | Validation errors highlight the appropriate fields; Confirm New Password field displays an error: 'Passwords do not match' | high |
| TC-007 |  | Enter an invalid Current Password and submit |  | 1. Enter <invalid current password> in the Current Password field<br>2. Enter a valid New Password<br>3. Fill Confirm New Password with the same valid New Password<br>4. Click Change Password | Validation errors highlight the appropriate fields; Current Password field displays an error: 'Current Password is invalid' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Test minimum length for New Password | User is on the Security Settings page | 1. Enter valid Current Password in the Current Password field<br>2. Enter exactly <minimum length> characters in the New Password field<br>3. Enter the same <minimum length> characters in the Confirm New Password field<br>4. Click Change Password | Form submits successfully; password is changed as per the strong-password policy | medium |
| TC-009 (boundary) |  | Test one character below minimum length for New Password | User is on the Security Settings page | 1. Enter valid Current Password in the Current Password field<br>2. Enter <minimum length - 1> characters in the New Password field<br>3. Enter the same <minimum length - 1> characters in the Confirm New Password field<br>4. Click Change Password | Validation errors highlight the New Password and Confirm New Password fields indicating the password is too short | medium |
| TC-010 (input_edge) |  | Test long string input for Current Password | User is on the Security Settings page | 1. Enter a long string (200+ characters) in the Current Password field<br>2. Enter valid New Password in the New Password field<br>3. Enter the same valid New Password in the Confirm New Password field<br>4. Click Change Password | Validation errors highlight the Current Password field indicating the input is too long | low |
| TC-011 (input_edge) |  | Test special characters in New Password | User is on the Security Settings page | 1. Enter valid Current Password in the Current Password field<br>2. Enter a New Password with special characters in the New Password field<br>3. Enter the same New Password with special characters in the Confirm New Password field<br>4. Click Change Password | Form submits successfully; password is changed as special characters are allowed | low |

---

## Support Center

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send a message with valid input | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select <valid category> from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. (Optional) Attach a <valid file type><br>5. Click Send Message | Message sent successfully. with a ticket ID | high |
| TC-002 | WF-002 | Request a callback with valid input | User logged in as <Role> | 1. Select <valid reason for call> from the Reason for Call dropdown<br>2. Enter <next business day> in the Preferred Date field<br>3. Select <valid time window> from the Preferred Time Window dropdown<br>4. Verify Phone Number field is pre-filled and editable<br>5. Click Request Callback | Callback request submitted. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Subject field blank and submit the message form |  | 1. Leave the Subject field blank<br>2. Fill in the Category, Message Body, and Attachment fields with valid data<br>3. Click Send Message | Inline validation error appears on the Subject field indicating it is required | high |
| TC-004 |  | Leave the Message Body field blank and submit the message form |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject, Category, and Attachment fields with valid data<br>3. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-005 |  | Select an invalid attachment type and submit the message form |  | 1. Fill in the Subject, Category, and Message Body fields with valid data<br>2. Attach a file with an invalid type<br>3. Click Send Message | Inline validation error appears indicating the attachment type is not allowed | high |
| TC-006 |  | Select a Preferred Date that is not the next business day and submit the callback form |  | 1. Select a Preferred Date that is today<br>2. Fill in the Reason for Call, Preferred Time Window, and Phone Number fields with valid data<br>3. Click Request Callback | Inline validation error appears on the Preferred Date field indicating it must be at least the next business day | high |
| TC-007 |  | Enter an invalid phone number format and submit the callback form |  | 1. Fill in the Reason for Call, Preferred Date, and Preferred Time Window fields with valid data<br>2. Enter an invalid phone number in the Phone Number field<br>3. Click Request Callback | Inline validation error appears on the Phone Number field indicating it must be a valid phone number format | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Test subject length at minimum allowed characters |  | 1. Select 'Account' from the Category dropdown<br>2. Enter exactly <minimum allowed length> characters in the Subject field<br>3. Enter valid content in the Message Body<br>4. Click 'Send Message' | Form submits successfully; entity is created with the <minimum allowed length> | medium |
| TC-009 (boundary) | WF-001 | Test subject length below minimum allowed characters |  | 1. Select 'Technical' from the Category dropdown<br>2. Enter <one unit below minimum> characters in the Subject field<br>3. Enter valid content in the Message Body<br>4. Click 'Send Message' | Subject displays an error indicating the value is below the minimum allowed | medium |
| TC-010 (boundary) | WF-002 | Test preferred date at minimum allowed (next business day) |  | 1. Select a Reason for Call from the dropdown<br>2. Enter the next business day in the Preferred Date field<br>3. Enter valid time in the Preferred Time Window<br>4. Enter a valid Phone Number<br>5. Click 'Request Callback' | Callback request submitted. | medium |
| TC-011 (boundary) | WF-002 | Test preferred date below minimum allowed (today) |  | 1. Select a Reason for Call from the dropdown<br>2. Enter today's date in the Preferred Date field<br>3. Enter valid time in the Preferred Time Window<br>4. Enter a valid Phone Number<br>5. Click 'Request Callback' | Preferred Date displays an error indicating it must be at least the next business day | medium |

---
