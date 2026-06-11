# Workflow Critique — Mifos

Generated: 2026-06-10T19:35:27.066729Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows match the actions present in the description and there are no missing or phantom workflows relative to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

Workflows match the described actions (Search Activity and Dashboard) and no missing form/state/table workflows or phantom actions were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: no missing workflows or phantom terminal actions were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

Workflows match the described search interactions (selecting results for Clients, Groups, Loans, Savings and the no-results case); no missing or phantom workflows detected against the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and no phantom workflows or invalid conditional branches were detected relative to the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

No missing workflows or phantom terminal actions found; the provided workflows cover the actions described in the description and there are no invalid conditional branches or empty on_success values requiring changes.

**Missing workflows:** none

**Phantom workflows:** none

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

All workflows correspond to actions described in the functional description; no missing required workflows or phantom terminal actions were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

Workflows match the provided AST and description; no missing workflows or phantom terminal actions were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows use conditional_branch references that do not exist in the (empty) AST, and multiple terminal actions for Fixed/Recurring deposit creation are not present in the AST or explicitly in the description — regeneration required.

**Missing workflows:**

- WF-003 conditional_branch references 'Accounting' which is not defined in AST visible_when/required_when or as a state key
- WF-004 conditional_branch references 'Enforce_Minimum_Required_Balance' which is not defined in AST visible_when/required_when or as a state key
- WF-005 conditional_branch references 'Is_Overdraft_Allowed' which is not defined in AST visible_when/required_when or as a state key
- WF-006 conditional_branch references 'Enable_Withhold_Tax' which is not defined in AST visible_when/required_when or as a state key
- WF-007 conditional_branch references 'Enable_Dormancy_Tracking' which is not defined in AST visible_when/required_when or as a state key
- WF-008 conditional_branch references 'Apply_Withdrawal_Fee_For_Transfers' which is not defined in AST visible_when/required_when or as a state key
- WF-010 conditional_branch references 'Pre_Mature_Closure_Applicable' which is not defined in AST visible_when/required_when or as a state key
- WF-011 conditional_branch references 'Accounting' which is not defined in AST visible_when/required_when or as a state key
- WF-013 conditional_branch references 'Is_Mandatory_Deposit' which is not defined in AST visible_when/required_when or as a state key
- WF-014 conditional_branch references 'Allow_Withdrawal' which is not defined in AST visible_when/required_when or as a state key
- WF-015 conditional_branch references 'Adjust_Advance_Towards_Future_Payments' which is not defined in AST visible_when/required_when or as a state key
- WF-016 conditional_branch references 'Accounting' which is not defined in AST visible_when/required_when or as a state key

**Phantom workflows:**

- WF-009 terminal_action='Create Fixed Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-010 terminal_action='Create Fixed Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-011 terminal_action='Create Fixed Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-012 terminal_action='Create Recurring Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-013 terminal_action='Create Recurring Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-014 terminal_action='Create Recurring Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-015 terminal_action='Create Recurring Deposit Product' not found in any AST node and not explicitly present in the description text
- WF-016 terminal_action='Create Recurring Deposit Product' not found in any AST node and not explicitly present in the description text

**Fixes applied:**

- Add the missing form/wizard and data_table components to the AST (Savings, Fixed Deposit, Recurring Deposit) including their submit_actions and row/bulk actions so workflows can be validated; specifically include 'Create Savings Product', 'Create Fixed Deposit Product', 'Create Recurring Deposit Product', 'Click Name link', and 'Add Charge' where applicable.
- Define the conditional fields referenced by workflows in the AST (e.g., Accounting, Enforce_Minimum_Required_Balance, Is_Overdraft_Allowed, Enable_Withhold_Tax, Enable_Dormancy_Tracking, Apply_Withdrawal_Fee_For_Transfers, Pre_Mature_Closure_Applicable, Is_Mandatory_Deposit, Allow_Withdrawal, Adjust_Advance_Towards_Future_Payments) under visible_when or required_when or as state keys in state_bound_action_bar, or remove/adjust the conditional_branch expressions in the workflows.
- If Fixed/Recurring product creation actions are intended, make those actions explicit in the description or add submit_actions in the AST for those product types; otherwise remove the phantom workflows for Create Fixed Deposit Product and Create Recurring Deposit Product.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional branches (Accounting) that do not exist in the provided AST and the AST is empty while the description defines many interactive components — regenerate with a populated AST and correct condition references.

