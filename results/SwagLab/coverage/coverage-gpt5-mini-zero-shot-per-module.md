# Test Coverage Report

**Ground Truth:** Swag Labs GT v1.3  
**Generated Suite:** openai/gpt-5-mini — 105 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 82 |
| GT cases covered by GEN | 52 |
| GT cases not covered by GEN | 30 |
| **Overall coverage** | **63.4%** |
| GEN cases with no GT counterpart (extras) | ~47 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 9 | 5 | **64%** |
| Product Inventory | 12 | 6 | 6 | **50%** |
| Product Detail | 9 | 6 | 3 | **67%** |
| Shopping Cart | 9 | 5 | 4 | **56%** |
| Checkout - Information | 12 | 9 | 3 | **75%** |
| Checkout - Overview | 8 | 5 | 3 | **63%** |
| Checkout - Confirmation | 7 | 4 | 3 | **57%** |
| Logout | 7 | 5 | 2 | **71%** |
| Reset App State | 4 | 3 | 1 | **75%** |
| **Total** | **82** | **52** | **30** | **63.4%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (5 missing)
- SL-LOGIN-008 Username case-variation with correct password
- SL-LOGIN-009 Accepted username with appended emoji
- SL-LOGIN-010 Rapid double-submit of Login with valid credentials
- SL-LOGIN-013 Login page elements displayed
- SL-LOGIN-014 'Enter' key submits login form

### Product Inventory (6 missing)
- SL-INV-006 Cannot perform 'Remove' when product NotInCart
- SL-INV-007 Cannot perform 'Add to cart' when product InCart
- SL-INV-008 Double-click Add on a NotInCart product
- SL-INV-009 Double-click Remove on an InCart product
- SL-INV-010 Rapidly add multiple distinct products
- SL-INV-012 Sort by Price (High to Low) functionality

### Product Detail (3 missing)
- SL-PD-005 Attempt to Add to cart when already In Cart
- SL-PD-006 Attempt to Remove when Not In Cart
- SL-PD-009 Product image is zoomable

### Shopping Cart (4 missing)
- SL-CART-004 Unauthenticated user cannot access Shopping Cart
- SL-CART-005 Unauthenticated user cannot begin checkout
- SL-CART-007 Unicode and emoji characters in product description
- SL-CART-008 Cart total quantity updates on page refresh

### Checkout - Information (3 missing)
- SL-CHK1-008 Leading and trailing whitespace in Last_Name
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (3 missing)
- SL-CHK2-003 Unauthenticated user attempts to Finish checkout
- SL-CHK2-004 Unauthenticated user attempts to Cancel checkout
- SL-CHK2-006 Browser Back after successful Finish

### Checkout - Confirmation (3 missing)
- SL-CHK3-003 Unauthenticated user cannot access Confirmation page
- SL-CHK3-004 Back Home button not accessible to restricted role
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (2 missing)
- SL-LOG-003 Unauthenticated user should not see Logout button
- SL-LOG-007 Cart cleared on logout

### Reset App State (1 missing)
- SL-RST-003 Unauthenticated user cannot perform Reset App State

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Login (~4 extra types)
- Login attempt with a very long username
- Attempt SQL-injection style username
- Password field masks input
- Accepted usernames list is visible on the login page

### Product Inventory (~5 extra types)
- Open Product Detail by clicking product image
- Empty inventory displays no-products message
- Very long product name and description rendering
- Sorting with duplicate names or identical prices
- Rapid add/remove toggling keeps cart badge consistent

### Product Detail (~9 extra types)
- Display product image, name, description, and price (general UI check)
- Action button reflects current cart state on page load
- Server error when adding to cart
- Invalid product id in URL
- Attempt to add to cart while offline
- Missing price field handling
- Very long product name and description rendering
- Extremely large or high-precision price displays
- Broken product image displays placeholder

### Shopping Cart (~6 extra types)
- Cart page displays added items with quantity, description and Remove button
- Remove last item results in empty cart state
- Checkout attempt when cart is empty is blocked
- Remove action fails due to server error
- Quantity is displayed as 1 and cannot be edited
- Checkout blocked when item data is invalid (missing price)

### Checkout - Information (~1 extra types)
- Alphanumeric postal code with spaces is accepted

### Checkout - Overview (~5 extra types)
- Finish blocked when payment information is missing or invalid
- Finish blocked when shipping information is missing
- Overview handling for empty cart (zero items)
- Server/network error when finishing
- Zero-price items or discounts resulting in zero total can be completed

### Checkout - Confirmation (~6 extra types)
- Back Home button operable via keyboard
- Confirmation message persists after page refresh
- Back Home clears very large cart (stress)
- Direct access to confirmation page without completing checkout is rejected/redirected
- Server error prevents clearing cart when clicking Back Home
- Empty or missing success message falls back to default

### Logout (~5 extra types)
- Re-login after logout
- Network/server error during logout
- Logout in one tab invalidates session in other open tabs
- Verify session token/cookie and local storage cleared after logout
- Submit protected POST action (checkout) after logout

### Reset App State (~6 extra types)
- Reset while on checkout page clears cart
- Reset fails due to server error
- Rapid repeated taps on Reset App State are idempotent
- Reset with very large cart (stress test)
- Reset while device is offline (no network) is handled gracefully
- Reset invoked while an add/remove operation is in progress resolves to a consistent final state
