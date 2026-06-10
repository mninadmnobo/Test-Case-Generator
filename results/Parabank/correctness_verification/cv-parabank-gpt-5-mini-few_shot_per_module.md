# Correctness Verification: Parabank (gpt-5-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Parabank.md`  
**Total Generated Test Cases:** 158  
**Modules Covered:** Login (12), Register (15), Accounts Overview (9), Open New Account (13), Transfer Funds (10), Payments (14), Request Loan (13), Update Contact Info (10), Manage Cards (16), Investments (11), Account Statements (10), Security Settings (11), Support Center (14)

---

## Error Analysis

### A. Precondition Errors

**Total:** 1

- **TC IDs:** Register TC-011 *(assumes max SSN length limit)*
- *Reasoning:*
  - **Register TC-011:** Precondition assumes a specific maximum length constraint for the SSN beyond the standard format.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** No hallucinations in test steps found. The pipeline aligned element interactions closely with the described UI.

---

### C. Expected Result Errors

**Total:** 2

- **TC IDs:** Request Loan TC-012 *(invalid down payment)*, Security Settings TC-008 *(weak password accepted)*
- *Reasoning:*
  - **Request Loan TC-012:** Expected result asserts loan approval for a down payment that mathematically fails the 10% minimum requirement.
  - **Security Settings TC-008:** Expected result asserts password change success despite missing the required special character.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Register TC-011 | Register | Precondition |
| Request Loan TC-012 | Request Loan | Expected Result |
| Security Settings TC-008 | Security Settings | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 158
- **Total Test Cases with Errors:** 3 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 155

**Overall Success Rate: 155 / 158 (98.10%)**

---

## Thesis Analysis

The `gpt-5-mini` model using the `few_shot_per_module` approach achieved a highly reliable **98.10% correctness rate** across 158 test cases. The few errors present were typical language model struggles with strict mathematical constraints (down payment calculation) and formatting rules (special characters), though greatly reduced compared to smaller models. This validates that few-shot examples effectively guide larger models to high accuracy.
