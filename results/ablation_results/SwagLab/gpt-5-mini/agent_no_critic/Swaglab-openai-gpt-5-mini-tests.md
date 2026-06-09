# Test Cases — Swaglab

Generated: 2026-06-09T09:09:13.162826Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 88 | 26 | 26 | 36 | 39 | 43 | 6 |

## Login

Total: **14** (positive: 6, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials redirects to Product Inventory | User on Login page, User not authenticated, Actor: <role> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | redirects to Product Inventory page | high |
| TC-002 | WF-002 | Login with non-matching credentials shows username/password mismatch error | User on Login page, User not authenticated, Actor: <role> | 1. Enter <non-matching username> in the Username field<br>2. Enter <non-matching password> in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-003 | WF-003 | Login attempt with locked_out_user shows locked out error | User on Login page, User not authenticated, Actor: <role> | 1. Enter locked_out_user in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-004 | WF-004 | Submitting with missing username and password provided shows username required error | User on Login page, User not authenticated, Actor: <role> | 1. Leave the Username field empty<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-005 | WF-005 | Submitting with username provided and missing password shows password required error | User on Login page, User not authenticated, Actor: <role> | 1. Enter <valid username> in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |
| TC-006 | WF-006 | Submitting with both username and password empty shows both required errors | User on Login page, User not authenticated, Actor: <role> | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Username is required.; Epic sadface: Password is required. | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-004 | Submit with Username blank (Password provided) | Login page is displayed | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | Form does not submit; page remains on the Login page; error banner displays: "Epic sadface: Username is required." indicating the Username field is required; no redirect to Product Inventory page. | high |
| TC-008 | WF-005 | Submit with Password blank (Username provided) | Login page is displayed | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | Form does not submit; page remains on the Login page; error banner displays: "Epic sadface: Password is required." indicating the Password field is required; no redirect to Product Inventory page. | high |
| TC-009 | WF-006 | Submit with both Username and Password blank | Login page is displayed | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Form does not submit; page remains on the Login page; error banner(s) display both messages: "Epic sadface: Username is required." and "Epic sadface: Password is required." indicating both fields are required; no redirect to Product Inventory page. | high |
| TC-010 | WF-002 | Submit non-matching credentials (invalid username/password) | Login page is displayed | 1. Enter <non-matching username> in the Username field<br>2. Enter <incorrect password> in the Password field<br>3. Click the Login button | Authentication blocked; page remains on the Login page; error banner displays: "Epic sadface: Username and password do not match any user in this service."; no redirect to Product Inventory page. | high |
| TC-011 | WF-003 | Locked-out user attempt (locked_out_user) | Login page is displayed | 1. Enter locked_out_user in the Username field<br>2. Enter <shared password> in the Password field<br>3. Click the Login button | Authentication blocked; page remains on the Login page; error banner displays: "Epic sadface: Sorry, this user has been locked out."; no redirect to Product Inventory page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) | WF-003 | Username with leading/trailing whitespace that matches locked_out_user after trimming | Login page is open | 1. Enter locked_out_user with leading and trailing spaces in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; error banner 'Epic sadface: Sorry, this user has been locked out.' is shown (this verifies whether the system trims whitespace before checking the locked_out_user constraint). | medium |
| TC-013 (input_edge) | WF-001 | Valid username with leading/trailing whitespace is accepted when trimmed | Login page is open | 1. Enter standard_user with leading and trailing spaces in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login succeeds and redirects to the Product Inventory page if the system trims whitespace before authentication; if trimming is not performed, the login is blocked and the error banner 'Epic sadface: Username and password do not match any user in this service.' is shown. | medium |
| TC-014 (interaction_edge) | WF-001 | Rapid double-click of Login button produces a single successful submission | Login page is open | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Rapidly click the Login button twice in quick succession | Submission succeeds once; only a single redirect to the Product Inventory page occurs and no duplicate navigations or duplicate session effects are observed (no second successful login action is performed). | medium |

---

## Product Inventory

