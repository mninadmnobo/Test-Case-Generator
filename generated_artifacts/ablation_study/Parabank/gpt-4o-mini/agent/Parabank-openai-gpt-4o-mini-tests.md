# Test Cases — Parabank

Generated: 2026-06-09T10:34:27.388700Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 193 | 23 | 99 | 71 | 98 | 76 | 19 |

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
| TC-004 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email_Username field<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it must be a valid email format | medium |
| TC-005 |  | Submit with password shorter than 8 characters |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Submit with password lacking required complexity |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <valid password without special character> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 | WF-002 | Attempt login with incorrect credentials |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <incorrect password> in the Password field<br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Email field with valid format |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'ValidPassword1!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-009 (boundary) |  | Password with exactly 8 characters |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Passw0!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-010 (boundary) |  | Password with 7 characters |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Pass1!' in the Password field<br>3. Click Sign In | Form submission is blocked; error message indicates password does not meet length requirement. | medium |
| TC-011 (input_edge) |  | Email field with invalid format |  | 1. Enter 'userexample.com' in the Email/Username field<br>2. Enter 'ValidPassword1!' in the Password field<br>3. Click Sign In | Form submission is blocked; error message indicates invalid email format. | low |
| TC-012 (input_edge) |  | Password with special characters only |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter '@#$%^&*' in the Password field<br>3. Click Sign In | Form submission is blocked; error message indicates password does not meet complexity requirements. | low |

---

## Register

Total: **26** (positive: 1, negative: 17, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Register with valid inputs | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Enter <valid SSN> in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <valid password> in the Password field<br>11. Enter <valid password> in the Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the First Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Street Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the ZIP Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-009 |  | Leave the Social Security Number field blank and submit |  | 1. Leave the Social Security Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Social Security Number field indicating it is required | high |
| TC-010 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Username field indicating it is required | high |
| TC-011 |  | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Password field indicating it is required | high |
| TC-012 |  | Leave the Confirm Password field blank and submit |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-013 |  | Enter an invalid format in the ZIP Code field and submit |  | 1. Enter <invalid ZIP Code format> in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the ZIP Code field indicating it must be 5 digits or 5+4 format | medium |
| TC-014 |  | Enter an invalid format in the Phone Number field and submit |  | 1. Enter <invalid Phone Number format> in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Phone Number field indicating it must follow format (123) 456-7890 | medium |
| TC-015 |  | Enter an invalid format in the Social Security Number field and submit |  | 1. Enter <invalid SSN format> in the Social Security Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Social Security Number field indicating it must follow format 123-45-6789 | medium |
| TC-016 |  | Enter an invalid email format in the Username field and submit |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Username field indicating it must be a valid email format | medium |
| TC-017 |  | Enter a short password in the Password field and submit |  | 1. Enter <password shorter than 8 characters> in the Password field<br>2. Fill all other required fields with valid data<br>3. Click Register | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-018 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Inline validation error appears on the Confirm Password field indicating the passwords must match | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) |  | ZIP Code with exactly 5 digits |  | 1. Enter '12345' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the ZIP Code '12345' | medium |
| TC-020 (boundary) |  | ZIP Code with 5+4 format |  | 1. Enter '12345-6789' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the ZIP Code '12345-6789' | medium |
| TC-021 (boundary) |  | Phone Number in valid format |  | 1. Enter '(123) 456-7890' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the Phone Number '(123) 456-7890' | medium |
| TC-022 (boundary) |  | Phone Number in invalid format |  | 1. Enter '1234567890' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Phone Number displays an error indicating the format is invalid | medium |
| TC-023 (boundary) |  | Password with exactly 8 characters |  | 1. Enter 'abcdefgh' in the Password field<br>2. Enter 'abcdefgh' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Form submits successfully; account is created with the Password 'abcdefgh' | medium |
| TC-024 (input_edge) |  | Long text in First Name field |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; First Name is saved as entered or truncated appropriately | low |
| TC-025 (input_edge) |  | Special characters in Last Name field |  | 1. Enter '@#$%^&*()' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Last Name displays an error indicating invalid characters | low |
| TC-026 (input_edge) |  | Leading/trailing whitespace in Username field |  | 1. Enter '   user@example.com   ' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Register | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounts Overview