**Missing workflows:**

- WF-001 conditional_branch references unknown field 'Accounting' (Accounting == None) — 'Accounting' is not defined in AST visible_when/required_when/state keys
- WF-002 conditional_branch references unknown field 'Accounting' (Accounting == Cash-based) — 'Accounting' is not defined in AST visible_when/required_when/state keys

**Phantom workflows:** none

**Fixes applied:**

- Add the 'Accounting' field/state to the AST (e.g., Step 7 radio field 'Accounting' with values 'None' and 'Cash-based') so conditional_branch values 'Accounting == None' and 'Accounting == Cash-based' are valid; or remove/adjust WF-001 and WF-002 conditional_branch to match actual AST field/state names.
- Populate the AST with components described on the page before regenerating workflows: include the Share Products data_table with row_actions (e.g., 'Click Product Name', 'Edit', 'Delete') and any bulk_actions; include the 7-step wizard/form with submit_actions (e.g., 'Create Share Product') and visible_when/required_when rules for fields (notably the Cash-based GL mapping fields visible_when Accounting == Cash-based), the Market Price row add/remove actions, and the Charges search-and-add interface.
- After updating the AST, regenerate workflows ensuring: one workflow per form.submit_action per unique visible_when/required_when condition, one workflow per data_table row_action and bulk_action, and that any conditional_branch expressions reference field names or state keys present in the AST (e.g., 'Accounting').

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Retry because multiple workflows contain conditional branches that reference a field/state not present in the provided AST.

**Missing workflows:**

- Workflow WF-005 conditional_branch 'Charge_Applies_To == Loan' references unknown field 'Charge_Applies_To' (field not present in AST)
- Workflow WF-006 conditional_branch 'Charge_Applies_To == Savings Account' references unknown field 'Charge_Applies_To' (field not present in AST)
- Workflow WF-007 conditional_branch 'Charge_Applies_To == Client' references unknown field 'Charge_Applies_To' (field not present in AST)
- Workflow WF-008 conditional_branch 'Charge_Applies_To == Shares' references unknown field 'Charge_Applies_To' (field not present in AST)

**Phantom workflows:** none

**Fixes applied:**

- For each workflow WF-005 through WF-008 either remove or correct the conditional_branch values to reference a real field/state present in the AST, or regenerate the workflows after updating the AST to include the Create Charge form with a field named 'Charge_Applies_To' (and any visible_when/required_when conditions).
- If the AST should include the Charges data_table and the Create Charge form (per the description), update/regenerate the AST to include: a data_table with row_actions ['Click Name','Edit','Delete'] and a form node for Create Charge containing the 'Charge_Applies_To' field and a submit_actions entry for 'Submit'; then regenerate workflows so conditions and terminal_action values map to AST nodes.
- Alternatively, if the AST is intentionally empty, remove workflows that reference form-field conditions (WF-005..WF-008) because their conditional_branch references cannot be validated against the AST.

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

All workflows correspond to actions present in the AST/description; no missing workflows, phantoms, or incorrect conditional branches were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

One or more workflows contain conditional_branch expressions that reference fields or state keys not present in the AST; regenerate after aligning workflows with the AST (or update the AST to include the referenced fields).

**Missing workflows:**

