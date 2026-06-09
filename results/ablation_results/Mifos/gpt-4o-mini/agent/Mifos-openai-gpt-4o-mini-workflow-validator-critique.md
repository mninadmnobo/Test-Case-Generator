# Workflow Critique — Mifos

Generated: 2026-06-09T09:26:36.651465Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the form submit action has missing combinations for required fields.

**Missing workflows:**

- No workflow for Login_Form: submit_action=Login with condition=valid credentials

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Login_Form: submit_action=Login with condition=valid credentials

---

## Home Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form actions and a phantom workflow detected.

**Missing workflows:**

- No workflow for button: action=Dashboard_Button
- No workflow for search: action=Search_Activity

**Phantom workflows:**

- WF-002 terminal_action=Search not found in any AST node

**Fixes applied:**

- Add workflow for button: action=Dashboard_Button
- Add workflow for search: action=Search_Activity
- Remove phantom WF-002 terminal_action=Search

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Summary_Cards display conditions.

**Missing workflows:**

- No workflow for Summary_Cards: display_when=data available, action=Amount Pending / Disbursed
- No workflow for Summary_Cards: display_when=data available, action=Amount Collected

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Summary_Cards: display_when=data available, action=Amount Pending / Disbursed
- Add workflows for Summary_Cards: display_when=data available, action=Amount Collected

---

## Global Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the case when no results are found is incorrectly linked to the Search_Results terminal action.

**Missing workflows:**

- No workflow for Search_Results: no results found action

**Phantom workflows:** none

**Fixes applied:**

- Remove WF-004 as it incorrectly links to Search_Results for no results found

---

## Client Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the data table actions.

**Missing workflows:**

- No workflow for Clients_Page: row_action=View

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Clients_Page: row_action=View

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form submit actions.

**Missing workflows:**

- No workflow for Create_Group_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Group_Form: terminal_action=Submit

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form submit actions and state actions.

**Missing workflows:**

- No workflow for Bulk_Import_Centers_Page: action=Submit
- No workflow for Center_Detail_Page: action=Activate
- No workflow for Center_Detail_Page: action=Edit
- No workflow for Center_Detail_Page: action=Close
- No workflow for Center_Detail_Page: action=Assign Staff

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing actions in Bulk_Import_Centers_Page and Center_Detail_Page

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Loan_Product_Stepper_Wizard: step=1, action=Submit
- No workflow for Loan_Product_Stepper_Wizard: step=2, action=Submit
- No workflow for Loan_Product_Stepper_Wizard: step=3, action=Submit
- No workflow for Loan_Product_Stepper_Wizard: step=4, action=Submit
- No workflow for Loan_Product_Stepper_Wizard: step=5, action=Submit
- No workflow for Loan_Product_Stepper_Wizard: step=6, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Loan_Product_Stepper_Wizard: step=1, action=Submit
- Add workflows for Loan_Product_Stepper_Wizard: step=2, action=Submit
- Add workflows for Loan_Product_Stepper_Wizard: step=3, action=Submit
- Add workflows for Loan_Product_Stepper_Wizard: step=4, action=Submit
- Add workflows for Loan_Product_Stepper_Wizard: step=5, action=Submit
- Add workflows for Loan_Product_Stepper_Wizard: step=6, action=Submit

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Savings_Product_Stepper: step=Details, action=Submit
- No workflow for Savings_Product_Stepper: step=Currency, action=Submit
- No workflow for Savings_Product_Stepper: step=Terms, action=Submit
- No workflow for Savings_Product_Stepper: step=Settings, action=Submit
- No workflow for Savings_Product_Stepper: step=Charges, action=Submit
- No workflow for Savings_Product_Stepper: step=Accounting, action=Submit
- No workflow for Fixed_Deposit_Products_Stepper: step=Pre-Closure, action=Submit
- No workflow for Fixed_Deposit_Products_Stepper: step=Deposit Term, action=Submit
- No workflow for Fixed_Deposit_Products_Stepper: step=Interest Rate Chart, action=Submit
- No workflow for Recurring_Deposit_Products_Stepper: step=Additional Features, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for all missing submit actions in Savings_Product_Stepper, Fixed_Deposit_Products_Stepper, and Recurring_Deposit_Products_Stepper.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form submit actions in the wizard steps.

**Missing workflows:**

- No workflow for Share_Product_Stepper_Wizard: step=1, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=2, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=3, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=4, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=5, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=6, action=Submit
- No workflow for Share_Product_Stepper_Wizard: step=7, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Share_Product_Stepper_Wizard: step=1, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=2, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=3, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=4, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=5, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=6, action=Submit
- Add workflows for Share_Product_Stepper_Wizard: step=7, action=Submit

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form fields and state actions.

**Missing workflows:**

- No workflow for Charge_Creation_Form: required fields Charge_Name, Charge_Applies_To, Currency, Charge_Time_Type, Charge_Calculation_Type, Amount must have corresponding workflows.

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Charge_Creation_Form submit_actions with required fields.
- Ensure all required fields have corresponding workflows.

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Floating_Rate_Form: terminal_action=Submit
- No workflow for Floating_Rates_Table: action=Edit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Floating_Rate_Form: terminal_action=Submit
- Add workflow for Floating_Rates_Table: action=Edit

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Delinquency_Range_Form: action=Submit
- No workflow for Create_Delinquency_Bucket_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Delinquency_Range_Form and Create_Delinquency_Bucket_Form with terminal action 'Submit'

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required actions in the Loan Application Wizard and Loan Detail Actions.

**Missing workflows:**

