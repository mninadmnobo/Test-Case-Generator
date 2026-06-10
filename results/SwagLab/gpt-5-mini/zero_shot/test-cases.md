# Test Cases — 

Generated:   
Model:   

## SwagLab

Total: **22** (positive: 9, negative: 8, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Login succeeds with valid credentials | User is on the Login page | 1. Enter username standard_user<br>2. Enter password secret_sauce<br>3. Click Login | User is authenticated and redirected to the Product Inventory page; header with hamburger, title, and cart icon is visible | high |
| TC-006 |  | Add single item to cart updates button text and cart badge | User is logged in as standard_user and on Product Inventory page | 1. Locate product 'Sauce Labs Backpack'<br>2. Click Add to cart for that product | Add to cart button changes to Remove for that item and cart icon badge increments to 1 | high |
| TC-007 |  | Remove item from inventory updates button and badge | User is logged in as standard_user and has at least one item in cart | 1. On Product Inventory or Product Detail page, click Remove for an item currently in cart | Button text changes from Remove back to Add to cart and cart badge decrements accordingly | medium |
| TC-008 |  | Open Product Detail from inventory and toggle cart state | User is logged in as standard_user and on Product Inventory page | 1. Click the product name or image for any listed product<br>2. On Product Detail page, verify product image, name, description, and price are shown<br>3. Click Add to cart (or Remove) on the detail page | Product Detail shows correct product information; Add to cart button toggles to Remove and cart badge updates; Back to products returns to Inventory | medium |
| TC-009 |  | Shopping Cart lists added items and allows removal | User is logged in as standard_user and one or more items have been added to cart | 1. Click the cart icon to open Shopping Cart<br>2. Verify each item shows name, description, quantity 1, price, and Remove button<br>3. Click Remove for an item | Removed item disappears from cart, cart badge decrements, and cart totals update accordingly | high |
| TC-010 |  | Complete checkout flow successfully | User is logged in as standard_user and has at least one item in cart | 1. Open Shopping Cart and click Checkout<br>2. On Checkout Information, enter First Name, Last Name, and Postal Code and click Continue<br>3. On Checkout Overview, verify items and totals then click Finish | User lands on Confirmation page with success message Thank you for your order!; clicking Back Home returns to Product Inventory and cart is cleared | high |
| TC-014 |  | Checkout Overview displays order summary and totals | User is logged in as standard_user, has items in cart, and has completed Checkout Information with valid values | 1. On Checkout Overview, review listed items and verify item prices<br>2. Verify totals section shows Item total, Tax, and Total<br>3. Click Cancel to exit checkout | Overview shows correct items and calculated totals; clicking Cancel returns user to Shopping Cart | medium |
| TC-015 |  | Confirmation Back Home clears cart and returns to inventory | User has completed checkout and is on Confirmation page | 1. Verify success message is displayed on Confirmation page<br>2. Click Back Home | User is redirected to Product Inventory and cart is empty with badge cleared and Add to cart buttons reset | high |
| TC-016 |  | Sort dropdown sorts products by name and price | User is logged in as standard_user and on Product Inventory page | 1. Open sort dropdown and select Name (A to Z)<br>2. Observe product order<br>3. Select Name (Z to A), then Price (low to high), then Price (high to low) | Product list reorders correctly for each sort option | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login fails with empty username | User is on the Login page | 1. Leave Username empty<br>2. Enter password secret_sauce<br>3. Click Login | Error banner displays: Epic sadface: Username is required. | medium |
| TC-003 |  | Login fails with empty password | User is on the Login page | 1. Enter username standard_user<br>2. Leave Password empty<br>3. Click Login | Error banner displays: Epic sadface: Password is required. | medium |
| TC-004 |  | Login fails with invalid credentials | User is on the Login page | 1. Enter username invalid_user<br>2. Enter password wrong_password<br>3. Click Login | Error banner displays: Epic sadface: Username and password do not match any user in this service. | medium |
| TC-005 |  | Locked out user cannot login | User is on the Login page | 1. Enter username locked_out_user<br>2. Enter password secret_sauce<br>3. Click Login | Error banner displays: Epic sadface: Sorry, this user has been locked out. | high |
| TC-011 |  | Checkout information fails when First Name is missing | User is logged in as standard_user and has at least one item in cart, User is on Checkout - Information page | 1. Leave First Name empty<br>2. Enter valid Last Name and Postal Code<br>3. Click Continue | Error banner displays: Error: First Name is required and user remains on Information step | medium |
| TC-012 |  | Checkout information fails when Last Name is missing | User is logged in as standard_user and has at least one item in cart, User is on Checkout - Information page | 1. Enter valid First Name<br>2. Leave Last Name empty<br>3. Enter valid Postal Code and click Continue | Error banner displays: Error: Last Name is required and user remains on Information step | medium |
| TC-013 |  | Checkout information fails when Postal Code is missing | User is logged in as standard_user and has at least one item in cart, User is on Checkout - Information page | 1. Enter valid First Name and Last Name<br>2. Leave Postal Code empty<br>3. Click Continue | Error banner displays: Error: Postal Code is required and user remains on Information step | medium |
| TC-019 |  | Protected pages are inaccessible after logout | User is logged in as standard_user | 1. Open hamburger menu and click Logout<br>2. Attempt to navigate directly to Inventory, Product Detail, Cart, and Checkout URLs | User is returned to Login page and access to protected pages requires re-authentication | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Add multiple items verifies badge increments and persists across pages | User is logged in as standard_user and on Product Inventory page | 1. Add three different products to the cart from the Inventory page<br>2. Navigate to one Product Detail and verify cart badge still shows 3<br>3. Go to Shopping Cart and verify all three items are listed | Cart badge shows 3 across pages; Shopping Cart lists three items each with quantity 1 | high |
| TC-018 |  | Reset App State clears cart and resets button states without logging out | User is logged in as standard_user and has one or more items in cart | 1. Open hamburger menu and click Reset App State<br>2. Observe cart badge and Add/Remove buttons on Inventory | Cart is cleared, badge removed or set to 0, Add to cart buttons are reset to initial state, and user remains logged in | high |
| TC-020 |  | Checkout accepts long postal code input boundary | User is logged in as standard_user and has at least one item in cart | 1. Start Checkout and enter First Name and Last Name<br>2. Enter a very long Postal Code string of 50 characters<br>3. Click Continue | System either accepts the postal code if within field constraints or shows a validation error; no application crash occurs | low |
| TC-021 |  | Form fields handle extremely long First/Last names | User is logged in as standard_user and on Checkout Information page | 1. Enter First Name and Last Name with 255-character strings<br>2. Enter a valid Postal Code and click Continue | System accepts inputs within allowed length or shows clear validation errors; page remains responsive and no data corruption occurs | low |
| TC-022 |  | Rapid add/remove toggle does not desync cart state | User is logged in as standard_user and on Product Inventory page | 1. Rapidly click Add to cart and Remove for the same product multiple times<br>2. Observe button label and cart badge after toggling | Final state of button and cart badge matches the last action; no duplicate entries or negative counts occur | low |

---
