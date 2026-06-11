# Test Cases — Swaglab

Generated: 2026-06-10T18:38:10.944513Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 73 | 21 | 23 | 29 | 34 | 20 | 16 |

## Login

Total: **13** (positive: 1, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <Guest> | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | authenticates and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Submit with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Page displays 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-006 |  | Attempt to login with locked out user |  | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click Login | Page displays 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Username field is empty |  | 1. Leave the Username field empty<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Username is required.' | medium |
| TC-008 (boundary) |  | Password field is empty |  | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field empty<br>3. Click Login | Error banner displays: 'Epic sadface: Password is required.' | medium |
| TC-009 (boundary) |  | Invalid credentials with valid username |  | 1. Enter 'standard_user' in the Username field<br>2. Enter 'wrong_password' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | medium |
| TC-010 (boundary) |  | Attempt login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Sorry, this user has been locked out.' | medium |
| TC-011 (input_edge) |  | Enter long username |  | 1. Enter a very long string (over 100 characters) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | low |
| TC-012 (input_edge) |  | Enter special characters in username |  | 1. Enter '@#$%^&*()' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | low |
| TC-013 (input_edge) |  | Leading/trailing whitespace in username |  | 1. Enter ' standard_user ' (with spaces) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | low |

---

## Product Inventory

Total: **10** (positive: 5, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View product detail | User logged in as <Customer> | 1. Click on a product name or image in the Product List | Product Detail page is displayed with the selected product information | high |
| TC-002 |  | Add item to cart | User logged in as <Customer> | 1. Click 'Add to cart' button for a product | The button changes to 'Remove' and the cart badge count updates accordingly | high |
| TC-003 |  | Remove item from cart | User logged in as <Customer>, Item is already in cart | 1. Click 'Remove' button for the product in the cart | The item is removed from the cart | high |
| TC-004 |  | Sort products by name A-Z | User logged in as <Customer> | 1. Select 'name (A–Z)' from the Sort_By dropdown | Products are sorted in alphabetical order from A to Z | medium |
| TC-005 |  | Sort products by price low-high | User logged in as <Customer> | 1. Select 'price (low–high)' from the Sort_By dropdown | Products are sorted in ascending order by price | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to add a product to cart without being logged in | User is not authenticated | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' for any product | User is redirected to the login page | high |
| TC-007 |  | Attempt to remove a product from cart without being logged in | User is not authenticated | 1. Navigate to the Product Inventory page<br>2. Click 'Remove' for any product | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) |  | Rapidly add and remove a product from the cart | User is logged in and on the Product Inventory page | 1. Click 'Add to cart' on a product<br>2. Immediately click 'Remove' on the same product | 'Remove' action succeeds; the product is removed from the cart and the cart badge count updates accordingly. | medium |
| TC-009 (input_edge) |  | Sort products using special characters | User is logged in and on the Product Inventory page | 1. Open the 'Sort By' dropdown<br>2. Select 'name (A–Z)' | Products are sorted alphabetically from A to Z; the first product in the list starts with the letter A. | low |
| TC-010 (input_edge) |  | Sort products using a long name | User is logged in and on the Product Inventory page | 1. Open the 'Sort By' dropdown<br>2. Select 'price (high–low)' | Products are sorted by price in descending order; the highest priced product appears at the top of the list. | low |

---

## Product Detail

Total: **9** (positive: 4, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Customer>, Product is not in cart | 1. Click 'Add to cart' button | The button changes to 'Remove' and the product is now in the cart | high |
| TC-002 | WF-002 | Remove product from cart | User logged in as <Customer>, Product is in cart | 1. Click 'Remove' button | The button changes to 'Add to cart' and the product is no longer in the cart | high |
| TC-003 | WF-003 | Navigate back to products | User logged in as <Customer> | 1. Click 'Back to products' button | User is redirected to the Product Inventory page | medium |
| TC-004 | WF-004 | Navigate to shopping cart | User logged in as <Customer> | 1. Click 'Shopping Cart' link | User is redirected to the Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to remove a product that is not in the cart | Product is not in the cart | 1. Navigate to the Product Detail page<br>2. Click on the 'Remove' button | No action occurs; 'Remove' button is not available | high |
| TC-006 |  | Attempt to add a product that is already in the cart | Product is already in the cart | 1. Navigate to the Product Detail page<br>2. Click on the 'Add to cart' button | No action occurs; 'Add to cart' button is not available | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (state_edge) |  | Rapid consecutive state transitions from Not In Cart to In Cart | Product is currently Not In Cart | 1. Click 'Add to cart'<br>2. Immediately click 'Remove' | Both actions are processed successfully; the product is removed from the cart. | medium |
| TC-008 (state_edge) |  | Rapid consecutive state transitions from In Cart to Not In Cart | Product is currently In Cart | 1. Click 'Remove'<br>2. Immediately click 'Add to cart' | Both actions are processed successfully; the product is added back to the cart. | medium |
| TC-009 (interaction_edge) |  | Back navigation after adding to cart | Product is added to cart | 1. Click 'Back to products'<br>2. Click 'Shopping Cart' | User is navigated to the Shopping Cart without duplication of the product. | low |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <Customer>, Shopping cart contains items | 1. Click the 'Remove' button for an item in the cart | The item is no longer visible in the cart | high |
| TC-002 | WF-002 | Continue shopping from the cart | User logged in as <Customer>, Shopping cart contains items | 1. Click 'Continue Shopping' | returns to Product Inventory | medium |
| TC-003 | WF-003 | Begin checkout from the cart | User logged in as <Customer>, Shopping cart contains items | 1. Click 'Checkout' | begins checkout | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to remove an item from an empty cart |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Remove' button for an item | No action occurs; the cart remains empty and no item is removed |  |
| TC-005 |  | Attempt to checkout with an empty cart |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Checkout' button | No action occurs; the checkout process does not begin |  |
| TC-006 |  | Attempt to continue shopping with an empty cart |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Continue Shopping' button | No action occurs; the user remains on the Shopping Cart page |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) |  | Rapidly click 'Continue Shopping' after adding an item | User has added an item to the cart | 1. Click 'Continue Shopping' button<br>2. Immediately click 'Continue Shopping' button again | 'Continue Shopping' redirects to Product Inventory without duplicating the item in the cart. | medium |
| TC-008 (interaction_edge) |  | Rapidly click 'Checkout' after adding an item | User has added an item to the cart | 1. Click 'Checkout' button<br>2. Immediately click 'Checkout' button again | Checkout process begins without any errors or duplicate entries. | medium |
| TC-009 (input_edge) |  | Attempt to remove an item from an empty cart | User's cart is empty | 1. Attempt to click 'Remove' button for a non-existent item | No action occurs; a message indicates the cart is empty. | low |

---

## Checkout - Information

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit the checkout information form with valid data | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-001 | Cancel the checkout information form | User logged in as <Customer> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill Last_Name and Zip_Postal_Code with valid data<br>3. Click Continue | Error: First Name is required is displayed | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill First_Name and Zip_Postal_Code with valid data<br>3. Click Continue | Error: Last Name is required is displayed | high |
| TC-005 |  | Leave the Zip/Postal Code field blank and submit |  | 1. Leave the Zip_Postal_Code field blank<br>2. Fill First_Name and Last_Name with valid data<br>3. Click Continue | Error: Postal Code is required is displayed | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First_Name, Last_Name, and Zip_Postal_Code fields blank<br>2. Click Continue | Error: First Name is required, Error: Last Name is required, and Error: Postal Code is required are displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Submit form with First Name empty |  | 1. Leave the First Name field empty<br>2. Fill in the Last Name field with 'Doe'<br>3. Fill in the Zip/Postal Code field with '12345'<br>4. Click Continue | Error banner displays: 'Error: First Name is required' | medium |
| TC-008 (boundary) |  | Submit form with Last Name empty |  | 1. Fill in the First Name field with 'John'<br>2. Leave the Last Name field empty<br>3. Fill in the Zip/Postal Code field with '12345'<br>4. Click Continue | Error banner displays: 'Error: Last Name is required' | medium |
| TC-009 (boundary) |  | Submit form with Zip/Postal Code empty |  | 1. Fill in the First Name field with 'John'<br>2. Fill in the Last Name field with 'Doe'<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner displays: 'Error: Postal Code is required' | medium |
| TC-010 (input_edge) |  | Submit form with long First Name |  | 1. Enter a very long string (200+ characters) in the First Name field<br>2. Fill in the Last Name field with 'Doe'<br>3. Fill in the Zip/Postal Code field with '12345'<br>4. Click Continue | Form submits successfully; entity is created with the long First Name | low |
| TC-011 (input_edge) |  | Submit form with special characters in Last Name |  | 1. Fill in the First Name field with 'John'<br>2. Enter special characters in the Last Name field (e.g., '!@#$%^&*()')<br>3. Fill in the Zip/Postal Code field with '12345'<br>4. Click Continue | Form submits successfully; entity is created with the special characters in Last Name | low |

---

## Checkout - Overview

Total: **9** (positive: 2, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Complete the order successfully | User logged in as <Customer>, Order items are present in the cart | 1. Click Finish | completes the order and navigates to the confirmation page | high |
| TC-002 |  | Cancel the checkout process | User logged in as <Customer>, Order items are present in the cart | 1. Click Cancel | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to finish checkout without providing payment information |  | 1. Leave the Payment Information section blank<br>2. Click Finish | Form does not submit; error shown on Payment Information field indicating it is required | high |
| TC-004 |  | Attempt to finish checkout without providing shipping information |  | 1. Leave the Shipping Information section blank<br>2. Click Finish | Form does not submit; error shown on Shipping Information field indicating it is required | high |
| TC-005 |  | Attempt to finish checkout with empty order summary |  | 1. Ensure the Order Summary is empty<br>2. Click Finish | Form does not submit; error shown on Order Summary field indicating it is required | high |
| TC-006 |  | Attempt to finish checkout with empty totals section |  | 1. Ensure the Totals Section is empty<br>2. Click Finish | Form does not submit; error shown on Totals Section field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long string in the Order Summary field |  | 1. Enter a string of 200+ characters in the Order Summary field | Order Summary field accepts the input or displays an error indicating the input is too long | low |
| TC-008 (input_edge) |  | Enter special characters in the Payment Information field |  | 1. Enter special characters (e.g., !@#$%^&*) in the Payment Information field | Payment Information field accepts the input or displays a specific error message | low |
| TC-009 (input_edge) |  | Enter leading and trailing whitespace in the Shipping Information field |  | 1. Enter '   123 Main St   ' in the Shipping Information field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Checkout - Confirmation

Total: **6** (positive: 2, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display success message on confirmation page | User logged in as <Customer>, User has completed an order | 1. Navigate to the Confirmation page | The page displays 'Thank you for your order!' | high |
| TC-002 |  | Return to Product Inventory from confirmation page | User logged in as <Customer>, User has completed an order | 1. Click 'Back Home' button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to access the confirmation page without completing the checkout process |  | 1. Navigate to the confirmation page directly | User is redirected to the checkout process; confirmation page is not displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) |  | Enter a long success message |  | 1. Enter a very long string (over 200 characters) in the Success_Message field | The system displays a truncated version of the success message, indicating it has exceeded the character limit. | low |
| TC-005 (input_edge) |  | Enter special characters in the success message |  | 1. Enter a success message containing special characters (e.g., @#$%^&*()!) | The system accepts the special characters and displays the success message correctly. | low |
| TC-006 (input_edge) |  | Enter leading and trailing whitespace in the success message |  | 1. Enter a success message with leading and trailing spaces | The system trims the whitespace and displays the success message without extra spaces. | low |

---

## Logout

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs out | User logged in as <User> | 1. Click the Logout button | ends the session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to logout while not logged in | user is not logged in | 1. Click the Logout button | Logout action is blocked; user remains on the current page and is not redirected to the login page | high |

---

## Reset App State

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Reset App State clears the cart and resets UI elements | User logged in as <User> | 1. Click the Reset App State Button | The cart is cleared; the cart badge state is reset; the add/remove button states are reset | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to reset app state without any items in the cart |  | 1. Ensure the cart is empty<br>2. Click on the Reset App State Button | No changes occur; the cart remains empty and the cart badge state is unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapid consecutive clicks on Reset App State button | User is logged in and has items in the cart | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again | The cart is cleared; the cart badge state resets; the add/remove button states reset without any error shown. | medium |
| TC-004 (interaction_edge) |  | Click Reset App State button after clearing the cart | User is logged in and has already cleared the cart | 1. Click the Reset App State button | The cart remains empty; the cart badge state resets; the add/remove button states reset without any error shown. | low |

---
