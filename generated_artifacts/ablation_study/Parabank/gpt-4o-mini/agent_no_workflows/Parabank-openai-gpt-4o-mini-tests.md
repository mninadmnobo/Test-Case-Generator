# Test Cases — Parabank

Generated: 2026-06-09T10:37:46.973502Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 191 | 22 | 95 | 74 | 92 | 73 | 26 |

## Login

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Sign In button | Signed in successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email field blank and submit |  | 1. Leave the Email_Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Leave the Password field blank<br>3. Click Sign In | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email_Username field<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it must be a valid email format | medium |
| TC-005 |  | Submit with a password shorter than 8 characters |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Submit with a password missing required character types |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password without uppercase, lowercase, number, or special character> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Fill the Email_Username field with a valid email<br>2. Fill the Password field with an incorrect password<br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Email field with valid format at boundary |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Password1!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-009 (boundary) |  | Email field with invalid format just below valid |  | 1. Enter 'user@example' in the Email/Username field<br>2. Enter 'Password1!' in the Password field<br>3. Click Sign In | Form submission is blocked; an error message indicating invalid email format is shown. | medium |
| TC-010 (boundary) |  | Password field with exactly 8 characters meeting all requirements |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Passw0rd!' in the Password field<br>3. Click Sign In | Form submits successfully; user is redirected to the Accounts Overview page. | medium |
| TC-011 (boundary) |  | Password field with 7 characters below minimum requirement |  | 1. Enter 'user@example.com' in the Email/Username field<br>2. Enter 'Pass1!' in the Password field<br>3. Click Sign In | Form submission is blocked; an error message indicating the password must be at least 8 characters is shown. | medium |

---

## Register

Total: **27** (positive: 1, negative: 17, edge: 9)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful registration with valid inputs | User logged in as <Guest> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <Street Address> in the Street Address field<br>4. Enter <City> in the City field<br>5. Select <State> from the State dropdown<br>6. Enter '12345' in the ZIP Code field<br>7. Enter '(123) 456-7890' in the Phone Number field<br>8. Enter '123-45-6789' in the Social Security Number field<br>9. Enter '<valid email>' in the Username field<br>10. Enter '<valid password>' in the Password field<br>11. Enter '<valid password>' in the Confirm Password field<br>12. Click Register | Account created successfully — please sign in | high |

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
| TC-019 (boundary) |  | ZIP Code minimum format |  | 1. Enter '12345' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created. | medium |
| TC-020 (boundary) |  | ZIP Code one digit below minimum |  | 1. Enter '1234' in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Register | ZIP Code displays an error indicating the value is invalid; 'must be 5 digits or 5+4 format'. | medium |
| TC-021 (boundary) |  | Phone Number minimum format |  | 1. Enter '(123) 456-7890' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created. | medium |
| TC-022 (boundary) |  | Phone Number one character below minimum |  | 1. Enter '(123) 456-789' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Register | Phone Number displays an error indicating the value is invalid; 'must follow format (123) 456-7890'. | medium |
| TC-023 (boundary) |  | Password minimum length |  | 1. Enter 'abcdefgh' in the Password field<br>2. Enter 'abcdefgh' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Form submits successfully; account is created. | medium |
| TC-024 (boundary) |  | Password one character below minimum length |  | 1. Enter 'abcdefg' in the Password field<br>2. Enter 'abcdefg' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Register | Password displays an error indicating the value is invalid; 'must be at least 8 characters'. | medium |
| TC-025 (input_edge) |  | Long text in First Name |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Form submits successfully; account is created. | low |
| TC-026 (input_edge) |  | Special characters in Last Name |  | 1. Enter '@#%&*' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Last Name displays an error indicating the value is invalid. | low |
| TC-027 (input_edge) |  | Leading and trailing whitespace in Username |  | 1. Enter '   user@example.com   ' in the Username field<br>2. Fill all other required fields with valid data<br>3. Click Register | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Accounts Overview

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View Account Details from Accounts Table | User logged in as <Customer>, Accounts Table is displayed with account rows | 1. Click on the Account Number of the first account in the table | The Account Details page for the selected account is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to click on Account Number | Account_Number is clickable | 1. Navigate to the Accounts Overview page<br>2. Click on the Account Number | No action occurs; the Account Details view does not open as the Account Number click functionality is not implemented. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (input_edge) |  | Enter a very long string in Account Type |  | 1. Locate the Account Type column in the Accounts Table<br>2. Enter a string of 200 characters in the Account Type field | The input is either accepted or truncated with a visible indicator | low |
| TC-004 (input_edge) |  | Enter special characters in Current Balance |  | 1. Locate the Current Balance column in the Accounts Table<br>2. Enter a string with special characters in the Current Balance field | A specific error is shown indicating invalid input for Current Balance | low |
| TC-005 (input_edge) |  | Enter leading and trailing whitespace in Account Status |  | 1. Locate the Account Status column in the Accounts Table<br>2. Enter a value with leading and trailing spaces in the Account Status field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Open New Account

