# Test Cases — Parabank

Generated: 2026-06-10T20:12:21.006470Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 190 | 22 | 103 | 65 | 105 | 66 | 19 |

## Login

Total: **12** (positive: 1, negative: 6, edge: 5)

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
| TC-005 |  | Enter a password that does not meet the complexity requirements and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Enter a password that does not include required character types and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password without uppercase letters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 | WF-002 | Submit with incorrect email and password |  | 1. Fill the Email_Username field with <invalid email><br>2. Fill the Password field with <invalid password><br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Email field with valid format edge case |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'ValidPass1!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-009 (boundary) |  | Password field with minimum length edge case |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Pass1!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-010 (boundary) |  | Password field just below minimum length |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Pass1' in the Password field<br>3. Click Sign In | Form submission is blocked; error message displayed indicating password requirements. | medium |
| TC-011 (input_edge) |  | Email field with invalid format |  | 1. Enter 'invalid-email' in the Email/Username field<br>2. Enter 'ValidPass1!' in the Password field<br>3. Click Sign In | Form submission is blocked; error message displayed indicating invalid email format. | low |
| TC-012 (input_edge) |  | Password field with special characters only |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter '@#$%^&*()' in the Password field<br>3. Click Sign In | Form submission is blocked; error message displayed indicating password requirements. | low |

---

## Register

Total: **29** (positive: 1, negative: 18, edge: 10)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid inputs | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Enter <valid SSN> in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <valid password> in the Password field<br>11. Enter the same <valid password> in the Confirm Password field<br>12. Click Register | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Leave the Social Security Number field blank |  | 1. Leave the Social Security Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it is required | high |
| TC-010 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it is required | high |
| TC-011 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Leave the Confirm Password field blank |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-013 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Register | Form does not submit; error shown on First_Name, Last_Name, Street_Address, City, State, ZIP_Code, Phone_Number, Social_Security_Number, Username, Password, Confirm_Password fields | high |
| TC-014 |  | Enter invalid format in ZIP Code field |  | 1. Enter <invalid ZIP Code format> in the ZIP_Code field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it must be 5 digits or 5+4 format | medium |
| TC-015 |  | Enter invalid format in Phone Number field |  | 1. Enter <invalid Phone Number format> in the Phone_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it must follow format (123) 456-7890 | medium |
| TC-016 |  | Enter invalid format in Social Security Number field |  | 1. Enter <invalid Social Security Number format> in the Social_Security_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it must follow format 123-45-6789 | medium |
| TC-017 |  | Enter invalid format in Username field |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it must be a valid email format | medium |
| TC-018 |  | Enter short password in Password field |  | 1. Enter <password shorter than 8 characters> in the Password field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-019 |  | Enter mismatched passwords |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Register | Inline validation error appears on the Confirm_Password field indicating it must match Password | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 (boundary) |  | ZIP Code with exactly 5 digits |  | 1. Enter exactly 5 digits in the ZIP Code field | Form submits successfully; entity is created with the ZIP Code 12345 | medium |
| TC-021 (boundary) |  | ZIP Code with 5+4 format |  | 1. Enter 5 digits followed by a hyphen and 4 digits in the ZIP Code field | Form submits successfully; entity is created with the ZIP Code 12345-6789 | medium |
| TC-022 (boundary) |  | ZIP Code with one digit below minimum |  | 1. Enter 4 digits in the ZIP Code field | ZIP Code field displays an error indicating the value is below the minimum allowed | medium |
| TC-023 (boundary) |  | Phone Number with correct format |  | 1. Enter a valid phone number in the format (123) 456-7890 in the Phone Number field | Form submits successfully; entity is created with the Phone Number (123) 456-7890 | medium |
| TC-024 (boundary) |  | Phone Number with incorrect format |  | 1. Enter a phone number in an incorrect format in the Phone Number field | Phone Number field displays an error indicating the format is invalid | medium |
| TC-025 (boundary) |  | Password with exactly 8 characters |  | 1. Enter exactly 8 characters in the Password field | Form submits successfully; entity is created with the Password of 8 characters | medium |
| TC-026 (boundary) |  | Password with one character below minimum |  | 1. Enter 7 characters in the Password field | Password field displays an error indicating the value is below the minimum allowed | medium |
| TC-027 (input_edge) |  | Long text in First Name field |  | 1. Enter a string of 200 characters in the First Name field | First Name field displays an error indicating the value exceeds the maximum length | low |
| TC-028 (input_edge) |  | Special characters in Last Name field |  | 1. Enter special characters in the Last Name field | Last Name field displays an error indicating the value is invalid | low |
| TC-029 (input_edge) |  | Leading/trailing whitespace in Username field |  | 1. Enter leading and trailing spaces in the Username (email) field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounts Overview

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Verify the Accounts Table displays correctly | User logged in as <Role> | 1. Navigate to the Accounts Overview module | The Accounts Table displays all customer accounts with masked Account Numbers, Account Types, Current Balances, Account Statuses, and Open Dates. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view account number |  | 1. Click on the Account Number | Action is blocked; no account number is displayed as the feature is not implemented yet. | high |

