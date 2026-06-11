# Workflow Critique — Parabank

Generated: 2026-06-10T20:20:34.160292Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference an 'Authentication' conditional/state that does not exist in the AST; regenerate workflows after aligning conditional branches with the AST (or update the AST to include the referenced form/state).

**Missing workflows:**

- WF-001: conditional_branch 'Authentication == Success' references 'Authentication' which is not defined in the AST (no state_bound_action_bar or visible/required field named 'Authentication').
- WF-002: conditional_branch 'Authentication == Failure' references 'Authentication' which is not defined in the AST (no state_bound_action_bar or visible/required field named 'Authentication').

**Phantom workflows:** none

**Fixes applied:**

- WF-001: Remove or correct the conditional_branch 'Authentication == Success' before regenerating; either (a) remove the conditional_branch (make workflow unconditional and base branching on form submit outcome), or (b) add a state_bound_action_bar or field named 'Authentication' with state 'Success' to the AST and then regenerate.
- WF-002: Remove or correct the conditional_branch 'Authentication == Failure' before regenerating; either (a) remove the conditional_branch, or (b) add a state_bound_action_bar or field named 'Authentication' with state 'Failure' to the AST and then regenerate.
- Update the AST to include the login form component: add a 'form' with fields Email/Username and Password (with the described validations), submit_actions including 'Sign In', and explicit on_success/on_error behaviors (Signed in successfully -> redirect to Accounts Overview; authentication failure -> show error and clear password). Then regenerate workflows so form submit outcomes map to concrete workflows.
- If 'Forgot Password?' should be a terminal action, add it to the AST (e.g., as a link/button component or as a form row_action) so its terminal_action is grounded in the AST before regenerating.

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The provided workflow matches the AST and description: the Register terminal_action appears in the description text, on_success reflects the described success behavior, and there are no missing workflows or phantoms relative to the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

The workflow list is acceptable: no missing workflows against the AST, no phantom terminal actions, and no incorrect conditional branches or empty on_success values.

**Missing workflows:** none

**Phantom workflows:** none

---

## Open New Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains no form/components, so every workflow's conditional_branch references fields or states that do not exist in the AST and must be regenerated after the AST is corrected.

**Missing workflows:**

- WF-001 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-002 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-003 conditional_branch references undefined fields: Account_Type, Deposit_Amount (AST has no form or those fields)
- WF-004 conditional_branch references undefined fields: Account_Type, Deposit_Amount (AST has no form or those fields)
- WF-005 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-006 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-007 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-008 conditional_branch references undefined fields: Account_Type, Deposit_Amount, Funding_Sufficient (AST has no form or those fields)
- WF-009 conditional_branch references undefined field: Account_Type (AST has no form or that field)
- WF-010 conditional_branch references undefined field: Deposit_Amount (AST has no form or that field)

**Phantom workflows:** none

**Fixes applied:**

- Add a form component to the AST for the account-opening page with fields and semantics that match the description: Account_Type (options: Checking, Savings), Deposit_Amount (numeric), Funding_Source (dropdown) and a derived/validated boolean Funding_Sufficient; include submit_actions: ['Open Account'] and any visible_when/required_when rules for fields. Then regenerate workflows so conditional_branch expressions reference those exact AST field names and the submit_action is matched to the form.
- Alternatively, if the AST is intentionally minimal, regenerate the workflows to remove or adjust conditional_branch expressions so they only reference fields/states present in the AST (or convert free-text conditions into AST-visible_when/required_when/state keys).

---

## Transfer Funds

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference a form submit action and conditional fields that are not present in the AST, so the workflow list must be regenerated against a complete AST.

**Missing workflows:**

- AST missing form with submit_actions containing 'Transfer' — workflows WF-001..WF-006 reference a Transfer submit action but no form node or submit_actions exist in AST.
- AST missing field/condition definitions referenced in conditional_branch expressions: Transfer_Type, Transfer_Amount_Valid, Sufficient_Funds, AccountNumbers_Match — these fields do not appear under any component's visible_when/required_when or as state keys.

**Phantom workflows:** none

**Fixes applied:**

