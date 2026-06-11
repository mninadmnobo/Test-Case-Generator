# Workflow Critique — Moodleteacher

Generated: 2026-06-10T21:11:04.554655Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing the required form component and its actions.

**Missing workflows:**

- No workflow for form: action=Log in

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for form: action=Log in

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list contains phantom workflows as the AST has no components defined.

**Missing workflows:** none

**Phantom workflows:**

- WF-001 terminal_action=New event not found in any AST node
- WF-002 terminal_action=Full calendar not found in any AST node
- WF-003 terminal_action=Import or export calendars not found in any AST node

**Fixes applied:**

- Remove phantom workflows WF-001, WF-002, WF-003

---

## Dashboard — Edit Mode

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST has no defined components.

**Missing workflows:**

- No workflows for any interactive components as the AST is empty

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for interactive components based on the description

---

## My Courses

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST has no defined components.

**Missing workflows:**

- No workflows for the status dropdown actions
- No workflows for the search field actions
- No workflows for the sort dropdown actions
- No workflows for the layout dropdown actions

**Phantom workflows:** none

**Fixes applied:**

- Define workflows for the status dropdown actions
- Define workflows for the search field actions
- Define workflows for the sort dropdown actions
- Define workflows for the layout dropdown actions

---

## Course Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the interactive components defined in the description.

---

## Course Edit Mode and Activity Chooser

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing workflows for actions that should be present based on the description.

**Missing workflows:**

- No workflow for adding a subsection action

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for adding a subsection

---

## Assignment Creation

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required components as the AST is empty.

**Missing workflows:**

- No workflows found for required actions in the assignment creation form.

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the assignment creation form actions.

---

## Course Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty while the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for the Course Settings form actions.

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing critical components as the AST has no defined components.

**Missing workflows:**

- No workflows found for any actions as the AST is empty.

**Phantom workflows:** none

**Fixes applied:**

- Define components in the AST to match the actions in the workflows.

---

## Assignment — Teacher View

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing required workflows for the interactive components described in the functional description.

**Missing workflows:**

- No workflows for the components described in the functional description, as the AST has no components defined.

**Phantom workflows:** none

**Fixes applied:**

- Define the necessary components in the AST to match the description and regenerate workflows.

---

## Assignment Submissions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty and the module has interactive components.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for interactive components as defined in the description.

---

## Gradebook — Grader Report

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty, and the module clearly has actions.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Regenerate workflows to include actions for the module.

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list contains phantom workflows as the AST has no defined components.

**Missing workflows:** none

**Phantom workflows:**

- WF-001 terminal_action=Edit profile not found in any AST node
- WF-002 terminal_action=Data retention summary not found in any AST node
- WF-003 terminal_action=Course profile link not found in any AST node
- WF-004 terminal_action=Blog entry link not found in any AST node
- WF-005 terminal_action=Browser sessions not found in any AST node
- WF-006 terminal_action=First and Last access not found in any AST node
- WF-007 terminal_action=Message not found in any AST node

**Fixes applied:**

- Remove phantom workflows WF-001, WF-002, WF-003, WF-004, WF-005, WF-006, WF-007

---

## Profile Edit

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is empty, indicating no interactive components are defined, yet workflows exist.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Remove workflows WF-001 and WF-002 due to absence of corresponding AST components

---

## Logout

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty but the module has an interactive component for logging out.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for the Log out action

---
