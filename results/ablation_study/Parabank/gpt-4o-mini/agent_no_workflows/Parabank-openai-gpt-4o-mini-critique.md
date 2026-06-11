# Semantic Critique — Parabank

Generated: 2026-06-10T20:11:17.884682Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the validation constraint for Confirm Password matching the Password field.

**Missing:**

- Sign_Up_Form.fields.Confirm_Password.constraints

**Phantoms:** none

**Fixes applied:**

- Add a constraint to Confirm_Password stating it must match the Password field.

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Accounts_Table.columns.Account_Status
- Accounts_Table.footer.Total_Balance

**Phantoms (hallucinations):**

- Accounts_Table.row_actions[0] (View Account action not in description)
- Accounts_Table.columns.Account_Number.type (should specify masked format)

**Fixes applied:**

- Add 'Account_Status' to 'Accounts_Table.columns'
- Remove 'View Account' action from 'Accounts_Table.row_actions'
- Specify 'Account_Number' type as 'masked'

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items include the contextual error messages for failed transfers and the handling of transaction ID.

**Missing:**

- Transfer_Form.submit_actions[0].on_failure
- Transfer_Form.submit_actions[0].transaction_id

**Phantoms:** none

**Fixes applied:**

- Add 'on_failure' to Transfer_Form.submit_actions[0] with contextual error messages.
- Add 'transaction_id' to Transfer_Form.submit_actions[0] for successful transfers.

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Loan_Application_Form.fields.Loan_Type.options
- Loan_Application_Form.submit_actions[0].preconditions

**Phantoms (hallucinations):**

- Loan_Simulation (button not in description)

**Fixes applied:**

- Add options for Loan_Type field in Loan_Application_Form.fields.Loan_Type
- Remove Loan_Simulation button from components

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Card_Request_Form.fields.Shipping_Address.constraints[0]
- Card_Controls_Form.fields.Travel_Notice.constraints[0]
- Card_Controls_Form.fields.Card_Status.options[0]

**Phantoms (hallucinations):**

- Card_Request_Form.fields.Account_to_Link (not specified in description)
- Card_Controls_Form.fields.New_Spending_Limit.constraints[0] (inferred constraint not stated in description)

**Fixes applied:**

- Add 'Shipping_Address' constraints to 'Card_Request_Form.fields.Shipping_Address'
- Add 'must be a valid date range' constraint to 'Card_Controls_Form.fields.Travel_Notice'
- Add 'Frozen' option to 'Card_Controls_Form.fields.Card_Status'

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Trade_Funds_Form.submit_actions[0].on_success (missing success message 'Trade executed successfully.')
- Recurring_Investment_Plan_Form.submit_actions[0].on_success (missing success message 'Plan created successfully.')
- Trade_Funds_Form.fields.Funding_or_Destination_Account (missing constraints for adequate balance)

**Phantoms (hallucinations):**

- Recurring_Investment_Plan_Form.fields.Fund_Symbol.constraints[0] (constraint 'must exist' not in description)
- Trade_Funds_Form.fields.Funding_or_Destination_Account (no constraints mentioned in description)

**Fixes applied:**

- Add success message 'Trade executed successfully.' to Trade_Funds_Form.submit_actions[0].on_success
- Add success message 'Plan created successfully.' to Recurring_Investment_Plan_Form.submit_actions[0].on_success
- Add constraints for adequate balance to Trade_Funds_Form.fields.Funding_or_Destination_Account

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the 'Generate Statement' button's type and has a phantom in the E_Statement_Preference_Form submit action.

**Missing:**

- Generate_Statement_Form.submit_actions[0].type

**Phantoms (hallucinations):**

- E_Statement_Preference_Form.submit_actions[0] (missing type for 'Save Preference' button)

**Fixes applied:**

- Add 'type' field with value 'button' to 'Generate_Statement_Form.submit_actions[0]'
- Add 'type' field with value 'button' to 'E_Statement_Preference_Form.submit_actions[0]'

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Schedule_Callback_Form.fields.Reason_for_Call.options
- Schedule_Callback_Form.fields.Preferred_Time_Window.type

**Phantoms (hallucinations):**

- Schedule_Callback_Form.fields.Preferred_Time_Window (type not specified in description)

**Fixes applied:**

- Add options for Reason_for_Call in Schedule_Callback_Form.fields.Reason_for_Call
- Specify type for Preferred_Time_Window in Schedule_Callback_Form.fields.Preferred_Time_Window

---