- Add a form component to the AST for the transfer page and include 'Transfer' in its submit_actions (or rename workflows' terminal_action to match the actual submit_action in the AST).
- Define the conditional fields used in workflows in the AST (e.g., a Transfer_Type field with values 'My_ParaBank_Account' and 'External_Account'; Transfer_Amount_Valid; Sufficient_Funds; AccountNumbers_Match) under the form's visible_when/required_when or equivalent so conditional_branch expressions reference real fields.
- If the AST intentionally omits these fields, update the workflows to use only fields and actions that exist in the AST (or add state_bound_action_bar/data_table nodes if relevant).
- Ensure on_success texts match any concrete on_success values specified in the AST for the Transfer action when regenerating workflows.

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The single workflow for terminal_action 'Pay' is valid relative to the provided AST and description: no missing form/state/data-table workflows, no phantom actions, and on_success is concrete.

**Missing workflows:** none

**Phantom workflows:** none

---

## Request Loan

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

All workflows reference a terminal action and conditional fields that do not exist in the provided AST (AST has no components); terminal_action 'Request Loan' is a phantom for every workflow and conditional_branch references unknown fields, so the workflow set must be regenerated after fixing the AST or workflows.

**Missing workflows:**

- No AST form or component defines a submit/available/row/bulk action 'Request Loan' while 12 workflows use that terminal_action (WF-001..WF-012).
- Conditional branches reference fields or states that do not exist in the AST: Loan_Type, Loan_Amount, Down_Payment, Collateral_Account_Balance, Credit_Engine_Result.

**Phantom workflows:**

- WF-001 terminal_action=Request Loan not found in AST
- WF-002 terminal_action=Request Loan not found in AST
- WF-003 terminal_action=Request Loan not found in AST
- WF-004 terminal_action=Request Loan not found in AST
- WF-005 terminal_action=Request Loan not found in AST
- WF-006 terminal_action=Request Loan not found in AST
- WF-007 terminal_action=Request Loan not found in AST
- WF-008 terminal_action=Request Loan not found in AST
- WF-009 terminal_action=Request Loan not found in AST
- WF-010 terminal_action=Request Loan not found in AST
- WF-011 terminal_action=Request Loan not found in AST
- WF-012 terminal_action=Request Loan not found in AST

**Fixes applied:**

- Add the Loan request form/component(s) to the AST with a submit_actions[] entry that includes 'Request Loan' and declare the fields Loan_Type, Loan_Amount, Down_Payment, Collateral_Account_Balance, and Credit_Engine_Result (or equivalent state keys) so conditional_branch expressions can be validated (recommended).
- Or, if the AST is correct and uses a different action name, regenerate workflows so terminal_action values match an existing AST action verb instead of 'Request Loan' (update WF-001..WF-012 accordingly).
- Ensure each conditional_branch references real field names defined in the AST (e.g., under visible_when or required_when) or real state keys in state_bound_action_bar; update branches or AST field names to match.
- If some denial reasons are modeled as credit engine result values, add those result values (e.g., Approved, Denied_Insufficient_Credit) to the AST so workflows that branch on Credit_Engine_Result are valid.

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

Workflow list is consistent with the AST and description: no missing workflows, no phantom terminal actions, and conditional/on_success checks passed.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference form fields and conditional branches that do not exist in the provided AST (no form/state nodes), so the workflow set must be regenerated to match the AST or the AST must be updated.

**Missing workflows:**

- AST contains no form or state nodes but workflows reference form submit actions: 'Request Card' and 'Update Controls' — corresponding form nodes/submit_actions are missing from AST.
- WF-002 conditional_branch references nonexistent fields/states: 'Spending limit', 'Travel notice dates', 'Status transition' (no matching visible_when/required_when or state keys in AST).
- WF-003 conditional_branch references nonexistent field: 'Spending limit' (no matching visible_when/required_when in AST).
- WF-004 conditional_branch references nonexistent field: 'Travel notice dates' (no matching visible_when/required_when in AST).
- WF-005 conditional_branch references nonexistent field/state: 'Status transition' (no matching visible_when/required_when or state key in AST).

**Phantom workflows:** none

**Fixes applied:**

- Either update the AST to include form components for the two forms described (Card request form with submit_action 'Request Card' and Card controls form with submit_action 'Update Controls', including fields: Card Type, Account to Link, Shipping Address, Select Existing Card, New Spending Limit, Travel Notice, Card Status, plus any visible_when/required_when and validation rules), or regenerate workflows to remove/replace conditional_branch expressions that reference fields/states not present in the AST.
- When regenerating workflows, ensure each form submit_action in the AST has at least one workflow per submit action, and that any conditional_branch uses exact field names found in the AST's visible_when/required_when or exact state keys from any state_bound_action_bar.
- If the AST should model state-bound actions, add a state_bound_action_bar with explicit state keys and available_actions so a workflow can be produced for every state × action pair.

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains no components but the workflows reference form fields and conditional states that do not exist in the AST; conditional_branch references must match AST fields or the AST must be expanded — regenerate.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- WF-001 conditional_branch references fields not present in AST: Action, Fund_Symbol_Exists, Quantity, Buying_Power, Required_Buying_Power — either add these fields/visibility/validation definitions to the AST (e.g., a trade form with these fields and validations) or remove/adjust the conditional_branch in the workflow.
- WF-002 conditional_branch references fields not present in AST: Action, Fund_Symbol_Exists, Quantity, Share_Balance — add corresponding form field/state definitions to AST or update the workflow conditional_branch to match AST.
- WF-003 conditional_branch references field not present in AST: Fund_Symbol_Exists — add this validation field to the AST or remove/update the conditional_branch.
- WF-004 conditional_branch references field not present in AST: Quantity — add Quantity field/validation to AST or update the workflow.
- WF-005 conditional_branch references fields not present in AST: Action, Buying_Power, Required_Buying_Power — add these fields/validations to AST or update the workflow.
- WF-006 conditional_branch references fields not present in AST: Action, Share_Balance, Quantity — add these fields/validations to AST or update the workflow.
- WF-007 conditional_branch references fields not present in AST: Start_Date, Contribution_Amount, Minimum, Funding_Account_Balance — add a recurring plan form with these fields/validations to the AST or update the workflow.
- WF-008 conditional_branch references field not present in AST: Start_Date — add Start_Date field/validation to AST or update the workflow.
- WF-009 conditional_branch references fields not present in AST: Contribution_Amount, Minimum — add these fields/validations to AST or update the workflow.
- WF-010 conditional_branch references fields not present in AST: Funding_Account_Balance, Contribution_Amount — add these fields/validations to AST or update the workflow.
- General: The AST is empty but the description describes two forms (trade funds form and recurring investment plan form) and read-only portfolio snapshot — regenerate the AST to include these components (forms with submit_actions: 'Execute Trade' and 'Create Plan', fields, validations, and on_success messages) so workflows can be validated against concrete component definitions.

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows contain conditional_branch references to fields/states that do not exist in the AST (AST has no components), so the workflows must be regenerated or the AST augmented.

**Missing workflows:**

- Conditional branch references unknown field: Statement_Period (used by workflows WF-001 and WF-002)
- Conditional branch references unknown field: Paperless_OptIn (used by workflows WF-003 and WF-004)

**Phantom workflows:** none

**Fixes applied:**

- Add a form component for the Generate Statement form to the AST that defines the field Statement_Period (values: Month_And_Year, Custom_Date_Range), include 'Generate Statement' in its submit_actions, and set on_success to 'Statement generated successfully.'
- Add a form component for the E-Statement Preference form to the AST that defines the field Paperless_OptIn (boolean) and Email_Address, include 'Save Preference' in its submit_actions, and set on_success to 'e-Statement preference updated.'
- Alternatively, remove or correct the conditional_branch expressions in the workflows so they reference fields or states that exist in the AST (or leave conditional_branch null if not applicable) and then regenerate workflows.

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

No missing workflows or phantom terminal actions detected; the single workflow matches the described Change Password action and its success message.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: both described form submit actions are represented, no missing workflows or phantoms were detected, and no incorrect conditional branches or empty on_success values requiring correction.

**Missing workflows:** none

**Phantom workflows:** none

---