- Conditional branch references unknown field 'Maximum_Age_Days' in workflow WF-002 (Create Delinquency Range with Maximum_Age_Days provided) — no such field under any form visible_when/required_when in AST.
- Conditional branch references unknown field 'Maximum_Age_Days' in workflow WF-003 (Create Delinquency Range with Maximum_Age_Days left blank) — no such field under any form visible_when/required_when in AST.
- Conditional branch references unknown field 'Ranges_Count' in workflow WF-005 (Create Delinquency Bucket with a single associated range) — no such field or state key in AST.
- Conditional branch references unknown field 'Ranges_Count' in workflow WF-006 (Create Delinquency Bucket with multiple associated ranges) — no such field or state key in AST.

**Phantom workflows:** none

**Fixes applied:**

- Update the AST to include the Create Delinquency Range form and its fields: Classification (required), Minimum_Age_Days (required), Maximum_Age_Days (optional). Add a submit_actions entry that includes 'Create Delinquency Range'. Then regenerate workflows so conditional_branch references 'Maximum_Age_Days' map to the AST field.
- Update the AST to include the Delinquency Ranges data_table with a row_action 'Click Classification link' (or add that action to row_actions). Then regenerate workflows or remove phantom/unsupported actions accordingly.
- Update the AST to include the Create Delinquency Bucket form with fields: Bucket Name (required) and a repeatable/child structure for associated ranges. Include a submit_actions entry 'Create Delinquency Bucket'. Then regenerate workflows so any conditional_branch referencing 'Ranges_Count' maps to an actual AST field (e.g., a computed Ranges_Count or a visible_when expression).
- Update the AST to include the Delinquency Buckets data_table with a row_action 'Click Bucket Name link'. Then regenerate workflows to match the AST row_actions.
- Alternatively, if you cannot modify the AST, remove or replace the conditional_branch expressions in WF-002, WF-003, WF-005, and WF-006 with conditions/fields that exist in the AST, or make them unconditional workflows (conditional_branch: null), then regenerate the workflow list.

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Many workflows reference conditional branches (states or fields) that do not exist in the provided AST (which is empty); regenerate after adding the form/state/data_table components and proper field/state keys.

**Missing workflows:**

- No form node for Loan Application wizard: submit action 'Submit' with visible_when/required_when conditions for Added_Charge and Collateral_Added (WF-001..WF-004 variants missing a matching form definition)
- No state_bound_action_bar: state='Submitted and Pending Approval' with actions 'Approve' (WF-005), 'Reject' (WF-006), 'Withdraw' (WF-007), 'Delete' (WF-008)
- No state_bound_action_bar: state='Approved' with actions 'Disburse' (WF-009..WF-013 variants) and 'Undo Approval' (WF-014)
- No state_bound_action_bar: state='Active' with actions 'Make Repayment' (WF-015..WF-018 variants), 'Waive Interest' (WF-019), 'Write Off' (WF-020), 'Close' (WF-021), 'Reschedule' (WF-022), 'Prepay Loan' (WF-023), 'Foreclosure' (WF-024), 'Charge Off' (WF-025), 'Assign Loan Officer' (WF-026)
- No data_table node for Transactions with row action 'Undo' (WF-027)
- Conditional branch fields referenced but not defined in AST: Added_Charge, Collateral_Added, Payment_Type, Disburse_To, and entity_state values ('Submitted and Pending Approval', 'Approved', 'Active') — these field/state keys must appear in AST visible_when/required_when or in a state_bound_action_bar

**Phantom workflows:** none

**Fixes applied:**

