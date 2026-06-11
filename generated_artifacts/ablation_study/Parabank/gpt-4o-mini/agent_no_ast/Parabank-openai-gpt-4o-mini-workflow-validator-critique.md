# Workflow Critique — Parabank

Generated: 2026-06-10T20:09:51.907383Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST is empty.

**Missing workflows:**

- No workflows for form submit_action: action=Sign In

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for the login form submit action.

---

## Register

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST has no defined components.

**Missing workflows:**

- No workflows for form submit_action: action=Register

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for the missing form submit_action: action=Register

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the dashboard actions.

---

## Open New Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing the required components as the AST is empty.

**Missing workflows:**

- No workflows found for any interactive components in the AST.

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for the missing interactive components in the AST.

---

## Transfer Funds

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is empty, indicating no interactive components, yet workflows exist.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Remove all workflows since the AST has no components.

---

## Payments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is empty, indicating no interactive components are defined, yet workflows exist.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Remove all workflows since the AST has no components

---

## Request Loan

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing the required interactive components as the AST contains no components.

**Missing workflows:**

- No workflows for interactive loan type cards: Personal, Auto, Home

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for loan type cards: Personal, Auto, Home

---

## Update Contact Info

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty as there are no components in the AST.

**Missing workflows:**

- No workflows when module clearly has actions.

**Phantom workflows:** none

**Fixes applied:**

- Add form component with submit_actions for 'Update Profile'.

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST does not contain any components, indicating a critical failure as workflows exist.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add components to the AST to reflect the forms and actions described in the functional description.

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the trade funds form and recurring investment plan form actions.

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is empty, indicating a critical failure as there are interactive components described.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add components to the AST to reflect the forms and actions described in the functional description.

---

## Security Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing as the AST contains no components, indicating a critical failure.

**Missing workflows:**

- No workflows found for the form actions in the Security Settings page.

**Phantom workflows:** none

**Fixes applied:**

- Add the necessary form components to the AST to match the workflows.

---

## Support Center

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is empty, indicating no interactive components are defined, yet workflows exist.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Remove workflows WF-001 and WF-002 due to absence of corresponding AST components.

---
