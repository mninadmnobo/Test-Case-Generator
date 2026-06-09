# Test Cases — Swaglab

Generated: 2026-06-09T08:59:35.980641Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 72 | 20 | 24 | 28 | 30 | 26 | 10 |

## Login

Total: **10** (positive: 1, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <User> | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | authenticates and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Enter invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Error shown: 'Epic sadface: Username and password do not match any user in this service.' | medium |
| TC-006 |  | Attempt login with locked out user |  | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click Login | Error shown: 'Epic sadface: Sorry, this user has been locked out.' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error message displayed indicating that the username is invalid or trimmed to maximum length. | low |
| TC-008 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter '@#$%^&*()' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error message displayed indicating that the username is invalid. | low |
| TC-009 (input_edge) |  | Enter leading and trailing whitespace in the Username field |  | 1. Enter '   standard_user   ' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Leading/trailing whitespace is trimmed; user is redirected to the Product Inventory page. | low |
| TC-010 (input_edge) |  | Enter zero-length password |  | 1. Enter 'standard_user' in the Username field<br>2. Enter '' in the Password field<br>3. Click Login | Error message displayed: 'Epic sadface: Password is required.' | medium |

---

## Product Inventory

Total: **13** (positive: 5, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View product details | User logged in as <User> | 1. Navigate to the Product Inventory page<br>2. Click on a product name | Product Detail page is displayed with the selected product's information | high |
| TC-002 |  | Add product to cart | User logged in as <User> | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' on a product | The button changes to 'Remove' and the cart badge count updates accordingly | high |
| TC-003 |  | Remove product from cart | User logged in as <User>, Product is added to cart | 1. Navigate to the Product Inventory page<br>2. Click 'Remove' on the product | The button changes back to 'Add to cart' and the cart badge count updates accordingly | high |
| TC-004 |  | Sort products by name (A–Z) | User logged in as <User> | 1. Navigate to the Product Inventory page<br>2. Select 'Name (A–Z)' from the sort dropdown | Products are sorted in alphabetical order from A to Z | medium |
| TC-005 |  | Sort products by price (low–high) | User logged in as <User> | 1. Navigate to the Product Inventory page<br>2. Select 'Price (low–high)' from the sort dropdown | Products are sorted in ascending order by price | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Product Name field blank and submit |  | 1. Leave the Product Name field blank<br>2. Fill the Price field with a valid number<br>3. Click Add to cart | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-007 |  | Leave the Price field blank and submit |  | 1. Fill the Product Name field with a valid name<br>2. Leave the Price field blank<br>3. Click Add to cart | Inline validation error appears on the Price field indicating it is required | high |
| TC-008 |  | Enter a non-numeric value in the Price field |  | 1. Fill the Product Name field with a valid name<br>2. Enter <non-numeric value> in the Price field<br>3. Click Add to cart | Inline validation error appears on the Price field indicating it must be a number | medium |
| TC-009 |  | Attempt to remove an item that is not in the cart |  | 1. Click Remove on a product that is not in the cart | No action occurs; the item remains unchanged in the cart | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter a valid price of 0 in the Price field |  | 1. Enter 0 in the Price field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the price of 0 | medium |
| TC-011 (boundary) |  | Enter a valid price of 1 in the Price field |  | 1. Enter 1 in the Price field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the price of 1 | medium |
| TC-012 (input_edge) |  | Enter a very long product name |  | 1. Enter a string of 200+ characters in the Product_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; product name is displayed correctly in the data table | low |
| TC-013 (input_edge) |  | Enter special characters in the Product_Name field |  | 1. Enter '!@#$%^&*()_+' in the Product_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; product name is displayed correctly in the data table | low |

---

## Product Detail

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Add product to cart | User logged in as <Customer>, Product is selected | 1. Click the 'Add to cart' button | The cart state updates to reflect the added product | high |
| TC-002 |  | Remove product from cart | User logged in as <Customer>, Product is already in the cart | 1. Click the 'Remove' button | The cart state updates to reflect the removed product | high |
| TC-003 |  | Navigate back to products | User logged in as <Customer>, Product Detail page is open | 1. Click the 'Back to products' button | Navigates to Product Inventory page | medium |
| TC-004 |  | Navigate to shopping cart | User logged in as <Customer>, Product Detail page is open | 1. Click the Cart Icon | Navigates to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to add a product to the cart when the product is out of stock | Product is out of stock | 1. Click on the 'Add to cart' button | Action is blocked; cart state remains unchanged; no product is added to the cart | high |
| TC-006 |  | Attempt to navigate back to products |  | 1. Click on the 'Back to products' button | Navigates to the Product Inventory page successfully | medium |
| TC-007 |  | Attempt to navigate to the shopping cart |  | 1. Click on the Cart Icon | Navigates to the Shopping Cart page successfully | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) |  | Rapidly click 'Add to cart' button twice | User is on the Product Detail page | 1. Click the 'Add to cart' button<br>2. Immediately click the 'Add to cart' button again | 'Add to cart' button reflects the current cart state; no duplicate items are added to the cart | medium |
| TC-009 (interaction_edge) |  | Click 'Back to products' button after adding to cart | User has clicked 'Add to cart' and the item is in the cart | 1. Click the 'Back to products' button | User is navigated to the Product Inventory page; cart state remains unchanged | medium |
| TC-010 (interaction_edge) |  | Click 'Cart Icon' after adding an item to cart | User has added an item to the cart | 1. Click the Cart Icon | User is navigated to the Shopping Cart page showing the added item | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <Customer>, Shopping cart has items added | 1. Click 'Remove' button for an item in the cart | The item is no longer visible in the cart | high |
| TC-002 | WF-002 | Continue shopping from the cart | User logged in as <Customer>, Shopping cart has items added | 1. Click 'Continue Shopping' button | returns to Product Inventory | medium |
| TC-003 | WF-003 | Begin checkout from the cart | User logged in as <Customer>, Shopping cart has items added | 1. Click 'Checkout' button | begins checkout | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to click 'Checkout' without any items in the cart |  | 1. Ensure the cart is empty<br>2. Click the 'Checkout' button | Checkout action is blocked; no transition occurs and the cart remains empty | high |
| TC-005 |  | Attempt to click 'Remove' on an item when no items are present in the cart |  | 1. Ensure the cart is empty<br>2. Attempt to click the 'Remove' button | Remove action is blocked; no items are removed and the cart remains empty | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) |  | Rapidly click 'Checkout' after adding an item | At least one item is in the cart | 1. Click 'Checkout'<br>2. Immediately click 'Checkout' again | 'Checkout' action succeeds; user is taken to the checkout page without errors. |  |
| TC-007 (interaction_edge) |  | Click 'Continue Shopping' after adding an item | At least one item is in the cart | 1. Click 'Continue Shopping' | User is redirected to the Product Inventory page without losing the cart state. |  |
| TC-008 (input_edge) |  | Remove an item from the cart | At least one item is in the cart | 1. Click 'Remove' on the first item in the cart | The item is removed from the cart; the cart updates to reflect the change. |  |
| TC-009 (input_edge) |  | Attempt to remove an item when the cart is empty | Cart is empty | 1. Attempt to click 'Remove' on a non-existent item | No action is taken; a message indicates the cart is empty. |  |

