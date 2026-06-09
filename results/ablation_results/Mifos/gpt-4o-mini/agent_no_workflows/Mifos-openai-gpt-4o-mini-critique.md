# Semantic Critique — Mifos

Generated: 2026-06-09T09:36:59.347119Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and has phantoms.

**Missing:**

- Login_Form.fields.Remember_me
- Login_Form.fields.Tenant.required (should be true)

**Phantoms (hallucinations):**

- Login_Form.fields.Tenant.options (options should not be inferred)

**Fixes applied:**

- Add 'Remember_me' field to 'Login_Form.fields'
- Set 'Tenant.required' to true

---

## Home Page

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

## Global Search

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several critical elements and contains phantoms.

**Missing:**

- Bulk_Import_Page.fields.Import_History_Table
- Client_Detail_Page.fields.Name
- Client_Detail_Page.fields.Status_Badge
- Client_Detail_Page.fields.Activation_Date
- Client_Detail_Page.fields.Office

**Phantoms (hallucinations):**

- Bulk_Import_Page.fields.Download_Template (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Is_Staff (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Active (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Open_Savings_Account (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Pending[0].fields.Activation_Date (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Active[1].fields.Destination_Office (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Active[2].fields.Closure_Reason (not explicitly mentioned in description)

**Fixes applied:**

- Add 'Import_History_Table' to 'Bulk_Import_Page.fields'
- Add 'Name' to 'Client_Detail_Page.fields'
- Add 'Status_Badge' to 'Client_Detail_Page.fields'
- Add 'Activation_Date' to 'Client_Detail_Page.fields'
- Add 'Office' to 'Client_Detail_Page.fields'

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Groups_Page.row_actions
- Group_Detail_Page.tabs[0].fields.Client_Members
- Group_Detail_Page.tabs[1].fields.Group_Loans
- Group_Detail_Page.tabs[1].fields.GLIM
- Group_Detail_Page.tabs[2].fields.Group_Savings
- Group_Detail_Page.tabs[2].fields.GSIM

**Phantoms (hallucinations):**

- Bulk_Import_Groups_Page.components.Groups_Template.fields.Download_Button (Download button not in description)
- Bulk_Import_Groups_Page.components.Groups_Upload.fields.Upload_Button (Upload button not in description)
- Group_Detail_Page.fields.Group_Name (Group name is passive display, not interactive)

**Fixes applied:**

- Add row_actions to Groups_Page
- Remove Download_Button from Groups_Template
- Remove Upload_Button from Groups_Upload
- Remove Group_Name from Group_Detail_Page.fields

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Bulk_Import_Centers_Page.fields.Template_Download
- Bulk_Import_Centers_Page.fields.File_Upload

**Phantoms (hallucinations):**

- Centers_Page.row_actions[0] (View action not in description)
- Bulk_Import_Centers_Page.submit_actions[0] (Import action not in description)

**Fixes applied:**

- Add 'Template_Download' field to 'Bulk_Import_Centers_Page.fields'
- Add 'File_Upload' field to 'Bulk_Import_Centers_Page.fields'
- Remove 'View' action from 'Centers_Page.row_actions'
- Remove 'Import' action from 'Bulk_Import_Centers_Page.submit_actions'

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Loan_Products_Page.row_actions[0].action_name (Edit option for existing product detail view)
- Loan_Product_Stepper.steps[5].fields (search-and-add interface for predefined charges)

**Phantoms (hallucinations):**

- Loan_Product_Stepper.steps[6].fields.GL_Account_Mappings.visible_when (condition not explicitly stated in description)

**Fixes applied:**

- Add 'Edit' action to Loan_Products_Page.row_actions
- Add fields for search-and-add interface in Loan_Product_Stepper.steps[5]
- Remove visible_when condition from Loan_Product_Stepper.steps[6].fields.GL_Account_Mappings

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several required fields and contains phantoms.

**Missing:**

- Fixed_Deposit_Products_Stepper.steps[1].fields
- Fixed_Deposit_Products_Stepper.steps[2].fields
- Fixed_Deposit_Products_Stepper.steps[3].fields
- Fixed_Deposit_Products_Stepper.steps[4].fields
- Fixed_Deposit_Products_Stepper.steps[5].fields
- Recurring_Deposit_Products_Stepper.steps[1].fields
- Recurring_Deposit_Products_Stepper.steps[2].fields
- Recurring_Deposit_Products_Stepper.steps[3].fields
- Recurring_Deposit_Products_Stepper.steps[4].fields
- Recurring_Deposit_Products_Stepper.steps[5].fields

**Phantoms (hallucinations):**

- Fixed_Deposit_Products_Stepper.steps[6] (missing step for Deposit Term)
- Fixed_Deposit_Products_Stepper.steps[7] (missing step for Interest Rate Chart)
- Recurring_Deposit_Products_Stepper.steps[6] (missing step for additional fields)

**Fixes applied:**

- Add required fields for Fixed Deposit Products steps 1-5.
- Add required fields for Recurring Deposit Products steps 1-5.
- Add missing steps for Fixed Deposit and Recurring Deposit Products.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Share_Product_Stepper.steps[2].fields.Currency.required
- Create_Share_Product_Stepper.steps[4].fields.Nominal_Shares_per_Client
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency
- Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period
- Create_Share_Product_Stepper.steps[6].fields.Search_and_Add_Interface

**Phantoms (hallucinations):**

- Create_Share_Product_Stepper.steps[3].fields.Nominal_Unit_Price (inferred from Nominal/Unit Price in description)
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Shares_per_Client (inferred from Minimum/Maximum/Nominal Shares per Client in description)
- Create_Share_Product_Stepper.steps[4].fields.Maximum_Shares_per_Client (inferred from Minimum/Maximum/Nominal Shares per Client in description)
- Create_Share_Product_Stepper.steps[4].fields.Nominal_Shares_per_Client (inferred from Minimum/Maximum/Nominal Shares per Client in description)

**Fixes applied:**

- Create_Share_Product_Stepper.steps[2].fields.Currency.required: true
- Create_Share_Product_Stepper.steps[4].fields.Nominal_Shares_per_Client: { type: 'number', required: false }
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency: { type: 'unspecified', required: false }
- Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period: { type: 'unspecified', required: false }
- Create_Share_Product_Stepper.steps[6].fields.Search_and_Add_Interface: { type: 'unspecified', required: false }

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required options for the Currency and Tax Group fields, and there are phantoms present.

**Missing:**

- Create_Charge_Form.fields.Currency.options
- Create_Charge_Form.fields.Tax_Group.options

**Phantoms:** none

**Fixes applied:**

- Add options for Currency in Create_Charge_Form.fields.Currency
- Add options for Tax Group in Create_Charge_Form.fields.Tax_Group

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Delinquency_Buckets_Page.fields.Delinquency_Ranges.item_fields.Range_Name
- Delinquency_Buckets_Page.fields.Delinquency_Ranges.item_fields.Minimum_Age_Days
- Delinquency_Buckets_Page.fields.Delinquency_Ranges.item_fields.Maximum_Age_Days

**Phantoms (hallucinations):**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges (inferred from description but not explicitly stated)

**Fixes applied:**

- Add fields for Delinquency Ranges in Create_Delinquency_Bucket_Form as specified in the description.

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several critical elements and contains phantoms.

**Missing:**

- Loan_Application_Wizard.steps[2].fields.Grace_Period
- Loan_Detail_Page.tabs[0].fields.Status_Badge
- Loan_Detail_Page.action_buttons.Pending_Approval.available_actions[0].fields.Approved_On_Date
- Loan_Detail_Page.action_buttons.Approved.available_actions[0].fields.Payment_Detail_Fields
- Loan_Detail_Page.action_buttons.Active.available_actions[0].fields.Payment_Type

**Phantoms (hallucinations):**

- Loan_Detail_Page.tabs[0].fields.Status_Badge (Status badges are color-coded but not defined)
- Loan_Detail_Page.action_buttons.Pending_Approval.available_actions[0].fields.Approved_On_Date (dialog with Approved On Date not mentioned)
- Loan_Detail_Page.action_buttons.Approved.available_actions[0].fields.Payment_Detail_Fields (not specified in description)
- Loan_Detail_Page.action_buttons.Active.available_actions[0].fields.Payment_Type (not specified in description)

**Fixes applied:**

- Add 'Grace_Period' field to Loan_Application_Wizard.steps[2].fields.
- Define 'Status_Badge' in Loan_Detail_Page.tabs[0].fields.
- Add 'Approved_On_Date' field to Loan_Detail_Page.action_buttons.Pending_Approval.available_actions[0].fields.
- Define 'Payment_Detail_Fields' in Loan_Detail_Page.action_buttons.Approved.available_actions[0].fields.
- Define 'Payment_Type' in Loan_Detail_Page.action_buttons.Active.available_actions[0].fields.

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Savings_Account_Creation_Form.fields.Nominal_Annual_Interest_Rate
- Savings_Account_Creation_Form.fields.Lock_in_Period
- Savings_Account_Creation_Form.fields.Minimum_Opening_Balance
- Savings_Account_Creation_Form.fields.Interest_Calculated_Using
- Savings_Account_Creation_Form.fields.Interest_Compounding_Period
- Savings_Account_Creation_Form.fields.Interest_Posting_Period
- Savings_Account_Creation_Form.fields.Days_in_Year
- Savings_Account_Detail_Page.tabs[0].fields.Status
- Savings_Account_Detail_Page.tabs[1].row_actions

**Phantoms (hallucinations):**

- Savings_Account_Detail_Page.tabs[0].fields.Status (Status field not in description)
- Savings_Account_Detail_Page.tabs[1].row_actions (No row actions specified in description)

**Fixes applied:**

- Add missing fields to Savings_Account_Creation_Form: Nominal_Annual_Interest_Rate, Lock_in_Period, Minimum_Opening_Balance, Interest_Calculated_Using, Interest_Compounding_Period, Interest_Posting_Period, Days_in_Year
- Add missing Status field to Savings_Account_Detail_Page.tabs[0]
- Remove phantom Status field from Savings_Account_Detail_Page.tabs[0]
- Remove phantom row_actions from Savings_Account_Detail_Page.tabs[1]

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- FD_Account_Creation_Form.fields.Deposit_Period_Unit
- RD_Account_Creation_Form.fields.Deposit_Period_Unit

**Phantoms (hallucinations):**

- FD_Account_Detail_Page.fields.deposit_amount (passive display field not in description)
- RD_Account_Detail_Page.fields.deposit_schedule (passive display field not in description)
- RD_Account_Detail_Page.fields.maturity_details (passive display field not in description)

**Fixes applied:**

- Add Deposit_Period_Unit field to FD_Account_Creation_Form
- Add Deposit_Period_Unit field to RD_Account_Creation_Form
- Remove deposit_amount field from FD_Account_Detail_Page
- Remove deposit_schedule field from RD_Account_Detail_Page
- Remove maturity_details field from RD_Account_Detail_Page

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Chart_of_Accounts.fields.GL_Code
- Chart_of_Accounts.fields.Account_Name
- Chart_of_Accounts.fields.Account_Type
- Chart_of_Accounts.fields.Usage

**Phantoms (hallucinations):**

- Create_GL_Account_Form.fields.Tag (not mentioned in description)

**Fixes applied:**

- Add required fields GL_Code, Account_Name, Account_Type, and Usage to Chart_of_Accounts.fields.
- Remove Tag field from Create_GL_Account_Form.fields.

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Journal_Entries_Table.filter_bar.fields.Office.required
- Journal_Entries_Table.filter_bar.fields.GL_Account.required
- Journal_Entries_Table.filter_bar.fields.Date_Range.required
- Journal_Entries_Table.filter_bar.fields.Transaction_ID.required
- Journal_Entries_Table.filter_bar.fields.Entry_Type.required
- Closing_Entries_Table.row_actions[0].on_success

**Phantoms (hallucinations):**

- Journal_Entries_Table.row_actions[0] (Add Journal Entry button not in description)
- Closing_Entries_Table.row_actions[0] (Create Closure button not in description)

**Fixes applied:**

- Set Journal_Entries_Table.filter_bar.fields.Office.required to true
- Set Journal_Entries_Table.filter_bar.fields.GL_Account.required to true
- Set Journal_Entries_Table.filter_bar.fields.Date_Range.required to true
- Set Journal_Entries_Table.filter_bar.fields.Transaction_ID.required to true
- Set Journal_Entries_Table.filter_bar.fields.Entry_Type.required to true
- Add Closing_Entries_Table.row_actions[0].on_success with appropriate description

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Rule_Form.fields.Debit_Tags_Debit_Account (should specify GL account dropdown or multi-select)
- Create_Rule_Form.fields.Credit_Tags_Credit_Account (should specify GL account dropdown or multi-select)
- Financial_Activity_Mappings_Table.row_actions[0].action_name (should specify Edit action)

**Phantoms (hallucinations):**

- Create_Rule_Form.fields.Rule_Name (unspecified type not in description)
- Create_Mapping_Form.fields.GL_Account (unspecified type not in description)

**Fixes applied:**

- Specify the type for Create_Rule_Form.fields.Debit_Tags_Debit_Account as 'dropdown or multi-select'.
- Specify the type for Create_Rule_Form.fields.Credit_Tags_Credit_Account as 'dropdown or multi-select'.
- Add 'Edit' action to Financial_Activity_Mappings_Table.row_actions.

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the required field 'External_ID' in the Create Office form and contains a phantom in the Office Detail page.

**Missing:**

- Create_Office_Form.fields.External_ID

**Phantoms (hallucinations):**

- Office_Detail_Page.fields (Edit option not in description)

**Fixes applied:**

- Add 'External_ID' as a required field in 'Create_Office_Form.fields'
- Remove 'Office_Detail_Page.fields' as it is not specified in the description

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Tellers_Page.row_actions[0].action_name (Create Teller button not in description)
- Teller_Detail_Page.fields.Cashiers_Section.fields (Cashiers section fields not defined)
- Cashier_Detail_Page.fields (fields for Cashier Detail page not fully defined)

**Phantoms (hallucinations):**

- Tellers_Page.row_actions[0] (Edit action not explicitly mentioned in description)
- Allocate_Cashier_Form.fields.Description (Description field not explicitly mentioned in allocation form)

**Fixes applied:**

- Add a Create Teller button to Tellers_Page.row_actions
- Define fields for Cashiers_Section in Teller_Detail_Page
- Ensure Cashier_Detail_Page has all required fields as per description

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms detected in the AST.

**Missing:**

- Create_User_Form.fields.Roles
- Create_User_Form.fields.Staff
- Create_Role_Form.fields.Permissions

**Phantoms (hallucinations):**

- Users_Table.row_actions[0] (View action not in description)
- Permissions_Page.fields (no fields specified in description)

**Fixes applied:**

- Add Roles field to Create_User_Form
- Add Staff field to Create_User_Form
- Add Permissions field to Create_Role_Form

---

## Reports

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Reports_Page.row_actions[0].fields.Parameters_Form.fields.Output_Options

**Phantoms (hallucinations):**

- Reports_Page.row_actions[0].action_name (Open Report button not in description)
- Reports_Page.row_actions[0].fields.Parameters_Form.fields (fields are not explicitly named in the description)

**Fixes applied:**

- Add Output_Options field to Parameters_Form
- Rename action_name to 'Run Report' in row_actions

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Account_Transfers_Form.fields.From_Office
- Account_Transfers_Form.fields.From_Client
- Account_Transfers_Form.fields.From_Account
- Account_Transfers_Form.fields.To_Office
- Account_Transfers_Form.fields.To_Client
- Account_Transfers_Form.fields.To_Account
- Create_Standing_Instruction_Form.fields.From_Account
- Create_Standing_Instruction_Form.fields.To_Account
- Create_Standing_Instruction_Form.fields.Transfer_Type
- Create_Standing_Instruction_Form.fields.Priority
- Create_Standing_Instruction_Form.fields.Amount
- Create_Standing_Instruction_Form.fields.Validity_From
- Create_Standing_Instruction_Form.fields.Validity_Till
- Create_Standing_Instruction_Form.fields.Recurrence_Frequency
- Create_Standing_Instruction_Form.fields.Recurrence_Interval

**Phantoms (hallucinations):**

- Standing_Instructions_Table.bulk_actions (no mention of bulk actions in description)
- Create_Standing_Instruction_Form.fields.Transfer_Type (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Priority (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Frequency (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Interval (not mentioned in description)

**Fixes applied:**

- Add missing fields to Account_Transfers_Form: From_Office, From_Client, From_Account, To_Office, To_Client, To_Account
- Add missing fields to Create_Standing_Instruction_Form: From_Account, To_Account, Transfer_Type, Priority, Amount, Validity_From, Validity_Till, Recurrence_Frequency, Recurrence_Interval
- Remove phantoms from Standing_Instructions_Table: bulk_actions
- Remove phantoms from Create_Standing_Instruction_Form: Transfer_Type, Priority, Recurrence_Frequency, Recurrence_Interval

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Tax_Groups_Table.bulk_actions
- Tax_Groups_Table.sortable_columns
- Tax_Groups_Table.columns[1].type (should be unspecified for associated components)
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.End_Date.required (should be false)

**Phantoms (hallucinations):**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields (no explicit mention of Tax Components section in description)

**Fixes applied:**

- Add bulk_actions to Tax_Groups_Table
- Add sortable_columns to Tax_Groups_Table
- Change Tax_Groups_Table.columns[1].type to unspecified
- Set Create_Tax_Group_Form.fields.Tax_Components.item_fields.End_Date.required to false

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Holidays_Page.submit_actions[0].fields.Repayments_Rescheduled_To
- Working_Days_Page.fields.Repayment_Rescheduling

**Phantoms (hallucinations):**

- Funds_Page.submit_actions[0].element_name (Create Fund button not in description)
- Payment_Types_Page.submit_actions[0].element_name (+ Create button not in description)
- Bulk_Import_Page.fields.Entity_Types.options[8] (more option not in description)

**Fixes applied:**

- Add 'Repayments_Rescheduled_To' field to Holidays_Page.submit_actions[0].fields
- Add 'Repayment_Rescheduling' field to Working_Days_Page.fields
- Remove 'Create Fund' from Funds_Page.submit_actions[0].element_name
- Remove '+ Create' from Payment_Types_Page.submit_actions[0].element_name
- Remove 'more' from Bulk_Import_Page.fields.Entity_Types.options

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected interactive elements and contains phantoms.

**Missing:**

- Manage_Scheduler_Jobs.row_actions[0] (action buttons for each job)
- Manage_Scheduler_Jobs.columns[3] (Previous_Run_Status should include start/end times)
- Manage_Codes.row_actions[0] (missing actions for adding, editing, reordering, and deactivating entries)
- Audit_Trails.row_actions[0] (missing actions for processing results)

**Phantoms (hallucinations):**

- Manage_Scheduler_Jobs.bulk_actions[0] (no bulk actions mentioned in description)
- Manage_Codes.bulk_actions[0] (no bulk actions mentioned in description)
- Manage_Data_Tables.fields.Column_Definitions.item_fields.Type.options[7] (dropdown option not mentioned in description)
- Audit_Trails.filters.search_fields[4] (Maker_ID not mentioned in description)
- Audit_Trails.filters.search_fields[5] (Checker_ID not mentioned in description)

**Fixes applied:**

- Add row_actions to Manage_Scheduler_Jobs for each job's action buttons.
- Include start/end times in Previous_Run_Status column of Manage_Scheduler_Jobs.
- Add row_actions to Manage_Codes for adding, editing, reordering, and deactivating entries.
- Add row_actions to Audit_Trails for processing results.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
