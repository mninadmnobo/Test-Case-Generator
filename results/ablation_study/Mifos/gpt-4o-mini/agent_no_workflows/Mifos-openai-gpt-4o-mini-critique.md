# Semantic Critique — Mifos

Generated: 2026-06-10T19:15:11.494431Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the Remember me checkbox and has a phantom Language_Selector field.

**Missing:**

- Login_Form.fields.Remember_Me

**Phantoms (hallucinations):**

- Login_Form.fields.Language_Selector (not mentioned in description)

**Fixes applied:**

- Add a Remember_Me field to Login_Form.fields
- Remove Language_Selector from Login_Form.fields

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains phantoms and missing elements related to the summary cards.

**Missing:** none

**Phantoms (hallucinations):**

- Summary_Cards.item_fields.Amount_Pending_Disbursed (field name not specified in description)
- Summary_Cards.item_fields.Amount_Collected (field name not specified in description)

**Fixes applied:**

- Rename Summary_Cards.item_fields.Amount_Pending_Disbursed to a name specified in the description.
- Rename Summary_Cards.item_fields.Amount_Collected to a name specified in the description.

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

The AST is missing several required fields and contains phantoms.

**Missing:**

- Create_Client_Wizard.steps[2].fields
- Create_Client_Wizard.steps[3].fields
- Client_Detail_Tabs.tabs[0].fields
- Client_Detail_Tabs.tabs[1].fields
- Client_Detail_Tabs.tabs[3].fields
- Client_Detail_Tabs.tabs[4].fields

**Phantoms (hallucinations):**

- Bulk_Import_Page.submit_actions[1] (Upload File button not in description)
- Client_Detail_Tabs.tabs[2].fields.Document_Type (Document_Type field in Identifiers tab not in description)
- Client_Detail_Tabs.tabs[2].fields.Document_Key (Document_Key field in Identifiers tab not in description)

**Fixes applied:**

- Create_Client_Wizard.steps[2].fields should be an empty object
- Create_Client_Wizard.steps[3].fields should be an empty object
- Client_Detail_Tabs.tabs[0].fields should be an empty object
- Client_Detail_Tabs.tabs[1].fields should be an empty object
- Client_Detail_Tabs.tabs[3].fields should be an empty object
- Client_Detail_Tabs.tabs[4].fields should be an empty object
- Remove Bulk_Import_Page.submit_actions[1]
- Remove Client_Detail_Tabs.tabs[2].fields.Document_Type
- Remove Client_Detail_Tabs.tabs[2].fields.Document_Key

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Bulk_Import_Groups_Page.fields.Groups_Template
- Bulk_Import_Groups_Page.fields.Office
- Bulk_Import_Groups_Page.fields.Staff
- Bulk_Import_Groups_Page.fields.Download
- Group_Detail_Page.fields.Loan_Accounts
- Group_Detail_Page.fields.Savings_Accounts
- Group_Detail_Page.fields.Collection_Sheet

**Phantoms (hallucinations):**

- Bulk_Import_Groups_Page.fields.Groups_Upload (not specified in description)
- Group_Detail_Page.fields.Group_Name (passive display field)
- Group_Detail_Page.fields.Account_Number (passive display field)
- Group_Detail_Page.fields.Status (passive display field)
- Group_Detail_Page.fields.Office (passive display field)
- Group_Detail_Page.fields.Staff (passive display field)

**Fixes applied:**

- Add 'Groups_Template' field to 'Bulk_Import_Groups_Page.fields'
- Add 'Office' field to 'Bulk_Import_Groups_Page.fields'
- Add 'Staff' field to 'Bulk_Import_Groups_Page.fields'
- Add 'Download' button to 'Bulk_Import_Groups_Page.fields'
- Add 'Loan_Accounts' field to 'Group_Detail_Page.fields'
- Add 'Savings_Accounts' field to 'Group_Detail_Page.fields'
- Add 'Collection_Sheet' field to 'Group_Detail_Page.fields'

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms detected in the AST.

**Missing:**

- Bulk_Import_Centers_Page.fields.template-download (file-upload pattern not fully represented)
- Center_Detail_Page.action_buttons (Activate, Edit, Close, Assign Staff buttons missing)