Total: **12** (positive: 2, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open a Checking account with valid initial deposit | User logged in as <Customer>, Funding Source Account has sufficient balance | 1. Select 'Checking' as the Account Type<br>2. Enter '25' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! Redirects to accounts overview | high |
| TC-002 |  | Open a Savings account with valid initial deposit | User logged in as <Customer>, Funding Source Account has sufficient balance | 1. Select 'Savings' as the Account Type<br>2. Enter '100' in the Initial Deposit Amount field<br>3. Select <Funding Source Account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully! Redirects to accounts overview | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account Type field blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill in the Initial Deposit Amount and Funding Source Account fields<br>3. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave the Initial Deposit Amount field blank and submit |  | 1. Leave the Initial Deposit Amount field blank<br>2. Select an Account Type and fill in the Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Enter a non-numeric value in the Initial Deposit Amount field |  | 1. Enter <non-numeric value> in the Initial Deposit Amount field<br>2. Select an Account Type and fill in the Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-006 |  | Enter an Initial Deposit Amount less than $25 for Checking and submit |  | 1. Select Checking as Account Type<br>2. Enter <amount less than $25> in the Initial Deposit Amount field<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-007 |  | Enter an Initial Deposit Amount less than $100 for Savings and submit |  | 1. Select Savings as Account Type<br>2. Enter <amount less than $100> in the Initial Deposit Amount field<br>3. Fill in the Funding Source Account<br>4. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-008 |  | Select a Funding Source Account with insufficient balance and submit |  | 1. Select an Account Type<br>2. Enter a valid Initial Deposit Amount<br>3. Select a Funding Source Account with insufficient balance<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it must have sufficient balance | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Test minimum deposit for Checking account | User selects Checking account type | 1. Enter exactly $25 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-010 (boundary) |  | Test minimum deposit for Savings account | User selects Savings account type | 1. Enter exactly $100 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-011 (boundary) |  | Test deposit amount just below minimum for Checking account | User selects Checking account type | 1. Enter $24.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Form submission is blocked; error message displayed indicating minimum deposit of $25 required. | medium |
| TC-012 (boundary) |  | Test deposit amount just below minimum for Savings account | User selects Savings account type | 1. Enter $99.99 in the Initial Deposit Amount field<br>2. Select a valid Funding Source Account<br>3. Click Open Account | Form submission is blocked; error message displayed indicating minimum deposit of $100 required. | medium |

---

## Transfer Funds

Total: **15** (positive: 3, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Transfer funds to My ParaBank Account | User logged in as <User>, sufficient funds | 1. Select 'My ParaBank Account' from the Transfer Type radio buttons<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Select <valid internal account> from the Internal Accounts dropdown<br>5. Click Transfer | Transfer completed successfully. | high |
| TC-002 |  | Transfer funds to External Account | User logged in as <User>, sufficient funds | 1. Select 'External Account' from the Transfer Type radio buttons<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <same valid external account number> in the Confirm Account Number field<br>6. Click Transfer | Transfer completed successfully. | high |
| TC-003 |  | Transfer funds with matching account numbers for External Account | User logged in as <User>, sufficient funds | 1. Select 'External Account' from the Transfer Type radio buttons<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Enter <valid external account number> in the External Account Number field<br>5. Enter <same valid external account number> in the Confirm Account Number field<br>6. Click Transfer | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Transfer Amount field blank and submit |  | 1. Leave the Transfer Amount field blank<br>2. Fill in all other required fields<br>3. Click Transfer | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-005 |  | Enter a Transfer Amount that exceeds available funds |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Fill in all other required fields<br>3. Click Transfer | Form does not submit; error shown: 'Insufficient funds' | high |
| TC-006 |  | Select External Account and leave Confirm Account Number blank |  | 1. Select 'External Account' for Transfer Type<br>2. Leave the Confirm Account Number field blank<br>3. Fill in all other required fields<br>4. Click Transfer | Inline validation error appears on the Confirm Account Number field indicating it is required | high |
| TC-007 |  | Enter mismatched account numbers for external transfer |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid external account number> in the External Account Number field<br>3. Enter <different external account number> in the Confirm Account Number field<br>4. Fill in all other required fields<br>5. Click Transfer | Form does not submit; error shown: 'Account numbers do not match' | high |
| TC-008 |  | Attempt to transfer without selecting a Source Account |  | 1. Leave the Source Account field blank<br>2. Fill in all other required fields<br>3. Click Transfer | Inline validation error appears on the Source Account field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Transfer amount at minimum valid value | User has sufficient funds | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter the minimum valid amount in the Transfer Amount field<br>4. Select an Internal Account from the dropdown<br>5. Click Transfer | Transfer completed successfully. | medium |
| TC-010 (boundary) |  | Transfer amount just below minimum valid value | User has sufficient funds | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter an amount just below the minimum valid amount in the Transfer Amount field<br>4. Select an Internal Account from the dropdown<br>5. Click Transfer | Transfer is blocked; error shown indicating the amount is invalid. | medium |
| TC-011 (boundary) |  | Transfer amount at maximum valid value | User has sufficient funds | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter the maximum valid amount in the Transfer Amount field<br>4. Select an Internal Account from the dropdown<br>5. Click Transfer | Transfer completed successfully. | medium |
| TC-012 (boundary) |  | Transfer amount just above maximum valid value | User has sufficient funds | 1. Select 'My ParaBank Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter an amount just above the maximum valid amount in the Transfer Amount field<br>4. Select an Internal Account from the dropdown<br>5. Click Transfer | Transfer is blocked; error shown indicating the amount is invalid. | medium |
| TC-013 (input_edge) |  | Enter a very long account number in External Account Number field |  | 1. Select 'External Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter a very long account number in the External Account Number field<br>4. Enter the same long account number in the Confirm Account Number field<br>5. Click Transfer | Transfer is blocked; error shown indicating the account number is invalid. | low |
| TC-014 (input_edge) |  | Enter special characters in External Account Number field |  | 1. Select 'External Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter special characters in the External Account Number field<br>4. Enter the same special characters in the Confirm Account Number field<br>5. Click Transfer | Transfer is blocked; error shown indicating the account number is invalid. | low |
| TC-015 (input_edge) |  | Enter leading/trailing whitespace in External Account Number field |  | 1. Select 'External Account' as Transfer Type<br>2. Select 'Checking' as Source Account<br>3. Enter leading and trailing whitespace in the External Account Number field<br>4. Enter the same value in the Confirm Account Number field<br>5. Click Transfer | Transfer is blocked; error shown indicating the account number is invalid. | low |

---

## Payments

Total: **18** (positive: 1, negative: 12, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit payment with valid details | User logged in as <User>, available funds must be sufficient | 1. Enter <valid payee name> in the Payee Name field<br>2. Enter <valid street address> in the Street Address field<br>3. Enter <valid city> in the City field<br>4. Enter <valid state> in the State field<br>5. Enter <valid ZIP code> in the ZIP Code field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Enter <valid payee account number> in the Payee Account Number field<br>8. Enter the same <valid payee account number> in the Confirm Account Number field<br>9. Enter <valid payment amount> in the Payment Amount field<br>10. Select <valid source account> from the Source Account dropdown<br>11. Click the Pay button | Payment submitted successfully with reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Payee Name field blank |  | 1. Leave the Payee_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Payee_Name field indicating it is required | high |
| TC-003 |  | Leave the Street Address field blank |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-004 |  | Leave the City field blank |  | 1. Leave the City field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the City field indicating it is required | high |
| TC-005 |  | Leave the State field blank |  | 1. Leave the State field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the State field indicating it is required | high |
| TC-006 |  | Leave the ZIP Code field blank |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-008 |  | Leave the Payee Account Number field blank |  | 1. Leave the Payee_Account_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Payee_Account_Number field indicating it is required | high |
| TC-009 |  | Leave the Confirm Account Number field blank |  | 1. Leave the Confirm_Account_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating it is required | high |
| TC-010 |  | Leave the Payment Amount field blank |  | 1. Leave the Payment_Amount field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Payment_Amount field indicating it is required | high |
| TC-011 |  | Leave the Source Account field blank |  | 1. Leave the Source_Account field blank<br>2. Fill all other required fields with valid data<br>3. Click Pay | Inline validation error appears on the Source_Account field indicating it is required | high |
| TC-012 |  | Submit with mismatched account numbers |  | 1. Enter a valid Payee_Account_Number<br>2. Enter a different value in the Confirm_Account_Number field<br>3. Fill all other required fields with valid data<br>4. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating it must match Payee Account Number | high |
| TC-013 |  | Attempt to pay with insufficient funds |  | 1. Fill all required fields with valid data<br>2. Ensure available funds are insufficient<br>3. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Payment Amount at minimum boundary | Available funds are sufficient | 1. Enter <minimum allowed value> in the Payment Amount field<br>2. Fill all other required fields<br>3. Click Pay | Payment submitted successfully with reference code | medium |
| TC-015 (boundary) |  | Payment Amount just below minimum boundary | Available funds are sufficient | 1. Enter <one unit below minimum> in the Payment Amount field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating the value is below the minimum allowed | medium |
| TC-016 (input_edge) |  | Long text in Payee Name field |  | 1. Enter a very long string (200+ characters) in the Payee Name field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating the value exceeds the maximum allowed length or is truncated | low |
| TC-017 (input_edge) |  | Special characters in Payee Name field |  | 1. Enter special characters (e.g., @#$%^&*) in the Payee Name field<br>2. Fill all other required fields<br>3. Click Pay | Inline error displayed indicating invalid characters | low |
| TC-018 (input_edge) |  | Leading/trailing whitespace in Phone Number field |  | 1. Enter '   123-456-7890   ' in the Phone Number field<br>2. Fill all other required fields<br>3. Click Pay | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Request Loan

Total: **21** (positive: 3, negative: 8, edge: 10)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a Personal Loan application with valid amounts | User logged in as <Applicant>, Credit engine simulates 80% approval rate | 1. Select 'Personal' from the Loan Type cards<br>2. Enter '15000' in the Loan Amount field<br>3. Enter '1500' in the Down Payment Amount field<br>4. Select a valid <Collateral Account> from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-002 |  | Submit an Auto Loan application with valid amounts | User logged in as <Applicant>, Credit engine simulates 80% approval rate | 1. Select 'Auto' from the Loan Type cards<br>2. Enter '20000' in the Loan Amount field<br>3. Enter '2000' in the Down Payment Amount field<br>4. Select a valid <Collateral Account> from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |
| TC-003 |  | Submit a Home Loan application with valid amounts | User logged in as <Applicant>, Credit engine simulates 80% approval rate | 1. Select 'Home' from the Loan Type cards<br>2. Enter '300000' in the Loan Amount field<br>3. Enter '30000' in the Down Payment Amount field<br>4. Select a valid <Collateral Account> from the dropdown<br>5. Click Submit | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Loan Amount field blank and submit |  | 1. Leave the Loan Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Leave the Down Payment Amount field blank and submit |  | 1. Leave the Down Payment Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it is required | high |
| TC-006 |  | Leave the Collateral Account dropdown unselected and submit |  | 1. Leave the Collateral Account dropdown unselected<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Collateral Account field indicating it is required | high |
| TC-007 |  | Enter a Down Payment Amount less than 10% of Loan Amount |  | 1. Enter <amount less than 10% of Loan Amount> in the Down Payment Amount field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it must be at least 10% of Loan Amount | medium |
| TC-008 |  | Enter a Down Payment Amount greater than Loan Amount |  | 1. Enter <amount greater than Loan Amount> in the Down Payment Amount field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Down Payment Amount field indicating it must be less than Loan Amount | medium |
| TC-009 |  | Enter a Collateral Account value that does not meet the 20% collateral value requirement |  | 1. Enter <amount less than 20% of collateral value> in the Collateral Account field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Collateral Account field indicating it must be at least 20% of collateral value | medium |
| TC-010 |  | Enter a Loan Amount outside the specified range for Personal loans |  | 1. Enter <amount less than $1,000> in the Loan Amount field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Loan Amount field indicating it must be between $1,000 and $50,000 | medium |
| TC-011 |  | Attempt to submit without meeting the credit engine precondition | credit engine simulates less than 80% approval rate | 1. Fill all required fields with valid data<br>2. Click Submit | Form does not submit; Loan is not created; error shown indicating insufficient credit history | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Test minimum Loan Amount for Personal loan |  | 1. Select 'Personal' from Loan Type cards<br>2. Enter exactly $1,000 in the Loan Amount field<br>3. Enter $100 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-013 (boundary) |  | Test maximum Loan Amount for Personal loan |  | 1. Select 'Personal' from Loan Type cards<br>2. Enter exactly $50,000 in the Loan Amount field<br>3. Enter $5,000 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-014 (boundary) |  | Test minimum Loan Amount for Auto loan |  | 1. Select 'Auto' from Loan Type cards<br>2. Enter exactly $5,000 in the Loan Amount field<br>3. Enter $500 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-015 (boundary) |  | Test maximum Loan Amount for Auto loan |  | 1. Select 'Auto' from Loan Type cards<br>2. Enter exactly $75,000 in the Loan Amount field<br>3. Enter $7,500 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-016 (boundary) |  | Test minimum Loan Amount for Home loan |  | 1. Select 'Home' from Loan Type cards<br>2. Enter exactly $50,000 in the Loan Amount field<br>3. Enter $5,000 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-017 (boundary) |  | Test maximum Loan Amount for Home loan |  | 1. Select 'Home' from Loan Type cards<br>2. Enter exactly $500,000 in the Loan Amount field<br>3. Enter $50,000 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Loan approved and created successfully! | medium |
| TC-018 (boundary) |  | Test Down Payment Amount less than minimum requirement |  | 1. Select 'Personal' from Loan Type cards<br>2. Enter $1,000 in the Loan Amount field<br>3. Enter $50 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Form submission is blocked; error message shown indicating down payment must be at least 10% of Loan Amount. | medium |
| TC-019 (boundary) |  | Test Down Payment Amount equal to Loan Amount |  | 1. Select 'Personal' from Loan Type cards<br>2. Enter $1,000 in the Loan Amount field<br>3. Enter $1,000 in the Down Payment Amount field<br>4. Select a valid Collateral Account<br>5. Click Submit | Form submission is blocked; error message shown indicating down payment must be less than Loan Amount. | medium |
| TC-020 (boundary) |  | Test Collateral Account with insufficient collateral funds |  | 1. Select 'Home' from Loan Type cards<br>2. Enter $100,000 in the Loan Amount field<br>3. Enter $10,000 in the Down Payment Amount field<br>4. Select a Collateral Account with insufficient funds<br>5. Click Submit | Form submission is blocked; error message shown indicating insufficient collateral funds. | medium |
| TC-021 (boundary) |  | Test Collateral Account with exactly 20% collateral value |  | 1. Select 'Home' from Loan Type cards<br>2. Enter $100,000 in the Loan Amount field<br>3. Enter $10,000 in the Down Payment Amount field<br>4. Select a Collateral Account with collateral value of $50,000<br>5. Click Submit | Loan approved and created successfully! | medium |

---

## Update Contact Info

Total: **20** (positive: 1, negative: 15, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful profile update with valid contact information | User logged in as <Customer>, Profile page is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Enter <valid state> in the State field<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click the Update Profile button | Profile updated successfully. | high |

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
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Update Profile | Form does not submit; error shown on all required fields | high |
| TC-010 |  | Enter invalid format in First Name field |  | 1. Enter <invalid format> in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it must be a valid format | medium |
| TC-011 |  | Enter invalid format in Last Name field |  | 1. Enter <invalid format> in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it must be a valid format | medium |
| TC-012 |  | Enter invalid format in Street Address field |  | 1. Enter <invalid format> in the Street Address field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it must be a valid format | medium |
| TC-013 |  | Enter invalid format in City field |  | 1. Enter <invalid format> in the City field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the City field indicating it must be a valid format | medium |
| TC-014 |  | Enter invalid format in State field |  | 1. Enter <invalid format> in the State field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the State field indicating it must be a valid format | medium |
| TC-015 |  | Enter invalid format in ZIP Code field |  | 1. Enter <invalid format> in the ZIP Code field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it must be a valid format | medium |
| TC-016 |  | Enter invalid format in Phone Number field |  | 1. Enter <invalid format> in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it must be a valid format | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid format<br>3. Click Update Profile | The form submits successfully; the First Name field displays the entered value correctly. | low |
| TC-018 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter '@#$%^&*()' in the Last Name field<br>2. Fill all other required fields with valid format<br>3. Click Update Profile | The form submission is blocked; the Last Name field highlights an error indicating invalid format. | low |
| TC-019 (input_edge) |  | Enter leading and trailing whitespace in the Street Address field |  | 1. Enter '   123 Main St   ' in the Street Address field<br>2. Fill all other required fields with valid format<br>3. Click Update Profile | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |
| TC-020 (input_edge) |  | Enter a zero in the ZIP Code field |  | 1. Enter '0' in the ZIP Code field<br>2. Fill all other required fields with valid format<br>3. Click Update Profile | The form submission is blocked; the ZIP Code field highlights an error indicating invalid format. | low |

---

## Manage Cards

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit Card Request Form with valid data | User logged in as <User> | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click Request Card | Card request submitted successfully with tracking ID | high |
| TC-002 |  | Update Card Controls with valid data | User logged in as <User>, At least one card exists | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid spending limit> in the New Spending Limit field<br>3. Click Update Controls | Card controls updated successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank and submit the Card Request Form |  | 1. Leave the Account to Link field blank<br>2. Select a Card Type<br>3. Fill the Shipping Address<br>4. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Submit the Card Request Form with an incomplete Shipping Address |  | 1. Select a Card Type<br>2. Fill the Account to Link<br>3. Leave the Shipping Address incomplete<br>4. Click Request Card | Inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-005 |  | Leave the Select Existing Card field blank and submit the Card Controls Form |  | 1. Leave the Select Existing Card field blank<br>2. Fill the New Spending Limit<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the Select Existing Card field indicating it is required | high |
| TC-006 |  | Submit the Card Controls Form with a non-numeric New Spending Limit |  | 1. Select an Existing Card<br>2. Enter <non-numeric value> in the New Spending Limit field<br>3. Select a Card Status<br>4. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating it must be a valid numeric limit | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Submit card request with incomplete address |  | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter a partial address in the Shipping Address field<br>3. Fill in a valid Account to Link<br>4. Click 'Request Card' | Form displays an error indicating the address must be complete | medium |
| TC-008 (boundary) |  | Submit card controls with invalid spending limit |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Enter a negative number in the New Spending Limit field<br>3. Click 'Update Controls' | Form displays an error indicating the spending limit must be a valid numeric limit | medium |
| TC-009 (boundary) |  | Add travel notice with end date before start date |  | 1. Click to add a new entry in the Travel Notice repeating group<br>2. Enter today's date in the Start_Date field<br>3. Enter yesterday's date in the End_Date field<br>4. Click 'Update Controls' | Form displays an error indicating the end date must be after the start date | medium |
| TC-010 (input_edge) |  | Submit card request with leading/trailing whitespace in address |  | 1. Select 'Credit' from the Card Type dropdown<br>2. Enter ' 123 Main St ' in the Shipping Address field<br>3. Fill in a valid Account to Link<br>4. Click 'Request Card' | Leading/trailing whitespace is trimmed; saved address shown in detail page has no extra spaces | low |
| TC-011 (input_edge) |  | Submit card controls with special characters in destinations |  | 1. Click to add a new entry in the Travel Notice repeating group<br>2. Enter 'New York @ 2023' in the Destinations field<br>3. Click 'Update Controls' | Form displays a success message indicating card controls updated successfully | low |

---

## Investments

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Execute a successful trade | User logged in as <Investor>, Customer has sufficient buying power | 1. Open the Trade Funds Form<br>2. Select 'Buy' from the Action dropdown<br>3. Enter <valid fund symbol> in the Fund Symbol field<br>4. Enter <valid quantity greater than zero> in the Quantity field<br>5. Click 'Execute Trade' | 'Trade executed successfully.' with order ID is displayed | high |
| TC-002 |  | Create a recurring investment plan successfully | User logged in as <Investor>, Funding account has adequate balance | 1. Open the Recurring Investment Plan Form<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid contribution amount meeting minimum> in the Contribution Amount field<br>4. Select 'Weekly' from the Frequency dropdown<br>5. Enter <valid future date> in the Start Date field<br>6. Click 'Create Plan' | 'Plan created successfully.' is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Quantity field blank and submit the Trade Funds Form |  | 1. Leave the Quantity field blank<br>2. Fill in the Action and Fund Symbol fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it is required | high |
| TC-004 |  | Submit the Trade Funds Form with a Quantity of zero |  | 1. Enter '0' in the Quantity field<br>2. Fill in the Action and Fund Symbol fields<br>3. Click Execute Trade | Inline validation error appears on the Quantity field indicating it must be greater than zero | high |
| TC-005 |  | Submit the Trade Funds Form with a non-existent Fund Symbol |  | 1. Enter <non-existent symbol> in the Fund Symbol field<br>2. Enter a valid Quantity<br>3. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating the symbol must exist | high |
| TC-006 |  | Submit the Recurring Investment Plan Form with a blank Contribution Amount |  | 1. Leave the Contribution Amount field blank<br>2. Fill in the Fund Symbol, Frequency, and Start Date fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it is required | high |
| TC-007 |  | Submit the Recurring Investment Plan Form with a Contribution Amount below minimum |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Fill in the Fund Symbol, Frequency, and Start Date fields<br>3. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it must meet minimum contribution | high |
| TC-008 |  | Submit the Recurring Investment Plan Form with a Start Date in the past |  | 1. Enter <past date> in the Start Date field<br>2. Fill in the Fund Symbol and Contribution Amount fields<br>3. Click Create Plan | Inline validation error appears on the Start Date field indicating it must be in the future | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Quantity exactly one | User is logged in with sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter 'AAPL' in the Fund Symbol field<br>3. Enter '1' in the Quantity field<br>4. Click 'Execute Trade' | Trade executes successfully; order ID is displayed. | medium |
| TC-010 (boundary) |  | Quantity zero | User is logged in with sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter 'AAPL' in the Fund Symbol field<br>3. Enter '0' in the Quantity field<br>4. Click 'Execute Trade' | Inline error shown indicating 'Quantity must be greater than zero'. | medium |
| TC-011 (boundary) |  | Start Date today | User is logged in with sufficient balance | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Monthly' from the Frequency dropdown<br>4. Enter today's date in the Start Date field<br>5. Click 'Create Plan' | Inline error shown indicating 'Start date must be in the future'. | medium |
| TC-012 (boundary) |  | Start Date in the future | User is logged in with sufficient balance | 1. Enter 'AAPL' in the Fund Symbol field<br>2. Enter '100' in the Contribution Amount field<br>3. Select 'Monthly' from the Frequency dropdown<br>4. Enter a date one day in the future in the Start Date field<br>5. Click 'Create Plan' | Plan created successfully; schedule is stored. | medium |
| TC-013 (input_edge) |  | Fund Symbol with special characters |  | 1. Enter 'AAPL@#$' in the Fund Symbol field<br>2. Click 'Execute Trade' | Inline error shown indicating 'Symbol must exist'. | low |
| TC-014 (input_edge) |  | Long Fund Symbol |  | 1. Enter a very long string (200+ characters) in the Fund Symbol field<br>2. Click 'Execute Trade' | Inline error shown indicating 'Symbol must exist'. | low |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Generate statement successfully | User logged in as <Account Holder> | 1. Enter a valid <Statement Period> in the Statement Period field<br>2. Select a valid <Account> from the Account dropdown<br>3. Click Generate Statement | Statement generated successfully. | high |
| TC-002 |  | Save e-statement preference successfully | User logged in as <Account Holder> | 1. Enter a valid <Email Address> in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Statement Period field blank and submit |  | 1. Leave the Statement_Period field blank<br>2. Select a valid Account<br>3. Click Generate Statement | Form does not submit; Statement_Period field displays an error: 'This field is required.' | high |
| TC-004 |  | Leave the Account dropdown unselected and submit |  | 1. Select a valid Statement_Period<br>2. Leave the Account dropdown unselected<br>3. Click Generate Statement | Form does not submit; Account field displays an error: 'This field is required.' | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email_Address field blank<br>2. Click Save Preference | Form does not submit; Email_Address field highlights with guidance. | high |
| TC-006 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email_Address field<br>2. Click Save Preference | Form does not submit; Email_Address field highlights with guidance. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Test Statement Period with minimum and maximum date range | User is on the Statements page | 1. Select the Account from the dropdown<br>2. Enter the minimum allowed date range in the Statement Period field<br>3. Click Generate Statement | Statement generated successfully. | medium |
| TC-008 (boundary) |  | Test Statement Period with a date range just past the maximum limit | User is on the Statements page | 1. Select the Account from the dropdown<br>2. Enter a date range just beyond the maximum allowed in the Statement Period field<br>3. Click Generate Statement | Unable to generate statement — please try again later. | medium |
| TC-009 (input_edge) |  | Test Email Address with special characters | User is on the e-Statement preference form | 1. Enter a valid email address with special characters in the Email Address field<br>2. Click Save Preference | e-Statement preference updated. | low |
| TC-010 (input_edge) |  | Test Email Address with leading and trailing whitespace | User is on the e-Statement preference form | 1. Enter a valid email address with leading and trailing spaces in the Email Address field<br>2. Click Save Preference | Email field is highlighted with guidance. | low |

---

## Security Settings

Total: **12** (positive: 1, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Change password with valid inputs | User logged in as <User>, User knows the current password | 1. Enter <valid current password> in the Current Password field<br>2. Enter <valid new password> in the New Password field<br>3. Enter <same valid new password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave Current Password field blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 |  | Leave New Password field blank and submit |  | 1. Fill Current Password with valid value<br>2. Leave the New Password field blank<br>3. Fill Confirm New Password with valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 |  | Leave Confirm New Password field blank and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 |  | Enter mismatched passwords and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with a different value<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'must match New Password' | high |
| TC-006 |  | Enter weak password and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with a weak password<br>3. Fill Confirm New Password with the same weak password<br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'must meet strong-password policy' | high |
| TC-007 |  | Enter incorrect current password and submit |  | 1. Fill Current Password with an incorrect value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with the same valid value<br>4. Click Change Password | Inline validation error appears on the Current Password field indicating 'must verify current password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter a valid current password and a new password that meets the strong-password policy | User is logged in, User knows their current password | 1. Enter valid Current Password in the Current_Password field<br>2. Enter a New Password that meets the strong-password policy in the New_Password field<br>3. Enter the same New Password in the Confirm_New_Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) |  | Enter a new password that is one character short of the strong-password policy | User is logged in, User knows their current password | 1. Enter valid Current Password in the Current_Password field<br>2. Enter a New Password that is one character short of the strong-password policy in the New_Password field<br>3. Enter the same New Password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the New_Password field indicating it must meet strong-password policy. | medium |
| TC-010 (boundary) |  | Enter a new password and a confirm password that does not match | User is logged in, User knows their current password | 1. Enter valid Current Password in the Current_Password field<br>2. Enter a valid New Password in the New_Password field<br>3. Enter a different password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the Confirm_New_Password field indicating it must match New Password. | medium |
| TC-011 (input_edge) |  | Enter a very long password exceeding the maximum length allowed by the strong-password policy | User is logged in, User knows their current password | 1. Enter valid Current Password in the Current_Password field<br>2. Enter a very long New Password in the New_Password field<br>3. Enter the same very long password in the Confirm_New_Password field<br>4. Click Change Password | Validation error highlights the New_Password field indicating it exceeds the maximum length allowed. | low |
| TC-012 (input_edge) |  | Enter a new password with leading and trailing whitespace | User is logged in, User knows their current password | 1. Enter valid Current Password in the Current_Password field<br>2. Enter a New Password with leading and trailing spaces in the New_Password field<br>3. Enter the same New Password with spaces in the Confirm_New_Password field<br>4. Click Change Password | Leading and trailing whitespace is trimmed; password change succeeds. | low |

---

## Support Center

Total: **15** (positive: 2, negative: 5, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a secure message successfully | User logged in as <User> | 1. Enter a valid subject in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter a message in the Message Body field<br>4. Click 'Send Message' | Message sent successfully with ticket ID | high |
| TC-002 |  | Request a callback successfully | User logged in as <User> | 1. Select 'Account' from the Reason for Call dropdown<br>2. Enter a valid date in the Preferred Date field that is at least the next business day<br>3. Enter a valid time in the Preferred Time Window field<br>4. Verify the Phone Number field is pre-filled and editable<br>5. Click 'Request Callback' | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Message Body field blank and submit |  | 1. Leave the Message Body field blank<br>2. Fill in the Subject field with valid text<br>3. Select a Category from the dropdown<br>4. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-004 |  | Submit the Secure Message Form with all fields empty |  | 1. Leave the Subject field blank<br>2. Leave the Category field blank<br>3. Leave the Message Body field blank<br>4. Leave the Attachment field blank<br>5. Click Send Message | Form does not submit; error shown on Subject, Message Body, and Category fields | high |
| TC-005 |  | Submit the Schedule Callback Form with an invalid phone number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Select a Reason for Call from the dropdown<br>3. Enter a valid Preferred Date<br>4. Click Request Callback | Inline validation error appears on the Phone Number field indicating it must be valid | high |
| TC-006 |  | Submit the Schedule Callback Form with a Preferred Date in the past |  | 1. Select a Reason for Call from the dropdown<br>2. Enter a Preferred Date that is in the past<br>3. Enter a valid Phone Number<br>4. Click Request Callback | Inline validation error appears on the Preferred Date field indicating it must be at least the next business day | high |
| TC-007 |  | Submit the Schedule Callback Form with all fields empty |  | 1. Leave the Reason for Call field blank<br>2. Leave the Preferred Date field blank<br>3. Leave the Preferred Time Window field blank<br>4. Leave the Phone Number field blank<br>5. Click Request Callback | Form does not submit; error shown on Reason for Call, Preferred Date, and Phone Number fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Subject length at minimum valid length |  | 1. Enter the minimum valid length subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message Body field<br>4. Click Send Message | Form submits successfully; message sent with ticket ID | medium |
| TC-009 (boundary) |  | Subject length below minimum valid length |  | 1. Enter a subject that is one character below the minimum valid length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message Body field<br>4. Click Send Message | Inline error displayed indicating the subject length is invalid | medium |
| TC-010 (boundary) |  | Preferred Date is exactly the next business day |  | 1. Select the next business day in the Preferred_Date field<br>2. Select a reason for call from the dropdown<br>3. Enter a phone number in the Phone_Number field<br>4. Click Request Callback | Form submits successfully; callback request submitted and email confirmation sent | medium |
| TC-011 (boundary) |  | Preferred Date is one day before the next business day |  | 1. Select a date that is one day before the next business day in the Preferred_Date field<br>2. Select a reason for call from the dropdown<br>3. Enter a phone number in the Phone_Number field<br>4. Click Request Callback | Inline error displayed indicating the date must be at least the next business day | medium |
| TC-012 (data_edge) |  | Upload file at valid attachment type limit |  | 1. Upload a file of a valid attachment type in the Attachment field<br>2. Enter a subject in the Subject field<br>3. Select a category from the dropdown<br>4. Enter a message body in the Message Body field<br>5. Click Send Message | Form submits successfully; message sent with ticket ID | medium |
| TC-013 (data_edge) |  | Upload file of invalid attachment type |  | 1. Upload a file of an invalid attachment type in the Attachment field<br>2. Enter a subject in the Subject field<br>3. Select a category from the dropdown<br>4. Enter a message body in the Message Body field<br>5. Click Send Message | Inline error displayed indicating the attachment type is invalid | medium |
| TC-014 (input_edge) |  | Enter a long message body |  | 1. Enter a long text (200+ characters) in the Message Body field<br>2. Enter a subject in the Subject field<br>3. Select a category from the dropdown<br>4. Click Send Message | Form submits successfully; message sent with ticket ID | low |
| TC-015 (input_edge) |  | Enter phone number in invalid format |  | 1. Enter a phone number in an invalid format in the Phone_Number field<br>2. Select a reason for call from the dropdown<br>3. Select a preferred date in the Preferred_Date field<br>4. Click Request Callback | Inline error displayed indicating the phone number format is invalid | low |

---
