# Test Coverage Report

**Ground Truth:** ParaBank Test Cases v1.1
**Generated Suite:** gpt-5-mini (few_shot_per_module) — 158 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same, similar, or an implied observable behaviour.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 120 |
| GT cases not covered by GEN | 80 |
| **Overall coverage** | **60.0%** |
| GEN cases with no GT counterpart (extras) | ~51 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 10 | 4 | **71.4%** |
| Register | 25 | 14 | 11 | **56.0%** |
| Accounts Overview | 9 | 8 | 1 | **88.9%** |
| Open New Account | 14 | 13 | 1 | **92.9%** |
| Transfer Funds | 16 | 11 | 5 | **68.8%** |
| Payments | 17 | 7 | 10 | **41.2%** |
| Request Loan | 20 | 12 | 8 | **60.0%** |
| Update Contact Info | 20 | 5 | 15 | **25.0%** |
| Manage Cards | 13 | 11 | 2 | **84.6%** |
| Investments | 15 | 8 | 7 | **53.3%** |
| Account Statements | 12 | 7 | 5 | **58.3%** |
| Security Settings | 11 | 6 | 5 | **54.5%** |
| Support Center | 14 | 8 | 6 | **57.1%** |
| **Total** | **200** | **120** | **80** | **60.0%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (4 missing)
- MW-LOGIN-011 Password without lowercase
- MW-LOGIN-012 Password without number
- MW-LOGIN-013 Password without special char
- MW-LOGIN-014 Extremely long email

### Register (11 missing)
- MW-REG-003 State dropdown
- MW-REG-007 Last Name empty
- MW-REG-008 Street Address empty
- MW-REG-009 City empty
- MW-REG-010 State not selected
- MW-REG-011 ZIP Code empty
- MW-REG-014 Phone Number empty
- MW-REG-016 SSN empty
- MW-REG-021 Confirm Password empty
- MW-REG-022 All fields empty
- MW-REG-026 Registration session timeout

### Accounts Overview (1 missing)
- MW-AO-008 Zero balance display

### Open New Account (1 missing)
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (5 missing)
- MW-TF-009 Same source and destination
- MW-TF-011 No source selected
- MW-TF-012 No destination selected
- MW-TF-014 Minimum transfer ($0.01)
- MW-TF-016 External routing number boundaries

### Payments (10 missing)
- MW-BP-002 Quick select payee
- MW-BP-005 Street Address empty
- MW-BP-006 City empty
- MW-BP-007 State empty
- MW-BP-008 ZIP Code empty
- MW-BP-009 Phone empty
- MW-BP-010 Account Number empty
- MW-BP-011 Confirm Account empty
- MW-BP-013 Amount empty
- MW-BP-017 XSS payload in Payee Name

### Request Loan (8 missing)
- MW-RL-004 Loan type cards
- MW-RL-006 Personal loan above maximum
- MW-RL-007 Auto loan below minimum
- MW-RL-009 Home loan below minimum
- MW-RL-010 Home loan above maximum
- MW-RL-014 No loan type selected
- MW-RL-017 Exact maximum Personal ($50,000)
- MW-RL-020 Down payment exactly one cent below 10%

### Update Contact Info (15 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-003 Update First Name
- MW-UCI-004 Update Last Name
- MW-UCI-005 Update Address
- MW-UCI-006 Update City
- MW-UCI-007 Update State
- MW-UCI-008 Update ZIP Code
- MW-UCI-011 Last Name empty
- MW-UCI-012 Address empty
- MW-UCI-013 City empty
- MW-UCI-014 State empty
- MW-UCI-015 ZIP Code empty
- MW-UCI-016 Phone empty
- MW-UCI-019 Special characters in City
- MW-UCI-020 Non-US ZIP code format

### Manage Cards (2 missing)
- MW-MC-004 No account selected
- MW-MC-013 Rapid status toggle

### Investments (7 missing)
- MW-INV-004 Fund symbol autocomplete
- MW-INV-007 Insufficient buying power
- MW-INV-009 Create weekly plan
- MW-INV-012 Below minimum contribution
- MW-INV-013 Insufficient funding balance
- MW-INV-014 Start date exactly today
- MW-INV-015 Sell exact total shares owned

