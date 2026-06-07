# Test Coverage Report

**Ground Truth:** Mifos Banking System GT v2.0  
**Generated Suite:** openai/gpt-4o-mini — 497 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording. Implied and partial coverage is accepted; specific boundary/edge conditions require explicit assertion to qualify.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 607 |
| GT cases covered by GEN | 396 |
| GT cases not covered by GEN | 211 |
| **Overall coverage** | **65.2%** |
| GEN cases with no GT counterpart (extras) | ~72 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 17 | 9 | 8 | **53%** |
| Home | 5 | 3 | 2 | **60%** |
| Dashboard | 13 | 7 | 6 | **54%** |
| Global Search | 11 | 7 | 4 | **64%** |
| Client Management | 29 | 22 | 7 | **76%** |
| Group Management | 18 | 15 | 3 | **83%** |
| Center Management | 18 | 14 | 4 | **78%** |
| Loan Products | 14 | 12 | 2 | **86%** |
| Savings Products | 15 | 10 | 5 | **67%** |
| Charges | 16 | 9 | 7 | **56%** |
| Loan Account | 29 | 22 | 7 | **76%** |
| Savings Account | 22 | 16 | 6 | **73%** |
| Accounting — Chart of Accounts | 11 | 7 | 4 | **64%** |
| Accounting — Journal Entries | 11 | 8 | 3 | **73%** |
| Users & Roles | 18 | 12 | 6 | **67%** |
| Offices | 11 | 8 | 3 | **73%** |
| Employees | 7 | 6 | 1 | **86%** |
| Reports | 10 | 5 | 5 | **50%** |
| Organization Settings | 15 | 11 | 4 | **73%** |
| Share Products | 12 | 10 | 2 | **83%** |
| Floating Rates | 11 | 9 | 2 | **82%** |
| Delinquency Management | 10 | 8 | 2 | **80%** |
| Share Account | 15 | 12 | 3 | **80%** |
| Fixed & Recurring Deposit Accounts | 20 | 16 | 4 | **80%** |
| Accounting — Closures | 8 | 6 | 2 | **75%** |
| Accounting Rules & Financial Activity Mappings | 9 | 7 | 2 | **78%** |
| Provisioning | 9 | 7 | 2 | **78%** |
| Teller & Cashier Management | 16 | 13 | 3 | **81%** |
| Account Transfers & Standing Instructions | 14 | 11 | 3 | **79%** |
| Tax Management | 11 | 10 | 1 | **91%** |
| System Administration | 18 | 10 | 8 | **56%** |
| Logout | 7 | 5 | 2 | **71%** |
| **Total** | **607** | **396** | **211** | **65.2%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (8 missing)
- MF-LOGIN-010 SQL injection payload in Username field
- MF-LOGIN-011 Massive password string (10,000 chars)
- MF-LOGIN-012 Rapid double click on Login button
- MF-LOGIN-013 Null byte injection
- MF-LOGIN-014 Cross-site scripting (XSS) in Tenant field
- MF-LOGIN-015 Emoji in username
- MF-LOGIN-020 Session persists on page refresh after successful login
- MF-LOGIN-022 Logout invalidates session token for subsequent protected requests

### Home (2 missing)
- MF-HOME-003 Top toolbar is visible on Home page
- MF-HOME-005 Home page route is accessible directly after authentication

### Dashboard (6 missing)
- MF-DASH-008 Dashboard — massive negative integer rendering
- MF-DASH-009 Dashboard — overlapping widgets test
- MF-DASH-011 Dashboard — deep link bypassing dashboard
- MF-DASH-012 Dashboard — session timeout exact boundary
- MF-DASH-013 Dashboard — unicode character rendering
- MF-DASH-006 Dashboard refresh after transaction reflects latest data

### Global Search (4 missing)
- MF-SEARCH-011 SQL injection in search bar
- MF-SEARCH-012 Exact 255 character search string
- MF-SEARCH-013 Rapid repeated searches (debounce)
- MF-SEARCH-014 Search using emoji

