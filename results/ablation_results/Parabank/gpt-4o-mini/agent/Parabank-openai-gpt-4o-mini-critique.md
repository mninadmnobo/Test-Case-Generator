# Semantic Critique — Parabank

Generated: 2026-06-09T10:34:27.386695Z

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

The AST is missing the required constraint for the Confirm Password field to match the Password field.

**Missing:**

- Sign_Up_Form.fields.Confirm_Password.constraints[0] (must match Password)

**Phantoms:** none

**Fixes applied:**

- Add a constraint to Confirm_Password: 'must match Password'

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms identified in the AST.

**Missing:**

- Customer_Accounts_Table.footer_row
- Customer_Accounts_Table.columns.Account_Number (masking detail not implemented)

**Phantoms (hallucinations):**

- Customer_Accounts_Table.row_actions[0] (View Account Number action not in description)

**Fixes applied:**

- Add footer row to Customer_Accounts_Table for total balance.
- Remove View Account Number action from row_actions as it is not mentioned.

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

The AST is missing critical elements related to the conditional logic and error handling.

**Missing:**

- Transfer_Form.fields.Destination_Options.item_fields.Account_Number.constraints[0] (missing 'sufficient funds required' for external transfers)
- Transfer_Form.submit_actions[0].on_failure (missing contextual error messages)

**Phantoms:** none

**Fixes applied:**

- Add a conditional for Destination_Options based on Transfer_Type selection.
- Add error handling for submit_actions to include contextual errors.

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and logic described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Card_Request_Form.fields.Shipping_Address.constraints[0]
- Card_Controls_Form.fields.Travel_Notice.item_fields.Dates.constraints[0]
- Card_Controls_Form.submit_actions[0].constraints[0]

**Phantoms (hallucinations):**

- Card_Request_Form.fields.Account_to_Link (no type specified in description)
- Card_Controls_Form.fields.Travel_Notice.item_fields.Dates (no constraints specified in description)

**Fixes applied:**

- Add 'address must be complete' constraint to 'Card_Request_Form.fields.Shipping_Address'
- Add 'valid date ranges' constraint to 'Card_Controls_Form.fields.Travel_Notice.item_fields.Dates'
- Remove 'valid numeric limits' phantom from 'Card_Controls_Form.submit_actions[0].constraints[0]'

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Trade_Funds_Form.fields.Funding_or_Destination_Account.constraints[0] (must have adequate balance constraint is missing)
- Recurring_Investment_Plan_Form.fields.Funding_Account.constraints[0] (must have adequate balance constraint is missing)

**Phantoms (hallucinations):**

- Trade_Funds_Form.fields.Fund_Symbol.constraints[0] (symbol must exist constraint is inferred but not explicitly stated in the description)
- Recurring_Investment_Plan_Form.fields.Fund_Symbol (no constraints mentioned in the description)

**Fixes applied:**

- Add 'must have adequate balance' constraint to 'Trade_Funds_Form.fields.Funding_or_Destination_Account'
- Add 'must have adequate balance' constraint to 'Recurring_Investment_Plan_Form.fields.Funding_Account'
- Remove 'symbol must exist' constraint from 'Trade_Funds_Form.fields.Fund_Symbol'
- Add constraints to 'Recurring_Investment_Plan_Form.fields.Fund_Symbol' as per description

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

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

There are missing elements and phantoms in the AST.

**Missing:**

- Secure_Message_Form.fields.Message_Body.type (should specify rich text)
- Schedule_Callback_Form.fields.Preferred_Time_Window.type (should specify time)

**Phantoms (hallucinations):**

- Secure_Message_Form.fields.Subject.type (unspecified is too vague)
- Schedule_Callback_Form.fields.Reason_for_Call.type (unspecified is too vague)
- Schedule_Callback_Form.fields.Phone_Number.type (unspecified is too vague)

**Fixes applied:**

- Update Secure_Message_Form.fields.Message_Body.type to 'rich_text'
- Update Schedule_Callback_Form.fields.Preferred_Time_Window.type to 'time'
- Specify Secure_Message_Form.fields.Subject.type to a more specific type
- Specify Schedule_Callback_Form.fields.Reason_for_Call.type to a more specific type
- Specify Schedule_Callback_Form.fields.Phone_Number.type to a more specific type

---
