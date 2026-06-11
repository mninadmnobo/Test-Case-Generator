# Workflow Critique — Moodleteacher

Generated: 2026-06-10T21:24:41.674635Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference UI elements and fields that are not present in the provided AST (unknown conditional fields and missing form/component definitions), so the workflow list cannot be validated as correct.

**Missing workflows:**

- AST missing form node for the login page: no form with submit_actions containing 'Log in' (required for workflows WF-001 and WF-002).
- Workflow WF-001 conditional_branch references unknown fields: Username, Password
- Workflow WF-002 conditional_branch references unknown fields: Username, Password, Credentials

**Phantom workflows:** none

**Fixes applied:**

- Add a form component in the AST for the login page with fields 'Username' and 'Password' and submit_actions: ['Log in'] so workflows WF-001 and WF-002 can be validated.
- Ensure the AST records the field names used in conditional_branch (Username, Password, Credentials) under the form's field definitions or visible_when/required_when; or update WF-001 and WF-002 to use conditional_branch conditions that reference actual AST field names or set conditional_branch to null.
- If 'Access as a guest' (WF-003) and 'Cookies notice' (WF-004) are interactive actions, add them to the AST (e.g., as button actions) so their terminal_action entries can be validated; otherwise remove those workflows.
- If the 'Lost password?' link is intended to be actionable (even if currently disabled), add it to the AST (or explicitly mark it as disabled) so any related workflow can be generated or omitted.

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the interactive elements described (timeline filters, search, calendar filters/navigation, event creation, and links); no missing or phantom workflows were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

All terminal actions in the workflow list map to actions described in the module description; no missing workflows, phantoms, or conditional/on_success issues were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all interactive actions described (click course name, star, remove, status filter, search, sort, layout) and contains no phantoms or incorrect conditional branches.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

All described interactive actions (toggle section chevron, 'Collapse all' link, and opening an activity/resource) are covered by workflows; no missing workflows or phantom actions detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The workflow list matches the described actions; no missing workflows or phantoms were detected against the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

All required terminal actions from the module description/AST are represented by workflows; no missing workflows, phantoms, or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference form fields and conditional branches that do not exist in the provided AST (which contains no components); regenerate with a matching AST or remove invalid conditions.

**Missing workflows:**

- Form node for Course Settings with submit_actions ['Save and display', 'Cancel'] is not present in AST but workflows assume a form submit — no matching form component found.
- Field definitions for conditional_branch references are missing in AST: Format, EndDate_Enabled, Group_Mode — workflows reference these but the AST has no fields or visible_when/required_when entries.

**Phantom workflows:** none

**Fixes applied:**

- Add a form component to the AST (e.g., component path 'form:CourseSettings') with submit_actions ['Save and display', 'Cancel'] and explicit fields for Course format, EndDate toggle (EndDate_Enabled), and Group mode (Group_Mode), including any visible_when/required_when rules. Then regenerate workflows so conditional_branch expressions reference those AST field names.
- If the AST intentionally omits field/state details, regenerate the workflows without conditional_branch constraints (or with conditional_branch values that match existing AST state keys/visible_when fields).
- Ensure every workflow terminal_action maps to a submit_actions/available_actions/row_actions/bulk_actions entry in the AST or appears explicitly as an action verb in the module description; update AST or workflows accordingly.

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Some workflows contain conditional_branch expressions that reference fields/states not present in the AST, so the workflow list must be regenerated.

**Missing workflows:**

- Workflow WF-004 conditional_branch references unknown field/state: 'Filter_Type == Alphabetical' (no 'Filter_Type' in AST visible_when/required_when or state keys).
- Workflow WF-005 conditional_branch references unknown field/state: 'Activation_Method == Name_Link' (no 'Activation_Method' in AST visible_when/required_when or state keys).
- Workflow WF-006 conditional_branch references unknown field/state: 'Activation_Method == Row_Action_Menu' (no 'Activation_Method' in AST visible_when/required_when or state keys).

**Phantom workflows:** none

**Fixes applied:**

- Fix WF-004: remove or correct conditional_branch 'Filter_Type == Alphabetical' — reference an actual visible_when/required_when field or a real state key from the AST, or set conditional_branch to null if no condition applies.
- Fix WF-005: remove or correct conditional_branch 'Activation_Method == Name_Link' — reference an actual visible_when/required_when field or a real state key from the AST, or set conditional_branch to null if no condition applies.
- Fix WF-006: remove or correct conditional_branch 'Activation_Method == Row_Action_Menu' — reference an actual visible_when/required_when field or a real state key from the AST, or set conditional_branch to null if no condition applies.

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

Workflows correspond to actions described on the page; no missing workflows or phantoms detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the actions described in the module text and no terminal actions appear to be phantom relative to the description; no missing form/state/data-table workflows detected from the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

Workflows align with the description and no AST-defined interactive nodes require additional workflows; no phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

All terminal actions in the workflow list match actions described in the module and there are no missing or phantom workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile Edit

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflows reference conditional_branch fields that do not exist in the provided AST (which has no components), so the list must be regenerated with a matching AST or corrected conditions.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add an Edit profile form component to the AST (e.g., components.forms['edit_profile']) with submit_actions ['Update profile','Cancel'] so the terminal actions in the workflows are tied to a form node.
- Represent the conditional fields used by the workflows in the AST: add boolean/form field entries for New_Picture_Uploaded, Upload_Constraints_Satisfied, and Required_Fields_Valid (under the form's visible_when/required_when or as explicit fields) so conditional_branch expressions reference real AST field names.
- Or, instead of changing the AST, update the workflows to remove or replace conditional_branch expressions that reference non-existent fields (WF-001, WF-002, WF-003, WF-004) so they reference actual field/state names present in the AST.
- If the description implies additional interactive controls (e.g., 'Expand all'), include those controls in the AST if they must influence workflows; otherwise omit them from conditional logic.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: the single 'Log out' workflow matches the description and there are no AST components requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---
