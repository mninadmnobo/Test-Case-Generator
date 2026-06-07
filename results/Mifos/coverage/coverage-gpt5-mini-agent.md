# Test Coverage Report

**Ground Truth:** Mifos Banking System GT v2.0 (Revised)
**Generated Suite:** openai/gpt-5-mini — 807 cases
**Analysis Date:** 2026-06-07
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour or a closely implied edge case, regardless of fixture names, test structure, or implementation wording. Partial UI element coverage and implied coverage of basic functionality via edge-case tests both qualify. Specific boundary conditions (e.g. special characters, exact field violations) must be explicitly present to count.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 607 |
| GT cases covered by GEN | 487 |
| GT cases not covered by GEN | 120 |
| **Overall coverage** | **80.2%** |
| GEN cases with no GT counterpart (extras) | ~200 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 9 | 3 | **75%** |
| Home | 5 | 5 | 0 | **100%** |
| Dashboard | 5 | 4 | 1 | **80%** |
| Global Search | 11 | 10 | 1 | **91%** |
| Client Management | 29 | 26 | 3 | **90%** |
| Group Management | 18 | 17 | 1 | **94%** |
| Center Management | 18 | 16 | 2 | **89%** |
| Loan Products | 14 | 12 | 2 | **86%** |
| Savings Products | 15 | 13 | 2 | **87%** |
| Charges | 16 | 13 | 3 | **81%** |
| Loan Account | 29 | 21 | 8 | **72%** |
| Savings Account | 22 | 20 | 2 | **91%** |
| Accounting – Chart of Accounts | 11 | 9 | 2 | **82%** |
| Accounting – Journal Entries | 11 | 10 | 1 | **91%** |
| Users & Roles | 18 | 13 | 5 | **72%** |
| Offices | 11 | 8 | 3 | **73%** |
| Employees | 7 | 4 | 3 | **57%** |
| Reports | 10 | 9 | 1 | **90%** |
| Organization Settings | 15 | 11 | 4 | **73%** |
| Share Products | 12 | 9 | 3 | **75%** |
| Floating Rates | 11 | 8 | 3 | **73%** |
| Delinquency Management | 10 | 7 | 3 | **70%** |
| Share Account | 15 | 14 | 1 | **93%** |
| Fixed & Recurring Deposit Accounts | 20 | 19 | 1 | **95%** |
| Accounting – Closures | 8 | 7 | 1 | **88%** |
| Accounting Rules & Financial Activity Mappings | 9 | 7 | 2 | **78%** |
| Provisioning | 9 | 6 | 3 | **67%** |
| Teller & Cashier Management | 16 | 14 | 2 | **88%** |
| Account Transfers & Standing Instructions | 14 | 10 | 4 | **71%** |
| Tax Management | 11 | 7 | 4 | **64%** |
| System Administration | 18 | 15 | 3 | **83%** |
| Logout | 7 | 6 | 1 | **86%** |
| **Total** | **607** | **487** | **120** | **80.2%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (3 missing)
- MF-LOGIN-010 SQL injection payload in Username field
- MF-LOGIN-013 Null byte injection in username
- MF-LOGIN-017 Direct access to login page after authenticated session preserves session or redirects

### Dashboard (1 missing)
- MF-DASH-012 Dashboard session timeout exact boundary redirect

### Global Search (1 missing)
- MF-SEARCH-018 Search results update correctly across entity types for same shared term without duplication

### Client Management (3 missing)
- MF-CLIENT-011 Pagination controls on clients list
- MF-CLIENT-027 Concurrent activation from two tabs is idempotent
- MF-CLIENT-028 Client charges tab supports add charge action through full collection workflow

### Group Management (1 missing)
- MF-GROUP-018 Group notes can be added and displayed chronologically

### Center Management (2 missing)
- MF-CENTER-014 Adding the same group to a center twice rapidly is caught by uniqueness constraint
- MF-CENTER-018 Add center notes

### Loan Products (2 missing)
- MF-LPROD-020 Interest rate above 100% produces warning or business rule response
- MF-LPROD-022 Term length of 100 years (1200 months) is accepted or produces a limit error

### Savings Products (2 missing)
- MF-SPROD-009 Create zero-interest savings product saves successfully with non-interest-bearing behavior
- MF-SPROD-019 Setting zero interest rate is accepted without error

