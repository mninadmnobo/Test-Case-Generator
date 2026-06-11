# Test Cases — Swaglab

Generated: 2026-06-09T08:57:45.212814Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 70 | 21 | 23 | 26 | 27 | 34 | 6 |

## Login

Total: **11** (positive: 1, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <User> | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | authenticates and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to login with empty Username |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Error banner displays: 'Epic sadface: Username is required.' | high |
| TC-003 |  | Attempt to login with empty Password |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Login | Error banner displays: 'Epic sadface: Password is required.' | high |
| TC-004 |  | Attempt to login with invalid credentials |  | 1. Fill the Username field with <invalid username><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error banner displays: 'Epic sadface: Username and password do not match any user in this service.' | medium |
| TC-005 |  | Attempt to login with locked out user |  | 1. Fill the Username field with locked_out_user<br>2. Fill the Password field with secret_sauce<br>3. Click Login | Error banner displays: 'Epic sadface: Sorry, this user has been locked out.' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) | WF-002 | Attempt to log in with empty Username |  | 1. Leave the Username field empty<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Epic sadface: Username is required. | medium |
| TC-007 (input_edge) | WF-003 | Attempt to log in with empty Password |  | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field empty<br>3. Click Login | Epic sadface: Password is required. | medium |
| TC-008 (input_edge) | WF-004 | Attempt to log in with invalid credentials |  | 1. Enter 'invalid_user' in the Username field<br>2. Enter 'wrong_password' in the Password field<br>3. Click Login | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-009 (input_edge) | WF-005 | Attempt to log in with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-010 (input_edge) |  | Enter long text in Username field |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Error message is displayed indicating the Username is too long or it accepts the input with truncation. | low |
| TC-011 (input_edge) |  | Enter special characters in Password field |  | 1. Enter 'standard_user' in the Username field<br>2. Enter special characters '!@#$%^&*()' in the Password field<br>3. Click Login | Error message is displayed indicating invalid password or it accepts the input. | low |

---

## Product Inventory