### Account Statements (5 missing)
- MW-AS-007 Opt-out of paperless
- MW-AS-009 Empty email with opt-in
- MW-AS-010 Custom date range spanning years
- MW-AS-011 Opt-out clears email field
- MW-AS-012 Invalid characters in email

### Security Settings (5 missing)
- MW-SS-004 New password missing uppercase
- MW-SS-005 New password missing lowercase
- MW-SS-006 New password missing number
- MW-SS-007 New password missing special char
- MW-SS-010 Passwords match but differ by trailing space

### Support Center (6 missing)
- MW-SC-003 Empty subject
- MW-SC-006 Category dropdown
- MW-SC-011 Email confirmation
- MW-SC-012 Callback preferred time overlapping cutoff
- MW-SC-013 Concurrent message submissions
- MW-SC-014 Extremely large attachment

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~2 extra types)
- Sign in with password at exact minimum length
- Fail authentication once and verify the password field is cleared and user can immediately retry

### Register (~3 extra types)
- Successful registration with password at minimum length
- Boundary ZIP codes (00000 and 99999) accepted if valid format
- Pasting fully formatted Phone and SSN (with separators) is accepted and preserved

### Accounts Overview (~3 extra types)
- Attempt to access Accounts Overview when not logged in
- Account full numbers are not exposed in the UI
- User with no accounts sees appropriate empty state and total zero

### Open New Account (~2 extra types)
- Enter a valid deposit amount including cents (decimal) and open account
- Attempt to open account with a very large deposit amount to test upper limits

### Transfer Funds (~1 extra types)
- User has no eligible source accounts (no Checking or Savings) and attempts transfer

### Payments (~8 extra types)
- Submit a payment that equals the exact available balance (exact-fund payment)
- Submit payment using an alternative source account (e.g., Savings)
- Submit payment with ZIP+4 and formatted phone number accepted
- Attempt payment with non-numeric characters in Payment Amount
- Attempt payment with zero or negative payment amount
- Attempt payment with invalid ZIP code format (letters or too short)
- Submit payment where Payee Account Number fields include leading/trailing spaces (trim behavior)
- Submit a minimal valid payment amount ($0.01)

### Request Loan (~2 extra types)
- Accept Loan Amounts with decimal/cents values
- Home loan at maximum boundary with exact 10% down payment and exact 20% collateral

### Update Contact Info (~5 extra types)
- Submit the Update Profile form without changing any values
- Attempt to update profile with an invalid State value (not in allowed list)
- Update Phone Number with common formatted value including parentheses and dashes
- Update names using very long input at system boundary length
- Enter a 9-digit ZIP code with hyphen (ZIP+4) and verify acceptance

### Manage Cards (~7 extra types)
- Attempt to request a card for an account not in good standing
- Enter non-numeric characters in the New Spending Limit field
- Attempt to update controls without selecting an existing card
- Request a card with a maximum-length shipping address
- Request a card with shipping address containing special/unicode characters
- Set New Spending Limit to zero to test boundary behavior
- Create a travel notice with a very long list of destinations

### Investments (~3 extra types)
- Create a recurring plan with Start Date = tomorrow (boundary future date)
- Execute a Buy trade when funding account balance equals the exact purchase cost (no leftover buying power)
- Execute a Buy trade using a very small fractional quantity (minimal positive quantity)

### Account Statements (~3 extra types)
- Generate statement for an account with no transactions returns an empty statement
- Generate statement when Start Date equals End Date (single-day statement)
- Save e-statement preference with a very long but valid email address

### Security Settings (~5 extra types)
- Open collapsed panel then change password successfully
- Attempt to submit with Current Password field empty
- Confirm New Password left empty
- Change password with new password at exact minimum length
- Change password containing Unicode characters and surrounding spaces

### Support Center (~7 extra types)
- Request callback with edited valid phone number and chosen time window
- Attempt to send secure message with Subject exceeding maximum length
- Request callback with Preferred Date on a weekend (non-business day)
- Send secure message with Subject exactly at maximum allowed length (boundary)
- Send secure message with minimal Subject length (1 character) and no attachment
- Request callback when today is Friday and chosen date is next Monday (next business day calculation)
- Request callback using international phone number in E.164 format
