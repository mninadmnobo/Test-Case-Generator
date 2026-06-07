# Test Coverage Report

**Ground Truth:** ParaBank Test Cases v1.1
**Generated Suite:** gpt-4o-mini (few_shot_per_module) — 71 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same, similar, or an implied observable behaviour.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 57 |
| GT cases not covered by GEN | 143 |
| **Overall coverage** | **28.5%** |
| GEN cases with no GT counterpart (extras) | ~14 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 5 | 9 | **35.7%** |
| Register | 25 | 4 | 21 | **16.0%** |
| Accounts Overview | 9 | 2 | 7 | **22.2%** |
| Open New Account | 14 | 7 | 7 | **50.0%** |
| Transfer Funds | 16 | 5 | 11 | **31.3%** |
| Payments | 17 | 4 | 13 | **23.5%** |
| Request Loan | 20 | 4 | 16 | **20.0%** |
| Update Contact Info | 20 | 3 | 17 | **15.0%** |
| Manage Cards | 13 | 4 | 9 | **30.8%** |
| Investments | 15 | 6 | 9 | **40.0%** |
| Account Statements | 12 | 4 | 8 | **33.3%** |
| Security Settings | 11 | 4 | 7 | **36.4%** |
| Support Center | 14 | 5 | 9 | **35.7%** |
| **Total** | **200** | **57** | **143** | **28.5%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (9 missing)
- MW-LOGIN-002 Valid login with username
- MW-LOGIN-004 Invalid email format
- MW-LOGIN-008 Empty password field
- MW-LOGIN-010 Password without uppercase
- MW-LOGIN-011 Password without lowercase
- MW-LOGIN-012 Password without number
- MW-LOGIN-013 Password without special char
- MW-LOGIN-014 Extremely long email
- MW-LOGIN-015 SQL injection in email

### Register (21 missing)
- MW-REG-003 State dropdown
- MW-REG-004 Phone auto-formatting
- MW-REG-005 SSN auto-formatting
- MW-REG-006 First Name empty
- MW-REG-007 Last Name empty
- MW-REG-008 Street Address empty
- MW-REG-009 City empty
- MW-REG-010 State not selected
- MW-REG-011 ZIP Code empty
- MW-REG-012 Invalid ZIP format
- MW-REG-013 Valid 5+4 ZIP
- MW-REG-014 Phone Number empty
- MW-REG-015 Invalid Phone format
- MW-REG-016 SSN empty
- MW-REG-017 Invalid SSN format
- MW-REG-019 Password less than 8 chars
- MW-REG-021 Confirm Password empty
- MW-REG-022 All fields empty
- MW-REG-023 Minimum valid inputs
- MW-REG-025 Email with leading/trailing spaces
- MW-REG-026 Registration session timeout

### Accounts Overview (7 missing)
- MW-AO-001 Welcome message
- MW-AO-003 Masked account numbers
- MW-AO-004 Total balance footer
- MW-AO-005 Accounts ordered by date
- MW-AO-006 Active account badges
- MW-AO-008 Zero balance display
- MW-AO-009 Extreme negative balance

### Open New Account (7 missing)
- MW-ONA-004 Real-time validation
- MW-ONA-005 Account type not selected
- MW-ONA-009 Insufficient funding balance
- MW-ONA-010 No funding account selected
- MW-ONA-013 Just below minimum
- MW-ONA-014 Deposit with excessive precision
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (11 missing)
- MW-TF-003 Source account filter
- MW-TF-004 Transfer type toggle
- MW-TF-005 Empty transfer amount
- MW-TF-006 Zero transfer amount
- MW-TF-007 Negative amount
- MW-TF-009 Same source and destination
- MW-TF-011 No source selected
- MW-TF-012 No destination selected
- MW-TF-014 Minimum transfer ($0.01)
- MW-TF-015 Transfer amount just above balance
- MW-TF-016 External routing number boundaries

### Payments (13 missing)
- MW-BP-002 Quick select payee
- MW-BP-003 Balance updated
- MW-BP-004 Payee Name empty
- MW-BP-005 Street Address empty
- MW-BP-006 City empty
- MW-BP-007 State empty
- MW-BP-008 ZIP Code empty
- MW-BP-009 Phone empty
- MW-BP-010 Account Number empty
- MW-BP-011 Confirm Account empty
- MW-BP-013 Amount empty
- MW-BP-015 No source account
- MW-BP-017 XSS payload in Payee Name

