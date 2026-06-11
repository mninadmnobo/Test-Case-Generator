# Test Cases — Swaglab

Generated: 2026-06-10T18:38:42.206508Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 77 | 23 | 25 | 29 | 34 | 34 | 9 |

## Login

Total: **12** (positive: 1, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User>, User is on the Login page | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | User is authenticated and redirected to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Error banner shows 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-005 |  | Attempt to login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | Error banner shows 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-002 | Attempt login with empty Username field |  | 1. Leave the Username field empty<br>2. Enter a valid password in the Password field<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-007 (boundary) | WF-003 | Attempt login with empty Password field |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |
| TC-008 (boundary) | WF-004 | Attempt login with invalid credentials |  | 1. Enter a username that is not in the accepted usernames list<br>2. Enter the shared password 'secret_sauce' in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-009 (boundary) | WF-005 | Attempt login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter the shared password 'secret_sauce' in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-010 (input_edge) |  | Enter long string in Username field |  | 1. Enter a very long string (200+ characters) in the Username field<br>2. Enter the shared password 'secret_sauce' in the Password field<br>3. Click the Login button | Login attempt is blocked; an error message is displayed indicating the username is invalid. | low |
| TC-011 (input_edge) |  | Enter special characters in Username field |  | 1. Enter special characters (e.g., @#$%^&) in the Username field<br>2. Enter the shared password 'secret_sauce' in the Password field<br>3. Click the Login button | Login attempt is blocked; an error message is displayed indicating the username is invalid. | low |
| TC-012 (input_edge) |  | Enter leading/trailing whitespace in Username field |  | 1. Enter '   standard_user   ' in the Username field<br>2. Enter the shared password 'secret_sauce' in the Password field<br>3. Click the Login button | Leading/trailing whitespace is trimmed; the username is saved as 'standard_user'. | low |

---

## Product Inventory

Total: **16** (positive: 7, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Product Detail | User logged in as <Role> | 1. Click on a product name or image | opens Product Detail page | high |
| TC-002 | WF-002 | Add to cart when not in cart | User logged in as <Role>, Product is not in cart | 1. Click 'Add to cart' button | The 'Add to cart' button changes to 'Remove'; the cart badge count updates accordingly. | high |
| TC-003 | WF-003 | Remove from cart when in cart | User logged in as <Role>, Product is in cart | 1. Click 'Remove' button | removes item from cart | high |
| TC-004 |  | Sort products by Name (A–Z) | User logged in as <Role> | 1. Select 'Name (A–Z)' from the Sort_By dropdown | Products are sorted in ascending order by name. | medium |
| TC-005 |  | Sort products by Name (Z–A) | User logged in as <Role> | 1. Select 'Name (Z–A)' from the Sort_By dropdown | Products are sorted in descending order by name. | medium |
| TC-006 |  | Sort products by Price (low–high) | User logged in as <Role> | 1. Select 'Price (low–high)' from the Sort_By dropdown | Products are sorted in ascending order by price. | medium |
| TC-007 |  | Sort products by Price (high–low) | User logged in as <Role> | 1. Select 'Price (high–low)' from the Sort_By dropdown | Products are sorted in descending order by price. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to add an item to cart when it is already in the cart | Item is already in the cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Add to cart' button for an item already in the cart | Status remains 'In Cart'; no item is added again; 'Add to cart' button is not visible | high |
| TC-009 |  | Attempt to remove an item from cart when it is not in the cart | Item is not in the cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Remove' button for an item not in the cart | Status remains 'Not In Cart'; no item is removed; 'Remove' button is not visible | high |
| TC-010 |  | Attempt to view product detail without selecting a product | No product is selected | 1. Navigate to the Product Inventory page<br>2. Click on the 'View Product Detail' action without selecting a product | No Product Detail page opens; error message indicates a product must be selected | medium |
| TC-011 | WF-002 | Attempt to add to cart when the item is already in the cart | Item is already in the cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Add to cart' button for an item already in the cart | Form does not submit; item is not added again; error shown on 'Add to cart' button | high |
| TC-012 | WF-003 | Attempt to remove from cart when the item is not in the cart | Item is not in the cart | 1. Navigate to the Product Inventory page<br>2. Click on the 'Remove' button for an item not in the cart | Form does not submit; item is not removed; error shown on 'Remove' button | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (state_edge) | WF-002 | Rapidly add and remove item from cart | Item is not in cart | 1. Click 'Add to cart'<br>2. Immediately click 'Remove' | 'Remove' action succeeds; item is removed from cart and 'Add to cart' button is displayed again. | medium |
| TC-014 (state_edge) | WF-003 | Rapidly remove item from cart | Item is in cart | 1. Click 'Remove'<br>2. Immediately click 'Remove' again | Second 'Remove' action is blocked; item remains in cart and 'Remove' button is still displayed. | medium |
| TC-015 (input_edge) |  | Sort dropdown with special characters |  | 1. Open the sort dropdown<br>2. Select 'Name (A–Z)' | Products are sorted alphabetically from A to Z. | low |
| TC-016 (input_edge) |  | Sort dropdown with long text |  | 1. Open the sort dropdown<br>2. Select 'Price (low–high)' | Products are sorted by price from low to high. | low |

---

## Product Detail

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Role>, Product is currently not in cart | 1. Click 'Add to cart' button | Product added to cart; success message shown | high |
| TC-002 | WF-002 | Remove product from cart | User logged in as <Role>, Product is currently in cart | 1. Click 'Remove' button | Product removed from cart; success message shown | high |
| TC-003 | WF-003 | Navigate back to products | User logged in as <Role> | 1. Click 'Back to products' button | Returned to Product Inventory page | medium |
| TC-004 | WF-004 | Go to shopping cart | User logged in as <Role> | 1. Click 'Go to Shopping Cart' button | Navigated to Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to remove product when not in cart | Product is not in cart | 1. Ensure product is not in cart<br>2. Click on Remove button | Action is blocked; no product is removed from cart; Remove button is not available | high |
| TC-006 |  | Attempt to add product to cart when already in cart | Product is in cart | 1. Ensure product is in cart<br>2. Click on Add to cart button | Action is blocked; no product is added to cart; Add to cart button is not available | high |
| TC-007 |  | Attempt to navigate back to products while on Product Detail page |  | 1. Click on Back to products button | Navigates back to Product Inventory page | medium |
| TC-008 |  | Attempt to go to shopping cart from Product Detail page |  | 1. Click on Go to Shopping Cart button | Navigates to Shopping Cart page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (state_edge) | WF-001 | Rapid consecutive state transitions from Not_In_Cart to In_Cart | Product is currently Not_In_Cart | 1. Click 'Add to cart'<br>2. Immediately click 'Remove' | Product removed from cart; success message shown | medium |
| TC-010 (state_edge) | WF-002 | Rapid consecutive state transitions from In_Cart to Not_In_Cart | Product is currently In_Cart | 1. Click 'Remove'<br>2. Immediately click 'Add to cart' | Product added to cart; success message shown | medium |
| TC-011 (interaction_edge) | WF-003 | Navigate back to products after adding to cart | Product has been added to cart | 1. Click 'Back to products' | Returned to Product Inventory page | medium |
| TC-012 (interaction_edge) | WF-004 | Navigate to shopping cart from product detail | Product has been added to cart | 1. Click 'Go to Shopping Cart' | Navigated to Shopping Cart page | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue Shopping from Shopping Cart | User logged in as <Role>, Shopping Cart contains items | 1. Click 'Continue Shopping' | returns to Product Inventory | high |
| TC-002 | WF-002 | Checkout from Shopping Cart | User logged in as <Role>, Shopping Cart contains items | 1. Click 'Checkout' | begins checkout process | high |
| TC-003 | WF-003 | Remove item from Shopping Cart | User logged in as <Role>, Shopping Cart contains items | 1. Click 'Remove' on an item in the cart | Item removed from cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to continue shopping without any items in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Continue Shopping' | User remains on the Shopping Cart page; no items are available to continue shopping | high |
| TC-005 | WF-002 | Attempt to checkout with no items in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Checkout' | User remains on the Shopping Cart page; cannot proceed to checkout with no items | high |
| TC-006 | WF-003 | Attempt to remove an item that is not in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Remove' on a non-existent item | No action occurs; item not found in cart | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapid navigation after clicking Continue Shopping | User is on the Shopping Cart page | 1. Click Continue Shopping<br>2. Immediately press the back button | User is redirected to the Product Inventory without pre-filled cart items | medium |
| TC-008 (interaction_edge) | WF-002 | Rapid navigation after clicking Checkout | User is on the Shopping Cart page | 1. Click Checkout<br>2. Immediately press the back button | User is redirected to the checkout process without pre-filled cart items | medium |
| TC-009 (interaction_edge) | WF-003 | Remove all items from cart | User has multiple items in the cart | 1. Click Remove on the first item<br>2. Click Remove on the second item<br>3. Click Remove on the third item | Form submits successfully; no items remain in the cart | medium |

---

## Checkout - Information

Total: **12** (positive: 2, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid checkout information | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel checkout process | User logged in as <Role> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill Last_Name and Zip_Postal_Code with valid values<br>3. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill First_Name and Zip_Postal_Code with valid values<br>3. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Zip/Postal Code field blank and submit |  | 1. Leave the Zip_Postal_Code field blank<br>2. Fill First_Name and Last_Name with valid values<br>3. Click Continue | Inline validation error appears on the Zip_Postal_Code field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the First_Name, Last_Name, and Zip_Postal_Code fields blank<br>2. Click Continue | Inline validation error appears on the First_Name, Last_Name, and Zip_Postal_Code fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Enter leading and trailing whitespace in First Name |  | 1. Enter '   John   ' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | Leading/trailing whitespace is trimmed; saved value shown in the overview step is 'John'. | low |
| TC-008 (input_edge) |  | Enter special characters in Last Name |  | 1. Enter 'John' in the First Name field<br>2. Enter '@Doe!' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | Form submits successfully; entity is created with Last Name as '@Doe!'. | low |
| TC-009 (input_edge) |  | Enter a very long string in Zip/Postal Code |  | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345678901234567890' in the Zip/Postal Code field<br>4. Click Continue | Form submits successfully; entity is created with Zip/Postal Code as '12345678901234567890'. | low |
| TC-010 (boundary) | WF-001 | Submit with empty First Name |  | 1. Leave First Name field empty<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | Error: First Name is required. | medium |
| TC-011 (boundary) | WF-001 | Submit with empty Last Name |  | 1. Enter 'John' in the First Name field<br>2. Leave Last Name field empty<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | Error: Last Name is required. | medium |
| TC-012 (boundary) | WF-001 | Submit with empty Zip/Postal Code |  | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Leave Zip/Postal Code field empty<br>4. Click Continue | Error: Postal Code is required. | medium |

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
| TC-003 | WF-001 | Attempt to finish the order without any payment information |  | 1. Leave the Payment Information section blank<br>2. Click Finish | Form does not submit; error shown on Payment Information field indicating it is required | high |
| TC-004 | WF-002 | Attempt to cancel the checkout without any prior action |  | 1. Click Cancel | User is exited from checkout; no changes made to the order | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid consecutive submission of the Finish button | User is on the overview step of the checkout process | 1. Click the Finish button to complete the order<br>2. Immediately click the Finish button again | The first submission completes the order; the second submission is blocked with a visible message indicating the order is already being processed. | medium |
| TC-006 (interaction_edge) | WF-002 | Rapid consecutive submission of the Cancel button | User is on the overview step of the checkout process | 1. Click the Cancel button to exit checkout<br>2. Immediately click the Cancel button again | The first click exits the checkout; the second click is ignored with no additional action taken. | medium |

---

## Checkout - Confirmation

Total: **4** (positive: 2, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Display success message and return to product inventory | User logged in as <Role> | 1. Navigate to the Confirmation page | The page displays 'Thank you for your order!' | high |
| TC-002 | WF-001 | Return to Product Inventory and clear the cart | User logged in as <Role>, User is on the Confirmation page | 1. Click the 'Back Home' button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to click 'Back Home' without a successful order |  | 1. Navigate to the Checkout - Confirmation page<br>2. Click the 'Back Home' button | The action is blocked; the user remains on the Confirmation page and the cart is not cleared. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully completed the checkout process | 1. Click the 'Back Home' button | User is redirected to Product Inventory; the cart is cleared and no duplicate order is created. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click on the Logout button | ends the session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to logout while not logged in | user must be logged in is NOT met | 1. Ensure the user is not logged in<br>2. Click the Logout button | Logout action is not performed; user remains on the current page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | First logout action succeeds and redirects to the login page; second logout action is ignored as the session has ended. | medium |
| TC-004 (input_edge) |  | Logout while not logged in | User is not logged in | 1. Attempt to click the Logout button | Logout button is disabled or not displayed, preventing logout action. | low |

---

## Reset App State

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State functionality | User logged in as <Role> | 1. Click Reset App State Button | clears the cart and resets in-app state | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to reset app state without any preconditions |  | 1. Click the Reset App State button | The app state does not reset; no changes occur to the cart or in-app state | high |

---