### Charges (3 missing)
- MF-CHARGE-014 Inactivating a charge definition leaves historical usage intact
- MF-CHARGE-015 Charge linked to a product appears correctly during account lifecycle events
- MF-CHARGE-016 Collected charge updates accounting and account balance correctly

### Loan Account (8 missing)
- MF-LOAN-006 Undo repayment or reverse transaction where supported
- MF-LOAN-010 Reschedule loan where supported
- MF-LOAN-011 Multi-disbursement loan additional tranche disbursement
- MF-LOAN-025 Apply payment allocation rules correctly for mixed due amounts
- MF-LOAN-026 Post penalty on overdue installment
- MF-LOAN-027 Loan schedule recalculates after transaction reversal
- MF-LOAN-029 Loan notes and documents can be added
- MF-LOAN-030 Loan guarantor or collateral tab accessible where feature is enabled

### Savings Account (2 missing)
- MF-SAV-021 Savings notes and documents can be maintained
- MF-SAV-022 Interest recalculation after backdated transaction is handled correctly

### Accounting – Chart of Accounts (2 missing)
- MF-COA-014 Cyclical parent-child account mapping is blocked with a validation error
- MF-COA-016 Negative initial balance on GL account is rejected

### Accounting – Journal Entries (1 missing)
- MF-JRN-010 Journal entry detail drill-down shows entry lines and metadata accurately

### Users & Roles (5 missing)
- MF-USER-006 Remove role from user
- MF-USER-007 Disable user removes authentication access
- MF-USER-008 Re-enable disabled user restores active status
- MF-USER-019 Password reset for existing user invalidates old password
- MF-USER-021 Maker-checker permissions enforced correctly through assigned roles

### Offices (3 missing)
- MF-OFFICE-004 View parent-child office hierarchy displayed correctly
- MF-OFFICE-010 Transfer dependent entities before office closure succeeds
- MF-OFFICE-011 Search or filter offices list by name

### Employees (3 missing)
- MF-EMP-003 Edit employee details and save successfully
- MF-EMP-004 View employee profile showing linked office and personal details
- MF-EMP-007 Deactivate employee blocks assignment to new clients or groups

### Reports (1 missing)
- MF-RPT-010 Schedule or bookmark a report where the feature is supported

### Organization Settings (4 missing)
- MF-ORG-008 Configure working days or non-working day rules
- MF-ORG-009 Holiday configuration correctly reschedules affected loan installments
- MF-ORG-013 Bulk import of offices via template upload
- MF-ORG-015 View and manage standing instructions or recurring payment configurations

### Share Products (3 missing)
- MF-SPROD-009 Inactivate or delete a share product
- MF-SPROD-011 Dividend posting to eligible share accounts
- MF-SPROD-012 Share product market price history is tracked and displayed

### Floating Rates (3 missing)
- MF-FRATE-009 Loan product linked to floating rate resolves the latest applicable period correctly
- MF-FRATE-010 Future-dated floating rate period does not affect current calculations before effective date
- MF-FRATE-011 Floating rate history is immutable for already effective periods where restricted

### Delinquency Management (3 missing)
- MF-DELINQ-005 Configure delinquency classification linked to loan product where supported
- MF-DELINQ-009 Delinquency bucket updates after a repayment that reduces overdue days
- MF-DELINQ-010 Write-off or closure removes loan from active delinquency population

### Share Account (1 missing)
- MF-SHARE-007 Post dividend to eligible share account and verify transaction is recorded correctly

### Fixed & Recurring Deposit Accounts (1 missing)
- MF-FD-020 Interest rate chart resolution applies the correct band for the account's deposit term

### Accounting – Closures (1 missing)
- MF-CLOSE-007 Closure for one office does not block journal entries for a different office

### Accounting Rules & Financial Activity Mappings (2 missing)
- MF-ACCRULE-007 Deleting a financial activity mapping removes it from automated posting without error
- MF-ACCRULE-009 Accounting rule applied to a transaction correctly routes debit and credit entries

### Provisioning (3 missing)
- MF-PROV-004 Provisioning criteria linked to loan product categorizes eligible loans during provisioning run
- MF-PROV-007 Provisioning journal entries are posted correctly after a run
- MF-PROV-009 Re-running provisioning updates entries without duplicating existing records

### Teller & Cashier Management (2 missing)
- MF-TELLER-011 Settle cash transaction updates cashier running balance correctly
- MF-TELLER-016 Cashier settlement report or summary is accessible and accurate

