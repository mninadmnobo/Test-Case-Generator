# Workflow Critique — Swaglab

Generated: 2026-06-09T09:19:08.601334Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the form's submit action and all constraint-based outcomes (empty fields, authentication failure, locked out user); no phantom workflows or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Product Inventory

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows contain phantom actions for the dropdown and several conditional_branch references that don't exist in the AST; the Open Product Detail action is combined across two distinct triggers and should be split.

**Missing workflows:**

- Products_Table.row_action 'Open Product Detail' requires distinct workflows per trigger ('Name' and 'Image'); only one combined workflow (WF-005) is present.
- Wrong conditional_branch field: workflows WF-001, WF-002, WF-003, WF-004 reference 'Sort_Option' which is not defined in the AST under visible_when/required_when or as a state key.
- Wrong conditional_branch field: workflows WF-006 and WF-007 reference 'in_cart' in conditional_branch, but 'in_cart' appears only in state_changes (not defined as a visible/required field or a state key in a state_bound_action_bar).

**Phantom workflows:**

- WF-001 terminal_action='Sort_Dropdown' not found as an action in AST (no matching submit_actions/available_actions/row_actions/bulk_actions or exact action verb in description).
- WF-002 terminal_action='Sort_Dropdown' not found as an action in AST (no matching submit_actions/available_actions/row_actions/bulk_actions or exact action verb in description).
- WF-003 terminal_action='Sort_Dropdown' not found as an action in AST (no matching submit_actions/available_actions/row_actions/bulk_actions or exact action verb in description).
- WF-004 terminal_action='Sort_Dropdown' not found as an action in AST (no matching submit_actions/available_actions/row_actions/bulk_actions or exact action verb in description).

**Fixes applied:**

- Replace phantom terminal_action 'Sort_Dropdown' (WF-001..WF-004) with explicit actions that match the AST (e.g., create terminal_action names like 'Select Sort Option: Name: A–Z' or add a corresponding action entry to the AST for the dropdown).
- Correct conditional_branch references for sort workflows: either define a field in the AST (e.g., selected_sort_option under the Sort_Dropdown component or as visible_when/required_when) named exactly as used in workflows, or remove conditional_branch and make the selected option explicit in the workflow name. Ensure option text matches AST exactly (use en-dash '–' and no CRLF).
- Fix WF-003 and WF-004 conditional_branch strings to match AST option text exactly ('Price: Low–High' and 'Price: High–Low' using the en-dash) if keeping conditional branches.
- For WF-006 and WF-007, either remove conditional_branch and rely on the row action preconditions (product in cart / product not in cart), or add an explicit state definition (state_bound_action_bar) or a visible field in the AST for 'in_cart' so 'in_cart == true/false' is a valid condition.
- Split WF-005 into two separate workflows: one for opening Product Detail via clicking the product Name, and one for opening via clicking the Image, so each distinct user action has its own workflow entry.

---

## Product Detail

**Verdict:** yes  
**Forced ship:** no  

All state-bound actions and navigation actions have matching workflows with correct conditional branches and on_success values; no missing or phantom workflows found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Shopping Cart

**Verdict:** yes  
**Forced ship:** no  

All actions in the AST have matching workflows, no phantom terminal actions, conditional branches, or empty on_success values were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Checkout - Information

**Verdict:** yes  
**Forced ship:** no  

All form submit actions have matching workflows, there are no phantom terminal actions, conditional branches and on_success values align with the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Checkout - Overview

**Verdict:** yes  
**Forced ship:** no  

All wizard submit actions have corresponding workflows with correct on_success texts; no missing workflows or phantoms detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Checkout - Confirmation

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the Confirmation page action: the 'Back Home' terminal action is present, not phantom, has correct on_success, and there are no conditional branches or other components requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the Logout button action, matches the AST element and on_success, and there are no missing or phantom workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Reset App State

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the module's interactive action (Reset App State) with matching on_success; no missing workflows or phantoms detected.

**Missing workflows:** none

**Phantom workflows:** none

---
