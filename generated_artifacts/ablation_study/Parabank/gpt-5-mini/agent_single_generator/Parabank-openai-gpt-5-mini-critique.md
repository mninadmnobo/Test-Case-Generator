# Semantic Critique — Parabank

Generated: 2026-06-09T10:57:12.107440Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the login form, required fields with stated validation constraints, the Sign In submit behavior (success and failure handling), and the Forgot Password? link—no critical elements missing.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures all interactive elements, required fields, validation rules, state dropdown options, and submit behaviors described in the specification.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents the interactive elements (clickable masked account number, default sort by open date, and footer total); it includes two passive display columns that are minor phantoms.

**Missing:** none

**Phantoms (hallucinations):**

- Customer_Accounts_Table.row_fields.Account_Type (passive display column — out-of-scope)
- Customer_Accounts_Table.row_fields.Account_Status (passive display badge — out-of-scope)

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the form, interactive account-type selection, deposit and funding fields, real-time validations, minimum deposit rules, funding-balance check, and success behavior with redirect.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the described interactive elements and validations; a single minor phantom (unnamed submit button labeled 'Transfer') was added but is acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Transfer_Form.submit_actions[0] (Transfer button not explicitly named in the description)

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements (all named form fields, Source_Account dropdown, Pay button), the explicit validations (account-number match, funds check, amount > 0), and the specified success/failure behaviors, so it is acceptable.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements and validations from the description; only a minor phantom is the explicit submit button name which was not specified in the description.

**Missing:** none

**Phantoms (hallucinations):**

- Loan_Request_Form.submit_actions[0].element_name (Request Loan button name not explicitly specified in description)

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the editable pre-filled form with the seven fields, the Update Profile submit action, validation behavior, success message and data refresh, and failure handling.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the two forms, their fields, buttons, validations, and success/failure behaviors described; no missing interactive elements or extraneous phantoms found.

**Missing:** none

**Phantoms:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the Trade Funds and Recurring Investment Plan forms, their interactive fields, validation rules, and submit actions; no missing interactive elements or extraneous phantoms were found.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents both forms, their fields, buttons, validation rules, conditional date inputs, and success/failure messages as described.

**Missing:** none

**Phantoms:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the collapsible panel, the change-password form with the three password fields, the Change Password submit action, policy checks, success message, and validation behavior described.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents both forms, their fields, validations, and submit behaviors described in the spec.

**Missing:** none

**Phantoms:** none

---
