# Workflow Critique — Moodleteacher

Generated: 2026-06-09T11:47:58.703585Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Login_Form: action=Log in

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Login_Form: action=Log in

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form actions in the Timeline block.

**Missing workflows:**

- No workflow for Timeline_Block: action=Time_Range

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Timeline_Block: action=Time_Range

---

## Dashboard — Edit Mode

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions related to existing blocks.

**Missing workflows:**

- No workflow for existing_blocks: action=Configure
- No workflow for existing_blocks: action=Move
- No workflow for existing_blocks: action=Delete

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for existing_blocks: action=Configure
- Add workflows for existing_blocks: action=Move
- Add workflows for existing_blocks: action=Delete

---

## My Courses

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There is a phantom workflow for terminal_action 'Course_Name' which is not found in any AST node.

**Missing workflows:** none

**Phantom workflows:**

- WF-003 terminal_action=Course_Name not found in any AST node

**Fixes applied:**

- Remove phantom workflow WF-003

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly match the actions described in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions and phantom workflows detected.

**Missing workflows:**

- No workflow for state_bound_action_bar: state=Activity Chooser, action=Add

**Phantom workflows:**

- WF-006 terminal_action=Add not found in any AST node
- WF-007 terminal_action=Add not found in any AST node

**Fixes applied:**

- Add workflow for state_bound_action_bar: state=Activity Chooser, action=Add
- Remove phantom workflows WF-006 and WF-007

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

All required workflows for form submit actions are present and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined for the Course Settings form.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions and phantom workflows detected.

**Missing workflows:**

- No workflow for Participants_Table: state=Active, action=View Profile
- No workflow for Participants_Table: state=Active, action=Edit Role
- No workflow for Participants_Table: state=Active, action=Send Message
- No workflow for Participants_Table: state=Active, action=With selected users…

**Phantom workflows:**

- WF-011 terminal_action=Message not found in any AST node

**Fixes applied:**

- Add workflows for missing state-bound actions in Participants_Table.
- Remove phantom workflow WF-011.

---

## Assignment — Teacher View

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the Grade button's submit action is missing.

**Missing workflows:**

- No workflow for button: action=Grade

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for button: action=Grade

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and correctly match the actions defined in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for actions in the Profile page AST.

**Missing workflows:**

- No workflow for Profile_Page: action=Edit_Profile_Link
- No workflow for Profile_Page: action=Data_Retention_Summary_Link
- No workflow for Profile_Page: action=Course_Profiles_Links
- No workflow for Profile_Page: action=Browser_Sessions_Link
- No workflow for Profile_Page: action=Grades_Overview_Link

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing actions: Edit_Profile_Link, Data_Retention_Summary_Link, Course_Profiles_Links, Browser_Sessions_Link, Grades_Overview_Link

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correct.

**Missing workflows:** none

**Phantom workflows:** none

---
