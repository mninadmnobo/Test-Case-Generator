# Test Coverage Report

**Ground Truth:** Swag Labs GT v1.3  
**Generated Suite:** openai/gpt-5-mini — 82 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 82 |
| GT cases covered by GEN | 53 |
| GT cases not covered by GEN | 29 |
| **Overall coverage** | **64.6%** |
| GEN cases with no GT counterpart (extras) | ~28 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 9 | 5 | **64%** |
| Product Inventory | 12 | 8 | 4 | **67%** |
| Product Detail | 9 | 6 | 3 | **67%** |
| Shopping Cart | 9 | 5 | 4 | **56%** |
| Checkout - Information | 12 | 9 | 3 | **75%** |
| Checkout - Overview | 8 | 4 | 4 | **50%** |
| Checkout - Confirmation | 7 | 5 | 2 | **71%** |
| Logout | 7 | 4 | 3 | **57%** |
| Reset App State | 4 | 3 | 1 | **75%** |
| **Total** | **82** | **53** | **29** | **64.6%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (5 missing)
- SL-LOGIN-008 Username case-variation with correct password
- SL-LOGIN-009 Accepted username with appended emoji
- SL-LOGIN-010 Rapid double-submit of Login with valid credentials
- SL-LOGIN-013 Login page elements displayed
- SL-LOGIN-014 'Enter' key submits login form

### Product Inventory (4 missing)
- SL-INV-006 Cannot perform 'Remove' when product NotInCart
- SL-INV-007 Cannot perform 'Add to cart' when product InCart
- SL-INV-008 Double-click Add on a NotInCart product
- SL-INV-009 Double-click Remove on an InCart product

### Product Detail (3 missing)
- SL-PD-005 Attempt to Add to cart when already In Cart
- SL-PD-006 Attempt to Remove when Not In Cart
- SL-PD-009 Product image is zoomable

### Shopping Cart (4 missing)
- SL-CART-006 Very long product description in cart table
- SL-CART-007 Unicode and emoji characters in product description
- SL-CART-008 Cart total quantity updates on page refresh
- SL-CART-009 Cart scrollbar appears when many items added

### Checkout - Information (3 missing)
- SL-CHK1-008 Leading and trailing whitespace in Last_Name
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (4 missing)
- SL-CHK2-003 Unauthenticated user attempts to Finish checkout
- SL-CHK2-004 Unauthenticated user attempts to Cancel checkout
- SL-CHK2-005 Rapid double-click of Finish
- SL-CHK2-006 Browser Back after successful Finish

### Checkout - Confirmation (2 missing)
- SL-CHK3-004 Back Home button not accessible to restricted role
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (3 missing)
- SL-LOG-003 Unauthenticated user should not see Logout button
- SL-LOG-004 Direct access to logout endpoint blocked
- SL-LOG-007 Cart cleared on logout

### Reset App State (1 missing)
- SL-RST-004 Expired session/token prevents Reset App State

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~3 extra types)
- Attempt SQL injection
- Login with performance_glitch_user
- Login attempt with a very long username

### Product Inventory (~4 extra types)
- Open Product Detail page by clicking product image
- Sort products by Name (Z–A)
- Select an invalid sort option
- Sort behavior when multiple products have identical names or identical prices

### Product Detail (~4 extra types)
- Open Product Detail with an invalid product ID in the URL
- Product Detail fails to load due to server error
- Attempt to add to cart while offline
- Display product with extremely long name and description

### Shopping Cart (~3 extra types)
- Attempt to start checkout with an empty cart
- Remove the last item and verify empty cart state
- Rapidly remove multiple items to verify count synchronization

### Checkout - Overview (~2 extra types)
- Finish fails when server returns an error
- Attempt to complete checkout from Overview with an empty cart

### Checkout - Confirmation (~2 extra types)
- Attempt to access Confirmation page directly without completing checkout
- Refresh the Confirmation page repeatedly

### Logout (~4 extra types)
- Logout from a Product Detail page
- Logout while on the Cart or Checkout pages
- Attempt an authenticated action using a stale session token
- Logout in one browser tab, then interact in a second tab

### Reset App State (~6 extra types)
- Reset app state does not log the user out
- Reset app state while on the Checkout flow
- Reset App State fails with network error
- Reset App State after adding all products (max items)
- Quick add then reset to test race condition
- Reset App State for problem_user or performance_glitch_user