Total: **6** (positive: 1, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Account Number for a customer account | User logged in as <Role> | 1. Click on the 'View Account Number' action for the account row | Account details displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view account number |  | 1. Click on the Account Number column | No action occurs; account number viewing feature is not implemented | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapidly click on View Account Number multiple times | User is logged in and on the Accounts Overview page | 1. Click on the View Account Number action for an account<br>2. Immediately click on the View Account Number action again | The first click displays the account details; the second click does not create a duplicate action. | medium |
| TC-004 (input_edge) |  | Enter a very long string in Account Type | User is on the Accounts Overview page | 1. Click on the Account Type cell for an account<br>2. Enter a string of 200+ characters | The input is either accepted or truncated with a visible indicator. | low |
| TC-005 (input_edge) |  | Enter special characters in Current Balance | User is on the Accounts Overview page | 1. Click on the Current Balance cell for an account<br>2. Enter special characters like @#$%^&*() | An error message is displayed indicating that the input is invalid. | low |
| TC-006 (input_edge) |  | Enter leading/trailing whitespace in Account Type | User is on the Accounts Overview page | 1. Click on the Account Type cell for an account<br>2. Enter '   Savings   ' | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Open New Account

Total: **12** (positive: 2, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Checking Account with valid deposit | User logged in as <Role>, Funding Source Account has sufficient balance | 1. Select 'Checking' as the Account Type<br>2. Enter 25 in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! and redirects to accounts overview | high |
| TC-002 | WF-002 | Open Savings Account with valid deposit | User logged in as <Role>, Funding Source Account has sufficient balance | 1. Select 'Savings' as the Account Type<br>2. Enter 100 in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! and redirects to accounts overview | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill in the Initial Deposit Amount with a valid amount<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave the Initial Deposit Amount field blank and submit |  | 1. Select an Account Type<br>2. Leave the Initial Deposit Amount field blank<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Enter a non-numeric value in the Initial Deposit Amount field |  | 1. Select an Account Type<br>2. Enter <non-numeric value> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-006 |  | Enter an Initial Deposit Amount less than the minimum for Checking and submit |  | 1. Select Checking as the Account Type<br>2. Enter <amount below minimum> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-007 |  | Enter an Initial Deposit Amount less than the minimum for Savings and submit |  | 1. Select Savings as the Account Type<br>2. Enter <amount below minimum> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-008 |  | Select a Funding Source Account with insufficient balance and submit |  | 1. Select an Account Type<br>2. Enter a valid Initial Deposit Amount<br>3. Select a Funding Source Account with insufficient balance<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it must have sufficient balance | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Initial deposit meets minimum for Checking | Account_Type is set to Checking, Funding_Source_Account has sufficient balance | 1. Enter exactly $25 in the Initial_Deposit_Amount field<br>2. Click Open Account | Account opened successfully! Redirects to accounts overview | medium |
| TC-010 (boundary) | WF-001 | Initial deposit below minimum for Checking | Account_Type is set to Checking, Funding_Source_Account has sufficient balance | 1. Enter $24.99 in the Initial_Deposit_Amount field<br>2. Click Open Account | Inline error shown: 'Deposit must be at least $25' | medium |
| TC-011 (boundary) | WF-002 | Initial deposit meets minimum for Savings | Account_Type is set to Savings, Funding_Source_Account has sufficient balance | 1. Enter exactly $100 in the Initial_Deposit_Amount field<br>2. Click Open Account | Account opened successfully! Redirects to accounts overview | medium |
| TC-012 (boundary) | WF-002 | Initial deposit below minimum for Savings | Account_Type is set to Savings, Funding_Source_Account has sufficient balance | 1. Enter $99.99 in the Initial_Deposit_Amount field<br>2. Click Open Account | Inline error shown: 'Deposit must be at least $100' | medium |

---

## Transfer Funds

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Transfer from My ParaBank Account | User logged in as <Role>, Sufficient funds available in the selected account | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Transfer completed successfully. | high |
| TC-002 | WF-002 | Transfer from External Account | User logged in as <Role>, Sufficient funds available in the selected account | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Enter <valid account number> in the Account Number field<br>5. Enter <valid account number> in the Confirm Account Number field<br>6. Click Submit | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Transfer Amount field blank |  | 1. Leave the Transfer Amount field blank<br>2. Select a Source Account<br>3. Choose a Transfer Type<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-004 |  | Enter an invalid Transfer Amount |  | 1. Enter <invalid amount> in the Transfer Amount field<br>2. Select a Source Account<br>3. Choose a Transfer Type<br>4. Click Submit | Inline validation error appears on the Transfer Amount field indicating it must be a valid amount | high |
| TC-005 |  | Enter Transfer Amount exceeding available funds |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Select a Source Account<br>3. Choose a Transfer Type<br>4. Click Submit | Error shown: 'Insufficient funds' | high |
| TC-006 |  | Enter mismatched account numbers for external transfer |  | 1. Select 'External Account' as Transfer Type<br>2. Enter <account number> in the Account Number field<br>3. Enter <different account number> in the Confirm Account Number field<br>4. Click Submit | Error shown: 'Account numbers do not match' | high |
| TC-007 |  | Leave Account Number field blank for external transfer |  | 1. Select 'External Account' as Transfer Type<br>2. Leave the Account Number field blank<br>3. Leave the Confirm Account Number field blank<br>4. Click Submit | Inline validation error appears on the Account Number field indicating it is required | high |
| TC-008 |  | Leave both Account Number fields blank for external transfer |  | 1. Select 'External Account' as Transfer Type<br>2. Leave the Account Number field blank<br>3. Leave the Confirm Account Number field blank<br>4. Click Submit | Inline validation error appears on the Account Number field indicating it is required; Inline validation error appears on the Confirm Account Number field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Transfer amount at minimum valid value | User has sufficient funds in the account | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter the minimum valid amount in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Transfer completed successfully. | medium |
| TC-010 (boundary) | WF-001 | Transfer amount just below minimum valid value | User has sufficient funds in the account | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter an amount just below the minimum valid amount in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Error displayed indicating insufficient funds. | medium |
| TC-011 (boundary) | WF-002 | Account number matches confirmation number | User selects External Account as Transfer Type | 1. Select 'External Account' as Transfer Type<br>2. Enter a valid account number in the Account_Number field<br>3. Enter the same account number in the Confirm_Account_Number field<br>4. Click Submit | Transfer completed successfully. | medium |
| TC-012 (boundary) | WF-002 | Account number does not match confirmation number | User selects External Account as Transfer Type | 1. Select 'External Account' as Transfer Type<br>2. Enter a valid account number in the Account_Number field<br>3. Enter a different account number in the Confirm_Account_Number field<br>4. Click Submit | Error displayed indicating account numbers do not match. | medium |
| TC-013 (input_edge) |  | Transfer amount with leading/trailing whitespace | User has sufficient funds in the account | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter '   100.00   ' in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Transfer completed successfully; amount displayed as '100.00' without extra spaces. | low |
| TC-014 (input_edge) |  | Transfer amount with special characters | User has sufficient funds in the account | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Enter '$100.00' in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Submit | Error displayed indicating invalid amount. | low |

---

## Payments

Total: **19** (positive: 1, negative: 12, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with valid account numbers and sufficient funds | User logged in as <role> | 1. Enter <valid payee name> in the Payee Name field<br>2. Enter <valid street address> in the Street Address field<br>3. Enter <valid city> in the City field<br>4. Enter <valid state> in the State field<br>5. Enter <valid ZIP code> in the ZIP Code field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Enter <valid payee account number> in the Payee Account Number field<br>8. Enter <same payee account number> in the Confirm Account Number field<br>9. Enter <valid payment amount> in the Payment Amount field<br>10. Select <valid source account> from the Source Account dropdown<br>11. Click Pay | Payment submitted successfully with reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Payee Name field blank and submit |  | 1. Leave the Payee_Name field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Name field indicating it is required | high |
| TC-003 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-004 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the City field indicating it is required | high |
| TC-005 |  | Leave the State field blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the State field indicating it is required | high |
| TC-006 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-008 |  | Leave the Payee Account Number field blank and submit |  | 1. Leave the Payee_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Account_Number field indicating it is required | high |
| TC-009 |  | Leave the Confirm Account Number field blank and submit |  | 1. Leave the Confirm_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating it is required | high |
| TC-010 |  | Leave the Payment Amount field blank and submit |  | 1. Leave the Payment_Amount field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payment_Amount field indicating it is required | high |
| TC-011 |  | Leave the Source Account field blank and submit |  | 1. Leave the Source_Account field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Source_Account field indicating it is required | high |
| TC-012 | WF-002 | Submit payment with account numbers not matching |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <different value> in the Confirm_Account_Number field<br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears indicating 'Account numbers do not match' | high |
| TC-013 | WF-003 | Submit payment with insufficient funds |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <valid Payee Account Number> in the Confirm_Account_Number field<br>3. Fill all other required fields<br>4. Enter <amount exceeding available balance> in the Payment_Amount field<br>5. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-002 | Confirm Account Number matches Payee Account Number exactly | Payee Account Number is set to a specific value | 1. Enter the same value in the Confirm Account Number field as in the Payee Account Number field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Payment submitted successfully with reference code | medium |
| TC-015 (boundary) | WF-002 | Confirm Account Number does not match Payee Account Number | Payee Account Number is set to a specific value | 1. Enter a different value in the Confirm Account Number field than in the Payee Account Number field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Account numbers do not match | medium |
| TC-016 (boundary) | WF-003 | Payment Amount equals available balance | Available funds are set to a specific amount | 1. Enter an amount in the Payment Amount field that equals the available funds<br>2. Fill all other required fields with valid data<br>3. Click Pay | Payment submitted successfully with reference code | medium |
| TC-017 (boundary) | WF-003 | Payment Amount exceeds available balance | Available funds are set to a specific amount | 1. Enter an amount in the Payment Amount field that exceeds the available funds<br>2. Fill all other required fields with valid data<br>3. Click Pay | Insufficient funds | medium |
| TC-018 (input_edge) |  | Enter a very long Payee Name |  | 1. Enter a string longer than 200 characters in the Payee Name field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline error shown indicating the field exceeds maximum length | low |
| TC-019 (input_edge) |  | Enter special characters in the Street Address |  | 1. Enter a string with special characters in the Street Address field<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline error shown indicating invalid characters | low |

---

## Request Loan

Total: **21** (positive: 3, negative: 10, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit loan application for Personal loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Personal' from the Loan Type options<br>2. Enter 15000 in the Loan Amount field<br>3. Enter 1500 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-002 | WF-002 | Submit loan application for Auto loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Auto' from the Loan Type options<br>2. Enter 30000 in the Loan Amount field<br>3. Enter 3000 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-003 | WF-003 | Submit loan application for Home loan | User logged in as <Role>, Credit engine simulates 80% approval rate | 1. Select 'Home' from the Loan Type options<br>2. Enter 200000 in the Loan Amount field<br>3. Enter 20000 in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Loan Amount field blank |  | 1. Leave the Loan Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Leave the Down Payment Amount field blank |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Leave the Down Payment Amount field blank<br>4. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it is required | high |
| TC-006 |  | Enter Down Payment Amount less than 10% of Loan Amount |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <amount less than 10% of Loan Amount> in the Down Payment Amount field<br>4. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it must be at least 10% of Loan Amount | high |
| TC-007 |  | Enter Down Payment Amount greater than Loan Amount |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <amount greater than Loan Amount> in the Down Payment Amount field<br>4. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it must be less than Loan Amount | high |
| TC-008 |  | Enter Loan Amount below minimum for Personal loan |  | 1. Select Personal as Loan Type<br>2. Enter <amount below $1,000> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Click Submit | Inline validation error appears on the Loan Amount field indicating it must be between $1,000 and $50,000 | high |
| TC-009 |  | Enter Loan Amount above maximum for Personal loan |  | 1. Select Personal as Loan Type<br>2. Enter <amount above $50,000> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Click Submit | Inline validation error appears on the Loan Amount field indicating it must be between $1,000 and $50,000 | high |
| TC-010 |  | Attempt to submit without sufficient collateral funds |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Select a Collateral Account with insufficient funds<br>5. Click Submit | Form does not submit; error shown indicating 'must have sufficient collateral funds' | high |
| TC-011 |  | Attempt to submit with collateral value less than 20% |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Select a Collateral Account with value less than 20% of the collateral value<br>5. Click Submit | Form does not submit; error shown indicating 'must be at least 20% of collateral value' | high |
| TC-012 | WF-001 | Attempt to submit loan application with insufficient credit history |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Select a Collateral Account with sufficient funds<br>5. Simulate insufficient credit history<br>6. Click Submit | Form does not submit; error shown indicating 'Insufficient credit history' | high |
| TC-013 | WF-001 | Attempt to submit loan application with inadequate collateral value |  | 1. Select Personal as Loan Type<br>2. Enter <valid amount> in the Loan Amount field<br>3. Enter <valid amount> in the Down Payment Amount field<br>4. Select a Collateral Account with inadequate collateral value<br>5. Click Submit | Form does not submit; error shown indicating 'Inadequate collateral value' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Test minimum Loan Amount for Personal loan | Loan_Type is set to Personal | 1. Enter $1,000 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submits successfully; loan approved and created successfully! | medium |
| TC-015 (boundary) | WF-001 | Test below minimum Loan Amount for Personal loan | Loan_Type is set to Personal | 1. Enter $999 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submission is blocked; error shown indicating Loan Amount must be at least $1,000 | medium |
| TC-016 (boundary) | WF-002 | Test maximum Loan Amount for Auto loan | Loan_Type is set to Auto | 1. Enter $75,000 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submits successfully; loan approved and created successfully! | medium |
| TC-017 (boundary) | WF-002 | Test above maximum Loan Amount for Auto loan | Loan_Type is set to Auto | 1. Enter $75,001 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submission is blocked; error shown indicating Loan Amount must be at most $75,000 | medium |
| TC-018 (boundary) | WF-003 | Test minimum Loan Amount for Home loan | Loan_Type is set to Home | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submits successfully; loan approved and created successfully! | medium |
| TC-019 (boundary) | WF-003 | Test below minimum Loan Amount for Home loan | Loan_Type is set to Home | 1. Enter $49,999 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Select a valid Collateral Account<br>4. Click Submit | Form submission is blocked; error shown indicating Loan Amount must be at least $50,000 | medium |
| TC-020 (input_edge) |  | Test long text in Loan_Type field |  | 1. Enter a very long string (200+ characters) in the Loan_Type field | Field displays an error indicating the input is too long | low |
| TC-021 (input_edge) |  | Test special characters in Loan_Type field |  | 1. Enter special characters (e.g., @#$%^&) in the Loan_Type field | Field displays an error indicating invalid characters | low |

---

## Update Contact Info

Total: **19** (positive: 1, negative: 14, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid contact information | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Enter <valid state> in the State field<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click Update Profile | Profile updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank |  | 1. Leave the State field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Enter an invalid format in the First Name field |  | 1. Enter <invalid format> in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-010 |  | Enter an invalid format in the Last Name field |  | 1. Enter <invalid format> in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-011 |  | Enter an invalid format in the Street Address field |  | 1. Enter <invalid format> in the Street Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-012 |  | Enter an invalid format in the City field |  | 1. Enter <invalid format> in the City field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-013 |  | Enter an invalid format in the State field |  | 1. Enter <invalid format> in the State field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-014 |  | Enter an invalid format in the ZIP Code field |  | 1. Enter <invalid format> in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |
| TC-015 |  | Enter an invalid format in the Phone Number field |  | 1. Enter <invalid format> in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | highlights invalid fields and displays an inline error banner | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submits successfully; First Name field displays the entered value correctly. | low |
| TC-017 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter '@#$%^&*()' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error banner displays indicating invalid format for Last Name. | medium |
| TC-018 (input_edge) |  | Enter leading and trailing whitespace in the Street Address field |  | 1. Enter '   123 Main St   ' in the Street Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |
| TC-019 (input_edge) |  | Enter a valid ZIP Code format but with incorrect length |  | 1. Enter '12345-678' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error banner displays indicating invalid format for ZIP Code. | medium |

---

## Manage Cards

Total: **13** (positive: 2, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Card Request Form with valid data | User logged in as <Role> | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click 'Request Card' | Card request submitted successfully with tracking ID | high |
| TC-002 | WF-002 | Update Card Controls with valid data | User logged in as <Role> | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid numeric limit> in the New Spending Limit field<br>3. Select 'Active' from the Card Status dropdown<br>4. Click 'Update Controls' | Card controls updated successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank |  | 1. Leave the Account to Link field blank<br>2. Fill in the Card Type and Shipping Address fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Leave the Shipping Address field incomplete |  | 1. Fill in the Account to Link field<br>2. Leave the Shipping Address field incomplete<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-005 |  | Leave the Select Existing Card field blank |  | 1. Leave the Select Existing Card field blank<br>2. Fill in the New Spending Limit and Card Status fields<br>3. Click Update Controls | Inline validation error appears on the Select Existing Card field indicating it is required | high |
| TC-006 |  | Submit with New Spending Limit as non-numeric |  | 1. Select an Existing Card<br>2. Enter <non-numeric value> in the New Spending Limit field<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating 'must be a valid numeric limit' | high |
| TC-007 |  | Submit with New Spending Limit exceeding policy limit |  | 1. Select an Existing Card<br>2. Enter <amount exceeding policy limit> in the New Spending Limit field<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating 'valid numeric limits' | high |
| TC-008 |  | Attempt to update card controls with invalid card status transition |  | 1. Select an Existing Card with Active status<br>2. Select Frozen as the new Card Status<br>3. Enter a valid New Spending Limit<br>4. Click Update Controls | Inline validation error appears indicating 'allowable card-status transitions' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit Card Request with incomplete address | User is on the Manage Cards page, Card Type is selected, Account to Link is filled | 1. Leave Shipping Address field empty<br>2. Click Request Card | Form submission is blocked; inline error shown indicating 'address must be complete' | medium |
| TC-010 (boundary) | WF-002 | Submit Card Controls with invalid numeric limit | User is on the Manage Cards page, Select Existing Card is chosen, Card Status is selected | 1. Enter a negative value in the New Spending Limit field<br>2. Click Update Controls | Form submission is blocked; inline error shown indicating 'must be a valid numeric limit' | medium |
| TC-011 (boundary) | WF-002 | Add maximum entries to Travel Notice | User is on the Manage Cards page, Select Existing Card is chosen, New Spending Limit is filled, Card Status is selected | 1. Add 5 entries to the Travel Notice<br>2. Attempt to add one more entry | Adding the sixth entry is blocked; inline error shown indicating maximum entries reached | medium |
| TC-012 (boundary) | WF-002 | Submit Card Controls with valid date range | User is on the Manage Cards page, Select Existing Card is chosen, New Spending Limit is filled, Card Status is selected | 1. Add a date in the Travel Notice<br>2. Add an earlier date in the Travel Notice<br>3. Click Update Controls | Form submission is blocked; inline error shown indicating 'valid date ranges' as the start date is after the end date | medium |
| TC-013 (input_edge) |  | Submit Shipping Address with special characters | User is on the Manage Cards page, Card Type is selected, Account to Link is filled | 1. Enter a Shipping Address with special characters (e.g., #, @, &)<br>2. Click Request Card | Form submission succeeds; address is accepted and tracking ID is shown | low |

---

## Investments

Total: **16** (positive: 3, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Execute Trade for Buy Action | User logged in as <Role>, Fund Symbol is valid, Funding or Destination Account has adequate balance | 1. Select 'Buy' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | executes same-day trade, updates holdings, displays Trade executed successfully with order ID | high |
| TC-002 | WF-002 | Execute Trade for Sell Action | User logged in as <Role>, Fund Symbol is valid, Funding or Destination Account has adequate balance | 1. Select 'Sell' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | executes same-day trade, updates holdings, displays Trade executed successfully with order ID | high |
| TC-003 | WF-003 | Create Recurring Investment Plan | User logged in as <Role>, Fund Symbol is valid, Funding Account has adequate balance | 1. Enter <valid fund symbol> in the Fund Symbol field<br>2. Enter <valid contribution amount meeting minimum> in the Contribution Amount field<br>3. Select <valid frequency> from the Frequency dropdown<br>4. Enter <future date> in the Start Date field<br>5. Select <valid funding account> from the Funding Account dropdown<br>6. Click Create Plan | stores the schedule, shows Plan created successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Quantity field blank |  | 1. Leave the Quantity field blank<br>2. Select a valid Action<br>3. Select a valid Fund Symbol<br>4. Select a valid Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-005 |  | Enter a Quantity of zero |  | 1. Enter 0 in the Quantity field<br>2. Select a valid Action<br>3. Select a valid Fund Symbol<br>4. Select a valid Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Quantity field indicating it must be greater than zero | high |
| TC-006 |  | Select a Funding or Destination Account with inadequate balance |  | 1. Enter a valid Quantity<br>2. Select a valid Action<br>3. Select a valid Fund Symbol<br>4. Select a Funding or Destination Account with inadequate balance<br>5. Click Execute Trade | Inline validation error appears on the Funding or Destination Account field indicating it must have adequate balance | high |
| TC-007 |  | Leave the Contribution Amount field blank |  | 1. Leave the Contribution Amount field blank<br>2. Select a valid Fund Symbol<br>3. Select a Frequency<br>4. Select a future Start Date<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it is required | high |
| TC-008 |  | Enter a Contribution Amount below the minimum |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Select a valid Fund Symbol<br>3. Select a Frequency<br>4. Select a future Start Date<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it must meet minimum | high |
| TC-009 |  | Select a Funding Account with inadequate balance |  | 1. Enter a valid Contribution Amount<br>2. Select a valid Fund Symbol<br>3. Select a Frequency<br>4. Select a future Start Date<br>5. Select a Funding Account with inadequate balance<br>6. Click Create Plan | Inline validation error appears on the Funding Account field indicating it must have adequate balance | high |
| TC-010 |  | Enter a Start Date in the past |  | 1. Enter a past date in the Start Date field<br>2. Select a valid Fund Symbol<br>3. Enter a valid Contribution Amount<br>4. Select a Frequency<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Start Date field indicating it must be in the future | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Quantity at minimum threshold | User has sufficient balance, Fund symbol exists | 1. Select 'Buy' from the Action dropdown<br>2. Enter '1' in the Quantity field<br>3. Select a valid Fund Symbol<br>4. Select a Funding Account with adequate balance<br>5. Click Execute Trade | Trade executed successfully with order ID displayed | medium |
| TC-012 (boundary) | WF-001 | Quantity just below minimum threshold | User has sufficient balance, Fund symbol exists | 1. Select 'Buy' from the Action dropdown<br>2. Enter '0' in the Quantity field<br>3. Select a valid Fund Symbol<br>4. Select a Funding Account with adequate balance<br>5. Click Execute Trade | Inline error appears indicating 'Quantity must be greater than zero' | medium |
| TC-013 (boundary) | WF-003 | Contribution Amount at minimum threshold | User has adequate balance, Fund symbol exists | 1. Select a valid Fund Symbol<br>2. Enter the minimum Contribution Amount in the Contribution Amount field<br>3. Select Frequency as 'Weekly'<br>4. Set Start Date to a future date<br>5. Select a Funding Account with adequate balance<br>6. Click Create Plan | Plan created successfully message is displayed | medium |
| TC-014 (boundary) | WF-003 | Contribution Amount just below minimum threshold | User has adequate balance, Fund symbol exists | 1. Select a valid Fund Symbol<br>2. Enter an amount below the minimum in the Contribution Amount field<br>3. Select Frequency as 'Weekly'<br>4. Set Start Date to a future date<br>5. Select a Funding Account with adequate balance<br>6. Click Create Plan | Inline error appears indicating 'Contribution Amount must meet minimum' | medium |
| TC-015 (boundary) | WF-003 | Start Date exactly today | User has adequate balance, Fund symbol exists | 1. Select a valid Fund Symbol<br>2. Enter a valid Contribution Amount in the Contribution Amount field<br>3. Select Frequency as 'Weekly'<br>4. Set Start Date to today's date<br>5. Select a Funding Account with adequate balance<br>6. Click Create Plan | Inline error appears indicating 'Start date must be in the future' | medium |
| TC-016 (boundary) | WF-003 | Start Date just in the past | User has adequate balance, Fund symbol exists | 1. Select a valid Fund Symbol<br>2. Enter a valid Contribution Amount in the Contribution Amount field<br>3. Select Frequency as 'Weekly'<br>4. Set Start Date to yesterday's date<br>5. Select a Funding Account with adequate balance<br>6. Click Create Plan | Inline error appears indicating 'Start date must be in the future' | medium |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate account statement successfully | User logged in as <Role>, Valid date range is established, Account is selected from the dropdown | 1. Enter <valid date range> in the Statement Period field<br>2. Select <valid account> from the Account dropdown<br>3. Click Generate Statement | Statement generated successfully | high |
| TC-002 | WF-002 | Save e-Statement preference successfully | User logged in as <Role> | 1. Enter <valid email address> in the Email Address field<br>2. Check the Opt into Paperless checkbox<br>3. Click Save Preference | e-Statement preference updated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Statement Period field blank and submit |  | 1. Leave the Statement Period field blank<br>2. Select an Account<br>3. Click Generate Statement | Inline validation error appears on the Statement Period field indicating it is required | high |
| TC-004 | WF-001 | Submit with an invalid date range in the Statement Period field |  | 1. Enter <invalid date range> in the Statement Period field<br>2. Select an Account<br>3. Click Generate Statement | Inline validation error appears on the Statement Period field indicating 'valid date range required' | high |
| TC-005 | WF-002 | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Check the Opt into Paperless checkbox<br>3. Click Save Preference | Inline validation error appears on the Email Address field indicating it is required | high |
| TC-006 | WF-002 | Submit with an invalid email format in the Email Address field |  | 1. Enter <invalid email format> in the Email Address field<br>2. Check the Opt into Paperless checkbox<br>3. Click Save Preference | Inline validation error appears on the Email Address field indicating 'valid email address required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Submit Statement Period with valid date range | User selects a valid date range for the Statement Period, User selects an Account from the dropdown | 1. Fill the Statement Period field with a valid date range<br>2. Select an Account<br>3. Click Generate Statement | Statement generated successfully | medium |
| TC-008 (boundary) | WF-001 | Submit Statement Period with invalid date range | User selects an Account from the dropdown | 1. Fill the Statement Period field with an invalid date range<br>2. Click Generate Statement | Unable to generate statement — please try again later | medium |
| TC-009 (boundary) | WF-002 | Submit Email Address with valid format |  | 1. Fill the Email Address field with a valid email format<br>2. Click Save Preference | e-Statement preference updated | medium |
| TC-010 (boundary) | WF-002 | Submit Email Address with invalid format |  | 1. Fill the Email Address field with an invalid email format<br>2. Click Save Preference | Email field is highlighted with guidance | medium |

---

## Security Settings

Total: **12** (positive: 1, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Change password successfully | User logged in as <Role>, User knows their current password | 1. Enter <valid current password> in the Current Password field<br>2. Enter <valid new password> in the New Password field<br>3. Enter <valid new password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave Current Password blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill in a valid New Password<br>3. Fill in a matching Confirm New Password<br>4. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 | WF-001 | Leave New Password blank and submit |  | 1. Enter a valid Current Password<br>2. Leave the New Password field blank<br>3. Fill in a matching Confirm New Password<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 | WF-001 | Leave Confirm New Password blank and submit |  | 1. Enter a valid Current Password<br>2. Fill in a valid New Password<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 | WF-001 | Enter invalid Current Password and submit |  | 1. Enter an invalid Current Password<br>2. Fill in a valid New Password<br>3. Fill in a matching Confirm New Password<br>4. Click Change Password | Inline validation error appears on the Current Password field indicating 'Must verify current password' | high |
| TC-006 | WF-001 | Enter New Password that does not meet strong-password policy |  | 1. Enter a valid Current Password<br>2. Enter a weak New Password<br>3. Fill in a matching Confirm New Password<br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'Must meet strong-password policy' | high |
| TC-007 | WF-001 | Enter mismatched New Password and Confirm New Password |  | 1. Enter a valid Current Password<br>2. Enter a valid New Password<br>3. Enter a different Confirm New Password<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'Must match New Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter a strong password that meets the policy | User is logged in, Current password is known | 1. Enter the current password in the Current Password field<br>2. Enter a strong password in the New Password field<br>3. Enter the same strong password in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) | WF-001 | Enter a weak password that does not meet the strong-password policy | User is logged in, Current password is known | 1. Enter the current password in the Current Password field<br>2. Enter a weak password in the New Password field<br>3. Enter the same weak password in the Confirm New Password field<br>4. Click Change Password | New Password field displays an error indicating the password does not meet the strong-password policy. | medium |
| TC-010 (boundary) | WF-001 | Enter a new password that does not match the confirmation | User is logged in, Current password is known | 1. Enter the current password in the Current Password field<br>2. Enter a strong password in the New Password field<br>3. Enter a different password in the Confirm New Password field<br>4. Click Change Password | Confirm New Password field displays an error indicating the passwords do not match. | medium |
| TC-011 (input_edge) | WF-001 | Enter a very long password | User is logged in, Current password is known | 1. Enter the current password in the Current Password field<br>2. Enter a password with 100+ characters in the New Password field<br>3. Enter the same long password in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | low |
| TC-012 (input_edge) | WF-001 | Enter special characters in the password fields | User is logged in, Current password is known | 1. Enter the current password in the Current Password field<br>2. Enter a password with special characters in the New Password field<br>3. Enter the same password with special characters in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | low |

---

## Support Center

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send message without attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Account' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click Send Message | Message sent successfully with ticket ID | high |
| TC-002 | WF-002 | Send message with attachment | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click 'Upload' and select a <valid attachment type><br>5. Click Send Message | Message sent successfully with ticket ID | high |
| TC-003 | WF-003 | Request callback | User logged in as <Role> | 1. Select 'Technical' from the Reason for Call dropdown<br>2. Enter <valid date> in the Preferred Date field<br>3. Enter <valid time window> in the Preferred Time Window field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Click Request Callback | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Message Body blank and submit |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject and Category fields<br>3. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-005 |  | Submit the Secure Message Form with an invalid Subject length |  | 1. Enter <invalid subject length> in the Subject field<br>2. Fill in the Category and Message Body fields<br>3. Click Send Message | Inline validation error appears on the Subject field indicating 'subject length must be valid' | medium |
| TC-006 |  | Submit the Schedule Callback Form with an invalid Phone Number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Fill in the Reason for Call, Preferred Date, and Preferred Time Window fields<br>3. Click Request Callback | Inline validation error appears on the Phone Number field indicating 'valid phone number format' | medium |
| TC-007 |  | Submit the Schedule Callback Form with a Preferred Date before the next business day |  | 1. Enter <date before next business day> in the Preferred Date field<br>2. Fill in the Reason for Call and Phone Number fields<br>3. Click Request Callback | Inline validation error appears on the Preferred Date field indicating 'date must be at least the next business day' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Send message with subject at minimum length | User is on the Secure Message Form | 1. Enter minimum valid length subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Click Send Message | Message sent successfully with ticket ID | medium |
| TC-009 (boundary) | WF-001 | Send message with subject below minimum length | User is on the Secure Message Form | 1. Enter subject below minimum valid length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Click Send Message | Inline error indicates subject length is invalid | medium |
| TC-010 (boundary) | WF-003 | Request callback with preferred date as tomorrow | User is on the Schedule Callback Form | 1. Select a reason for call from the dropdown<br>2. Enter tomorrow's date in the Preferred Date field<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Callback request submitted and email confirmation sent | medium |
| TC-011 (boundary) | WF-003 | Request callback with preferred date as today | User is on the Schedule Callback Form | 1. Select a reason for call from the dropdown<br>2. Enter today's date in the Preferred Date field<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Inline error indicates date must be at least the next business day | medium |
| TC-012 (data_edge) | WF-002 | Upload file at exact size limit | User is on the Secure Message Form | 1. Enter a valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Upload a file exactly at the size limit in the Attachment field<br>5. Click Send Message | Message sent successfully with ticket ID | medium |
| TC-013 (data_edge) | WF-002 | Upload file over size limit | User is on the Secure Message Form | 1. Enter a valid subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a valid message body in the Message Body field<br>4. Upload a file one byte over the size limit in the Attachment field<br>5. Click Send Message | Inline error indicates invalid attachment type | medium |

---
