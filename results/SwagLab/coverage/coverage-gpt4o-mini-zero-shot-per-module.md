# Test Coverage Report

**Ground Truth:** Swag Labs GT v1.3  
**Generated Suite:** openai/gpt-4o-mini — 54 cases  
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
| GEN cases with no GT counterpart (extras) | ~19 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 8 | 6 | **57%** |
| Product Inventory | 12 | 6 | 6 | **50%** |
| Product Detail | 9 | 3 | 6 | **33%** |
| Shopping Cart | 9 | 2 | 7 | **22%** |
| Checkout - Information | 12 | 7 | 5 | **58%** |
| Checkout - Overview | 8 | 2 | 6 | **25%** |
| Checkout - Confirmation | 7 | 3 | 4 | **43%** |
| Logout | 7 | 2 | 5 | **29%** |
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

### Product Inventory (6 missing)
- SL-INV-007 Cannot perform 'Add to cart' when product InCart
- SL-INV-008 Double-click Add on a NotInCart product
- SL-INV-009 Double-click Remove on an InCart product
- SL-INV-010 Rapidly add multiple distinct products
- SL-INV-011 Products displayed with correct formatting
- SL-INV-012 Sort by Price (High to Low) functionality

### Product Detail (6 missing)
- SL-PD-002 Remove product from cart when product is in cart
- SL-PD-005 Attempt to Add to cart when already In Cart
- SL-PD-006 Attempt to Remove when Not In Cart
- SL-PD-007 Rapid double-click 'Add to cart'
- SL-PD-008 Rapid double-click 'Remove'
- SL-PD-009 Product image is zoomable

### Shopping Cart (7 missing)
- SL-CART-001 Remove an item from the cart
- SL-CART-004 Unauthenticated user cannot access Shopping Cart
- SL-CART-005 Unauthenticated user cannot begin checkout
- SL-CART-006 Very long product description in cart table
- SL-CART-007 Unicode and emoji characters in product description
- SL-CART-008 Cart total quantity updates on page refresh
- SL-CART-009 Cart scrollbar appears when many items added

### Checkout - Information (5 missing)
- SL-CHK1-006 Click Cancel returns user to Shopping Cart
- SL-CHK1-007 Whitespace-only in First_Name
- SL-CHK1-008 Leading and trailing whitespace in Last_Name
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (6 missing)
- SL-CHK2-003 Unauthenticated user attempts to Finish checkout
- SL-CHK2-004 Unauthenticated user attempts to Cancel checkout
- SL-CHK2-005 Rapid double-click of Finish
- SL-CHK2-006 Browser Back after successful Finish
- SL-CHK2-007 Very long shipping address entered prior to Overview
- SL-CHK2-008 Total price correctly includes tax calculation

### Checkout - Confirmation (4 missing)
- SL-CHK3-004 Back Home button not accessible to restricted role
- SL-CHK3-005 Rapid double-click of Back Home button
- SL-CHK3-006 Use browser Back to return to Confirmation
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (5 missing)
- SL-LOG-002 Accessing a protected page after logout redirects
- SL-LOG-004 Direct access to logout endpoint blocked
- SL-LOG-005 Rapid double-click Logout
- SL-LOG-006 Browser Back after logout
- SL-LOG-007 Cart cleared on logout

### Reset App State (1 missing)
- SL-RST-004 Expired session/token prevents Reset App State

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~2 extra types)
- Login attempt with maximum length username
- Login attempt with special characters in username

### Product Inventory (~1 extra types)
- Add maximum number of products to cart

### Product Detail (~3 extra types)
- Attempt to add out-of-stock product to cart
- Check product detail with maximum length description
- Check product detail with empty fields

### Shopping Cart (~5 extra types)
- User successfully views items in the cart
- User tries to remove an item that is not in the cart
- User views cart with maximum number of items
- User views cart with one item
- User views cart with empty state

### Checkout - Overview (~3 extra types)
- Attempt to finish order with empty cart
- Order summary with maximum items
- Order summary with zero total

### Checkout - Confirmation (~2 extra types)
- Confirmation page with empty cart
- Confirmation page with maximum length message

### Logout (~2 extra types)
- Logout while session is about to expire
- Logout from multiple tabs

### Reset App State (~1 extra types)
- Reset app state multiple times in quick succession