### Account Transfers & Standing Instructions (4 missing)
- MF-TRANSFER-006 Standing instruction executes automatically on the configured recurring schedule
- MF-TRANSFER-009 Failed standing instruction is logged with a visible failure reason
- MF-TRANSFER-013 Account transfer between savings accounts posts correctly to both accounts
- MF-TRANSFER-014 Edit or cancel a standing instruction successfully updates or removes the instruction

### Tax Management (4 missing)
- MF-TAX-004 Tax component linked to a savings product applies withholding correctly on interest posting
- MF-TAX-008 Tax group containing multiple components posts composite withholding entries
- MF-TAX-009 Deactivating a tax component prevents its future use in new configurations
- MF-TAX-011 Tax amounts in accounting entries reconcile with configured rates and transaction values

### System Administration (3 missing)
- MF-SYS-009 Configure maker-checker settings and verify pending action is held until checker approval
- MF-SYS-017 Checker approval completes a pending maker action
- MF-SYS-018 Checker rejection cancels a pending maker action without executing the operation

### Logout (1 missing)
- MF-LOGOUT-006 Logout clears user-specific UI state so a subsequent login as a different user sees a clean state

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~2 extra types)
- Whitespace trimming behavior on username blur (leading/trailing space handling)
- Post-login back-navigation clears credential fields and disables login button

### Home Page (~4 extra types)
- Search Activity field in Home page — long string, special characters, and whitespace trim behavior
- Rapid double-click on Dashboard button treated as single navigation

### Dashboard (~3 extra types)
- Client Trends chart series and legend verification per selected office
- Rapid office switching between data-present and no-data states verifying "No Data" indicator
- Search Activity field on Dashboard page input acceptance tests

### Global Search (~2 extra types)
- Race condition: select a result while dropdown is still updating from rapid character entry
- Result group display showing entity name, identifier, and status for each entity type

### Client Management (~10 extra types)
- Bulk Import page navigation, template download, file upload, and import history download
- Address details step in Create Client wizard and persistence to client detail page
- Family members addition in wizard with subsequent detail page verification
- Duplicate identifier prevention within the wizard before server round-trip
- Rapid back-then-resubmit duplicate prevention for client creation
- State violation checks — Reactivate unavailable for Pending, Activate unavailable for Active/Closed, no actions for Rejected/Withdrawn

### Group Management (~10 extra types)
- Bulk import template download and file upload with import history entry
- Transfer clients between groups from different group lifecycle states (Pending, Active, Closed)
- Schedule and record group meetings from Calendar/Meeting tab
- Collection sheet generation and numeric field validation in the sheet
- Rapid consecutive state transitions: Activate then immediately Close
- Back-button duplicate prevention on group creation

### Center Management (~7 extra types)
- Bulk import template download and upload for centers
- Collection sheet — entering amounts and non-numeric validation
- Submitted_On boundary tests: today, yesterday, one day in the future
- Add-then-remove-all Groups before submit (zero-group-member boundary)
- Rapid re-submission after successful create prevents duplicates

### Loan Products (~6 extra types)
- Step-by-step wizard field persistence verification (Currency, Settings, Terms, Charges, Accounting steps individually confirmed on detail page)
- Visible_when toggle for GL account dropdowns when switching Accounting Method between None and non-None
- Add then remove charge in wizard and submit with zero charges

### Savings Products (~7 extra types)
- Conditional field reveal tests: Enforce Minimum Required Balance, Overdraft, Enable Withhold Tax, Enable Dormancy Tracking
- Accounting step GL field reveal when Cash-based selected
- Non-integer Decimal Places validation
- Jump-to-step-without-completing-required-fields is blocked

### Share Products (~5 extra types)
- Delete share product from table row action and from detail view
- Edit product from table row action
- Filter products table by search term

### Charges (~5 extra types)
- Charge wizard with conditional field visibility (percentage-based charge flow)
- Charge search-and-add within loan/savings product wizard Charges step
- Add-then-remove charge before wizard submit results in zero charges on product

### Loan Account (~10 extra types)
- Comprehensive state violation guards (wrong-state actions not available per lifecycle state)
- Repayment allocation with payment type selection
- Backdated transaction date validation against closure dates
- Entry-line count boundary in journal context
- Loan detail tab navigation verification

