# Test Cases — Swaglab

Generated: 2026-06-10T18:37:40.505302Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 67 | 18 | 26 | 23 | 36 | 18 | 13 |

## Login

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User> | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | User authenticated and redirected to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Attempt to login with empty Username field |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Login | Error banner shows 'Epic sadface: Username is required.' | high |
| TC-003 | WF-003 | Attempt to login with empty Password field |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Login | Error banner shows 'Epic sadface: Password is required.' | high |
| TC-004 | WF-004 | Attempt to login with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | Error banner shows 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-005 | WF-005 | Attempt to login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | Error banner shows 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error shown indicating the username is too long or the form submits successfully with the username truncated. | low |
| TC-007 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter '@#$%^&*()' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error shown indicating invalid characters in the Username field. | low |
| TC-008 (input_edge) |  | Enter leading and trailing whitespace in the Username field |  | 1. Enter '   standard_user   ' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Leading/trailing whitespace is trimmed; user is authenticated and redirected to the Product Inventory page. | low |
| TC-009 (input_edge) |  | Enter zero as Username |  | 1. Enter '0' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error shown: 'Epic sadface: Username and password do not match any user in this service.' | low |

---

## Product Inventory

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Role> | 1. Click 'Add to cart' button for a product | Item added to cart; button changes to 'Remove' | high |
| TC-002 | WF-002 | Remove product from cart | User logged in as <Role>, Item is in the cart | 1. Click 'Remove' button for the product | Item removed from cart; button changes to 'Add to cart' | high |
| TC-003 | WF-003 | View product detail | User logged in as <Role> | 1. Click on a product name or image | Product detail page opens | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to add a product to cart without being logged in | User is not logged in | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' on any product | User is redirected to the login page | high |
| TC-005 | WF-002 | Attempt to remove a product from cart without being logged in | User is not logged in | 1. Navigate to the Product Inventory page<br>2. Click 'Remove' on any product | User is redirected to the login page | high |
| TC-006 | WF-003 | Attempt to view product detail without being logged in | User is not logged in | 1. Navigate to the Product Inventory page<br>2. Click on a product name or image | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long product name | User is logged in, Product Inventory page is open | 1. Locate the product name input field<br>2. Enter a string of 200+ characters in the product name field | Product name input is accepted or truncated with a visible indicator | low |
| TC-008 (input_edge) |  | Enter special characters in the product description | User is logged in, Product Inventory page is open | 1. Locate the product description input field<br>2. Enter special characters and emojis in the product description field | Product description input is accepted or a specific error is shown | low |
| TC-009 (input_edge) |  | Enter leading and trailing whitespace in the product name | User is logged in, Product Inventory page is open | 1. Locate the product name input field<br>2. Enter '   Product Name   ' in the product name field | Leading/trailing whitespace is trimmed; saved product name shows 'Product Name' | low |

---

