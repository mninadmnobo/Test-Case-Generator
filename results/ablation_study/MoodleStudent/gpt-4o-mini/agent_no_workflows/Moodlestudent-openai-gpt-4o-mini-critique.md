# Semantic Critique — Moodlestudent

Generated: 2026-06-10T21:41:26.452168Z

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

## My Courses

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the course card visual representation and has phantoms related to the course card structure.

**Missing:**

- Course_Grid.fields.Course_Banner_Image
- Course_Grid.fields.Category_Name

**Phantoms (hallucinations):**

- Course_Grid.row_actions[0] (Star this course action not explicitly mentioned in description)
- Course_Grid.row_actions[1] (Remove from view action not explicitly mentioned in description)

**Fixes applied:**

- Add Course_Banner_Image field to Course_Grid.fields
- Add Category_Name field to Course_Grid.fields

---

## Course Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing expected elements and contains phantoms.

**Missing:**

- Course_Sections.sections[0].section_name

**Phantoms (hallucinations):**

- Course_Sections.sections[0].actions[0] (Collapse all action is not explicitly mentioned in the description)

**Fixes applied:**

- Add a section_name field to Course_Sections.sections[0] with the appropriate value.
- Remove the Collapse all action from Course_Sections.sections[0].actions[0] as it is not explicitly mentioned.

---

## Participants

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the Select attribute dropdown and has a phantom for the View Profile action.

**Missing:**

- Filter_System.fields.Select_Attribute_Dropdown

**Phantoms (hallucinations):**

- Participants_Table.row_actions[0] (View Profile action not explicitly mentioned in description)

**Fixes applied:**

- Add a Select attribute dropdown to Filter_System.fields
- Remove the View Profile action from Participants_Table.row_actions

---

## Grades

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Assignment

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Submission_Status_Section.fields.Submission_Status (specific submission status messages are not defined)
- Submission_Status_Section.fields.Grading_Status (specific grading status messages are not defined)
- Submission_Status_Section.fields.Time_Remaining (specific time remaining field is not defined)
- Submission_Status_Section.fields.Last_Modified (specific last modified field is not defined)
- Submission_Status_Section.fields.Submission_Comments (specific submission comments field is not defined)

**Phantoms (hallucinations):**

- Submission_Form.fields.Online_Text_Editor (not explicitly mentioned in the description)
- Submission_Form.fields.File_Upload_Area (not explicitly mentioned in the description)

**Fixes applied:**

- Define specific submission status messages in Submission_Status_Section.fields.Submission_Status.
- Define specific grading status messages in Submission_Status_Section.fields.Grading_Status.
- Define specific time remaining field in Submission_Status_Section.fields.Time_Remaining.
- Define specific last modified field in Submission_Status_Section.fields.Last_Modified.
- Define specific submission comments field in Submission_Status_Section.fields.Submission_Comments.
- Remove Online_Text_Editor and File_Upload_Area from Submission_Form.fields as they are phantoms.

---

## Activities

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
