# Workflow Critique — Parabank

Generated: 2026-06-09T10:57:12.120438Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action and the Forgot Password link, with matching on_success behaviors and no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the Registration_Form submit action 'Register' with matching on_success; no missing workflows, phantoms, or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the only interactive item described (clickable but unimplemented Account Number) and there are no forms, state-bound actions, or declared row/bulk actions missing workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action for both Account_Type branches; no missing workflows, no phantom terminal actions, and on_success values match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: both Transfer_Type branches (internal and external) are covered, terminal_action matches the form's submit action, conditional branches reference existing fields, and on_success matches the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the Bill_Payment_Form submit action 'Pay', matches the AST on_success, there are no phantom workflows, and no missing conditional/state/table actions.

**Missing workflows:** none

**Phantom workflows:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action for each Loan_Type condition; no missing workflows, phantoms, wrong conditional branches, or empty on_success values detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the form submit action ('Update Profile'), there are no phantom terminal actions, conditional branches and on_success match the AST, and no required workflows are missing.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

All form submit actions have matching workflows, no phantom terminal actions were found, conditional branches reference AST preconditions/fields, and on_success values match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and match the AST submit actions; no phantom workflows, missing state/row actions, or incorrect conditional branches were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and consistent with the AST: form submit actions and conditional variants are covered, no phantom terminal_actions, and on_success texts match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the Change Password form submit action with matching on_success; no missing workflows, phantoms, or conditional errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and match the AST submit actions; no phantoms or conditional-branch issues detected.

**Missing workflows:** none

**Phantom workflows:** none

---
