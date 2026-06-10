# Test Cases — 

Generated:   
Model:   

## SwagLab

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Login with valid credentials | User is on the Swag Labs login page | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is redirected to the Product Inventory page with the list of products displayed | high |
| P-002 |  | Add a product to the cart from the Product Inventory page | User logged in as standard_user, User is on the Product Inventory page | 1. Click 'Add to cart' for the first product listed<br>2. Observe the cart badge in the header | The cart badge count increases by 1; the 'Add to cart' button changes to 'Remove' | high |
| P-003 |  | Complete a full checkout with multiple items in the cart | User logged in as standard_user, At least two products have been added to the cart | 1. Click the shopping cart icon to navigate to the Shopping Cart page<br>2. Click Checkout<br>3. Enter 'Jane' in the First Name field<br>4. Enter 'Smith' in the Last Name field<br>5. Enter '12345' in the Zip/Postal Code field<br>6. Click Continue<br>7. Review the order summary on the Overview page<br>8. Click Finish | Confirmation page displays 'Thank you for your order!'; the cart badge is no longer visible | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Attempt to log in with an invalid username | User is on the Swag Labs login page | 1. Enter 'invalid_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username and password do not match any user in this service.'; the user remains on the login page | high |
| N-002 |  | Attempt to checkout with empty required fields | User logged in as standard_user, At least one product has been added to the cart, User is on the Shopping Cart page | 1. Click Checkout<br>2. Leave First Name, Last Name, and Zip/Postal Code fields empty<br>3. Click Continue | An error banner is displayed for each missing field; user remains on the Information form | high |
| N-003 |  | Attempt to log out and access protected pages | User logged in as standard_user, User is on the Product Inventory page | 1. Click the hamburger menu<br>2. Click Logout<br>3. Attempt to navigate back to the Product Inventory page | User is redirected to the login page; protected pages are not accessible without logging in again | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Login with empty username and password fields | User is on the Swag Labs login page | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username is required.'; the user remains on the login page | medium |
| E-002 |  | Enter maximum length for Zip/Postal Code | User logged in as standard_user, At least one product has been added to the cart, User is on the Checkout - Information page | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '123456789' in the Zip/Postal Code field<br>4. Click Continue | User is redirected to the Overview page with the order summary displayed; the system accepts the maximum length input | medium |
| E-003 |  | Reset app state and verify cart is empty | User logged in as standard_user, At least one product has been added to the cart, User is on the Product Inventory page | 1. Click the hamburger menu<br>2. Click Reset App State<br>3. Observe the cart badge in the header | The cart badge count is 0; all 'Add to cart' buttons are reset to their original state | medium |

---
