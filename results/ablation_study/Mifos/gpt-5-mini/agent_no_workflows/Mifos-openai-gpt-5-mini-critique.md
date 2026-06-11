# Semantic Critique — Mifos

Generated: 2026-06-10T19:53:17.696986Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only a small inferred navigation target for the Forgot Password link was added but it's a minor phantom.

**Missing:** none

**Phantoms (hallucinations):**

- Login_Form.links[0].on_click (navigates to Password Recovery)

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (Search Activity input and Dashboard button) and the precondition; no missing or extraneous interactive items found.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (Dashboard button, Search Activity, office selection implied by 'selected office', Client Trends chart with legends, and two summary cards); only a minor inferred property (legend_toggleable) is present.

**Missing:** none

**Phantoms (hallucinations):**

- Dashboard_Page.components.Client_Trends_Chart.legend_toggleable (legend toggle behavior not specified in description)

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (search icon, search input, dropdown results grouped by entity type, selection navigation, no-results message, partial/case-insensitive matching) with only a minor inferred property.

**Missing:** none

**Phantoms (hallucinations):**

- components.Search_Results_Dropdown.groups.[].item_fields.Select_Result.interaction_area (row) — 'row' interaction area is an implementation detail not specified in the description

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (clients table, search, status filter, import/create buttons, bulk import actions, create-client wizard steps and fields, client detail state-bound actions, and tabs/sub-tabs) with no significant missing or phantom interactive items.

**Missing:** none

**Phantoms:** none

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described (groups table and actions, create-group form and Add Clients interface, bulk import panels and history, detail page actions and tabs, and collection sheet feature) with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures all interactive elements (centers table with link and top actions, Create Center form fields and submit, bulk import template/download and file upload, center detail action bar and tabs, and collection sheet repeating groups for batch entry).

**Missing:** none

**Phantoms:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the interactive elements in the description (filter bar, data table with clickable Name, create button, 6-step wizard with specified fields and step-6 conditional GL fields, charge search/add, and product detail with Edit), with no missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements, steps, fields, options and explicit conditionals described for Savings, Fixed Deposit, and Recurring Deposit products; no missing items or extraneous phantoms found.

**Missing:** none

**Phantoms:** none

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements from the description (data table, create button, 7-step wizard with required fields, repeating market price rows, charges search-add, conditional accounting fields, and detail view actions) with no critical issues.

**Missing:** none

**Phantoms:** none

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (table with clickable Name, Create form with required fields and conditional Charge Time Type options, detail view with Edit/Delete, and Edit form); only a minor extra row action is present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Charges_Table.row_actions[0] (View link is not explicitly named in the description — Name is the clickable link)

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents the interactive elements described: the Floating Rates table with linkable name, the Create button, the creation/edit form with required name, base/active checkboxes, repeating Rate Periods (From Date, Interest Rate, Is Differential Rate) including the single-base constraint, and the detail view with rate history and Edit action.

**Missing:** none

**Phantoms:** none

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the pages, tables, links, forms, required fields, and the repeating ranges input; only two minor inferred submit buttons were added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Delinquency_Range_Form.submit_actions[0] (Save button label not specified in description)
- Create_Delinquency_Bucket_Form.submit_actions[0] (Save button label not specified in description)

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements from the description; only minor inferred visibility rules for payment detail fields appear but are non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- Loan_Detail_Page.action_bar.states.Approved.available_actions[0].fields.Payment_Details.visible_when
- Loan_Detail_Page.action_bar.states.Active.available_actions[0].fields.Payment_Details.visible_when

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, state-bound actions, deposit/withdraw forms, constraints, product auto-population, charges repeating group, and tabs as described; only minor placeholder arrays were added.

**Missing:** none

**Phantoms (hallucinations):**

- Savings_Account_Detail_Tabs.tabs[1].fields.Transactions.row_actions
- Savings_Account_Detail_Tabs.tabs[1].fields.Transactions.bulk_actions

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The AST covers all interactive elements from the description (application form fields, submit action, state-bound actions with required fields, and the three tabs with tables); two minor inferred items were added but do not block use.

**Missing:** none

**Phantoms (hallucinations):**

- components.Share_Account_Detail_Tabs.tabs[2].components.Charges_Table (columns for Charges tab were not specified in the description)
- components.Share_Account_Detail_Actions.states.Active.available_actions[1].fields.Credit_to_Savings_Account (a dropdown to choose the savings account for redemption was inferred; description only stated redemption is credited to the linked savings account)

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the interactive elements described (FD and RD creation forms with their fields, detail page tabs, and the listed action buttons); no significant missing items or extraneous phantoms were found.

**Missing:** none

**Phantoms:** none

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (tree with row action, Create GL Account form with required fields and constraints, and Account detail view with Edit/Delete) with no significant omissions or extraneous items.

**Missing:** none

**Phantoms:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements in the description (tables, filters, forms, repeating entry lines, add-row action, running totals constraint, and closures behavior).

**Missing:** none

**Phantoms:** none

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains multiple phantom interactive column definitions for the Accounting Rules table and omits explicit field types for required Rule_Name fields; regenerate with corrected column types and explicit field types.

**Missing:**

- components.Create_Rule_Form.fields.Rule_Name.type
- components.Edit_Rule_Form.fields.Rule_Name.type

