# Test Cases — 

Generated:   
Model:   

## SwagLab

Total: **10** (positive: 4, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful login with valid credentials | User is on the login page | 1. Enter valid username (e.g., standard_user)<br>2. Enter valid password (secret_sauce)<br>3. Click on the Login button | User is redirected to the Product Inventory page | high |
| TC005 |  | Add item to cart from Product Inventory | User is logged in and on the Product Inventory page | 1. Click on 'Add to cart' button for a product | Item is added to the cart and the button changes to 'Remove'; cart badge count updates accordingly | high |
| TC008 |  | Complete checkout successfully | User is on the Checkout - Overview page | 1. Click on 'Finish' button | User is redirected to the Checkout - Confirmation page with a success message | high |
| TC010 |  | Reset App State | User is logged in and on the Product Inventory page | 1. Click on 'Reset App State' from the hamburger menu | App state is reset, cart is cleared, and add/remove button states are reset | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Login attempt with empty username | User is on the login page | 1. Leave the username field empty<br>2. Enter valid password (secret_sauce)<br>3. Click on the Login button | Error banner displays: 'Epic sadface: Username is required.' | high |
| TC003 |  | Login attempt with invalid credentials | User is on the login page | 1. Enter invalid username (e.g., invalid_user)<br>2. Enter valid password (secret_sauce)<br>3. Click on the Login button | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC006 |  | Attempt to checkout with missing required fields | User is on the Checkout - Information page | 1. Leave First Name field empty<br>2. Leave Last Name field empty<br>3. Leave Zip/Postal Code field empty<br>4. Click on 'Continue' | Error banners display: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required' | high |
| TC009 |  | Logout and access protected pages | User is logged in and on the Product Inventory page | 1. Click on 'Logout' button<br>2. Attempt to access the Product Inventory page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC004 |  | Login attempt with maximum length username | User is on the login page | 1. Enter a username with maximum allowed length (e.g., 20 characters)<br>2. Enter valid password (secret_sauce)<br>3. Click on the Login button | User is redirected to the Product Inventory page | medium |
| TC007 |  | Checkout with maximum length Zip/Postal Code | User is on the Checkout - Information page | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter a Zip/Postal Code with maximum allowed length<br>4. Click on 'Continue' | User proceeds to the Checkout - Overview page | medium |

---
