# Test Coverage Report

**Ground Truth:** Parabank GT v1.1  
**Generated Suite:** openai/gpt-4o-mini — 180 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 142 |
| GT cases not covered by GEN | 58 |
| **Overall coverage** | **71.0%** |
| GEN cases with no GT counterpart (extras) | ~17 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 12 | 2 | **85.7%** |
| Register | 25 | 16 | 9 | **64.0%** |
| Accounts Overview | 9 | 2 | 7 | **22.2%** |
| Open New Account | 14 | 12 | 2 | **85.7%** |
| Transfer Funds | 16 | 10 | 6 | **62.5%** |
| Payments | 17 | 14 | 3 | **82.4%** |
| Request Loan | 20 | 17 | 3 | **85.0%** |
| Update Contact Info | 20 | 16 | 4 | **80.0%** |
| Manage Cards | 13 | 10 | 3 | **76.9%** |
| Investments | 15 | 9 | 6 | **60.0%** |
| Account Statements | 12 | 6 | 6 | **50.0%** |
| Security Settings | 11 | 8 | 3 | **72.7%** |
| Support Center | 14 | 10 | 4 | **71.4%** |
| **Total** | **200** | **142** | **58** | **71.0%** |

---

## Missing Scenarios (Gaps)

### Login (2 missing)
- MW-LOGIN-006 Unregistered email
- MW-LOGIN-015 SQL injection in email

### Register (9 missing)
- MW-REG-004 Phone auto-formatting
- MW-REG-005 SSN auto-formatting
- MW-REG-014 Phone Number empty
- MW-REG-016 SSN empty
- MW-REG-021 Confirm Password empty
- MW-REG-022 All fields empty
- MW-REG-024 Maximum length inputs
- MW-REG-025 Email with leading/trailing spaces
- MW-REG-026 Registration session timeout

### Accounts Overview (7 missing)
- MW-AO-001 Welcome message displayed
- MW-AO-004 Total balance calculation
- MW-AO-005 Accounts ordered by date
- MW-AO-006 Active status badge
- MW-AO-007 High volume of accounts
- MW-AO-008 Zero balance display
- MW-AO-009 Extreme negative balance

### Open New Account (2 missing)
- MW-ONA-014 Deposit with excessive precision
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (6 missing)
- MW-TF-003 Source account filter
- MW-TF-004 Transfer type toggle
- MW-TF-009 Same source and destination
- MW-TF-011 No source selected
- MW-TF-012 No destination selected
- MW-TF-013 Transfer exact balance

### Payments (3 missing)
- MW-BP-002 Quick select payee
- MW-BP-016 Payee name maximum length
- MW-BP-017 XSS payload in Payee Name

### Request Loan (3 missing)
- MW-RL-004 Loan type cards
- MW-RL-014 No loan type selected
- MW-RL-015 No collateral account

### Update Contact Info (4 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-017 Invalid ZIP format
- MW-UCI-019 Special characters in City
- MW-UCI-020 Non-US ZIP code format

### Manage Cards (3 missing)
- MW-MC-011 Spending limit exactly at policy maximum
- MW-MC-012 Travel notice for same day
- MW-MC-013 Rapid status toggle

### Investments (6 missing)
- MW-INV-001 View portfolio snapshot
- MW-INV-003 Sell funds
- MW-INV-004 Fund symbol autocomplete
- MW-INV-008 Sell more than owned
- MW-INV-010 Create monthly plan
- MW-INV-015 Sell exact total shares owned

### Account Statements (6 missing)
- MW-AS-002 Generate custom date range
- MW-AS-004 No account selected
- MW-AS-005 Generation failure
- MW-AS-007 Opt-out of paperless
- MW-AS-010 Custom date range spanning years
- MW-AS-011 Opt-out clears email field

### Security Settings (3 missing)
- MW-SS-009 New password matches current password
- MW-SS-010 Passwords match but differ by trailing space
- MW-SS-011 Extreme length password

### Support Center (4 missing)
- MW-SC-003 Empty subject
- MW-SC-012 Callback preferred time overlapping cutoff
- MW-SC-013 Concurrent message submissions
- MW-SC-014 Extremely large attachment

---

## Extra Scenarios

### Login (~2 extra types)
- Password length edge case boundaries
- Special characters and whitespace handling in fields

### Register (~2 extra types)
- Validation of leading/trailing whitespace trimming
- Testing username input with special characters

### Accounts Overview (~1 extra types)
- Attempting unimplemented actions (e.g., clicking unlinked account numbers)

### Open New Account (~1 extra types)
- Depositing non-numeric values explicitly

### Transfer Funds (~2 extra types)
- Exceeding max allowed entries for external accounts
- Input boundaries for repeating external account groups

### Payments (~1 extra types)
- Payment Amount at minimum allowed value edge cases

### Request Loan (~1 extra types)
- Submitting extremely long text or special characters in the loan amount field

### Update Contact Info (~2 extra types)
- Submitting maximum length strings
- Extra validation of whitespace trimming in names

### Manage Cards (~1 extra types)
- Requesting a card with an incomplete shipping address

### Investments (~1 extra types)
- Testing excessively long fund symbols

### Account Statements (~1 extra types)
- Validating long email lengths during paperless opt-in

### Security Settings (~1 extra types)
- Providing incorrect current password handling edge cases

### Support Center (~1 extra types)
- Subject length at exactly the minimum boundary value
