# Semantic Critique — Parabank

Generated: 2026-06-09T10:39:19.180094Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described in the functional description.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains phantoms and missing elements related to the dropdown options for the State field.

**Missing:**

- Sign_Up_Form.fields.State.options

**Phantoms:** none

**Fixes applied:**

- Add options for the State dropdown in Sign_Up_Form.fields.State.options

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Customer_Accounts_Table.footer_row
- Customer_Accounts_Table.columns.Account_Number (masking detail not implemented)

**Phantoms (hallucinations):**

- Customer_Accounts_Table.row_actions[0] (View Account Number action not in description)

**Fixes applied:**

- Add a footer row to Customer_Accounts_Table for total balance.
- Remove the View Account Number action from row_actions.

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

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

- Card_Request_Form.fields.Shipping_Address.constraints[0] (address must be complete is not explicitly stated in the description)
- Card_Request_Form.submit_actions[0].constraints[0] (no constraints were mentioned for the Request Card button)
- Card_Controls_Form.fields.Travel_Notice.constraints[0] (date range must be valid is not explicitly stated in the description)
- Card_Controls_Form.submit_actions[0].constraints[0] (no constraints were mentioned for the Update Controls button)

**Phantoms (hallucinations):**

- Card_Request_Form.fields.Account_to_Link (not mentioned in the description)
- Card_Controls_Form.fields.New_Spending_Limit.constraints[0] (numeric limit must be valid is not explicitly stated in the description)
- Card_Controls_Form.fields.Card_Status.constraints[0] (allowable transitions must be valid is not explicitly stated in the description)

**Fixes applied:**

- Remove Card_Request_Form.fields.Account_to_Link
- Remove Card_Request_Form.fields.Shipping_Address.constraints[0]
- Remove Card_Controls_Form.fields.New_Spending_Limit.constraints[0]
- Remove Card_Controls_Form.fields.Card_Status.constraints[0]
- Remove Card_Request_Form.submit_actions[0].constraints[0]
- Remove Card_Controls_Form.submit_actions[0].constraints[0]

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Trade_Funds_Form.fields.Funding_or_Destination_Account.constraints[0] (should specify adequate balance)
- Recurring_Investment_Plan_Form.fields.Funding_Account.constraints[0] (should specify adequate balance)

**Phantoms (hallucinations):**

- Trade_Funds_Form.fields.Funding_or_Destination_Account (no specific mention in description)
- Recurring_Investment_Plan_Form.fields.Fund_Symbol (no specific mention in description)

**Fixes applied:**

- Add 'Funding_or_Destination_Account' constraints to specify adequate balance.
- Remove 'Funding_Account' field from Recurring_Investment_Plan_Form as it is not specified.

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items: 1 minor and 1 critical, and there are phantoms present.

**Missing:**

- Generate_Statement_Form.fields.Statement_Period.type (should specify month-and-year or custom date range)
- E_Statement_Preference_Form.fields.Opt_into_Paperless_Statements.required (should be true)

**Phantoms (hallucinations):**

- Generate_Statement_Form.fields.Statement_Period.constraints[0] (valid date range required is inferred, not stated in description)
- E_Statement_Preference_Form.fields.Opt_into_Paperless_Statements.required (should be true)

**Fixes applied:**

- Update Generate_Statement_Form.fields.Statement_Period.type to specify month-and-year or custom date range.
- Set E_Statement_Preference_Form.fields.Opt_into_Paperless_Statements.required to true.

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

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
