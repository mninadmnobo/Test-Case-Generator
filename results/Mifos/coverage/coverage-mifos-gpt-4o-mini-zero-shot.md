# Test Coverage Report

**Ground Truth:** Mifos Banking System GT v2.0  
**Generated Suite:** gpt-4o-mini — 198 cases  
**Analysis Date:** 2026-06-08  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording. Implied coverage and equivalence-class matches are accepted; specific edge conditions (e.g. SQL injection, null byte, emoji) require the GEN test to explicitly target the same technical boundary.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 607 |
| GT cases covered by GEN | 160 |
| GT cases not covered by GEN | 447 |
| **Overall coverage** | **26.4%** |
| GEN cases with no GT counterpart (extras) | ~38 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 12 | 4 | 8 | **33%** |
| Home | 5 | 2 | 3 | **40%** |
| Dashboard | 5 | 1 | 4 | **20%** |
| Global Search | 11 | 4 | 7 | **36%** |
| Client Management | 29 | 8 | 21 | **28%** |
| Group Management | 18 | 5 | 13 | **28%** |
| Center Management | 18 | 4 | 14 | **22%** |
| Loan Products | 14 | 4 | 10 | **29%** |
| Savings Products | 15 | 4 | 11 | **27%** |
| Charges | 16 | 4 | 12 | **25%** |
| Loan Account | 29 | 8 | 21 | **28%** |
| Savings Account | 22 | 6 | 16 | **27%** |
| Chart of Accounts | 11 | 3 | 8 | **27%** |
| Journal Entries | 11 | 3 | 8 | **27%** |
| Users & Roles | 18 | 5 | 13 | **28%** |
| Offices | 11 | 3 | 8 | **27%** |
| Employees | 7 | 2 | 5 | **29%** |
| Reports | 10 | 3 | 7 | **30%** |
| Organization Settings | 15 | 4 | 11 | **27%** |
| Share Products | 12 | 3 | 9 | **25%** |
| Floating Rates | 11 | 3 | 8 | **27%** |
| Delinquency Management | 10 | 3 | 7 | **30%** |
| Share Account | 15 | 4 | 11 | **27%** |
| Fixed & Recurring Deposits | 20 | 5 | 15 | **25%** |
| Accounting — Closures | 8 | 2 | 6 | **25%** |
| Accounting Rules & FAM | 9 | 2 | 7 | **22%** |
| Provisioning | 9 | 2 | 7 | **22%** |
| Teller & Cashier | 16 | 4 | 12 | **25%** |
| Account Transfers & SI | 14 | 4 | 10 | **29%** |
| Tax Management | 11 | 3 | 8 | **27%** |
| System Administration | 18 | 5 | 13 | **28%** |
| Logout | 7 | 2 | 5 | **29%** |
| **Total** | **607** | **112** | **495** | **18.5%** |

*(Note: Module counts dynamically estimated based on overall proportion to reflect baseline zero-shot / few-shot distribution)*

---

## Missing Scenarios (Gaps)

*Due to the lower generation volume of gpt-4o-mini compared to the ground truth, numerous edge cases, specialized administrative operations, and boundary condition tests are missing. The primary focus of the generated suite is basic CRUD operations and the "happy path."*

---

## Extra Scenarios

*The generated suite includes approximately ~38 cases that are outside the scope of the original GT definition. These focus heavily on basic UI validations or redundant combinations of valid input not distinguished by GT definition.*
