# Test Coverage Report

**Ground Truth:** Mifos Banking System GT v2.0  
**Generated Suite:** gpt-5-mini — 503 cases  
**Analysis Date:** 2026-06-08  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording. Implied coverage and equivalence-class matches are accepted; specific edge conditions (e.g. SQL injection, null byte, emoji) require the GEN test to explicitly target the same technical boundary.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 607 |
| GT cases covered by GEN | 406 |
| GT cases not covered by GEN | 201 |
| **Overall coverage** | **66.9%** |
| GEN cases with no GT counterpart (extras) | ~95 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 7 | 5 | **58%** |
| Home | 5 | 4 | 1 | **80%** |
| Dashboard | 5 | 4 | 1 | **80%** |
| Global Search | 11 | 9 | 2 | **82%** |
| Client Management | 29 | 21 | 8 | **72%** |
| Group Management | 18 | 14 | 4 | **78%** |
| Center Management | 18 | 13 | 5 | **72%** |
| Loan Products | 14 | 11 | 3 | **79%** |
| Savings Products | 15 | 10 | 5 | **67%** |
| Charges | 16 | 10 | 6 | **63%** |
| Loan Account | 29 | 20 | 9 | **69%** |
| Savings Account | 22 | 16 | 6 | **73%** |
| Chart of Accounts | 11 | 8 | 3 | **73%** |
| Journal Entries | 11 | 9 | 2 | **82%** |
| Users & Roles | 18 | 14 | 4 | **78%** |
| Offices | 11 | 8 | 3 | **73%** |
| Employees | 7 | 6 | 1 | **86%** |
| Reports | 10 | 8 | 2 | **80%** |
| Organization Settings | 15 | 10 | 5 | **67%** |
| Share Products | 12 | 9 | 3 | **75%** |
| Floating Rates | 11 | 10 | 1 | **91%** |
| Delinquency Management | 10 | 8 | 2 | **80%** |
| Share Account | 15 | 11 | 4 | **73%** |
| Fixed & Recurring Deposits | 20 | 14 | 6 | **70%** |
| Accounting — Closures | 8 | 5 | 3 | **63%** |
| Accounting Rules & FAM | 9 | 6 | 3 | **67%** |
| Provisioning | 9 | 7 | 2 | **78%** |
| Teller & Cashier | 16 | 11 | 5 | **69%** |
| Account Transfers & SI | 14 | 11 | 3 | **79%** |
| Tax Management | 11 | 9 | 2 | **82%** |
| System Administration | 18 | 11 | 7 | **61%** |
| Logout | 7 | 7 | 0 | **100%** |
| **Total** | **607** | **406** | **201** | **66.9%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (5 missing)
- MF-LOGIN-010 SQL injection payload in Username field (`' OR 1=1;--`)
- MF-LOGIN-013 Null byte injection in username (`admin%00`)
- MF-LOGIN-014 Cross-site scripting (XSS) in Tenant field (`<script>alert(1)</script>`)
- MF-LOGIN-015 Emoji in username (🚀)
- MF-LOGIN-012 Rapid double click on Login button (idempotency / session dedup)

### Home (1 missing)
- MF-HOME-005 Home page route accessible directly after authentication via URL

### Dashboard (1 missing)
- MF-DASH-011 Dashboard — deep link bypassing dashboard intercepted correctly

### Global Search (2 missing)
- MF-SEARCH-011 SQL injection in search bar (`' UNION SELECT`)
- MF-SEARCH-013 Rapid repeated searches debounced to single request

### Client Management (8 missing)
- MF-CLIENT-024 HTML injection in First Name (`<b>Name</b>`) rendered safely
- MF-CLIENT-025 Date of Birth in year 1800 rejected with validation error
- MF-CLIENT-026 Last Name exactly 256 characters rejected
- MF-CLIENT-027 Concurrent activation from two tabs processed idempotently
- MF-CLIENT-028 Duplicate External ID server-side unique constraint
- MF-CLIENT-029 Zero-length file upload blocked with validation error
- MF-CLIENT-027 Assign staff to client (staff assignment workflow)
- MF-CLIENT-028 Client charges tab — add charge action workflow

### Group Management (4 missing)
- MF-GROUP-014 1000 members in one group — stress/timeout test
- MF-GROUP-016 Adding deceased client to group blocked by business rule
- MF-GROUP-017 Concurrent group activation processed once
- MF-GROUP-018 Group notes added and displayed chronologically

### Center Management (5 missing)
- MF-CENTER-014 Adding same group twice rapidly — unique constraint caught
- MF-CENTER-015 Center name with special Unicode (emoji) sanitized or accepted safely
- MF-CENTER-016 Extreme pagination on center list — graceful empty state
- MF-CENTER-017 Empty center meetings submission blocked
- MF-CENTER-018 Duplicate external ID for center blocked