### Client Management (7 missing)
- MF-CLIENT-024 HTML injection in First Name
- MF-CLIENT-025 Date of Birth in year 1800
- MF-CLIENT-026 Exact 256 char Last Name
- MF-CLIENT-027 Concurrent activation (two tabs)
- MF-CLIENT-028 Duplicate External ID (negative — server-side uniqueness)
- MF-CLIENT-029 Zero length file upload
- MF-CLIENT-011 Pagination on clients list

### Group Management (3 missing)
- MF-GROUP-014 1000 members in one group stress test
- MF-GROUP-016 Adding deceased client to group
- MF-GROUP-017 Concurrent group activation

### Center Management (4 missing)
- MF-CENTER-015 Center name with special Unicode characters
- MF-CENTER-016 Extreme pagination on center list
- MF-CENTER-017 Empty center meetings submission
- MF-CENTER-018 Duplicate external ID center

### Loan Products (2 missing)
- MF-LPROD-021 Exactly 0 decimal places validation
- MF-LPROD-020 Interest rate above 100%

### Savings Products (5 missing)
- MF-SPROD-009 Create zero-interest savings product
- MF-SPROD-016 Overdraft limit negative value
- MF-SPROD-017 Interest rate with 10 decimal places precision
- MF-SPROD-018 Minimum balance greater than maximum balance
- MF-SPROD-021 Extreme maximum withdrawal fee boundary

### Charges (7 missing)
- MF-CHARGE-006 Create savings withdrawal charge
- MF-CHARGE-007 Create client-level charge
- MF-CHARGE-008 View charge details
- MF-CHARGE-014 Inactivate charge definition
- MF-CHARGE-015 Charge linked to product appears during account lifecycle
- MF-CHARGE-016 Charge collected from account updates accounting and balance
- MF-CHARGE-017 Waive charge from applicable account

### Loan Account (7 missing)
- MF-LOAN-022 Repayment exactly 0.01
- MF-LOAN-023 Overpayment exactly 0.01 over balance
- MF-LOAN-024 Negative repayment amount
- MF-LOAN-025 Disburse on future date validation
- MF-LOAN-026 Rapid double click approve
- MF-LOAN-027 Write-off with zero balance
- MF-LOAN-030 Loan guarantor or collateral tab accessible

### Savings Account (6 missing)
- MF-SAV-007 Post interest to savings account
- MF-SAV-010 Reactivate or reopen eligible savings account
- MF-SAV-020 Rapid double click withdraw
- MF-SAV-021 Deposit negative amount
- MF-SAV-022 Activate on future date validation
- MF-SAV-022 Interest recalculation after backdated transaction

### Accounting — Chart of Accounts (4 missing)
- MF-COA-005 Disable or close GL account
- MF-COA-013 HTML tags in description
- MF-COA-014 Cyclical parent-child mapping
- MF-COA-015 Delete GL account in use

### Accounting — Journal Entries (3 missing)
- MF-JRN-012 10,000 line items (stress test)
- MF-JRN-014 Negative debit amount
- MF-JRN-015 Duplicate transaction reference

### Users & Roles (6 missing)
- MF-USER-018 Disable own currently logged-in user account
- MF-USER-020 Rapid password change loop
- MF-USER-021 Username matches SQL reserved word
- MF-USER-022 Space-only first name validation
- MF-USER-023 HTML in last name (XSS)
- MF-USER-024 Assign to deleted office

### Offices (3 missing)
- MF-OFFICE-010 Open in future date validation
- MF-OFFICE-013 Delete root office
- MF-OFFICE-015 100+ deep hierarchy stress test

### Employees (1 missing)
- MF-EMP-009 Duplicate mobile number validation

