# Correctness Verification: Parabank (gpt-5-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Parabank.md`  
**Total Generated Test Cases:** 198  
**Modules Covered:** Login (14), Register (20), Accounts Overview (12), Open New Account (15), Transfer Funds (15), Payments (13), Request Loan (14), Update Contact Info (15), Manage Cards (16), Investments (20), Account Statements (13), Security Settings (12), Support Center (19)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Account Statements TC-010 *(assumes max date range)*, Support Center TC-018 *(assumes tomorrow is business day)*
- *Reasoning:*
  - **Account Statements TC-010:** Instructs to use a "maximum allowed date range" which is not constrained in the spec.
  - **Support Center TC-018:** Assumes tomorrow is a business day for a callback request, which can fail if run on a weekend.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** No hallucinations in test steps found.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Transfer Funds TC-011 *(assumes internal transfer limit)*
- *Reasoning:*
  - **Transfer Funds TC-011:** Expects a validation error for a very large internal transfer amount, falsely assuming a maximum transfer limit exists beyond the account balance.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Account Statements TC-010 | Account Statements | Precondition |
| Support Center TC-018 | Support Center | Precondition |
| Transfer Funds TC-011 | Transfer Funds | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 198
- **Total Test Cases with Errors:** 3 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 195

**Overall Success Rate: 195 / 198 (98.48%)**

---

## Thesis Analysis

The `gpt-5-mini` using the `zero_shot_per_module` approach achieved an outstanding **98.48% correctness rate** across nearly 200 test cases. It successfully avoided the rigid validation failures often introduced by flawed few-shot examples in smaller models, proving that highly capable foundation models can strictly adhere to constraints even in zero-shot settings when prompted per module.
