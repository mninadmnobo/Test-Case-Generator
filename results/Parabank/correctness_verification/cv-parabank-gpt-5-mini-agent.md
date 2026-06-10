# Correctness Verification: Parabank (gpt-5-mini — Agent)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-5-mini/agent/test-cases.md`  
**Functional Description:** `dataset/Parabank.md`  
**Total Generated Test Cases:** 230  
**Modules Covered:** Login (12), Register (22), Accounts Overview (13), Open New Account (19), Transfer Funds (19), Payments (14), Request Loan (32), Update Contact Info (12), Manage Cards (18), Investments (20), Account Statements (19), Security Settings (11), Support Center (19)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Login TC-001 *(assumes logged in)*, Payments TC-009 *(assumes scheduled payment capability)*
- *Reasoning:*
  - **Login TC-001:** Precondition specifies the user is already "logged in." A user cannot log in if they are already authenticated (violates initial state).
  - **Payments TC-009:** Assumes the user can set a "scheduled payment date" in the future. Parabank's simplified payment system executes immediately.

---

### B. Test Steps Errors

**Total:** 1

- **TC IDs:** Transfer Funds TC-015 *(save transfer template)*
- *Reasoning:*
  - **Transfer Funds TC-015:** Steps instruct the user to "Save as recurring transfer template." This feature is not in the functional description.

---

### C. Expected Result Errors

**Total:** 1

- **TC IDs:** Request Loan TC-024 *(auto-debit assumption)*
- *Reasoning:*
  - **Request Loan TC-024:** Expected result assumes that an auto-debit is automatically set up for the loan account, which is an extrapolated enterprise feature.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Login TC-001 | Login | Precondition |
| Payments TC-009 | Payments | Precondition |
| Transfer Funds TC-015 | Transfer Funds | Test Steps |
| Request Loan TC-024 | Request Loan | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 230
- **Total Test Cases with Errors:** 4
- **Total Correct Test Cases:** 226

**Overall Success Rate: 226 / 230 (98.26%)**

---

## Thesis Analysis

The GPT-5-mini Agent approach delivered a highly accurate **98.26% correctness rate** while generating an immense volume of test cases (230). A 100% success rate on 200+ cases is rarely genuine in LLM generation; here, we see the model made exactly 4 extremely plausible, "intelligent" hallucinations (assuming real-world banking features like auto-debit and scheduled payments). Despite this, it generated **226 fully valid test cases**—the highest of any approach. The agentic pipeline successfully scales exploration while maintaining near-perfect logical accuracy.