### Reports (5 missing)
- MF-REPORT-003 Run report without parameters when not required
- MF-REPORT-004 Export report to file
- MF-REPORT-008 50 year date range timeout handling
- MF-REPORT-010 Scheduled or background report visibility
- MF-REPORT-011 Report output reflects latest committed transactions

### Organization Settings (4 missing)
- MF-ORG-004 Configure currency settings
- MF-ORG-016 Overlapping working days validation
- MF-ORG-017 Set maker-checker false then bypass
- MF-ORG-015 Holiday affects repayment or transaction scheduling rules

### Share Products (2 missing)
- MF-SHPROD-011 Nominal price 6 decimal places precision
- MF-SHPROD-013 Negative total shares validation

### Floating Rates (2 missing)
- MF-FRATE-010 Exactly 0% floating rate boundary
- MF-FRATE-014 Rapid double click add rate

### Delinquency Management (2 missing)
- MF-DELINQ-009 Delinquency categorization updates after repayment
- MF-DELINQ-010 Write-off removes loan from active delinquency population

### Share Account (3 missing)
- MF-SHARE-016 Redeem before lock-in period ends
- MF-SHARE-017 Rapid double click approve
- MF-SHARE-014 Share balance and nominal/market value display updates after transactions

### Fixed & Recurring Deposit Accounts (4 missing)
- MF-DEP-017 Deposit term of 100 years (limit error)
- MF-DEP-019 Negative deposit amount
- MF-DEP-020 Withdrawal before maturity blocked
- MF-DEP-021 Rapid double click close

### Accounting — Closures (2 missing)
- MF-CLOSE-009 Reversing closure with subsequent transactions blocked
- MF-CLOSE-010 Closure notes exceeding 2000 characters

### Accounting Rules & Financial Activity Mappings (2 missing)
- MF-FAM-007 Rule mapping debit to income (invalid schema)
- MF-FAM-008 Cyclical rule mapping (A→B→A)

### Provisioning (2 missing)
- MF-PROV-010 Run provisioning twice in a day (idempotency)
- MF-PROV-011 Invalid asset class code

### Teller & Cashier Management (3 missing)
- MF-TELLER-014 Allocating overlapping cashier dates
- MF-TELLER-016 Delete active teller blocked
- MF-TELLER-017 Extreme length teller name

### Account Transfers & Standing Instructions (3 missing)
- MF-TRF-014 Standing instruction to same account validation
- MF-TRF-015 Standing instruction on past date validation
- MF-TRF-016 Rapid double click transfer (idempotency)

### Tax Management (1 missing)
- MF-TAX-011 Overlapping components in group (duplicate date ranges)

### System Administration (8 missing)
- MF-SYS-004 Manage hooks/webhooks configuration
- MF-SYS-007 Manage password preferences or security settings
- MF-SYS-009 Manage maker-checker settings
- MF-SYS-012 Save invalid hook endpoint configuration
- MF-SYS-014 Set invalid password policy values
- MF-SYS-015 Hook URL XSS payload
- MF-SYS-016 Maker-checker workflow holds pending action until checker approval
- MF-SYS-019 Hook invocation occurs on configured business event

### Logout (2 missing)
- MF-LOGOUT-007 Back button after logout to submit cached form (CSRF)
- MF-LOGOUT-008 Opening new tab after logout redirects to login

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~1 extra type)
- Leading/trailing whitespace trimming in username/password fields

### Home Page (~2 extra types)
- Rapid re-submission after redirect to dashboard (back button behaviour)
- Long text and special character input in Search Activity field on Home page

### Dashboard (~4 extra types)
- Individual no-data states tested per widget card (Amount Pending Disbursed, Amount Collected, Client Trends Chart) as separate negative cases rather than one combined scenario
- Search Activity field usage as a standalone workflow separate from dashboard navigation

### Global Search (~2 extra types)
- Unauthenticated access attempt to search input field
- Leading and trailing whitespace trimming in search input

