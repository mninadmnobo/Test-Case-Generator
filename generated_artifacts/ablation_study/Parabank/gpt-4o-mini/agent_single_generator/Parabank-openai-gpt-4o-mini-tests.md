# Test Cases — Parabank

Generated: 2026-06-09T10:39:19.187010Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 100 | 26 | 50 | 24 | 71 | 26 | 3 |

## Login

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User is registered, User is on the login page | 1. Enter a valid email address.<br>2. Enter a valid password.<br>3. Click on 'Sign In' button. | User is redirected to the Accounts Overview page with message 'Signed in successfully.' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Failed login attempt with incorrect password | User is registered, User is on the login page | 1. Enter a valid email address.<br>2. Enter an incorrect password.<br>3. Click on 'Sign In' button. | Error message 'Incorrect email or password. Please try again.' is displayed, and the password field is cleared. | high |
| TC-003 | WF-002 | Failed login attempt with invalid email format | User is on the login page | 1. Enter an invalid email format.<br>2. Enter a valid password.<br>3. Click on 'Sign In' button. | Error message 'Incorrect email or password. Please try again.' is displayed, and the password field is cleared. | medium |
| TC-004 | WF-002 | Failed login attempt with empty fields | User is on the login page | 1. Leave the email field empty.<br>2. Leave the password field empty.<br>3. Click on 'Sign In' button. | Error message 'Incorrect email or password. Please try again.' is displayed, and the password field is cleared. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Valid password with maximum length | User is registered, User is on the login page | 1. Enter a valid email address.<br>2. Enter a password with exactly 20 characters including uppercase, lowercase, number, and special character.<br>3. Click on 'Sign In' button. | User is redirected to the Accounts Overview page with message 'Signed in successfully.' | low |
| TC-006 | WF-001 | Valid password with minimum length | User is registered, User is on the login page | 1. Enter a valid email address.<br>2. Enter a password with exactly 8 characters including uppercase, lowercase, number, and special character.<br>3. Click on 'Sign In' button. | User is redirected to the Accounts Overview page with message 'Signed in successfully.' | low |
| TC-007 | WF-001 | Invalid password without special character | User is registered, User is on the login page | 1. Enter a valid email address.<br>2. Enter a password without a special character but meets other criteria.<br>3. Click on 'Sign In' button. | Error message 'Incorrect email or password. Please try again.' is displayed, and the password field is cleared. | medium |

---

## Register

