# Specification Coverage: SwagLab (gpt-5-mini Agent)

**Objective:** Trace the original functional requirements from the input dataset to the generated test cases.

## Coverage Matrix

| Req ID | Functional Description (From `SwagLab.md`) | Mapped Generated Test Case (From `test-cases.md`) | Status |
|--------|------------------------------------------|---------------------------------------------------|--------|
| **REQ-01** | Submit valid credentials authenticates and redirects to Product Inventory. | **Login TC-001:** Successful login with accepted username and correct password | ✅ Covered |
| **REQ-02** | Submit invalid credentials shows error banner ("Epic sadface: Username and password do not match..."). | **Login TC-003 / TC-010:** Submit with invalid credentials (username/password mismatch) | ✅ Covered |
| **REQ-03** | `locked_out_user` shows "Epic sadface: Sorry, this user has been locked out." | **Login TC-002 / TC-011:** Locked out user submits credentials and sees locked-out error | ✅ Covered |
| **REQ-04** | Missing required fields display specific error banners (Username/Password is required). | **Login TC-004 to TC-009:** Submit with missing Username/Password shows required error | ✅ Covered |
| **REQ-05** | Product Inventory has a sort dropdown allowing sorting by Name (A-Z). | **Product Inventory TC-004:** Sort products by Name (A–Z) using Sort_By dropdown | ✅ Covered |
| **REQ-06** | Clicking a product name or image opens the Product Detail page. | **Product Inventory TC-001:** Open Product Detail from product name | ✅ Covered |
| **REQ-07** | Clicking "Add to cart" adds the item, changes button to "Remove", and updates cart badge. | **Product Inventory TC-002:** Add product to cart from product list | ✅ Covered |
| **REQ-08** | Clicking "Remove" reverses the action (removes item, updates badge, changes button to Add). | **Product Inventory TC-003:** Remove product from cart from product list | ✅ Covered |
| **REQ-09** | Product Detail page "Add to cart" / "Remove" button reflects/updates the current cart state. | **Product Detail TC-001 / TC-002:** Add/Remove product to cart when product is not/in cart | ✅ Covered |
| **REQ-10** | A "Back to products" button returns to the Product Inventory page. | **Product Detail TC-003:** Navigate back to Product Inventory via Back to products link | ✅ Covered |
| **REQ-11** | Shopping Cart page lists items with a "Remove" button per item. | **Shopping Cart TC-001:** Remove an item from the cart | ✅ Covered |
| **REQ-12** | "Continue Shopping" returns to Product Inventory. | **Shopping Cart TC-002:** Continue Shopping navigates to Product Inventory | ✅ Covered |
| **REQ-13** | "Checkout" begins the checkout flow. | **Shopping Cart TC-003:** Begin Checkout from the cart | ✅ Covered |
| **REQ-14** | Checkout Info clicking "Continue" validates required fields (First/Last Name, Postal Code). | **Checkout Info TC-002 to TC-005 / TC-007 to TC-010:** Missing required fields show corresponding error banners | ✅ Covered |
| **REQ-15** | Checkout Info "Cancel" returns to the Shopping Cart. | **Checkout Info TC-006:** Click Cancel returns user to Shopping Cart | ✅ Covered |
| **REQ-16** | Checkout Overview clicking "Finish" completes the order and navigates to confirmation page. | **Checkout Overview TC-001:** Finish checkout navigates to confirmation page | ✅ Covered |
| **REQ-17** | Confirmation page provides a "Back Home" button that returns to Product Inventory and clears cart. | **Checkout Confirmation TC-002:** Back Home button returns to Product Inventory and results in an empty cart | ✅ Covered |
| **REQ-18** | Logout ends the session and returns the user to the login page. | **Logout TC-001:** Click Logout redirects user to Login Page | ✅ Covered |
| **REQ-19** | After logout, protected pages (inventory, detail, cart, checkout) are not accessible. | **Logout TC-002 / TC-005:** After logout, protected pages are inaccessible without logging in | ✅ Covered |
| **REQ-20** | Reset App State clears the cart and resets in-app state without logging user out. | *Not explicitly mapped in the provided snippet* | ⚠️ Partial/Missed |

## Summary
The pipeline successfully converted **19 out of 20 (95%)** of the core functional requirements from the input description into explicit, high-quality executable test cases.