Total: **11** (positive: 5, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Product Detail from Product Inventory | User logged in as <Role> | 1. Click on a product name or image in the Product Inventory page | opens Product Detail page | high |
| TC-002 | WF-002 | Add item to cart from Product Inventory | User logged in as <Role> | 1. Click 'Add to cart' button for a product in the Product Inventory page | adds item to cart; button changes to 'Remove'; cart badge count increments | high |
| TC-003 | WF-003 | Remove item from cart in Product Inventory | User logged in as <Role>, Item is already in the cart | 1. Click 'Remove' button for the item in the Product Inventory page | removes item from cart; button changes to 'Add to cart'; cart badge count decrements | high |
| TC-004 |  | Sort products by Name A–Z | User logged in as <Role> | 1. Select 'Name A–Z' from the Sort_By dropdown | Products are sorted in alphabetical order from A to Z | medium |
| TC-005 |  | Sort products by Price low–high | User logged in as <Role> | 1. Select 'Price low–high' from the Sort_By dropdown | Products are sorted in ascending order by price | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to add a product to cart without being logged in | User is not logged in | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' on any product | User is redirected to the login page | high |
| TC-007 | WF-002 | Attempt to add the same product to cart multiple times |  | 1. Click 'Add to cart' on a product<br>2. Click 'Add to cart' on the same product again | Cart badge count does not increment beyond 1; error message displayed indicating product is already in the cart | medium |
| TC-008 | WF-003 | Attempt to remove a product from cart when it is not in the cart |  | 1. Click 'Remove' on a product that is not in the cart | Error message displayed indicating product is not in the cart | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (interaction_edge) | WF-002 | Rapid add to cart and remove actions | User is logged in, Product is available in inventory | 1. Click 'Add to cart' for a product<br>2. Immediately click 'Remove' for the same product | Cart badge count decrements by 1; button changes back to 'Add to cart' | medium |
| TC-010 (interaction_edge) | WF-001 | View product detail after rapid actions | User is logged in, Product is available in inventory | 1. Click 'Add to cart' for a product<br>2. Click 'View Product Detail' for the same product | Product Detail page opens without any error; cart remains unchanged | medium |
| TC-011 (input_edge) |  | Sort dropdown edge cases | User is logged in, Product list is populated | 1. Select 'Name A–Z' from the Sort By dropdown<br>2. Select 'Name Z–A' from the Sort By dropdown<br>3. Select 'Price low–high' from the Sort By dropdown<br>4. Select 'Price high–low' from the Sort By dropdown | Product list updates correctly for each sorting option without any errors | low |

---

## Product Detail

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Role>, Product is currently not in cart | 1. Click 'Add to cart' button | Product added to cart | high |
| TC-002 | WF-002 | Remove product from cart | User logged in as <Role>, Product is currently in cart | 1. Click 'Remove' button | Product removed from cart | high |
| TC-003 | WF-003 | Navigate back to products | User logged in as <Role> | 1. Click 'Back to products' button | Returned to Product Inventory page | medium |
| TC-004 | WF-004 | Go to Shopping Cart | User logged in as <Role> | 1. Click 'Go to Shopping Cart' button | Navigated to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to add product to cart when it is already in the cart | Product is already in cart | 1. Click 'Add to cart' button | Action is blocked; 'Add to cart' button is not available in the current state. | high |
| TC-006 | WF-002 | Attempt to remove product from cart when it is not in the cart | Product is not in cart | 1. Click 'Remove' button | Action is blocked; 'Remove' button is not available in the current state. | high |
| TC-007 | WF-003 | Attempt to navigate back to products |  | 1. Click 'Back to products' button | Navigated to Product Inventory page. | medium |
| TC-008 | WF-004 | Attempt to go to shopping cart |  | 1. Click 'Go to Shopping Cart' button | Navigated to Shopping Cart. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (state_edge) | WF-001 | Rapid consecutive state transitions after adding to cart | Product is currently Not_In_Cart | 1. Click 'Add to cart'<br>2. Immediately click 'Remove' | Product is removed from cart; state changes to Not_In_Cart | medium |
| TC-010 (state_edge) | WF-002 | Rapid consecutive state transitions after removing from cart | Product is currently In_Cart | 1. Click 'Remove'<br>2. Immediately click 'Add to cart' | Product is added to cart; state changes to In_Cart | medium |
| TC-011 (interaction_edge) | WF-003 | Navigate back to products after adding to cart | Product is currently In_Cart | 1. Click 'Back to products' | Returned to Product Inventory page; product state remains In_Cart | low |
| TC-012 (interaction_edge) | WF-004 | Navigate to Shopping Cart after adding product | Product is currently In_Cart | 1. Click 'Go to Shopping Cart' | Navigated to Shopping Cart; product is listed in the cart | low |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <Role>, Cart contains at least one item | 1. Click the 'Remove' button next to an item in the cart | Item removed from cart | high |
| TC-002 | WF-002 | Continue shopping | User logged in as <Role>, Cart contains items | 1. Click the 'Continue Shopping' button | returns to Product Inventory | medium |
| TC-003 | WF-003 | Begin checkout | User logged in as <Role>, Cart contains items | 1. Click the 'Checkout' button | begins checkout | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to remove an item from the cart when the cart is empty |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Remove' button for an item | No action occurs; the cart remains empty and no items are removed |  |
| TC-005 | WF-002 | Attempt to continue shopping when no items are in the cart |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Continue Shopping' button | Remains on the Shopping Cart page; no navigation occurs |  |
| TC-006 | WF-003 | Attempt to checkout when the cart is empty |  | 1. Ensure the shopping cart is empty<br>2. Click the 'Checkout' button | No action occurs; remains on the Shopping Cart page |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly remove items from the cart | User has multiple items in the cart | 1. Click 'Remove' on the first item<br>2. Immediately click 'Remove' on the second item | Both items are removed from the cart; the cart updates correctly without errors. | medium |
| TC-008 (interaction_edge) | WF-002 | Return to Product Inventory after adding items | User has items in the cart | 1. Click 'Continue Shopping' | User is redirected to Product Inventory; cart remains unchanged. | medium |
| TC-009 (interaction_edge) | WF-003 | Checkout with items in the cart | User has items in the cart | 1. Click 'Checkout' | User is directed to the checkout process; items from the cart are retained. | medium |

---

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Checkout Form with valid information | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel Checkout Form | User logged in as <Customer> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave First Name blank and submit |  | 1. Leave the First Name field blank<br>2. Fill Last Name and Zip/Postal Code with valid values<br>3. Click Continue | Inline validation error appears on the First Name field indicating it is required | high |
| TC-004 | WF-001 | Leave Last Name blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill First Name and Zip/Postal Code with valid values<br>3. Click Continue | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Zip/Postal Code blank and submit |  | 1. Leave the Zip/Postal Code field blank<br>2. Fill First Name and Last Name with valid values<br>3. Click Continue | Inline validation error appears on the Zip/Postal Code field indicating it is required | high |
| TC-006 | WF-001 | Leave all required fields blank and submit |  | 1. Leave the First Name, Last Name, and Zip/Postal Code fields blank<br>2. Click Continue | Inline validation error appears on the First Name field indicating it is required; Inline validation error appears on the Last Name field indicating it is required; Inline validation error appears on the Zip/Postal Code field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Submit form with First Name empty |  | 1. Leave the First Name field empty<br>2. Fill Last Name with valid data<br>3. Fill Zip/Postal Code with valid data<br>4. Click Continue | Error banner displays 'Error: First Name is required' | medium |
| TC-008 (boundary) | WF-001 | Submit form with Last Name empty |  | 1. Fill First Name with valid data<br>2. Leave the Last Name field empty<br>3. Fill Zip/Postal Code with valid data<br>4. Click Continue | Error banner displays 'Error: Last Name is required' | medium |
| TC-009 (boundary) | WF-001 | Submit form with Zip/Postal Code empty |  | 1. Fill First Name with valid data<br>2. Fill Last Name with valid data<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner displays 'Error: Postal Code is required' | medium |
| TC-010 (interaction_edge) | WF-002 | Click Cancel after filling some fields |  | 1. Fill First Name with valid data<br>2. Fill Last Name with valid data<br>3. Click Cancel | User is returned to the Shopping Cart without any data saved | low |

---

## Checkout - Overview

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish the order successfully | User logged in as <Role> | 1. Click Finish | completes the order and navigates to the confirmation page | high |
| TC-002 | WF-002 | Cancel the checkout successfully | User logged in as <Role> | 1. Click Cancel | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to finish the order without any payment information |  | 1. Leave the Payment Information section blank<br>2. Click Finish | Form does not submit; error shown indicating Payment Information is required | high |
| TC-004 | WF-002 | Attempt to cancel the checkout without any prior action |  | 1. Click Cancel | Exits checkout without any changes made to the order | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid re-submission after redirect | Order summary is displayed, User has valid payment and shipping information | 1. Click the Finish button to complete the order<br>2. Press the browser back button immediately after the confirmation page loads | User is redirected to the checkout overview step without the order being duplicated | medium |
| TC-006 (interaction_edge) | WF-002 | Cancel checkout and verify exit behavior | User is on the checkout overview step | 1. Click the Cancel button | User is exited from the checkout process and returns to the previous page | medium |

---

## Checkout - Confirmation

Total: **4** (positive: 2, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User views confirmation message and returns to product inventory | User logged in as <Customer>, Order has been successfully placed | 1. Observe the confirmation page | The page shows 'Thank you for your order!' and returns to Product Inventory and clears the cart | high |
| TC-002 | WF-001 | User clicks Back Home button | User logged in as <Customer>, Order has been successfully placed | 1. Click Back Home button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to click 'Back Home' without any prior action |  | 1. Navigate to the Confirmation Page<br>2. Click the 'Back Home' button | The page remains on the Confirmation Page; no transition occurs; the cart is not cleared. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully completed the checkout process | 1. Click the 'Back Home' button | User is redirected to Product Inventory; the cart is cleared and the confirmation page is not pre-filled | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click on the Logout button | ends the session and returns the user to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to logout while not logged in | user must not be logged in | 1. Ensure the user is not logged in<br>2. Click on the Logout button | Logout action is not performed; user remains on the current page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Attempt to log out when already logged out | User is not logged in | 1. Click the Logout button | Logout button is disabled or does not respond to the click | medium |
| TC-004 (interaction_edge) | WF-001 | Rapid consecutive logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is ignored; user is redirected to the login page only once | medium |

---

## Reset App State

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State successfully clears the cart and resets in-app state | User logged in as <role> | 1. Click Reset App State Button | clears the cart, resets in-app state, including cart badge and add/remove button states | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to reset app state without any preconditions |  | 1. Click on the Reset App State button | No action occurs; the app state remains unchanged. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid consecutive state transitions after reset | User is logged in and has items in the cart | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again | Second reset action is blocked; a message indicates that the state is already reset | medium |

---