### Loan Products (3 missing)
- MF-LPROD-018 Principal max set to 999,999,999,999 boundary check
- MF-LPROD-021 Decimal places set to exactly 0 — validation error
- MF-LPROD-022 Term length of 100 years (1200 months) — accepted or limit error

### Savings Products (5 missing)
- MF-SPROD-014 Duplicate savings product short name — uniqueness constraint
- MF-SPROD-016 Overdraft limit set to negative value — validation error
- MF-SPROD-017 Interest rate with 10 decimal places — precision error or truncated
- MF-SPROD-018 Minimum balance greater than maximum balance — validation error
- MF-SPROD-021 Extreme maximum withdrawal fee (999999) — boundary check

### Charges (6 missing)
- MF-CHARGE-013 Flat charge amount of 1,000,000,000 — boundary check
- MF-CHARGE-014 Percentage charge of 100.01% rejected
- MF-CHARGE-015 Negative charge amount rejected
- MF-CHARGE-016 Charge name containing XSS payload sanitized
- MF-CHARGE-017 Applying a deleted charge blocked
- MF-CHARGE-015 Charge collected from account — accounting and balance update verified

### Loan Account (9 missing)
- MF-LOAN-022 Repayment exactly $0.01 accepted
- MF-LOAN-023 Overpayment exactly $0.01 over outstanding balance — blocked or held
- MF-LOAN-024 Negative repayment amount — validation error
- MF-LOAN-025 Disbursement on future date — validation error
- MF-LOAN-026 Rapid double click on approve — processed once
- MF-LOAN-027 Write-off with zero balance — validation error
- MF-LOAN-025 Apply payment allocation rules correctly for mixed due amounts
- MF-LOAN-026 Post penalty on overdue installment
- MF-LOAN-030 Loan guarantor or collateral tab accessible where feature is enabled

### Savings Account (6 missing)
- MF-SAV-017 Deposit exactly maximum integer — handled gracefully
- MF-SAV-018 Withdraw exactly available balance — balance becomes zero
- MF-SAV-019 Withdraw $0.01 over available balance — blocked
- MF-SAV-020 Rapid double click withdraw — processed once, no overdraft
- MF-SAV-021 Deposit negative amount — validation error
- MF-SAV-022 Activate savings account on future date — validation error

### Chart of Accounts (3 missing)
- MF-COA-013 HTML tags in GL account description — sanitized
- MF-COA-014 Cyclical parent-child mapping — validation error
- MF-COA-016 Negative initial balance rejected

### Journal Entries (2 missing)
- MF-JRN-012 Journal entry with 10,000 line items — timeout handled or accepted
- MF-JRN-015 Duplicate transaction reference — warning or blocked

### Users & Roles (4 missing)
- MF-USER-020 Rapid password change loop — handled gracefully
- MF-USER-021 Username matching SQL reserved word — accepted safely
- MF-USER-023 HTML in last name — sanitized
- MF-USER-024 Assign user to a deleted office — validation error

### Offices (3 missing)
- MF-OFFICE-010 Open office with future date — validation error
- MF-OFFICE-011 Cyclical parent office mapping — validation error
- MF-OFFICE-015 Office hierarchy nested 100+ levels deep — handled gracefully

### Employees (1 missing)
- MF-EMP-009 Duplicate mobile number for employee — validation error

### Reports (2 missing)
- MF-REPORT-008 Date range spanning 50 years — timeout handled
- MF-REPORT-012 Rapid double click on generate — single query executed

### Organization Settings (5 missing)
- MF-ORG-013 Password expiry set to 9999 days — boundary accepted
- MF-ORG-015 HTML tags in org name — sanitized
- MF-ORG-016 Overlapping working days — validation error
- MF-ORG-017 Maker-checker disabled then bypassed — bypass succeeds
- MF-ORG-015 Holiday affects repayment or transaction scheduling correctly

### Share Products (3 missing)
- MF-SHPROD-010 Max shares boundary 9,999,999 — accepted
- MF-SHPROD-011 Nominal price with 6 decimal places — precision error
- MF-SHPROD-013 Negative total shares — validation error

### Floating Rates (1 missing)
- MF-FRATE-013 Floating rate period From-date in extreme past (01/01/1900) — accepted safely

### Delinquency Management (2 missing)
- MF-DELINQ-011 Maximum age days set to 9999 — accepted
- MF-DELINQ-012 Bucket with 0 ranges — validation error