---

## Open New Account

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Account with Checking type | User logged in as <role> | 1. Select 'Checking' from the Account Type options<br>2. Enter '25' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |
| TC-002 | WF-002 | Open Account with Savings type | User logged in as <role> | 1. Select 'Savings' from the Account Type options<br>2. Enter '100' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill in the Initial Deposit Amount and Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave the Initial Deposit Amount field blank and submit |  | 1. Select an Account Type<br>2. Leave the Initial Deposit Amount field blank<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Leave the Funding Source Account field blank and submit |  | 1. Select an Account Type<br>2. Fill in the Initial Deposit Amount<br>3. Leave the Funding Source Account field blank<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it is required | high |
| TC-006 |  | Enter a non-numeric value in the Initial Deposit Amount field |  | 1. Select an Account Type<br>2. Enter <non-numeric value> in the Initial Deposit Amount field<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-007 |  | Enter an Initial Deposit Amount below the minimum for Checking |  | 1. Select Checking as Account Type<br>2. Enter <amount below $25> in the Initial Deposit Amount field<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-008 |  | Enter an Initial Deposit Amount below the minimum for Savings |  | 1. Select Savings as Account Type<br>2. Enter <amount below $100> in the Initial Deposit Amount field<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-009 |  | Select a Funding Source Account with insufficient balance |  | 1. Select an Account Type<br>2. Fill in the Initial Deposit Amount<br>3. Select a Funding Source Account that has insufficient balance<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it must have sufficient balance | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Minimum deposit for Checking account | User selects Checking account type | 1. Enter exactly $25 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-011 (boundary) | WF-001 | Deposit below minimum for Checking account | User selects Checking account type | 1. Enter $24.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Real-time validation error displayed: 'Initial Deposit Amount must be at least $25 for Checking'. | medium |
| TC-012 (boundary) | WF-002 | Minimum deposit for Savings account | User selects Savings account type | 1. Enter exactly $100 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-013 (boundary) | WF-002 | Deposit below minimum for Savings account | User selects Savings account type | 1. Enter $99.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Real-time validation error displayed: 'Initial Deposit Amount must be at least $100 for Savings'. | medium |

---

