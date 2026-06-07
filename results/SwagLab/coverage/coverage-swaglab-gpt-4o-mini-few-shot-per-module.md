# Test Coverage Report

**Ground Truth:** Swag Labs GT v1.3  
**Generated Suite:** openai/gpt-4o-mini — 38 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 82 |
| GT cases covered by GEN | 36 |
| GT cases not covered by GEN | 46 |
| **Overall coverage** | **43.9%** |
| GEN cases with no GT counterpart (extras) | ~7 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 8 | 6 | **57%** |
| Product Inventory | 12 | 5 | 7 | **42%** |
| Product Detail | 9 | 3 | 6 | **33%** |
| Shopping Cart | 9 | 2 | 7 | **22%** |
| Checkout - Information | 12 | 6 | 6 | **50%** |
| Checkout - Overview | 8 | 3 | 5 | **38%** |
| Checkout - Confirmation | 7 | 3 | 4 | **43%** |
| Logout | 7 | 3 | 4 | **43%** |
| Reset App State | 4 | 3 | 1 | **75%** |
| **Total** | **82** | **36** | **46** | **43.9%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (6 missing)
- SL-LOGIN-007 Accepted username with leading and trailing whitespace
- SL-LOGIN-008 Username case-variation with correct password
- SL-LOGIN-009 Accepted username with appended emoji
- SL-LOGIN-010 Rapid double-submit of Login with valid credentials
- SL-LOGIN-013 Login page elements displayed
- SL-LOGIN-014 'Enter' key submits login form

### Product Inventory (7 missing)
- SL-INV-001 Open Product Detail from product name
- SL-INV-003 Remove product from cart from product list
- SL-INV-004 Sort products by Name (A–Z)
- SL-INV-006 Cannot perform 'Remove' when product NotInCart
- SL-INV-007 Cannot perform 'Add to cart' when product InCart
- SL-INV-010 Rapidly add multiple distinct products
- SL-INV-011 Products displayed with correct formatting

### Product Detail (6 missing)
- SL-PD-004 Open Shopping Cart via cart icon
- SL-PD-005 Attempt to Add to cart when already In Cart
- SL-PD-006 Attempt to Remove when Not In Cart
- SL-PD-007 Rapid double-click 'Add to cart'
- SL-PD-008 Rapid double-click 'Remove'
- SL-PD-009 Product image is zoomable

### Shopping Cart (7 missing)
- SL-CART-003 Begin Checkout from the cart
- SL-CART-004 Unauthenticated user cannot access Shopping Cart
- SL-CART-005 Unauthenticated user cannot begin checkout
- SL-CART-006 Very long product description in cart table
- SL-CART-007 Unicode and emoji characters in product description
- SL-CART-008 Cart total quantity updates on page refresh
- SL-CART-009 Cart scrollbar appears when many items added

### Checkout - Information (6 missing)
- SL-CHK1-006 Click Cancel returns user to Shopping Cart
- SL-CHK1-007 Whitespace-only in First_Name
- SL-CHK1-008 Leading and trailing whitespace in Last_Name
- SL-CHK1-010 Special characters and emoji in name fields
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (5 missing)
- SL-CHK2-003 Unauthenticated user attempts to Finish checkout
- SL-CHK2-004 Unauthenticated user attempts to Cancel checkout
- SL-CHK2-005 Rapid double-click of Finish
- SL-CHK2-006 Browser Back after successful Finish
- SL-CHK2-007 Very long shipping address entered prior to Overview

### Checkout - Confirmation (4 missing)
- SL-CHK3-004 Back Home button not accessible to restricted role
- SL-CHK3-005 Rapid double-click of Back Home button
- SL-CHK3-006 Use browser Back to return to Confirmation
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (4 missing)
- SL-LOG-003 Unauthenticated user should not see Logout button
- SL-LOG-004 Direct access to logout endpoint blocked
- SL-LOG-006 Browser Back after logout
- SL-LOG-007 Cart cleared on logout

### Reset App State (1 missing)
- SL-RST-004 Expired session/token prevents Reset App State

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~2 extra types)
- Log in with maximum length username and password
- Log in with minimum length username and password

### Product Detail (~1 extra types)
- Attempt to add a product to the cart when not logged in

### Shopping Cart (~3 extra types)
- View items in the shopping cart
- Attempt to checkout with an empty cart
- Add maximum number of items to the cart and verify the display

### Checkout - Confirmation (~1 extra types)
- Check confirmation page after multiple rapid checkouts