**Phantoms (hallucinations):**

- Centers_Page.row_actions[0] (View action not mentioned in description)
- Bulk_Import_Centers_Page.fields.template-download (field not explicitly mentioned in description)

**Fixes applied:**

- Add action buttons to Center_Detail_Page: Activate, Edit, Close, Assign Staff
- Remove View action from Centers_Page.row_actions as it is not mentioned in the description

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing required fields and phantoms present in the AST.

**Missing:**

- Loan_Product_Stepper_Wizard.steps[2].fields.Principal_Amount.constraints[0] (Minimum value required not explicitly stated)
- Loan_Product_Stepper_Wizard.steps[2].fields.Principal_Amount.constraints[1] (Default value required not explicitly stated)
- Loan_Product_Stepper_Wizard.steps[2].fields.Principal_Amount.constraints[2] (Maximum value required not explicitly stated)
- Loan_Product_Stepper_Wizard.steps[3].fields.Grace_Period (required field missing)
- Loan_Product_Stepper_Wizard.steps[3].fields.Arrears_Tolerance (required field missing)
- Loan_Product_Stepper_Wizard.steps[4].fields.Number_of_Repayments.constraints[0] (Minimum value required not explicitly stated)
- Loan_Product_Stepper_Wizard.steps[4].fields.Number_of_Repayments.constraints[1] (Default value required not explicitly stated)
- Loan_Product_Stepper_Wizard.steps[4].fields.Number_of_Repayments.constraints[2] (Maximum value required not explicitly stated)

**Phantoms (hallucinations):**

- Loan_Product_Stepper_Wizard.steps[2].fields.Currency_Selection (not explicitly mentioned in description)
- Loan_Product_Stepper_Wizard.steps[3].fields.Repayment_Strategy (not explicitly mentioned in description)
- Loan_Product_Stepper_Wizard.steps[4].fields.Repaid_Every (not explicitly mentioned in description)
- Loan_Product_Stepper_Wizard.steps[6].fields.GL_Account_Mappings (not explicitly mentioned in description)

**Fixes applied:**

- Add constraints for Principal_Amount in step 2 as required.
- Add required fields Grace_Period and Arrears_Tolerance in step 3.
- Add constraints for Number_of_Repayments in step 4 as required.
- Remove phantom fields Currency_Selection, Repayment_Strategy, Repaid_Every, and GL_Account_Mappings.

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields for the Fixed Deposit and Recurring Deposit Products steps.

**Missing:**

- Fixed_Deposit_Products_Stepper.steps[5].fields.Pre_Mature_Closure_Applicable
- Fixed_Deposit_Products_Stepper.steps[6].fields.Minimum_Deposit_Term
- Fixed_Deposit_Products_Stepper.steps[6].fields.Maximum_Deposit_Term
- Fixed_Deposit_Products_Stepper.steps[6].fields.In_Multiples_Of
- Fixed_Deposit_Products_Stepper.steps[6].fields.Minimum_Deposit_Amount
- Fixed_Deposit_Products_Stepper.steps[6].fields.Maximum_Deposit_Amount
- Fixed_Deposit_Products_Stepper.steps[6].fields.Default_Deposit_Amount
- Recurring_Deposit_Products_Stepper.steps[1].fields.Is_Mandatory_Deposit

**Phantoms:** none

**Fixes applied:**

- Add required fields for Fixed Deposit Products steps as per description.
- Add Is_Mandatory_Deposit field in Recurring Deposit Products step 1.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items: 1 critical (Currency field should be required), and there are phantoms present.

**Missing:**

- Create_Share_Product_Stepper.steps[2].fields.Currency.required

**Phantoms (hallucinations):**