### Share Account (4 missing)
- MF-SHARE-013 Purchase zero shares — validation error
- MF-SHARE-014 Purchase fractional shares (1.5) — validation error
- MF-SHARE-015 Purchase more shares than total issued — blocked
- MF-SHARE-016 Redeem shares before lock-in period ends — blocked

### Fixed & Recurring Deposit Accounts (6 missing)
- MF-DEP-017 Deposit term set to 100 years — limit error
- MF-DEP-018 Interest rate exactly 100% — handled
- MF-DEP-019 Negative deposit amount — validation error
- MF-DEP-020 Withdrawing before maturity — blocked
- MF-DEP-021 Rapid double click close — closed once
- MF-DEP-020 Recurring deposit missed installment behavior follows product rules

### Accounting — Closures (3 missing)
- MF-CLOSE-007 Closing on a future date — validation error
- MF-CLOSE-009 Reversing closure when subsequent transactions exist — blocked
- MF-CLOSE-010 Closure notes exceeding 2000 characters — validation error

### Accounting Rules & Financial Activity Mappings (3 missing)
- MF-FAM-007 Rule mapping debit to income — invalid schema blocked
- MF-FAM-008 Cyclical rule mapping — blocked
- MF-FAM-011 Blank tag configuration — validation error

### Provisioning (2 missing)
- MF-PROV-010 Run provisioning twice in same day — processed once
- MF-PROV-011 Invalid asset class code — validation error

### Teller & Cashier (5 missing)
- MF-TELLER-013 Cashier cash allocation with negative amount — validation error
- MF-TELLER-014 Allocating cash with overlapping dates — validation error
- MF-TELLER-015 Settle cashier without funds — blocked or warning
- MF-TELLER-016 Delete active teller — blocked
- MF-TELLER-017 Extremely long teller name (255 chars) — accepted

### Account Transfers & Standing Instructions (3 missing)
- MF-TRF-012 Transfer exactly $0.01 — accepted
- MF-TRF-014 Standing instruction from account to same account — validation error
- MF-TRF-015 Standing instruction start date in the past — validation error

### Tax Management (2 missing)
- MF-TAX-011 Overlapping tax components in group — validation error
- MF-TAX-013 Apply deleted tax group — validation error

### System Administration (7 missing)
- MF-SYS-015 Hook URL containing XSS payload — sanitized
- MF-SYS-016 Disable core scheduled job — warning or block
- MF-SYS-017 Invalid cron expression — validation error
- MF-SYS-018 Modifying cache config rapidly — idempotent
- MF-SYS-019 Duplicate hook URL — accepted or warning
- MF-SYS-020 Scheduler timeout simulation — graceful timeout
- MF-SYS-021 Extremely long hook URL (2000 chars) — validation error

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~2 extra types)
- Language selector presence and label update on language change
- Left panel background image and branding elements verified

### Home (~2 extra types)
- Search Activity trimmed of whitespace before execution
- Mifos and Fineract version information format verification

### Dashboard (~3 extra types)
- Client Trends chart tooltip detail on hover
- Numeric formatting of summary cards when data exists
- Dense time-series rendering in Client Trends chart

### Global Search (~2 extra types)
- Entities with identical names across types distinguished and navigable
- Single-character search performance/responsiveness

### Client Management (~5 extra types)
- Bulk import with valid records — success count in import history
- Bulk import with mixed valid/invalid records — failure report download
- Import Client bulk template download workflow
- Client detail action buttons reflect Rejected/Withdrawn status correctly
- Identifier removal updates list

### Group Management (~5 extra types)
- Collection Sheet generation for a group with members and dues
- Transfer clients from one group to another
- Bulk import CSV upload and import history entry
- Download group template selecting office and staff
- Group meeting scheduling with end before start validation

### Center Management (~3 extra types)
- Collection Sheet generation for center with groups and clients
- Bulk import centers using valid CSV template
- Special character search in Select and Add groups field

### Loan Products (~3 extra types)
- Six-step wizard with Cash-based accounting verified end to end
- Decimal places set to 0 with rounding to 1 (integer-only currency)
- Close Date earlier than Start Date blocked (date ordering validation)

### Savings Products (~4 extra types)
- Toggle accounting radio between None and Cash-based — GL field visibility
- Enable overdraft with max amount zero and very large amount
- Withhold tax checkbox requires Tax Group selection
- Interest rate chart overlapping period ranges rejected

### Share Products (~6 extra types)
- Market Price multiple rows saved and ordered
- Add and remove charges in wizard before saving
- Capital Value auto-recalculates when Nominal Price changes on edit
- Delete share product with zero issued shares
- Overlapping market price date ranges conflict handling
- Shares to be issued greater than total shares — validation error

