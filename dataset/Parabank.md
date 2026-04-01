# Parabank

## Website URL

<https://parabank.parasoft.com/parabank/index.htm>

## Navigation

Parabank is a sample banking application. When visitors arrive, they see the sign-in page, which offers an Email / Username and Password form, a Register link for new customers, and a Forgot Password? link for credential recovery. After a successful log-in, users reach their account dashboard displaying every account and balance. The left-hand navigation menu now contains the following options: ① Accounts Overview (default dashboard view), ② Open New Account, ③ Transfer Funds, ④ Bill Pay, ⑤ Request Loan, ⑥ Update Contact Info, ⑦ Manage Cards, ⑧ Investments, ⑨ Account Statements, ⑩ Security Settings, ⑪ Support Center, and ⑫ Log Out.

## Functional Description

### 1. Login

The login page contains a login form with Username and Password fields, along with a sign-in action and links for registration and password recovery. When the user submits the form, the system validates the provided credentials against registered-user data. If authentication succeeds, the user is redirected to the Accounts Overview area; if it fails, an authentication error is shown and another attempt is allowed.

### 2. Forgot Password

The forgot-password flow is accessible from the login page via the "Forgot Password?" link. The recovery form requires First Name, Last Name, Street Address, City, State, ZIP Code, and SSN. On submit, the system validates completeness and data match against customer records. On success, the system displays account-recovery details and allows the user to continue to sign-in; on failure, it shows a clear "No matching customer information" style error and keeps the form editable.
Support and help-desk capabilities are also available in this journey for users needing assistance. Users can submit a secure support message with Subject, Category (Account, Technical, Security, Other), Message Body, and optional attachment, and they can request a callback by providing reason, preferred date/time window, and phone number. The system validates attachment type, message/body completeness, callback date constraints (next business day), and phone format before creating support tickets.

### 3. Registration

The registration page presents a comprehensive sign-up form with required inputs for First Name, Last Name, Street Address, City, State (dropdown with all US states), ZIP Code, Phone Number, Social Security Number, Username (email format), Password, and Confirm Password, plus a "Register" button. The system enforces specific validation constraints: Username must be a valid email format, Phone Number must follow the format (123) 456-7890 with automatic formatting, ZIP Code must be 5 digits or 5+4 format (12345 or 12345-6789), SSN must follow the format 123-45-6789 with automatic formatting, Password must be at least 8 characters, and Confirm Password must match the Password field. On submission, the system validates field completeness, pattern conformance, and password match. Success produces "Account created successfully — please sign in," then redirects to the login page, otherwise specific field-level errors are displayed for correction.

### 4. Open New Account

This page contains an account-opening form where users select account type (Checking or Savings), choose a funding source account, and submit the request. The system validates required selections and account/funding consistency before creating the new account and returning a success confirmation.

### 5. Account Overview

The dashboard displays a welcome message with the user's name and a table of all customer accounts. Each row shows Account Number (clickable but not implemented yet), Account Type, Current Balance, Account Status (Active badge), and Open Date. The table includes a footer row displaying the total balance across all accounts. Rows are ordered by account creation date (earliest first). Account numbers are masked for security (showing only last 4 digits as ****5001).

### 6. Transfer Funds

The transfer page presents a form to move funds between accounts using amount, source account, and destination account inputs. The system validates transfer amount and account selections, executes valid transfers, and displays confirmation. Invalid requests (for example insufficient funds or invalid amount) return contextual errors.
Extended scenarios that resemble advanced money movement can be covered here as optional cases, but core coverage should prioritize the standard transfer flow.

### 7. Bill Pay

The bill-payment page houses a payment form with fields for Payee Name, Street Address, City, State, ZIP Code, Phone Number, Payee Account Number plus Confirm Account Number, Payment Amount, and Source Account (dropdown), finished by a "Pay" button. On submission, the system validates all entries, enforces account-number match, checks available funds, executes the payment, returns "Payment submitted successfully." with a reference code, and updates balances. Errors (e.g., "Account numbers do not match," "Insufficient funds") are displayed inline and the form remains editable.

### 8. Find Transactions

The transactions search module allows users to locate account activity using multiple filters such as date range, amount, transaction ID/check number, and transaction type. The system validates filter combinations, retrieves matching transactions, and renders sortable results with amount, date, description, and status. Empty result sets show a no-data message without breaking the page flow.
Statement-related reporting scenarios can be treated as optional extensions under this module, while core coverage should focus on transaction search and result validation.

### 9. Update Profile

The customer profile page offers an editable form pre-filled with First Name, Last Name, Street Address, City, State, ZIP Code, and Phone Number, plus an "Update Profile" button. Submission triggers validation of each entry (format and completeness). Success produces "Profile updated successfully." and refreshes the data; failures highlight invalid fields and display an inline error banner.
Card-management and security-preference scenarios can be included as optional profile-maintenance extensions when broader coverage is needed, but core cases should prioritize contact-info updates and validation behavior.

### 10. Request Loan

The loan page allows users to submit a loan request with amount and funding context. The system evaluates eligibility, returns an approval outcome when criteria are met, or returns a denial message when criteria are not met. This module should include both successful and unsuccessful decision paths.

### 11. Logout

Authenticated users can end the session using the Log Out menu action. On logout, the server invalidates the current session and clears authentication state. The user is redirected to the sign-in page and protected pages are no longer accessible via browser back navigation without re-authentication.