- Add a 'Loan Application' wizard form component to the AST with a Submit submit_action and explicit visible_when/required_when definitions (or boolean fields) for Added_Charge and Collateral_Added so WF-001..WF-004 map to real form conditions.
- Add a state_bound_action_bar component to the AST that enumerates the loan states (at least: 'Submitted and Pending Approval', 'Approved', 'Active', plus others as needed) and lists available_actions for each state (e.g., Submitted and Pending Approval -> [Approve, Reject, Withdraw, Delete]; Approved -> [Disburse, Undo Approval]; Active -> [Make Repayment, Waive Interest, Write Off, Close, Reschedule, Prepay Loan, Foreclosure, Charge Off, Assign Loan Officer]). Regenerate workflows so conditional_branch uses the exact state keys from this component.
- Define payment-related fields in the AST (e.g., Payment_Type with allowed values Cash, Check, Mobile Money, Bank Transfer; Disburse_To with values Savings/Client) so Disburse workflows (WF-009..WF-013) and repayment variants (WF-015..WF-018) can reference real field names.
- Add a Transactions data_table component to the AST with a row_actions array including 'Undo' so WF-027 maps to a real row action.
- Ensure conditional_branch expressions in regenerated workflows use the exact field/state identifiers as defined in the AST (match capitalization and spacing or use normalized keys), or remove conditions if they are not represented in the AST.
- After updating the AST as above, regenerate the workflows so each form submit_action, each state × available_action pair, and each data_table row/bulk action has a corresponding workflow, and so no conditional_branch references undefined fields or states.

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

All workflows correspond to actions described in the module description and there are no missing form/state/table workflows or phantom terminal actions given the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

All workflows correspond to actions described in the module description, there are no phantom terminal actions, and no AST-driven combinations were required by the provided (empty) AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

No missing or phantom workflows detected against the provided AST and description; workflows cover the actions described (create, approve, activate, deposit, premature close, close on maturity) and have concrete on_success texts.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The provided workflows do not align with the (empty) AST and the page description: the AST lacks the Create GL Account form and data_table components described, so workflows for form submit (success and validation error) and explicit data_table row/bulk actions are missing or mismatched.

**Missing workflows:**

- AST missing form node for Create GL Account: no workflow corresponds to a form submit action (e.g., 'Save'/'Create'/'Submit') and the duplicate-GL-Code validation error path is not represented.
- AST missing data_table node for Chart of Accounts: no workflows map to data_table row_actions (e.g., 'View Details' or 'Open Detail') that should correspond to clicking an account name to open detail view.
- AST has no explicit mapping for parent-account-dependent behavior: missing workflow(s) for selecting Parent Account constrained to header accounts of the same Account Type (conditional variation by Account Type).
- AST lacks explicit form submit/validation actions for Edit from detail view: no workflow covers form submission for edits including success and potential validation failure.
- AST lacks an explicit action mapping for Delete that ties to the detail-view/delete confirmation flow (e.g., delete confirmation submit).

**Phantom workflows:** none

**Fixes applied:**

- Add a 'form' component to the AST for the Create GL Account form with submit_actions (e.g., ['Save','Create','Submit']) and validation rules (GL Code must be unique). Regenerate workflows to include: (a) opening the create form, (b) submitting the form successfully (terminal_action should match a submit_action like 'Save' not just the create-button label), and (c) submitting the form with a duplicate GL Code validation error (error path).
- Add a 'data_table' component to the AST for the Chart of Accounts with row_actions including at least ['View Details'/'Open Detail' (Click Account Name), 'Edit', 'Delete']. Regenerate workflows so there is one workflow per row_action (View/Open Detail, Edit, Delete).
- Model Parent Account dependency in the AST (visible_when or required_when tied to Account Type) and regenerate workflows to cover the conditional branch where Parent Account dropdown options change by Account Type (one workflow per distinct Account Type condition if it affects behavior).
- Add explicit 'form' or 'submit_actions' entries in the AST for Edit and Delete confirmation if they are forms/actions, and regenerate workflows to include both successful and error/confirmation paths (e.g., Edit submit success, Edit validation error if applicable, Delete confirmation submit).
- Ensure terminal_action strings in workflows exactly match the action names defined in the AST (e.g., use 'Save' or 'Create' for form submit actions rather than the button label '+ Create GL Account' which opens the form). Regenerate after aligning names so there are no phantom or mismatched actions.

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference form fields and conditions that do not exist in the provided AST (empty components), so conditional branches are invalid and the model must be regenerated with matching AST nodes or workflows updated.

