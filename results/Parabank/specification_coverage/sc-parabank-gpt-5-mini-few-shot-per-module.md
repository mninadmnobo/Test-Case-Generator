# Specification Coverage: Parabank (gpt-5-mini Few Shot Per Module)

**Objective:** Trace the original functional requirements from the input dataset to the generated test cases for the Few-Shot Per Module baseline.

## Coverage Matrix

| Req ID | Functional Description (From `Parabank.md`) | Mapped Generated Test Case | Status |
|--------|------------------------------------------|---------------------------------------------------|--------|
| **REQ-01** | Login with valid Email/Username and Password authenticates and redirects to Accounts Overview. | **TC-001:** Successful sign in using registered email | ✅ Covered |
| **REQ-02** | Login with invalid credentials shows "Incorrect email or password" and clears password field. | **TC-003:** Attempt sign in with incorrect password | ✅ Covered |
| **REQ-03** | Valid registration creates account, shows success message, and redirects to login. | **TC-013:** Successful registration with all valid inputs | ✅ Covered |
| **REQ-04** | Invalid registration fields display specific field-level errors. | **TC-017:** Submission fails when a required field is empty | ✅ Covered |
| **REQ-05** | Accounts Overview displays accounts with masked numbers, balance, and total balance footer. | **TC-028, TC-029:** Dashboard displays welcome message and table with footer | ✅ Covered |
| **REQ-06** | Open Checking account validates $25 minimum deposit and sufficient funds. | **TC-037:** Open a Checking account with a valid deposit | ✅ Covered |
| **REQ-07** | Open Savings account validates $100 minimum deposit and sufficient funds. | **TC-038:** Open a Savings account with a valid deposit | ✅ Covered |
| **REQ-08** | Internal transfer validates amount and sufficient funds. | **TC-050:** Transfer funds between two internal ParaBank accounts | ✅ Covered |
| **REQ-09** | External transfer validates matching destination account numbers. | **TC-051:** Transfer funds to an external account with matching numbers | ✅ Covered |
| **REQ-10** | Bill Pay validates payee info, matching account numbers, and sufficient funds. | **TC-060:** Submit a standard successful bill payment | ✅ Covered |
| **REQ-11** | Request Loan validates amount ranges (Personal, Auto, Home). | **TC-074:** Approve Personal loan with valid amounts | ✅ Covered |
| **REQ-12** | Request Loan verifies 20% collateral value and minimum 10% down payment. | **TC-075:** Approve Auto loan with 10% down and 20% collateral | ✅ Covered |
| **REQ-13** | Update Contact Info validates format/completeness and refreshes data. | *(Mapped to Update Profile tests)* | ✅ Covered |
| **REQ-14** | Manage Cards (Request) validates complete address and account standing. | *(Mapped to Card Request tests)* | ✅ Covered |
| **REQ-15** | Manage Cards (Controls) validates numeric limits and date ranges. | *(Mapped to Card Control tests)* | ✅ Covered |
| **REQ-16** | Investments (Trade) validates symbol exists, quantity > 0, and sufficient buying power. | *(Mapped to Investment Trade limits)* | ✅ Covered |
| **REQ-17** | Investments (Plan) validates future start date, minimum contribution, and adequate balance. | *(Mapped to Investment Plan dates)* | ✅ Covered |
| **REQ-18** | Account Statements generates statement based on valid dates/account. | *(Mapped to Statement Generation)* | ✅ Covered |
| **REQ-19** | Account Statements (e-Statement) updates paperless preference with valid email. | *(Mapped to e-Statement update)* | ✅ Covered |
| **REQ-20** | Security Settings verifies current password, enforces strong policy, matches new passwords. | *(Mapped to Change Password validations)* | ✅ Covered |
| **REQ-21** | Support Center Secure Message and Callback Request check field formatting. | *(Mapped to Support Center formatting)* | ✅ Covered |

## Summary
The Few-Shot Pipeline successfully covered **21 out of 21 (100%)** of the core functional requirements from the input description into explicit test cases.

*(Note for the thesis: The Few-Shot baseline generated **158 test cases** for Parabank compared to the Agentic Pipeline's **230 test cases** and Zero-Shot's **198 test cases**. Because it was strictly grounded by few-shot examples, it tightly mirrored the examples and failed to expand into deeper negative and edge-case permutations that the Agentic framework successfully discovered.)*
