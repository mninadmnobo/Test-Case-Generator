# Semantic Critique — Moodleteacher

Generated: 2026-06-10T21:31:04.864511Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements (Username, Password, Log in, Lost password? disabled, Access as a guest, Cookies notice) and the described submission behaviors, with no extraneous items.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST accurately includes all interactive elements described (timeline filters/search/empty state; calendar filters, navigation, new event button, and links) with no extraneous items.

**Missing:** none

**Phantoms:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements (Edit Mode toggle; Reset page to default; + Add a block and its Add Block page listing all block types plus Cancel; per-block move handle and three-dot options menu with Configure/Move/Delete) and their Edit-mode visibility and persistence behaviors.

**Missing:** none

**Phantoms:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements from the description (status/search/sort/layout controls, course link navigation, and per-card three-dot menu actions) with no extra or missing interactive items.

**Missing:** none

**Phantoms:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

AST correctly models the interactive elements (navigation tab bar container, Collapse all link, collapsible section chevrons, and clickable activity/resource names) with appropriate action consequences and conditional visibility for section items.

**Missing:** none

**Phantoms:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

AST accurately models the Edit mode toggle, per-section and per-activity inline actions/menus, bulk actions toolbar, Add controls (activity/subsection), and the Activity Chooser modal with filter, search, tiles, favorite toggle, and Add/Cancel actions.

**Missing:** none

**Phantoms:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

AST accurately models the form panels, fields, conditionals, and actions; only minor omissions (Activity Chooser trigger and explicit rich-text type for Description) remain.

**Missing:**

- Activity_Chooser.Assignment_selection (the initial selection action that opens the Assignment Creation form is not represented)
- Assignment_Creation_Form.panels[General].fields.Description (should be explicitly type: rich_text / rich text editor)

**Phantoms:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

AST matches the description; all interactive elements are present and organized correctly, with only two minor inferred items flagged.

**Missing:** none

**Phantoms (hallucinations):**

- Course_Settings_Form.panels[0].fields.Course_End_Date.constraints[1] ("must be after Course_Start_Date" constraint is an inferred validation not explicitly stated in the description)
- Course_Settings_Form.panels[5].fields.Grouping.visible_when (visibility conditional on Group_Mode is inferred; description did not explicitly state the grouping dropdown is conditional)

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements from the description; only minor inferred items are present that do not block use.

**Missing:** none

**Phantoms (hallucinations):**

- components.Enrol_Users_Dialog.submit_actions[1] (Cancel button not mentioned in the description)
- components.Participants_Table.row_actions[1].on_trigger (explicitly states 'opens Edit Role dialog' — the description only listed an 'edit role' action without specifying a dialog)

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the Grade button, the grading interface, and the tab bar with the five named tabs; the grading summary metrics are read-only and their omission is acceptable.

**Missing:** none

**Phantoms:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (search/filter controls, quick-grading toggle, student profile link, online preview, file/feedback file links, inline editable Final Grade enabled by quick grading, and row action to open grading) with no critical omissions.

**Missing:** none

**Phantoms:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (report selector, search/group filters, edit-mode toggle, per-column settings action, per-cell edit action, inline editing and Save changes with validation) with no significant missing items or unsupported phantoms.

**Missing:** none

**Phantoms:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models all interactive elements named in the description (Message button, Edit profile link, Data retention link, repeating course profile links, miscellaneous and reports links) and includes the Login Activity card with no interactive fields as expected.

**Missing:** none

**Phantoms:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

AST is acceptable; only minor missing field-type detail and unspecified additional-name fields are noted.

**Missing:**

- Edit_Profile_Form.sections[0].fields.Description.type (expected 'rich_text' editor type)
- Edit_Profile_Form.sections[2].fields (Additional_Names: expected one or more optional alternative name fields for alternative name formats)

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST correctly models the single interactive element (Log out button) and its outcome; a single inferred precondition was added but is minor.

**Missing:** none

**Phantoms (hallucinations):**

- components.Log_Out.preconditions[0] ("user must be logged in")

---
