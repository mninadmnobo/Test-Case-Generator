# Workflow Critique — Moodlestudent

Generated: 2026-06-10T21:48:21.955744Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference form fields and component states that do not exist in the provided AST (missing 'login_form' and 'lost_password' definitions and other components), so the workflow list must be regenerated or the AST updated.

**Missing workflows:**

- No form node 'login_form' in AST but workflows reference submit_action 'Log in' (WF-001, WF-002) — missing form and its field definitions (username, password, credentials_valid).
- Conditional branch references undefined fields: 'login_form.username', 'login_form.password', 'login_form.credentials_valid' (used by WF-001 and WF-002).
- Conditional branch references undefined field 'lost_password.enabled' (used by WF-005) and AST has no 'lost_password' component or link definition.
- AST contains no components for the buttons/links referenced by WF-003 ('Access as a guest') and WF-004 ('Cookies notice').

**Phantom workflows:** none

**Fixes applied:**

- Add a form node 'login_form' to the AST with fields: username, password, credentials_valid and a submit_actions entry including 'Log in'; then regenerate workflows so conditional_branch expressions reference these AST fields exactly.
- Add a component or link node 'lost_password' with an 'enabled' property and an action 'Lost password?' in the AST, or remove WF-005 if the link should not be modeled; then regenerate workflows.
- Add button/link components for 'Access as a guest' and 'Cookies notice' in the AST (with their actions) or remove WF-003 and WF-004; then regenerate workflows.
- Alternatively, if the AST is intentionally minimal, remove or rewrite conditional_branch expressions in workflows to avoid referencing nonexistent AST fields (use only conditions that exist in the AST), then regenerate.

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Many workflows contain conditional_branch expressions that reference fields or states not defined in the AST (which is empty), so the workflow list must be regenerated after correcting the AST or the conditions.

**Missing workflows:**

- Conditional field 'timeline_items_in_range' referenced by workflows WF-001 and WF-002 not found in AST
- Conditional field 'search_results_count' referenced by workflows WF-004 and WF-005 not found in AST
- Conditional field 'course_has_events_in_month' referenced by workflows WF-006 and WF-007 not found in AST
- Conditional field 'target_month_has_events' referenced by workflows WF-009, WF-010, WF-011, and WF-012 not found in AST
- Conditional field 'Edit_Mode' referenced by workflows WF-016, WF-017, WF-018, WF-019, WF-020, and WF-021 not found in AST

**Phantom workflows:** none

**Fixes applied:**

- Add corresponding visible_when/required_when fields or state keys to the AST for 'timeline_items_in_range', or remove/replace the conditional_branch values in WF-001 and WF-002 to match fields actually defined in the AST.
- Add corresponding visible_when/required_when fields or state keys to the AST for 'search_results_count', or remove/replace the conditional_branch values in WF-004 and WF-005 to match fields actually defined in the AST.
- Add corresponding visible_when/required_when fields or state keys to the AST for 'course_has_events_in_month', or remove/replace the conditional_branch values in WF-006 and WF-007 to match fields actually defined in the AST.
- Add corresponding visible_when/required_when fields or state keys to the AST for 'target_month_has_events', or remove/replace the conditional_branch values in WF-009, WF-010, WF-011, and WF-012 to match fields actually defined in the AST.
- Add a state or flag for 'Edit_Mode' in the AST (e.g., part of a state_bound_action_bar or a visible_when on edit-only controls), or remove/replace the conditional_branch values in WF-016 through WF-021 to use real AST-defined conditions.
- Alternatively, populate the AST 'components' with nodes for the Timeline and Calendar blocks and the Edit-mode controls (including the explicit field/state names used in these workflows), then regenerate workflows so conditional_branch entries match the AST definitions.

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and map to actions described in the module text; no phantom workflows or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

Workflows match the actions present in the AST and description (no missing workflows, phantoms, or incorrect conditional branches detected).

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the described participant page interactions; no missing workflows, phantoms, or incorrect conditional branches were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Grades

**Verdict:** yes  
**Forced ship:** no  

All terminal actions correspond to verbs in the description, no AST nodes require additional workflows, and there are no missing or phantom workflows or conditional/on_success issues.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows use conditional_branch expressions that reference fields/states not present in the AST (AST is empty); regenerate with conditions that match the AST or update the AST to include those fields/states.

**Missing workflows:**

- Conditional branch references unknown field 'Assignment_Interface' used by workflows WF-001, WF-002, WF-003, WF-004, WF-005, WF-006
- Conditional branch references unknown field 'Submission_Status' used by workflows WF-007, WF-008
- Conditional branch references unknown field 'Due_Date' used by workflows WF-007, WF-008
- Conditional branch references unknown field 'Teacher_Permits_Resubmission' used by workflows WF-007, WF-008

**Phantom workflows:** none

**Fixes applied:**

- Define 'Assignment_Interface' in the AST (e.g., as form visible_when conditions or a config field) with possible values Online_Text, File_Upload, Both so WF-001..WF-006 conditional_branch expressions are valid; OR remove/clear the Assignment_Interface conditional_branch on those workflows.
- Define fields/states 'Submission_Status', 'Due_Date', and 'Teacher_Permits_Resubmission' in the AST (as visible_when/required_when fields or state keys in a state_bound_action_bar) so WF-007 and WF-008 conditional_branch expressions are valid; OR remove/replace those conditional_branch expressions.
- If these workflows correspond to a submission form, add a form component to the AST with submit_actions including 'Submit' and (if needed) an explicit 'Add submission' action, and include visibility conditions that match the conditional_branch values used by the workflows; then regenerate workflows to align exactly with the AST action names and condition keys.

---

## Activities

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the interactive actions described (expand/collapse sections and clicking activity names); no missing workflows or phantoms found against the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the interactive actions described (message, links, and profile form actions); no missing workflows or phantoms found based on the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: the single 'Log out' workflow matches the action mentioned in the description and the AST contains no interactive components requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---
