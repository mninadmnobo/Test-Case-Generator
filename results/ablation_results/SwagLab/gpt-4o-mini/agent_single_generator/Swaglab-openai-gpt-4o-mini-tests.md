# Test Cases — Swaglab

Generated: 2026-06-09T09:01:25.024101Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 64 | 23 | 25 | 16 | 33 | 25 | 6 |

## Login

Total: **8** (positive: 1, negative: 5, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User is on the login page, User has valid credentials | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click on the Login button | User is authenticated and redirected to the Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Login with locked out user | User is on the login page | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click on the Login button | Epic sadface: Sorry, this user has been locked out. | high |
| TC-003 | WF-003 | Login with empty Username field | User is on the login page | 1. Leave the Username field empty<br>2. Enter 'secret_sauce' in the Password field<br>3. Click on the Login button | Epic sadface: Username is required. | high |
| TC-004 | WF-004 | Login with empty Password field | User is on the login page | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field empty<br>3. Click on the Login button | Epic sadface: Password is required. | high |
| TC-005 | WF-005 | Login with invalid credentials | User is on the login page | 1. Enter 'invalid_user' in the Username field<br>2. Enter 'invalid_password' in the Password field<br>3. Click on the Login button | Epic sadface: Username and password do not match any user in this service. | high |
| TC-006 | WF-003 | Login with empty fields | User is on the login page | 1. Leave both Username and Password fields empty<br>2. Click on the Login button | Epic sadface: Username is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Login with maximum length username | User is on the login page | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click on the Login button | User is authenticated and redirected to the Product Inventory page | medium |
| TC-008 | WF-001 | Login with minimum length username | User is on the login page | 1. Enter 's' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click on the Login button | Epic sadface: Username and password do not match any user in this service. | medium |

---

## Product Inventory

Total: **10** (positive: 5, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View product detail by clicking product name | User logged in as Customer, Product list is displayed | 1. Click on a product name or image<br>2. Observe the resulting page | Product Detail page opens displaying product information | high |
| TC-002 | WF-002 | Add product to cart | User logged in as Customer, Product list is displayed | 1. Click on 'Add to cart' button for a product<br>2. Observe the button change to 'Remove' | Item is added to cart and button changes to 'Remove' | high |
| TC-003 | WF-003 | Remove product from cart | User logged in as Customer, Product has been added to cart | 1. Click on 'Remove' button for the product<br>2. Observe the button change back to 'Add to cart' | Item is removed from cart and button changes back to 'Add to cart' | high |
| TC-009 | WF-001 | Sort products by price low to high | User logged in as Customer, Product list is displayed | 1. Select 'Price (low–high)' from sort dropdown<br>2. Observe the product list order | Products are displayed in ascending order of price | medium |
| TC-010 | WF-001 | Sort products by name Z to A | User logged in as Customer, Product list is displayed | 1. Select 'Name (Z–A)' from sort dropdown<br>2. Observe the product list order | Products are displayed in descending order by name | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to view product detail without clicking | User logged in as Customer, Product list is displayed | 1. Do not click on any product name or image | Product Detail page does not open | medium |
| TC-005 | WF-002 | Add product to cart when already in cart | User logged in as Customer, Product has been added to cart | 1. Click on 'Add to cart' button for the product again | Button remains 'Remove' and item count in cart does not increase | medium |
| TC-006 | WF-003 | Remove product from cart when not in cart | User logged in as Customer, Product is not in cart | 1. Click on 'Remove' button for the product | Button remains 'Add to cart' and no action is performed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-002 | Add product with zero price to cart | User logged in as Customer, Product list is displayed with a product priced at $0 | 1. Click on 'Add to cart' button for the product priced at $0 | Item is added to cart and button changes to 'Remove' | low |
| TC-008 | WF-002 | Add product with maximum price to cart | User logged in as Customer, Product list is displayed with a product priced at maximum allowable value | 1. Click on 'Add to cart' button for the product priced at maximum value | Item is added to cart and button changes to 'Remove' | low |

---

## Product Detail

Total: **8** (positive: 4, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart successfully | User logged in as Customer, Product is not in cart | 1. Navigate to Product Detail page<br>2. Click on 'Add to cart' button | Product added to cart confirmation message is displayed | high |
| TC-002 | WF-002 | Remove product from cart successfully | User logged in as Customer, Product is in cart | 1. Navigate to Product Detail page<br>2. Click on 'Remove' button | Product removed from cart confirmation message is displayed | high |
| TC-003 | WF-003 | Navigate back to products | User logged in as Customer | 1. Navigate to Product Detail page<br>2. Click on 'Back to products' button | Returned to Product Inventory page | medium |
| TC-004 | WF-004 | Go to Shopping Cart | User logged in as Customer | 1. Navigate to Product Detail page<br>2. Click on 'Go to Shopping Cart' button | Navigated to Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to add product to cart when already in cart | User logged in as Customer, Product is in cart | 1. Navigate to Product Detail page<br>2. Click on 'Add to cart' button | Add to cart button is disabled or error message is displayed | high |
| TC-006 | WF-002 | Attempt to remove product from cart when not in cart | User logged in as Customer, Product is not in cart | 1. Navigate to Product Detail page<br>2. Click on 'Remove' button | Remove button is disabled or error message is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-003 | Check back button functionality | User logged in as Customer | 1. Navigate to Product Detail page<br>2. Click on 'Back to products' button | Returned to Product Inventory page without any errors | medium |
| TC-008 | WF-004 | Check shopping cart navigation | User logged in as Customer | 1. Navigate to Product Detail page<br>2. Click on 'Go to Shopping Cart' button | Navigated to Shopping Cart page without any errors | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User clicks Continue Shopping | User logged in as Customer, Shopping Cart has items | 1. Click on 'Continue Shopping' button | User is redirected to Product Inventory page | high |
| TC-002 | WF-002 | User clicks Checkout | User logged in as Customer, Shopping Cart has items | 1. Click on 'Checkout' button | User begins the checkout process | high |
| TC-003 | WF-003 | User removes an item from the cart | User logged in as Customer, Shopping Cart has items | 1. Click on 'Remove' button for an item | The item is removed from the cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | User clicks Continue Shopping with empty cart | User logged in as Customer, Shopping Cart is empty | 1. Click on 'Continue Shopping' button | User remains on Shopping Cart page with a message indicating the cart is empty | medium |
| TC-005 | WF-002 | User clicks Checkout with empty cart | User logged in as Customer, Shopping Cart is empty | 1. Click on 'Checkout' button | User is shown a message indicating that the cart is empty and cannot proceed to checkout | high |
| TC-006 | WF-003 | User attempts to remove an item that is not in the cart | User logged in as Customer, Shopping Cart has items | 1. Click on 'Remove' button for an item that is not in the cart | No action is taken, and a message indicates the item is not found in the cart | low |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | User clicks Continue Shopping multiple times | User logged in as Customer, Shopping Cart has items | 1. Click on 'Continue Shopping' button<br>2. Click on 'Continue Shopping' button again | User is redirected to Product Inventory page each time without errors | medium |
| TC-008 | WF-002 | User clicks Checkout multiple times | User logged in as Customer, Shopping Cart has items | 1. Click on 'Checkout' button<br>2. Click on 'Checkout' button again | User begins the checkout process each time without errors | medium |
| TC-009 | WF-003 | User removes all items from the cart | User logged in as Customer, Shopping Cart has multiple items | 1. Click on 'Remove' button for each item in the cart | All items are removed from the cart, and the cart is empty | high |

---

## Checkout - Information

Total: **8** (positive: 2, negative: 5, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit form with valid data | User logged in as Customer, On the Checkout Information page | 1. Enter 'John' in First Name field<br>2. Enter 'Doe' in Last Name field<br>3. Enter '12345' in Zip/Postal Code field<br>4. Click on 'Continue' button | User is redirected to the overview step | high |
| TC-005 | WF-002 | Cancel Checkout Form | User logged in as Customer, On the Checkout Information page | 1. Click on 'Cancel' button | User is returned to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit form with missing First Name | User logged in as Customer, On the Checkout Information page | 1. Leave First Name field empty<br>2. Enter 'Doe' in Last Name field<br>3. Enter '12345' in Zip/Postal Code field<br>4. Click on 'Continue' button | Error banner displays 'Error: First Name is required' | high |
| TC-003 | WF-001 | Submit form with missing Last Name | User logged in as Customer, On the Checkout Information page | 1. Enter 'John' in First Name field<br>2. Leave Last Name field empty<br>3. Enter '12345' in Zip/Postal Code field<br>4. Click on 'Continue' button | Error banner displays 'Error: Last Name is required' | high |
| TC-004 | WF-001 | Submit form with missing Zip/Postal Code | User logged in as Customer, On the Checkout Information page | 1. Enter 'John' in First Name field<br>2. Enter 'Doe' in Last Name field<br>3. Leave Zip/Postal Code field empty<br>4. Click on 'Continue' button | Error banner displays 'Error: Postal Code is required' | high |
| TC-006 | WF-001 | Submit form with empty fields | User logged in as Customer, On the Checkout Information page | 1. Leave all fields empty<br>2. Click on 'Continue' button | Error banner displays 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required' | high |
| TC-008 | WF-001 | Submit form with invalid Zip/Postal Code | User logged in as Customer, On the Checkout Information page | 1. Enter 'John' in First Name field<br>2. Enter 'Doe' in Last Name field<br>3. Enter 'abcde' in Zip/Postal Code field<br>4. Click on 'Continue' button | Error banner displays validation error for Zip/Postal Code | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Submit form with maximum length names | User logged in as Customer, On the Checkout Information page | 1. Enter 'A very long first name that exceeds typical length' in First Name field<br>2. Enter 'A very long last name that exceeds typical length' in Last Name field<br>3. Enter '12345' in Zip/Postal Code field<br>4. Click on 'Continue' button | Error banner displays validation error for First Name and Last Name | medium |

---

## Checkout - Overview

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete the order successfully | User logged in as Customer, Items are present in the cart | 1. Navigate to the Checkout Overview step<br>2. Click on the 'Finish' button | User is navigated to the confirmation page with order completion message | high |
| TC-002 | WF-002 | Cancel the checkout process | User logged in as Customer, Items are present in the cart | 1. Navigate to the Checkout Overview step<br>2. Click on the 'Cancel' button | User is exited from the checkout process and returned to the previous page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to finish order with empty cart | User logged in as Customer, Cart is empty | 1. Navigate to the Checkout Overview step<br>2. Click on the 'Finish' button | Error message displayed indicating that the cart is empty and cannot complete the order | high |
| TC-004 | WF-002 | Attempt to cancel checkout without items | User logged in as Customer, Cart is empty | 1. Navigate to the Checkout Overview step<br>2. Click on the 'Cancel' button | User is still exited from the checkout process and returned to the previous page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Check maximum items in order summary | User logged in as Customer, Cart has maximum allowed items | 1. Navigate to the Checkout Overview step | Order summary displays all items correctly without truncation | low |
| TC-006 | WF-001 | Check total calculation with maximum values | User logged in as Customer, Cart contains items with maximum price | 1. Navigate to the Checkout Overview step | Totals section displays correct calculations for item total, tax, and total amount | low |

---

## Checkout - Confirmation

Total: **6** (positive: 3, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Display success message after order confirmation | User logged in as Customer, User has completed an order | 1. Navigate to the confirmation page<br>2. Observe the success message | Success message 'Thank you for your order!' is displayed | high |
| TC-002 | WF-001 | Back Home button functionality | User logged in as Customer, User is on the confirmation page | 1. Click on the 'Back Home' button | User is redirected to Product Inventory and the cart is cleared | high |
| TC-003 | WF-001 | Back Home button is visible on confirmation page | User logged in as Customer, User has completed an order | 1. Navigate to the confirmation page | 'Back Home' button is visible and clickable | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Back Home button disabled when no order is completed | User logged in as Customer, User has not completed any order | 1. Navigate to the confirmation page | 'Back Home' button is disabled or not present | high |
| TC-005 | WF-001 | Success message is not displayed if order is not completed | User logged in as Customer, User has not completed any order | 1. Navigate to the confirmation page | Success message is not displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Boundary test for success message length | User logged in as Customer, User has completed an order | 1. Navigate to the confirmation page | Success message does not exceed character limit and is fully displayed | medium |

---

## Logout

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful logout redirects to login page | User logged in as regular user | 1. Click on the Logout button | User is redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Logout button is disabled when user is not logged in | User not logged in | 1. Attempt to click on the Logout button | Logout button is disabled and no action is taken | medium |
| TC-003 | WF-001 | Access protected pages after logout | User logged in as regular user, User has logged out | 1. Attempt to access the inventory page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Logout action while session is active | User logged in as regular user | 1. Click on the Logout button multiple times in quick succession | User is redirected to the login page only once | medium |

---

## Reset App State

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset app state successfully | User logged in as Customer, Cart has items | 1. Click on the Reset Action button | The cart is cleared and in-app state is reset (cart badge and add/remove button states reflect the reset) | high |
| TC-002 | WF-001 | Reset app state with empty cart | User logged in as Customer, Cart is empty | 1. Click on the Reset Action button | The cart remains empty and in-app state is reset (cart badge and add/remove button states reflect the reset) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to reset app state without being logged in | User not logged in | 1. Click on the Reset Action button | The action is blocked and an error message is displayed indicating the user must log in first | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Reset app state with a large number of items | User logged in as Customer, Cart has 1000 items | 1. Click on the Reset Action button | The cart is cleared and in-app state is reset without performance issues | medium |
| TC-005 | WF-001 | Reset app state when already reset | User logged in as Customer, Cart is already empty | 1. Click on the Reset Action button | The cart remains empty and in-app state is reset (no change in state) | low |

---
