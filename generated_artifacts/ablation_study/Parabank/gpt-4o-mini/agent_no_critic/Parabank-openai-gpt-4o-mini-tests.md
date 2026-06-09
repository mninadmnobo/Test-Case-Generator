# Test Cases — Parabank

Generated: 2026-06-09T10:35:52.573855Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 190 | 23 | 106 | 61 | 106 | 68 | 16 |

## Login

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click Sign In | Signed in successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email field blank and submit |  | 1. Leave the Email_Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Leave the Password field blank<br>3. Click Sign In | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email_Username field<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it must be a valid email format | medium |
| TC-005 |  | Enter a password that is too short and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Enter a password that does not meet complexity requirements and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <valid password without uppercase or special character> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 |  | Submit with incorrect email and password |  | 1. Fill the Email_Username field with <non-registered email><br>2. Fill the Password field with <incorrect password><br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Email field with invalid format |  | 1. Enter 'invalid-email' in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Form submission is blocked; error message indicates invalid email format. | medium |
| TC-009 (boundary) |  | Password with exactly 8 characters but missing special character |  | 1. Enter a valid email in the Email/Username field<br>2. Enter 'Password1' in the Password field<br>3. Click Sign In | Form submission is blocked; error message indicates password requirements are not met. | medium |
| TC-010 (input_edge) |  | Email field with leading and trailing whitespace |  | 1. Enter '   user@example.com   ' in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Leading/trailing whitespace is trimmed; email is saved as 'user@example.com'. | low |
| TC-011 (input_edge) |  | Password with special characters |  | 1. Enter a valid email in the Email/Username field<br>2. Enter 'Password@123' in the Password field<br>3. Click Sign In | Form submission succeeds; user is redirected to Accounts Overview page. | medium |

---

## Register

