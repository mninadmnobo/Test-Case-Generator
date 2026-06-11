# Semantic Critique — Mifos

Generated: 2026-06-09T09:26:36.597478Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and has phantoms.

**Missing:**

- Login_Form.fields.Tenant.required
- Login_Form.fields.Remember_me.required

**Phantoms (hallucinations):**

- Login_Form.fields.Tenant.options (options inferred without explicit mention in description)
- Login_Form.submit_actions[0].constraints[0] (constraint inferred without explicit mention in description)

**Fixes applied:**

- Set Login_Form.fields.Tenant.required to true
- Set Login_Form.fields.Remember_me.required to true
- Remove Login_Form.fields.Tenant.options
- Remove Login_Form.submit_actions[0].constraints

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

Missing items and phantoms detected in the AST.

**Missing:**

- Clients_Page.row_actions[0].action_name (View action for Name not present)
- Client_Detail_Page.tabs[0].fields (General tab should have fields)
- Client_Detail_Page.tabs[1].fields (Accounts tab should have fields)

**Phantoms (hallucinations):**

- Bulk_Import_Page.fields.Download_Template (Download client Excel template not explicitly mentioned)
- Client_Detail_Page.tabs[1].tabs[0].fields (Loans tab should have fields)
- Client_Detail_Page.tabs[1].tabs[1].fields (Savings tab should have fields)
- Client_Detail_Page.tabs[1].tabs[2].fields (Shares tab should have fields)
- Client_Detail_Page.tabs[1].tabs[3].fields (Fixed Deposits tab should have fields)
- Client_Detail_Page.tabs[1].tabs[4].fields (Recurring Deposits tab should have fields)

**Fixes applied:**

- Add 'View' action to Clients_Page.row_actions
- Add fields to Client_Detail_Page.tabs[0] (General tab)
- Add fields to Client_Detail_Page.tabs[1] (Accounts tab)

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Groups_Page.row_actions
- Bulk_Import_Groups_Page.import_history_table.sortable_columns

**Phantoms (hallucinations):**

- Groups_Page.bulk_actions[0] (Import Groups button not in description)
- Groups_Page.bulk_actions[1] (Create New Group button not in description)
- Bulk_Import_Groups_Page.fields.Groups_Template.fields.Download (Download button not in description)
- Bulk_Import_Groups_Page.fields.Groups_Upload.fields.Upload (Upload button not in description)
- Group_Detail_Page.fields.Group_Name (passive display field not in description)
- Group_Detail_Page.fields.Account_Number (passive display field not in description)
- Group_Detail_Page.fields.Status (passive display field not in description)
- Group_Detail_Page.fields.Office (passive display field not in description)
- Group_Detail_Page.fields.Staff (passive display field not in description)

**Fixes applied:**

- Add row_actions to Groups_Page
- Remove phantom buttons from Groups_Page and Bulk_Import_Groups_Page
- Remove passive display fields from Group_Detail_Page

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Loan_Product_Stepper_Wizard.steps[2].fields.Currency
- Loan_Product_Stepper_Wizard.steps[3].fields.Repayment_Strategy
- Loan_Product_Stepper_Wizard.steps[4].fields.Repaid_Every.frequency

**Phantoms (hallucinations):**

- Loan_Product_Stepper_Wizard.steps[5].fields.Predefined_Charges (search-and-add interface not specified in description)

**Fixes applied:**

- Add 'Currency' field in step 2 of the Loan_Product_Stepper_Wizard.
- Add 'Repayment_Strategy' field in step 3 of the Loan_Product_Stepper_Wizard.
- Add 'Repaid_Every.frequency' field in step 4 of the Loan_Product_Stepper_Wizard.
- Remove 'Predefined_Charges' field in step 5 of the Loan_Product_Stepper_Wizard.

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Savings_Product_Stepper.steps[6].fields.Accounting_Method
- Fixed_Deposit_Products_Stepper.steps[7].fields.Pre-Closure
- Recurring_Deposit_Products_Stepper.steps[10].fields.Recurring_Frequency

**Phantoms (hallucinations):**

- Fixed_Deposit_Products_Stepper.steps[7].fields.Pre-Closure (not mentioned in description)
- Recurring_Deposit_Products_Stepper.steps[10].fields.Is_Mandatory_Deposit (not mentioned in description)
- Recurring_Deposit_Products_Stepper.steps[10].fields.Allow_Withdrawal (not mentioned in description)
- Recurring_Deposit_Products_Stepper.steps[10].fields.Adjust_Advance_Towards_Future_Payments (not mentioned in description)

**Fixes applied:**