## Product Detail

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <role> | 1. Click 'Add to cart' button | Product added to cart; success message shown | high |
| TC-002 | WF-002 | Remove product from cart | User logged in as <role>, Product is in cart | 1. Click 'Remove' button | Product removed from cart; success message shown | high |
| TC-003 | WF-003 | Navigate back to products | User logged in as <role> | 1. Click 'Back to products' button | Returned to Product Inventory page | medium |
| TC-004 | WF-004 | Navigate to shopping cart | User logged in as <role> | 1. Click on the cart icon | Navigated to Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to add product to cart without being logged in | User is not authenticated | 1. Click 'Add to cart' button | User is redirected to the login page; no product is added to cart | high |
| TC-006 | WF-002 | Attempt to remove product from cart without being logged in | User is not authenticated | 1. Click 'Remove' button | User is redirected to the login page; no product is removed from cart | high |
| TC-007 | WF-003 | Attempt to navigate back to products without being logged in | User is not authenticated | 1. Click 'Back to products' button | User is redirected to the login page; no navigation occurs | high |
| TC-008 | WF-004 | Attempt to navigate to shopping cart without being logged in | User is not authenticated | 1. Click on cart icon | User is redirected to the login page; no navigation occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (interaction_edge) | WF-001 | Rapid re-submission after adding to cart | Product is displayed on the Product Detail page | 1. Click 'Add to cart' button<br>2. Immediately click 'Add to cart' button again | Second submission attempt is blocked; only one product appears in the cart | medium |
| TC-010 (interaction_edge) | WF-002 | Rapid re-submission after removing from cart | Product is in the cart | 1. Click 'Remove' button<br>2. Immediately click 'Remove' button again | Second submission attempt is blocked; product remains removed from the cart | medium |
| TC-011 (interaction_edge) | WF-003 | Navigate back to products after adding to cart | Product is displayed on the Product Detail page, Product has been added to the cart | 1. Click 'Back to products' button | Returned to Product Inventory page without any cart state change | medium |
| TC-012 (interaction_edge) | WF-004 | Navigate to Shopping Cart after adding to cart | Product is displayed on the Product Detail page, Product has been added to the cart | 1. Click on the cart icon | Navigated to Shopping Cart page displaying the added product | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User clicks Continue Shopping | User logged in as <Role>, Shopping Cart contains items | 1. Click Continue Shopping | Returned to Product Inventory | high |
| TC-002 | WF-002 | User clicks Checkout | User logged in as <Role>, Shopping Cart contains items | 1. Click Checkout | Started checkout process | high |
| TC-003 | WF-003 | User removes an item from the cart | User logged in as <Role>, Shopping Cart contains items | 1. Click Remove button for an item | Item removed from cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Unauthenticated user attempts to access the Shopping Cart |  | 1. Attempt to access the Shopping Cart page | User is redirected to the login page | high |
| TC-005 | WF-002 | Unauthenticated user attempts to checkout |  | 1. Attempt to click Checkout button | User is redirected to the login page | high |
| TC-006 | WF-003 | Unauthenticated user attempts to remove an item from the cart |  | 1. Attempt to click Remove button for an item | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Add a very long description to an item |  | 1. Add an item with a description of more than 200 characters to the cart | Item is added to the cart with the long description displayed correctly | low |
| TC-008 (input_edge) |  | Add an item with special characters in the description |  | 1. Add an item with a description containing special characters (e.g., @#$%^&*()) to the cart | Item is added to the cart with the description displayed correctly | low |
| TC-009 (interaction_edge) |  | Rapidly click Continue Shopping after adding an item | Item is added to the cart | 1. Click Continue Shopping<br>2. Immediately click Continue Shopping again | User is redirected to Product Inventory without any errors or duplicate actions | medium |

---

## Checkout - Information

Total: **10** (positive: 2, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit form with all required fields filled | User logged in as <role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click Continue | Proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel checkout process | User logged in as <role> | 1. Click Cancel | Returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Submit form with all required fields empty |  | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Postal Code field blank<br>4. Click Continue | Error banner displays 'Error: First Name is required', 'Error: Last Name is required', and 'Error: Postal Code is required' | high |
| TC-004 |  | Submit form with missing First Name |  | 1. Leave the First Name field blank<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click Continue | Error banner displays 'Error: First Name is required' | high |
| TC-005 |  | Submit form with missing Last Name |  | 1. Enter <valid first name> in the First Name field<br>2. Leave the Last Name field blank<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click Continue | Error banner displays 'Error: Last Name is required' | high |
| TC-006 |  | Submit form with missing Postal Code |  | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Leave the Postal Code field blank<br>4. Click Continue | Error banner displays 'Error: Postal Code is required' | high |
| TC-007 |  | Cancel checkout process |  | 1. Click Cancel | Returns to the Shopping Cart | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long string in First Name field |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill Last Name with a valid name<br>3. Fill Postal Code with a valid code<br>4. Click Continue | Form submits successfully; entity is created with the long First Name | low |
| TC-009 (input_edge) |  | Enter special characters in Last Name field |  | 1. Enter valid First Name<br>2. Enter special characters in the Last Name field<br>3. Fill Postal Code with a valid code<br>4. Click Continue | Form submits successfully; entity is created with the special characters in Last Name | low |
| TC-010 (input_edge) |  | Enter value with leading/trailing whitespace in Postal Code field |  | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter ' 12345 ' in the Postal Code field<br>4. Click Continue | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Checkout - Overview

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish the order | User logged in as <role>, Order summary is displayed with cart items and totals | 1. Click 'Finish' | Order completed; navigates to confirmation page | high |
| TC-002 | WF-002 | Cancel the checkout process | User logged in as <role>, Order summary is displayed with cart items and totals | 1. Click 'Cancel' | Exited checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to finish order without completing payment information |  | 1. Navigate to the checkout overview<br>2. Click Finish | Order is not completed; user remains on the overview page with an error indicating payment information is required | high |
| TC-004 | WF-002 | Attempt to cancel checkout without any prior actions |  | 1. Navigate to the checkout overview<br>2. Click Cancel | User is exited from checkout; no changes to the order are made | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapidly click Finish after viewing the order summary | User is on the overview step with an order summary displayed | 1. Click Finish<br>2. Immediately click Finish again | Order is completed; navigates to confirmation page without error | medium |
| TC-006 (interaction_edge) | WF-002 | Rapidly click Cancel after viewing the order summary | User is on the overview step with an order summary displayed | 1. Click Cancel<br>2. Immediately click Cancel again | Exited checkout; no additional confirmation prompts shown | medium |

---

## Checkout - Confirmation

Total: **3** (positive: 1, negative: 2, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm order and return home | User logged in as <role> | 1. Click the 'Back Home' button | The page displays 'Thank you for your order!' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access confirmation page |  | 1. Navigate to the confirmation page without logging in | User is redirected to the login page | high |
| TC-003 | WF-001 | Attempt to confirm order without items in cart |  | 1. Navigate to the confirmation page with an empty cart | Confirmation page does not display a success message; user remains on the page | high |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs out | User logged in as <User Role> | 1. Click the Logout button | User is redirected to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Unauthenticated user attempts to access a protected page |  | 1. Logout from the application<br>2. Attempt to access the inventory page | User is redirected to the login page; access to the inventory page is blocked. | high |
| TC-003 |  | Unauthenticated user attempts to access another protected page |  | 1. Logout from the application<br>2. Attempt to access the checkout page | User is redirected to the login page; access to the checkout page is blocked. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Attempt to access protected pages after logout | User is logged in | 1. Click on Logout<br>2. Attempt to access the inventory page | User is redirected to the login page; access to the inventory page is blocked. | medium |
| TC-005 (input_edge) |  | Attempt to access protected pages immediately after logout | User is logged in | 1. Click on Logout<br>2. Press the back button in the browser | User is redirected to the login page; the inventory page is not displayed. | medium |

---

## Reset App State

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State action | User logged in as <role> | 1. Click on the 'Reset App State' button | Cart cleared and in-app state reset | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to reset app state |  | 1. Attempt to perform the Reset App State action without logging in | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid consecutive reset actions | User is logged in and has items in the cart | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again | First reset action clears the cart and resets in-app state; second action is blocked with no additional effect. | medium |
| TC-004 (input_edge) |  | Attempt to reset state with an empty cart | User is logged in and cart is empty | 1. Click the Reset App State button | Cart remains empty; in-app state reset successfully without errors. | low |

---
