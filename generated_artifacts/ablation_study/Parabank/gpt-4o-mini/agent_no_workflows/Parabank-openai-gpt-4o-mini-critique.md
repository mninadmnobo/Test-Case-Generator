# Semantic Critique — Parabank

Generated: 2026-06-09T10:37:46.970541Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described in the functional description.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Accounts_Table.footer_row
- Accounts_Table.columns.Account_Number.masking

**Phantoms (hallucinations):**

- Accounts_Table.row_actions[0] (View Account Details action not in description)
- Accounts_Table.columns.Account_Type.type (unspecified not defined in description)
- Accounts_Table.columns.Current_Balance.type (unspecified not defined in description)
- Accounts_Table.columns.Account_Status.type (unspecified not defined in description)
- Accounts_Table.columns.Open_Date.type (unspecified not defined in description)

**Fixes applied:**

- Add footer_row to Accounts_Table
- Add masking to Accounts_Table.columns.Account_Number
- Remove row_actions from Accounts_Table

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and validation requirements described.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Transfer_Form.fields.Destination_Options.fields.Internal_Accounts.visible_when
- Transfer_Form.submit_actions[0].on_failure

**Phantoms (hallucinations):**

- Transfer_Form.fields.Destination_Options.type (unspecified type not in description)

**Fixes applied:**

- Add 'visible_when' condition for Internal_Accounts based on Transfer_Type.
- Add 'on_failure' action to submit_actions for failure messages.

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

The AST is missing critical elements related to validation and denial reasons.

**Missing:**

- Loan_Application_Form.fields.Loan_Amount.constraints[2]
- Loan_Application_Form.submit_actions[0].on_failure

**Phantoms:** none

**Fixes applied:**

- Add a constraint for Loan_Amount to validate against down payment and collateral value.
- Add an on_failure message for the submit action to specify denial reasons.

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Card_Request_Form.fields.Shipping_Address.constraints[0] (address must be complete is not explicitly stated in the description)
- Card_Request_Form.fields.Account_to_Link (this field is missing from the AST)
- Card_Controls_Form.fields.New_Spending_Limit.constraints[0] (must be a valid numeric limit is not explicitly stated in the description)
- Card_Controls_Form.fields.Card_Status (this field is missing from the AST)

**Phantoms (hallucinations):**

- Card_Request_Form.submit_actions[0].element_name (Request Card button not in description)
- Card_Controls_Form.submit_actions[0].element_name (Update Controls button not in description)

**Fixes applied:**

- Add 'Account_to_Link' field to 'Card_Request_Form.fields'
- Remove 'Request Card' from 'Card_Request_Form.submit_actions'
- Remove 'Update Controls' from 'Card_Controls_Form.submit_actions'
- Add 'Card_Status' field to 'Card_Controls_Form.fields'
- Add 'Shipping_Address' constraints to 'Card_Request_Form.fields.Shipping_Address'

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Trade_Funds_Form.fields.Funding_or_Destination_Account
- Recurring_Investment_Plan_Form.fields.Funding_Account

**Phantoms (hallucinations):**

- Recurring_Investment_Plan_Form.fields.Funding_Account (not mentioned in description)

**Fixes applied:**

- Add 'Funding_or_Destination_Account' field to 'Trade_Funds_Form.fields'
- Add 'Funding_Account' field to 'Recurring_Investment_Plan_Form.fields'

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the 'Generate Statement' button and has a phantom in the failure message for the e-statement preference form.

**Missing:**

- Generate_Statement_Form.submit_actions[0].element_name (Generate Statement button not in description)

**Phantoms (hallucinations):**

- E_Statement_Preference_Form.submit_actions[0].on_failure (highlights the email field with guidance not in description)

**Fixes applied:**

- Add 'Generate Statement' button to Generate_Statement_Form.submit_actions.
- Change E_Statement_Preference_Form.submit_actions[0].on_failure to a valid failure message.

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