- Add missing fields for Fixed Deposit Products and Recurring Deposit Products as per description.
- Ensure all fields in the AST are explicitly mentioned in the description.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Share_Product_Stepper_Wizard.steps[2].fields.Currency
- Share_Product_Stepper_Wizard.steps[2].fields.Decimal_Places
- Share_Product_Stepper_Wizard.steps[2].fields.Currency_In_Multiples_Of
- Share_Product_Stepper_Wizard.steps[4].fields.Minimum_Active_Period_Frequency
- Share_Product_Stepper_Wizard.steps[4].fields.Lock_in_Period
- Share_Product_Stepper_Wizard.steps[6].fields.Charges

**Phantoms (hallucinations):**

- Share_Product_Stepper_Wizard.steps[6].fields.Charges (field not in description)

**Fixes applied:**

- Add required fields for Currency, Decimal Places, and Currency In Multiples Of in step 2.
- Add required fields for Minimum Active Period Frequency and Lock-in Period in step 4.
- Remove Charges field from step 6.

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains missing elements and phantoms.

**Missing:**

- Charges_Table.columns[4].type
- Charge_Creation_Form.fields.Charge_Time_Type.options[0]
- Charge_Creation_Form.fields.Charge_Time_Type.options[1]
- Charge_Creation_Form.fields.Charge_Time_Type.options[2]
- Charge_Creation_Form.fields.Charge_Time_Type.options[3]
- Charge_Creation_Form.fields.Charge_Time_Type.options[4]

**Phantoms (hallucinations):**

- Charge_Creation_Form.fields.Charge_Name.type (unspecified type not defined in description)
- Charge_Creation_Form.fields.Currency.type (unspecified type not defined in description)
- Charge_Creation_Form.fields.Amount.type (unspecified type not defined in description)

**Fixes applied:**

- Charges_Table.columns[4].type should be 'unspecified'
- Charge_Creation_Form.fields.Charge_Time_Type.options should include 'Disbursement', 'Specified Due Date', 'Installment Fee', 'Overdue Fees', 'Tranche Disbursement', 'Savings Activation', 'Withdrawal Fee', 'Annual Fee', 'Monthly Fee', 'Overdraft Fee'

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.From_Date.required
- Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Interest_Rate.required
- Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Is_Differential_Rate

**Phantoms (hallucinations):**

- Floating_Rates_Table.columns[1].type (unspecified type not defined in description)
- Floating_Rates_Table.columns[2].type (unspecified type not defined in description)
- Floating_Rates_Table.columns[3].type (unspecified type not defined in description)

**Fixes applied:**

- Add 'required' to 'Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.From_Date'
- Add 'required' to 'Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Interest_Rate'
- Add 'Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Is_Differential_Rate' to the AST

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Range_Description
- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Days

**Phantoms (hallucinations):**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges (inferred from description but not explicitly stated)

**Fixes applied:**

- Add 'Range_Description' and 'Days' fields to 'Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields'.

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected elements and contains phantoms.

**Missing:**

- Loan_Detail_Page.tabs[0].fields.Disbursement_Details
- Loan_Detail_Page.tabs[0].fields.Repayment_Schedule_Summary
- Loan_Detail_Page.tabs[0].fields.Total_Paid
- Loan_Detail_Page.tabs[0].fields.Total_Outstanding
- Loan_Detail_Page.tabs[0].fields.Total_Overdue
- Loan_Detail_Page.tabs[0].fields.Charges_Summary
- Loan_Detail_Page.tabs[1].row_actions
- Loan_Detail_Page.tabs[2].row_actions
- Loan_Detail_Page.tabs[3].fields
- Loan_Detail_Page.tabs[4].fields
- Loan_Detail_Page.tabs[5].fields

**Phantoms (hallucinations):**

- Loan_Application_Wizard.steps[3].fields.Add_Charge (button not in description)
- Loan_Detail_Page.tabs[0].fields (passive display fields not in description)
- Loan_Detail_Page.tabs[1].sortable_columns (passive display fields not in description)
- Loan_Detail_Page.tabs[2].sortable_columns (passive display fields not in description)

**Fixes applied:**

- Add missing fields to Loan_Detail_Page.tabs[0] as specified in the description.
- Remove phantom fields from Loan_Application_Wizard.steps[3].fields.Add_Charge.
- Remove passive display fields from Loan_Detail_Page.tabs[0].fields.
- Remove passive display fields from Loan_Detail_Page.tabs[1].sortable_columns.
- Remove passive display fields from Loan_Detail_Page.tabs[2].sortable_columns.

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Savings_Account_Detail_Tabs.tabs[1].row_actions (missing actions for Transactions tab)
- Savings_Account_Actions.states[Active].available_actions[1].constraints (missing validation for Withdraw action)

**Phantoms (hallucinations):**

