# Specification Coverage: SwagLab (gpt-5-mini Single Generator / Few Shot)

**Objective:** Trace the original functional requirements from the input dataset to the generated test cases for the baseline Single Generator approach.

## Coverage Matrix

| Req ID | Functional Description (From `SwagLab.md`) | Mapped Generated Test Case (From `few_shot_per_module/test-cases.md`) | Status |
|--------|------------------------------------------|---------------------------------------------------|--------|
| **REQ-01** | Submit valid credentials authenticates and redirects to Product Inventory. | **Login TC-001:** Successful login with standard_user | ✅ Covered |
| **REQ-02** | Submit invalid credentials shows error banner ("Epic sadface: Username and password do not match..."). | **Login TC-005:** Attempt to log in with invalid username and/or password | ✅ Covered |
| **REQ-03** | `locked_out_user` shows "Epic sadface: Sorry, this user has been locked out." | **Login TC-004:** Attempt to log in with locked_out_user | ✅ Covered |
| **REQ-04** | Missing required fields display specific error banners (Username/Password is required). | **Login TC-006 to TC-008:** Attempt to log in with missing username/password | ✅ Covered |
| **REQ-05** | Product Inventory has a sort dropdown allowing sorting by Name (A-Z). | **Product Inventory TC-017:** Sort products by Name (A–Z) displays ascending alphabetical order | ✅ Covered |
| **REQ-06** | Clicking a product name or image opens the Product Detail page. | **Product Inventory TC-015 / TC-016:** Open Product Detail page by clicking product name/image | ✅ Covered |
| **REQ-07** | Clicking "Add to cart" adds the item, changes button to "Remove", and updates cart badge. | **Product Inventory TC-013:** Add a single product to the cart updates button and cart badge | ✅ Covered |
| **REQ-08** | Clicking "Remove" reverses the action (removes item, updates badge, changes button to Add). | **Product Inventory TC-014:** Remove a product from the cart updates button and cart badge | ✅ Covered |
| **REQ-09** | Product Detail page "Add to cart" / "Remove" button reflects/updates the current cart state. | **Product Detail TC-026 / TC-027:** Add/Remove product to cart from Product Detail | ✅ Covered |
| **REQ-10** | A "Back to products" button returns to the Product Inventory page. | **Product Detail TC-028:** Navigate back to Product Inventory and to Shopping Cart from Product Detail | ✅ Covered |
| **REQ-11** | Shopping Cart page lists items with a "Remove" button per item. | **Shopping Cart TC-035:** Remove a single item from the cart | ✅ Covered |
| **REQ-12** | "Continue Shopping" returns to Product Inventory. | **Shopping Cart TC-036:** Return to Product Inventory using Continue Shopping | ✅ Covered |
| **REQ-13** | "Checkout" begins the checkout flow. | **Shopping Cart TC-037:** Begin checkout from Shopping Cart | ✅ Covered |
| **REQ-14** | Checkout Info clicking "Continue" validates required fields (First/Last Name, Postal Code). | **Checkout Info TC-046 to TC-048:** Submit form with First/Last Name or Postal Code missing | ✅ Covered |
| **REQ-15** | Checkout Info "Cancel" returns to the Shopping Cart. | **Checkout Info TC-044:** Click Cancel returns user to the Shopping Cart | ✅ Covered |
| **REQ-16** | Checkout Overview clicking "Finish" completes the order and navigates to confirmation page. | **Checkout Overview TC-051:** Complete order from Overview by clicking Finish | ✅ Covered |
| **REQ-17** | Confirmation page provides a "Back Home" button that returns to Product Inventory and clears cart. | **Checkout Confirmation TC-058:** Display success message and Back Home clears cart after completing checkout | ✅ Covered |
| **REQ-18** | Logout ends the session and returns the user to the login page. | **Logout TC-065:** Logout from the Inventory page via the menu | ✅ Covered |
| **REQ-19** | After logout, protected pages (inventory, detail, cart, checkout) are not accessible. | **Logout TC-068:** Attempt to access Inventory URL directly after logging out | ✅ Covered |
| **REQ-20** | Reset App State clears the cart and resets in-app state without logging user out. | *Not explicitly mapped in the provided snippet* | ⚠️ Partial/Missed |

## Summary
The Baseline Single Generator model successfully covered **19 out of 20 (95%)** of the core functional requirements for this simple e-commerce application. 

*(Note for the thesis: Because SwagLab is a simple, non-state-dependent application, both the Pipeline and the Baseline achieved 95% specification coverage. The Pipeline's superiority on SwagLab is demonstrated by its ability to prevent the 42% test bloat hallucinated by the Baseline, not necessarily by covering more core requirements).*