- Create_Share_Product_Stepper.steps[2].fields.Decimal_Places (not mentioned in description)
- Create_Share_Product_Stepper.steps[2].fields.Currency_In_Multiples_Of (not mentioned in description)
- Create_Share_Product_Stepper.steps[3].fields.Shares_to_be_Issued (not mentioned in description)
- Create_Share_Product_Stepper.steps[3].fields.Capital_Value (not mentioned in description)
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Maximum_Nominal_Shares_per_Client (not mentioned in description)
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency (not mentioned in description)
- Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period (not mentioned in description)
- Create_Share_Product_Stepper.steps[6].fields.Search_and_Add (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.GL_Account_Mappings (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.Share_Reference (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.Share_Suspense (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.Equity_in_Shares (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.Income_from_Fees (not mentioned in description)
- Create_Share_Product_Stepper.steps[7].fields.Share_Equity (not mentioned in description)

**Fixes applied:**

- Create_Share_Product_Stepper.steps[2].fields.Currency.required = true
- Remove fields: Create_Share_Product_Stepper.steps[2].fields.Decimal_Places
- Remove fields: Create_Share_Product_Stepper.steps[2].fields.Currency_In_Multiples_Of
- Remove fields: Create_Share_Product_Stepper.steps[3].fields.Shares_to_be_Issued
- Remove fields: Create_Share_Product_Stepper.steps[3].fields.Capital_Value
- Remove fields: Create_Share_Product_Stepper.steps[4].fields.Minimum_Maximum_Nominal_Shares_per_Client
- Remove fields: Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency
- Remove fields: Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period
- Remove fields: Create_Share_Product_Stepper.steps[6].fields.Search_and_Add
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.GL_Account_Mappings
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.Share_Reference
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.Share_Suspense
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.Equity_in_Shares
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.Income_from_Fees
- Remove fields: Create_Share_Product_Stepper.steps[7].fields.Share_Equity

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and has phantoms.

**Missing:**

- Create_Charge_Form.fields.Charge_Time_Type.options
- Create_Charge_Form.fields.Charge_Time_Type.required
- Create_Charge_Form.fields.Charge_Time_Type.type

**Phantoms (hallucinations):**

- Create_Charge_Form.fields.Charge_Time_Type (options vary by entity not reflected)
- Create_Charge_Form.fields.Charge_Calculation_Type.required (not specified in description)
- Create_Charge_Form.fields.Tax_Group.required (not specified in description)
- Create_Charge_Form.fields.Payment_Mode.required (not specified in description)

**Fixes applied:**

- Create_Charge_Form.fields.Charge_Time_Type: Add 'required: true' and specify options based on entity.
- Create_Charge_Form.fields.Charge_Calculation_Type: Add 'required: true'.
- Create_Charge_Form.fields.Tax_Group: Add 'required: true'.
- Create_Charge_Form.fields.Payment_Mode: Add 'required: true'.

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Create_Floating_Rate_Form.fields.Rate_Periods
- Create_Floating_Rate_Form.fields.Rate_Periods.rows[0].From_Date
- Create_Floating_Rate_Form.fields.Rate_Periods.rows[0].Interest_Rate
- Create_Floating_Rate_Form.fields.Rate_Periods.rows[0].Is_Differential_Rate

**Phantoms (hallucinations):**

- Floating_Rates_Table.row_actions[0] (View action not in description)
- Floating_Rates_Table.row_actions[1] (Edit action not in description)

**Fixes applied:**

- Add Rate_Periods table to Create_Floating_Rate_Form.fields
- Add From_Date, Interest_Rate, and Is_Differential_Rate fields to Rate_Periods

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Delinquency_Buckets_Page.fields.Delinquency_Ranges

**Phantoms (hallucinations):**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Range_Name (not explicitly mentioned in description)

**Fixes applied:**

- Add Delinquency_Buckets_Page.fields.Delinquency_Ranges as a repeating group with appropriate item fields.
- Remove Range_Name from Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Loan_Application_Wizard.steps[2].fields.Grace_Period
- Loan_Detail_Page.action_buttons.Active[0].fields.Payment_Type.options

**Phantoms (hallucinations):**

- Loan_Application_Wizard.steps[3].fields.Inherited_Charges (not mentioned in description)
- Loan_Detail_Page.action_buttons.Active[0].fields.Transaction_Amount (should be pre-filled with amount due)

**Fixes applied:**

- Add 'Grace_Period' field to Loan_Application_Wizard.steps[2].fields
- Populate 'Payment_Type.options' in Loan_Detail_Page.action_buttons.Active[0].fields.Transaction_Amount

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected elements and contains phantoms.

**Missing:**

- Savings_Account_Detail_Page.tabs[0].fields.Account_Number
- Savings_Account_Detail_Page.tabs[0].fields.Product_Name
- Savings_Account_Detail_Page.tabs[0].fields.Client_Name
- Savings_Account_Detail_Page.tabs[0].fields.Account_Balance
- Savings_Account_Detail_Page.tabs[0].fields.Available_Balance
- Savings_Account_Detail_Page.tabs[0].fields.Status_Badge
- Savings_Account_Detail_Page.tabs[1].fields.Date
- Savings_Account_Detail_Page.tabs[1].fields.Type
- Savings_Account_Detail_Page.tabs[1].fields.Amount
- Savings_Account_Detail_Page.tabs[1].fields.Running_Balance

**Phantoms (hallucinations):**

- Savings_Account_Detail_Page.tabs[0].fields.Status (not explicitly mentioned in description)
- Savings_Account_Detail_Page.tabs[0].fields.Status_Badge (passive display field)
- Savings_Account_Detail_Page.tabs[1].row_actions[0] (View action not mentioned in description)
- Savings_Account_Detail_Page.tabs[1].row_actions[1] (Edit action not mentioned in description)
- Savings_Account_Detail_Page.tabs[1].row_actions[2] (Delete action not mentioned in description)

**Fixes applied:**

- Add missing fields to Savings_Account_Detail_Page.tabs[0]: Account_Number, Product_Name, Client_Name, Account_Balance, Available_Balance, Status_Badge
- Add missing fields to Savings_Account_Detail_Page.tabs[1]: Date, Type, Amount, Running_Balance
- Remove phantom fields from Savings_Account_Detail_Page.tabs[0]: Status, Status_Badge
- Remove phantom actions from Savings_Account_Detail_Page.tabs[1]: View, Edit, Delete

---

## Share Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Share_Account_Application_Form.fields.External_ID
- Share_Account_Detail_Page.tabs[0].fields.Amount
- Share_Account_Detail_Page.tabs[0].fields.Status
- Share_Account_Detail_Page.tabs[1].fields.Amount_Per_Share
- Share_Account_Detail_Page.tabs[1].fields.Total_Amount

**Phantoms (hallucinations):**

- Share_Account_Detail_Page.tabs[0].fields.Type (invented field in Purchased Shares tab)
- Share_Account_Detail_Page.tabs[0].fields.Date (passive display field not in description)
- Share_Account_Detail_Page.tabs[1].fields.Date (passive display field not in description)

**Fixes applied:**

- Add 'External_ID' field to 'Share_Account_Application_Form.fields'
- Add 'Amount' field to 'Share_Account_Detail_Page.tabs[0].fields'
- Add 'Status' field to 'Share_Account_Detail_Page.tabs[0].fields'
- Add 'Amount_Per_Share' field to 'Share_Account_Detail_Page.tabs[1].fields'
- Add 'Total_Amount' field to 'Share_Account_Detail_Page.tabs[1].fields'
- Remove 'Type' field from 'Share_Account_Detail_Page.tabs[0].fields'
- Remove 'Date' field from 'Share_Account_Detail_Page.tabs[0].fields'
- Remove 'Date' field from 'Share_Account_Detail_Page.tabs[1].fields'

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items include Deposit Period unit and critical action buttons for the RD Account Detail page.

**Missing:**

- FD_Account_Creation_Form.fields.Deposit_Period.unit
- RD_Account_Detail.row_actions[3] (Close on Maturity button not in description)

**Phantoms:** none

**Fixes applied:**

- Add 'unit' field to 'FD_Account_Creation_Form.fields.Deposit_Period' with options for Days, Months, Years.
- Add 'Close on Maturity' action button to 'RD_Account_Detail.row_actions'.

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Journal_Entry_Creation_Form.fields.Entry_Lines.item_fields.Add_Row
- Journal_Entry_Creation_Form.constraints[1] (validation error blocking submission not present)
- Closure_Creation_Form.preconditions[1] (missing explicit trigger language)

**Phantoms (hallucinations):**

- Journal_Entry_Creation_Form.fields.Payment_Details (not mentioned in description)
- Journal_Entry_Creation_Form.constraints[0] (constraint phrasing inferred, not stated)

**Fixes applied:**

- Add 'Add_Row' field to 'Journal_Entry_Creation_Form.fields.Entry_Lines.item_fields'
- Add a validation error constraint to 'Journal_Entry_Creation_Form.constraints'
- Clarify precondition language in 'Closure_Creation_Form.preconditions'

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Rule_Form.fields.Office.required (should be true)
- Accounting_Rules_Table.row_actions[0].action_name (Edit action is missing)
- Accounting_Rules_Table.row_actions[1].action_name (Delete action is missing)
- Financial_Activity_Mappings_Table.row_actions (should include actions for mapping)

**Phantoms (hallucinations):**

- Create_Rule_Form.fields.Rule_Name.type (should be text instead of unspecified)
- Create_Mapping_Form.fields.GL_Account.type (should be text instead of dropdown)

**Fixes applied:**

- Set Create_Rule_Form.fields.Office.required to true
- Add Edit action to Accounting_Rules_Table.row_actions
- Add Delete action to Accounting_Rules_Table.row_actions
- Add row_actions to Financial_Activity_Mappings_Table
- Change Create_Rule_Form.fields.Rule_Name.type to text
- Change Create_Mapping_Form.fields.GL_Account.type to text

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Office_Form.fields.External_ID (not specified as required in description)

**Fixes applied:**

- Update Create_Office_Form.fields.External_ID to be required based on description.

---

## Employees

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Employees_Table.row_actions[0].action_name (Edit action is not linked to a specific employee)
- Create_Employee_Form.fields.Is_Loan_Officer (should be included in the dropdown context)
- Staff_Detail_Page.fields.Name (should be a clickable link)

**Phantoms (hallucinations):**

- Create_Employee_Form.fields.Mobile_Number (not mentioned as required in the description)
- Staff_Detail_Page.fields.Name (passive display field not in description)

**Fixes applied:**

- Add 'Edit' action to Employees_Table.row_actions linked to specific employee.
- Include 'Is_Loan_Officer' in the dropdown context for loan creation.
- Make 'Name' in Staff_Detail_Page a clickable link.

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing required fields and contains phantoms.

**Missing:**

- Teller_Detail.fields.Cashiers.row_actions[0] (Edit option missing)
- Teller_Detail.fields.Cashiers.row_actions[0] (Allocate Cashier button missing)

**Phantoms (hallucinations):**

- Create_Teller_Form.fields.Description (not specified as required or optional in description)
- Allocate_Cashier_Form.fields.Description (not specified as required or optional in description)
- Cashier_Detail.fields.Opening_Balance (not specified in description)
- Cashier_Detail.fields.Cash_In_Hand (not specified in description)

**Fixes applied:**

- Add 'Edit' option to 'Teller_Detail.fields.Cashiers.row_actions'
- Add '+ Allocate Cashier' button to 'Teller_Detail.fields.Cashiers.row_actions'
- Remove 'Description' field from 'Create_Teller_Form.fields' and 'Allocate_Cashier_Form.fields'
- Remove 'Opening_Balance' and 'Cash_In_Hand' fields from 'Cashier_Detail.fields'

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing items and phantoms in the AST.

**Missing:**

- Create_User_Form.fields.Staff (Staff dropdown should be required)
- Create_User_Form.fields.Roles (Roles should be required)
- Create_Role_Form.fields.Description (Description should be required)

**Phantoms (hallucinations):**

- Create_User_Form.fields.Staff (Staff dropdown not mentioned in description)
- Create_User_Form.fields.Roles (Roles field not mentioned as optional)
- Permissions_Page.fields.Permissions (Permissions matrix not explicitly described)

**Fixes applied:**

- Create_User_Form.fields.Staff: change required to true
- Create_User_Form.fields.Roles: change required to true
- Create_Role_Form.fields.Description: change required to true
- Permissions_Page.fields.Permissions: remove this field as it is a phantom

---

## Reports

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements related to the reports and has phantoms present.

**Missing:**

- Reports_Page.sortable_columns
- Reports_Page.row_actions
- Reports_Page.bulk_actions

**Phantoms (hallucinations):**

- Parameters_Form.fields.Fund (dropdown not specified in description)
- Parameters_Form.fields.Office (field not specified as required)
- Parameters_Form.fields.Branch (field not specified as required)
- Parameters_Form.fields.Currency (field not specified as required)
- Parameters_Form.fields.Loan_Product (field not specified as required)
- Parameters_Form.fields.Date_Range (field not specified as required)
- Parameters_Form.fields.Loan_Officer (field not specified as required)

**Fixes applied:**

- Add sortable_columns to Reports_Page
- Add row_actions to Reports_Page
- Add bulk_actions to Reports_Page
- Remove Fund field from Parameters_Form.fields
- Set all fields in Parameters_Form.fields to required: true

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Account_Transfers_Form.fields.From_Account
- Account_Transfers_Form.fields.To_Account

**Phantoms (hallucinations):**

- Standing_Instructions_Table.bulk_actions[0] (Enable action not in description)
- Standing_Instructions_Table.bulk_actions[1] (Disable action not in description)
- Standing_Instructions_Table.bulk_actions[2] (Delete action not in description)

**Fixes applied:**

- Add 'From_Account' field to 'Account_Transfers_Form.fields'
- Add 'To_Account' field to 'Account_Transfers_Form.fields'
- Remove 'Enable' action from 'Standing_Instructions_Table.bulk_actions'
- Remove 'Disable' action from 'Standing_Instructions_Table.bulk_actions'
- Remove 'Delete' action from 'Standing_Instructions_Table.bulk_actions'

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Debit_Account_Type
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Debit_Account

**Phantoms (hallucinations):**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account_Type (not mentioned in description)
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account (not mentioned in description)

**Fixes applied:**

- Add Debit_Account_Type and Debit_Account fields to Create_Tax_Group_Form.fields.Tax_Components.item_fields
- Remove Credit_Account_Type and Credit_Account from Create_Tax_Group_Form.fields.Tax_Components.item_fields

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms detected in the AST.

**Missing:**

- Working_Days_Page.fields.Working_Days.options
- Currencies_Page.fields
- Funds_Page.fields
- Bulk_Import_Page.fields.Upload_Interface

**Phantoms (hallucinations):**

- Working_Days_Page.fields.Repayment_Rescheduling (not explicitly mentioned in description)
- Payment_Types_Page.fields (no fields defined despite description mentioning columns)

**Fixes applied:**

- Add options for Working_Days_Page.fields.Working_Days
- Define fields for Currencies_Page and Funds_Page
- Add Upload_Interface to Bulk_Import_Page.fields

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected interactive elements and contains phantoms.

**Missing:**

- Manage_Scheduler_Jobs.row_actions[0].fields.Job_Name
- Manage_Scheduler_Jobs.row_actions[0].fields.Previous_Run_Status.start_time
- Manage_Scheduler_Jobs.row_actions[0].fields.Previous_Run_Status.end_time
- Manage_Codes.row_actions[0].fields.Values
- Audit_Trails.row_actions[0].fields.Action_Name
- Audit_Trails.row_actions[0].fields.Entity_Name
- Audit_Trails.row_actions[0].fields.Resource_ID
- Audit_Trails.row_actions[0].fields.Processing_Result

**Phantoms (hallucinations):**

- Manage_Scheduler_Jobs.row_actions[0].fields.Currently_Running (not mentioned in description)
- Audit_Trails.row_actions[0].action_name (View button not mentioned in description)

**Fixes applied:**

- Add Job_Name field to Manage_Scheduler_Jobs.row_actions[0].fields
- Add Previous_Run_Status.start_time and Previous_Run_Status.end_time fields to Manage_Scheduler_Jobs.row_actions[0].fields
- Add Values field to Manage_Codes.row_actions[0].fields
- Add Action_Name, Entity_Name, Resource_ID, and Processing_Result fields to Audit_Trails.row_actions[0].fields
- Remove Currently_Running field from Manage_Scheduler_Jobs.row_actions[0].fields
- Remove View action from Audit_Trails.row_actions[0]

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