- Savings_Account_Creation_Form.fields.Field_Officer (unspecified type not defined in description)
- Savings_Account_Creation_Form.fields.Nominal_Annual_Interest_Rate (unspecified type not defined in description)
- Savings_Account_Creation_Form.fields.Minimum_Opening_Balance (unspecified type not defined in description)
- Savings_Account_Creation_Form.fields.Lock_in_Period (unspecified type not defined in description)
- Savings_Account_Actions.states[Active].available_actions[0].fields.Payment_Details (not mentioned in description)

**Fixes applied:**

- Add row_actions to Transactions tab in Savings_Account_Detail_Tabs
- Add constraints for Withdraw action in Savings_Account_Actions.states[Active].available_actions[1]

---

## Share Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several phantoms and missing elements related to the Share Account Detail page and Charges section.

**Missing:**

- Share_Account_Detail_Page.fields.Charges_Section
- Share_Account_Detail_Page.fields.Action_Buttons
- Share_Account_Detail_Page.fields.Action_Buttons.Pending
- Share_Account_Detail_Page.fields.Action_Buttons.Approved
- Share_Account_Detail_Page.fields.Action_Buttons.Active

**Phantoms (hallucinations):**

- Share_Account_Detail_Page.fields.Account_Number (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Product_Name (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Client_Name (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Status_Badge (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Total_Approved_Shares (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Total_Pending_Shares (not explicitly mentioned in description)
- Share_Account_Detail_Page.fields.Unit_Price (not explicitly mentioned in description)

**Fixes applied:**

- Add missing fields to Share_Account_Detail_Page as per description.
- Include action buttons for Pending, Approved, and Active states in Share_Account_Detail_Page.

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- FD_Account_Creation_Form.fields.Deposit_Period_Unit
- RD_Account_Creation_Form.fields.Deposit_Period_Unit

**Phantoms (hallucinations):**

- FD_Account_Creation_Form.fields.Fixed_Deposit_Product (not mentioned in description as required)
- RD_Account_Creation_Form.fields.Recurring_Deposit_Product (not mentioned in description as required)

**Fixes applied:**

- Remove FD_Account_Creation_Form.fields.Fixed_Deposit_Product
- Remove RD_Account_Creation_Form.fields.Recurring_Deposit_Product

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_GL_Account_Form.fields.Parent_Account.options
- Create_GL_Account_Form.fields.Account_Usage.required

**Phantoms (hallucinations):**

- Chart_of_Accounts.row_actions[0] (View action not in description)
- Create_GL_Account_Form.fields.Tag (Tag dropdown not mentioned in description)

**Fixes applied:**

- Populate Create_GL_Account_Form.fields.Parent_Account.options with header accounts of the same type.
- Set Create_GL_Account_Form.fields.Account_Usage.required to true.

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains missing elements and phantoms.

**Missing:**

- Closing_Entries_Table.submit_actions[0].fields.Closing_Date

**Phantoms (hallucinations):**

- Closing_Entries_Table.submit_actions[0] (Create Closure button not in description)

**Fixes applied:**

- Add Closing_Date field to Closing_Entries_Table.submit_actions[0].fields
- Remove phantom Create Closure button from Closing_Entries_Table.submit_actions[0]

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Create_Rule_Form.fields.Office.required (should be true)
- Financial_Activity_Mappings_Table.row_actions[0].action_name (should be 'Edit')
- Financial_Activity_Mappings_Table.row_actions[1].action_name (should be 'Delete')

**Phantoms (hallucinations):**

- Create_Rule_Form.fields.Debit_Tags_Account (not mentioned in description)
- Create_Rule_Form.fields.Credit_Tags_Account (not mentioned in description)
- Financial_Activity_Mappings_Table.columns.Financial_Activity (should be named 'Financial Activity')

**Fixes applied:**

- Create_Rule_Form.fields.Office.required should be set to true
- Add 'Edit' action to Financial_Activity_Mappings_Table.row_actions
- Add 'Delete' action to Financial_Activity_Mappings_Table.row_actions
- Remove Create_Rule_Form.fields.Debit_Tags_Account
- Remove Create_Rule_Form.fields.Credit_Tags_Account
- Rename Financial_Activity_Mappings_Table.columns.Financial_Activity to 'Financial Activity'

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

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

- Teller_Detail.fields.Cashiers_Section.fields (missing fields for Cashiers section)
- Cashier_Detail.fields (missing fields for Cashier Detail page)

**Phantoms (hallucinations):**

- Tellers_Table.row_actions[0] (View action not in description)
- Cashier_Transactions_List.row_actions (no actions mentioned in description)

**Fixes applied:**

- Add fields to Teller_Detail.fields.Cashiers_Section for Cashier assignments.
- Add fields to Cashier_Detail.fields for Opening Balance and Cash In Hand.

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_User_Form.fields.Staff
- Create_User_Form.fields.Override_Password_Expiry_Policy
- Create_User_Form.fields.Send_Password_to_Email
- Permissions_Page.fields.Permissions.options[0].checkbox
- Permissions_Page.fields.Permissions.options[1].checkbox
- Permissions_Page.fields.Permissions.options[2].checkbox
- Permissions_Page.fields.Permissions.options[3].checkbox
- Permissions_Page.fields.Permissions.options[4].checkbox

**Phantoms (hallucinations):**

- Create_User_Form.fields.Roles (multi-select checkboxes not specified in description)
- Create_Role_Form.fields.Description (not specified as required or optional in description)
- Permissions_Page.fields.Permissions (checkboxes for permissions not specified in description)

**Fixes applied:**

- Create_User_Form.fields.Staff: Add field for Staff dropdown linking to a staff record.
- Create_User_Form.fields.Override_Password_Expiry_Policy: Add checkbox for Override Password Expiry Policy.
- Create_User_Form.fields.Send_Password_to_Email: Add checkbox for Send Password to Email.
- Permissions_Page.fields.Permissions.options: Add checkboxes for each permission with appropriate names.

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Account_Transfers_Form.fields.From_Account
- Account_Transfers_Form.fields.To_Account_Type
- Standing_Instructions_Table.row_actions[0].action_name (Enable action not in description)
- Standing_Instructions_Table.row_actions[1].action_name (Disable action not in description)
- Standing_Instructions_Table.row_actions[2].action_name (Delete action not in description)

**Phantoms (hallucinations):**

- Account_Transfers_Form.fields.From_Account (not mentioned in description)
- Account_Transfers_Form.fields.To_Account_Type (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Transfer_Type (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Priority (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Amount (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Frequency (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Interval (not mentioned in description)

**Fixes applied:**

- Add 'From_Account' field to 'Account_Transfers_Form.fields'
- Add 'To_Account_Type' field to 'Account_Transfers_Form.fields'
- Remove 'Enable' action from 'Standing_Instructions_Table.row_actions'
- Remove 'Disable' action from 'Standing_Instructions_Table.row_actions'
- Remove 'Delete' action from 'Standing_Instructions_Table.row_actions'
- Remove 'Transfer_Type' field from 'Create_Standing_Instruction_Form.fields'
- Remove 'Priority' field from 'Create_Standing_Instruction_Form.fields'
- Remove 'Amount' field from 'Create_Standing_Instruction_Form.fields'
- Remove 'Recurrence_Frequency' field from 'Create_Standing_Instruction_Form.fields'
- Remove 'Recurrence_Interval' field from 'Create_Standing_Instruction_Form.fields'

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account_Type
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account

**Phantoms (hallucinations):**

- Create_Tax_Component_Form.fields.Credit_Account_Type (not mentioned in description)
- Create_Tax_Component_Form.fields.Credit_Account (not mentioned in description)

**Fixes applied:**

- Add Credit_Account_Type and Credit_Account fields to Create_Tax_Group_Form.fields.Tax_Components.item_fields
- Remove Credit_Account_Type and Credit_Account fields from Create_Tax_Component_Form.fields

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Holidays_Page.submit_actions[0].fields.Repayements_Rescheduled_To
- Payment_Types_Page.submit_actions[0].fields

**Phantoms (hallucinations):**

- Holidays_Page.submit_actions[0].fields.Repayements_Rescheduled_To (not mentioned in description)
- Payment_Types_Page.submit_actions[0] (Create button not specified in description)

**Fixes applied:**

- Add 'Repayments_Rescheduled_To' field under Holidays_Page.submit_actions[0].fields
- Remove 'Create' button from Payment_Types_Page.submit_actions[0] as it is not specified in the description

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms identified in the AST.

**Missing:**

- Manage_Scheduler_Jobs.columns[3] (Previous_Run_Status should include Success/Failed with start/end times)
- Audit_Trails.columns[8] (Client/Loan/Savings details should be specified)
- Audit_Trails.filters.search_fields[4] (Maker_ID should be included)
- Audit_Trails.filters.search_fields[5] (Checker_ID should be included)

**Phantoms (hallucinations):**

- Manage_Scheduler_Jobs.global_actions[0] (Start/Stop Scheduler action not explicitly named in description)
- Manage_Codes.columns[0] (Clicking a code to open its values for adding, editing, reordering, and deactivating entries is not represented)
- Manage_Data_Tables.fields.Column_Definitions.item_fields[0] (Adding, editing, reordering, and deactivating entries is not represented)

**Fixes applied:**

- Add 'Previous_Run_Status' column to 'Manage_Scheduler_Jobs' with details for Success/Failed with start/end times.
- Add 'Client/Loan/Savings_Details' column to 'Audit_Trails'.
- Include 'Maker_ID' and 'Checker_ID' in the search fields for 'Audit_Trails'.
- Remove phantom actions and fields that are not explicitly mentioned in the description.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
