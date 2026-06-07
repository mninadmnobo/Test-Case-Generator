# Test Coverage Report

**Ground Truth:** Swag Labs Test Cases v1.3  
**Generated Suite:** openai/gpt-5-mini — 92 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 82 |
| GT cases covered by GEN | 70 |
| GT cases not covered by GEN | 12 |
| **Overall coverage** | **85.4%** |
| GEN cases with no GT counterpart (extras) | ~22 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Login | 14 | 12 | 2 | **85.7%** |
| Product Inventory | 12 | 10 | 2 | **83.3%** |
| Product Detail | 9 | 8 | 1 | **88.9%** |
| Shopping Cart | 9 | 7 | 2 | **77.8%** |
| Checkout - Information | 12 | 10 | 2 | **83.3%** |
| Checkout - Overview | 8 | 7 | 1 | **87.5%** |
| Checkout - Confirmation | 7 | 6 | 1 | **85.7%** |
| Logout | 7 | 6 | 1 | **85.7%** |
| Reset App State | 4 | 4 | 0 | **100.0%** |
| **Total** | **82** | **70** | **12** | **85.4%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Login (2 missing)
- SL-LOGIN-013 Login page elements displayed
- SL-LOGIN-014 'Enter' key submits login form

### Product Inventory (2 missing)
- SL-INV-011 Products displayed with correct formatting
- SL-INV-012 Sort by Price (High to Low) functionality

### Product Detail (1 missing)
- SL-PD-009 Product image is zoomable

### Shopping Cart (2 missing)
- SL-CART-008 Cart total quantity updates on page refresh
- SL-CART-009 Cart scrollbar appears when many items added

### Checkout - Information (2 missing)
- SL-CHK1-011 Autofill works for shipping information
- SL-CHK1-012 Pressing 'Enter' in Postal Code field submits form

### Checkout - Overview (1 missing)
- SL-CHK2-008 Total price correctly includes tax calculation

### Checkout - Confirmation (1 missing)
- SL-CHK3-007 Success image (Pony Express) displayed

### Logout (1 missing)
- SL-LOG-007 Cart cleared on logout

---

## Extra Scenarios

### Login (~3 extra types)
- Additional boundary tests for inline password errors

### Product Inventory (~4 extra types)
- Multiple permutations of clicking 'Add' rapidly

### Product Detail (~4 extra types)
- Navigating immediately after clicking 'Add to cart' before UI refresh

### Checkout (~6 extra types)
- Duplicate tab scenarios
- Refresh scenarios during confirmation
- Unicode handling inside cardholder details

### Logout (~5 extra types)
- Double-clicking buttons
- Verifying cached UI state on back navigation