Total: **13** (positive: 4, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Product Detail from product name | User logged in as <role>, Product Inventory page is reachable with at least one product <product> | 1. Navigate to the Product Inventory page<br>2. Click the <product> name (or image) in the product list | navigates to Product Detail page (triggered by clicking product name or image) | high |
| TC-002 | WF-002 | Add product to cart from product list (NotInCart → InCart) | User logged in as <role>, <product> is in state NotInCart and is visible in the Product Inventory list | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' on the row for <product> | adds item to cart; changes row action to 'Remove'; updates cart badge count | high |
| TC-003 | WF-003 | Remove product from cart from product list (InCart → NotInCart) | User logged in as <role>, <product> is in state InCart and is visible in the Product Inventory list | 1. Navigate to the Product Inventory page<br>2. Click 'Remove' on the row for <product> | removes item from cart; changes row action to 'Add to cart'; updates cart badge count | high |
| TC-004 |  | Sort product list by Price (Low–High) | User logged in as <role>, Product Inventory page lists multiple products with prices | 1. Navigate to the Product Inventory page<br>2. Open the Sort dropdown<br>3. Select 'Price (Low–High)' from the Sort dropdown | Product table rows are ordered by Price (Low–High); the product list displays items sorted with lower-priced products before higher-priced products | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user cannot access Product Inventory page | User is not authenticated | 1. Open the Product Inventory page URL in a browser as an unauthenticated user | User is redirected to the login page; Product Inventory page is not shown; page displays the login prompt (e.g., 'Sign in' or equivalent). | high |
| TC-006 | WF-001 | Unauthenticated user cannot open Product Detail page by clicking product name/image | User is not authenticated, A product exists in the catalog | 1. Open the Product Inventory page URL in a browser as an unauthenticated user<br>2. Click the product name or product image for any listed product | User is redirected to the login page instead of the Product Detail page; Product Detail page is not displayed; a login prompt is shown. | high |
| TC-007 | WF-003 | Attempt to Remove an item when product is NotInCart (wrong-state action) | User is authenticated, A product exists and its product_state is NotInCart, Cart badge count is known (capture current value as <initial cart count>) | 1. Open the Product Inventory page while signed in<br>2. Locate the row for the product whose state is NotInCart<br>3. Attempt to locate and click a 'Remove' action/button in that product's row | No 'Remove' button is visible or clickable for that product; clicking a non-existent 'Remove' is not possible; product remains in NotInCart state; cart badge remains unchanged at <initial cart count>; no removal action is performed. | high |
| TC-008 | WF-002 | Attempt to 'Add to cart' when product is already InCart (wrong-state action) | User is authenticated, A product exists and its product_state is InCart, Cart badge count is known (capture current value as <initial cart count>) | 1. Open the Product Inventory page while signed in<br>2. Locate the row for the product whose state is InCart<br>3. Attempt to locate and click an 'Add to cart' button in that product's row | No 'Add to cart' button is visible or clickable for that product; clicking a non-existent 'Add to cart' is not possible; product remains in InCart state; cart badge remains unchanged at <initial cart count>; no duplicate add action is performed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Add first product to an empty cart (boundary from zero to non-zero) | User is logged in, Product list page is open, Cart is empty (cart badge is hidden or shows zero) | 1. Locate a product row that shows 'Add to cart' (product is in NotInCart state)<br>2. Click the 'Add to cart' button for that product | Click succeeds: the product row action changes to 'Remove' and the cart badge becomes visible with count equal to <minimum non-zero count>; UI shows the cart badge and the row now displays 'Remove'. | medium |
| TC-010 (boundary) | WF-003 | Remove the last product from the cart (boundary from non-zero to zero) | User is logged in, Product list page is open, A single product is already in the cart (row shows 'Remove' and cart badge shows <minimum non-zero count>) | 1. Click the 'Remove' button on the product that is currently in the cart | Click succeeds: the product row action changes to 'Add' and the cart badge is removed or shows <zero>; the UI no longer displays the non-zero cart count and the row displays 'Add'. | medium |
| TC-011 (state_edge) | WF-002 | Rapid double-click on 'Add to cart' (prevent duplicate adds) | User is logged in, Product list page is open, Target product is in NotInCart state and cart has no entry for this product | 1. Focus the target product row<br>2. Perform two rapid clicks on the 'Add to cart' button (two clicks within ~1 second) | First click succeeds and adds the product; the second immediate click is blocked/ignored: the cart badge increments by exactly <minimum non-zero count> only once and the row action changes to 'Remove' (no duplicate entries created). The UI shows the button disabled or unchanged during the second click and no additional increment occurs. | medium |
| TC-012 (interaction_edge) | WF-002 | Add to cart, navigate to Product Detail, press browser Back, then attempt Add again (history-induced duplicate prevention) | User is logged in, Product list page is open, Target product is in NotInCart state | 1. Click 'Add to cart' for the target product<br>2. Click the product name or image to open the Product Detail page<br>3. Use the browser back button to return to the Product List page<br>4. Observe the row action for the same product and, if it shows 'Add', click it | Navigation and history do not create duplicates: after returning from the Product Detail page the row should reflect the current cart state (it should show 'Remove' if the product is already added). If the tester clicks 'Add' again, that second add is blocked/ignored and the cart badge reflects only the original add (no extra increments). The UI shows 'Remove' for an already-added product or prevents a second add, and no duplicate cart entry is created. | medium |
| TC-013 (state_edge) |  | Click Add then immediately click Remove (rapid consecutive state transitions) | User is logged in, Product list page is open, Target product is in NotInCart state; cart does not contain this product | 1. Click 'Add to cart' on the target product<br>2. Immediately click 'Remove' on the same product before the cart badge visible update completes | Rapid consecutive transitions result in a consistent final state: the UI settles to the state corresponding to the last successful action (after Add then Remove the final state is NotInCart). The cart badge shows no net change (returns to <zero or hidden>), the row displays 'Add', and no duplicate or inconsistent entries appear. The rapid transitions are handled without producing an incorrect cart count. | medium |

---

## Product Detail

Total: **11** (positive: 4, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User logged in as <role>, Product Detail page is open for <target product> and product is in Not_In_Cart state | 1. Click the 'Add to cart' button in the Product Action Bar | Button label changes to 'Remove' on the Product Detail page (on_success: adds product to cart) | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User logged in as <role>, Product Detail page is open for <target product> and product is in In_Cart state | 1. Click the 'Remove' button in the Product Action Bar | Button label changes to 'Add to cart' on the Product Detail page (on_success: removes product from cart) | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via Back to products link | User logged in as <role>, Product Detail page is open for <target product> | 1. Click the 'Back to products' link | Product Inventory page is displayed (on_success: navigates to Product Inventory page) | medium |
| TC-004 | WF-004 | Open Shopping Cart via Cart Icon from Product Detail | User logged in as <role>, Product Detail page is open for <target product> | 1. Click the Cart Icon link in the page header | Shopping Cart page is displayed (on_success: navigates to Shopping Cart) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-002 | Attempt 'Remove' action when product is Not_In_Cart | User is logged in (if required) and is on the Product Detail page for <product>, The <product> is in state Not_In_Cart (not present in the shopping cart) | 1. Ensure the Product Detail page for <product> is open and the product is Not_In_Cart<br>2. Attempt to locate the 'Remove' button on the page<br>3. If the 'Remove' button is visible, click the 'Remove' button | The 'Remove' button is not visible (or is rendered disabled) on the Product Detail page when the product is in state Not_In_Cart; clicking the control is not possible / has no effect. The product remains in state Not_In_Cart and no item is removed from the shopping cart; no state transition or navigation occurs. | high |
| TC-006 | WF-001 | Attempt 'Add to cart' action when product is already In_Cart | User is logged in (if required) and is on the Product Detail page for <product>, The <product> is in state In_Cart (already present in the shopping cart) | 1. Ensure the Product Detail page for <product> is open and the product is In_Cart<br>2. Attempt to locate the 'Add to cart' button on the page<br>3. If the 'Add to cart' button is visible, click the 'Add to cart' button | The 'Add to cart' button is not visible (or is rendered disabled) on the Product Detail page when the product is in state In_Cart; clicking the control is not possible / has no effect. The product remains in state In_Cart and no duplicate item is added to the shopping cart; no state transition or navigation occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (state_edge) | WF-001 | Rapid double-click on Add to cart results in single add | Product Detail page is open for a product currently in state Not_In_Cart | 1. Verify the action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. Immediately click the 'Add to cart' button again (second click within ~500ms).<br>4. Click the Cart Icon to open the Shopping Cart. | First Add action succeeds; the second rapid click is blocked. Visible outcome: the Product Detail button label changes to 'Remove' and the Shopping Cart shows the product exactly once (no duplicate entries). | medium |
| TC-008 (state_edge) |  | Quick consecutive Add then Remove transitions return to original state | Product Detail page is open for a product currently in state Not_In_Cart | 1. Verify the action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. As soon as the button label updates to 'Remove', click the 'Remove' button. | Both state transitions succeed. Visible outcome: after the rapid Remove, the button label returns to 'Add to cart' and the product is not present in the Shopping Cart (final state is Not_In_Cart). | medium |
| TC-009 (state_edge) | WF-002 | Remove action is not available when product is Not_In_Cart | Product Detail page is open for a product currently in state Not_In_Cart | 1. Verify the action button label reads 'Add to cart'.<br>2. Inspect the action area for a 'Remove' button (attempt to find or focus it). | Remove action is blocked / not available. Visible outcome: no 'Remove' button is present or it is disabled, and no state change occurs (product remains Not_In_Cart and Shopping Cart remains unchanged). | medium |
| TC-010 (interaction_edge) | WF-003 | State persistence across Back to products navigation and re-open | Product Detail page is open for a product currently in state Not_In_Cart | 1. Verify the action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. Click the 'Back to products' link.<br>4. From the Product Inventory page, open the same product's Product Detail page. | Add action succeeds and state persists across navigation. Visible outcome: the reopened Product Detail shows the action button as 'Remove' and the Shopping Cart (when opened) contains the product. | medium |
| TC-011 (interaction_edge) | WF-004 | Navigate to Shopping Cart while Add to cart transition is in-flight | Product Detail page is open for a product currently in state Not_In_Cart | 1. Verify the action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. Immediately click the Cart Icon to navigate to the Shopping Cart before waiting for any UI confirmation on Product Detail. | Navigation to Shopping Cart succeeds and Add completes. Visible outcome: the Shopping Cart page opens and displays the product (Add action succeeded); Product Detail would show 'Remove' if returned to. | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the Cart Items table | User logged in as <role>, Shopping Cart contains at least one item with description <item description> | 1. Navigate to the Shopping Cart page<br>2. Locate the row for <item description> in the Cart Items table<br>3. Click the Remove button for <item description> | The Cart Items table no longer displays a row for <item description>; remaining cart rows (if any) are still visible | high |
| TC-002 | WF-002 | Continue shopping navigates to Product Inventory | User logged in as <role>, Shopping Cart page is open | 1. Click the 'Continue Shopping' link in the Cart Page Actions bar | The Product Inventory page is displayed | medium |
| TC-003 | WF-003 | Begin checkout from Cart | User logged in as <role>, Shopping Cart page is open with at least one item | 1. Click the 'Checkout' button in the Cart Page Actions bar | The Checkout page is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Shopping Cart | User is not logged in / no authenticated session | 1. Open the Shopping Cart page at <Shopping Cart URL> | Access is blocked: the user is redirected to the login page; the Login page is displayed (login form visible) and the Shopping Cart content (cart items table and action bar) is not shown. The Shopping Cart is not accessible without authentication. | high |
| TC-005 | WF-002 | Continue Shopping link does not navigate to Product Inventory | User is on the Shopping Cart page with at least one item listed in the cart | 1. Click the 'Continue Shopping' link in the Cart_Page_Actions | Navigation is blocked: clicking 'Continue Shopping' does not load the Product Inventory page; the Shopping Cart page remains visible and the browser URL remains <Shopping Cart URL>. No Product Inventory content is displayed and no navigation to <Product Inventory URL> occurs. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click Remove on the same item row | User is signed in (if required), Cart contains a visible row for the test product (at least one item present) | 1. Navigate to the Shopping Cart page<br>2. Locate the row for the test product<br>3. Click the row's Remove button<br>4. Immediately click the same row's Remove button again | First Remove click succeeds: the item's row is removed and the Remove button for that row is no longer present. The second Remove attempt is blocked / error shown (the UI ignores the second click or the Remove action is disabled) and no additional change to cart contents occurs (no negative quantity or duplicate removals). | medium |
| TC-007 (state_edge) | WF-003 | Remove the last item then immediately click Checkout | User is signed in (if required), Cart contains exactly one visible item row | 1. Navigate to the Shopping Cart page<br>2. Click the single item's Remove button<br>3. Immediately click the Checkout button in the action bar | Removal of the last item succeeds: the cart shows no item rows. The immediate Checkout attempt is blocked / error shown: the system does not begin the checkout process when the cart is empty (the user remains on the cart page and Checkout is disabled or ignored). | medium |
| TC-008 (interaction_edge) | WF-002 | Continue Shopping then press browser Back — cart state preservation and no duplicate items | User is signed in (if required), Cart contains multiple visible item rows (two or more items) | 1. Navigate to the Shopping Cart page<br>2. Note the number of visible item rows and their descriptions<br>3. Click Continue Shopping<br>4. On the Product Inventory page, press the browser Back button | Navigation to Product Inventory succeeds and returning via browser Back succeeds: the Shopping Cart page is shown with the same items and same count as before navigation (no duplicate rows were added and no items were lost). | low |
| TC-009 (state_edge) | WF-003 | Rapid double-click Checkout (prevent duplicate checkout start) | User is signed in (if required), Cart contains at least one visible item row | 1. Navigate to the Shopping Cart page<br>2. Click the Checkout button<br>3. Immediately click the Checkout button again | First Checkout click succeeds: the UI begins the checkout process and navigates to the Checkout page. The second Checkout click is blocked / error shown (the UI ignores the second click or disables the Checkout action) and no duplicate checkout/navigation occurs (user remains on a single checkout flow). | medium |

---

## Checkout - Information

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with all required fields filled proceeds to overview | User logged in as <role>, Checkout - Information page is open with items ready for checkout | 1. Enter <first name> in the First Name field<br>2. Enter <last name> in the Last Name field<br>3. Enter <postal code> in the Postal Code field<br>4. Click the Continue button | proceeds to overview step | high |
| TC-002 | WF-002 | Click Continue with all required fields missing shows error banner with field-specific messages | User logged in as <role>, Checkout - Information page is open | 1. Ensure First Name field is empty<br>2. Ensure Last Name field is empty<br>3. Ensure Postal Code field is empty<br>4. Click the Continue button | displays error banner with field-specific messages: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required' | high |
| TC-003 | WF-003 | Click Cancel returns to Shopping Cart | User logged in as <role>, Checkout - Information page is open | 1. Click the Cancel button | returns to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Continue blocked when First Name is missing (other fields present) | User is on the Checkout - Information page | 1. Enter <valid Last Name> in the Last_Name field<br>2. Enter <valid Postal Code> in the Postal_Code field<br>3. Leave the First_Name field blank<br>4. Click the Continue button | Form does not submit; user remains on Checkout - Information page; an error banner is shown and the First_Name field displays an error: 'Error: First Name is required'. | high |
| TC-005 |  | Continue blocked when Last Name is missing (other fields present) | User is on the Checkout - Information page | 1. Enter <valid First Name> in the First_Name field<br>2. Enter <valid Postal Code> in the Postal_Code field<br>3. Leave the Last_Name field blank<br>4. Click the Continue button | Form does not submit; user remains on Checkout - Information page; an error banner is shown and the Last_Name field displays an error: 'Error: Last Name is required'. | high |
| TC-006 |  | Continue blocked when Postal Code is missing (other fields present) | User is on the Checkout - Information page | 1. Enter <valid First Name> in the First_Name field<br>2. Enter <valid Last Name> in the Last_Name field<br>3. Leave the Postal_Code field blank<br>4. Click the Continue button | Form does not submit; user remains on Checkout - Information page; an error banner is shown and the Postal_Code field displays an error: 'Error: Postal Code is required'. | high |
| TC-007 | WF-002 | Continue blocked when all required fields are empty | User is on the Checkout - Information page | 1. Leave the First_Name field blank<br>2. Leave the Last_Name field blank<br>3. Leave the Postal_Code field blank<br>4. Click the Continue button | Form does not submit; user remains on Checkout - Information page; an error banner is shown containing all three messages: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required'. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Required fields filled with only whitespace characters are treated as missing | User is on the Checkout - Information page | 1. Enter only whitespace characters in the First_Name field<br>2. Enter only whitespace characters in the Last_Name field<br>3. Enter only whitespace characters in the Postal_Code field<br>4. Click the Continue button | Submission is blocked; an error banner is shown with the field-specific messages: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required'. | medium |
| TC-009 (input_edge) | WF-001 | Very long input (>200 characters) in name and postal code fields | User is on the Checkout - Information page | 1. Enter a very long string (>200 characters) in the First_Name field<br>2. Enter a very long string (>200 characters) in the Last_Name field<br>3. Enter a very long string (>200 characters) in the Postal_Code field<br>4. Click the Continue button | Either the submission succeeds and the flow proceeds to the overview step (succeeds), or the Continue action is blocked and a visible validation indicator (inline error or banner) is shown indicating the field(s) exceed the maximum allowed length. | medium |
| TC-010 (input_edge) | WF-001 | Names and postal code containing emoji, non-Latin unicode and special characters | User is on the Checkout - Information page | 1. Enter emoji and other special/unicode characters in the First_Name field<br>2. Enter emoji and other special/unicode characters in the Last_Name field<br>3. Enter emoji and other special/unicode characters in the Postal_Code field<br>4. Click the Continue button | Form submits successfully and proceeds to the overview step (succeeds); the overview step displays the entered characters as provided, or if characters are not allowed the Continue action is blocked and a visible validation message is shown. | medium |
| TC-011 (interaction_edge) | WF-001 | Browser Back after successful Continue then attempt to Continue again (rapid back-navigation) | User is on the Checkout - Information page | 1. Enter valid values in First_Name, Last_Name, and Postal_Code fields<br>2. Click the Continue button and confirm the app proceeds to the overview step<br>3. Use the browser Back button to return to the Checkout - Information page<br>4. Without changing values, click the Continue button again | Either the browser Back returns a blank Checkout form and the second Continue is blocked until required fields are re-entered (is blocked), or the app immediately returns to the overview and prevents a duplicate proceed; in either case the system prevents an accidental silent duplicate proceed (behavior succeeds in preventing duplicate automatic submission). | low |

---

## Checkout - Overview

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout from Overview navigates to confirmation | User logged in as <role>, User has at least one item in the cart and is on the Checkout Overview page which displays an order summary with Item total, Tax, Total, and payment and shipping information | 1. On the Checkout Overview page, click the Finish button | completes order and navigates to confirmation page | high |
| TC-002 | WF-002 | Cancel checkout from Overview exits checkout | User logged in as <role>, User has at least one item in the cart and is on the Checkout Overview page which displays an order summary with Item total, Tax, Total, and payment and shipping information | 1. On the Checkout Overview page, click the Cancel button | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user cannot access Checkout Overview | User is not authenticated (not logged in) | 1. Open the Checkout Overview page URL | User is redirected to the Login page; Checkout Overview is not displayed and Finish/Cancel actions are not available. | high |
| TC-004 | WF-001 | User without checkout permission cannot complete order by clicking Finish | Logged in as <unauthorized role> (does not have permission to complete orders) | 1. Log in as <unauthorized role><br>2. Navigate to the Checkout Overview page<br>3. Click the Finish button | Finish action is blocked; order is not completed; user remains on Checkout Overview (no navigation to confirmation page); an authorization error is displayed (e.g., visible banner or modal indicating insufficient permissions). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-001 | Rapid double-click on Finish during Overview (prevent duplicate order) | User is signed in, Cart contains items and totals are displayed on the Overview step, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Immediately (within one second) click the Finish button again | First click succeeds: confirmation page is displayed and the Finish button becomes disabled/indicates processing; the second click is blocked / ignored and does not create a second order. Only one order appears in the user's order history and only one confirmation page is produced. | medium |
| TC-006 (interaction_edge) | WF-001 | Finish, then press browser Back and attempt Finish again (no duplicate creation) | User is signed in, Cart contains items and totals are displayed on the Overview step, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Wait until the confirmation page is displayed<br>3. Use the browser Back button to return to the Checkout - Overview step<br>4. Click the Finish button again | First Finish succeeds and confirmation page was previously shown. After navigating back and clicking Finish again, the second submission is blocked / ignored; no duplicate order is created and the user is either redirected to the same confirmation page for the original order or shown a message indicating the order has already completed. | medium |
| TC-007 (interaction_edge) | WF-001 | Click Finish while network is offline (network-failure during submit) | User is signed in, Cart contains items and totals are displayed on the Overview step, User is on the Checkout - Overview step | 1. Disable the browser/network connectivity (simulate offline)<br>2. Click the Finish button | The submission is blocked / error shown: an error banner or inline error appears indicating the order could not be completed due to a network error; no order is created. The Finish button remains available (or shows retry) so the user can attempt submission again after connectivity is restored. | medium |
| TC-008 (interaction_edge) | WF-002 | Click Cancel immediately after clicking Finish (race between Finish and Cancel) | User is signed in, Cart contains items and totals are displayed on the Overview step, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Immediately click the Cancel button while the Finish request is still in progress | The Cancel action is blocked while submission is in-flight: the initial Finish succeeds and the user is navigated to the confirmation page. The Cancel click does not abort the in-progress submit and does not exit checkout. | low |

---

## Checkout - Confirmation

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Back Home redirects to Product Inventory and clears cart | User logged in as <Customer>, Confirmation page is open after completing checkout and shows the order success message | 1. On the Confirmation page, verify the Back Home button is visible<br>2. Click the Back Home button | Browser navigates to the Product Inventory page; the shopping cart is visibly empty (no items). (on_success: redirects to Product Inventory and clears cart) | high |
| TC-002 |  | Confirmation page displays order success message | User logged in as <Customer> | 1. Navigate to the Confirmation page (e.g., complete checkout flow to reach this page)<br>2. Observe the page content | A prominent order success message is displayed on the Confirmation page (for example: "Thank you for your order!") and the Back Home button is visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user cannot view Confirmation page | User is not logged in / unauthenticated | 1. Navigate directly to the Confirmation page URL (e.g. the order confirmation route) | Access is blocked: user is redirected to the Login page; Confirmation page content (the success message and the 'Back Home' button) is not shown | high |
| TC-004 | WF-001 | 'Back Home' button is non-functional and does not clear the cart | User has completed checkout and is currently on the Confirmation page, Shopping cart should have been cleared by the checkout success flow (precondition expectation) | 1. On the Confirmation page, click the 'Back Home' button | Action is blocked / fails: clicking the 'Back Home' button does not navigate to Product Inventory (user remains on Confirmation page) and the cart remains populated (items are still present in the cart) | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Back Home causes duplicate navigation or duplicate cart-clear | User has completed checkout and is shown the Confirmation Page with the success message visible, Cart is in the post-checkout state (items pending clear on Back Home action) | 1. On the Confirmation Page, click the Back Home button<br>2. Immediately click the Back Home button a second time (within one second of the first click) | The first click redirects to Product Inventory and clears the cart; the second click is ignored and does not create a duplicate action. Product Inventory is displayed and the cart shows as empty — action succeeds. | medium |
| TC-006 (interaction_edge) | WF-001 | Browser Back after returning home does not restore cart contents or re-trigger order | User has completed checkout and is shown the Confirmation Page with the success message visible, Cart contains items until Back Home is clicked | 1. On the Confirmation Page, click the Back Home button<br>2. On Product Inventory (after redirect), click the browser Back button once | Browser Back navigates to the Confirmation Page (success message visible) but the cart remains cleared; no items reappear in the cart and no new order can be generated from that page — the cart-empty indicator is visible on Product Inventory and the overall flow succeeds. | medium |
| TC-007 (input_edge) |  | Confirmation message contains very long text (200+ chars) — rendering / truncation behavior | User completes checkout and is shown the Confirmation Page, The confirmation message contains an unusually long message or reference text (e.g., 200+ characters) | 1. Observe the confirmation message area on the Confirmation Page | The confirmation message renders without breaking the page layout: the full text is visible via wrapping or a visible scroll area and does not overlap other UI elements. The message display succeeds and there is no visual overflow or unreadable content. | low |

---

## Logout

Total: **8** (positive: 1, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Logout button redirects to Login page and prevents access to protected pages | User logged in as <role> | 1. Click the 'Logout' button | ends session and redirects to login page; protected pages (inventory, detail, cart, checkout) are not accessible without logging in again | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt Logout when not logged in — Logout control should not be available | User is not authenticated (no active session) | 1. Open the application main page while not logged in<br>2. Look for the Logout button in the header/navigation<br>3. If the Logout button appears, attempt to click it | Logout button is not present or is disabled for unauthenticated users; clicking is not possible. No logout action occurs and the user remains not authenticated; page continues to show login/sign-in controls or a public view. | high |
| TC-003 | WF-001 | Directly navigate to Logout endpoint without an active session — should be blocked/redirected | User is not authenticated (no active session) | 1. In the browser address bar, navigate to the application's logout endpoint: <logout URL> | Browser is redirected to the Login page; the Login page (login form) is displayed and no session is created or modified. The attempted logout does not produce an authenticated session or access to protected content. | high |
| TC-004 | WF-001 | Access protected pages (inventory, detail, cart, checkout) without logging in — access must be blocked | User is not authenticated (no active session) | 1. Navigate to the inventory page: <inventory URL><br>2. Navigate to a product detail page: <detail URL><br>3. Navigate to the cart page: <cart URL><br>4. Navigate to the checkout page: <checkout URL> | For each protected page navigation, the user is redirected to the Login page and the protected content is not displayed; the Login form is shown and access is blocked until authentication. No protected page content is visible at any step. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Logout button | User is logged in and a protected page is visible | 1. Click the Logout button once<br>2. Immediately click the Logout button again before the first redirect completes | First click succeeds: session ends and user is redirected to the login page. Second click is ignored (no second session change or duplicate redirect); login page remains visible and no error is shown. | medium |
| TC-006 (state_edge) | WF-001 | Click Logout after server-side session expiry while UI still shows logged-in state | User is logged in and displayed as logged in in the UI | 1. Wait until the server-side session TTL expires (UI still shows logged-in state)<br>2. Click the Logout button | Clicking Logout succeeds: user is redirected to the login page and any attempt to access protected pages is blocked; no server error is shown in the UI. | medium |
| TC-007 (interaction_edge) | WF-001 | Browser Back after logout attempts to show protected page | User is logged in and on a protected page | 1. Click the Logout button<br>2. After being redirected to the login page, click the browser Back button | Navigation to the protected page is blocked / error shown: either the browser shows the login page or the protected page reloads and immediately redirects to the login page; protected content is not accessible. | medium |
| TC-008 (interaction_edge) | WF-001 | Open protected page in new tab after logout using direct URL | User is logged in | 1. Click the Logout button<br>2. Open a new browser tab<br>3. Enter the URL of a protected page (e.g., inventory) in the address bar and press Enter | Access to the protected page is blocked / error shown: the new tab displays the login page (or an equivalent authentication prompt) and protected content is not shown. | low |

---

## Reset App State

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Reset App State clears cart and resets add/remove button states without logging out | User logged in as <role>, Cart contains at least one item and at least one item action button currently shows the 'Remove' state | 1. Open the main app page containing the cart and product listing<br>2. Observe that the cart badge indicates items are present and at least one product action button shows the 'Remove' state<br>3. Click the 'Reset App State' button | Cart list displays no items and the cart badge is not visible; product action buttons that previously showed 'Remove' now show the default 'Add' state; the user remains logged in (user avatar or Logout button is visible). | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to invoke Reset App State | User is not authenticated (no active session) | 1. Navigate to the screen where the Reset App State button is exposed<br>2. Click the Reset App State button | User is redirected to the Login page (login screen is displayed) and the Reset App State action is not executed; the cart and in-app state remain unchanged (cart contents and cart badge remain as before). | high |
| TC-003 | WF-001 | Reset App State must not log the user out | User is authenticated and signed in, User has items in the cart and non-default in-app states (e.g., add/remove buttons in 'Added' state and cart badge > 0) | 1. Click the Reset App State button | Reset App State runs but does not log the user out: the cart is cleared and in-app UI is reset (cart badge resets, add/remove buttons return to initial state) AND the user remains signed in (user avatar/name remains visible and user session is active). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (state_edge) | WF-001 | Press Reset when cart already empty | User is logged in, Cart is empty (no items in cart; cart badge cleared/hidden) | 1. Verify the cart is empty and cart badge is not showing<br>2. Click the 'Reset App State' button | Reset App State action succeeds; cart remains empty (cart badge stays cleared/hidden), add/remove button states are reset to their default 'Add' state, and the user remains logged in (user avatar/name remains visible). No error is shown. | medium |
| TC-005 (interaction_edge) | WF-001 | Rapid double-press of Reset button | User is logged in, Cart contains at least one item (cart badge shows items) | 1. Confirm cart contains items and cart badge is visible<br>2. Click the 'Reset App State' button<br>3. Immediately (within a second) click the 'Reset App State' button again | First Reset click succeeds clearing the cart and resetting UI; the immediate second click also succeeds harmlessly (no error shown) and does not re-add items or leave the UI in an inconsistent state. Final visible state: cart cleared (badge cleared/hidden), add/remove buttons in default 'Add' state, and user remains logged in. | medium |
| TC-006 (state_edge) | WF-001 | Press Reset while an item add is in progress | User is logged in, Cart may be empty or contain items, There is an item that can be added via the in-app 'Add' control | 1. Click 'Add' for an item to start the add operation (do not wait for any asynchronous completion indicator to finish)<br>2. While the add operation is in progress, click the 'Reset App State' button<br>3. Wait for UI operations to settle (any spinners or progress indicators finish) | Reset App State action succeeds and final UI shows cart cleared (cart badge cleared/hidden) and add/remove buttons returned to their default 'Add' state. Any pending add does not leave an item in the cart. The user remains logged in and no error is shown. | medium |
| TC-007 (interaction_edge) | WF-001 | Press Reset while device is offline | User is logged in, Cart contains at least one item, App is put into offline mode (network disconnected) from the UI or system settings | 1. Confirm app indicates offline state (offline banner or system network disabled)<br>2. Click the 'Reset App State' button | Reset App State action succeeds locally while offline: cart is cleared (cart badge cleared/hidden) and in-app UI states (add/remove buttons) are reset to default. User remains logged in locally (session not cleared) and no server error modal is shown. If the app surfaces that the action will be synchronized when online, that indicator is visible. | medium |

---
