# Swag Labs Test Cases

**Website URL:** <https://www.saucedemo.com/>

---

## Table of Contents

1. [Login](#1-login)
2. [Product Inventory](#2-product-inventory)
3. [Product Detail](#3-product-detail)
4. [Shopping Cart](#4-shopping-cart)
5. [Checkout - Information](#5-checkout---information)
6. [Checkout - Overview](#6-checkout---overview)
7. [Checkout - Confirmation](#7-checkout---confirmation)
8. [Navigation Menu](#8-navigation-menu)
9. [Logout](#9-logout)
10. [Reset App State](#10-reset-app-state)

---

## Test Credentials

| Username | Description |
|----------|-------------|
| standard_user | Standard user for normal testing |
| locked_out_user | User that is locked out |
| problem_user | User with UI/functionality problems |
| performance_glitch_user | User with delayed responses |
| error_user | User that triggers errors |
| visual_user | User with visual glitches |

**Password for all users:** secret_sauce

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-001 | Valid login with standard_user | None | 1. Navigate to login page<br>2. Enter "standard_user" as username<br>3. Enter "secret_sauce" as password<br>4. Click "Login" | User redirected to product inventory page | High |
| SL-LOGIN-002 | Login page elements displayed | None | 1. Navigate to login page | Username field, Password field, Login button, and accepted usernames/password info visible | Medium |
| SL-LOGIN-003 | Login with each valid user type | None | 1. Login with standard_user<br>2. Logout<br>3. Repeat for each user type | All valid users can log in (except locked_out_user) | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-004 | Invalid username | None | 1. Enter invalid username<br>2. Enter valid password<br>3. Click "Login" | Error message: "Epic sadface: Username and password do not match" | High |
| SL-LOGIN-005 | Invalid password | None | 1. Enter valid username<br>2. Enter incorrect password<br>3. Click "Login" | Error message displayed, user remains on login page | High |
| SL-LOGIN-006 | Empty username | None | 1. Leave username empty<br>2. Enter password<br>3. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-007 | Empty password | None | 1. Enter username<br>2. Leave password empty<br>3. Click "Login" | Error message: "Epic sadface: Password is required" | High |
| SL-LOGIN-008 | Both fields empty | None | 1. Leave both fields empty<br>2. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-009 | Locked out user | None | 1. Enter "locked_out_user"<br>2. Enter "secret_sauce"<br>3. Click "Login" | Error message: "Epic sadface: Sorry, this user has been locked out" | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-010 | Username with leading/trailing spaces | None | 1. Enter " standard_user " (with spaces)<br>2. Enter valid password<br>3. Click "Login" | Login fails or spaces trimmed and login succeeds | Medium |
| SL-LOGIN-011 | Case sensitivity | None | 1. Enter "Standard_User" (different case)<br>2. Enter valid password<br>3. Click "Login" | Login fails (username is case-sensitive) | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-012 | Password field masking | None | 1. Enter text in password field | Password characters are masked | High |
| SL-LOGIN-013 | Error message dismissible | SL-LOGIN-004 completed | 1. Click X button on error message | Error message disappears | Medium |
| SL-LOGIN-014 | Tab navigation | None | 1. Use Tab key to navigate | Focus moves: username → password → Login button | Medium |
| SL-LOGIN-015 | Enter key submission | None | 1. Fill credentials<br>2. Press Enter | Form submits | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-016 | Direct navigation to login page while authenticated | User already logged in | 1. Enter the login page URL manually | User is redirected to Home page or active session is preserved | Medium |
| SL-LOGIN-017 | Session persists on page refresh after successful login | User logged in | 1. Login successfully<br>2. Refresh browser tab | User remains authenticated and current page reloads successfully | High |

---

## 2. Product Inventory

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-001 | Products displayed | User logged in | 1. View inventory page | All products displayed with name, description, price, and "Add to cart" button | High |
| SL-INV-002 | Add product to cart | User logged in | 1. Click "Add to cart" on any product | Button changes to "Remove", cart badge shows "1" | High |
| SL-INV-003 | Add multiple products | User logged in | 1. Add product 1 to cart<br>2. Add product 2 to cart<br>3. Add product 3 to cart | Cart badge shows "3" | High |
| SL-INV-004 | Remove product from cart | Product in cart | 1. Click "Remove" button | Button changes to "Add to cart", cart badge decrements | High |
| SL-INV-005 | Sort A-Z (default) | User logged in | 1. Check default sort order | Products sorted alphabetically A-Z | High |
| SL-INV-006 | Sort Z-A | User logged in | 1. Select "Name (Z to A)" from dropdown | Products sorted alphabetically Z-A | High |
| SL-INV-007 | Sort Price low to high | User logged in | 1. Select "Price (low to high)" | Products sorted by price ascending | High |
| SL-INV-008 | Sort Price high to low | User logged in | 1. Select "Price (high to low)" | Products sorted by price descending | High |
| SL-INV-009 | Navigate to product detail | User logged in | 1. Click on product name or image | Navigates to product detail page | High |
| SL-INV-010 | Cart icon navigation | User logged in | 1. Click cart icon | Navigates to shopping cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-011 | Access inventory without login | Not logged in | 1. Navigate directly to inventory URL | Redirected to login or access denied | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-012 | Product images displayed | User logged in | 1. View inventory | All products have images | Medium |
| SL-INV-013 | Price formatting | User logged in | 1. View product prices | Prices formatted as $XX.XX | Medium |
| SL-INV-014 | Cart badge visibility | User logged in, cart empty | 1. View cart icon | No badge shown when cart is empty | Medium |
| SL-INV-015 | Cart badge updates real-time | User logged in | 1. Add item<br>2. Observe badge | Badge updates immediately | High |
| SL-INV-016 | Sort dropdown options | User logged in | 1. Click sort dropdown | Shows 4 options: A-Z, Z-A, Price low-high, Price high-low | Medium |
| SL-INV-017 | Hamburger menu visible | User logged in | 1. View top-left corner | Hamburger menu icon visible | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-018 | Refresh preserves sort order | Inventory sorted | 1. Sort inventory Z-A<br>2. Refresh page<br>3. Check sort order | Sort order preserved as Z-A | High |
| SL-INV-019 | problem_user missing add-to-cart buttons | Logged in as problem_user | 1. View inventory | Some products may not have "Add to cart" buttons | High |
| SL-INV-020 | performance_glitch_user delayed cart badge | Logged in as performance_glitch_user | 1. Add item to cart<br>2. Observe badge update delay | Cart badge updates with slight delay | Medium |

---

## 3. Product Detail

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-001 | Product details displayed | User logged in | 1. Click on a product | Product name, description, price, and image displayed | High |
| SL-PD-002 | Add to cart from detail page | User logged in, on product detail | 1. Click "Add to cart" | Product added, button changes to "Remove", cart badge updates | High |
| SL-PD-003 | Remove from cart on detail page | Product in cart, on detail page | 1. Click "Remove" | Product removed, button changes to "Add to cart" | High |
| SL-PD-004 | Back to products | On product detail page | 1. Click "Back to products" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-005 | Large product image | On product detail | 1. View product image | Larger image than inventory thumbnail | Medium |
| SL-PD-006 | Price matches inventory | On product detail | 1. Compare price with inventory listing | Price is identical | High |
| SL-PD-007 | Cart state preserved | Product added from inventory | 1. Navigate to product detail | "Remove" button shown (not "Add to cart") | High |

---

## 4. Shopping Cart

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-001 | View cart with items | Items added to cart | 1. Click cart icon | All added items displayed with name, description, price, quantity | High |
| SL-CART-002 | Remove item from cart | Items in cart | 1. Click "Remove" on an item | Item removed from cart, list updates | High |
| SL-CART-003 | Continue shopping | On cart page | 1. Click "Continue Shopping" | Returns to inventory page | High |
| SL-CART-004 | Proceed to checkout | Items in cart | 1. Click "Checkout" | Navigates to checkout information page | High |
| SL-CART-005 | Cart persists across pages | Items added | 1. Navigate to different pages<br>2. Return to cart | Items still in cart | High |
| SL-CART-006 | Quantity display | Items in cart | 1. View cart | Quantity shown as "1" for each item | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-007 | Empty cart | No items added | 1. Navigate to cart | Empty cart state or message displayed | Medium |
| SL-CART-008 | Checkout with empty cart | No items in cart | 1. Navigate to cart<br>2. Try to checkout | Prevented or appropriate error | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-009 | Cart item layout | Items in cart | 1. View cart | Each item shows quantity, name, description, price | Medium |
| SL-CART-010 | Remove button for each item | Multiple items in cart | 1. View cart | Each item has its own "Remove" button | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-011 | Cart persists across pages | Items added | 1. Navigate to different pages<br>2. Return to cart | Items still in cart | High |
| SL-CART-012 | Multi-tab cart sync | Cart open in tab 1 | 1. Add item in tab 1<br>2. Switch to tab 2 cart<br>3. Refresh tab 2 | Cart in tab 2 shows new item | Medium |
| SL-CART-013 | No duplicate items in cart | Standard user, item added | 1. Add item from inventory<br>2. Navigate to product detail<br>3. Try to add same item again | Item not duplicated, quantity remains 1 | High |

---

## 5. Checkout - Information

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-001 | Complete checkout info | Items in cart, on checkout page | 1. Enter First Name<br>2. Enter Last Name<br>3. Enter Postal Code<br>4. Click "Continue" | Navigates to checkout overview | High |
| SL-CHK1-002 | Cancel checkout | On checkout info page | 1. Click "Cancel" | Returns to cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-003 | First Name empty | On checkout info | 1. Leave First Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: First Name is required" | High |
| SL-CHK1-004 | Last Name empty | On checkout info | 1. Leave Last Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Last Name is required" | High |
| SL-CHK1-005 | Postal Code empty | On checkout info | 1. Leave Postal Code empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Postal Code is required" | High |
| SL-CHK1-006 | All fields empty | On checkout info | 1. Leave all fields empty<br>2. Click "Continue" | Error message for first required field | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-007 | Single character inputs | On checkout info | 1. Enter single character in each field<br>2. Click "Continue" | Form accepts or rejects appropriately | Low |
| SL-CHK1-008 | Very long inputs | On checkout info | 1. Enter very long strings<br>2. Click "Continue" | System handles gracefully (truncates or accepts) | Low |
| SL-CHK1-009 | Special characters | On checkout info | 1. Enter special characters in fields<br>2. Click "Continue" | System handles appropriately | Low |
| SL-CHK1-010 | Numeric First/Last Name | On checkout info | 1. Enter numbers in name fields<br>2. Click "Continue" | May accept (no strict validation) | Low |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-011 | Form elements displayed | On checkout info | 1. View page | First Name, Last Name, Postal Code fields, Continue and Cancel buttons visible | Medium |
| SL-CHK1-012 | Error message style | Error triggered | 1. Submit with empty field | Error displayed with red styling and X icon | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-013 | Partial form submission | On checkout info | 1. Enter only First Name<br>2. Leave others empty<br>3. Click Continue | Partial submission prevented, errors for missing fields | High |
| SL-CHK1-014 | Special characters in name | On checkout info | 1. Enter "John@123" in First Name<br>2. Click Continue | May accept or reject depending on validation | Low |
| SL-CHK1-015 | Browser back during checkout | Checkout info page | 1. Fill checkout form<br>2. Click browser back<br>3. Go forward | State may or may not be preserved | Low |

---

## 6. Checkout - Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-001 | Order summary displayed | Completed checkout info | 1. View checkout overview | All cart items listed with prices | High |
| SL-CHK2-002 | Item total correct | Items in cart | 1. View Item total | Sum of all item prices | High |
| SL-CHK2-003 | Tax calculated | On overview page | 1. View Tax amount | Tax calculated (typically 8%) | High |
| SL-CHK2-004 | Total correct | On overview page | 1. View Total | Total = Item Total + Tax | High |
| SL-CHK2-005 | Finish purchase | On overview page | 1. Click "Finish" | Order placed, confirmation page shown | High |
| SL-CHK2-006 | Cancel from overview | On overview page | 1. Click "Cancel" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-007 | Payment info displayed | On overview page | 1. View payment section | Shows "SauceCard #31337" | Medium |
| SL-CHK2-008 | Shipping info displayed | On overview page | 1. View shipping section | Shows shipping method (Free Pony Express) | Medium |
| SL-CHK2-009 | Price breakdown clear | On overview page | 1. View totals section | Item total, Tax, and Total clearly labeled | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-010 | Tax calculation accuracy | On overview page with known total | 1. View Tax amount | Tax is calculated consistently from the item total | High |
| SL-CHK2-011 | Total calculation accuracy | On overview page with known total | 1. View Total | Total equals item total plus tax | High |
| SL-CHK2-012 | Duplicate finish action handled gracefully | On overview page | 1. Click Finish twice quickly | Only one order is placed and the UI remains stable | Medium |

---

## 7. Checkout - Confirmation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-001 | Confirmation displayed | Order completed | 1. Complete checkout | "Thank you for your order!" message displayed | High |
| SL-CHK3-002 | Cart cleared | Order completed | 1. View cart after order | Cart is empty, no badge | High |
| SL-CHK3-003 | Back to products | On confirmation page | 1. Click "Back Home" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-004 | Success image displayed | Order completed | 1. View confirmation page | Pony Express image or checkmark visible | Medium |
| SL-CHK3-005 | Order dispatch message | Order completed | 1. View confirmation page | "Your order has been dispatched" or similar message | Medium |

---

## 8. Navigation Menu

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-NAV-001 | Open hamburger menu | User logged in | 1. Click hamburger icon (☰) | Side menu opens with options | High |
| SL-NAV-002 | All Items navigation | Menu open | 1. Click "All Items" | Navigates to inventory page | High |
| SL-NAV-003 | About navigation | Menu open | 1. Click "About" | Navigates to Sauce Labs website | Medium |
| SL-NAV-004 | Close menu | Menu open | 1. Click X or outside menu | Menu closes | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-NAV-005 | Menu items visible | Menu open | 1. View menu | All Items, About, Logout, Reset App State visible | Medium |
| SL-NAV-006 | Menu animation | Open/close menu | 1. Open and close menu | Smooth slide animation | Low |

---

## 9. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGOUT-001 | Successful logout | User logged in | 1. Open hamburger menu<br>2. Click "Logout" | User redirected to login page | High |
| SL-LOGOUT-002 | Session cleared | Logged out | 1. Try to access inventory directly | Redirected to login | High |
| SL-LOGOUT-003 | Cart cleared on logout | Items in cart, logged out | 1. Log back in<br>2. Check cart | Cart is empty (session reset) | High |
| SL-LOGOUT-004 | Back button after logout | Logged out | 1. Click browser back button | Cannot access protected pages | High |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGOUT-005 | Logout clears user-specific UI state | User logged in and navigation state exists | 1. Logout<br>2. Login as different user | New user does not inherit previous user's UI state in unauthorized ways | Medium |
| SL-LOGOUT-006 | Logout from any module behaves consistently | User logged in on non-home route | 1. Logout from multiple pages/modules | Logout always invalidates session and returns to login page | Medium |

---

## 10. Reset App State

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-RESET-001 | Reset clears cart | Items in cart | 1. Open hamburger menu<br>2. Click "Reset App State" | Cart cleared, badge removed | High |
| SL-RESET-002 | Reset button states | Items added (buttons show "Remove") | 1. Click "Reset App State" | All "Remove" buttons revert to "Add to cart" | High |
| SL-RESET-003 | Reset preserves login | User logged in with items | 1. Click "Reset App State" | User remains logged in | Medium |

### Additional Coverage Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-RESET-004 | Reset clears cart items | Items in cart | 1. Add multiple items<br>2. Click Reset App State | Cart completely empty | High |
| SL-RESET-005 | Reset reverts buttons | Items in cart (Remove buttons visible) | 1. Click Reset App State<br>2. Go to inventory | All buttons revert to "Add to cart" | High |
| SL-RESET-006 | Reset preserves login state | User logged in | 1. Click Reset App State | User remains logged in | Medium |

---

## Test Summary

| Module | Total Tests | High Priority | Medium Priority | Low Priority |
|--------|-------------|---------------|-----------------|--------------|
| Login | 17 | 10 | 7 | 0 |
| Product Inventory | 20 | 14 | 6 | 0 |
| Product Detail | 7 | 6 | 1 | 0 |
| Shopping Cart | 13 | 7 | 6 | 0 |
| Checkout - Information | 15 | 7 | 2 | 6 |
| Checkout - Overview | 12 | 8 | 4 | 0 |
| Checkout - Confirmation | 5 | 3 | 2 | 0 |
| Navigation Menu | 6 | 2 | 3 | 1 |
| Logout | 6 | 4 | 2 | 0 |
| Reset App State | 6 | 4 | 2 | 0 |
| **TOTAL** | **107** | **65** | **35** | **7** |
