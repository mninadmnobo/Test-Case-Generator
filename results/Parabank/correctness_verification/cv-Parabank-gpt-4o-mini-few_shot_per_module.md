# Correctness Verification: Parabank (gpt-4o-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Parabank/gpt-4o-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Parabank.md`  
**Total Generated Test Cases:** 71  
**Modules Covered:** Login (5), Register (5), Accounts Overview (4), Open New Account (7), Transfer Funds (6), Payments (4), Request Loan (5), Update Contact Info (4), Manage Cards (6), Investments (7), Account Statements (6), Security Settings (5), Support Center (7)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Accounts Overview TC-014 *(assumes maximum allowed accounts limit)*, Support Center TC-071 *(assumes tomorrow is a business day)*
- *Reasoning:*
  - **Accounts Overview TC-014:** Precondition states "User has the maximum allowed number of accounts." Parabank's functional specifications do not mention a system limit on the maximum number of accounts. This assumes a hallucinated system limit.
  - **Support Center TC-071:** Precondition states "User logged in" and steps instruct to "Enter tomorrow's date as the Preferred Date" for the earliest possible callback date. The functional requirements state the system "ensures the date is at least the next business day." The precondition fails to guarantee tomorrow is a weekday, meaning the expected result of success is logically flawed if run on a Friday.

---

### B. Test Steps Errors

**Total:** 0

- **TC IDs:** None
- *Reasoning:*
  - **N/A:** No hallucinations in test steps found. The pipeline aligned element interactions and step sequences closely with the described UI.

---

### C. Expected Result Errors

**Total:** 5

- **TC IDs:** Register TC-006 *(invalid password accepted)*, Register TC-009 *(invalid password accepted)*, Register TC-010 *(invalid password accepted)*, Request Loan TC-034 *(invalid down payment approved)*, Request Loan TC-036 *(invalid down payment approved)*
- *Reasoning:*
  - **Register TC-006:** Expected result asserts "Account created successfully" despite providing the password 'Password123', which lacks the mandatory special character specified in the requirements.
  - **Register TC-009:** Expected result asserts successful registration while using the password 'Pass123', which is only 7 characters long and lacks a special character, violating the 8-character and special character constraints.
  - **Register TC-010:** Expected result asserts successful registration while using the password 'Password123', missing the required special character.
  - **Request Loan TC-034:** Expected result expects "Loan approved and created successfully!" for a $500,000 home loan with a $10,000 down payment. The $10,000 is only 2% of $500,000, which strictly violates the 10% minimum down payment requirement.
  - **Request Loan TC-036:** Same mathematical error as TC-034. Expected result asserts loan approval for a $500,000 loan with a $10,000 down payment (2%), violating the 10% requirement.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Register TC-006 | Register | Expected Result |
| Register TC-009 | Register | Expected Result |
| Register TC-010 | Register | Expected Result |
| Accounts Overview TC-014 | Accounts Overview | Precondition |
| Request Loan TC-034 | Request Loan | Expected Result |
| Request Loan TC-036 | Request Loan | Expected Result |
| Support Center TC-071 | Support Center | Precondition |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 71
- **Total Test Cases with Errors:** 7 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 64

**Overall Success Rate: 64 / 71 (90.14%)**

---

## Thesis Analysis

The `gpt-4o-mini` with the `few_shot_per_module` approach achieved a strong **90.14% correctness rate** while generating 71 test cases. It successfully aligned test steps and element interactions strictly with the functional description, exhibiting zero test step hallucinations. 

The errors identified reveal a specific vulnerability in how the model handles strict mathematical and character-level data validation constraints. The majority of errors (5 out of 7) stemmed from failing to strictly apply numeric/formatting constraints within hardcoded test data—specifically, calculating the 10% minimum down payment correctly and ensuring hardcoded passwords included special characters and met minimum length requirements.

This finding highlights that while the `few_shot_per_module` approach scales structural coverage well, lightweight models (`gpt-4o-mini`) may still struggle with generating explicit test data payloads that satisfy strict mathematical or character-level rules when constructing boundary edge cases.
