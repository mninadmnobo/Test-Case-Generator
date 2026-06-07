# Test Coverage Report

**Ground Truth:** Parabank GT v1.1  
**Generated Suite:** openai/gpt-5-mini (Agent) — 230 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 200 |
| GT cases covered by GEN | 170 |
| GT cases not covered by GEN | 30 |
| **Overall coverage** | **85.0%** |
| GEN cases with no GT counterpart (extras) | ~25 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 11 | 3 | **78.6%** |
| Register | 25 | 23 | 2 | **92.0%** |
| Accounts Overview | 9 | 6 | 3 | **66.7%** |
| Open New Account | 14 | 12 | 2 | **85.7%** |
| Transfer Funds | 16 | 14 | 2 | **87.5%** |
| Payments | 17 | 13 | 4 | **76.5%** |
| Request Loan | 20 | 18 | 2 | **90.0%** |
| Update Contact Info | 20 | 17 | 3 | **85.0%** |
| Manage Cards | 13 | 10 | 3 | **76.9%** |
| Investments | 15 | 12 | 3 | **80.0%** |
| Account Statements | 12 | 9 | 3 | **75.0%** |
| Security Settings | 11 | 9 | 2 | **81.8%** |
| Support Center | 14 | 11 | 3 | **78.6%** |
| **Total** | **200** | **170** | **30** | **85.0%** |

---

## Missing Scenarios (Gaps)

### Login (3 missing)
- MW-LOGIN-002 Valid login with username
- MW-LOGIN-014 Login with extremely long email
- MW-LOGIN-015 SQL injection in email

### Register (2 missing)
- MW-REG-004 Phone auto-formatting
- MW-REG-026 Registration session timeout

### Accounts Overview (3 missing)
- MW-AO-001 Welcome message displayed
- MW-AO-008 Zero balance display
- MW-AO-009 Extreme negative balance

### Open New Account (2 missing)
- MW-ONA-014 Deposit with excessive precision
- MW-ONA-015 Duplicate account prevention

### Transfer Funds (2 missing)
- MW-TF-003 Source account filter
- MW-TF-016 External routing number boundaries

### Payments (4 missing)
- MW-BP-002 Quick select payee
- MW-BP-004 Payee Name empty
- MW-BP-005 Street Address empty
- MW-BP-017 XSS payload in Payee Name

### Request Loan (2 missing)
- MW-RL-004 Loan type cards
- MW-RL-014 No loan type selected

### Update Contact Info (3 missing)
- MW-UCI-001 Pre-populated form
- MW-UCI-019 Special characters in City
- MW-UCI-020 Non-US ZIP code format

### Manage Cards (3 missing)
- MW-MC-004 No account selected
- MW-MC-012 Travel notice for same day
- MW-MC-013 Rapid status toggle

### Investments (3 missing)
- MW-INV-001 View portfolio snapshot
- MW-INV-003 Sell funds
- MW-INV-010 Create monthly plan

### Account Statements (3 missing)
- MW-AS-002 Generate custom date range
- MW-AS-005 Generation failure
- MW-AS-010 Custom date range spanning years

### Security Settings (2 missing)
- MW-SS-009 New password matches current password
- MW-SS-010 Passwords match but differ by trailing space

### Support Center (3 missing)
- MW-SC-003 Empty subject
- MW-SC-012 Callback preferred time overlapping cutoff
- MW-SC-013 Concurrent message submissions

---

## Extra Scenarios

### Login (~2 extra types)
- Password validation edge cases slightly below minimum length
- Special character omissions

### Register (~3 extra types)
- Validation of leading/trailing whitespace trimming
- Browser back-button resubmission prevention
- Continuous digits formatting triggers

### Accounts Overview (~2 extra types)
- Identical Open_Date sorting stability
- Rapid consecutive clicking on account links

### Open New Account (~2 extra types)
- Exact sufficiency of funding source balance
- Excessive decimal precision handling

### Transfer Funds (~3 extra types)
- Highly precise decimal amounts logic
- Browser back-button duplicate prevention

### Payments (~2 extra types)
- Confirm account number mismatch explicit handling
- Payee name exceeding typical length limits

### Request Loan (~3 extra types)
- Exact threshold bounds for all loan types
- Collateral balance exactly equaling required margin

### Update Contact Info (~1 extra types)
- Refresh page without modifications check

### Manage Cards (~2 extra types)
- Shipping address whitespace trimming
- Invalid repeating-group updates

### Investments (~2 extra types)
- Start Date far in the future
- Search autocomplete whitespace handling

### Account Statements (~1 extra types)
- Toggle opt-in and off behavior

### Security Settings (~1 extra types)
- Idempotency checks on submit button

### Support Center (~1 extra types)
- Rich text validation for empty spaces
