# Workflow Critique — Moodlestudent

Generated: 2026-06-10T21:40:06.883707Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing the required components from the AST, which is empty.

**Missing workflows:**

- No workflows for form submit_actions: action=Log in

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for the missing form actions

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the interactive components described in the functional description.

---

## My Courses

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing critical workflows for the interactive components described in the functional description.

**Missing workflows:**

- No workflow for state_bound_action_bar: action=Status dropdown
- No workflow for state_bound_action_bar: action=Search field
- No workflow for state_bound_action_bar: action=Sort dropdown
- No workflow for state_bound_action_bar: action=Layout dropdown

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for the status dropdown, search field, sort dropdown, and layout dropdown actions.

---

## Course Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

All workflows are phantoms as their terminal actions are not found in any AST node.

**Missing workflows:** none

**Phantom workflows:**

- WF-001 terminal_action=View not found in any AST node
- WF-002 terminal_action=Collapse all not found in any AST node
- WF-003 terminal_action=Access not found in any AST node

**Fixes applied:**

- Remove phantom workflows WF-001, WF-002, WF-003

---

## Participants

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required workflows for the interactive components described in the functional description.

**Missing workflows:**

- No workflow for data_table: action=View profile

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for data_table: action=View profile

---

## Grades

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the Grades page as it contains interactive components.

---

## Assignment

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty but the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the interactive components defined in the description.

---

## Activities

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the Activities page actions.

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST has no defined structure.

**Missing workflows:**

- No workflows defined for any interactive components in the AST.

**Phantom workflows:** none

**Fixes applied:**

- Define the components in the AST to match the actions in the workflows.

---

## Logout

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty but the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for the action 'Log out' since the AST has no components.

---
