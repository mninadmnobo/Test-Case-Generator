# Test Coverage Report

**Ground Truth:** ParaBank Test Cases v1.1
**Generated Suite:** gpt-4o-mini (zero_shot_per_module) — 92 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same, similar, or an implied observable behaviour.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 94 |
| GT cases not covered by GEN | 106 |
| **Overall coverage** | **47.0%** |
| GEN cases with no GT counterpart (extras) | ~18 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 12 | 2 | **85.7%** |
| Register | 25 | 8 | 17 | **32.0%** |
| Accounts Overview | 9 | 6 | 3 | **66.7%** |
| Open New Account | 14 | 6 | 8 | **42.9%** |
| Transfer Funds | 16 | 6 | 10 | **37.5%** |
| Payments | 17 | 13 | 4 | **76.5%** |
| Request Loan | 20 | 7 | 13 | **35.0%** |
| Update Contact Info | 20 | 9 | 11 | **45.0%** |
| Manage Cards | 13 | 6 | 7 | **46.2%** |
| Investments | 15 | 7 | 8 | **46.7%** |
| Account Statements | 12 | 5 | 7 | **41.7%** |
| Security Settings | 11 | 4 | 7 | **36.4%** |
| Support Center | 14 | 5 | 9 | **35.7%** |
| **Total** | **200** | **94** | **106** | **47.0%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (2 missing)
- MW-LOGIN-002 Valid login with username
- MW-LOGIN-015 SQL injection in email

### Register (17 missing)
- MW-REG-003 State dropdown
- MW-REG-004 Phone auto-formatting
- MW-REG-005 SSN auto-formatting
- MW-REG-006 First Name empty
- MW-REG-007 Last Name empty
- MW-REG-008 Street Address empty
- MW-REG-009 City empty
- MW-REG-010 State not selected
- MW-REG-011 ZIP Code empty
- MW-REG-013 Valid 5+4 ZIP
- MW-REG-014 Phone Number empty
- MW-REG-016 SSN empty
- MW-REG-019 Password less than 8 chars
- MW-REG-021 Confirm Password empty
- MW-REG-023 Minimum valid inputs
- MW-REG-025 Email with leading/trailing spaces
- MW-REG-026 Registration session timeout

### Accounts Overview (3 missing)
- MW-AO-005 Accounts ordered by date
- MW-AO-008 Zero balance display
- MW-AO-009 Extreme negative balance

### Open New Account (8 missing)
- MW-ONA-004 Real-time validation
- MW-ONA-009 Insufficient funding balance
- MW-ONA-010 No funding account selected
- MW-ONA-011 Exact minimum Checking ($25)
- MW-ONA-012 Exact minimum Savings ($100)
- MW-ONA-013 Just below minimum
- MW-ONA-014 Deposit with excessive precision
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (10 missing)
- MW-TF-003 Source account filter
- MW-TF-004 Transfer type toggle
- MW-TF-007 Negative amount
- MW-TF-009 Same source and destination
- MW-TF-011 No source selected
- MW-TF-012 No destination selected
- MW-TF-013 Transfer exact balance
- MW-TF-014 Minimum transfer ($0.01)
- MW-TF-015 Transfer amount just above balance
- MW-TF-016 External routing number boundaries

### Payments (4 missing)
- MW-BP-002 Quick select payee
- MW-BP-003 Balance updated
- MW-BP-015 No source account
- MW-BP-017 XSS payload in Payee Name

### Request Loan (13 missing)
- MW-RL-002 Auto loan approved
- MW-RL-004 Loan type cards
- MW-RL-005 Personal loan below minimum
- MW-RL-006 Personal loan above maximum
- MW-RL-008 Auto loan above maximum
- MW-RL-009 Home loan below minimum
- MW-RL-011 Down payment >= loan
- MW-RL-013 Down payment < 10%
- MW-RL-014 No loan type selected
- MW-RL-015 No collateral account
- MW-RL-017 Exact maximum Personal ($50,000)
- MW-RL-019 Non-numeric loan amount
- MW-RL-020 Down payment exactly one cent below 10%

### Update Contact Info (11 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-003 Update First Name
- MW-UCI-004 Update Last Name
- MW-UCI-005 Update Address
- MW-UCI-006 Update City
- MW-UCI-007 Update State
- MW-UCI-008 Update ZIP Code
- MW-UCI-009 Update Phone
- MW-UCI-018 Invalid Phone format
- MW-UCI-019 Special characters in City
- MW-UCI-020 Non-US ZIP code format

### Manage Cards (7 missing)
- MW-MC-002 Request Credit card
- MW-MC-004 No account selected
- MW-MC-006 Add travel notice
- MW-MC-007 Freeze card
- MW-MC-008 Unfreeze card
- MW-MC-012 Travel notice for same day
- MW-MC-013 Rapid status toggle

### Investments (8 missing)
- MW-INV-001 View portfolio snapshot
- MW-INV-003 Sell funds
- MW-INV-004 Fund symbol autocomplete
- MW-INV-008 Sell more than owned
- MW-INV-010 Create monthly plan
- MW-INV-013 Insufficient funding balance
- MW-INV-014 Start date exactly today
- MW-INV-015 Sell exact total shares owned

### Account Statements (7 missing)
- MW-AS-001 Generate monthly statement
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

### Accounts Overview (~1 extra types)
- Display empty accounts state for users with no accounts

### Open New Account (~2 extra types)
- Maximum deposit amount boundary test
- Zero deposit amount boundary test

### Transfer Funds (~1 extra types)
- Maximum length account number boundary test

### Payments (~1 extra types)
- Exact available balance edge case

### Request Loan (~2 extra types)
- Down payment greater than loan amount negative test
- Empty loan amount field boundary test

### Update Contact Info (~1 extra types)
- Maximum length fields boundary test

### Manage Cards (~3 extra types)
- Invalid account status on card request
- Maximum length address boundary test
- Maximum spending limit boundary test

### Investments (~1 extra types)
- Maximum quantity trade execution boundary test

### Account Statements (~2 extra types)
- Maximum date range boundary test
- Maximum length email boundary test

### Security Settings (~2 extra types)
- Empty fields submission
- Strong password containing special characters boundary test

### Support Center (~2 extra types)
- Maximum subject length boundary test
- Earliest possible date callback boundary test