**Missing workflows:**

- WF-001 conditional_branch references unknown fields: Total_Debits, Total_Credits, Office, Currency, Transaction_Date (no matching form/fields in AST)
- WF-002 conditional_branch references unknown fields: Total_Debits, Total_Credits (no matching form/fields in AST)
- WF-003 conditional_branch references unknown fields: Office, Currency, Transaction_Date (no matching form/fields in AST)
- WF-004 conditional_branch references unknown fields: Closing_Date, Office (no matching form/fields in AST)
- WF-005 conditional_branch references unknown fields: Closing_Date, Office (no matching form/fields in AST)

**Phantom workflows:** none

**Fixes applied:**

- Add a form component in the AST for the 'Add Journal Entry' flow with submit_actions including 'Add Journal Entry' and define fields referenced by workflows: Office, Currency, Transaction_Date, Total_Debits, Total_Credits (or else remove/adjust conditional_branch expressions to use fields present in the AST).
- Add a form component in the AST for the 'Create Closure' flow with submit_actions including 'Create Closure' and define fields referenced by workflows: Office, Closing_Date (or else remove/adjust conditional_branch expressions to use fields present in the AST).
- If the AST intentionally omits form field names, update each workflow's conditional_branch to reference only fields or state keys that exist in the AST, or remove conditional_branch entirely for those workflows.
- Ensure the AST includes data_table components or row/bulk actions if you expect workflows that end at table actions, so workflows can be validated against row_actions[]/bulk_actions[].

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

All workflows correspond to actions mentioned in the description and there are no missing or phantom workflows against the provided AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

Workflows match the description and there are no missing or phantom workflows relative to the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

Workflows appear complete and correct relative to the provided description and AST (no missing or phantom workflows detected).

**Missing workflows:** none

**Phantom workflows:** none

---

## Employees

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The Structural Model (AST) is empty while the description and workflows reference multiple interactive components (Employees data table, Create Employee form, Staff Detail Edit) — regenerate the AST and workflows.

**Missing workflows:**

- AST missing data_table 'Employees' with expected row_actions: 'Name (clickable link)' (View/Details) and any row actions for editing; no corresponding data_table node or row_actions[] entries found in AST.
- AST missing form 'Create Employee' with submit_actions (e.g., 'Create' or 'Save'); no form node or submit_actions[] found in AST — workflows must include a terminal_action for the form submit and one per visible_when/required_when condition if present.
- AST missing Staff Detail/available_actions (e.g., 'Edit') or a state_bound_action_bar for employee detail actions; no available_actions[] found in AST for the Edit action referenced by workflows.

**Phantom workflows:** none

**Fixes applied:**

- Regenerate the Structural Model so it includes: a data_table component named 'Employees' with row_actions including the Name link (View/Details) and any Edit/View actions; a form component named 'Create Employee' with explicit submit_actions (e.g., 'Create'/'Save') and any visible_when/required_when rules; and the Staff Detail component with available_actions including 'Edit'.
- After AST regeneration, regenerate workflows to (a) include one workflow per form submit_action (and per visible/required condition combinations), (b) include one workflow per data_table row_action and bulk_action, and (c) include one workflow per available_action/state in any state_bound_action_bar.
- Remove or update any workflow terminal_action that cannot be matched to the regenerated AST nodes or to explicit actions in the description.

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

All workflows map to actions found in the description/AST; no missing workflows, phantoms, wrong conditional branches, or empty on_success values detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Structural model (AST) contains no components but the workflows reference forms, a data table, and permission checkboxes — regenerate with an AST that includes the described components and actions so workflows can be validated.

**Missing workflows:**