## Transfer Funds

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Transfer to My ParaBank Account | User logged in as <User>, sufficient funds | 1. Select 'My ParaBank Account' from the Transfer Type radio buttons<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Select <valid internal account> from the Internal Accounts dropdown<br>5. Click Transfer | Transfer completed successfully. | high |
| TC-002 | WF-002 | Transfer to External Account | User logged in as <User>, sufficient funds | 1. Select 'External Account' from the Transfer Type radio buttons<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <valid external account number> in the Confirm Account Number field<br>6. Click Transfer | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Transfer Amount field blank |  | 1. Select 'My ParaBank Account' for Transfer Type<br>2. Leave the Transfer Amount field blank<br>3. Select a Source Account<br>4. Click Transfer | Form does not submit; Transfer Amount field displays an error: 'Must be a positive amount' | high |
| TC-004 |  | Enter a negative Transfer Amount |  | 1. Select 'My ParaBank Account' for Transfer Type<br>2. Enter <negative amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Click Transfer | Form does not submit; Transfer Amount field displays an error: 'Must be a positive amount' | high |
| TC-005 |  | Leave External Account Number blank for external transfer |  | 1. Select 'External Account' for Transfer Type<br>2. Leave the External Account Number field blank<br>3. Leave the Confirm Account Number field blank<br>4. Click Transfer | Form does not submit; External Account Number field displays an error: 'This field is required' | high |
| TC-006 |  | Leave Confirm Account Number blank for external transfer |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Leave the Confirm Account Number field blank<br>4. Click Transfer | Form does not submit; Confirm Account Number field displays an error: 'This field is required' | high |
| TC-007 |  | Enter mismatched account numbers for external transfer |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <different account number> in the Confirm Account Number field<br>4. Click Transfer | Form does not submit; Confirm Account Number field displays an error: 'Account numbers do not match' | high |
| TC-008 | WF-002 | Attempt transfer without sufficient funds | insufficient funds | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <valid amount> in the Transfer Amount field<br>4. Click Transfer | Form does not submit; error shown: 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Transfer amount is zero | Transfer_Type is set to External Account, Source_Account is selected | 1. Enter 0 in the Transfer_Amount field<br>2. Enter a valid External_Account_Number<br>3. Enter the same External_Account_Number in Confirm_Account_Number<br>4. Click Transfer | Transfer is blocked; an error message displays indicating 'Transfer amount must be valid.' | medium |
| TC-010 (boundary) | WF-002 | Transfer amount is just above zero | Transfer_Type is set to External Account, Source_Account is selected | 1. Enter 0.01 in the Transfer_Amount field<br>2. Enter a valid External_Account_Number<br>3. Enter the same External_Account_Number in Confirm_Account_Number<br>4. Click Transfer | Transfer completes successfully; 'Transfer completed successfully.' message is shown. | medium |
| TC-011 (boundary) | WF-002 | Account number mismatch | Transfer_Type is set to External Account, Source_Account is selected | 1. Enter a valid Transfer_Amount<br>2. Enter a valid External_Account_Number<br>3. Enter a different number in Confirm_Account_Number<br>4. Click Transfer | Transfer is blocked; an error message displays indicating 'Account numbers do not match.' | medium |
| TC-012 (boundary) | WF-001 | Transfer amount is just above zero for internal transfer | Transfer_Type is set to My ParaBank Account, Source_Account is selected | 1. Enter 0.01 in the Transfer_Amount field<br>2. Select an Internal_Account from the dropdown<br>3. Click Transfer | Transfer completes successfully; 'Transfer completed successfully.' message is shown. | medium |
| TC-013 (input_edge) |  | Leading/trailing whitespace in account number fields | Transfer_Type is set to External Account, Source_Account is selected | 1. Enter ' 123456 ' in the External_Account_Number field<br>2. Enter ' 123456 ' in the Confirm_Account_Number field<br>3. Click Transfer | Leading/trailing whitespace is trimmed; Transfer completes successfully. | low |
| TC-014 (input_edge) |  | Special characters in account number fields | Transfer_Type is set to External Account, Source_Account is selected | 1. Enter '1234@56' in the External_Account_Number field<br>2. Enter '1234@56' in the Confirm_Account_Number field<br>3. Click Transfer | Transfer is blocked; an error message displays indicating invalid characters. | low |

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
| TC-012 | WF-002 | Submit payment with account number mismatch |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <different value> in the Confirm_Account_Number field<br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating 'Account numbers do not match' | high |
| TC-013 | WF-003 | Submit payment with insufficient funds |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <valid value> in the Confirm_Account_Number field<br>3. Enter <amount exceeding available balance> in the Payment_Amount field<br>4. Fill all other required fields<br>5. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-002 | Account number mismatch on confirmation | Payee Account Number is set to a valid value | 1. Enter a different value in the Confirm Account Number field than the Payee Account Number<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline error displays: 'Account numbers do not match' | medium |
| TC-015 (boundary) | WF-003 | Payment submission with insufficient funds | Payment Amount exceeds available funds in Source Account | 1. Fill all required fields with valid data<br>2. Enter a Payment Amount that exceeds available funds<br>3. Click Pay | Inline error displays: 'Insufficient funds' | medium |
| TC-016 (input_edge) |  | Special characters in Payee Name |  | 1. Enter special characters in the Payee Name field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Form submits successfully; payment is processed with the special characters retained in the Payee Name | low |
| TC-017 (input_edge) |  | Leading/trailing whitespace in Phone Number |  | 1. Enter leading and trailing spaces in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Request Loan