### Savings Account (~8 extra types)
- Minimum-balance enforcement boundary tests: withdraw to exactly minimum, withdraw one unit below minimum blocked
- Overdraft-enabled account allows withdrawal one unit above available balance
- Rapid consecutive Approve then Activate state transitions
- Add-then-remove charges on create form still allows submit

### Share Account (~8 extra types)
- Requested Shares boundary: minimum, one below minimum, maximum, one above maximum
- Fractional share quantity rejected
- External ID whitespace trimming on save
- Rapid Approve-then-Activate concurrency edge

### Fixed & Recurring Deposit Accounts (~7 extra types)
- Deposit Amount zero boundary rejected
- Deposit Period Number zero rejected
- Expected First Deposit On: yesterday blocked, today accepted
- Rapid re-submission after creation blocked (no duplicate)
- Excessive decimal precision in Deposit Amount is rounded on save

### Accounting — Chart of Accounts (~4 extra types)
- Parent Account dropdown filtered to only header accounts of the selected Account Type
- Previously selected Parent Account is cleared when Account Type changes
- GL Code uniqueness triggered even with leading/trailing whitespace matching existing code

### Accounting — Journal Entries & Closures (~7 extra types)
- Remove the only entry line blocked (min=1 constraint)
- Balanced vs off-by-one-unit entry line totals boundary
- Create closure then immediately attempt journal entry on same closing date
- Office whitespace trimming on saved journal entry record

### Accounting Rules & Financial Activity Mappings (~7 extra types)
- Financial Activity dropdown shows only unmapped activities
- Create Mapping when all activities already mapped shows empty dropdown
- Rule Name XSS/special character input handling
- Delete confirmation dialog cancellation preserves rule

### Provisioning (~5 extra types)
- Provisioning criteria form field validation (leave required fields blank)
- Provisioning entry line amount format validation

### Offices (~7 extra types)
- Office creation form field-level validation (each required field individually)
- Submitted On boundary: today accepted, one day in future blocked
- Very long Office Name accepted or truncated gracefully
- Rapid re-submission after successful create is blocked

### Employees (~7 extra types)
- Employee creation form field-level validation
- Join Date boundary: today accepted, future date behavior
- Special characters and emoji in employee name

### Teller & Cashier Management (~6 extra types)
- Allocate Cashier same-day Start and End Date accepted
- Allocate Cashier End Date before Start Date blocked
- Settle Cash excessive decimal precision blocked
- Settle Cash with Transaction Date = today accepted
- Teller Name whitespace trimming on save

### Users & Roles (~4 extra types)
- Permission checkbox toggle on Role Permissions page
- Rapid re-submission after create user catches duplicate username via browser back
- Password/Repeat Password mismatch caused by trailing whitespace difference

### Reports (~71 extra types)
- Full matrix of tab (All, Clients, Funds, Accounting, XBRL) × action (Name link open, row click open, View On Screen, Export Excel, Export CSV, Export PDF) permutations far exceeding the GT scope
- Date Range boundary tests: single-day range, far-future zero-row result, rapid double-click of Run Report
- Export to Excel with zero data rows still produces a valid file with headers

### Account Transfers & Standing Instructions (~9 extra types)
- Transfer form field-level boundary tests (zero amount, past/future date)
- Standing instruction form date-order validation
- Bulk import with empty file or headers-only template

### Tax Management (~8 extra types)
- Tax component creation conditional field validation
- Tax group composition and deactivation of individual components
- Date range validation on tax component effective periods

### Organization Settings (~6 extra types)
- Holiday date-order validation (To Date before From Date blocked)
- Same-day holiday accepted
- Bulk import Clients with headers-only file shows zero-import result
- Non-admin role cannot access Organization section
- Holiday Pending and Active states show no available actions

### System Administration (~10 extra types)
- Scheduler job inline CRON expression edit (valid and invalid minimal expressions)
- Code Values editor: Add/Edit/Move Up/Move Down boundary conditions including first-item Move Up and last-item Move Down blocked
- Data Table: add columns then remove all, create with zero columns succeeds
- Audit Trails maker-checker: Approve when disabled, Approve on non-Pending entry blocked, Reject when disabled
- Audit Trails date filter: same-day range accepted, out-of-order range blocked

### Logout (~4 extra types)
- Profile icon inaccessible when unauthenticated
- Direct navigation to Profile Settings while unauthenticated redirected to login
- Invoking logout endpoint while unauthenticated redirected to login
- Concurrent logout in two tabs: second tab also lands on login page cleanly