# Workflow Critique — Mifos

Generated: 2026-06-09T09:49:13.873274Z

## Login

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Home Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflow for the Search Activity input field.

**Missing workflows:**

- No workflow for Search_Activity_Input: action=Search

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Search_Activity_Input with the appropriate terminal action.

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and match the actions described in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Global Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the search results dropdown based on entity types.

**Missing workflows:**

- No workflow for Search_Results: entity_type=Clients
- No workflow for Search_Results: entity_type=Groups
- No workflow for Search_Results: entity_type=Loans
- No workflow for Search_Results: entity_type=Savings accounts

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Search_Results based on entity types: Clients, Groups, Loans, Savings accounts

---

## Client Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions and phantom workflows detected.

**Missing workflows:**

- No workflow for state_bound_action_bar: state=Active, action=Edit
- No workflow for state_bound_action_bar: state=Active, action=Transfer Client
- No workflow for state_bound_action_bar: state=Active, action=Close
- No workflow for state_bound_action_bar: state=Active, action=Add Charge
- No workflow for state_bound_action_bar: state=Active, action=New Loan
- No workflow for state_bound_action_bar: state=Active, action=New Savings
- No workflow for state_bound_action_bar: state=Active, action=New Share Account
- No workflow for state_bound_action_bar: state=Rejected, action=Edit
- No workflow for state_bound_action_bar: state=Withdrawn, action=Edit

**Phantom workflows:**

- WF-007 terminal_action=Edit not found in any AST node
- WF-008 terminal_action=Reject not found in any AST node
- WF-009 terminal_action=Withdraw not found in any AST node
- WF-010 terminal_action=Reactivate not found in any AST node

**Fixes applied:**

- Add workflows for missing state-bound actions for Active and Rejected states.
- Remove phantom workflows WF-007, WF-008, WF-009, WF-010.

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for bulk actions and a phantom workflow for the terminal action 'Upload'.

**Missing workflows:**

- No workflow for Groups_Page: bulk action=Create New Group
- No workflow for Bulk_Import_Groups_Page: submit_action=Upload

**Phantom workflows:**

- WF-003 terminal_action=Upload not found in any AST node

**Fixes applied:**

- Add workflow for Groups_Page: bulk action=Create New Group
- Add workflow for Bulk_Import_Groups_Page: submit_action=Upload
- Remove phantom workflow WF-003

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Bulk Import Centers page submit action.

**Missing workflows:**

- No workflow for Bulk_Import_Centers_Page: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Bulk_Import_Centers_Page: action=Submit

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Loan_Product_Stepper: step=1, action=Submit
- No workflow for Loan_Product_Stepper: step=2, action=Submit
- No workflow for Loan_Product_Stepper: step=3, action=Submit
- No workflow for Loan_Product_Stepper: step=4, action=Submit
- No workflow for Loan_Product_Stepper: step=5, action=Submit
- No workflow for Loan_Product_Stepper: step=6, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Loan_Product_Stepper submit actions for each step.

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form submit actions in the stepper wizards.

**Missing workflows:**

- No workflow for Savings_Product_Stepper: step=1, action=Submit
- No workflow for Fixed_Deposit_Products_Stepper: step=1, action=Submit
- No workflow for Recurring_Deposit_Products_Stepper: step=1, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Savings_Product_Stepper: step=1, action=Submit
- Add workflows for Fixed_Deposit_Products_Stepper: step=1, action=Submit
- Add workflows for Recurring_Deposit_Products_Stepper: step=1, action=Submit

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form fields and state actions.

**Missing workflows:**

- No workflow for Share_Product_Stepper: step=1, action=Next
- No workflow for Share_Product_Stepper: step=2, action=Next
- No workflow for Share_Product_Stepper: step=3, action=Next
- No workflow for Share_Product_Stepper: step=4, action=Next
- No workflow for Share_Product_Stepper: step=5, action=Next
- No workflow for Share_Product_Stepper: step=6, action=Next
- No workflow for Share_Product_Stepper: step=7, action=Finish

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Share_Product_Stepper: step=1, action=Next
- Add workflows for Share_Product_Stepper: step=2, action=Next
- Add workflows for Share_Product_Stepper: step=3, action=Next
- Add workflows for Share_Product_Stepper: step=4, action=Next
- Add workflows for Share_Product_Stepper: step=5, action=Next
- Add workflows for Share_Product_Stepper: step=6, action=Next
- Add workflows for Share_Product_Stepper: step=7, action=Finish

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Charge_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Charge_Form: terminal_action=Submit

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Creation_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Creation_Form: action=Submit

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for required form fields and state actions.

