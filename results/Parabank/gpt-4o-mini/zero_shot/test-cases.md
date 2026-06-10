# Test Cases — 

Generated:   
Model:   

## Parabank

Total: **36** (positive: 12, negative: 12, edge: 12)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful login with valid credentials | User has a registered account with valid credentials. | 1. Navigate to the login page.<br>2. Enter valid Email/Username and Password.<br>3. Click on the 'Sign In' button. | User sees 'Signed in successfully.' and is redirected to the Accounts Overview page. | high |
| TC004 |  | Successful registration with valid details | User is on the registration page. | 1. Fill in all required fields with valid data.<br>2. Click on the 'Register' button. | User sees 'Account created successfully — please sign in,' and is redirected to the login page. | high |
| TC007 |  | Successful fund transfer between accounts | User is logged in and has sufficient funds in source account. | 1. Navigate to the Transfer Funds page.<br>2. Select 'My ParaBank Account' as transfer type.<br>3. Enter a valid Transfer Amount.<br>4. Select Source Account.<br>5. Click on 'Transfer' button. | User sees 'Transfer completed successfully.' with a transaction ID. | high |
| TC010 |  | Successful bill payment | User is logged in and has sufficient funds. | 1. Navigate to the Payments page.<br>2. Fill in all required fields with valid data.<br>3. Click on the 'Pay' button. | User sees 'Payment submitted successfully.' with a reference code. | high |
| TC013 |  | Successful update of contact information | User is logged in and on the Update Contact Info page. | 1. Update any field with valid data.<br>2. Click on the 'Update Profile' button. | User sees 'Profile updated successfully.' and the data refreshes. | high |
| TC016 |  | Successful request for a loan | User is logged in and on the Request Loan page. | 1. Select a loan type.<br>2. Fill in Loan Amount within allowed range.<br>3. Fill in Down Payment Amount.<br>4. Click on 'Request Loan' button. | User sees 'Loan approved and created successfully!' with account details. | high |
| TC019 |  | Successful card request | User is logged in and on the Manage Cards page. | 1. Fill in all required fields in the card request form.<br>2. Click on the 'Request Card' button. | User sees 'Card request submitted successfully.' with a tracking ID. | high |
| TC022 |  | Successful investment trade execution | User is logged in and has sufficient buying power. | 1. Navigate to the Investments page.<br>2. Fill in all required fields in the trade funds form.<br>3. Click on the 'Execute Trade' button. | User sees 'Trade executed successfully.' with an order ID. | high |
| TC025 |  | Successful generation of account statement | User is logged in and on the Account Statements page. | 1. Fill in the Statement Period and select an Account.<br>2. Click on the 'Generate Statement' button. | User sees 'Statement generated successfully.' with the relevant transactions displayed. | high |
| TC028 |  | Successful password change | User is logged in and on the Security Settings page. | 1. Fill in Current Password, New Password, and Confirm New Password.<br>2. Click on the 'Change Password' button. | User sees 'Password changed successfully.' | high |
| TC031 |  | Successful message sent to support center | User is logged in and on the Support Center page. | 1. Fill in all required fields in the secure message form.<br>2. Click on the 'Send Message' button. | User sees 'Message sent successfully.' with a ticket ID. | high |
| TC034 |  | Successful callback request | User is logged in and on the Support Center page. | 1. Fill in all required fields in the schedule callback form.<br>2. Click on the 'Request Callback' button. | User sees 'Callback request submitted.' and receives an email confirmation. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Failed login with incorrect password | User has a registered account. | 1. Navigate to the login page.<br>2. Enter valid Email/Username and an incorrect Password.<br>3. Click on the 'Sign In' button. | User sees 'Incorrect email or password. Please try again,' and the password field is cleared. | high |
| TC005 |  | Registration fails with invalid email format | User is on the registration page. | 1. Fill in all required fields with an invalid email format.<br>2. Click on the 'Register' button. | User sees an error message indicating the email format is invalid. | high |
| TC008 |  | Failed fund transfer due to insufficient funds | User is logged in and has insufficient funds in source account. | 1. Navigate to the Transfer Funds page.<br>2. Select 'My ParaBank Account' as transfer type.<br>3. Enter a Transfer Amount greater than available balance.<br>4. Select Source Account.<br>5. Click on 'Transfer' button. | User sees 'Insufficient funds' error message. | high |
| TC011 |  | Failed bill payment due to account number mismatch | User is logged in. | 1. Navigate to the Payments page.<br>2. Fill in Payee Account Number and Confirm Account Number with different values.<br>3. Click on the 'Pay' button. | User sees 'Account numbers do not match' error message. | high |
| TC014 |  | Failed update of contact information with invalid ZIP code | User is logged in and on the Update Contact Info page. | 1. Enter an invalid ZIP code.<br>2. Click on the 'Update Profile' button. | User sees an error message indicating the ZIP code is invalid. | high |
| TC017 |  | Loan request fails due to insufficient collateral value | User is logged in and on the Request Loan page. | 1. Select a loan type.<br>2. Fill in Loan Amount and Down Payment Amount that do not meet requirements.<br>3. Click on 'Request Loan' button. | User sees 'Inadequate collateral value.' error message. | high |
| TC020 |  | Card request fails due to incomplete address | User is logged in and on the Manage Cards page. | 1. Fill in all required fields but leave Shipping Address incomplete.<br>2. Click on the 'Request Card' button. | User sees an error message indicating the address is incomplete. | high |
| TC023 |  | Trade execution fails due to insufficient buying power | User is logged in and has insufficient buying power. | 1. Navigate to the Investments page.<br>2. Fill in all required fields in the trade funds form.<br>3. Click on the 'Execute Trade' button. | User sees an error message indicating insufficient buying power. | high |
| TC026 |  | Failed statement generation due to invalid date range | User is logged in and on the Account Statements page. | 1. Fill in an invalid date range for Statement Period.<br>2. Click on the 'Generate Statement' button. | User sees 'Unable to generate statement — please try again later.' | high |
| TC029 |  | Password change fails due to mismatched new passwords | User is logged in and on the Security Settings page. | 1. Fill in Current Password, New Password, and a different Confirm New Password.<br>2. Click on the 'Change Password' button. | User sees an error message indicating the passwords do not match. | high |
| TC032 |  | Failed message sending due to missing message body | User is logged in and on the Support Center page. | 1. Fill in Subject and Category but leave Message Body empty.<br>2. Click on the 'Send Message' button. | User sees an error message indicating the message body is required. | high |
| TC035 |  | Callback request fails due to invalid phone number format | User is logged in and on the Support Center page. | 1. Fill in all required fields but enter an invalid Phone Number.<br>2. Click on the 'Request Callback' button. | User sees an error message indicating the phone number format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC003 |  | Login with maximum length email and password | User has a registered account with maximum length email and password. | 1. Navigate to the login page.<br>2. Enter maximum length Email/Username and Password.<br>3. Click on the 'Sign In' button. | User sees 'Signed in successfully.' and is redirected to the Accounts Overview page. | medium |
| TC006 |  | Registration with maximum length fields | User is on the registration page. | 1. Fill in all required fields with maximum length data.<br>2. Click on the 'Register' button. | User sees 'Account created successfully — please sign in,' and is redirected to the login page. | medium |
| TC009 |  | Transfer with maximum amount allowed | User is logged in and has sufficient funds. | 1. Navigate to the Transfer Funds page.<br>2. Select 'My ParaBank Account' as transfer type.<br>3. Enter the maximum allowed Transfer Amount.<br>4. Select Source Account.<br>5. Click on 'Transfer' button. | User sees 'Transfer completed successfully.' with a transaction ID. | medium |
| TC012 |  | Bill payment with maximum amount allowed | User is logged in and has sufficient funds. | 1. Navigate to the Payments page.<br>2. Fill in all required fields with maximum allowed Payment Amount.<br>3. Click on the 'Pay' button. | User sees 'Payment submitted successfully.' with a reference code. | medium |
| TC015 |  | Update contact info with maximum length fields | User is logged in and on the Update Contact Info page. | 1. Fill in all fields with maximum length data.<br>2. Click on the 'Update Profile' button. | User sees 'Profile updated successfully.' and the data refreshes. | medium |
| TC018 |  | Loan request with maximum allowed amount | User is logged in and on the Request Loan page. | 1. Select a loan type.<br>2. Fill in Loan Amount at the maximum limit.<br>3. Fill in Down Payment Amount.<br>4. Click on 'Request Loan' button. | User sees 'Loan approved and created successfully!' with account details. | medium |
| TC021 |  | Card request with maximum length fields | User is logged in and on the Manage Cards page. | 1. Fill in all required fields with maximum length data.<br>2. Click on the 'Request Card' button. | User sees 'Card request submitted successfully.' with a tracking ID. | medium |
| TC024 |  | Trade execution with maximum quantity allowed | User is logged in and has sufficient buying power. | 1. Navigate to the Investments page.<br>2. Fill in all required fields with maximum quantity.<br>3. Click on the 'Execute Trade' button. | User sees 'Trade executed successfully.' with an order ID. | medium |
| TC027 |  | Statement generation with maximum date range | User is logged in and on the Account Statements page. | 1. Fill in the maximum allowed date range for Statement Period.<br>2. Click on the 'Generate Statement' button. | User sees 'Statement generated successfully.' with the relevant transactions displayed. | medium |
| TC030 |  | Password change with maximum length new password | User is logged in and on the Security Settings page. | 1. Fill in Current Password, maximum length New Password, and Confirm New Password.<br>2. Click on the 'Change Password' button. | User sees 'Password changed successfully.' | medium |
| TC033 |  | Message sent with maximum length subject | User is logged in and on the Support Center page. | 1. Fill in Subject with maximum length text.<br>2. Fill in all other required fields.<br>3. Click on the 'Send Message' button. | User sees 'Message sent successfully.' with a ticket ID. | medium |
| TC036 |  | Callback request with maximum length fields | User is logged in and on the Support Center page. | 1. Fill in all fields with maximum length data.<br>2. Click on the 'Request Callback' button. | User sees 'Callback request submitted.' and receives an email confirmation. | medium |

---
