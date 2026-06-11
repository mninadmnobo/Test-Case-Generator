# Semantic Critique — Moodlestudent

Generated: 2026-06-10T21:53:47.304064Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements (Username, Password, Log in submit, disabled Lost password link, Access as a guest button, Cookies notice button) and the described success/failure behaviors.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST covers all interactive elements from the description; only minor inferred config pages were added but they are reasonable and non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- components.Timeline_Configuration_Page (configuration page not explicitly named in description)
- components.Calendar_Configuration_Page (configuration page not explicitly named in description)

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (filter controls, search, layout, sortable control, course link navigation, and card actions) with no significant missing or phantom items.

**Missing:** none

**Phantoms:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models the interactive elements described: navigation tab bar (empty tabs object since none named), repeating collapsible sections with per-section toggle, activity/resource links, and the 'Collapse all' link; no unsupported or missing interactive items detected.

**Missing:** none

**Phantoms:** none

---

## Participants

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements described; only minor inferred items are present.

**Missing:** none

**Phantoms (hallucinations):**

- Participants_Table.sortable_columns[1] ("First name" - inferred separate column; description only specified "First/Last name" as sortable)
- Participants_Table.sortable_columns[2] ("Last name" - inferred separate column; description only specified "First/Last name" as sortable)

---

## Grades

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the required aggregation/footer row and a clear mapping for the Grade item (course name) group header and does contains a minor phantom action name for the toggle; regenerate with the aggregation row and clearer header mapping.

**Missing:**

- Grades_Page.aggregation_row (AGGREGATION Course total footer row displaying cumulative grade across weighted items)
- Grades_Page.grouping.group_header.field_name (explicit field representing the 'Grade item' course-name header)
- Grades_Page.report_type (source indicated as 'User report' per description)

**Phantoms (hallucinations):**

- Grades_Page.grouping.group_header.toggle_action.action_name ('Toggle' label is not specified in the description)

**Fixes applied:**

- Add an aggregation/footer row at Grades_Page.aggregation_row with label 'AGGREGATION Course total' and fields showing cumulative values for Calculated weight, Grade (cumulative), Percentage (cumulative), and Contribution to course total; position it as the table footer and include a note: 'displays the cumulative grade across all weighted items'.
- Add Grades_Page.grouping.group_header.field_name and set it to 'Grade item (course name)' or include an explicit field object: Grades_Page.grouping.group_header.field = { "name": "Grade item", "content": "course name (collapsible header)" } so the header maps to the 'Grade item' column.
- Add Grades_Page.report_type = 'User report' (or Grades_Page.data_source = 'User report') to reflect that this view is the user's own grades via a User report.
- Replace or generalize Grades_Page.grouping.group_header.toggle_action.action_name 'Toggle' with a non-labeled action descriptor, e.g. Grades_Page.grouping.group_header.toggle_action = { "type": "expand_collapse" } (remove the literal 'Toggle' label which is not specified in the description).
- Explicitly indicate indentation of graded activities under the header by adding Grades_Page.grouping.item_rows.indentation = 'indented under header' or an equivalent property to make the nested structure explicit.

---

## Assignment

**Verdict:** yes  
**Forced ship:** no  

AST correctly covers the interactive elements (add/edit/view submission, conditional form fields, submit action, and state-bound actions) with only minor inferred items.

**Missing:** none

**Phantoms (hallucinations):**

- components.Submission_Action_Bar.states.Graded.available_actions[1] (View feedback action not explicitly named in description; description only says feedback appears on the page)
- components.Submission_Action_Bar.states.Submitted for grading.available_actions[1].preconditions[2] ("submission not graded" precondition is not stated in the description)

---

## Activities

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements (collapsible sections, default states, assignments table with clickable Name) with only minor inferred properties.

**Missing:** none

**Phantoms (hallucinations):**

- Activities_Page.components.Additional_Activity_Sections.item_fields.collapsed_by_default (inferred field; description did not specify a configurable 'collapsed_by_default' field for additional sections)
- Activities_Page.components.Additional_Activity_Sections.item_fields.toggle_control (inferred field; description only said sections are expandable via an arrow but did not define a per-item toggle_control field)

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described (buttons, links, form with collapsible panels, fields, and submit actions); only a minor inferred action is present.

**Missing:** none

**Phantoms (hallucinations):**

- Profile_Page.elements.Message_Button.on_success (opens message composer)

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST correctly models the single interactive element (Log out) and its effects; the only minor inferred item is a precondition.

**Missing:** none

**Phantoms (hallucinations):**

- components.Logout_Button.preconditions[0] (user must be logged in)

---