**Missing workflows:**

- No workflow for Create_Delinquency_Range_Form: terminal action=Submit with required fields Classification and Minimum_Age_Days
- No workflow for Create_Delinquency_Bucket_Form: terminal action=Submit with required field Bucket_Name

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Delinquency_Range_Form with terminal action=Submit
- Add workflows for Create_Delinquency_Bucket_Form with terminal action=Submit

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state actions in the Loan Detail Actions component.

**Missing workflows:**

- No workflow for state_bound_action_bar: state=Approved, action=Undo Approval

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for state_bound_action_bar: state=Approved, action=Undo Approval

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for state-bound actions in the Dormant, Closed, and Blocked states.

**Missing workflows:**

- No workflow for state_bound_action_bar: state=Dormant, action=No actions for Dormant Savings Account
- No workflow for state_bound_action_bar: state=Closed, action=No actions for Closed Savings Account
- No workflow for state_bound_action_bar: state=Blocked, action=No actions for Blocked Savings Account

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Dormant, Closed, and Blocked states with appropriate actions.

---

## Share Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Share_Account_Application_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Share_Account_Application_Form: action=Submit

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correct according to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_GL_Account_Form: terminal action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_GL_Account_Form: terminal action=Submit

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and data table actions.

**Missing workflows:**

- No workflow for Journal_Entry_Creation_Form: terminal action=Submit
- No workflow for Closing_Entries_Table: row action=View
- No workflow for Closing_Entries_Table: row action=Edit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Journal_Entry_Creation_Form: terminal action=Submit
- Add workflows for Closing_Entries_Table: row action=View
- Add workflows for Closing_Entries_Table: row action=Edit

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Rule_Form: terminal_action=Submit
- No workflow for Financial_Activity_Mappings_Table: action=Create Mapping

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Rule_Form: terminal_action=Submit
- Add workflow for Financial_Activity_Mappings_Table: action=Create Mapping

---

## Provisioning

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Creation_Form: action=+ Create
- No workflow for Provisioning_Entries_Table: action=+ Create Provisioning Entry

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Creation_Form: action=+ Create
- Add workflow for Provisioning_Entries_Table: action=+ Create Provisioning Entry

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Office_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Office_Form: terminal_action=Submit

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

- No workflow for Create_Teller_Form: terminal_action=Submit
- No workflow for Cashier_Detail: action=Allocate Cash
- No workflow for Cashier_Detail: action=Settle Cash

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Teller_Form: terminal_action=Submit
- Add workflow for Cashier_Detail: action=Allocate Cash
- Add workflow for Cashier_Detail: action=Settle Cash

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

Missing workflows for form submit actions related to the parameters form.

**Missing workflows:**

- No workflow for Parameters_Form: action=Run_Report

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Parameters_Form: action=Run_Report

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Account_Transfers_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Account_Transfers_Form: action=Submit

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Tax_Component_Form: terminal_action=Submit
- No workflow for Create_Tax_Group_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Tax_Component_Form: terminal_action=Submit
- Add workflows for Create_Tax_Group_Form: terminal_action=Submit

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Working_Days_Page: action=Submit
- No workflow for Bulk_Import_Page: action=Submit
- No workflow for Currencies_Page: action=Submit
- No workflow for Funds_Page: action=Create Fund
- No workflow for Payment_Types_Page: action=+ Create

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing form submit actions: Working_Days_Page, Bulk_Import_Page, Currencies_Page, Funds_Page, Payment_Types_Page

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state machine actions.

**Missing workflows:**

- No workflow for Manage_Data_Tables: action=Submit
- No workflow for Audit_Trails: state=Pending, action=Approve
- No workflow for Audit_Trails: state=Pending, action=Reject

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Manage_Data_Tables: action=Submit
- Add workflow for Audit_Trails: state=Pending, action=Approve
- Add workflow for Audit_Trails: state=Pending, action=Reject

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---