### Request Loan (16 missing)
- MW-RL-002 Auto loan approved
- MW-RL-003 Home loan approved
- MW-RL-004 Loan type cards
- MW-RL-005 Personal loan below minimum
- MW-RL-006 Personal loan above maximum
- MW-RL-007 Auto loan below minimum
- MW-RL-008 Auto loan above maximum
- MW-RL-009 Home loan below minimum
- MW-RL-010 Home loan above maximum
- MW-RL-011 Down payment >= loan
- MW-RL-014 No loan type selected
- MW-RL-015 No collateral account
- MW-RL-016 Exact minimum Personal ($1,000)
- MW-RL-017 Exact maximum Personal ($50,000)
- MW-RL-019 Non-numeric loan amount
- MW-RL-020 Down payment exactly one cent below 10%

### Update Contact Info (17 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-003 Update First Name
- MW-UCI-004 Update Last Name
- MW-UCI-005 Update Address
- MW-UCI-006 Update City
- MW-UCI-007 Update State
- MW-UCI-008 Update ZIP Code
- MW-UCI-009 Update Phone
- MW-UCI-011 Last Name empty
- MW-UCI-012 Address empty
- MW-UCI-013 City empty
- MW-UCI-014 State empty
- MW-UCI-015 ZIP Code empty
- MW-UCI-016 Phone empty
- MW-UCI-018 Invalid Phone format
- MW-UCI-019 Special characters in City
- MW-UCI-020 Non-US ZIP code format

### Manage Cards (9 missing)
- MW-MC-002 Request Credit card
- MW-MC-004 No account selected
- MW-MC-006 Add travel notice
- MW-MC-007 Freeze card
- MW-MC-008 Unfreeze card
- MW-MC-010 Travel notice end before start
- MW-MC-011 Limit exactly equal policy maximum
- MW-MC-012 Travel notice for same day
- MW-MC-013 Rapid status toggle

### Investments (9 missing)
- MW-INV-001 View portfolio snapshot
- MW-INV-003 Sell funds
- MW-INV-004 Fund symbol autocomplete
- MW-INV-006 Zero quantity
- MW-INV-008 Sell more than owned
- MW-INV-010 Create monthly plan
- MW-INV-013 Insufficient funding balance
- MW-INV-014 Start date exactly today
- MW-INV-015 Sell exact total shares owned

### Account Statements (8 missing)
- MW-AS-001 Generate monthly statement
- MW-AS-004 No account selected
- MW-AS-005 Generation failure
- MW-AS-007 Opt-out of paperless
- MW-AS-009 Empty email with opt-in
- MW-AS-010 Custom date range spanning years
- MW-AS-011 Opt-out clears email field
- MW-AS-012 Invalid characters in email

### Security Settings (7 missing)
- MW-SS-003 New password too short
- MW-SS-004 New password missing uppercase
- MW-SS-005 New password missing lowercase
- MW-SS-006 New password missing number
- MW-SS-007 New password missing special char
- MW-SS-009 New password matches current password
- MW-SS-010 Passwords match but differ by trailing space

### Support Center (9 missing)
- MW-SC-002 Send with attachment
- MW-SC-003 Empty subject
- MW-SC-006 Category dropdown
- MW-SC-008 Phone pre-filled
- MW-SC-009 Date too soon
- MW-SC-011 Email confirmation
- MW-SC-012 Callback preferred time overlapping cutoff
- MW-SC-013 Concurrent message submissions
- MW-SC-014 Extremely large attachment

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Accounts Overview (~2 extra types)
- Access accounts overview when not logged in
- Single account overview view

### Transfer Funds (~1 extra types)
- Transfer very large amount within system limits

### Request Loan (~1 extra types)
- Request loan with maximum allowable amount

### Update Contact Info (~1 extra types)
- Update with maximum length fields boundary test

### Manage Cards (~2 extra types)
- Request credit card with max address length
- Update controls with spending limit of zero

### Investments (~1 extra types)
- Trade execution with maximum allowable quantity

### Account Statements (~2 extra types)
- Generate statement for max date range boundary test
- Update e-statement with max length email boundary test

### Security Settings (~1 extra types)
- Weak password that meets length requirement

### Support Center (~2 extra types)
- Max allowed subject length
- Earliest possible date for callback
