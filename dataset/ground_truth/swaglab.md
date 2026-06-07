# Swag Labs Test Cases

**Website URL:** https://www.saucedemo.com/
**Test Suite Version:** 1.3

---

## Table of Contents
1. [Login](#1-login)
2. [Product Inventory](#2-product-inventory)
3. [Product Detail](#3-product-detail)
4. [Shopping Cart](#4-shopping-cart)
5. [Checkout - Information](#5-checkout---information)
6. [Checkout - Overview](#6-checkout---overview)
7. [Checkout - Confirmation](#7-checkout---confirmation)
8. [Logout](#8-logout)
9. [Reset App State](#9-reset-app-state)

---

## 1. Login

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-LOGIN-001 | Successful login with accepted username and correct password | Redirects to inventory | High |
| SL-LOGIN-002 | Locked out user submits credentials | Locked out error shown | High |
| SL-LOGIN-003 | Submit unrecognized username with a password | Credential mismatch error | High |
| SL-LOGIN-004 | Submit with missing Username and provided Password | Username required error | High |
| SL-LOGIN-005 | Submit with provided Username and missing Password | Password required error | High |
| SL-LOGIN-006 | Submit with both Username and Password missing | Both required errors | High |
| SL-LOGIN-007 | Accepted username with leading and trailing whitespace | Login succeeds | Medium |
| SL-LOGIN-008 | Username case-variation with correct password | Login blocked | Medium |
| SL-LOGIN-009 | Accepted username with appended emoji | Login blocked | Low |
| SL-LOGIN-010 | Rapid double-submit of Login with valid credentials | Successful login, no duplicates | Medium |
| SL-LOGIN-011 | Submit with invalid credentials | Credential mismatch error | High |
| SL-LOGIN-012 | Submit with provided Username and missing Password (inline) | Inline password required error | Medium |
| SL-LOGIN-013 | Login page elements displayed | All input fields and buttons visible | Medium |
| SL-LOGIN-014 | 'Enter' key submits login form | Form submits on enter | Medium |

## 2. Product Inventory

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-INV-001 | Open Product Detail from product name | Navigates to detail page | High |
| SL-INV-002 | Add product to cart from product list | Button changes to Remove, badge updates | High |
| SL-INV-003 | Remove product from cart from product list | Button changes to Add, badge updates | High |
| SL-INV-004 | Sort products by Name (A–Z) | Products sorted A-Z | High |
| SL-INV-005 | Unauthenticated user cannot access Inventory | Redirects to login | High |
| SL-INV-006 | Cannot perform 'Remove' when product NotInCart | Remove button unavailable | Medium |
| SL-INV-007 | Cannot perform 'Add to cart' when product InCart | Add button unavailable | Medium |
| SL-INV-008 | Double-click Add on a NotInCart product | Single item added | Medium |
| SL-INV-009 | Double-click Remove on an InCart product | Single item removed | Medium |
| SL-INV-010 | Rapidly add multiple distinct products | All items added to cart | Medium |
| SL-INV-011 | Products displayed with correct formatting | Images and text align properly | High |
| SL-INV-012 | Sort by Price (High to Low) functionality | Products sorted by price descending | High |

## 3. Product Detail

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-PD-001 | Add product to cart when product is not in cart | Added to cart | High |
| SL-PD-002 | Remove product from cart when product is in cart | Removed from cart | High |
| SL-PD-003 | Navigate back to Product Inventory via link | Returns to inventory | High |
| SL-PD-004 | Open Shopping Cart via cart icon | Navigates to cart | High |
| SL-PD-005 | Attempt to Add to cart when already In Cart | Add action blocked/hidden | Medium |
| SL-PD-006 | Attempt to Remove when Not In Cart | Remove action blocked/hidden | Medium |
| SL-PD-007 | Rapid double-click 'Add to cart' | Single item added | Medium |
| SL-PD-008 | Rapid double-click 'Remove' | Single item removed | Medium |
| SL-PD-009 | Product image is zoomable | Image expands on click | Low |

## 4. Shopping Cart

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-CART-001 | Remove an item from the cart | Item disappears from list | High |
| SL-CART-002 | Continue Shopping navigates to Product Inventory | Returns to inventory | High |
| SL-CART-003 | Begin Checkout from the cart | Navigates to checkout info | High |
| SL-CART-004 | Unauthenticated user cannot access Shopping Cart | Redirects to login | High |
| SL-CART-005 | Unauthenticated user cannot begin checkout | Checkout action blocked | High |
| SL-CART-006 | Very long product description in cart table | Description wraps cleanly | Low |
| SL-CART-007 | Unicode and emoji characters in product description | Characters render correctly | Low |
| SL-CART-008 | Cart total quantity updates on page refresh | Badge persists value | Medium |
| SL-CART-009 | Cart scrollbar appears when many items added | List becomes scrollable | Low |

## 5. Checkout - Information

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-CHK1-001 | Continue with all required fields filled | Navigates to overview | High |
| SL-CHK1-002 | Continue with multiple required fields missing | Error banners shown | High |
| SL-CHK1-003 | Continue with First Name missing | First name error | High |
| SL-CHK1-004 | Continue with Last Name missing | Last name error | High |
| SL-CHK1-005 | Continue with Zip/Postal Code missing | Postal code error | High |
| SL-CHK1-006 | Click Cancel returns user to Shopping Cart | Navigates to cart | High |
| SL-CHK1-007 | Whitespace-only in First_Name | Blocked as empty | Medium |
| SL-CHK1-008 | Leading and trailing whitespace in Last_Name | Whitespace trimmed | Medium |
| SL-CHK1-009 | Very long text in name fields (200+ chars) | Text truncated or accepted | Low |
| SL-CHK1-010 | Special characters and emoji in name fields | Characters preserved | Low |
| SL-CHK1-011 | Autofill works for shipping information | Fields populate from browser | Medium |
| SL-CHK1-012 | Pressing 'Enter' in Postal Code field submits form | Form submits successfully | Medium |

## 6. Checkout - Overview

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-CHK2-001 | Finish checkout navigates to confirmation page | Navigates to confirmation | High |
| SL-CHK2-002 | Cancel exits checkout from overview | Returns to inventory | High |
| SL-CHK2-003 | Unauthenticated user attempts to Finish checkout | Blocked | High |
| SL-CHK2-004 | Unauthenticated user attempts to Cancel checkout | Blocked | High |
| SL-CHK2-005 | Rapid double-click of Finish | Only one order created | Medium |
| SL-CHK2-006 | Browser Back after successful Finish | Duplicate order blocked | High |
| SL-CHK2-007 | Very long shipping address entered prior to Overview | Address displays cleanly | Low |
| SL-CHK2-008 | Total price correctly includes tax calculation | Math is accurate | High |

## 7. Checkout - Confirmation

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-CHK3-001 | Confirmation page displays the success message | Message visible | High |
| SL-CHK3-002 | Back Home button returns to Product Inventory | Navigates to inventory | High |
| SL-CHK3-003 | Unauthenticated user cannot access Confirmation page | Redirects to login | High |
| SL-CHK3-004 | Back Home button not accessible to restricted role | Button disabled/hidden | Medium |
| SL-CHK3-005 | Rapid double-click of Back Home button | Single navigation event | Medium |
| SL-CHK3-006 | Use browser Back to return to Confirmation | Navigation succeeds | Medium |
| SL-CHK3-007 | Success image (Pony Express) displayed | Image renders | Medium |

## 8. Logout

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-LOG-001 | Click Logout redirects user to Login Page | Navigates to login | High |
| SL-LOG-002 | Accessing a protected page after logout redirects | Redirects to login | High |
| SL-LOG-003 | Unauthenticated user should not see Logout button | Button hidden | High |
| SL-LOG-004 | Direct access to logout endpoint blocked | Blocked | High |
| SL-LOG-005 | Rapid double-click Logout | Single logout event | Medium |
| SL-LOG-006 | Browser Back after logout | Protected content blocked | High |
| SL-LOG-007 | Cart cleared on logout | Cart is empty on next login | High |

## 9. Reset App State

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SL-RST-001 | Reset clears a populated cart and resets buttons | State cleared | High |
| SL-RST-002 | Reset when cart is already empty keeps UI cleared | No errors thrown | Medium |
| SL-RST-003 | Unauthenticated user cannot perform Reset App State | Blocked | High |
| SL-RST-004 | Expired session/token prevents Reset App State | Blocked | High |

---

## Test Summary

| Module | Total Tests | High Priority | Medium Priority | Low Priority |
|--------|-------------|---------------|-----------------|--------------|
| Login | 14 | 7 | 6 | 1 |
| Product Inventory | 12 | 7 | 5 | 0 |
| Product Detail | 9 | 4 | 4 | 1 |
| Shopping Cart | 9 | 5 | 1 | 3 |
| Checkout - Information | 12 | 6 | 4 | 2 |
| Checkout - Overview | 8 | 6 | 1 | 1 |
| Checkout - Confirmation | 7 | 3 | 4 | 0 |
| Logout | 7 | 6 | 1 | 0 |
| Reset App State | 4 | 3 | 1 | 0 |
| **TOTAL** | **82** | **47** | **27** | **8** |