- AST does not contain a data_table for Users page; missing workflow binding for data_table row_action: Click Username (link)
- AST does not contain a form for Create User; missing form.submit_action: Submit Create User form
- AST does not contain a form for Create Role; missing form.submit_action: Submit Create Role form
- AST does not contain a permissions page component with checkbox actions; missing permission checkbox actions: Enable/Disable Permission Checkbox

**Phantom workflows:** none

**Fixes applied:**

- Add a data_table component for the Users page in the AST (e.g., components.UsersPage.users_table) and include 'Click Username (link)' in row_actions so WF-001 can be matched to that row action.
- Add a Create User form node to the AST (e.g., components.CreateUserForm) and include 'Submit Create User form' in submit_actions; include field definitions and any visible_when/required_when conditions so form workflows can be enumerated.
- Add a Create Role form node to the AST (e.g., components.CreateRoleForm) and include 'Submit Create Role form' in submit_actions; include the subsequent permissions page node.
- Add a permissions matrix component to the AST (e.g., components.RolePermissionsPage) and include checkbox actions (row_actions or submit_actions) for enabling/disabling permissions so WF-004 can be matched.
- If any of the workflows are not intended to be supported, remove them from the workflow list; otherwise regenerate workflows after the AST is populated with the described components and actions.

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers opening the parameters form, running the report, and exporting to Excel/CSV/PDF; no missing workflows or phantoms were detected against the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows contain conditional_branch expressions that reference fields or states not present in the provided AST (which is empty), so the workflow set cannot be validated as correct.

**Missing workflows:**

- Conditional branch in WF-001 references unknown fields: Transfer_Amount and Available_Balance (no corresponding form fields in AST).
- Conditional branch in WF-002 references unknown fields: Transfer_Amount and Available_Balance (no corresponding form fields in AST).
- Conditional branch in WF-005 references unknown state key: Status == Disabled (no state_bound_action_bar or state keys in AST).
- Conditional branch in WF-006 references unknown state key: Status == Active (no state_bound_action_bar or state keys in AST).
- AST is empty but description indicates interactive components (Account Transfers form, Standing Instructions data_table); corresponding AST nodes are missing so workflows cannot be fully validated.

**Phantom workflows:** none

**Fixes applied:**

- Add an Account Transfers form node to the AST with fields including Transfer_Amount and Available_Balance (or rename conditional_branch expressions to match the actual AST field names) so WF-001 and WF-002 conditional branches validate.
- Add a Standing Instructions data_table and/or a state_bound_action_bar for the listing with a Status state that defines keys Active and Disabled (or change WF-005 and WF-006 conditional_branch to use existing AST state keys) so those workflows validate.
- Populate the AST with submit_actions and row/bulk actions (Submit, + Create Standing Instruction, Enable, Disable, Delete) so phantoms and missing-action checks can be accurately performed; then regenerate workflows.
- If the AST intentionally omits these components, remove or null out conditional_branch expressions that reference non-existent fields/states from the workflows and ensure terminal_action values match AST node actions or the exact verbs in the description.

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

All workflows map to actions described in the input; no missing workflows, phantoms, or invalid conditional branches were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Reject — many workflows reference a conditional field 'Entity_Type' that does not exist in the AST (bulk import workflows), and there are phantom terminal actions (e.g., Save Working Days, Save Currencies) not present in the AST or description.

**Missing workflows:**