---

## Checkout - Information

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit the checkout information form with valid data | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel the checkout information form | User logged in as <Customer> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill Last Name with <valid value><br>3. Fill Zip/Postal Code with <valid value><br>4. Click Continue | Error: First Name is required is displayed | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Fill First Name with <valid value><br>2. Leave the Last Name field blank<br>3. Fill Zip/Postal Code with <valid value><br>4. Click Continue | Error: Last Name is required is displayed | high |
| TC-005 |  | Leave the Zip/Postal Code field blank and submit |  | 1. Fill First Name with <valid value><br>2. Fill Last Name with <valid value><br>3. Leave the Zip/Postal Code field blank<br>4. Click Continue | Error: Postal Code is required is displayed | high |
| TC-006 |  | Leave all required fields empty and submit |  | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Zip/Postal Code field blank<br>4. Click Continue | Error: First Name is required, Error: Last Name is required, Error: Postal Code is required are displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Submit with First Name field empty |  | 1. Leave the First Name field empty<br>2. Fill in the Last Name field with a valid name<br>3. Fill in the Zip/Postal Code field with a valid code<br>4. Click Continue | Error banner displays 'Error: First Name is required' | medium |
| TC-008 (boundary) |  | Submit with Last Name field empty |  | 1. Fill in the First Name field with a valid name<br>2. Leave the Last Name field empty<br>3. Fill in the Zip/Postal Code field with a valid code<br>4. Click Continue | Error banner displays 'Error: Last Name is required' | medium |
| TC-009 (boundary) |  | Submit with Zip/Postal Code field empty |  | 1. Fill in the First Name field with a valid name<br>2. Fill in the Last Name field with a valid name<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner displays 'Error: Postal Code is required' | medium |
| TC-010 (input_edge) |  | Submit with long string in First Name |  | 1. Enter a very long string in the First Name field (200+ characters)<br>2. Fill in the Last Name field with a valid name<br>3. Fill in the Zip/Postal Code field with a valid code<br>4. Click Continue | Form submits successfully; entity is created with the long First Name | low |
| TC-011 (input_edge) |  | Submit with special characters in Last Name |  | 1. Fill in the First Name field with a valid name<br>2. Enter special characters in the Last Name field<br>3. Fill in the Zip/Postal Code field with a valid code<br>4. Click Continue | Form submits successfully; entity is created with the special characters in Last Name | low |