- No workflow for Loan_Application_Wizard: submit_action=Submit
- No workflow for state_bound_action_bar: state=Active, action=Make Repayment
- No workflow for state_bound_action_bar: state=Active, action=Waive Interest
- No workflow for state_bound_action_bar: state=Active, action=Write Off
- No workflow for state_bound_action_bar: state=Active, action=Close
- No workflow for state_bound_action_bar: state=Active, action=Reschedule
- No workflow for state_bound_action_bar: state=Active, action=Prepay Loan
- No workflow for state_bound_action_bar: state=Active, action=Foreclosure
- No workflow for state_bound_action_bar: state=Active, action=Charge Off
- No workflow for state_bound_action_bar: state=Active, action=Assign Loan Officer

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Loan_Application_Wizard: submit_action=Submit
- Add workflow for state_bound_action_bar: state=Active, action=Make Repayment
- Add workflow for state_bound_action_bar: state=Active, action=Waive Interest
- Add workflow for state_bound_action_bar: state=Active, action=Write Off
- Add workflow for state_bound_action_bar: state=Active, action=Close
- Add workflow for state_bound_action_bar: state=Active, action=Reschedule
- Add workflow for state_bound_action_bar: state=Active, action=Prepay Loan
- Add workflow for state_bound_action_bar: state=Active, action=Foreclosure
- Add workflow for state_bound_action_bar: state=Active, action=Charge Off
- Add workflow for state_bound_action_bar: state=Active, action=Assign Loan Officer

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions in the Pending and Approved states.

**Missing workflows:**

- No workflow for state_bound_action_bar: state=Pending, action=Withdraw Application
- No workflow for state_bound_action_bar: state=Approved, action=Activate
- No workflow for state_bound_action_bar: state=Approved, action=Undo Approval

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Withdraw Application in Pending state.
- Add workflows for Activate and Undo Approval in Approved state.

---

## Share Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state machine actions.

**Missing workflows:**

- No workflow for Share_Account_Application_Form: action=Submit
- No workflow for state_bound_action_bar: state=Pending, action=Approve
- No workflow for state_bound_action_bar: state=Pending, action=Reject
- No workflow for state_bound_action_bar: state=Approved, action=Activate
- No workflow for state_bound_action_bar: state=Approved, action=Undo Approval
- No workflow for state_bound_action_bar: state=Active, action=Apply Additional Shares
- No workflow for state_bound_action_bar: state=Active, action=Redeem Shares
- No workflow for state_bound_action_bar: state=Active, action=Close

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Share_Account_Application_Form: action=Submit
- Add workflow for state_bound_action_bar: state=Pending, action=Approve
- Add workflow for state_bound_action_bar: state=Pending, action=Reject
- Add workflow for state_bound_action_bar: state=Approved, action=Activate
- Add workflow for state_bound_action_bar: state=Approved, action=Undo Approval
- Add workflow for state_bound_action_bar: state=Active, action=Apply Additional Shares
- Add workflow for state_bound_action_bar: state=Active, action=Redeem Shares
- Add workflow for state_bound_action_bar: state=Active, action=Close

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for FD_Account_Creation_Form: terminal_action=Submit
- No workflow for RD_Account_Creation_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for FD_Account_Creation_Form: terminal_action=Submit
- Add workflows for RD_Account_Creation_Form: terminal_action=Submit

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is missing a workflow for the form's submit action.

**Missing workflows:**

- No workflow for Create_GL_Account_Form: terminal action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Create_GL_Account_Form: terminal action=Submit

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Add_Journal_Entry_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Add_Journal_Entry_Form: action=Submit

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Rule_Form: terminal_action=Submit
- No workflow for Create_Mapping_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Rule_Form: terminal_action=Submit
- Add workflows for Create_Mapping_Form: terminal_action=Submit

---

## Provisioning

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the form submit action and state machine actions.

**Missing workflows:**

- No workflow for Create_Criteria_Form: action=+ Create

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Criteria_Form: action=+ Create

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Office_Form: terminal action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Office_Form: terminal action=Submit

---

## Employees

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Employee_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Employee_Form: terminal_action=Submit

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Teller_Form: action=Submit
- No workflow for Teller_Detail: state=Cashiers_Section, action=Edit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Teller_Form: action=Submit
- Add workflow for Teller_Detail: state=Cashiers_Section, action=Edit

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_User_Form: terminal_action=Submit
- No workflow for Create_Role_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_User_Form and Create_Role_Form with terminal_action=Submit

---

## Reports

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for row actions in the data table.

**Missing workflows:**

- No workflow for data_table: action=Report_Parameters

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for data_table: action=Report_Parameters

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Account Transfers form submit action.

**Missing workflows:**

- No workflow for Account_Transfers_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Account_Transfers_Form: terminal_action=Submit

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Tax_Component_Form: terminal_action=Save
- No workflow for Create_Tax_Group_Form: terminal_action=Save

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Tax_Component_Form: terminal_action=Save
- Add workflows for Create_Tax_Group_Form: terminal_action=Save

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and a phantom workflow detected.

**Missing workflows:**

- No workflow for Holidays_Page: terminal action=+ Create Holiday
- No workflow for Funds_Page: terminal action=Create Fund
- No workflow for Payment_Types_Page: terminal action=+ Create

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing form submit actions: + Create Holiday, Create Fund, + Create

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Manage_Data_Tables: submit_action=Submit
- No workflow for Manage_Scheduler_Jobs: action=Start/Stop Scheduler

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Manage_Data_Tables: submit_action=Submit
- Add workflow for Manage_Scheduler_Jobs: action=Start/Stop Scheduler

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correct according to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---
