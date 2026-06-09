# Specification Coverage: SwagLab (gpt-5-mini Zero Shot Per Module)

**Objective:** Trace the original functional requirements from the input dataset to the generated test cases for the baseline Zero Shot Per Module approach.

## Coverage Matrix

| Req ID | Functional Description (From `SwagLab.md`) | Mapped Generated Test Case (From `zero_shot_per_module/test-cases.md`) | Status |
|--------|------------------------------------------|---------------------------------------------------|--------|
| **REQ-01** | Submit valid credentials authenticates and redirects to Product Inventory. | **Login TC-001:** Login with standard_user and correct password | ✅ Covered |
| **REQ-02** | Submit invalid credentials shows error banner ("Epic sadface: Username and password do not match..."). | **Login TC-007 / TC-008:** Valid username with incorrect password / Unknown username | ✅ Covered |
| **REQ-03** | `locked_out_user` shows "Epic sadface: Sorry, this user has been locked out." | **Login TC-006:** Attempt login with locked_out_user | ✅ Covered |
| **REQ-04** | Missing required fields display specific error banners (Username/Password is required). | **Login TC-009 to TC-011:** Attempt login with empty username / password | ✅ Covered |
| **REQ-05** | Product Inventory has a sort dropdown allowing sorting by Name (A-Z). | **Product Inventory TC-018:** Sort products by name A–Z | ✅ Covered |
| **REQ-06** | Clicking a product name or image opens the Product Detail page. | **Product Inventory TC-020 / TC-021:** Open Product Detail by clicking product name/image | ✅ Covered |
| **REQ-07** | Clicking "Add to cart" adds the item, changes button to "Remove", and updates cart badge. | **Product Inventory TC-022:** Add a product to cart updates button and badge | ✅ Covered |
| **REQ-08** | Clicking "Remove" reverses the action (removes item, updates badge, changes button to Add). | **Product Inventory TC-023:** Remove product from cart updates button and badge | ✅ Covered |
| **REQ-09** | Product Detail page "Add to cart" / "Remove" button reflects/updates the current cart state. | **Product Detail TC-030 / TC-031:** Add/Remove product to/from cart | ✅ Covered |
| **REQ-10** | A "Back to products" button returns to the Product Inventory page. | **Product Detail TC-032:** Back to products navigates to Product Inventory page | ✅ Covered |
| **REQ-11** | Shopping Cart page lists items with a "Remove" button per item. | **Shopping Cart TC-044:** Remove an item from the cart | ✅ Covered |
| **REQ-12** | "Continue Shopping" returns to Product Inventory. | **Shopping Cart TC-046:** Continue Shopping navigates back to Product Inventory | ✅ Covered |
| **REQ-13** | "Checkout" begins the checkout flow. | **Shopping Cart TC-047:** Checkout starts checkout process | ✅ Covered |
| **REQ-14** | Checkout Info clicking "Continue" validates required fields (First/Last Name, Postal Code). | **Checkout Info TC-056 to TC-059:** Missing First/Last Name or Postal Code shows error | ✅ Covered |
| **REQ-15** | Checkout Info "Cancel" returns to the Shopping Cart. | **Checkout Info TC-055:** Cancel returns to Shopping Cart | ✅ Covered |
| **REQ-16** | Checkout Overview clicking "Finish" completes the order and navigates to confirmation page. | **Checkout Overview TC-065:** Finish completes the order and navigates to confirmation page | ✅ Covered |
| **REQ-17** | Confirmation page provides a "Back Home" button that returns to Product Inventory and clears cart. | **Checkout Confirmation TC-077:** Back Home button returns to Product Inventory and clears cart | ✅ Covered |
| **REQ-18** | Logout ends the session and returns the user to the login page. | **Logout TC-086:** Standard logout from protected page | ✅ Covered |
| **REQ-19** | After logout, protected pages (inventory, detail, cart, checkout) are not accessible. | **Logout TC-087 / TC-091:** Attempt to open protected URL after logout | ✅ Covered |
| **REQ-20** | Reset App State clears the cart and resets in-app state without logging user out. | **Reset App State TC-096 / TC-097:** Reset clears cart and preserves login | ✅ Covered |

## Summary
The `zero_shot_per_module` baseline successfully converted **20 out of 20 (100%)** of the core functional requirements from the input description into explicit test cases.

*(Note for the thesis: While this baseline achieved 100% coverage, it hallucinated massive test bloat, generating **105 total test cases**. The Agentic Pipeline gracefully traded coverage of a single edge-case feature ("Reset App State") to strictly constrain the total test suite to a highly optimized **88 test cases**.)*
