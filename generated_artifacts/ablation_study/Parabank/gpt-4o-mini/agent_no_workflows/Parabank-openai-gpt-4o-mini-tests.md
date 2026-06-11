# Test Cases — Parabank

Generated: 2026-06-10T20:11:17.886680Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 192 | 25 | 103 | 64 | 104 | 68 | 20 |

## Login

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs in with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click Sign In | Signed in successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email field blank and submit |  | 1. Leave the Email_Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Leave the Password field blank<br>3. Click Sign In | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email_Username field<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it must be a valid email format | medium |
| TC-005 |  | Submit with a password that does not meet complexity requirements |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Submit with a password that lacks required character types |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password without uppercase letters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 |  | Submit with incorrect email and password |  | 1. Fill the Email_Username field with <non-registered email><br>2. Fill the Password field with <incorrect password><br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Email field with invalid format |  | 1. Enter 'invalid-email-format' in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Form submission is blocked; inline error shows 'must be a valid email format' | medium |
| TC-009 (boundary) |  | Password with exactly 8 characters but missing required types |  | 1. Enter a valid email in the Email/Username field<br>2. Enter 'abcdefg1' in the Password field<br>3. Click Sign In | Form submission is blocked; inline error shows 'must include uppercase, lowercase, number, and special character' | medium |
| TC-010 (boundary) |  | Password with exactly 8 characters including all required types |  | 1. Enter a valid email in the Email/Username field<br>2. Enter 'Abcdef1!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page with a message 'Signed in successfully.' | medium |
| TC-011 (input_edge) |  | Password with leading and trailing whitespace |  | 1. Enter a valid email in the Email/Username field<br>2. Enter '   Abcdef1!   ' in the Password field<br>3. Click Sign In | Leading/trailing whitespace is trimmed; user is redirected to the Accounts Overview page with a message 'Signed in successfully.' | low |

---

## Register

Total: **24** (positive: 1, negative: 17, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful registration with valid inputs | User is on the registration page | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter '12345' in the ZIP Code field<br>7. Enter '(123) 456-7890' in the Phone Number field<br>8. Enter '123-45-6789' in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <valid password> in the Password field<br>11. Enter the same <valid password> in the Confirm Password field<br>12. Click Register | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field unselected |  | 1. Leave the State field unselected<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Enter an invalid ZIP Code format |  | 1. Enter <invalid ZIP Code format> in the ZIP Code field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it must be 5 digits or 5+4 format | medium |
| TC-009 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-010 |  | Enter an invalid Phone Number format |  | 1. Enter <invalid Phone Number format> in the Phone Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it must follow the format (123) 456-7890 | medium |
| TC-011 |  | Leave the Social Security Number field blank |  | 1. Leave the Social Security Number field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it is required | high |
| TC-012 |  | Enter an invalid Social Security Number format |  | 1. Enter <invalid Social Security Number format> in the Social Security Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it must follow the format 123-45-6789 | medium |
| TC-013 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it is required | high |
| TC-014 |  | Enter an invalid Username format |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it must be a valid email format | medium |
| TC-015 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it is required | high |
| TC-016 |  | Enter a Password shorter than 8 characters |  | 1. Enter <password shorter than minimum length> in the Password field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-017 |  | Leave the Confirm Password field blank |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-018 |  | Enter a Confirm Password that does not match Password |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Register | Inline validation error appears on the Confirm_Password field indicating it must match the Password field | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) |  | ZIP Code with exactly 5 digits |  | 1. Enter '12345' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the ZIP Code '12345' | medium |
| TC-020 (boundary) |  | ZIP Code with 5+4 format |  | 1. Enter '12345-6789' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created with the ZIP Code '12345-6789' | medium |
| TC-021 (boundary) |  | ZIP Code with 4 digits (invalid) |  | 1. Enter '1234' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | ZIP Code displays an error indicating the value is below the minimum allowed | medium |
| TC-022 (boundary) |  | Phone Number with invalid format |  | 1. Enter '1234567890' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Phone Number displays an error indicating the format must be (123) 456-7890 | medium |
| TC-023 (boundary) |  | Password with exactly 8 characters |  | 1. Enter 'abcdefgh' in the Password field<br>2. Enter 'abcdefgh' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Form submits successfully; account is created with the Password 'abcdefgh' | medium |
| TC-024 (boundary) |  | Password with 7 characters (invalid) |  | 1. Enter 'abcdefg' in the Password field<br>2. Enter 'abcdefg' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Password displays an error indicating it must be at least 8 characters | medium |

---