---

## Checkout - Overview

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete the order successfully | User logged in as <Customer>, Order items are present in the cart | 1. Click Finish | completes the order and navigates to the confirmation page | high |
| TC-002 | WF-002 | Cancel the checkout process | User logged in as <Customer>, Order items are present in the cart | 1. Click Cancel | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to finish checkout without any payment information |  | 1. Leave the Payment Information blank<br>2. Click Finish | Form does not submit; error shown indicating Payment Information is required | high |
| TC-004 |  | Attempt to finish checkout without any shipping information |  | 1. Leave the Shipping Information blank<br>2. Click Finish | Form does not submit; error shown indicating Shipping Information is required | high |
| TC-005 |  | Click Cancel to exit checkout |  | 1. Click Cancel | Exits checkout without completing the order | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long string in the Order Summary field |  | 1. Enter a string of 200+ characters in the Order Summary field | Order Summary field accepts the input without error or truncation | low |
| TC-007 (input_edge) |  | Enter special characters in the Payment Information field |  | 1. Enter special characters (e.g., @#$%^&*) in the Payment Information field | Payment Information field accepts the input without error | low |
| TC-008 (input_edge) |  | Enter leading and trailing whitespace in the Shipping Information field |  | 1. Enter '   Shipping Address   ' in the Shipping Information field | Leading/trailing whitespace is trimmed; saved value shown has no extra spaces | low |

---

## Checkout - Confirmation

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User returns to Product Inventory from Confirmation page | User logged in as <Customer>, User has completed a purchase | 1. Click 'Back Home' button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access the confirmation page without completing the checkout process |  | 1. Navigate to the confirmation page directly | User is redirected to the login page or an error message is displayed indicating that the checkout process is incomplete | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully submitted an order and is on the confirmation page. | 1. Click the 'Back Home' button.<br>2. Immediately press the browser back button. | User is redirected to the Product Inventory page; no duplicate order is created. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs out | User logged in as <User> | 1. Click the Logout button | ends the session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to logout while not logged in | User is not logged in | 1. Attempt to click the Logout button | Logout action is blocked; user remains on the current page and is not redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapid consecutive logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is blocked; user remains on the login page without any session termination | medium |
| TC-004 (interaction_edge) |  | Logout after session timeout | User was logged in, but session has timed out | 1. Click the Logout button | Logout action is blocked; user remains on the current page with an error message indicating session timeout | medium |

---

## Reset App State

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Reset app state successfully | User logged in as <User> | 1. Click Reset App State Button | clears cart and resets in-app state | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to reset app state without being logged in | User is not logged in | 1. Attempt to click the Reset App State Button | User is blocked from resetting app state; remains on the current page without any changes. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapid consecutive clicks on the Reset App State button | User is logged in and has items in the cart | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again | The app state resets successfully; the cart is cleared and the reset action is confirmed without errors. |  |
| TC-004 (interaction_edge) |  | Click the Reset App State button after adding an item to the cart | User is logged in and has added items to the cart | 1. Add an item to the cart<br>2. Click the Reset App State button | The cart is cleared and the in-app state resets; the cart badge is updated to reflect the cleared state. |  |

---
