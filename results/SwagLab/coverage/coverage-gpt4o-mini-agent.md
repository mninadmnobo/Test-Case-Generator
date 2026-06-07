# Test Coverage Report

**Ground Truth:** Swag Labs Test Cases v1.3  
**Generated Suite:** openai/gpt-4o-mini — 66 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 82 |
| GT cases covered by GEN | 46 |
| GT cases not covered by GEN | 36 |
| **Overall coverage** | **56.1%** |
| GEN cases with no GT counterpart (extras) | ~14 |

*Note: The `gpt-4o-mini` agent generated a smaller suite (66 cases vs 92 from the previous model) resulting in a correspondingly lower coverage rate against the 82 Ground Truth cases.*

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 9 | 5 | **64.3%** |
| Product Inventory | 12 | 9 | 3 | **75.0%** |
| Product Detail | 9 | 6 | 3 | **66.7%** |
| Shopping Cart | 9 | 3 | 6 | **33.3%** |
| Checkout - Information | 12 | 9 | 3 | **75.0%** |
| Checkout - Overview | 8 | 3 | 5 | **37.5%** |
| Checkout - Confirmation | 7 | 2 | 5 | **28.6%** |
| Logout | 7 | 3 | 4 | **42.9%** |
| Reset App State | 4 | 2 | 2 | **50.0%** |
| **Total** | **82** | **46** | **36** | **56.1%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were absent from the `gpt-4o-mini` suite:

### Login (5 missing)
- SL-LOGIN-006 Submit with both Username and Password missing
- SL-LOGIN-008 Username case-variation with correct password
- SL-LOGIN-010 Rapid double-submit of Login with valid credentials
- SL-LOGIN-013 Login page elements displayed
- SL-LOGIN-014 'Enter' key submits login form

### Product Inventory (3 missing)
- SL-INV-005 Unauthenticated user cannot access Inventory
- SL-INV-010 Rapidly add multiple distinct products
- SL-INV-011 Products displayed with correct formatting

### Product Detail (3 missing)
- SL-PD-005 Attempt to Add to cart when already In Cart
- SL-PD-006 Attempt to Remove when Not In Cart
- SL-PD-009 Product image is zoomable

### Shopping Cart (6 missing)
- SL-CART-004 Unauthenticated user cannot access Shopping Cart
- SL-CART-005 Unauthenticated user cannot begin checkout
- SL-CART-006 Very long product description in cart table
- SL-CART-007 Unicode and emoji characters in product description
- SL-CART-008 Cart total quantity updates on page refresh
- SL-CART-009 Cart scrollbar appears when many items added

### Checkout - Information (3 missing)
- SL-CHK1-009 Very long text in name fields (200+ chars)
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (5 missing)
- SL-CHK2-003 Unauthenticated user attempts to Finish checkout
- SL-CHK2-004 Unauthenticated user attempts to Cancel checkout
- SL-CHK2-006 Browser Back after successful Finish
- SL-CHK2-007 Very long shipping address entered prior to Overview
- SL-CHK2-008 Total price correctly includes tax calculation

### Checkout - Confirmation (5 missing)
- SL-CHK3-001 Confirmation page displays the success message
- SL-CHK3-003 Unauthenticated user cannot access Confirmation page
- SL-CHK3-004 Back Home button not accessible to restricted role
- SL-CHK3-006 Use browser Back to return to Confirmation
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (4 missing)
- SL-LOG-002 Accessing a protected page after logout redirects
- SL-LOG-004 Direct access to logout endpoint blocked
- SL-LOG-006 Browser Back after logout
- SL-LOG-007 Cart cleared on logout

### Reset App State (2 missing)
- SL-RST-002 Reset when cart is already empty keeps UI cleared
- SL-RST-004 Expired session/token prevents Reset App State

---

## Extra Scenarios

The agent generated the following extra edge cases that had no direct equivalent in the expanded GT scope (~14 total). Examples include:

- **Login:** Attempt login with extremely long Username.
- **Product Inventory:** Attempt to add/remove product from cart without selecting an item (edge states).
- **Product Detail:** Attempt to add a product to the cart when the cart is already at maximum capacity.
- **Shopping Cart:** Attempt to continue shopping or begin checkout with an empty cart.
- **Checkout Flows:** Attempt to finish the order without any payment or shipping information.