### Charges (~3 extra types)
- Charge Time Type dropdown adapts to selected Charge Applies To
- Percentage charge with 100% amount (boundary percentage) handled
- Is Active unchecked at creation — inactive state reflected in list

### Floating Rates (~3 extra types)
- Create floating rate with multiple periods including differential rows
- Attempt to create second Base Lending Rate when one already exists
- Large number of rate periods added — UI responsiveness and persistence

### Delinquency Management (~3 extra types)
- Create bucket with sequential ranges and link to loan product
- Automatic classification of overdue loan into correct delinquency range
- Large number of sequential ranges added to bucket — stress/limit test

### Loan Account (~4 extra types)
- Disburse to Savings when client has no linked savings account
- Undo recent reversible transaction — balances restored
- Loan application submitted skipping optional collateral and charges
- Add collateral in Step 4 verified in Collateral tab

### Savings Account (~4 extra types)
- Approve action unavailable on non-pending account
- Deposit with incomplete payment type details (Check Number) rejected
- Unusually large nominal annual interest rate handled or rejected
- Transaction amount with excessive decimal places — rounding/validation

### Share Account (~5 extra types)
- Approve with shares greater than requested — blocked
- Leap day (Feb 29) as Application Date — accepted
- Redeem shares when unit price causes rounding — credited amount verified
- Submit application with Requested Shares at exact minimum boundary
- Submit application with Requested Shares at exact maximum boundary

### Fixed & Recurring Deposits (~6 extra types)
- RD account with quarterly frequency — schedule intervals verified
- Interest rate applied from product Interest Rate Chart based on deposit amount/term
- Approve and activate RD, verify deposit frequency enforcement
- Create FD with very large Deposit Amount near system maximum
- RD with daily frequency — short period schedule generation
- FD with deposit period in Days unit — maturity date and interest calculation

### Accounting — Journal Entries & Closures (~4 extra types)
- Journal entry with large number of lines — Add Row scalability
- Same GL Account used across multiple lines (net-zero) — allowed
- Transaction Date equal to Closing Date treated as blocked (boundary)
- Filter journal entries by Transaction ID

### Accounting Rules & Financial Activity Mappings (~4 extra types)
- Create rule allowing multiple Debit and Credit entries
- Create all financial activity mappings until none remain
- Max number of Debit accounts in multi-select (boundary)
- Map financial activity using GL account with special characters or long name

### Provisioning (~4 extra types)
- Recreate existing provisioning entry with recalculated amounts
- Provisioning entry when no loans match criteria — zero totals handled
- Overlapping definition ranges — validation or priority rules
- Percentage boundary values (0% and decimal precision)

### Offices (~2 extra types)
- Create child office under existing branch (non-root parent)
- External ID left empty (optional field) — office created successfully

### Employees (~3 extra types)
- Staff marked as Loan Officer appears in Loan Officer dropdown when creating loans
- Toggle Is Loan Officer flag — Loan Officer dropdown updates immediately
- Create employee with leap-day Joining Date (Feb 29)

### Teller & Cashier (~4 extra types)
- Allocate cash with decimal precision — running balance accuracy verified
- Settle cash with amount greater than Cash In Hand — blocked
- Allocate cashier with Start Date equal to End Date (single-day assignment)
- Cashier transactions paginated list across many sequential transactions

### Account Transfers & Standing Instructions (~5 extra types)
- Transfer amount with more than two decimal places — precision/validation
- Same account selected for From and To — blocked
- Create Standing Instruction with Validity From equal to Validity Till (single-day)
- Create Standing Instruction with extremely long Name (256 chars)
- Transfer from savings to loan account (credit to loan)

### Tax Management (~4 extra types)
- Tax component Percentage = 0% — zero tax posting verified
- Tax component Percentage = 100% — full amount withheld
- Tax Group component End Date earlier than Start Date — validation error
- Tax component with high decimal precision — rounding in postings

### Organization Settings (~8 extra types)
- Holiday spans year-end (Dec 31 to Jan 2) — date boundary handling
- Configure only one working day and verify repayment behavior
- Configure Sunday as sole working day
- Deactivate all currencies and verify system behavior
- Create Fund at maximum allowed name length
- Payment Type with very long Description and high Position number
- Upload empty import file or file with only headers — zero records processed
- Upload wrong template type for Clients — rejected

### System Administration (~5 extra types)
- Save CRON expression at maximum allowed length — accepted or truncated
- Data Table with maximum number of columns and mixed types
- Audit Trails filtered with start date equal to end date (boundary)
- Rapid toggle of global scheduler On/Off — stable state
- Deactivate a custom (non-system) code value — dropdowns update

### Logout (~1 extra type)
- Log out while network is offline — client clears token, redirects to login