Total: **20** (positive: 3, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Request for Personal Loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Personal' from the Loan Type cards<br>2. Enter 15000 in the Loan Amount field<br>3. Enter 1500 in the Down Payment Amount field<br>4. Select a <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |
| TC-002 | WF-002 | Submit Loan Request for Auto Loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Auto' from the Loan Type cards<br>2. Enter 30000 in the Loan Amount field<br>3. Enter 3000 in the Down Payment Amount field<br>4. Select a <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |
| TC-003 | WF-003 | Submit Loan Request for Home Loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Home' from the Loan Type cards<br>2. Enter 200000 in the Loan Amount field<br>3. Enter 20000 in the Down Payment Amount field<br>4. Select a <valid collateral account> from the Collateral Account dropdown<br>5. Click Submit Loan Request | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Loan Amount field blank and submit |  | 1. Leave the Loan Amount field blank<br>2. Fill all other required fields<br>3. Click Submit Loan Request | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Leave the Down Payment Amount field blank and submit |  | 1. Select a Loan Type<br>2. Leave the Down Payment Amount field blank<br>3. Fill all other required fields<br>4. Click Submit Loan Request | Inline validation error appears on the Down Payment Amount field indicating it is required | high |
| TC-006 |  | Enter a Down Payment Amount less than 10% of Loan Amount |  | 1. Select a Loan Type<br>2. Enter <amount less than 10% of Loan Amount> in the Down Payment Amount field<br>3. Fill all other required fields<br>4. Click Submit Loan Request | Form does not submit; error shown on Down Payment Amount field indicating it must be at least 10% of Loan Amount | high |
| TC-007 |  | Enter a Down Payment Amount greater than Loan Amount |  | 1. Select a Loan Type<br>2. Enter <amount greater than Loan Amount> in the Down Payment Amount field<br>3. Fill all other required fields<br>4. Click Submit Loan Request | Form does not submit; error shown on Down Payment Amount field indicating it must be less than Loan Amount | high |
| TC-008 |  | Enter a Collateral Account with insufficient funds |  | 1. Select a Loan Type<br>2. Enter a valid Loan Amount<br>3. Enter a valid Down Payment Amount<br>4. Select a Collateral Account with insufficient funds<br>5. Click Submit Loan Request | Form does not submit; error shown indicating 'must have sufficient collateral funds' | high |
| TC-009 |  | Enter a Collateral Account with less than 20% of collateral value |  | 1. Select a Loan Type<br>2. Enter a valid Loan Amount<br>3. Enter a valid Down Payment Amount<br>4. Select a Collateral Account with less than 20% of collateral value<br>5. Click Submit Loan Request | Form does not submit; error shown indicating 'must be at least 20% of collateral value' | high |
| TC-010 | WF-001 | Attempt to submit a loan request without meeting credit approval precondition |  | 1. Select Loan Type as Personal<br>2. Enter a valid Loan Amount<br>3. Enter a valid Down Payment Amount<br>4. Select a valid Collateral Account<br>5. Click Submit Loan Request | Form does not submit; error shown indicating 'Insufficient credit history' | high |
| TC-011 | WF-002 | Attempt to submit a loan request without meeting credit approval precondition for Auto Loan |  | 1. Select Loan Type as Auto<br>2. Enter a valid Loan Amount<br>3. Enter a valid Down Payment Amount<br>4. Select a valid Collateral Account<br>5. Click Submit Loan Request | Form does not submit; error shown indicating 'Insufficient credit history' | high |
| TC-012 | WF-003 | Attempt to submit a loan request without meeting credit approval precondition for Home Loan |  | 1. Select Loan Type as Home<br>2. Enter a valid Loan Amount<br>3. Enter a valid Down Payment Amount<br>4. Select a valid Collateral Account<br>5. Click Submit Loan Request | Form does not submit; error shown indicating 'Insufficient credit history' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Test minimum loan amount for Personal loan | Select Loan Type as Personal | 1. Enter exactly $1,000 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Loan approved and created successfully! | medium |
| TC-014 (boundary) | WF-001 | Test maximum loan amount for Personal loan | Select Loan Type as Personal | 1. Enter exactly $50,000 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Loan approved and created successfully! | medium |
| TC-015 (boundary) | WF-001 | Test loan amount just below minimum for Personal loan | Select Loan Type as Personal | 1. Enter $999 in the Loan Amount field<br>2. Enter $99 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Submission is blocked; error shown indicating Loan Amount must be at least $1,000. | medium |
| TC-016 (boundary) | WF-001 | Test down payment exactly 10% of loan amount for Personal loan | Select Loan Type as Personal | 1. Enter $10,000 in the Loan Amount field<br>2. Enter $1,000 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Loan approved and created successfully! | medium |
| TC-017 (boundary) | WF-002 | Test maximum loan amount for Auto loan | Select Loan Type as Auto | 1. Enter exactly $75,000 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Loan approved and created successfully! | medium |
| TC-018 (boundary) | WF-002 | Test loan amount just above maximum for Auto loan | Select Loan Type as Auto | 1. Enter $75,001 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Submission is blocked; error shown indicating Loan Amount must be less than or equal to $75,000. | medium |
| TC-019 (boundary) | WF-003 | Test minimum loan amount for Home loan | Select Loan Type as Home | 1. Enter exactly $50,000 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Loan approved and created successfully! | medium |
| TC-020 (boundary) | WF-003 | Test down payment just below minimum for Home loan | Select Loan Type as Home | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $4,999 in the Down Payment Amount field<br>3. Select a Collateral Account with sufficient funds<br>4. Click Submit Loan Request | Submission is blocked; error shown indicating Down Payment Amount must be at least 10% of Loan Amount. | medium |

---

## Update Contact Info

Total: **20** (positive: 1, negative: 15, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid contact information | User logged in as <Customer>, Profile form is pre-filled with valid data | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Enter <valid state> in the State field<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click Update Profile | Profile updated successfully. | high |

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
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Form does not submit; error shown on all required fields | high |
| TC-010 |  | Enter invalid format in First Name field |  | 1. Enter <invalid format> in the First_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it must be a valid format | medium |
| TC-011 |  | Enter invalid format in Last Name field |  | 1. Enter <invalid format> in the Last_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it must be a valid format | medium |
| TC-012 |  | Enter invalid format in Street Address field |  | 1. Enter <invalid format> in the Street_Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it must be a valid format | medium |
| TC-013 |  | Enter invalid format in City field |  | 1. Enter <invalid format> in the City field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it must be a valid format | medium |
| TC-014 |  | Enter invalid format in State field |  | 1. Enter <invalid format> in the State field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it must be a valid format | medium |
| TC-015 |  | Enter invalid format in ZIP Code field |  | 1. Enter <invalid format> in the ZIP_Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it must be a valid format | medium |
| TC-016 |  | Enter invalid format in Phone Number field |  | 1. Enter <invalid format> in the Phone_Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it must be a valid format | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline error banner displays indicating the First Name format is invalid | low |
| TC-018 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter '@#$%' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline error banner displays indicating the Last Name format is invalid | low |
| TC-019 (input_edge) |  | Enter a ZIP Code with leading/trailing whitespace |  | 1. Enter ' 12345 ' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Saved value in the detail page shows '12345' without leading/trailing spaces | low |
| TC-020 (input_edge) |  | Enter a valid Phone Number with special characters |  | 1. Enter '(123) 456-7890' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline error banner displays indicating the Phone Number format is invalid | low |

---

## Manage Cards

Total: **13** (positive: 2, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Card Request Form with valid data | User logged in as <Role> | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click Request Card | Card request submitted successfully. | high |
| TC-002 | WF-002 | Update Card Controls with valid data | User logged in as <Role> | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid numeric limit> in the New Spending Limit field<br>3. Select 'Active' from the Card Status dropdown<br>4. Click Update Controls | Card controls updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank and submit |  | 1. Leave the Account to Link field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Leave the Shipping Address field blank and submit |  | 1. Leave the Shipping Address field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating it is required | high |
| TC-005 |  | Submit the Card Request form with all required fields empty |  | 1. Leave the Card Type field blank<br>2. Leave the Account to Link field blank<br>3. Leave the Shipping Address field blank<br>4. Click Request Card | Form does not submit; error shown on Account to Link and Shipping Address fields | high |
| TC-006 |  | Submit with a non-numeric New Spending Limit |  | 1. Select an Existing Card<br>2. Enter <non-numeric value> in the New Spending Limit field<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating it must be numeric | high |
| TC-007 |  | Submit with New Spending Limit exceeding policy |  | 1. Select an Existing Card<br>2. Enter <amount exceeding policy> in the New Spending Limit field<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating it must be within policy | high |
| TC-008 |  | Submit with an invalid Card Status transition |  | 1. Select an Existing Card<br>2. Enter a valid New Spending Limit<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears indicating the status must follow allowable transitions | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit card request with incomplete address | User is on the Manage Cards page | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter a valid Account to Link<br>3. Leave the Shipping Address field incomplete<br>4. Click 'Request Card' | Form submission is blocked; inline error indicates address must be complete. | medium |
| TC-010 (boundary) | WF-002 | Submit card controls with spending limit exceeding policy | User is on the Manage Cards page | 1. Select an existing card from the Select Existing Card dropdown<br>2. Enter a spending limit above the policy limit<br>3. Select 'Active' from the Card Status dropdown<br>4. Click 'Update Controls' | Form submission is blocked; inline error indicates the limit must be within policy. | medium |
| TC-011 (boundary) | WF-002 | Submit card controls with minimum numeric spending limit | User is on the Manage Cards page | 1. Select an existing card from the Select Existing Card dropdown<br>2. Enter the minimum allowed spending limit<br>3. Select 'Active' from the Card Status dropdown<br>4. Click 'Update Controls' | Form submits successfully; card controls updated successfully. | medium |
| TC-012 (input_edge) |  | Enter long text in the Account to Link field | User is on the Manage Cards page | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter a very long string (200+ characters) in the Account to Link field<br>3. Enter a valid Shipping Address<br>4. Click 'Request Card' | Form submission is blocked; inline error indicates the input is too long. | low |
| TC-013 (input_edge) |  | Enter special characters in the Shipping Address field | User is on the Manage Cards page | 1. Select 'Credit' from the Card Type dropdown<br>2. Enter a valid Account to Link<br>3. Enter special characters in the Shipping Address field<br>4. Click 'Request Card' | Form submission is blocked; inline error indicates the address must be complete. | low |

---

## Investments

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Execute a trade successfully | User logged in as <Role>, Customer has sufficient buying power or share balance | 1. Select 'Buy' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | executes same-day trade, updates holdings, displays 'Trade executed successfully.' with order ID | high |
| TC-002 | WF-002 | Create a recurring investment plan successfully | User logged in as <Role>, Funding account has adequate balance | 1. Enter <valid fund symbol> in the Fund Symbol field<br>2. Enter <valid contribution amount meeting minimum> in the Contribution Amount field<br>3. Select 'Weekly' from the Frequency dropdown<br>4. Enter a future date in the Start Date field<br>5. Select <valid funding account> from the Funding Account dropdown<br>6. Click Create Plan | stores the schedule, shows 'Plan created successfully.' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Quantity field blank and submit |  | 1. Leave the Quantity field blank<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-004 |  | Enter a Quantity of zero and submit |  | 1. Enter 0 in the Quantity field<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating 'must be greater than zero' | high |
| TC-005 |  | Select a non-existent Fund Symbol and submit |  | 1. Enter <non-existent symbol> in the Fund Symbol field<br>2. Fill all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating 'symbol must exist' | high |
| TC-006 |  | Leave the Contribution Amount field blank and submit |  | 1. Leave the Contribution Amount field blank<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it is required | high |
| TC-007 |  | Enter a Contribution Amount below the minimum and submit |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating 'must meet minimum contribution' | high |
| TC-008 |  | Select a Funding Account with inadequate balance and submit |  | 1. Select <account with inadequate balance> in the Funding Account field<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Funding Account field indicating 'must have adequate balance' | high |
| TC-009 |  | Enter a Start Date in the past and submit |  | 1. Enter <past date> in the Start Date field<br>2. Fill all other required fields<br>3. Click Create Plan | Inline validation error appears on the Start Date field indicating 'must be in the future' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Quantity exactly one | User is logged in with sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter 'AAPL' in the Fund Symbol field<br>3. Enter '1' in the Quantity field<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Trade executed successfully. with order ID is displayed | medium |
| TC-011 (boundary) | WF-001 | Quantity one less than minimum | User is logged in with sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter 'AAPL' in the Fund Symbol field<br>3. Enter '0' in the Quantity field<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Inline error appears indicating 'Quantity must be greater than zero' | medium |
| TC-012 (boundary) | WF-002 | Start Date exactly today | User is logged in with adequate balance | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Monthly' from the Frequency dropdown<br>4. Enter today's date in the Start Date field<br>5. Select a Funding Account<br>6. Click Create Plan | Inline error appears indicating 'Start date must be in the future' | medium |
| TC-013 (boundary) | WF-002 | Start Date one day in the future | User is logged in with adequate balance | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Monthly' from the Frequency dropdown<br>4. Enter a date one day in the future in the Start Date field<br>5. Select a Funding Account<br>6. Click Create Plan | Plan created successfully. is displayed | medium |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate statement with valid inputs | User logged in as <Role>, Valid date range is available, Account is selected | 1. Enter <valid date range> in the Statement Period field<br>2. Select <valid account> from the Account dropdown<br>3. Click Generate Statement | Statement generated successfully. | high |
| TC-002 | WF-002 | Save e-Statement preference with valid email | User logged in as <Role> | 1. Enter <valid email> in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Account dropdown blank and submit |  | 1. Leave the Account field blank<br>2. Fill the Statement Period with a valid date range<br>3. Click Generate Statement | Form does not submit; Account field is highlighted with an error indicating it is required | high |
| TC-004 | WF-001 | Submit with an invalid Statement Period date range |  | 1. Select a valid Account<br>2. Enter <invalid date range> in the Statement Period field<br>3. Click Generate Statement | Form does not submit; error shown indicating 'valid date range required' | high |
| TC-005 | WF-002 | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Click Save Preference | Form does not submit; Email Address field is highlighted with an error indicating it is required | high |
| TC-006 | WF-002 | Submit with an invalid Email Address format |  | 1. Enter <invalid email format> in the Email Address field<br>2. Click Save Preference | Form does not submit; Email Address field is highlighted with guidance indicating 'valid email format required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Enter a valid date range for Statement Period |  | 1. Select a valid date range in the Statement Period field<br>2. Select an account from the dropdown<br>3. Click Generate Statement | Statement generated successfully. | medium |
| TC-008 (boundary) | WF-001 | Enter an invalid date range for Statement Period |  | 1. Select an invalid date range in the Statement Period field<br>2. Select an account from the dropdown<br>3. Click Generate Statement | Unable to generate statement — please try again later. | medium |
| TC-009 (boundary) | WF-002 | Enter a valid email address |  | 1. Enter a valid email address in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | medium |
| TC-010 (boundary) | WF-002 | Enter an invalid email address |  | 1. Enter an invalid email address in the Email Address field<br>2. Click Save Preference | highlights email field with guidance | medium |

---

## Security Settings

Total: **12** (positive: 1, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Change Password Successfully | User logged in as <Role>, User knows their current password | 1. Enter <valid current password> in the Current Password field<br>2. Enter <valid new password> in the New Password field<br>3. Enter <same valid new password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave Current Password field blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill the New Password and Confirm New Password fields with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 |  | Leave New Password field blank and submit |  | 1. Fill the Current Password field with valid value<br>2. Leave the New Password field blank<br>3. Fill the Confirm New Password field with valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 |  | Leave Confirm New Password field blank and submit |  | 1. Fill the Current Password field with valid value<br>2. Fill the New Password field with valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 |  | Enter invalid Current Password and submit |  | 1. Fill the Current Password field with an invalid value<br>2. Fill the New Password field with valid value<br>3. Fill the Confirm New Password field with the same valid value<br>4. Click Change Password | Inline validation error appears on the Current Password field indicating 'must verify current password' | high |
| TC-006 |  | Enter New Password that does not meet strong-password policy |  | 1. Fill the Current Password field with valid value<br>2. Fill the New Password field with a weak password<br>3. Fill the Confirm New Password field with the same weak password<br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'must meet strong-password policy' | high |
| TC-007 |  | Enter mismatched New Password and Confirm New Password |  | 1. Fill the Current Password field with valid value<br>2. Fill the New Password field with a valid value<br>3. Fill the Confirm New Password field with a different value<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'must match New Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter a valid current password and a new password that meets the strong-password policy |  | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a New Password that meets the strong-password policy in the New_Password field<br>3. Enter the same New Password in the Confirm_New_Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) | WF-001 | Enter a New Password that is one character short of the strong-password policy |  | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a New Password that is one character short of the strong-password policy in the New_Password field<br>3. Enter the same New Password in the Confirm_New_Password field<br>4. Click Change Password | New Password displays an error indicating it does not meet the strong-password policy. | medium |
| TC-010 (boundary) | WF-001 | Enter a New Password and Confirm New Password that do not match |  | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a valid New Password in the New_Password field<br>3. Enter a different password in the Confirm_New_Password field<br>4. Click Change Password | Confirm New Password displays an error indicating it must match New Password. | medium |
| TC-011 (input_edge) | WF-001 | Enter a very long string in the New Password field |  | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a very long string (200+ characters) in the New_Password field<br>3. Enter the same very long string in the Confirm_New_Password field<br>4. Click Change Password | New Password displays an error indicating it exceeds the maximum length allowed. | low |
| TC-012 (input_edge) | WF-001 | Enter special characters in the New Password field |  | 1. Enter a valid Current Password in the Current_Password field<br>2. Enter a password with special characters in the New_Password field<br>3. Enter the same password with special characters in the Confirm_New_Password field<br>4. Click Change Password | Password changed successfully. | low |

---

## Support Center

Total: **15** (positive: 3, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send message without attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Account' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click Send Message | Message sent successfully with ticket ID | high |
| TC-002 | WF-002 | Send message with attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click Upload to select a <valid attachment><br>5. Click Send Message | Message sent successfully with ticket ID | high |
| TC-003 | WF-003 | Request callback | User logged in as <Role> | 1. Select <valid reason> from the Reason for Call dropdown<br>2. Enter <valid date> in the Preferred Date field<br>3. Enter <valid time window> in the Preferred Time Window field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Click Request Callback | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Message Body field blank and submit |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject and Category fields<br>3. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-005 |  | Leave the Subject field blank and submit |  | 1. Leave the Subject field blank<br>2. Fill in the Message Body and Category fields<br>3. Click Send Message | Inline validation error appears on the Subject field indicating it must be valid | high |
| TC-006 |  | Submit the Schedule Callback form with an invalid Phone Number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Select a Reason for Call<br>3. Enter a Preferred Date<br>4. Click Request Callback | Inline validation error appears on the Phone Number field indicating it must be valid | high |
| TC-007 |  | Submit the Schedule Callback form with a Preferred Date that is not the next business day |  | 1. Enter <date not the next business day> in the Preferred Date field<br>2. Select a Reason for Call<br>3. Enter a Phone Number<br>4. Click Request Callback | Inline validation error appears on the Preferred Date field indicating it must be at least the next business day | high |
| TC-008 | WF-001 | Submit the Secure Message Form without a Message Body |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject and Category fields<br>3. Click Send Message | Form does not submit; error shown on Message Body field | high |
| TC-009 | WF-003 | Submit the Schedule Callback form without selecting a Reason for Call |  | 1. Leave the Reason for Call field blank<br>2. Enter a Preferred Date<br>3. Enter a Phone Number<br>4. Click Request Callback | Inline validation error appears on the Reason for Call field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-002 | Attachment type validation edge case | User is on the Secure Message Form | 1. Enter a valid Subject in the Subject field<br>2. Select a Category from the dropdown<br>3. Enter a Message Body<br>4. Upload an attachment of a valid type (e.g., .pdf)<br>5. Click Send Message | Message sent successfully with ticket ID | medium |
| TC-011 (boundary) | WF-002 | Attachment type rejection edge case | User is on the Secure Message Form | 1. Enter a valid Subject in the Subject field<br>2. Select a Category from the dropdown<br>3. Enter a Message Body<br>4. Upload an attachment of an invalid type (e.g., .exe)<br>5. Click Send Message | Error displayed indicating invalid attachment type | medium |
| TC-012 (boundary) | WF-003 | Preferred Date boundary case | User is on the Schedule Callback Form | 1. Select a Reason for Call from the dropdown<br>2. Enter today's date in the Preferred Date field<br>3. Enter a valid Preferred Time Window<br>4. Enter a valid Phone Number<br>5. Click Request Callback | Error displayed indicating the date must be at least the next business day | medium |
| TC-013 (boundary) | WF-003 | Preferred Date success case | User is on the Schedule Callback Form | 1. Select a Reason for Call from the dropdown<br>2. Enter a date that is the next business day in the Preferred Date field<br>3. Enter a valid Preferred Time Window<br>4. Enter a valid Phone Number<br>5. Click Request Callback | Callback request submitted and email confirmation sent | medium |
| TC-014 (input_edge) |  | Long Subject edge case | User is on the Secure Message Form | 1. Enter a Subject with a very long string (200+ characters) in the Subject field<br>2. Select a Category from the dropdown<br>3. Enter a Message Body<br>4. Click Send Message | Error displayed indicating subject length must be valid | low |
| TC-015 (input_edge) |  | Special characters in Phone Number edge case | User is on the Schedule Callback Form | 1. Select a Reason for Call from the dropdown<br>2. Enter a valid Preferred Date<br>3. Enter a valid Preferred Time Window<br>4. Enter a Phone Number with special characters (e.g., 123-456-7890)<br>5. Click Request Callback | Error displayed indicating phone number format must be valid | low |

---
