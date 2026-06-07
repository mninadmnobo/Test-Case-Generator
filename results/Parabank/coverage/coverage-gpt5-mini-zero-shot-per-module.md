# Test Coverage Report

**Ground Truth:** ParaBank Test Cases v1.1
**Generated Suite:** gpt-5-mini (zero_shot_per_module) — 198 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same, similar, or an implied observable behaviour.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 119 |
| GT cases not covered by GEN | 81 |
| **Overall coverage** | **59.5%** |
| GEN cases with no GT counterpart (extras) | ~80 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 9 | 5 | **64.3%** |
| Register | 25 | 14 | 11 | **56.0%** |
| Accounts Overview | 9 | 6 | 3 | **66.7%** |
| Open New Account | 14 | 11 | 3 | **78.6%** |
| Transfer Funds | 16 | 10 | 6 | **62.5%** |
| Payments | 17 | 7 | 10 | **41.2%** |
| Request Loan | 20 | 13 | 7 | **65.0%** |
| Update Contact Info | 20 | 5 | 15 | **25.0%** |
| Manage Cards | 13 | 9 | 4 | **69.2%** |
| Investments | 15 | 12 | 3 | **80.0%** |
| Account Statements | 12 | 9 | 3 | **75.0%** |
| Security Settings | 11 | 5 | 6 | **45.5%** |
| Support Center | 14 | 9 | 5 | **64.3%** |
| **Total** | **200** | **119** | **81** | **59.5%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (5 missing)
- MW-LOGIN-002 Valid login with username
- MW-LOGIN-006 Unregistered email
- MW-LOGIN-011 Password without lowercase
- MW-LOGIN-012 Password without number
- MW-LOGIN-013 Password without special char

### Register (11 missing)
- MW-REG-003 State dropdown
- MW-REG-007 Last Name empty
- MW-REG-008 Street Address empty
- MW-REG-009 City empty
- MW-REG-011 ZIP Code empty
- MW-REG-014 Phone Number empty
- MW-REG-016 SSN empty
- MW-REG-021 Confirm Password empty
- MW-REG-022 All fields empty
- MW-REG-025 Email with leading/trailing spaces
- MW-REG-026 Registration session timeout

### Accounts Overview (3 missing)
- MW-AO-007 High volume of accounts
- MW-AO-008 Zero balance display
- MW-AO-009 Extreme negative balance

### Open New Account (3 missing)
- MW-ONA-012 Exact minimum Savings ($100)
- MW-ONA-013 Just below minimum
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (6 missing)
- MW-TF-007 Negative amount
- MW-TF-009 Same source and destination
- MW-TF-012 No destination selected
- MW-TF-014 Minimum transfer ($0.01)
- MW-TF-015 Transfer amount just above balance
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

### Request Loan (7 missing)
- MW-RL-004 Loan type cards
- MW-RL-006 Personal loan above maximum
- MW-RL-007 Auto loan below minimum
- MW-RL-009 Home loan below minimum
- MW-RL-014 No loan type selected
- MW-RL-016 Exact minimum Personal ($1,000)
- MW-RL-020 Down payment exactly one cent below 10%

### Update Contact Info (15 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-003 Update First Name
- MW-UCI-004 Update Last Name
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

### Manage Cards (4 missing)
- MW-MC-002 Request Credit card
- MW-MC-004 No account selected
- MW-MC-012 Travel notice for same day
- MW-MC-013 Rapid status toggle

### Investments (3 missing)
- MW-INV-010 Create monthly plan
- MW-INV-014 Start date exactly today
- MW-INV-015 Sell exact total shares owned

### Account Statements (3 missing)
- MW-AS-010 Custom date range spanning years
- MW-AS-011 Opt-out clears email field
- MW-AS-012 Invalid characters in email

### Security Settings (6 missing)
- MW-SS-004 New password missing uppercase
- MW-SS-005 New password missing lowercase
- MW-SS-006 New password missing number
- MW-SS-007 New password missing special char
- MW-SS-009 New password matches current password
- MW-SS-010 Passwords match but differ by trailing space

### Support Center (5 missing)
- MW-SC-003 Empty subject
- MW-SC-011 Email confirmation
- MW-SC-012 Callback preferred time overlapping cutoff
- MW-SC-013 Concurrent message submissions
- MW-SC-014 Extremely large attachment

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~4 extra types)
- Password exactly 8 characters long
- Forgot password link functionality
- Email with leading/trailing spaces is trimmed
- Password contains Unicode characters

### Register (~8 extra types)
- Password exactly 8 chars
- Email with uppercase and plus-addressing
- Auto-formatting phone number on blur
- Auto-formatting SSN on blur
- Street address special characters
- ZIP code with leading zeros
- Password with spaces and special characters
- Very long username domain

### Accounts Overview (~6 extra types)
- Clicking masked account number behavior
- Zero accounts empty state display
- Account numbers shorter than 4 digits handled gracefully
- Very large balances summed without overflow
- Deterministic ordering of same open date
- Server error handles gracefully

### Open New Account (~5 extra types)
- Funding account balance equals deposit amount exactly
- Deposit amount with cents/decimals
- Deposit amount with more than 2 decimals
- Extremely large deposit amount
- Switching account type triggers real-time revalidation

### Transfer Funds (~5 extra types)
- Confirm external account empty
- External account containing non-digit chars
- Transfer amount with exactly 2 decimal places
- Transfer amount with > 2 decimal places
- UI updates correctly when switching transfer types

### Payments (~6 extra types)
- Correct validation error and resubmit without reload
- Invalid ZIP code format
- Invalid phone number format
- Zero or negative payment amounts
- Confirm account formatted with dashes causes mismatch
- Extremely long payee name boundary test

### Request Loan (~3 extra types)
- Non-numeric loan amount rejected
- All required fields left empty multiple validation
- Collateral account balance exactly 20% of loan

### Update Contact Info (~10 extra types)
- Accept common phone formats
- Trim leading/trailing spaces
- Accept 2 letter state uppercase
- Reject phone with letters
- Reject invalid state code
- Reject all cleared fields
- Reject short phone
- Accept ZIP+4 without dash
- Accept names with hyphens
- Accept city with non-ASCII characters

### Manage Cards (~7 extra types)
- Missing street in address
- Account not in good standing
- Leave card type unselected
- Non-numeric spending limit
- Activate frozen card with admin hold
- Extremely large spending limit
- Leave travel notice empty while updating other fields

### Investments (~7 extra types)
- Snapshot read-only validation
- Snapshot updates after trade
- Reject trade when action not selected
- Reject trade when funding not selected
- Multiple inline validation failures
- Fractional quantity allowed/handled
- Create recurring plan with exact account balance

### Account Statements (~4 extra types)
- Forms side-by-side layout
- Opt in without email
- Single-day custom range
- Custom range including Leap Year Feb 29

### Security Settings (~6 extra types)
- Reject new password exceeding max length
- XSS prevention in password
- Submit all fields empty
- Minimum allowed length meeting complexity
- Maximum allowed length limit check
- Unicode/emoji characters in password

### Support Center (~9 extra types)
- Message with no attachment
- Edit pre-filled phone number
- Missing message body
- Exceed max subject length
- Unsupported attachment type
- Missing reason for call dropdown
- Date in past
- Rich text body only
- Next business day boundary (Friday to Monday)
