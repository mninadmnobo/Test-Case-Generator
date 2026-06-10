# Correctness Verification: Parabank (gpt-4o-mini — Agent)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-4o-mini/agent/test-cases.md`  
**Functional Description:** `dataset/functional_description/Parabank.md`  
**Total Generated Test Cases:** 180  
**Modules Covered:** Login (12), Register (19), Accounts Overview (4), Open New Account (15), Transfer Funds (13), Payments (17), Request Loan (20), Update Contact Info (12), Manage Cards (18), Investments (16), Account Statements (10), Security Settings (10), Support Center (14)

---

## Error Analysis

### A. Precondition Errors

**Total:** 4

- **TC IDs:** Login TC-001 *(User logged in)*, Register TC-001 *(User logged in)*, Payments TC-014 *(minimum payment amount)*, Payments TC-015 *(minimum payment amount)*
- *Reasoning:*
  - **Login TC-001 & Register TC-001:** Both preconditions specify the user is already "logged in." A user cannot log in or register if they are already authenticated.
  - **Payments TC-014 & TC-015:** These tests assume there is a "minimum allowed Payment Amount" constraint. The functional description does not mention any minimum payment amount. The model hallucinated a business rule constraint.

---

### B. Test Steps Errors

**Total:** 4

- **TC IDs:** Transfer Funds TC-002, TC-009, TC-011, TC-012 *(repeating group/Add Destination)*
- *Reasoning:*
  - **Transfer Funds TC-002, 009, 011, 012:** The steps instruct the user to "Click 'Add Destination'" or add multiple external accounts using a "repeating group". The functional description for Transfer Funds only states that users "enter and confirm the account number" for external transfers. It does not contain a repeating group feature for multiple destinations.

---

### C. Expected Result Errors

**Total:** 8

- **TC IDs:** Login TC-002, TC-003, TC-004, TC-005, TC-006 *(inline validation errors)*, Accounts Overview TC-001 *(account number display)*, Account Statements TC-003, TC-004 *(inline validation errors)*
- *Reasoning:*
  - **Login TC-002 to TC-006:** The expected results claim an "Inline validation error appears". The functional description specifies that on failure, the system "shows 'Incorrect email or password...'" using a standard banner, not field-level inline validation.
  - **Accounts Overview TC-001:** The expected result states the "Account number displayed" after clicking the cell. The functional description explicitly notes that this feature is "(clickable but not implemented yet)".
  - **Account Statements TC-003 & TC-004:** The expected results claim the Statement Period field is highlighted with an inline error, whereas the spec explicitly describes a general banner "Unable to generate statement".

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Login TC-001 | Login | Precondition |
| Login TC-002 | Login | Expected Result |
| Login TC-003 | Login | Expected Result |
| Login TC-004 | Login | Expected Result |
| Login TC-005 | Login | Expected Result |
| Login TC-006 | Login | Expected Result |
| Register TC-001 | Register | Precondition |
| Accounts Overview TC-001 | Accounts Overview | Expected Result |
| Transfer Funds TC-002 | Transfer Funds | Steps |
| Transfer Funds TC-009 | Transfer Funds | Steps |
| Transfer Funds TC-011 | Transfer Funds | Steps |
| Transfer Funds TC-012 | Transfer Funds | Steps |
| Payments TC-014 | Payments | Precondition |
| Payments TC-015 | Payments | Precondition |
| Account Statements TC-003 | Account Statements | Expected Result |
| Account Statements TC-004 | Account Statements | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 180
- **Total Test Cases with Errors:** 16
- **Total Correct Test Cases:** 164

**Overall Success Rate: 164 / 180 (91.11%)**

---

## Thesis Analysis

The GPT-4o-mini Agent approach achieved a realistic **91.11% correctness rate** while generating a substantial 180 test cases. While the baseline few-shot approach achieved 90.14% (on only 71 cases), the Agent successfully generated **164 valid tests**—more than double the correct volume of the baseline. The agent's errors were primarily "intelligent hallucinations"—extrapolating common banking features (like repeating groups for transfers and minimum payment amounts) onto the simplified Parabank app. It wins on absolute volume of correct edge cases discovered.
