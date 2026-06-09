# Test Cases — Swaglab

Generated: 2026-06-09T08:58:25.975004Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 72 | 21 | 23 | 28 | 33 | 29 | 10 |

## Login

Total: **12** (positive: 1, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <Role> | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | User is authenticated and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Attempt to login with empty Username |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 | WF-003 | Attempt to login with empty Password |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 | WF-004 | Attempt to login with invalid credentials |  | 1. Fill the Username field with <invalid username><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error banner displays 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-005 | WF-005 | Attempt to login with locked out user |  | 1. Fill the Username field with 'locked_out_user'<br>2. Fill the Password field with <valid password><br>3. Click Login | Error banner displays 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-002 | Submit with empty Username |  | 1. Leave the Username field empty<br>2. Enter a valid Password<br>3. Click Login | Epic sadface: Username is required. | medium |
| TC-007 (boundary) | WF-003 | Submit with empty Password |  | 1. Enter a valid Username<br>2. Leave the Password field empty<br>3. Click Login | Epic sadface: Password is required. | medium |
| TC-008 (boundary) | WF-004 | Submit with invalid credentials |  | 1. Enter a Username that is not in the accepted list<br>2. Enter a random Password<br>3. Click Login | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-009 (boundary) | WF-005 | Login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter the shared Password 'secret_sauce'<br>3. Click Login | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-010 (input_edge) |  | Submit with long Username |  | 1. Enter a very long string (200+ characters) in the Username field<br>2. Enter the shared Password 'secret_sauce'<br>3. Click Login | The form displays an error indicating the username is too long. | low |
| TC-011 (input_edge) |  | Submit with special characters in Username |  | 1. Enter special characters (e.g., '@#$%^&*') in the Username field<br>2. Enter the shared Password 'secret_sauce'<br>3. Click Login | The form displays an error indicating the username is invalid. | low |
| TC-012 (input_edge) |  | Submit with leading/trailing whitespace in Username |  | 1. Enter '   standard_user   ' in the Username field<br>2. Enter the shared Password 'secret_sauce'<br>3. Click Login | Leading/trailing whitespace is trimmed; user is redirected to Product Inventory page. | low |

---

## Product Inventory

Total: **14** (positive: 7, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View product detail | User logged in as <Role> | 1. Click on a product name or image | Product detail page opens | high |
| TC-002 | WF-002 | Add product to cart | User logged in as <Role>, Product is not in cart | 1. Click 'Add to cart' button for a product | Button changes to 'Remove'; cart badge count updates accordingly | high |
| TC-003 | WF-003 | Remove product from cart | User logged in as <Role>, Product is in cart | 1. Click 'Remove' button for a product | removes item from cart | high |
| TC-004 |  | Sort products by name A-Z | User logged in as <Role> | 1. Select 'Name (A–Z)' from the Sort By dropdown | Products are sorted in ascending order by name | medium |
| TC-005 |  | Sort products by name Z-A | User logged in as <Role> | 1. Select 'Name (Z–A)' from the Sort By dropdown | Products are sorted in descending order by name | medium |
| TC-006 |  | Sort products by price low-high | User logged in as <Role> | 1. Select 'Price (low–high)' from the Sort By dropdown | Products are sorted in ascending order by price | medium |
| TC-007 |  | Sort products by price high-low | User logged in as <Role> | 1. Select 'Price (high–low)' from the Sort By dropdown | Products are sorted in descending order by price | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to add a product to cart when it is already in the cart | Product is already in cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Remove' button for the product | Status remains 'In_Cart'; no transition occurs; 'Add to cart' button is visible | high |
| TC-009 |  | Attempt to remove a product from cart when it is not in the cart | Product is not in cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Remove' button for the product | Status remains 'Not_In_Cart'; no transition occurs; 'Add to cart' button is visible | high |
| TC-010 |  | Attempt to sort products without selecting a sort option |  | 1. Navigate to the Product Inventory page<br>2. Leave the 'Sort By' dropdown unchanged<br>3. Attempt to sort the products | Products remain unsorted; no sorting action occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (state_edge) | WF-002 | Rapid consecutive state transitions for adding to cart | Product is not in cart | 1. Click 'Add to cart'<br>2. Immediately click 'Add to cart' again | Second 'Add to cart' action is blocked; button remains 'Remove' | medium |
| TC-012 (state_edge) | WF-003 | Rapid consecutive state transitions for removing from cart | Product is in cart | 1. Click 'Remove'<br>2. Immediately click 'Remove' again | Second 'Remove' action is blocked; product remains removed from cart | medium |
| TC-013 (input_edge) |  | Sort dropdown with special characters |  | 1. Select 'Name (A–Z)' from the Sort By dropdown<br>2. Select 'Name (Z–A)' from the Sort By dropdown | Products are sorted correctly by name in both ascending and descending order | low |
| TC-014 (input_edge) |  | Sort dropdown with leading/trailing whitespace |  | 1. Select '  Price (low–high)  ' from the Sort By dropdown | Leading/trailing whitespace is trimmed; products are sorted by price low to high | low |

---

## Product Detail

Total: **6** (positive: 3, negative: 3, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Role>, Product is displayed on the Product Detail page | 1. Click the 'Add to cart / Remove' button | The cart state updates to reflect the added product | high |
| TC-002 | WF-002 | Navigate back to products | User logged in as <Role>, Product is displayed on the Product Detail page | 1. Click the 'Back to products' button | Navigates to Product Inventory page | medium |
| TC-003 | WF-003 | Navigate to shopping cart | User logged in as <Role>, Product is displayed on the Product Detail page | 1. Click the Cart Icon | Navigates to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to add a product to the cart when the cart is already full | Cart is full | 1. Click on the 'Add to cart / Remove' button | Action is blocked; cart state remains unchanged; error message displayed indicating the cart is full. | high |
| TC-005 | WF-002 | Attempt to navigate back to products when the product detail page is not loaded | Product detail page is not loaded | 1. Click on the 'Back to products' button | Navigation is blocked; user remains on the current page; no transition occurs. | high |
| TC-006 | WF-003 | Attempt to navigate to the shopping cart when the cart is empty | Cart is empty | 1. Click on the 'Cart Icon' | Navigation is blocked; user remains on the Product Detail page; error message displayed indicating the cart is empty. | high |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove item from cart | User logged in as <Role>, Cart contains items | 1. Click 'Remove' button for an item in the cart | Item removed from cart | high |
| TC-002 | WF-002 | Continue shopping | User logged in as <Role>, Cart contains items | 1. Click 'Continue Shopping' button | returns to Product Inventory | medium |
| TC-003 | WF-003 | Begin checkout | User logged in as <Role>, Cart contains items | 1. Click 'Checkout' button | begins checkout | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to remove an item from the cart when the cart is empty |  | 1. Ensure the cart is empty<br>2. Click the 'Remove' button for an item | No action occurs; the item is not removed from the cart; an error message is displayed indicating that the cart is empty. | high |
| TC-005 | WF-002 | Attempt to continue shopping when no items are in the cart |  | 1. Ensure the cart is empty<br>2. Click the 'Continue Shopping' button | No action occurs; the user remains on the Shopping Cart page; an error message is displayed indicating that there are no items to continue shopping with. | high |
| TC-006 | WF-003 | Attempt to checkout when the cart is empty |  | 1. Ensure the cart is empty<br>2. Click the 'Checkout' button | No action occurs; the user remains on the Shopping Cart page; an error message is displayed indicating that the cart is empty. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapid removal of items from cart | User has multiple items in the cart | 1. Click 'Remove' on the first item in the cart<br>2. Immediately click 'Remove' on the second item | Both items are removed from the cart; the cart updates successfully without errors. | medium |
| TC-008 (interaction_edge) | WF-002 | Continue shopping after removing items | User has items in the cart | 1. Click 'Remove' on an item in the cart<br>2. Click 'Continue Shopping' button | User is returned to Product Inventory without the removed item in the cart. | medium |
| TC-009 (interaction_edge) | WF-003 | Checkout with items in cart | User has items in the cart | 1. Click 'Checkout' button | User begins the checkout process with items still in the cart. | medium |

---

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit form with valid data | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel and return to Shopping Cart | User logged in as <Role> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill Last Name with <valid last name><br>3. Fill Zip/Postal Code with <valid zip code><br>4. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Fill First Name with <valid first name><br>2. Leave the Last Name field blank<br>3. Fill Zip/Postal Code with <valid zip code><br>4. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Zip/Postal Code field blank and submit |  | 1. Fill First Name with <valid first name><br>2. Fill Last Name with <valid last name><br>3. Leave the Zip/Postal Code field blank<br>4. Click Continue | Inline validation error appears on the Zip_Postal_Code field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Zip/Postal Code field blank<br>4. Click Continue | Form does not submit; errors shown on First_Name, Last_Name, and Zip_Postal_Code fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | First Name field is empty |  | 1. Leave the First Name field empty<br>2. Fill in Last Name and Zip/Postal Code with valid values<br>3. Click Continue | Error banner displays 'Error: First Name is required' | medium |
| TC-008 (boundary) |  | Last Name field is empty |  | 1. Leave the Last Name field empty<br>2. Fill in First Name and Zip/Postal Code with valid values<br>3. Click Continue | Error banner displays 'Error: Last Name is required' | medium |
| TC-009 (boundary) |  | Zip/Postal Code field is empty |  | 1. Leave the Zip/Postal Code field empty<br>2. Fill in First Name and Last Name with valid values<br>3. Click Continue | Error banner displays 'Error: Postal Code is required' | medium |
| TC-010 (input_edge) |  | Enter long text in First Name field |  | 1. Enter a string longer than 200 characters in the First Name field<br>2. Fill in Last Name and Zip/Postal Code with valid values<br>3. Click Continue | Form submits successfully; First Name displays the entered value on the overview step | low |

---

## Checkout - Overview

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish the order successfully | User logged in as <Role> | 1. Click Finish | completes the order and navigates to the confirmation page | high |
| TC-002 | WF-002 | Cancel the checkout successfully | User logged in as <Role> | 1. Click Cancel | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to finish the order without providing payment information |  | 1. Leave the Payment Information section blank<br>2. Click Finish | Form does not submit; error shown on Payment Information field indicating it is required | high |
| TC-004 |  | Attempt to finish the order without providing shipping information |  | 1. Leave the Shipping Information section blank<br>2. Click Finish | Form does not submit; error shown on Shipping Information field indicating it is required | high |
| TC-005 |  | Click Cancel to exit checkout |  | 1. Click Cancel | Exits checkout; no order is completed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully completed the order | 1. Click Finish to complete the order<br>2. Press the browser back button | User is redirected to the confirmation page without a second order being created | medium |
| TC-007 (interaction_edge) | WF-002 | Cancel checkout after starting | User is on the checkout overview step | 1. Click Cancel to exit checkout | User is exited from the checkout process and returned to the previous page | medium |
| TC-008 (input_edge) |  | Enter long text in payment information | User is filling out the payment information | 1. Enter a very long string (200+ characters) in the Payment Information field | Field accepts the input or shows a visible error indicating the input is too long | low |
| TC-009 (input_edge) |  | Enter special characters in shipping information | User is filling out the shipping information | 1. Enter special characters (e.g., !@#$%^&*) in the Shipping Information field | Field accepts the input or shows a specific error indicating invalid characters | low |

---

## Checkout - Confirmation

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User views confirmation message and returns to product inventory | User logged in as <Customer>, User has completed an order | 1. Observe the confirmation page displays the success message<br>2. Click the 'Back Home' button | The page shows 'Thank you for your order!' and returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to click 'Back Home' without a successful order |  | 1. Navigate to the Checkout - Confirmation page<br>2. Click the 'Back Home' button | No action occurs; the user remains on the Confirmation page and the cart is not cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully completed the checkout process | 1. Click the 'Back Home' button | User is redirected to the Product Inventory page; the cart is cleared and the confirmation message is not displayed. | medium |
| TC-004 (input_edge) |  | Leading/trailing whitespace in success message | Confirmation page is displayed | 1. Observe the 'Success_Message' field | 'Success_Message' displays 'Thank you for your order!' without leading or trailing whitespace. | low |
| TC-005 (input_edge) |  | Special characters in success message | Confirmation page is displayed | 1. Observe the 'Success_Message' field | 'Success_Message' displays 'Thank you for your order!' without any errors despite special characters being present. | low |

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
| TC-002 | WF-001 | Attempt to logout while not logged in | user must not be logged in | 1. Ensure the user is not logged in<br>2. Click the Logout button | Logout action is not performed; user remains on the current page and is not redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click Logout button<br>2. Immediately click Logout button again | Second logout attempt is blocked; user remains on the login page without session termination. | medium |
| TC-004 (input_edge) |  | Attempt to access protected pages after logout | User is logged in, User clicks Logout | 1. Click Logout button<br>2. Attempt to navigate to inventory page | User is redirected to the login page; access to inventory page is blocked. | medium |

---

## Reset App State

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State action clears the cart and resets in-app state | User logged in as <Role> | 1. Click the 'Reset App State' button | The cart is cleared and the in-app state is reset | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to reset app state without any preconditions |  | 1. Click on the 'Reset App State' button | The app state remains unchanged; the cart is not cleared and no reset occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid consecutive clicks on Reset App State button | User is logged in and has items in the cart | 1. Click the Reset App State button quickly multiple times | Only one reset action occurs; cart is cleared and in-app state is reset without errors. | medium |

---