## Accounts Overview

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View Account details from Accounts Table | User logged in as <User>, Account_Number is clickable | 1. Click on the Account_Number in the Accounts Table | User navigates to account details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to click on Account Number | Account_Number is clickable | 1. Navigate to the Accounts Overview page<br>2. Attempt to click on the Account Number | No action occurs; the Account details do not load as the click action is not implemented. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (input_edge) |  | Enter long string in Account Type column |  | 1. Navigate to Accounts Overview<br>2. Attempt to enter a string longer than 200 characters in the Account Type column | Input is either accepted or truncated with a visible indicator | low |
| TC-004 (input_edge) |  | Enter special characters in Current Balance column |  | 1. Navigate to Accounts Overview<br>2. Attempt to enter special characters in the Current Balance column | Input is either accepted or a specific error is shown | low |
| TC-005 (input_edge) |  | Enter value with leading/trailing whitespace in Open Date column |  | 1. Navigate to Accounts Overview<br>2. Attempt to enter a date with leading and trailing spaces in the Open Date column | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Open New Account

Total: **13** (positive: 2, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open a Checking account with valid initial deposit | User logged in as <Customer>, Funding Source Account has sufficient balance | 1. Select 'Checking' as the Account Type<br>2. Enter '25' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |
| TC-002 |  | Open a Savings account with valid initial deposit | User logged in as <Customer>, Funding Source Account has sufficient balance | 1. Select 'Savings' as the Account Type<br>2. Enter '100' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the dropdown<br>4. Click 'Open Account' | Account opened successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill in the Initial Deposit Amount and Funding Source Account fields with valid data<br>3. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave the Initial Deposit Amount field blank and submit |  | 1. Leave the Initial Deposit Amount field blank<br>2. Select an Account Type and fill in the Funding Source Account field with valid data<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Leave the Funding Source Account field blank and submit |  | 1. Leave the Funding Source Account field blank<br>2. Select an Account Type and fill in the Initial Deposit Amount field with valid data<br>3. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it is required | high |
| TC-006 |  | Enter a non-numeric value in the Initial Deposit Amount field |  | 1. Enter <non-numeric value> in the Initial Deposit Amount field<br>2. Select an Account Type and fill in the Funding Source Account field with valid data<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-007 |  | Enter an Initial Deposit Amount below minimum for Checking |  | 1. Enter <amount below $25> in the Initial Deposit Amount field<br>2. Select Checking as the Account Type and fill in the Funding Source Account field with valid data<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-008 |  | Enter an Initial Deposit Amount below minimum for Savings |  | 1. Enter <amount below $100> in the Initial Deposit Amount field<br>2. Select Savings as the Account Type and fill in the Funding Source Account field with valid data<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-009 |  | Select a Funding Source Account with insufficient balance |  | 1. Select an Account Type<br>2. Enter a valid Initial Deposit Amount<br>3. Select a Funding Source Account that has insufficient balance<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it must have sufficient balance | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Minimum deposit for Checking account |  | 1. Select 'Checking' as Account Type<br>2. Enter exactly $25 in the Initial Deposit Amount field<br>3. Select a Funding Source Account with sufficient balance<br>4. Click 'Open Account' | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-011 (boundary) |  | Minimum deposit for Savings account |  | 1. Select 'Savings' as Account Type<br>2. Enter exactly $100 in the Initial Deposit Amount field<br>3. Select a Funding Source Account with sufficient balance<br>4. Click 'Open Account' | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-012 (boundary) |  | Below minimum deposit for Checking account |  | 1. Select 'Checking' as Account Type<br>2. Enter $24 in the Initial Deposit Amount field<br>3. Select a Funding Source Account with sufficient balance<br>4. Click 'Open Account' | Error displayed indicating 'Initial Deposit Amount must be at least $25 for Checking'. | medium |
| TC-013 (boundary) |  | Below minimum deposit for Savings account |  | 1. Select 'Savings' as Account Type<br>2. Enter $99 in the Initial Deposit Amount field<br>3. Select a Funding Source Account with sufficient balance<br>4. Click 'Open Account' | Error displayed indicating 'Initial Deposit Amount must be at least $100 for Savings'. | medium |

---

## Transfer Funds

Total: **16** (positive: 5, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Transfer funds to My ParaBank Account | User logged in as <Account Holder>, sufficient funds | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Transfer | Transfer completed successfully. | high |
| TC-002 |  | Transfer funds to an External Account | User logged in as <Account Holder>, sufficient funds | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <same valid external account number> in the Confirm Account Number field<br>6. Click Transfer | Transfer completed successfully. | high |
| TC-003 |  | Transfer funds to an Internal Account | User logged in as <Account Holder>, sufficient funds | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Select an account from the Internal Accounts dropdown<br>5. Click Transfer | Transfer completed successfully. | high |
| TC-004 |  | Attempt transfer with mismatched external account numbers | User logged in as <Account Holder>, sufficient funds | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <different external account number> in the Confirm Account Number field<br>6. Click Transfer | Account numbers do not match. | high |
| TC-005 |  | Attempt transfer with insufficient funds | User logged in as <Account Holder>, insufficient funds | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid transfer amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Transfer | Insufficient funds. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave Transfer Amount blank and submit |  | 1. Leave the Transfer Amount field blank<br>2. Select a Source Account<br>3. Click Transfer | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-007 |  | Submit with all required fields empty for external transfer |  | 1. Select External Account as Transfer Type<br>2. Leave the External Account Number field blank<br>3. Leave the Confirm Account Number field blank<br>4. Click Transfer | Inline validation error appears on the External Account Number field indicating it is required; Inline validation error appears on the Confirm Account Number field indicating it is required | high |
| TC-008 |  | Enter mismatched account numbers for external transfer |  | 1. Select External Account as Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <different account number> in the Confirm Account Number field<br>4. Click Transfer | Error shown: 'Account numbers do not match' | high |
| TC-009 |  | Attempt transfer with insufficient funds | sufficient funds is not met | 1. Select External Account as Transfer Type<br>2. Enter <amount exceeding available balance> in the Transfer Amount field<br>3. Select a Source Account<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter the same <valid external account number> in the Confirm Account Number field<br>6. Click Transfer | Error shown: 'Insufficient funds' | high |
| TC-010 |  | Attempt transfer without selecting a Source Account |  | 1. Select External Account as Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter the same <valid external account number> in the Confirm Account Number field<br>4. Leave the Source Account field blank<br>5. Click Transfer | Inline validation error appears on the Source Account field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Enter a valid Transfer Amount of 0 |  | 1. Select 'External Account' for Transfer_Type<br>2. Enter '0' in the Transfer_Amount field<br>3. Fill all other required fields<br>4. Click Transfer | Form submission is blocked; error message indicates that the Transfer Amount must be present and valid. | medium |
| TC-012 (boundary) |  | Enter a valid Transfer Amount of 1 |  | 1. Select 'External Account' for Transfer_Type<br>2. Enter '1' in the Transfer_Amount field<br>3. Fill all other required fields<br>4. Click Transfer | Form submits successfully; transfer is processed. | medium |
| TC-013 (input_edge) |  | Enter a very long External Account Number |  | 1. Select 'External Account' for Transfer_Type<br>2. Enter a long number (more than the maximum allowed digits) in the External_Account_Number field<br>3. Fill all other required fields<br>4. Click Transfer | Form submission is blocked; error message indicates that the value is invalid. | low |
| TC-014 (input_edge) |  | Enter a valid External Account Number with leading/trailing spaces |  | 1. Select 'External Account' for Transfer_Type<br>2. Enter ' 123456 ' in the External_Account_Number field<br>3. Fill all other required fields<br>4. Click Transfer | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces. | low |
| TC-015 (input_edge) |  | Enter special characters in the External Account Number |  | 1. Select 'External Account' for Transfer_Type<br>2. Enter '@#$%^&*()' in the External_Account_Number field<br>3. Fill all other required fields<br>4. Click Transfer | Form submission is blocked; error message indicates that the value is invalid. | low |
| TC-016 (state_edge) |  | Rapidly switch between transfer types |  | 1. Select 'My ParaBank Account' for Transfer_Type<br>2. Immediately switch to 'External Account'<br>3. Fill in the External_Account_Number field<br>4. Click Transfer | Form submits successfully; transfer is processed without errors. | medium |

---

## Payments

Total: **17** (positive: 1, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit payment with valid details | User logged in as <User>, User has sufficient funds in the selected source account | 1. Enter <valid payee name> in the Payee Name field<br>2. Enter <valid street address> in the Street Address field<br>3. Enter <valid city> in the City field<br>4. Enter <valid state> in the State field<br>5. Enter <valid ZIP code> in the ZIP Code field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Enter <valid payee account number> in the Payee Account Number field<br>8. Enter the same <valid payee account number> in the Confirm Account Number field<br>9. Enter <valid payment amount> in the Payment Amount field<br>10. Select <valid source account> from the Source Account dropdown<br>11. Click Pay | Payment submitted successfully with reference code | high |

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
| TC-012 |  | Submit with Payee Account Number and Confirm Account Number not matching |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <different value> in the Confirm_Account_Number field<br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears indicating 'Account numbers do not match' | high |
| TC-013 |  | Submit with insufficient funds |  | 1. Enter <valid Payee Account Number> in the Payee_Account_Number field<br>2. Enter <valid Confirm Account Number> in the Confirm_Account_Number field<br>3. Enter <amount exceeding available balance> in the Payment_Amount field<br>4. Fill all other required fields<br>5. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Payment Amount at minimum value |  | 1. Enter <minimum value> in the <Payment Amount> field<br>2. Fill all other required fields<br>3. Click Pay | Payment submitted successfully with reference code | medium |
| TC-015 (boundary) |  | Payment Amount just below minimum value |  | 1. Enter <one unit below minimum value> in the <Payment Amount> field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating insufficient funds | medium |
| TC-016 (input_edge) |  | Long text in Payee Name |  | 1. Enter a long string (200+ characters) in the <Payee Name> field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating the value exceeds maximum length | low |
| TC-017 (input_edge) |  | Special characters in Street Address |  | 1. Enter special characters in the <Street Address> field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating invalid characters | low |

---

## Request Loan

Total: **18** (positive: 4, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a Personal Loan Application | User logged in as <User>, Loan Type is selected as Personal | 1. Enter 15000 in the Loan Amount field<br>2. Enter 1500 in the Down Payment Amount field<br>3. Select <valid collateral account> from the Collateral Account dropdown<br>4. Click Submit | Loan approved and created successfully! | high |
| TC-002 |  | Submit an Auto Loan Application | User logged in as <User>, Loan Type is selected as Auto | 1. Enter 20000 in the Loan Amount field<br>2. Enter 2000 in the Down Payment Amount field<br>3. Select <valid collateral account> from the Collateral Account dropdown<br>4. Click Submit | Loan approved and created successfully! | high |
| TC-003 |  | Submit a Home Loan Application | User logged in as <User>, Loan Type is selected as Home | 1. Enter 300000 in the Loan Amount field<br>2. Enter 30000 in the Down Payment Amount field<br>3. Select <valid collateral account> from the Collateral Account dropdown<br>4. Click Submit | Loan approved and created successfully! | high |
| TC-004 |  | Simulate Loan Approval Rate | User logged in as <User> | 1. Click on the Loan Simulation button | simulates 80% approval rate | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Loan_Type field blank and submit |  | 1. Leave the Loan_Type field blank<br>2. Fill Loan_Amount, Down_Payment_Amount, and Collateral_Account with valid values<br>3. Click Submit | Inline validation error appears on the Loan_Type field indicating it is required | high |
| TC-006 |  | Leave Loan_Amount field blank and submit |  | 1. Leave the Loan_Amount field blank<br>2. Fill Loan_Type, Down_Payment_Amount, and Collateral_Account with valid values<br>3. Click Submit | Inline validation error appears on the Loan_Amount field indicating it is required | high |
| TC-007 |  | Leave Down_Payment_Amount field blank and submit |  | 1. Leave the Down_Payment_Amount field blank<br>2. Fill Loan_Type, Loan_Amount, and Collateral_Account with valid values<br>3. Click Submit | Inline validation error appears on the Down_Payment_Amount field indicating it is required | high |
| TC-008 |  | Leave Collateral_Account field blank and submit |  | 1. Leave the Collateral_Account field blank<br>2. Fill Loan_Type, Loan_Amount, and Down_Payment_Amount with valid values<br>3. Click Submit | Inline validation error appears on the Collateral_Account field indicating it is required | high |
| TC-009 |  | Submit with Down_Payment_Amount less than 10% of Loan Amount |  | 1. Select a Loan_Type<br>2. Enter <amount above $1,000> in the Loan_Amount field<br>3. Enter <amount less than 10% of Loan_Amount> in the Down_Payment_Amount field<br>4. Select a valid Collateral_Account<br>5. Click Submit | Form does not submit; Down_Payment_Amount is not at least 10% of Loan Amount | high |
| TC-010 |  | Submit with Down_Payment_Amount greater than Loan Amount |  | 1. Select a Loan_Type<br>2. Enter <amount above $1,000> in the Loan_Amount field<br>3. Enter <amount greater than Loan_Amount> in the Down_Payment_Amount field<br>4. Select a valid Collateral_Account<br>5. Click Submit | Form does not submit; Down_Payment_Amount must be less than Loan Amount | high |
| TC-011 |  | Submit with Collateral_Account funds insufficient for required collateral value |  | 1. Select a Loan_Type<br>2. Enter <valid Loan_Amount> in the Loan_Amount field<br>3. Enter <valid Down_Payment_Amount> in the Down_Payment_Amount field<br>4. Select a Collateral_Account with insufficient funds<br>5. Click Submit | Form does not submit; error shown indicating insufficient collateral funds | high |
| TC-012 |  | Submit with Collateral_Account value less than 20% of Loan Amount |  | 1. Select a Loan_Type<br>2. Enter <valid Loan_Amount> in the Loan_Amount field<br>3. Enter <valid Down_Payment_Amount> in the Down_Payment_Amount field<br>4. Select a Collateral_Account with value less than 20% of Loan Amount<br>5. Click Submit | Form does not submit; error shown indicating must have at least 20% collateral value | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Test Loan Amount at minimum for Personal loan |  | 1. Select 'Personal' as Loan Type<br>2. Enter $1,000 in the Loan Amount field<br>3. Enter $100 in the Down Payment Amount field<br>4. Select a valid option in the Collateral Account dropdown<br>5. Click Submit | Form submits successfully; loan is created with Loan Amount of $1,000 | medium |
| TC-014 (boundary) |  | Test Loan Amount just above maximum for Personal loan |  | 1. Select 'Personal' as Loan Type<br>2. Enter $50,001 in the Loan Amount field<br>3. Enter $100 in the Down Payment Amount field<br>4. Select a valid option in the Collateral Account dropdown<br>5. Click Submit | Form is blocked; error shown indicating Loan Amount exceeds maximum allowed for Personal loan | medium |
| TC-015 (boundary) |  | Test Down Payment Amount at minimum required for Loan Amount |  | 1. Select 'Auto' as Loan Type<br>2. Enter $5,000 in the Loan Amount field<br>3. Enter $500 in the Down Payment Amount field<br>4. Select a valid option in the Collateral Account dropdown<br>5. Click Submit | Form submits successfully; loan is created with Down Payment Amount of $500 | medium |
| TC-016 (boundary) |  | Test Down Payment Amount just below 10% of Loan Amount |  | 1. Select 'Home' as Loan Type<br>2. Enter $100,000 in the Loan Amount field<br>3. Enter $9,999 in the Down Payment Amount field<br>4. Select a valid option in the Collateral Account dropdown<br>5. Click Submit | Form is blocked; error shown indicating Down Payment Amount must be at least 10% of Loan Amount | medium |
| TC-017 (boundary) |  | Test Collateral value at minimum required for approval |  | 1. Select 'Home' as Loan Type<br>2. Enter $100,000 in the Loan Amount field<br>3. Enter $10,000 in the Down Payment Amount field<br>4. Select a valid option in the Collateral Account dropdown<br>5. Click Submit | Form is blocked; error shown indicating collateral value must be at least 20% of Loan Amount | medium |
| TC-018 (input_edge) |  | Enter long text in Loan Type field |  | 1. Enter a string of 200 characters in the Loan Type field | Field displays an error indicating input exceeds maximum length allowed | low |

---

## Update Contact Info

Total: **20** (positive: 1, negative: 15, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Update customer profile with valid information | User logged in as <Customer>, Customer profile page is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Enter <valid state> in the State field<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click Update Profile | Profile updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Form does not submit; error shown on First_Name, Last_Name, Street_Address, City, State, ZIP_Code, Phone_Number fields indicating they are required | high |
| TC-010 |  | Enter invalid format in First Name field and submit |  | 1. Enter <invalid format> in the First_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it must be in valid format | medium |
| TC-011 |  | Enter invalid format in Last Name field and submit |  | 1. Enter <invalid format> in the Last_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it must be in valid format | medium |
| TC-012 |  | Enter invalid format in Street Address field and submit |  | 1. Enter <invalid format> in the Street_Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it must be in valid format | medium |
| TC-013 |  | Enter invalid format in City field and submit |  | 1. Enter <invalid format> in the City field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it must be in valid format | medium |
| TC-014 |  | Enter invalid format in State field and submit |  | 1. Enter <invalid format> in the State field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it must be in valid format | medium |
| TC-015 |  | Enter invalid format in ZIP Code field and submit |  | 1. Enter <invalid format> in the ZIP_Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it must be in valid format | medium |
| TC-016 |  | Enter invalid format in Phone Number field and submit |  | 1. Enter <invalid format> in the Phone_Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it must be in valid format | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (input_edge) |  | Enter a very long string in the First Name field | User is on the Update Contact Info form | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error banner displays indicating the First Name is invalid. | low |
| TC-018 (input_edge) |  | Enter special characters in the Last Name field | User is on the Update Contact Info form | 1. Enter special characters (e.g., @#$%) in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error banner displays indicating the Last Name is invalid. | low |
| TC-019 (input_edge) |  | Enter a valid ZIP Code with leading/trailing whitespace | User is on the Update Contact Info form | 1. Enter ' 12345 ' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |
| TC-020 (input_edge) |  | Enter a valid Phone Number with more than allowed digits | User is on the Update Contact Info form | 1. Enter a Phone Number with 15 digits in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error banner displays indicating the Phone Number is invalid. | low |

---

## Manage Cards

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Card Request Form with valid data | User logged in as <User>, Account is in good standing | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click Request Card | Card request submitted successfully. | high |
| TC-002 |  | Update Card Controls with valid data | User logged in as <User> | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid spending limit below policy limit> in the New Spending Limit field<br>3. Select 'Active' from the Card Status dropdown<br>4. Click Update Controls | Card controls updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank and submit |  | 1. Leave the Account to Link field blank<br>2. Fill in the Card Type and Shipping Address fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Leave the Shipping Address field blank and submit |  | 1. Leave the Shipping Address field blank<br>2. Fill in the Card Type and Account to Link fields<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating it is required | high |
| TC-005 |  | Submit the Card Request Form with an incomplete address |  | 1. Fill in the Account to Link field<br>2. Fill in the Shipping Address field with incomplete information<br>3. Select a Card Type<br>4. Click Request Card | Inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-006 |  | Attempt to update controls without selecting an existing card |  | 1. Leave the Select Existing Card field blank<br>2. Fill in the New Spending Limit field<br>3. Click Update Controls | Inline validation error appears on the Select Existing Card field indicating it is required | high |
| TC-007 |  | Submit the Card Controls Form with a spending limit above policy limit |  | 1. Select an Existing Card<br>2. Enter <amount above policy limit> in the New Spending Limit field<br>3. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating 'must be below policy limit' | high |
| TC-008 |  | Enter an invalid date range in the Travel Notice field |  | 1. Select an Existing Card<br>2. Enter <invalid date range> in the Travel Notice field<br>3. Click Update Controls | Inline validation error appears on the Travel Notice field indicating 'must be a valid date range' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Test New Spending Limit at policy limit | User has selected an existing card | 1. Enter the maximum allowed spending limit in the New Spending Limit field<br>2. Fill all other required fields<br>3. Click Update Controls | Card controls updated successfully. | medium |
| TC-010 (boundary) |  | Test New Spending Limit above policy limit | User has selected an existing card | 1. Enter a value above the maximum allowed spending limit in the New Spending Limit field<br>2. Fill all other required fields<br>3. Click Update Controls | Inline error displayed indicating the spending limit exceeds policy limits. | medium |
| TC-011 (boundary) |  | Test Travel Notice with valid date range |  | 1. Enter a valid start date and end date in the Travel Notice field<br>2. Fill all other required fields<br>3. Click Update Controls | Card controls updated successfully. | medium |
| TC-012 (boundary) |  | Test Travel Notice with invalid date range |  | 1. Enter an end date that is before the start date in the Travel Notice field<br>2. Fill all other required fields<br>3. Click Update Controls | Inline error displayed indicating the date range is invalid. | medium |
| TC-013 (input_edge) |  | Test Shipping Address with leading/trailing whitespace |  | 1. Enter a shipping address with leading and trailing spaces in the Shipping Address field<br>2. Fill all other required fields<br>3. Click Request Card | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |
| TC-014 (input_edge) |  | Test Shipping Address with special characters |  | 1. Enter a shipping address containing special characters in the Shipping Address field<br>2. Fill all other required fields<br>3. Click Request Card | Shipping address is accepted without error. | low |

---

## Investments

Total: **18** (positive: 2, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Execute a successful trade | User logged in as <Investor>, User has sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter '10' in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | Trade executed successfully. Order ID is displayed. | high |
| TC-002 |  | Create a successful recurring investment plan | User logged in as <Investor>, User has adequate balance in the funding account | 1. Enter <valid fund symbol> in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Monthly' from the Frequency dropdown<br>4. Select a date in the future in the Start Date field<br>5. Select <valid funding account> from the Funding Account dropdown<br>6. Click Create Plan | Plan created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Fund Symbol field blank and submit the Trade Funds Form |  | 1. Leave the Fund Symbol field blank<br>2. Fill in all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating it is required | high |
| TC-004 |  | Leave the Quantity field blank and submit the Trade Funds Form |  | 1. Leave the Quantity field blank<br>2. Fill in all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-005 |  | Enter a Fund Symbol that does not exist and submit the Trade Funds Form |  | 1. Enter <non-existent fund symbol> in the Fund Symbol field<br>2. Fill in all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating 'symbol must exist' | high |
| TC-006 |  | Enter a Quantity of zero and submit the Trade Funds Form |  | 1. Enter 0 in the Quantity field<br>2. Fill in all other required fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating 'must be greater than zero' | high |
| TC-007 |  | Leave the Contribution Amount field blank and submit the Recurring Investment Plan Form |  | 1. Leave the Contribution Amount field blank<br>2. Fill in all other required fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it is required | high |
| TC-008 |  | Enter a Contribution Amount below the minimum and submit the Recurring Investment Plan Form |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Fill in all other required fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating 'must meet minimum' | high |
| TC-009 |  | Leave the Start Date field blank and submit the Recurring Investment Plan Form |  | 1. Leave the Start Date field blank<br>2. Fill in all other required fields<br>3. Click Create Plan | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 |  | Enter a Start Date that is not in the future and submit the Recurring Investment Plan Form |  | 1. Enter <past date> in the Start Date field<br>2. Fill in all other required fields<br>3. Click Create Plan | Inline validation error appears on the Start Date field indicating 'must be in the future' | high |
| TC-011 |  | Leave the Funding Account field blank and submit the Recurring Investment Plan Form |  | 1. Leave the Funding Account field blank<br>2. Fill in all other required fields<br>3. Click Create Plan | Inline validation error appears on the Funding Account field indicating it is required | high |
| TC-012 |  | Attempt to create a plan without adequate balance in the Funding Account |  | 1. Fill in all required fields with valid data<br>2. Ensure the Funding Account does not have adequate balance<br>3. Click Create Plan | Inline validation error appears indicating 'funding account must have adequate balance' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Test Quantity with minimum valid value |  | 1. Select 'Buy' from the Action dropdown<br>2. Enter exactly 1 in the Quantity field<br>3. Enter a valid Fund Symbol<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Trade executes successfully; order ID is displayed | medium |
| TC-014 (boundary) |  | Test Quantity with below minimum value |  | 1. Select 'Buy' from the Action dropdown<br>2. Enter 0 in the Quantity field<br>3. Enter a valid Fund Symbol<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Inline error shown indicating 'Quantity must be greater than zero' | medium |
| TC-015 (boundary) |  | Test Contribution Amount with minimum valid value |  | 1. Enter exactly the minimum required amount in the Contribution Amount field<br>2. Enter a valid Fund Symbol<br>3. Select a Frequency<br>4. Enter a Start Date in the future<br>5. Select a Funding Account<br>6. Click Create Plan | Plan created successfully; success message is displayed | medium |
| TC-016 (boundary) |  | Test Contribution Amount with below minimum value |  | 1. Enter an amount below the minimum in the Contribution Amount field<br>2. Enter a valid Fund Symbol<br>3. Select a Frequency<br>4. Enter a Start Date in the future<br>5. Select a Funding Account<br>6. Click Create Plan | Inline error shown indicating 'Contribution Amount must meet minimum' | medium |
| TC-017 (boundary) |  | Test Start Date with today's date |  | 1. Enter today's date in the Start Date field<br>2. Enter a valid Fund Symbol<br>3. Enter a valid Contribution Amount<br>4. Select a Frequency<br>5. Select a Funding Account<br>6. Click Create Plan | Inline error shown indicating 'Start date must be in the future' | medium |
| TC-018 (boundary) |  | Test Start Date with a date in the past |  | 1. Enter a date in the past in the Start Date field<br>2. Enter a valid Fund Symbol<br>3. Enter a valid Contribution Amount<br>4. Select a Frequency<br>5. Select a Funding Account<br>6. Click Create Plan | Inline error shown indicating 'Start date must be in the future' | medium |

---

## Account Statements

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Generate statement with valid date range and account selection | User logged in as <Account Holder>, Valid date range is established | 1. Select <valid account> from the Account dropdown<br>2. Enter <valid start date> and <valid end date> in the Statement Period fields<br>3. Click Generate Statement | Statement generated successfully. | high |
| TC-002 |  | Save e-statement preference with valid email address | User logged in as <Account Holder> | 1. Enter <valid email address> in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account dropdown empty and submit the Generate Statement form |  | 1. Leave the Account field blank<br>2. Fill in the Statement Period with a valid date range<br>3. Click Generate Statement | Form does not submit; Account field is highlighted with an error indicating it is required. | high |
| TC-004 |  | Leave the Email Address field blank and submit the e-Statement Preference form |  | 1. Leave the Email Address field blank<br>2. Click Save Preference | Form does not submit; Email Address field is highlighted with an error indicating it is required. | high |
| TC-005 |  | Enter an invalid email format in the Email Address field |  | 1. Enter <invalid email format> in the Email Address field<br>2. Click Save Preference | Form does not submit; Email Address field displays an error: 'Please provide a valid email address.' | medium |
| TC-006 |  | Submit the Generate Statement form with an invalid date range |  | 1. Enter <invalid date range> in the Statement Period field<br>2. Select a valid Account<br>3. Click Generate Statement | Form does not submit; Statement Period field displays an error indicating valid date range required. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Test valid date range for Statement Period | User is on the Statements page | 1. Enter a valid date range in the Statement Period field<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Statement generated successfully. | medium |
| TC-008 (boundary) |  | Test invalid date range for Statement Period | User is on the Statements page | 1. Enter an invalid date range in the Statement Period field<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Unable to generate statement — please try again later. | medium |
| TC-009 (input_edge) |  | Test valid email address format | User is on the e-statement preference form | 1. Enter a valid email address in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | medium |
| TC-010 (input_edge) |  | Test invalid email address format | User is on the e-statement preference form | 1. Enter an invalid email address in the Email Address field<br>2. Click Save Preference | Please provide a valid email address. | medium |
| TC-011 (input_edge) |  | Test email address with leading/trailing whitespace | User is on the e-statement preference form | 1. Enter '    test@example.com    ' in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | low |

---

## Security Settings

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Change password successfully with valid inputs | User logged in as <User>, User knows the current password | 1. Enter <current password> in the Current Password field<br>2. Enter <valid strong password> in the New Password field<br>3. Enter <valid strong password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave Current Password blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 |  | Leave New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Leave the New Password field blank<br>3. Fill Confirm New Password with valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 |  | Leave Confirm New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 |  | Enter invalid Current Password and submit |  | 1. Enter <invalid current password> in the Current Password field<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating 'must verify current password' | high |
| TC-006 |  | Enter New Password that does not meet strong-password policy |  | 1. Fill Current Password with valid value<br>2. Enter <weak password> in the New Password field<br>3. Fill Confirm New Password with the same <weak password><br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'must meet strong-password policy' | high |
| TC-007 |  | Enter New Password and Confirm New Password that do not match |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with a different value<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'must match New Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter a strong password that meets the policy exactly | User is logged in and on the Security Settings page | 1. Enter the current password in the Current Password field<br>2. Enter a strong password that meets the strong-password policy in the New Password field<br>3. Enter the same strong password in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) |  | Enter a password that is one character short of the strong password requirement | User is logged in and on the Security Settings page | 1. Enter the current password in the Current Password field<br>2. Enter a password that is one character short of the strong-password policy in the New Password field<br>3. Enter the same short password in the Confirm New Password field<br>4. Click Change Password | New Password displays an error indicating it does not meet the strong-password policy. | medium |
| TC-010 (boundary) |  | Enter a mismatched password in Confirm New Password field | User is logged in and on the Security Settings page | 1. Enter the current password in the Current Password field<br>2. Enter a strong password in the New Password field<br>3. Enter a different password in the Confirm New Password field<br>4. Click Change Password | Confirm New Password displays an error indicating it must match New Password. | medium |
| TC-011 (input_edge) |  | Enter a very long password exceeding the maximum length | User is logged in and on the Security Settings page | 1. Enter the current password in the Current Password field<br>2. Enter a very long password (over the maximum length) in the New Password field<br>3. Enter the same long password in the Confirm New Password field<br>4. Click Change Password | New Password displays an error indicating it exceeds the maximum length allowed. | low |

---

## Support Center

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Send a secure message successfully | User logged in as <User> | 1. Enter 'Test Subject' in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter 'This is a test message.' in the Message Body<br>4. Upload a valid file type in the Attachment field<br>5. Click 'Send Message' | Message sent successfully with ticket ID | high |
| TC-002 |  | Request a callback successfully | User logged in as <User> | 1. Select 'Account' from the Reason for Call dropdown<br>2. Enter a date that is at least the next business day in the Preferred Date field<br>3. Enter '10:00 AM - 11:00 AM' in the Preferred Time Window field<br>4. Verify the Phone Number field is pre-filled and editable<br>5. Click 'Request Callback' | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Subject field blank and submit |  | 1. Leave the Subject field blank<br>2. Fill in the Category field with a valid option<br>3. Fill in the Message Body field with valid content<br>4. Click Send Message | Inline validation error appears on the Subject field indicating it is required | high |
| TC-004 |  | Leave the Message Body field blank and submit |  | 1. Fill in the Subject field with valid content<br>2. Fill in the Category field with a valid option<br>3. Leave the Message Body field blank<br>4. Click Send Message | Inline validation error appears on the Message Body field indicating it must be present | high |
| TC-005 |  | Submit the Secure Message Form with an invalid attachment type |  | 1. Fill in the Subject field with valid content<br>2. Fill in the Category field with a valid option<br>3. Fill in the Message Body field with valid content<br>4. Upload an invalid file type in the Attachment field<br>5. Click Send Message | Inline validation error appears on the Attachment field indicating attachment types must be valid | high |
| TC-006 |  | Leave the Reason for Call field blank and submit the Schedule Callback Form |  | 1. Leave the Reason for Call field blank<br>2. Fill in the Preferred Date field with a valid date<br>3. Fill in the Preferred Time Window field with valid content<br>4. Fill in the Phone Number field with a valid number<br>5. Click Request Callback | Inline validation error appears on the Reason for Call field indicating it is required | high |
| TC-007 |  | Submit the Schedule Callback Form with an invalid phone number format |  | 1. Fill in the Reason for Call field with a valid option<br>2. Fill in the Preferred Date field with a valid date<br>3. Fill in the Preferred Time Window field with valid content<br>4. Enter an invalid phone number format in the Phone Number field<br>5. Click Request Callback | Inline validation error appears on the Phone Number field indicating phone number format must be valid | high |
| TC-008 |  | Submit the Schedule Callback Form with a Preferred Date before the next business day |  | 1. Fill in the Reason for Call field with a valid option<br>2. Enter a date that is not the next business day in the Preferred Date field<br>3. Fill in the Preferred Time Window field with valid content<br>4. Fill in the Phone Number field with a valid number<br>5. Click Request Callback | Inline validation error appears on the Preferred Date field indicating date must be at least the next business day | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Subject field at maximum length |  | 1. Enter a subject string at the maximum allowed length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message Body field<br>4. Click Send Message | Form submits successfully; message sent with ticket ID | medium |
| TC-010 (boundary) |  | Subject field exceeds maximum length |  | 1. Enter a subject string exceeding the maximum allowed length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message Body field<br>4. Click Send Message | Inline error displayed indicating subject length is invalid | medium |
| TC-011 (boundary) |  | Preferred Date is set to the next business day |  | 1. Select a reason for the call from the dropdown<br>2. Set the Preferred Date to the next business day<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Callback request submitted and email confirmation sent | medium |
| TC-012 (boundary) |  | Preferred Date set to today |  | 1. Select a reason for the call from the dropdown<br>2. Set the Preferred Date to today<br>3. Enter a valid phone number in the Phone Number field<br>4. Click Request Callback | Inline error displayed indicating date must be at least the next business day | medium |
| TC-013 (input_edge) |  | Message Body with long text |  | 1. Enter a very long string (200+ characters) in the Message Body field<br>2. Enter a valid subject in the Subject field<br>3. Select a category from the dropdown<br>4. Click Send Message | Form submits successfully; message sent with ticket ID | low |
| TC-014 (input_edge) |  | Phone Number with special characters |  | 1. Select a reason for the call from the dropdown<br>2. Set the Preferred Date to the next business day<br>3. Enter a phone number with special characters in the Phone Number field<br>4. Click Request Callback | Inline error displayed indicating phone number format must be valid | low |

---