### Client Management (~4 extra types)
- Bulk import via file upload (size limit at/above boundary, file picker validation)
- Reactivation of closed client as a distinct positive workflow
- Transfer to same office treated as a distinct negative scenario with explicit error assertion
- Whitespace trimming in External ID field

### Group Management (~4 extra types)
- Bulk import for groups via file upload (size limit boundary tests)
- Submitted On field blank as a distinct negative scenario separate from other required-field tests
- Empty required fields combination boundary test

### Center Management (~3 extra types)
- Bulk import for centers (file upload valid/exceeding size limit)
- Rapid state transition from Active to Activate and Active to Close as state-edge tests

### Loan Products (~3 extra types)
- Multi-step wizard progression modelled as separate positive test per step (Steps 1–6 as individual cases)
- Negative values for Grace Period and Arrears Tolerance as distinct negative cases

### Savings Products (~3 extra types)
- Fixed Deposit product creation and Recurring Deposit product creation treated as separate creation workflows under the savings products module
- Rapid re-submission after successful product creation (browser back button)

### Share Products (~5 extra types)
- Detailed field-by-field required validation tests (Total Shares, Nominal Price, Min Shares, Nominal Shares, Minimum Active Period, Lock-in, From Date, Share Value) as separate negative cases
- Rapid wizard step navigation as an interaction edge test

### Charges (~1 extra type)
- Delete charge from table as a distinct workflow

### Floating Rates (~2 extra types)
- Editing without sufficient permissions tested as a distinct negative
- Invalid non-numeric Interest Rate field as a separate negative

### Delinquency Management (~1 extra type)
- View classification/bucket details while unauthenticated as separate negative cases

### Share Account (~2 extra types)
- Undo approval workflow as a distinct positive test
- Rapid double-approval as a state-edge test

### Fixed & Recurring Deposit Accounts (~3 extra types)
- Draft state activation of RD account and "Close on Maturity" from Active state each tested as both positive and negative (state contradiction)
- Very large deposit amount boundary tests for both FD and RD

### Accounting — Journal Entries & Closures (~3 extra types)
- Combined module (Journal Entries + Closures in one GEN module) introduces extra closure field-blank scenarios not in the separate GT closure module
- Closure on same date as journal entry and closure before existing journal entries as boundary cases

### Accounting Rules & Financial Activity Mappings (~2 extra types)
- Duplicate Financial Activity mapping (same activity mapped twice) as a boundary negative
- Delete accounting rule as a distinct positive workflow

### Provisioning (~3 extra types)
- Review and Recreate provisioning entry as distinct positive workflows
- Maximum definitions boundary (exactly 2 rows) and overflow (3rd row blocked) tests

### Teller & Cashier Management (~4 extra types)
- Settle cash with Amount at zero boundary test
- Settle cash with Amount above maximum boundary test
- Allocate cashier with Start Date equal to End Date
- Access Create Teller form without authentication

### Account Transfers & Standing Instructions (~5 extra types)
- Standing instruction form validated field by field (Name, Transfer Type, Priority, Recurrence Frequency, Recurrence Interval) as individual negative tests
- Transfer on future date and on today's date as separate data-edge tests
- Long description input in transfer form

### Tax Management (~2 extra types)
- Debit/Credit Account Type and Account fields modelled during tax component creation (more detailed than GT)
- End Date in tax group component modelled as a distinct field

### Organization Settings (~3 extra types)
- Fund creation workflow (form open + submit) as distinct positive cases
- Payment type creation modelled as a separate workflow
- Bulk import download template and upload data as separate positive cases

### Reports (~3 extra types)
- Long text and special character inputs in report parameter fields as input edge tests
- Leading/trailing whitespace in all parameter fields as a batch edge test

### System Administration (~2 extra types)
- Maximum allowed column definition entries and one-above-maximum as boundary cases for data table creation
- Leading/trailing whitespace trimming in Data Table Name

### Logout (~1 extra type)
- Unauthenticated user attempting to click logout (no session to terminate)