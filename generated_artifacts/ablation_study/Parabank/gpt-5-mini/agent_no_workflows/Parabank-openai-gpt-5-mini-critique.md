# Semantic Critique — Parabank

Generated: 2026-06-09T10:50:52.836004Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents the login form, its required fields, validation constraints, submit actions (success and failure behaviors), and the 'Forgot Password?' link.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive fields, validations, auto-formatting, and submit behaviors described for the registration page.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the single interactive element (clickable, masked Account Number) and sorting; two minor phantom items found but not blocking.

**Missing:** none

**Phantoms (hallucinations):**

- components.Accounts_Table.interactive_columns['Account Number'].click_target (click target 'Account Detail' is not specified in the description)
- components.Accounts_Table.row_actions[0] (Open Account row action is not mentioned in the description)

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the form, selection options, fields, real-time validation, conditional minimums, funding-account balance check, and success redirect.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements, conditionals, and validations described; only two minor inferred items were added.

**Missing:** none

**Phantoms (hallucinations):**

- Transfer_Form.submit_actions[0].element_name ("Transfer" button label is not explicitly named in the description)
- Transfer_Form.submit_actions[0].on_failure_messages[2] ("invalid_amount" / "Invalid transfer amount." message is an inferred error not specified in the description)

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the bill-payment form, its fields, matching-account validation, funds check, submit action, and success/failure behavior.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST captures all interactive elements, validations, and simulated credit engine behavior from the description; only one minor phantom (unspecified submit button label) is present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Request_Loan_Form.submit_actions[0].element_name (Submit Loan Request button label not explicitly specified in the description)

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST includes the form, all seven fields, the Update Profile submit action, validation precondition, and success/failure behaviors as described, with no missing or extraneous interactive elements.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the two forms, their fields, validations, and submit behaviors; only two minor inferred details were added but are non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- Card_Controls_Form.submit_actions[0].preconditions[0] ("a card must be selected" is an inferred precondition not explicitly stated in the description)
- Card_Controls_Form.fields.Travel_Notice.item_fields.Destinations.min (min: 0 was added as an inferred constraint for the repeating destinations)

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (both forms, their fields, validations, and submit actions) described on the Investments page with no missing or extraneous interactive items.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents both side-by-side forms, their fields (statement period options, month/year or date range, account, paperless checkbox, email), submit actions, and success/failure behaviors with no missing or extraneous interactive elements.

**Missing:** none

**Phantoms:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the collapsible panel, the change-password form with all three password fields, the Change Password button, and the described validation and success/failure behaviors.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

AST includes both forms, all described interactive fields, validation constraints, and submit actions with success/failure behaviors; no missing or extraneous interactive elements found.

**Missing:** none

**Phantoms:** none

---