Total: **8** (positive: 1, negative: 6, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid inputs | User is on the registration page, User is not logged in | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter a valid ZIP Code (12345)<br>7. Enter a valid Phone Number ((123) 456-7890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (at least 8 characters)<br>11. Enter the same Password in Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Registration fails with missing First Name | User is on the registration page, User is not logged in | 1. Leave First Name field empty<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter a valid ZIP Code (12345)<br>7. Enter a valid Phone Number ((123) 456-7890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (at least 8 characters)<br>11. Enter the same Password in Confirm Password field<br>12. Click the Register button | Error message indicating First Name is required | high |
| TC-003 | WF-001 | Registration fails with invalid ZIP Code format | User is on the registration page, User is not logged in | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter an invalid ZIP Code (1234)<br>7. Enter a valid Phone Number ((123) 456-7890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (at least 8 characters)<br>11. Enter the same Password in Confirm Password field<br>12. Click the Register button | Error message indicating ZIP Code format is invalid | high |
| TC-004 | WF-001 | Registration fails with mismatched Password and Confirm Password | User is on the registration page, User is not logged in | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter a valid ZIP Code (12345)<br>7. Enter a valid Phone Number ((123) 456-7890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (Password123)<br>11. Enter a different Password in Confirm Password field (Password456)<br>12. Click the Register button | Error message indicating Passwords do not match | high |
| TC-005 | WF-001 | Registration fails with invalid Phone Number format | User is on the registration page, User is not logged in | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter valid ZIP Code (12345)<br>7. Enter an invalid Phone Number (1234567890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (at least 8 characters)<br>11. Enter the same Password in Confirm Password field<br>12. Click the Register button | Error message indicating Phone Number format is invalid | high |
| TC-006 | WF-001 | Registration fails with empty form submission | User is on the registration page, User is not logged in | 1. Leave all fields empty<br>2. Click the Register button | Error messages indicating all fields are required | high |
| TC-007 | WF-001 | Registration fails with too short Password | User is on the registration page, User is not logged in | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter valid Street Address<br>4. Enter valid City<br>5. Select a valid State from dropdown<br>6. Enter valid ZIP Code (12345)<br>7. Enter valid Phone Number ((123) 456-7890)<br>8. Enter valid Social Security Number (123-45-6789)<br>9. Enter valid Username (user@example.com)<br>10. Enter a short Password (123)<br>11. Enter the same short Password in Confirm Password field<br>12. Click the Register button | Error message indicating Password must be at least 8 characters | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Registration with maximum length inputs | User is on the registration page, User is not logged in | 1. Enter First Name with maximum length (50 characters)<br>2. Enter Last Name with maximum length (50 characters)<br>3. Enter Street Address with maximum length (100 characters)<br>4. Enter City with maximum length (50 characters)<br>5. Select a valid State from dropdown<br>6. Enter a valid ZIP Code (12345)<br>7. Enter a valid Phone Number ((123) 456-7890)<br>8. Enter a valid Social Security Number (123-45-6789)<br>9. Enter a valid Username (user@example.com)<br>10. Enter a valid Password (at least 8 characters)<br>11. Enter the same Password in Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | medium |

---

## Accounts Overview

Total: **5** (positive: 3, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Account Number successfully | User logged in as Customer, User has at least one account | 1. Navigate to Accounts Overview<br>2. Click on the Account Number of an account | Account details displayed with full account number | high |
| TC-004 | WF-001 | Sort accounts by Open Date | User logged in as Customer, User has multiple accounts | 1. Navigate to Accounts Overview<br>2. Click on the Open Date column header to sort | Accounts are sorted by Open Date in ascending order | medium |
| TC-005 | WF-001 | Check total balance in footer | User logged in as Customer, User has multiple accounts | 1. Navigate to Accounts Overview | Footer displays the correct total balance across all accounts | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view Account Number when no accounts exist | User logged in as Customer, User has no accounts | 1. Navigate to Accounts Overview<br>2. Attempt to click on Account Number | No account details displayed; appropriate error message shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | View Account Number with masked digits | User logged in as Customer, User has at least one account | 1. Navigate to Accounts Overview<br>2. Observe the Account Number displayed | Account Number is displayed as ****5001, with only last 4 digits visible | low |

---

## Open New Account

Total: **10** (positive: 2, negative: 6, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Checking Account with Valid Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Checking' as Account Type<br>2. Enter '25' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirected to accounts overview. | high |
| TC-002 | WF-002 | Open Savings Account with Valid Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Savings' as Account Type<br>2. Enter '100' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirected to accounts overview. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Open Checking Account with Insufficient Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Checking' as Account Type<br>2. Enter '20' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Error: Initial deposit must be at least $25 for Checking. | high |
| TC-004 | WF-002 | Open Savings Account with Insufficient Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Savings' as Account Type<br>2. Enter '50' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Error: Initial deposit must be at least $100 for Savings. | high |
| TC-005 | WF-001 | Open Checking Account without Selecting Account Type | User logged in as Customer, Funding account has sufficient balance | 1. Leave Account Type unselected<br>2. Enter '25' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Error: Account Type must be selected. | high |
| TC-006 | WF-001 | Open Account with Non-numeric Deposit Amount | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Checking' as Account Type<br>2. Enter 'abc' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Error: Initial Deposit Amount must be numeric. | high |
| TC-007 | WF-001 | Open Checking Account with Invalid Funding Source | User logged in as Customer, Funding account has insufficient balance | 1. Select 'Checking' as Account Type<br>2. Enter '25' in Initial Deposit Amount<br>3. Select an invalid Funding Source Account<br>4. Click 'Open Account' | Error: Funding account must have sufficient balance. | high |
| TC-008 | WF-002 | Open Savings Account with Invalid Funding Source | User logged in as Customer, Funding account has insufficient balance | 1. Select 'Savings' as Account Type<br>2. Enter '100' in Initial Deposit Amount<br>3. Select an invalid Funding Source Account<br>4. Click 'Open Account' | Error: Funding account must have sufficient balance. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Open Checking Account with Maximum Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Checking' as Account Type<br>2. Enter '10000' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirected to accounts overview. | medium |
| TC-010 | WF-002 | Open Savings Account with Maximum Deposit | User logged in as Customer, Funding account has sufficient balance | 1. Select 'Savings' as Account Type<br>2. Enter '50000' in Initial Deposit Amount<br>3. Select a valid Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirected to accounts overview. | medium |

---

## Transfer Funds

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful transfer from My ParaBank Account | User logged in as Account Holder, User has sufficient funds in Checking or Savings | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter a valid Transfer Amount<br>3. Select Source Account from dropdown<br>4. Click on Submit | Transfer completed successfully. | high |
| TC-003 | WF-002 | Successful transfer to External Account | User logged in as Account Holder, User has sufficient funds in Checking or Savings | 1. Select 'External Account' as Transfer Type<br>2. Enter a valid Transfer Amount<br>3. Select Source Account from dropdown<br>4. Enter a valid External Account Number<br>5. Confirm the External Account Number<br>6. Click on Submit | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Transfer amount exceeds available balance | User logged in as Account Holder, User has insufficient funds | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter an amount greater than available balance<br>3. Select Source Account from dropdown<br>4. Click on Submit | Insufficient funds | high |
| TC-004 | WF-002 | Account numbers do not match for external transfer | User logged in as Account Holder, User has sufficient funds in Checking or Savings | 1. Select 'External Account' as Transfer Type<br>2. Enter a valid Transfer Amount<br>3. Select Source Account from dropdown<br>4. Enter a valid External Account Number<br>5. Enter a different number in Confirm Account Number<br>6. Click on Submit | Account numbers do not match | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Transfer amount is zero | User logged in as Account Holder, User has sufficient funds in Checking or Savings | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter 0 in Transfer Amount<br>3. Select Source Account from dropdown<br>4. Click on Submit | Transfer amount must be a valid amount | medium |
| TC-006 | WF-002 | Transfer amount is negative | User logged in as Account Holder, User has sufficient funds in Checking or Savings | 1. Select 'External Account' as Transfer Type<br>2. Enter a negative amount in Transfer Amount<br>3. Select Source Account from dropdown<br>4. Enter a valid External Account Number<br>5. Confirm the External Account Number<br>6. Click on Submit | Transfer amount must be a valid amount | medium |

---

## Payments

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with valid details | User logged in as Customer, User has sufficient funds | 1. Fill in Payee Name with 'John Doe'<br>2. Fill in Street Address with '123 Main St'<br>3. Fill in City with 'Anytown'<br>4. Fill in State with 'CA'<br>5. Fill in ZIP Code with '90210'<br>6. Fill in Phone Number with '123-456-7890'<br>7. Fill in Payee Account Number with '987654321'<br>8. Fill in Confirm Account Number with '987654321'<br>9. Fill in Payment Amount with '100'<br>10. Select Source Account from dropdown<br>11. Click on 'Pay' button | Payment submitted successfully with reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Submit payment with account number mismatch | User logged in as Customer, User has sufficient funds | 1. Fill in Payee Name with 'John Doe'<br>2. Fill in Street Address with '123 Main St'<br>3. Fill in City with 'Anytown'<br>4. Fill in State with 'CA'<br>5. Fill in ZIP Code with '90210'<br>6. Fill in Phone Number with '123-456-7890'<br>7. Fill in Payee Account Number with '987654321'<br>8. Fill in Confirm Account Number with '123456789'<br>9. Fill in Payment Amount with '100'<br>10. Select Source Account from dropdown<br>11. Click on 'Pay' button | Account numbers do not match | high |
| TC-003 | WF-003 | Submit payment with insufficient funds | User logged in as Customer, User has insufficient funds | 1. Fill in Payee Name with 'John Doe'<br>2. Fill in Street Address with '123 Main St'<br>3. Fill in City with 'Anytown'<br>4. Fill in State with 'CA'<br>5. Fill in ZIP Code with '90210'<br>6. Fill in Phone Number with '123-456-7890'<br>7. Fill in Payee Account Number with '987654321'<br>8. Fill in Confirm Account Number with '987654321'<br>9. Fill in Payment Amount with '1000'<br>10. Select Source Account from dropdown<br>11. Click on 'Pay' button | Insufficient funds | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Submit payment with maximum length Payee Name | User logged in as Customer, User has sufficient funds | 1. Fill in Payee Name with 'A very long payee name that exceeds normal length'<br>2. Fill in Street Address with '123 Main St'<br>3. Fill in City with 'Anytown'<br>4. Fill in State with 'CA'<br>5. Fill in ZIP Code with '90210'<br>6. Fill in Phone Number with '123-456-7890'<br>7. Fill in Payee Account Number with '987654321'<br>8. Fill in Confirm Account Number with '987654321'<br>9. Fill in Payment Amount with '100'<br>10. Select Source Account from dropdown<br>11. Click on 'Pay' button | Payment submitted successfully with reference code | medium |
| TC-005 | WF-001 | Submit payment with zero Payment Amount | User logged in as Customer, User has sufficient funds | 1. Fill in Payee Name with 'John Doe'<br>2. Fill in Street Address with '123 Main St'<br>3. Fill in City with 'Anytown'<br>4. Fill in State with 'CA'<br>5. Fill in ZIP Code with '90210'<br>6. Fill in Phone Number with '123-456-7890'<br>7. Fill in Payee Account Number with '987654321'<br>8. Fill in Confirm Account Number with '987654321'<br>9. Fill in Payment Amount with '0'<br>10. Select Source Account from dropdown<br>11. Click on 'Pay' button | Payment amount must be greater than zero | medium |

---

## Request Loan

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid Personal Loan application | User logged in as Customer, Loan_Type selected as Personal | 1. Enter Loan Amount as $10,000<br>2. Enter Down Payment Amount as $1,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | high |
| TC-003 | WF-002 | Submit valid Auto Loan application | User logged in as Customer, Loan_Type selected as Auto | 1. Enter Loan Amount as $20,000<br>2. Enter Down Payment Amount as $2,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | high |
| TC-005 | WF-003 | Submit valid Home Loan application | User logged in as Customer, Loan_Type selected as Home | 1. Enter Loan Amount as $150,000<br>2. Enter Down Payment Amount as $15,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit Personal Loan application with insufficient down payment | User logged in as Customer, Loan_Type selected as Personal | 1. Enter Loan Amount as $10,000<br>2. Enter Down Payment Amount as $500<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Inadequate collateral value | high |
| TC-004 | WF-002 | Submit Auto Loan application with insufficient collateral | User logged in as Customer, Loan_Type selected as Auto | 1. Enter Loan Amount as $20,000<br>2. Enter Down Payment Amount as $2,000<br>3. Select Collateral Account with insufficient funds<br>4. Click Submit | Insufficient credit history | high |
| TC-006 | WF-003 | Submit Home Loan application with down payment less than 10% | User logged in as Customer, Loan_Type selected as Home | 1. Enter Loan Amount as $150,000<br>2. Enter Down Payment Amount as $5,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Inadequate collateral value | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Submit Personal Loan application with maximum amount | User logged in as Customer, Loan_Type selected as Personal | 1. Enter Loan Amount as $50,000<br>2. Enter Down Payment Amount as $5,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-008 | WF-002 | Submit Auto Loan application with maximum amount | User logged in as Customer, Loan_Type selected as Auto | 1. Enter Loan Amount as $75,000<br>2. Enter Down Payment Amount as $7,500<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | medium |
| TC-009 | WF-003 | Submit Home Loan application with maximum amount | User logged in as Customer, Loan_Type selected as Home | 1. Enter Loan Amount as $500,000<br>2. Enter Down Payment Amount as $50,000<br>3. Select Collateral Account with sufficient funds<br>4. Click Submit | Loan approved and created successfully! | medium |

---

## Update Contact Info

Total: **6** (positive: 2, negative: 4, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful profile update with valid data | User logged in as Customer, User has valid contact information | 1. Navigate to the customer profile page.<br>2. Update First Name to 'John'.<br>3. Update Last Name to 'Doe'.<br>4. Update Street Address to '123 Main St'.<br>5. Update City to 'Anytown'.<br>6. Update State to 'CA'.<br>7. Update ZIP Code to '90210'.<br>8. Update Phone Number to '(123) 456-7890'.<br>9. Click on 'Update Profile' button. | Profile updated successfully. | high |
| TC-005 | WF-001 | Successful profile update with maximum length fields | User logged in as Customer, User has valid contact information | 1. Navigate to the customer profile page.<br>2. Update First Name to 'A very long first name that exceeds normal length'.<br>3. Update Last Name to 'A very long last name that exceeds normal length'.<br>4. Update Street Address to '123 Long Address Street that is quite lengthy'.<br>5. Update City to 'A very long city name'.<br>6. Update State to 'California'.<br>7. Update ZIP Code to '90210'.<br>8. Update Phone Number to '(123) 456-7890'.<br>9. Click on 'Update Profile' button. | Profile updated successfully. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Failed profile update due to empty First Name | User logged in as Customer, User has partially filled contact information | 1. Navigate to the customer profile page.<br>2. Leave First Name empty.<br>3. Update Last Name to 'Doe'.<br>4. Update Street Address to '123 Main St'.<br>5. Update City to 'Anytown'.<br>6. Update State to 'CA'.<br>7. Update ZIP Code to '90210'.<br>8. Update Phone Number to '(123) 456-7890'.<br>9. Click on 'Update Profile' button. | Highlights invalid fields and displays an inline error banner. | high |
| TC-003 | WF-002 | Failed profile update due to invalid Phone Number format | User logged in as Customer, User has partially filled contact information | 1. Navigate to the customer profile page.<br>2. Update First Name to 'John'.<br>3. Update Last Name to 'Doe'.<br>4. Update Street Address to '123 Main St'.<br>5. Update City to 'Anytown'.<br>6. Update State to 'CA'.<br>7. Update ZIP Code to '90210'.<br>8. Update Phone Number to '1234567890'.<br>9. Click on 'Update Profile' button. | Highlights invalid fields and displays an inline error banner. | high |
| TC-004 | WF-002 | Failed profile update due to invalid ZIP Code format | User logged in as Customer, User has partially filled contact information | 1. Navigate to the customer profile page.<br>2. Update First Name to 'John'.<br>3. Update Last Name to 'Doe'.<br>4. Update Street Address to '123 Main St'.<br>5. Update City to 'Anytown'.<br>6. Update State to 'CA'.<br>7. Update ZIP Code to 'ABCDE'.<br>8. Update Phone Number to '(123) 456-7890'.<br>9. Click on 'Update Profile' button. | Highlights invalid fields and displays an inline error banner. | high |
| TC-006 | WF-002 | Failed profile update due to all fields empty | User logged in as Customer, User is on the customer profile page | 1. Navigate to the customer profile page.<br>2. Leave all fields empty.<br>3. Click on 'Update Profile' button. | Highlights invalid fields and displays an inline error banner. | high |

---

## Manage Cards

Total: **9** (positive: 3, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Request a Debit Card with valid details | User logged in as Customer, User has a valid account | 1. Select 'Debit' from Card Type dropdown<br>2. Enter valid Account to Link<br>3. Enter complete Shipping Address<br>4. Click on 'Request Card' button | Card request submitted successfully. | high |
| TC-002 | WF-001 | Request a Credit Card with valid details | User logged in as Customer, User has a valid account | 1. Select 'Credit' from Card Type dropdown<br>2. Enter valid Account to Link<br>3. Enter complete Shipping Address<br>4. Click on 'Request Card' button | Card request submitted successfully. | high |
| TC-004 | WF-002 | Update card controls with valid inputs | User logged in as Customer, User has an existing card | 1. Select an existing card from Select Existing Card dropdown<br>2. Enter a valid New Spending Limit<br>3. Select a valid Card Status<br>4. Click on 'Update Controls' button | Card controls updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Request Card with incomplete Shipping Address | User logged in as Customer, User has a valid account | 1. Select 'Debit' from Card Type dropdown<br>2. Enter valid Account to Link<br>3. Enter incomplete Shipping Address<br>4. Click on 'Request Card' button | Error message indicating that the address must be complete. | high |
| TC-005 | WF-002 | Update card controls with invalid New Spending Limit | User logged in as Customer, User has an existing card | 1. Select an existing card from Select Existing Card dropdown<br>2. Enter an invalid New Spending Limit (e.g., above policy limit)<br>3. Select a valid Card Status<br>4. Click on 'Update Controls' button | Inline validation error for spending limit. | high |
| TC-006 | WF-002 | Update card controls with invalid Card Status transition | User logged in as Customer, User has an existing card | 1. Select an existing card from Select Existing Card dropdown<br>2. Enter a valid New Spending Limit<br>3. Select an invalid Card Status transition (e.g., from Frozen to Active without proper conditions)<br>4. Click on 'Update Controls' button | Inline validation error for card status transition. | high |
| TC-008 | WF-001 | Request Card with no Account to Link | User logged in as Customer | 1. Select 'Debit' from Card Type dropdown<br>2. Leave Account to Link empty<br>3. Enter complete Shipping Address<br>4. Click on 'Request Card' button | Error message indicating that Account to Link is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-002 | Update card controls with future Travel Notice dates | User logged in as Customer, User has an existing card | 1. Select an existing card from Select Existing Card dropdown<br>2. Enter a valid New Spending Limit<br>3. Enter a valid Travel Notice date range in the future<br>4. Click on 'Update Controls' button | Card controls updated successfully. | medium |
| TC-009 | WF-002 | Update card controls with negative New Spending Limit | User logged in as Customer, User has an existing card | 1. Select an existing card from Select Existing Card dropdown<br>2. Enter a negative New Spending Limit<br>3. Select a valid Card Status<br>4. Click on 'Update Controls' button | Inline validation error for spending limit. | high |

---

## Investments

Total: **10** (positive: 2, negative: 6, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Execute a successful trade with valid inputs | User logged in as Trader, User has sufficient buying power | 1. Select 'Buy' from Action dropdown<br>2. Enter a valid Fund Symbol<br>3. Enter a quantity greater than zero<br>4. Select a Funding Account<br>5. Click on 'Execute Trade' | Trade executed successfully. Order ID displayed. | high |
| TC-005 | WF-002 | Create a successful recurring investment plan with valid inputs | User logged in as Investor, User has adequate balance in funding account | 1. Enter a valid Fund Symbol<br>2. Enter a contribution amount that meets the minimum<br>3. Select a frequency from the dropdown<br>4. Enter a start date in the future<br>5. Select a Funding Account<br>6. Click on 'Create Plan' | Plan created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to execute trade with insufficient buying power | User logged in as Trader, User has insufficient buying power | 1. Select 'Buy' from Action dropdown<br>2. Enter a valid Fund Symbol<br>3. Enter a quantity greater than zero<br>4. Select a Funding Account<br>5. Click on 'Execute Trade' | Error message displayed indicating insufficient buying power. | high |
| TC-003 | WF-001 | Attempt to execute trade with invalid fund symbol | User logged in as Trader | 1. Select 'Buy' from Action dropdown<br>2. Enter an invalid Fund Symbol<br>3. Enter a quantity greater than zero<br>4. Select a Funding Account<br>5. Click on 'Execute Trade' | Error message displayed indicating that the symbol must exist. | high |
| TC-004 | WF-001 | Attempt to execute trade with quantity less than or equal to zero | User logged in as Trader, User has sufficient buying power | 1. Select 'Buy' from Action dropdown<br>2. Enter a valid Fund Symbol<br>3. Enter a quantity of zero<br>4. Select a Funding Account<br>5. Click on 'Execute Trade' | Error message displayed indicating quantity must be greater than zero. | high |
| TC-006 | WF-002 | Attempt to create a recurring investment plan with a start date in the past | User logged in as Investor | 1. Enter a valid Fund Symbol<br>2. Enter a contribution amount that meets the minimum<br>3. Select a frequency from the dropdown<br>4. Enter a start date in the past<br>5. Select a Funding Account<br>6. Click on 'Create Plan' | Error message displayed indicating start date must be in the future. | high |
| TC-007 | WF-002 | Attempt to create a recurring investment plan with contribution amount below minimum | User logged in as Investor, User has adequate balance in funding account | 1. Enter a valid Fund Symbol<br>2. Enter a contribution amount below the minimum<br>3. Select a frequency from the dropdown<br>4. Enter a start date in the future<br>5. Select a Funding Account<br>6. Click on 'Create Plan' | Error message displayed indicating contribution must meet minimum. | high |
| TC-008 | WF-002 | Attempt to create a recurring investment plan with an invalid funding account | User logged in as Investor | 1. Enter a valid Fund Symbol<br>2. Enter a contribution amount that meets the minimum<br>3. Select a frequency from the dropdown<br>4. Enter a start date in the future<br>5. Select an invalid Funding Account<br>6. Click on 'Create Plan' | Error message displayed indicating funding account must have adequate balance. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Execute trade with maximum quantity allowed | User logged in as Trader, User has sufficient buying power | 1. Select 'Buy' from Action dropdown<br>2. Enter a valid Fund Symbol<br>3. Enter the maximum quantity allowed<br>4. Select a Funding Account<br>5. Click on 'Execute Trade' | Trade executed successfully. Order ID displayed. | medium |
| TC-010 | WF-002 | Create a recurring investment plan with maximum contribution amount | User logged in as Investor, User has adequate balance in funding account | 1. Enter a valid Fund Symbol<br>2. Enter the maximum contribution amount allowed<br>3. Select a frequency from the dropdown<br>4. Enter a start date in the future<br>5. Select a Funding Account<br>6. Click on 'Create Plan' | Plan created successfully. | medium |

---

## Account Statements

Total: **8** (positive: 2, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate statement with valid date range and account selection | User logged in as account holder, User has at least one account | 1. Select a valid date range for the Statement Period<br>2. Choose an account from the dropdown<br>3. Click on 'Generate Statement' | Statement generated successfully. | high |
| TC-003 | WF-003 | Save e-Statement preference with valid email address | User logged in as account holder | 1. Check the 'Opt into Paperless Statements' checkbox<br>2. Enter a valid email address<br>3. Click on 'Save Preference' | e-Statement preference updated. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Attempt to generate statement with invalid date range | User logged in as account holder, User has at least one account | 1. Select an invalid date range for the Statement Period<br>2. Choose an account from the dropdown<br>3. Click on 'Generate Statement' | Unable to generate statement — please try again later. | high |
| TC-004 | WF-004 | Attempt to save e-Statement preference with invalid email address | User logged in as account holder | 1. Check the 'Opt into Paperless Statements' checkbox<br>2. Enter an invalid email address<br>3. Click on 'Save Preference' | highlights email field with guidance | high |
| TC-006 | WF-002 | Generate statement with future date range | User logged in as account holder, User has at least one account | 1. Select a future date for the Statement Period<br>2. Choose an account from the dropdown<br>3. Click on 'Generate Statement' | Unable to generate statement — please try again later. | medium |
| TC-007 | WF-003 | Save e-Statement preference with empty email field | User logged in as account holder | 1. Check the 'Opt into Paperless Statements' checkbox<br>2. Leave the email address field empty<br>3. Click on 'Save Preference' | highlights email field with guidance | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Generate statement with boundary date range | User logged in as account holder, User has at least one account | 1. Select the earliest possible date for the Statement Period<br>2. Choose an account from the dropdown<br>3. Click on 'Generate Statement' | Statement generated successfully. | medium |
| TC-008 | WF-004 | Save e-Statement preference with email exceeding character limit | User logged in as account holder | 1. Check the 'Opt into Paperless Statements' checkbox<br>2. Enter an email address exceeding the character limit<br>3. Click on 'Save Preference' | highlights email field with guidance | medium |

---

## Security Settings

Total: **7** (positive: 1, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successfully change password with valid inputs | User logged in as regular user, User knows current password | 1. Enter valid current password.<br>2. Enter a new password that meets strong-password policy.<br>3. Confirm the new password by entering it again.<br>4. Click on 'Change Password' button. | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Fail to change password with incorrect current password | User logged in as regular user | 1. Enter an incorrect current password.<br>2. Enter a new password that meets strong-password policy.<br>3. Confirm the new password by entering it again.<br>4. Click on 'Change Password' button. | Validation error highlighting the current password field. | high |
| TC-003 | WF-001 | Fail to change password with new password not meeting policy | User logged in as regular user, User knows current password | 1. Enter valid current password.<br>2. Enter a new password that does not meet strong-password policy.<br>3. Confirm the new password by entering it again.<br>4. Click on 'Change Password' button. | Validation error highlighting the new password field. | high |
| TC-004 | WF-001 | Fail to change password with new passwords not matching | User logged in as regular user, User knows current password | 1. Enter valid current password.<br>2. Enter a new password that meets strong-password policy.<br>3. Enter a different password in the confirm field.<br>4. Click on 'Change Password' button. | Validation error highlighting the confirm password field. | high |
| TC-005 | WF-001 | Fail to change password with empty fields | User logged in as regular user | 1. Leave all fields empty.<br>2. Click on 'Change Password' button. | Validation errors highlighting all fields. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Edge case: New password at maximum length | User logged in as regular user, User knows current password | 1. Enter valid current password.<br>2. Enter a new password that is at the maximum allowed length.<br>3. Confirm the new password by entering it again.<br>4. Click on 'Change Password' button. | Password changed successfully. | medium |
| TC-007 | WF-001 | Edge case: New password at minimum length | User logged in as regular user, User knows current password | 1. Enter valid current password.<br>2. Enter a new password that is at the minimum allowed length.<br>3. Confirm the new password by entering it again.<br>4. Click on 'Change Password' button. | Validation error highlighting the new password field. | medium |

---

## Support Center

Total: **10** (positive: 3, negative: 5, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send Message without Attachment with valid inputs | User logged in as Customer, User on Support Center page | 1. Enter valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message in the Message Body<br>4. Click on Send Message | Message sent successfully with ticket ID displayed | high |
| TC-002 | WF-002 | Send Message with Attachment with valid inputs | User logged in as Customer, User on Support Center page | 1. Enter valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message in the Message Body<br>4. Upload a valid attachment<br>5. Click on Send Message | Message sent successfully with ticket ID displayed | high |
| TC-003 | WF-003 | Request Callback with valid inputs | User logged in as Customer, User on Support Center page | 1. Select a reason for call from the dropdown<br>2. Enter a valid date that is at least the next business day<br>3. Enter a preferred time window<br>4. Verify the Phone Number is pre-filled and editable<br>5. Click on Request Callback | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Send Message without Subject | User logged in as Customer, User on Support Center page | 1. Leave the Subject field empty<br>2. Select a category from the dropdown<br>3. Enter a message in the Message Body<br>4. Click on Send Message | Inline guidance displayed indicating Subject is required | high |
| TC-005 | WF-001 | Send Message without Message Body | User logged in as Customer, User on Support Center page | 1. Enter valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Leave the Message Body empty<br>4. Click on Send Message | Inline guidance displayed indicating Message Body is required | high |
| TC-006 | WF-002 | Send Message with invalid Attachment type | User logged in as Customer, User on Support Center page | 1. Enter valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message in the Message Body<br>4. Upload an invalid attachment type<br>5. Click on Send Message | Inline guidance displayed indicating invalid attachment type | high |
| TC-007 | WF-003 | Request Callback with invalid Phone Number format | User logged in as Customer, User on Support Center page | 1. Select a reason for call from the dropdown<br>2. Enter a valid date that is at least the next business day<br>3. Enter a preferred time window<br>4. Modify the Phone Number to an invalid format<br>5. Click on Request Callback | Inline guidance displayed indicating Phone Number format is invalid | high |
| TC-008 | WF-003 | Request Callback with date in the past | User logged in as Customer, User on Support Center page | 1. Select a reason for call from the dropdown<br>2. Enter a date that is in the past<br>3. Enter a preferred time window<br>4. Click on Request Callback | Inline guidance displayed indicating date must be at least the next business day | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Send Message with Subject exceeding maximum length | User logged in as Customer, User on Support Center page | 1. Enter a subject that exceeds the maximum length<br>2. Select a category from the dropdown<br>3. Enter a message in the Message Body<br>4. Click on Send Message | Inline guidance displayed indicating subject length must be valid | high |
| TC-010 | WF-003 | Request Callback with Preferred Date as today | User logged in as Customer, User on Support Center page | 1. Select a reason for call from the dropdown<br>2. Enter today's date as the Preferred Date<br>3. Enter a preferred time window<br>4. Click on Request Callback | Inline guidance displayed indicating date must be at least the next business day | high |

---