**Phantoms (hallucinations):**

- components.Accounting_Rules_Table.columns[1] (Office column typed as dropdown — description lists Office as a table column/display, not an interactive dropdown)
- components.Accounting_Rules_Table.columns[2] (Debit_Account(s) column typed as dropdown with allow_multiple — table column is a display column in the description, not an input control)
- components.Accounting_Rules_Table.columns[3] (Credit_Account(s) column typed as dropdown with allow_multiple — table column is a display column in the description, not an input control)

**Fixes applied:**

- components.Create_Rule_Form.fields.Rule_Name.type: set to "text" (explicitly declare Rule_Name as a text input and keep required: true).
- components.Edit_Rule_Form.fields.Rule_Name.type: set to "text" (explicitly declare Rule_Name as a text input and keep required: true).
- components.Accounting_Rules_Table.columns[1].type: change from "dropdown" to "text" (Office is a display column, not an interactive dropdown in the table).
- components.Accounting_Rules_Table.columns[2].type: change from "dropdown" to "text" and remove "allow_multiple" (Debit Account(s) is a display column in the table; multi-select applies only in the create/edit forms).
- components.Accounting_Rules_Table.columns[3].type: change from "dropdown" to "text" and remove "allow_multiple" (Credit Account(s) is a display column in the table; multi-select applies only in the create/edit forms).

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only minor inferred controls (add-row and a row action duplicate) are present.

**Missing:** none

**Phantoms (hallucinations):**

- Provisioning_Criteria_Form.add_row_action (Add Row button name inferred but not explicitly named in description)
- Provisioning_Criteria_Table.row_actions[0] (Open Criteria row action not explicitly described; description only specified the Criteria Name link)

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (hierarchical table with Office Name link, Create Office form and fields, Office Detail with Edit and edit form); only one minor phantom row action was added.

**Missing:** none

**Phantoms (hallucinations):**

- components.Offices_Page.components.Offices_Table.row_actions[0] (Open Detail row action not mentioned in the description)

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the Employees data table (including Name link, Office, Is Loan Officer indicator, Status), the + Create Employee action and all creation form fields with required flags, the Is Loan Officer consequence, and the Staff Detail page with Edit action.

**Missing:** none

**Phantoms:** none

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately includes all interactive elements described (tables, clickable Teller Name, Create/Edit/Allocate buttons, forms with required fields, Cashier actions, and transactions table) with no missing critical items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; two inferred submit actions are present but acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- components.Create_User_Form.submit_actions[0] (inferred 'submit' action not named in description)
- components.Create_Role_Form.submit_actions[0] (inferred 'submit' action not named in description)

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the described Reports page: category tabs, report table rows with clickable Name links, the parameters form containing Office/Branch/Currency/Loan Product/Date Range/Loan Officer/Fund and Output options, a Run Report action, and a sortable, paginated result table.

**Missing:** none

**Phantoms:** none

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements: Account Transfers form (fields, validations, Submit), Standing Instructions table (columns, create button, row actions), and Create Standing Instruction form with required fields and recurrence settings.

**Missing:** none

**Phantoms:** none

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures all interactive elements (tables, create buttons, forms, required fields, repeating components, and references from products/charges) and aligns with the description; no critical items missing.

**Missing:** none

**Phantoms:** none

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately covers the interactive elements described; only two minor inferred items (a date constraint and a state-bound action bar) are present but not critical.

**Missing:** none

**Phantoms (hallucinations):**

- components.Create_Holiday_Form.constraints[0] (constraint 'To_Date must be on or after From_Date' is not specified in the description)
- components.Holidays_Action_Bar (state_bound_action_bar was introduced though description only mentions a Status column)

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST includes several inferred interactive elements not present in the description (phantoms); please remove or explicitly document them and regenerate.

**Missing:** none

**Phantoms (hallucinations):**

- components.Audit_Trails.row_actions[2].fields.Rejection_Comment (Rejection_Comment field on Reject action not mentioned in description)
- components.Audit_Trails.filters_actions[0] (Apply_Filters action not explicitly described)
- components.Audit_Trails.filters_actions[1] (Reset_Filters action not explicitly described)
- components.Manage_Codes.Code_Detail.submit_actions[1] (Cancel submit action not specified in description)
- components.Manage_Data_Tables.Create_Data_Table_Form.submit_actions[1] (Cancel submit action not specified in description)

**Fixes applied:**

- components.Audit_Trails.row_actions[2].fields — Remove the Rejection_Comment field unless the description explicitly requires capturing a rejection comment when rejecting an audit action; if it is required, add that requirement to the description.
- components.Audit_Trails.filters_actions — Remove the Apply_Filters and Reset_Filters actions or update the description to explicitly state that there are Apply and Reset buttons for filters.
- components.Manage_Codes.Code_Detail.submit_actions[1] — Remove the Cancel submit action or update the description to explicitly mention a Cancel button for saving code list changes.
- components.Manage_Data_Tables.Create_Data_Table_Form.submit_actions[1] — Remove the Cancel submit action or update the description to explicitly mention a Cancel button on the Create Data Table form.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the profile icon toggle, dropdown items (Profile Settings and Log Out), preconditions, and Log Out side effects including session termination, token clearing, and redirect behavior.

**Missing:** none

**Phantoms:** none

---
