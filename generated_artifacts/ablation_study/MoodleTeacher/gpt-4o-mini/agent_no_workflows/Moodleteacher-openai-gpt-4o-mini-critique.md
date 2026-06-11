# Semantic Critique — Moodleteacher

Generated: 2026-06-10T21:13:47.256916Z

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

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

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

The AST accurately reflects the interactive elements described with no missing items or phantoms.

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

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items: 1 critical (creation form for activity), and there are phantoms present.

**Missing:**

- Activity_Chooser_Modal.fields.Activity_Resource_Tiles.tiles[0].actions[1] (Creation form for selected activity not present)

**Phantoms (hallucinations):**

- Course_Page.bulk_actions[0] (Bulk Actions button not explicitly mentioned in description)

**Fixes applied:**

- Add a creation form for each activity tile in Activity_Chooser_Modal.fields.Activity_Resource_Tiles.tiles
- Remove the Bulk Actions button from Course_Page.bulk_actions

---

## Assignment Creation

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several missing items and phantoms.

**Missing:**

- Assignment_Creation_Form.fields.Availability.fields.Enable_Toggles.fields.Allow_Submissions_From_Toggle
- Assignment_Creation_Form.fields.Availability.fields.Enable_Toggles.fields.Due_Date_Toggle
- Assignment_Creation_Form.fields.Availability.fields.Enable_Toggles.fields.Cut_Off_Date_Toggle
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Max_Uploaded_Files
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Max_Submission_Size
- Assignment_Creation_Form.fields.Submission_Types.fields.File_Submissions.fields.Accepted_File_Types
- Assignment_Creation_Form.fields.Group_Submission_Settings.fields.Grouping_Selection

**Phantoms (hallucinations):**

- Assignment_Creation_Form.fields.Tags (tag entry field not explicitly mentioned in description)
- Assignment_Creation_Form.fields.Competencies (course competency linking controls not explicitly mentioned in description)

**Fixes applied:**

- Add missing fields for Enable Toggles in Availability panel
- Add missing fields for File Submissions in Submission Types panel
- Add missing Grouping Selection field in Group Submission Settings panel
- Remove phantom fields for Tags and Competencies

---

## Course Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Course_Settings_Form.fields.Course_End_Date.enabled_when

**Phantoms (hallucinations):**

- Course_Settings_Form.fields.Course_Visibility (not mentioned in description)
- Course_Settings_Form.fields.Course_Format.fields.Layout_Controls (not mentioned in description)
- Course_Settings_Form.fields.Course_Format.fields.Appearance_Settings (not mentioned in description)
- Course_Settings_Form.fields.Groups.fields.Group_Mode (not mentioned in description)
- Course_Settings_Form.fields.Groups.fields.Grouping (not mentioned in description)

**Fixes applied:**

- Remove Course_Settings_Form.fields.Course_Visibility
- Remove Course_Settings_Form.fields.Course_Format.fields.Layout_Controls
- Remove Course_Settings_Form.fields.Course_Format.fields.Appearance_Settings
- Remove Course_Settings_Form.fields.Groups.fields.Group_Mode
- Remove Course_Settings_Form.fields.Groups.fields.Grouping

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms identified in the AST.

**Missing:**

- Participants_Table.row_actions[0] (three-dot action menu options not present)
- Participants_Table.bulk_actions[0].options[0] (options for bulk actions not defined)

**Phantoms (hallucinations):**

- Participants_Table.row_actions[0] (view profile, edit role, send a message options not in description)
- Participants_Table.bulk_actions[0] (With selected users… dropdown options not defined)

**Fixes applied:**

- Define row_actions in Participants_Table with options for view profile, edit role, and send a message.
- Define bulk_actions options in Participants_Table for the With selected users… dropdown.

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Assignment Submissions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required interactive elements and contains phantoms.

**Missing:**

- Submissions_Table.fields.Student_Identity.type (should specify 'link' as required)
- Submissions_Table.fields.Submission_Status.type (should specify 'select' as required)
- Submissions_Table.fields.Grading_Status.type (should specify 'select' as required)
- Submissions_Table.row_actions[1].enabled_when (should specify condition explicitly)

**Phantoms (hallucinations):**

- Submissions_Table.row_actions[1] (Quick Grading action not explicitly mentioned in description)

**Fixes applied:**

- Submissions_Table.fields.Student_Identity.type should be set to 'link' and required to true
- Submissions_Table.fields.Submission_Status.type should be set to 'select' and required to true
- Submissions_Table.fields.Grading_Status.type should be set to 'select' and required to true
- Submissions_Table.row_actions[1].enabled_when should be removed or clarified

---

## Gradebook — Grader Report

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected interactive elements and contains phantoms.

**Missing:**

- Grader_Report.filter_controls.fields.User_Search
- Grader_Report.filter_controls.fields.Group_Filter
- Grader_Report.columns.Grade_Columns.actions[0].action_name

**Phantoms (hallucinations):**

- Grader_Report.overall_average_row (display field not in description)
- Grader_Report.edit_mode.fields.Grade_Cells (unspecified type not in description)

**Fixes applied:**

- Add 'User_Search' field under 'Grader_Report.filter_controls.fields' with type 'search'.
- Add 'Group_Filter' field under 'Grader_Report.filter_controls.fields' with type 'dropdown'.
- Rename 'Grader_Report.columns.Grade_Columns.actions[0]' to match the description's action name.

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Login_Activity_Card.fields.First_Access (exact dates and relative time indicators not included)
- Login_Activity_Card.fields.Last_Access (exact dates and relative time indicators not included)

**Phantoms (hallucinations):**

- User_Details_Card.fields.Visibility_Note (not mentioned in description)
- User_Details_Card.fields.Timezone (not mentioned in description)
- Course_Details_Card.fields.Course_Profiles_Links (not mentioned in description)

**Fixes applied:**

- Remove User_Details_Card.fields.Visibility_Note
- Remove User_Details_Card.fields.Timezone
- Remove Course_Details_Card.fields.Course_Profiles_Links
- Add Login_Activity_Card.fields.First_Access with exact dates and relative time indicators
- Add Login_Activity_Card.fields.Last_Access with exact dates and relative time indicators

---

## Profile Edit

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Edit_Profile_Form.fields.General.fields.Email_Address.required
- Edit_Profile_Form.fields.User_Picture.fields.Current_Picture

**Phantoms (hallucinations):**

- Edit_Profile_Form.fields.User_Picture.fields.Current_Picture (not mentioned in description)

**Fixes applied:**

- Add required: true to Edit_Profile_Form.fields.General.fields.Email_Address
- Remove Edit_Profile_Form.fields.User_Picture.fields.Current_Picture

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents the interactive element and its behavior as described.

**Missing:** none

**Phantoms:** none

---