- Workflow WF-006 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Clients) — field not found in AST visible_when/required_when or state keys
- Workflow WF-007 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Clients) — field not found in AST visible_when/required_when or state keys
- Workflow WF-008 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Groups) — field not found in AST visible_when/required_when or state keys
- Workflow WF-009 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Groups) — field not found in AST visible_when/required_when or state keys
- Workflow WF-010 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Centers) — field not found in AST visible_when/required_when or state keys
- Workflow WF-011 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Centers) — field not found in AST visible_when/required_when or state keys
- Workflow WF-012 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Offices) — field not found in AST visible_when/required_when or state keys
- Workflow WF-013 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Offices) — field not found in AST visible_when/required_when or state keys
- Workflow WF-014 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Staff) — field not found in AST visible_when/required_when or state keys
- Workflow WF-015 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Staff) — field not found in AST visible_when/required_when or state keys
- Workflow WF-016 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Users) — field not found in AST visible_when/required_when or state keys
- Workflow WF-017 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Users) — field not found in AST visible_when/required_when or state keys
- Workflow WF-018 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Loans) — field not found in AST visible_when/required_when or state keys
- Workflow WF-019 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Loans) — field not found in AST visible_when/required_when or state keys
- Workflow WF-020 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Savings) — field not found in AST visible_when/required_when or state keys
- Workflow WF-021 conditional_branch references unknown field 'Entity_Type' (Entity_Type == Savings) — field not found in AST visible_when/required_when or state keys

**Phantom workflows:**

- WF-002 terminal_action='Save Working Days' not found in AST and not explicitly present in the description text
- WF-003 terminal_action='Save Currencies' not found in AST and not explicitly present in the description text

**Fixes applied:**

- Remove or correct the conditional_branch usages referencing 'Entity_Type' for bulk import workflows (WF-006 through WF-021). Either (a) update the AST to include a field named 'Entity_Type' (with the listed entity options), or (b) regenerate these workflows with no conditional_branch or with a condition that matches an actual field/state present in the AST.
- Replace or clarify the terminal_action for WF-002 and WF-003: if the UI uses explicit 'Save' buttons, ensure the AST includes those form submit_actions named 'Save Working Days' and 'Save Currencies'; otherwise regenerate workflows using the actual terminal action names present in the AST or description.
- Ensure the AST is populated with the interactive components implied by the description (forms for Holidays, Working Days, Currencies, Funds, Payment Types, and a Bulk Import component with entity selection and Download/Upload actions), then regenerate workflows so conditional branches and terminal_action values align with the AST.
- Alternatively, if the AST is correct and minimal, regenerate the workflow list to remove any workflows that reference non-existent fields/states and to only include terminal_action values explicitly present in the AST or description.

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Some workflows have conditional branches that reference fields/states not present in the AST, and at least one terminal_action appears to be a phantom; regenerate after correcting the AST or workflows.

**Missing workflows:**

- Wrong conditional branch: WF-013 references condition 'maker-checker == true AND Processing_Result == Pending' but AST has no fields/visible_when/required_when entries or state_bound_action_bar states named 'maker-checker' or 'Processing_Result'.
- Wrong conditional branch: WF-014 references condition 'maker-checker == true AND Processing_Result == Pending' but AST has no fields/visible_when/required_when entries or state_bound_action_bar states named 'maker-checker' or 'Processing_Result'.

**Phantom workflows:**

- WF-005 terminal_action='Save Configuration' not found in AST nodes and not explicitly present in the description text as a distinct action (no form submit_actions include 'Save Configuration').

**Fixes applied:**

- Add the referenced condition fields/states to the AST (e.g., include a 'maker-checker' boolean field in relevant form components or a state_bound_action_bar with a 'Processing_Result' state containing 'Pending', 'Approved', 'Rejected') so WF-013 and WF-014 conditional_branch expressions refer to real AST elements.
- Or remove/adjust the conditional_branch in WF-013 and WF-014 to use field/state names that exist in the AST.
- Either add a form/submit action named 'Save Configuration' to the AST (submit_actions including 'Save Configuration') or rename the WF-005 terminal_action to match an existing AST action/explicit action verb in the description (for example 'Edit Configuration Value' + corresponding submit action).
- Regenerate the workflow list after updating the AST so all terminal_action values map to AST actions and all conditional_branch expressions reference actual AST fields/states.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: no missing workflows, phantoms, or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---
