# Semantic Critique — Moodleteacher

Generated: 2026-06-09T11:47:58.694984Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Assignment Creation

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Assignment_Creation_Form.fields.Availability.fields.Enable_Toggles
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Maximum_Number_Of_Uploaded_Files
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Maximum_Submission_Size
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Accepted_File_Types
- Assignment_Creation_Form.fields.Submission_Settings.fields.Attempts_Reopened_Settings
- Assignment_Creation_Form.fields.Group_Submission_Settings.fields.Grouping_Selection
- Assignment_Creation_Form.fields.Tags
- Assignment_Creation_Form.fields.Competencies

**Phantoms (hallucinations):**

- Assignment_Creation_Form.fields.Availability.fields.Enable_Toggles (not mentioned in description)
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Maximum_Number_Of_Uploaded_Files (not mentioned in description)
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Maximum_Submission_Size (not mentioned in description)
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Accepted_File_Types (not mentioned in description)
- Assignment_Creation_Form.fields.Submission_Settings.fields.Attempts_Reopened_Settings (not mentioned in description)
- Assignment_Creation_Form.fields.Group_Submission_Settings.fields.Grouping_Selection (not mentioned in description)
- Assignment_Creation_Form.fields.Tags (not mentioned in description)
- Assignment_Creation_Form.fields.Competencies (not mentioned in description)

**Fixes applied:**

- Add 'Enable_Toggles' field under 'Availability' with type 'checkbox'.
- Add 'Maximum_Number_Of_Uploaded_Files' field under 'File_Submissions' with type 'number'.
- Add 'Maximum_Submission_Size' field under 'File_Submissions' with type 'number'.
- Add 'Accepted_File_Types' field under 'File_Submissions' with type 'unspecified'.
- Add 'Attempts_Reopened_Settings' field under 'Submission_Settings' with type 'unspecified'.
- Add 'Grouping_Selection' field under 'Group_Submission_Settings' with type 'unspecified'.
- Add 'Tags' field under 'Tags' with type 'unspecified'.
- Add 'Competencies' field under 'Competencies' with type 'unspecified'.

---

## Course Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms present in the AST.

**Missing:**

- Course_Settings_Form.fields.Course_End_Date.enabled_when
- Course_Settings_Form.fields.Groups
- Course_Settings_Form.fields.Tags

**Phantoms (hallucinations):**

- Course_Settings_Form.fields.Layout_Controls (not explicitly mentioned in description)
- Course_Settings_Form.fields.Appearance_Settings (not explicitly mentioned in description)
- Course_Settings_Form.fields.Completion_Tracking (not explicitly mentioned in description)

**Fixes applied:**

- Add Course_End_Date.enabled_when to specify the toggle condition.
- Add Groups field to Course_Settings_Form.fields.
- Add Tags field to Course_Settings_Form.fields.

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Participants_Page.fields.Enrolled_Users_Scope_Dropdown
- Participants_Table.bulk_actions[0].options[0] (Enroll action not explicitly mentioned)
- Participants_Table.bulk_actions[0].options[1] (Remove action not explicitly mentioned)
- Participants_Table.bulk_actions[0].options[2] (Message action not explicitly mentioned)

**Phantoms (hallucinations):**

- Participants_Table.columns[3] (Email address not specified in description)
- Participants_Table.columns[4] (Roles not specified in description)
- Participants_Table.columns[5] (Groups not specified in description)
- Participants_Table.columns[6] (Last access to course not specified in description)
- Participants_Table.columns[7] (Status not specified in description)

**Fixes applied:**

- Add 'Enrolled_Users_Scope_Dropdown' to 'Participants_Page.fields'
- Remove 'Email address', 'Roles', 'Groups', 'Last access to course', and 'Status' from 'Participants_Table.columns' as they are passive display fields.
- Clarify bulk actions in 'Participants_Table.bulk_actions[0].options' to match description.

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Gradebook — Grader Report

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected interactive elements and contains phantoms.

**Missing:**

- Grader_Report.row_actions[0].fields (missing per-cell three-dot menu for editing individual grade entries)
- Grader_Report.columns[0].action_menu.options[0] (missing per-column action menu for each column header)
- Grader_Report.edit_mode.enabled (missing toggle for Edit mode)

**Phantoms (hallucinations):**

- Grader_Report.row_actions[0] (Edit Grade Entry action not explicitly mentioned in description)
- Grader_Report.overall_average_row.type (unspecified type not mentioned in description)

**Fixes applied:**

- Add per-cell three-dot menu for editing individual grade entries in Grader_Report.row_actions[0].fields
- Add per-column action menu for each column header in Grader_Report.columns[0].action_menu.options[0]
- Add toggle for Edit mode in Grader_Report.edit_mode.enabled

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms identified in the AST.

**Missing:**

- Profile_Page.fields.User_Details_Card.fields.Email_Address
- Profile_Page.fields.Miscellaneous_Card.fields.Blog_Entries_Links
- Profile_Page.fields.Miscellaneous_Card.fields.Forum_Posts_Links
- Profile_Page.fields.Miscellaneous_Card.fields.Forum_Discussions_Links
- Profile_Page.fields.Miscellaneous_Card.fields.Learning_Plans_Links

**Phantoms (hallucinations):**

- Profile_Page.fields.Profile_Initials_Icon (not explicitly mentioned in description)
- Profile_Page.fields.Profile_Description (optional but not detailed in description)

**Fixes applied:**

- Add Email_Address field to User_Details_Card.
- Add Blog_Entries_Links, Forum_Posts_Links, Forum_Discussions_Links, and Learning_Plans_Links fields to Miscellaneous_Card.

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents the interactive element and its behavior as described.

**Missing:** none

**Phantoms:** none

---