Total: **26** (positive: 1, negative: 17, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid inputs | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Enter <valid SSN> in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <valid password> in the Password field<br>11. Enter <valid password> in the Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Leave the Social Security Number field blank and submit |  | 1. Leave the Social_Security_Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it is required | high |
| TC-010 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it is required | high |
| TC-011 |  | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Leave the Confirm Password field blank and submit |  | 1. Leave the Confirm_Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-013 |  | Enter an invalid format in the ZIP Code field and submit |  | 1. Enter <invalid ZIP code format> in the ZIP_Code field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it must be 5 digits or 5+4 format | medium |
| TC-014 |  | Enter an invalid format in the Phone Number field and submit |  | 1. Enter <invalid phone number format> in the Phone_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it must follow format (123) 456-7890 | medium |
| TC-015 |  | Enter an invalid format in the Social Security Number field and submit |  | 1. Enter <invalid SSN format> in the Social_Security_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it must follow format 123-45-6789 | medium |
| TC-016 |  | Enter an invalid format in the Username field and submit |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it must be a valid email format | medium |
| TC-017 |  | Enter a short password and submit |  | 1. Enter <password shorter than 8 characters> in the Password field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-018 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields<br>4. Click Register | Inline validation error appears on the Confirm_Password field indicating it must match Password | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-001 | Enter exactly 5 digits in the ZIP Code field |  | 1. Enter '12345' in the ZIP_Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the ZIP Code '12345' | medium |
| TC-020 (boundary) | WF-001 | Enter 4 digits in the ZIP Code field |  | 1. Enter '1234' in the ZIP_Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | ZIP_Code field displays an error indicating the value is below the minimum allowed (must be 5 digits or 5+4 format) | medium |
| TC-021 (boundary) | WF-001 | Enter exactly 10 digits in the Phone Number field |  | 1. Enter '(123) 456-7890' in the Phone_Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the Phone Number '(123) 456-7890' | medium |
| TC-022 (boundary) | WF-001 | Enter an invalid Phone Number format |  | 1. Enter '1234567890' in the Phone_Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Phone_Number field displays an error indicating the format must be (123) 456-7890 | medium |
| TC-023 (boundary) | WF-001 | Enter exactly 8 characters in the Password field |  | 1. Enter 'abcdefgh' in the Password field<br>2. Enter 'abcdefgh' in the Confirm_Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Form submits successfully; account is created with the Password 'abcdefgh' | medium |
| TC-024 (boundary) | WF-001 | Enter 7 characters in the Password field |  | 1. Enter 'abcdefg' in the Password field<br>2. Enter 'abcdefg' in the Confirm_Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Password field displays an error indicating it must be at least 8 characters | medium |
| TC-025 (input_edge) | WF-001 | Enter a long string in the First Name field |  | 1. Enter 'A very long first name that exceeds typical lengths for a name' in the First_Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the long First Name | low |
| TC-026 (input_edge) | WF-001 | Enter special characters in the Username field |  | 1. Enter 'user@name.com' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the Username 'user@name.com' | low |

---

## Accounts Overview

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Account Number action is clickable | User logged in as <Role> | 1. Observe the Customer Accounts Table is displayed | The Account Number column shows masked numbers as ****5001 for each account | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view account number | User is authenticated | 1. Click on the Account Number link | Action is blocked; no account number is displayed; the link is not implemented yet. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Click on Account Number to view details | User is logged in and on the Accounts Overview page | 1. Locate the Account Number column in the Customer Accounts Table<br>2. Click on the Account Number link | Account Number link is clickable but does not lead to any action; no error is shown. | medium |
| TC-004 (input_edge) |  | Verify table displays total balance correctly | User is logged in and on the Accounts Overview page | 1. Check the footer of the Customer Accounts Table | Total balance displayed in the footer is accurate and reflects the sum of all current balances. | low |

---

## Open New Account

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Account with Checking type | User logged in as <Role>, Funding account has sufficient balance | 1. Select 'Checking' from the Account Type options<br>2. Enter 25 in the Initial Deposit Amount field<br>3. Select <valid funding source account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |
| TC-002 | WF-002 | Open Account with Savings type | User logged in as <Role>, Funding account has sufficient balance | 1. Select 'Savings' from the Account Type options<br>2. Enter 100 in the Initial Deposit Amount field<br>3. Select <valid funding source account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account Type field blank |  | 1. Leave the Account Type field blank<br>2. Fill Initial Deposit Amount with a valid amount<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave the Initial Deposit Amount field blank |  | 1. Select Checking or Savings for Account Type<br>2. Leave the Initial Deposit Amount field blank<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Enter a non-numeric value in the Initial Deposit Amount field |  | 1. Select Checking or Savings for Account Type<br>2. Enter <non-numeric value> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-006 |  | Enter an Initial Deposit Amount less than required for Checking |  | 1. Select Checking for Account Type<br>2. Enter <amount below $25> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-007 |  | Enter an Initial Deposit Amount less than required for Savings |  | 1. Select Savings for Account Type<br>2. Enter <amount below $100> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-008 |  | Leave the Funding Source Account field blank |  | 1. Select Checking or Savings for Account Type<br>2. Enter a valid Initial Deposit Amount<br>3. Leave the Funding Source Account field blank<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it is required | high |
| TC-009 |  | Attempt to open account without sufficient balance in funding source |  | 1. Select Checking or Savings for Account Type<br>2. Enter a valid Initial Deposit Amount<br>3. Select a Funding Source Account with insufficient balance<br>4. Click Open Account | Form does not submit; error shown indicating funding account must have sufficient balance | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Initial deposit amount for Checking type at minimum | Account Type is set to Checking, Funding Source Account has sufficient balance | 1. Select 'Checking' for Account Type<br>2. Enter exactly $25 in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirects to accounts overview. | medium |
| TC-011 (boundary) | WF-001 | Initial deposit amount for Checking type just below minimum | Account Type is set to Checking, Funding Source Account has sufficient balance | 1. Select 'Checking' for Account Type<br>2. Enter $24.99 in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click 'Open Account' | Inline error shown: 'Initial Deposit Amount must be at least $25 for Checking' | medium |
| TC-012 (boundary) | WF-002 | Initial deposit amount for Savings type at minimum | Account Type is set to Savings, Funding Source Account has sufficient balance | 1. Select 'Savings' for Account Type<br>2. Enter exactly $100 in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click 'Open Account' | Account opened successfully! Redirects to accounts overview. | medium |
| TC-013 (boundary) | WF-002 | Initial deposit amount for Savings type just below minimum | Account Type is set to Savings, Funding Source Account has sufficient balance | 1. Select 'Savings' for Account Type<br>2. Enter $99.99 in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click 'Open Account' | Inline error shown: 'Initial Deposit Amount must be at least $100 for Savings' | medium |

---

## Transfer Funds

Total: **13** (positive: 2, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit transfer to My ParaBank Account | User logged in as <Role> | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Transfer completed successfully. | high |
| TC-002 | WF-002 | Submit transfer to External Account | User logged in as <Role> | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <valid external account number> in the Confirm Account Number field<br>6. Click Submit | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Transfer Amount field blank and submit |  | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Leave the Transfer Amount field blank<br>3. Select a Source Account<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-004 |  | Submit with all required fields empty |  | 1. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-005 |  | Enter a negative amount in the Transfer Amount field |  | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <negative amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it must be a positive amount | medium |
| TC-006 |  | Attempt to submit an external transfer with mismatched account numbers |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <different account number> in the Confirm Account Number field<br>4. Enter <amount> in the Transfer Amount field<br>5. Select a Source Account<br>6. Click Submit | Inline validation error appears indicating 'Account numbers do not match' | high |
| TC-007 |  | Attempt to submit an external transfer with insufficient funds |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <valid external account number> in the Confirm Account Number field<br>4. Enter <amount exceeding available balance> in the Transfer Amount field<br>5. Select a Source Account<br>6. Click Submit | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Transfer amount is zero | User selects 'External Account' as Transfer_Type, User selects a Source Account | 1. Enter '0' in the Transfer_Amount field<br>2. Enter a valid External_Account_Number<br>3. Enter the same number in the Confirm_Account_Number field<br>4. Click Submit | Form submission is blocked; 'Transfer amount must be a positive amount' error is displayed. | medium |
| TC-009 (boundary) | WF-002 | Transfer amount exceeds available funds | User selects 'External Account' as Transfer_Type, User selects a Source Account | 1. Enter an amount greater than available funds in the Transfer_Amount field<br>2. Enter a valid External_Account_Number<br>3. Enter the same number in the Confirm_Account_Number field<br>4. Click Submit | Form submission is blocked; 'Insufficient funds' error is displayed. | medium |
| TC-010 (boundary) | WF-002 | Confirm account number does not match | User selects 'External Account' as Transfer_Type, User selects a Source Account | 1. Enter a valid External_Account_Number<br>2. Enter a different number in the Confirm_Account_Number field<br>3. Enter a valid amount in the Transfer_Amount field<br>4. Click Submit | Form submission is blocked; 'Account numbers do not match' error is displayed. | medium |
| TC-011 (boundary) | WF-001 | Transfer amount is a valid positive amount | User selects 'My ParaBank Account' as Transfer_Type, User selects a Source Account | 1. Enter a valid positive amount in the Transfer_Amount field<br>2. Click Submit | Form submits successfully; 'Transfer completed successfully.' message is displayed. | medium |
| TC-012 (input_edge) |  | Enter a long account number |  | 1. Enter a long string of numbers (more than typical account number length) in the External_Account_Number field<br>2. Enter the same long string in the Confirm_Account_Number field<br>3. Enter a valid amount in the Transfer_Amount field<br>4. Click Submit | Form submission is blocked; specific error indicating account number length is shown. | low |
| TC-013 (input_edge) |  | Enter special characters in account number |  | 1. Enter special characters (e.g., '@#$%') in the External_Account_Number field<br>2. Enter the same special characters in the Confirm_Account_Number field<br>3. Enter a valid amount in the Transfer_Amount field<br>4. Click Submit | Form submission is blocked; specific error indicating invalid characters in account number is shown. | low |

---

## Payments

Total: **17** (positive: 1, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with valid details | User logged in as <Role> | 1. Enter <valid payee name> in the Payee Name field<br>2. Enter <valid street address> in the Street Address field<br>3. Enter <valid city> in the City field<br>4. Enter <valid state> in the State field<br>5. Enter <valid ZIP code> in the ZIP Code field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Enter <valid payee account number> in the Payee Account Number field<br>8. Enter the same <valid payee account number> in the Confirm Account Number field<br>9. Enter <valid payment amount> in the Payment Amount field<br>10. Select <valid source account> from the Source Account dropdown<br>11. Click Pay | Payment submitted successfully with reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Payee Name field blank |  | 1. Leave the Payee_Name field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Name field indicating it is required | high |
| TC-003 |  | Leave the Street Address field blank |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-004 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the City field indicating it is required | high |
| TC-005 |  | Leave the State field blank |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the State field indicating it is required | high |
| TC-006 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-008 |  | Leave the Payee Account Number field blank |  | 1. Leave the Payee_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Account_Number field indicating it is required | high |
| TC-009 |  | Leave the Confirm Account Number field blank |  | 1. Leave the Confirm_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating it is required | high |
| TC-010 |  | Leave the Payment Amount field blank |  | 1. Leave the Payment_Amount field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payment_Amount field indicating it is required | high |
| TC-011 |  | Leave the Source Account field blank |  | 1. Leave the Source_Account field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Source_Account field indicating it is required | high |
| TC-012 | WF-002 | Submit payment with account number mismatch |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <different value> in the Confirm_Account_Number field<br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears indicating 'Account numbers do not match' | high |
| TC-013 | WF-003 | Submit payment with insufficient funds |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <valid Confirm Account Number> in the Confirm_Account_Number field<br>3. Enter <amount exceeding available funds> in the Payment_Amount field<br>4. Fill all other required fields<br>5. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-002 | Confirm Account Number does not match Payee Account Number | Enter a valid Payee Account Number, Enter a different Confirm Account Number | 1. Enter 'Valid Payee Name' in the Payee_Name field<br>2. Enter '123 Main St' in the Street_Address field<br>3. Enter 'Anytown' in the City field<br>4. Enter 'CA' in the State field<br>5. Enter '90210' in the ZIP_Code field<br>6. Enter '555-1234' in the Phone_Number field<br>7. Enter '123456789' in the Payee_Account_Number field<br>8. Enter '987654321' in the Confirm_Account_Number field<br>9. Enter '100' in the Payment_Amount field<br>10. Select a valid option from the Source_Account dropdown<br>11. Click the Pay button | Inline error displayed: 'Account numbers do not match' | medium |
| TC-015 (boundary) | WF-003 | Payment Amount exceeds available funds | Enter valid account details, Ensure the Payment Amount exceeds available funds | 1. Enter 'Valid Payee Name' in the Payee_Name field<br>2. Enter '123 Main St' in the Street_Address field<br>3. Enter 'Anytown' in the City field<br>4. Enter 'CA' in the State field<br>5. Enter '90210' in the ZIP_Code field<br>6. Enter '555-1234' in the Phone_Number field<br>7. Enter '123456789' in the Payee_Account_Number field<br>8. Enter '123456789' in the Confirm_Account_Number field<br>9. Enter '1000' in the Payment_Amount field<br>10. Select a valid option from the Source_Account dropdown<br>11. Click the Pay button | Inline error displayed: 'Insufficient funds' | medium |
| TC-016 (input_edge) |  | Long input for Payee Name |  | 1. Enter a string of 200 characters in the Payee_Name field<br>2. Fill all other required fields with valid data<br>3. Click the Pay button | Form submits successfully; Payee_Name displays the full 200 characters | low |
| TC-017 (input_edge) |  | Special characters in Street Address |  | 1. Enter '!@#$%^&*()' in the Street_Address field<br>2. Fill all other required fields with valid data<br>3. Click the Pay button | Form submits successfully; Street_Address displays '!@#$%^&*()' | low |

---

## Request Loan

Total: **18** (positive: 3, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Request with Personal Loan Type | User logged in as <Role> | 1. Select 'Personal' from the Loan Type cards<br>2. Enter 15000 in the Loan Amount field<br>3. Enter 1500 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |
| TC-002 | WF-002 | Submit Loan Request with Auto Loan Type | User logged in as <Role> | 1. Select 'Auto' from the Loan Type cards<br>2. Enter 30000 in the Loan Amount field<br>3. Enter 3000 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |
| TC-003 | WF-003 | Submit Loan Request with Home Loan Type | User logged in as <Role> | 1. Select 'Home' from the Loan Type cards<br>2. Enter 200000 in the Loan Amount field<br>3. Enter 20000 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Loan Amount field blank and submit |  | 1. Leave the Loan Amount field blank<br>2. Fill all other required fields<br>3. Click Submit Loan Request | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Leave the Down Payment Amount field blank and submit |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Leave the Down Payment Amount field blank<br>4. Click Submit Loan Request | Inline validation error appears on the Down Payment Amount field indicating it is required | high |
| TC-006 |  | Enter Down Payment Amount greater than Loan Amount |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <down payment amount greater than loan amount> in the Down Payment Amount field<br>4. Click Submit Loan Request | Inline validation error appears on the Down Payment Amount field indicating it must be less than Loan Amount | high |
| TC-007 |  | Enter Down Payment Amount less than 10% of Loan Amount |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <down payment amount less than 10% of loan amount> in the Down Payment Amount field<br>4. Click Submit Loan Request | Inline validation error appears on the Down Payment Amount field indicating it must be at least 10% of Loan Amount | high |
| TC-008 |  | Attempt to submit with insufficient collateral funds |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <valid down payment amount> in the Down Payment Amount field<br>4. Select <collateral account with insufficient funds> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Submission is blocked; error shown indicating 'Inadequate collateral value' | high |
| TC-009 |  | Attempt to submit with collateral value less than 20% of loan amount |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <valid down payment amount> in the Down Payment Amount field<br>4. Select <collateral account with value less than 20% of loan amount> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Submission is blocked; error shown indicating 'must be at least 20% of collateral value' | high |
| TC-010 | WF-001 | Submit Loan Request with Personal Loan Type but insufficient credit history |  | 1. Select Personal as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <valid down payment amount> in the Down Payment Amount field<br>4. Select <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Submission is blocked; error shown indicating 'Insufficient credit history' | high |
| TC-011 | WF-002 | Submit Loan Request with Auto Loan Type but insufficient credit history |  | 1. Select Auto as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <valid down payment amount> in the Down Payment Amount field<br>4. Select <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Submission is blocked; error shown indicating 'Insufficient credit history' | high |
| TC-012 | WF-003 | Submit Loan Request with Home Loan Type but insufficient credit history |  | 1. Select Home as Loan Type<br>2. Enter <valid loan amount> in the Loan Amount field<br>3. Enter <valid down payment amount> in the Down Payment Amount field<br>4. Select <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Submission is blocked; error shown indicating 'Insufficient credit history' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Test Down Payment at minimum required for Personal Loan | Select 'Personal' loan type | 1. Enter $1,000 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field | Form submits successfully; loan request is created with Down Payment of $100 (10% of Loan Amount) | medium |
| TC-014 (boundary) | WF-001 | Test Down Payment just below minimum required for Personal Loan | Select 'Personal' loan type | 1. Enter $1,000 in the Loan Amount field<br>2. Enter $99 in the Down Payment Amount field | Submission is blocked; error shown indicating 'Down Payment must be at least 10% of Loan Amount' | medium |
| TC-015 (boundary) | WF-002 | Test Loan Amount at maximum for Auto Loan | Select 'Auto' loan type | 1. Enter $75,000 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field | Form submits successfully; loan request is created with Loan Amount of $75,000 | medium |
| TC-016 (boundary) | WF-002 | Test Loan Amount just above maximum for Auto Loan | Select 'Auto' loan type | 1. Enter $75,001 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field | Submission is blocked; error shown indicating 'Loan Amount must be between $5,000 and $75,000' | medium |
| TC-017 (boundary) | WF-003 | Test Down Payment just below 20% of Collateral for Home Loan | Select 'Home' loan type | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $10,000 in the Collateral Account field<br>3. Enter $9,999 in the Down Payment Amount field | Submission is blocked; error shown indicating 'Down Payment must be at least 10% of Loan Amount' | medium |
| TC-018 (boundary) | WF-003 | Test Down Payment at minimum required for Home Loan | Select 'Home' loan type | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $10,000 in the Collateral Account field<br>3. Enter $5,000 in the Down Payment Amount field | Form submits successfully; loan request is created with Down Payment of $5,000 (10% of Loan Amount) | medium |

---

## Update Contact Info

Total: **19** (positive: 1, negative: 14, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update customer profile with valid information | User logged in as <Customer>, Customer profile page is open with pre-filled fields | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Enter <valid state> in the State field<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click Update Profile | Profile updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank |  | 1. Leave the State field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Submit with invalid format in First Name |  | 1. Enter <invalid format> in the First_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-010 |  | Submit with invalid format in Last Name |  | 1. Enter <invalid format> in the Last_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-011 |  | Submit with invalid format in Street Address |  | 1. Enter <invalid format> in the Street_Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-012 |  | Submit with invalid format in City |  | 1. Enter <invalid format> in the City field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-013 |  | Submit with invalid format in State |  | 1. Enter <invalid format> in the State field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-014 |  | Submit with invalid format in ZIP Code |  | 1. Enter <invalid format> in the ZIP_Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-015 |  | Submit with invalid format in Phone Number |  | 1. Enter <invalid format> in the Phone_Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (input_edge) | WF-001 | Enter a long string in the First Name field |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields with valid formats<br>3. Click Update Profile | Inline error banner displays indicating the First Name format is invalid | low |
| TC-017 (input_edge) | WF-001 | Enter special characters in the Last Name field |  | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields with valid formats<br>3. Click Update Profile | Inline error banner displays indicating the Last Name format is invalid | low |
| TC-018 (input_edge) | WF-001 | Enter leading/trailing whitespace in the Street Address field |  | 1. Enter leading and trailing whitespace in the Street Address field<br>2. Fill all other required fields with valid formats<br>3. Click Update Profile | Inline error banner displays indicating the Street Address format is invalid | low |
| TC-019 (input_edge) | WF-001 | Enter a valid ZIP Code with incorrect format |  | 1. Enter a ZIP Code that is not in a valid format<br>2. Fill all other required fields with valid formats<br>3. Click Update Profile | Inline error banner displays indicating the ZIP Code format is invalid | low |

---

## Manage Cards

Total: **16** (positive: 2, negative: 10, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Card Request with valid details | User logged in as <Role>, Account is in good standing | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click Request Card | Card request submitted successfully; shows tracking ID | high |
| TC-002 | WF-002 | Update Card Controls with valid details | User logged in as <Role> | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid numeric limit> in the New Spending Limit field<br>3. Click Add under Travel Notice<br>4. Enter <destination> in the Destination field<br>5. Enter <valid start date> in the Start Date field<br>6. Enter <valid end date> in the End Date field<br>7. Select 'Active' from the Card Status dropdown<br>8. Click Update Controls | Card controls updated successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank |  | 1. Leave the Account to Link field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Leave the Shipping Address field blank |  | 1. Leave the Shipping Address field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating it is required | high |
| TC-005 |  | Submit the Card Request Form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Request Card | Form does not submit; error shown on Account to Link and Shipping Address fields | high |
| TC-006 |  | Submit with an incomplete Shipping Address |  | 1. Fill the Account to Link field<br>2. Fill the Shipping Address field with an incomplete address<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-007 |  | Leave the Select Existing Card field blank |  | 1. Leave the Select Existing Card field blank<br>2. Fill all other required fields<br>3. Click Update Controls | Inline validation error appears on the Select Existing Card field indicating it is required | high |
| TC-008 |  | Leave the New Spending Limit field blank |  | 1. Leave the New Spending Limit field blank<br>2. Fill all other required fields<br>3. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating it is required | high |
| TC-009 |  | Submit the Card Controls Form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Controls | Form does not submit; error shown on Select Existing Card, New Spending Limit, and Card Status fields | high |
| TC-010 |  | Submit with an invalid New Spending Limit |  | 1. Fill the Select Existing Card field<br>2. Fill the New Spending Limit field with <non-numeric input><br>3. Fill all other required fields<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating 'must be a valid numeric limit' | high |
| TC-011 |  | Submit with an invalid date range in Travel Notice |  | 1. Fill the Select Existing Card field<br>2. Fill the New Spending Limit field<br>3. Fill the Travel Notice with Start_Date after End_Date<br>4. Click Update Controls | Inline validation error appears indicating 'valid date ranges' | high |
| TC-012 |  | Attempt to update controls without account in good standing | account must be in good standing | 1. Fill all required fields in Card Controls Form<br>2. Click Update Controls | Form does not submit; error shown indicating account must be in good standing | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Submit card request with incomplete address | Account is in good standing | 1. Select 'Debit' from Card Type dropdown<br>2. Enter incomplete address in Shipping Address field<br>3. Select an account to link<br>4. Click 'Request Card' | Form submission is blocked; an error message indicates that the address must be complete | medium |
| TC-014 (boundary) | WF-002 | Submit card controls with invalid numeric limit | Select an existing card | 1. Enter a negative number in New Spending Limit field<br>2. Select Active from Card Status dropdown<br>3. Click 'Update Controls' | Form submission is blocked; an inline error message indicates that the limit must be a valid numeric limit | medium |
| TC-015 (boundary) | WF-002 | Submit card controls with valid date range | Select an existing card | 1. Enter a valid destination in Travel Notice<br>2. Enter today's date in Start Date field<br>3. Enter a date in the future in End Date field<br>4. Click 'Update Controls' | Form submits successfully; displays 'Card controls updated successfully.' | medium |
| TC-016 (input_edge) |  | Enter long text in Shipping Address |  | 1. Enter a very long string (200+ characters) in Shipping Address field<br>2. Click 'Request Card' | Form submission is blocked; an error message indicates the address must be complete | low |

---

## Investments

Total: **18** (positive: 3, negative: 10, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Execute Trade for Buy action | User logged in as <Role>, Customer has sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | Trade executed successfully with order ID | high |
| TC-002 | WF-002 | Execute Trade for Sell action | User logged in as <Role>, Customer has sufficient share balance | 1. Select 'Sell' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | Trade executed successfully with order ID | high |
| TC-003 | WF-003 | Create Recurring Investment Plan | User logged in as <Role>, Funding account has adequate balance | 1. Enter <valid fund symbol> in the Fund Symbol field<br>2. Enter <valid contribution amount meeting minimum> in the Contribution Amount field<br>3. Select <valid frequency> from the Frequency dropdown<br>4. Enter <valid future date> in the Start Date field<br>5. Select <valid funding account> from the Funding Account dropdown<br>6. Click Create Plan | Plan created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Quantity field blank and submit |  | 1. Select 'Buy' from the Action dropdown<br>2. Leave the Quantity field blank<br>3. Fill in the Fund Symbol and Funding or Destination Account<br>4. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-005 |  | Enter a Quantity of zero and submit |  | 1. Select 'Buy' from the Action dropdown<br>2. Enter '0' in the Quantity field<br>3. Fill in the Fund Symbol and Funding or Destination Account<br>4. Click Execute Trade | Inline validation error appears on the Quantity field indicating it must be greater than zero | high |
| TC-006 |  | Submit with all required fields empty in Trade Funds Form |  | 1. Click Execute Trade | Form does not submit; error shown on Action, Fund Symbol, Quantity, and Funding or Destination Account fields | high |
| TC-007 |  | Enter an invalid Fund Symbol and submit |  | 1. Select 'Buy' from the Action dropdown<br>2. Enter <invalid fund symbol> in the Fund Symbol field<br>3. Enter '1' in the Quantity field<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating symbol must exist | high |
| TC-008 |  | Enter a Contribution Amount below minimum and submit |  | 1. Click Create Plan in the Recurring Investment Plan Form<br>2. Enter <amount below minimum> in the Contribution Amount field<br>3. Fill in the Fund Symbol, Frequency, Start Date, and Funding Account<br>4. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it must meet minimum | high |
| TC-009 |  | Enter a Start Date in the past and submit |  | 1. Click Create Plan in the Recurring Investment Plan Form<br>2. Enter <past date> in the Start Date field<br>3. Fill in the Fund Symbol, Contribution Amount, Frequency, and Funding Account<br>4. Click Create Plan | Inline validation error appears on the Start Date field indicating it must be in the future | high |
| TC-010 |  | Submit with all required fields empty in Recurring Investment Plan Form |  | 1. Click Create Plan | Form does not submit; error shown on Fund Symbol, Contribution Amount, Frequency, Start Date, and Funding Account fields | high |
| TC-011 |  | Submit with a Funding Account that has inadequate balance |  | 1. Click Create Plan in the Recurring Investment Plan Form<br>2. Fill in the Fund Symbol, Contribution Amount, Frequency, Start Date<br>3. Select a Funding Account with inadequate balance<br>4. Click Create Plan | Inline validation error appears indicating funding account must have adequate balance | high |
| TC-012 | WF-001 | Attempt to execute trade without sufficient buying power |  | 1. Select 'Buy' from the Action dropdown<br>2. Enter '1' in the Quantity field<br>3. Fill in the Fund Symbol and Funding or Destination Account<br>4. Click Execute Trade | Form does not submit; error shown indicating customer must have sufficient buying power or share balance | high |
| TC-013 | WF-003 | Attempt to create a recurring investment plan without adequate balance in funding account |  | 1. Click Create Plan in the Recurring Investment Plan Form<br>2. Fill in the Fund Symbol, Contribution Amount, Frequency, Start Date<br>3. Select a Funding Account with inadequate balance<br>4. Click Create Plan | Form does not submit; error shown indicating funding account must have adequate balance | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Quantity is exactly 1 | User selects 'Buy' from Action dropdown, User selects a valid Fund Symbol, User has sufficient buying power | 1. Enter '1' in the Quantity field<br>2. Select a Funding or Destination Account<br>3. Click Execute Trade | Trade executed successfully with order ID is displayed | medium |
| TC-015 (boundary) | WF-001 | Quantity is 0 | User selects 'Buy' from Action dropdown, User selects a valid Fund Symbol, User has sufficient buying power | 1. Enter '0' in the Quantity field<br>2. Select a Funding or Destination Account<br>3. Click Execute Trade | Inline error displayed indicating Quantity must be greater than zero | medium |
| TC-016 (boundary) | WF-003 | Start Date is today | User selects a valid Fund Symbol, User enters a valid Contribution Amount, User selects a Funding Account | 1. Enter today's date in the Start Date field<br>2. Select Frequency<br>3. Click Create Plan | Inline error displayed indicating Start date must be in the future | medium |
| TC-017 (boundary) | WF-003 | Contribution Amount meets minimum | User selects a valid Fund Symbol, User selects a Funding Account, User enters a valid Start Date | 1. Enter the minimum required Contribution Amount in the Contribution Amount field<br>2. Select Frequency<br>3. Click Create Plan | Plan created successfully is displayed | medium |
| TC-018 (boundary) | WF-003 | Contribution Amount is below minimum | User selects a valid Fund Symbol, User selects a Funding Account, User enters a valid Start Date | 1. Enter an amount below the minimum in the Contribution Amount field<br>2. Select Frequency<br>3. Click Create Plan | Inline error displayed indicating Contribution Amount must meet minimum | medium |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate statement with valid date range and account selection | User logged in as <Role>, Valid date range is available | 1. Select <valid account> from the Account dropdown<br>2. Enter <valid start date> and <valid end date> in the Statement Period fields<br>3. Click Generate Statement | Statement generated successfully. | high |
| TC-002 | WF-002 | Save e-statement preference with valid email address | User logged in as <Role> | 1. Enter <valid email> in the Email Address field<br>2. Check the Opt into Paperless Statements checkbox<br>3. Click Save Preference | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account dropdown blank and submit |  | 1. Leave the Account dropdown blank<br>2. Fill in the Statement Period with valid dates<br>3. Click Generate Statement | Inline validation error appears on the Account field indicating it is required | high |
| TC-004 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Click Save Preference | Inline validation error appears on the Email Address field indicating it is required | high |
| TC-005 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email Address field<br>2. Click Save Preference | Inline validation error appears on the Email Address field indicating it must be a valid email format | medium |
| TC-006 |  | Submit with an invalid Statement Period date range |  | 1. Enter <invalid date range> in the Statement Period field<br>2. Select a valid Account<br>3. Click Generate Statement | Inline validation error appears on the Statement Period field indicating valid date range required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Test valid date range for Statement Period | User is on the Statements page | 1. Select a valid date range for the Statement Period.<br>2. Select an account from the dropdown.<br>3. Click Generate Statement. | Statement generated successfully. | medium |
| TC-008 (boundary) | WF-001 | Test invalid date range for Statement Period | User is on the Statements page | 1. Select an invalid date range for the Statement Period.<br>2. Select an account from the dropdown.<br>3. Click Generate Statement. | Unable to generate statement — please try again later. | medium |
| TC-009 (boundary) | WF-002 | Test valid email format for Email Address | User is on the e-Statement Preference form | 1. Enter a valid email address in the Email Address field.<br>2. Optionally, check the Opt into Paperless Statements checkbox.<br>3. Click Save Preference. | e-Statement preference updated. | medium |
| TC-010 (boundary) | WF-002 | Test invalid email format for Email Address | User is on the e-Statement Preference form | 1. Enter an invalid email address in the Email Address field.<br>2. Click Save Preference. | highlights email field with guidance. | medium |

---

## Security Settings

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Change Password Successfully | User logged in as <Role> | 1. Enter <valid current password> in the Current Password field<br>2. Enter <valid new password> in the New Password field<br>3. Enter the same <valid new password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave Current Password blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 | WF-001 | Leave New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Leave the New Password field blank<br>3. Fill Confirm New Password with valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 | WF-001 | Leave Confirm New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 | WF-001 | Enter incorrect Current Password |  | 1. Fill Current Password with invalid value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with the same valid value<br>4. Click Change Password | Inline validation error appears on the Current Password field indicating 'must verify current password' | high |
| TC-006 | WF-001 | Enter New Password that does not meet strong-password policy |  | 1. Fill Current Password with valid value<br>2. Fill New Password with invalid value<br>3. Fill Confirm New Password with the same invalid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'must meet strong-password policy' | high |
| TC-007 | WF-001 | Enter mismatched New Password and Confirm New Password |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with a different value<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'must match New Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter a strong password that meets all criteria | User is logged in and on the Security Settings page | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a strong password in the New_Password field<br>3. Enter the same strong password in the Confirm_New_Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) | WF-001 | Enter a New Password that does not meet strong-password policy | User is logged in and on the Security Settings page | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a weak password in the New_Password field<br>3. Enter the same weak password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the New_Password field indicating it does not meet the strong-password policy. | medium |
| TC-010 (boundary) | WF-001 | Enter New Password and Confirm New Password that do not match | User is logged in and on the Security Settings page | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a strong password in the New_Password field<br>3. Enter a different strong password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the Confirm_New_Password field indicating it must match the New Password. | medium |
| TC-011 (input_edge) | WF-001 | Enter a very long New Password | User is logged in and on the Security Settings page | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a New Password that is excessively long (over 100 characters)<br>3. Enter the same long password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the New_Password field indicating it exceeds the maximum allowed length. | low |

---

## Support Center

Total: **14** (positive: 3, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send Message without Attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Account' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click Send Message | Message sent successfully with ticket ID | high |
| TC-002 | WF-002 | Send Message with Attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click 'Upload' and select a <valid attachment type><br>5. Click Send Message | Message sent successfully with ticket ID | high |
| TC-003 | WF-003 | Request Callback | User logged in as <Role> | 1. Select <valid reason> from the Reason for Call dropdown<br>2. Enter <valid date> in the Preferred Date field<br>3. Enter <valid time window> in the Preferred Time Window field<br>4. Verify Phone Number field is pre-filled and editable<br>5. Click Request Callback | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Message Body field blank and submit |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject field with valid text<br>3. Select a Category from the dropdown<br>4. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-005 |  | Leave the Subject field blank and submit |  | 1. Leave the Subject field blank<br>2. Fill in the Message Body with valid text<br>3. Select a Category from the dropdown<br>4. Click Send Message | Inline validation error appears on the Subject field indicating it must be valid | high |
| TC-006 |  | Submit with an invalid phone number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Select a Reason for Call from the dropdown<br>3. Enter a Preferred Date that is valid<br>4. Click Request Callback | Inline validation error appears on the Phone Number field indicating the format must be valid | high |
| TC-007 |  | Select a Preferred Date that is not the next business day |  | 1. Select a Preferred Date that is not the next business day<br>2. Select a Reason for Call from the dropdown<br>3. Enter a valid Phone Number<br>4. Click Request Callback | Inline validation error appears on the Preferred Date field indicating the date must be at least the next business day | high |
| TC-008 |  | Submit the secure message form with an invalid attachment type |  | 1. Fill in the Subject field with valid text<br>2. Select a Category from the dropdown<br>3. Fill in the Message Body with valid text<br>4. Upload an invalid attachment type<br>5. Click Send Message | Inline validation error appears on the Attachment field indicating attachment types must be valid | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Subject field at minimum length |  | 1. Enter a valid minimum length subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Click Send Message | Message sent successfully with ticket ID | medium |
| TC-010 (boundary) | WF-001 | Subject field below minimum length |  | 1. Enter a subject that is one character below the minimum length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Click Send Message | Inline guidance displays an error indicating the subject length is invalid | medium |
| TC-011 (boundary) | WF-003 | Preferred Date is the next business day |  | 1. Select a reason for the call from the dropdown<br>2. Enter the date of the next business day in the Preferred Date field<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Callback request submitted and email confirmation sent | medium |
| TC-012 (boundary) | WF-003 | Preferred Date before the next business day |  | 1. Select a reason for the call from the dropdown<br>2. Enter a date that is one day before the next business day in the Preferred Date field<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Inline guidance displays an error indicating the date must be at least the next business day | medium |
| TC-013 (input_edge) |  | Long subject text |  | 1. Enter a very long subject text (200+ characters) in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Click Send Message | Inline guidance displays an error indicating the subject length is invalid | low |
| TC-014 (input_edge) |  | Special characters in message body |  | 1. Enter a message body with special characters in the Message Body field<br>2. Click Send Message | Message sent successfully with ticket ID | low |

---
