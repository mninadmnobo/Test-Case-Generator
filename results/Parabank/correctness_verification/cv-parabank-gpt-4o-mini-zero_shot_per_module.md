# Correctness Verification: Parabank (gpt-4o-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-4o-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Parabank.md`  
**Total Generated Test Cases:** 92  
**Modules Covered:** Login (7), Register (9), Accounts Overview (7), Open New Account (8), Transfer Funds (7), Payments (6), Request Loan (7), Update Contact Info (5), Manage Cards (8), Investments (8), Account Statements (7), Security Settings (6), Support Center (7)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Accounts Overview TC-020 *(assumes maximum allowed accounts limit)*, Account Statements TC-075 *(assumes maximum date range)*
- *Reasoning:*
  - **Accounts Overview TC-020:** Precondition states "User has maximum allowed customer accounts." Parabank's functional specifications do not mention a system limit on the maximum number of accounts.
  - **Account Statements TC-075:** Instructs to "Select the maximum allowed date range (e.g., 1 year)." The functional description does not restrict the date range to a maximum limit.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** No hallucinations in test steps found. The pipeline aligned element interactions closely with the described UI.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Support Center TC-092 *(allows callback for today's date)*
- *Reasoning:*
  - **Support Center TC-092:** The steps specify "Select today's date if it is a business day..." and the expected result is "Callback request submitted." The functional description explicitly states the system "ensures the date is at least the next business day." Thus, a callback cannot be scheduled for today, and it should result in a validation error.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Accounts Overview TC-020 | Accounts Overview | Precondition |
| Account Statements TC-075 | Account Statements | Precondition |
| Support Center TC-092 | Support Center | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 92
- **Total Test Cases with Errors:** 3 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 89

**Overall Success Rate: 89 / 92 (96.74%)**

---

## Thesis Analysis

The `gpt-4o-mini` with the `zero_shot_per_module` approach achieved an impressive **96.74% correctness rate** across 92 test cases. Unlike the few-shot approach, it avoided hardcoding specific invalid passwords or incorrect down payments, which helped it bypass the constraint execution failures seen in other approaches. The minimal errors present were minor hallucinations of system bounds (max accounts, max date ranges) and a slight misinterpretation of the "next business day" logic. This supports the thesis that breaking down tasks per module effectively scales test case generation with very high logical accuracy.
