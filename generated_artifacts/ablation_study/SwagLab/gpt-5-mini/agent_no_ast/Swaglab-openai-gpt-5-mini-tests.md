# Test Cases — Swaglab

Generated: 2026-06-10T18:43:00.887191Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 85 | 32 | 24 | 29 | 36 | 39 | 10 |

## Login

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid test user (standard_user) | User at Login page, User role: <role> | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | System authenticates and redirects to the Product Inventory page. | high |
| TC-002 | WF-002 | Login attempt with empty Username shows required error | User at Login page, User role: <role> | 1. Leave the Username field empty<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-003 | WF-003 | Login attempt with empty Password shows required error | User at Login page, User role: <role> | 1. Enter standard_user in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |
| TC-004 | WF-004 | Login attempt by locked out user shows locked out error | User at Login page, User role: <role> | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-005 | WF-005 | Login attempt with invalid credentials shows mismatch error | User at Login page, User role: <role> | 1. Enter standard_user in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Submit with Username blank (Password provided) | User is on the Login page | 1. Leave the Username field blank<br>2. Enter <secret_sauce> in the Password field<br>3. Click the Login button | An error banner displays: "Epic sadface: Username is required."; the login is blocked and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-007 | WF-003 | Submit with Password blank (Username provided) | User is on the Login page | 1. Enter <valid test username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | An error banner displays: "Epic sadface: Password is required."; the login is blocked and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-008 |  | Submit with all required fields blank | User is on the Login page | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | An error banner displays: "Epic sadface: Username is required."; the login is blocked and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-009 | WF-004 | Locked-out test user cannot login | User is on the Login page | 1. Enter <locked_out_user> in the Username field<br>2. Enter <secret_sauce> in the Password field<br>3. Click the Login button | An error banner displays: "Epic sadface: Sorry, this user has been locked out."; the login is blocked and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-010 | WF-005 | Valid username with incorrect password is rejected | User is on the Login page | 1. Enter <valid test username> in the Username field<br>2. Enter <incorrect password> in the Password field (value not equal to <secret_sauce>)<br>3. Click the Login button | An error banner displays: "Epic sadface: Username and password do not match any user in this service."; the login is blocked and the user remains on the Login page (no redirect to Product Inventory). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) | WF-001 | Username with leading and trailing whitespace | Login page is displayed | 1. Enter username with leading and trailing whitespace (e.g. ' standard_user ') in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login succeeds; form submits successfully and system authenticates and redirects to the Product Inventory page | medium |
| TC-012 (input_edge) | WF-005 | Username with different letter casing (case-sensitivity check) | Login page is displayed | 1. Enter the valid username with altered case (e.g. 'Standard_User') in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; error banner displays: "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-013 (input_edge) | WF-005 | Very long Username input (200+ characters) | Login page is displayed | 1. Enter a very long string (200+ characters) in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; error banner displays: "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-014 (interaction_edge) | WF-002 | Browser Back after successful login then attempt submit with empty fields | Login page is displayed | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button<br>4. After redirect to the Product Inventory page, click the browser Back button<br>5. Click the Login button without entering Username or Password | Second submission is blocked; error banner displays: "Epic sadface: Username is required." | low |

---

## Product Inventory

Total: **14** (positive: 8, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add a product to cart from Product Inventory list | User logged in as <role>, Multiple products exist in the inventory including <target product> | 1. Navigate to the Product Inventory page<br>2. Locate the row/card for <target product> in the product list<br>3. Click the 'Add to cart' button on the <target product> row/card | Item added to cart; the button changes to "Remove"; cart badge count updates accordingly. | high |
| TC-002 | WF-002 | Remove a product from cart from Product Inventory list | User logged in as <role>, <target product> is already in the cart and appears on the Product Inventory page with a 'Remove' button | 1. Navigate to the Product Inventory page<br>2. Locate the row/card for <target product> which shows the 'Remove' button<br>3. Click the 'Remove' button on the <target product> row/card | Item removed from cart; the button changes back to "Add to cart"; cart badge count updates accordingly. | high |
| TC-003 | WF-003 | Open Product Detail by clicking product name | User logged in as <role>, Multiple products exist in the inventory including <target product> | 1. Navigate to the Product Inventory page<br>2. Click the product name for <target product> in the product list | Product Detail page opens for the selected product. | high |
| TC-004 | WF-004 | Open Product Detail by clicking product image | User logged in as <role>, Multiple products exist in the inventory including <target product> | 1. Navigate to the Product Inventory page<br>2. Click the product image for <target product> in the product list | Product Detail page opens for the selected product. | high |
| TC-005 | WF-005 | Sort products by Name (A–Z) | User logged in as <role>, Product Inventory contains multiple products with varying names including <product with lower name> and <product with higher name> | 1. Navigate to the Product Inventory page<br>2. Open the sort dropdown<br>3. Select 'Name (A–Z)' from the sort options | Product list is sorted by name in ascending (A–Z) order. | medium |
| TC-006 | WF-006 | Sort products by Name (Z–A) | User logged in as <role>, Product Inventory contains multiple products with varying names including <product with lower name> and <product with higher name> | 1. Navigate to the Product Inventory page<br>2. Open the sort dropdown<br>3. Select 'Name (Z–A)' from the sort options | Product list is sorted by name in descending (Z–A) order. | medium |
| TC-007 | WF-007 | Sort products by Price (low–high) | User logged in as <role>, Product Inventory contains multiple products with varying prices including at least one <lower-priced product> and one <higher-priced product> | 1. Navigate to the Product Inventory page<br>2. Open the sort dropdown<br>3. Select 'Price (low–high)' from the sort options | Product list is sorted by price from low to high. | medium |
| TC-008 | WF-008 | Sort products by Price (high–low) | User logged in as <role>, Product Inventory contains multiple products with varying prices including at least one <lower-priced product> and one <higher-priced product> | 1. Navigate to the Product Inventory page<br>2. Open the sort dropdown<br>3. Select 'Price (high–low)' from the sort options | Product list is sorted by price from high to low. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Unauthenticated user cannot access Product Inventory page | User is not authenticated (not logged in) | 1. Open the application in a browser as an unauthenticated user<br>2. Navigate to the Product Inventory page | User is redirected to the Login page; the Login form (Email and Password fields and Sign In button) is visible; the Product Inventory list (product names, images, prices) is not displayed; no 'Add to cart' or 'Remove' buttons and no cart badge are visible — access to the inventory is blocked. | high |
| TC-010 |  | Unauthenticated user cannot open Product Detail page directly | User is not authenticated (not logged in) | 1. As an unauthenticated user, navigate directly to a Product Detail page for <product><br>2. Observe the resulting page | User is redirected to the Login page; Product Detail content (product name, image, description, price) is not displayed; the product page is blocked until the user signs in. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid double-click Add to cart prevents duplicate additions | User is logged in, Product Inventory page is visible, At least one product is shown with an "Add to cart" button and cart badge is visible, The selected product is not currently in the cart (button text = "Add to cart") | 1. Locate a visible product item with an "Add to cart" button<br>2. Click the product's "Add to cart" button<br>3. Immediately click the product's "Add to cart" button again (single click) | First click succeeds and adds the item: the product button changes to "Remove" and the cart badge increments by one. The second click is ignored (no second addition); cart badge does not increment a second time and only one cart entry appears for the product (UI shows a single changed button to "Remove"). | medium |
| TC-012 (interaction_edge) | WF-002 | Immediate toggle Add → Remove before UI update yields consistent final state | User is logged in, Product Inventory page is visible, At least one product is shown with an "Add to cart" button and cart badge is visible, The selected product is not currently in the cart (button text = "Add to cart") | 1. Locate a visible product item with an "Add to cart" button<br>2. Click the product's "Add to cart" button<br>3. Immediately (before visual state stabilizes) click the product's displayed "Remove" button (single click) | The sequence of rapid Add then Remove succeeds in producing a consistent final state: the product ends not in the cart (button shows "Add to cart") and the cart badge reflects the single net change (no phantom increments). There is no visible duplication of the item in the cart and the UI does not display an inconsistent intermediate state after actions complete. | medium |
| TC-013 (interaction_edge) | WF-007 | Repeated/rapid sort by Price (low–high) is deterministic (detect non-deterministic ordering) | User is logged in, Product Inventory page is visible, At least five products are listed so ordering can be observed, Cart contents are irrelevant | 1. Locate the sort dropdown on the Product Inventory page<br>2. Select the sort option Price (low–high)<br>3. Immediately re-select the sort option Price (low–high) (click) — repetition 1<br>4. Re-select the sort option Price (low–high) (click) — repetition 2<br>5. Re-select the sort option Price (low–high) (click) — repetition 3<br>6. Re-select the sort option Price (low–high) (click) — repetition 4<br>7. Observe and compare the visible product list order after each selection | Each sort action succeeds; the visible order of products after each repeated Price (low–high) selection is identical (deterministic). If any repetition yields a different visible order, that indicates non-deterministic sorting (test fails). | medium |
| TC-014 (input_edge) | WF-003 | Product name with very long length, leading/trailing whitespace, and special/unicode characters displays correctly on detail page | User is logged in, Product Inventory page is visible, A product exists whose displayed Name contains leading and/or trailing whitespace, includes special/unicode characters (e.g., emoji), and is a very long string (200+ characters) | 1. Locate the product in the list whose Name matches the described characteristics<br>2. Click the product Name to open the Product Detail page<br>3. Observe the Name as shown on the Product Detail page | Opening the Product Detail page succeeds; the product Name shown on the detail page preserves special/unicode characters and emoji, leading/trailing whitespace is trimmed in the saved/displayed value, and if the name exceeds visible width it is truncated with an ellipsis on the list but the full name is accessible/visible on the Product Detail page (detail page shows the full trimmed string). | low |

---

## Product Detail

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart from Product Detail page | User logged in as <role>, Product Detail page is open for <product> | 1. On the Product Detail page for <product>, verify the product image, name, description, and price are visible<br>2. Click the 'Add to cart' button | Product added to cart; page reflects updated cart state | high |
| TC-002 | WF-002 | Remove product from cart using Remove button on Product Detail page | User logged in as <role>, Product Detail page is open for <product>, The <product> is currently in the cart | 1. On the Product Detail page for <product>, verify the 'Remove' button is visible (reflecting current cart state)<br>2. Click the 'Remove' button | Product removed from cart; page reflects updated cart state | high |
| TC-003 | WF-003 | Return to Product Inventory via Back to products button | User logged in as <role>, Product Detail page is open for <product> | 1. On the Product Detail page for <product>, click the 'Back to products' button | Returns to the Product Inventory page | medium |
| TC-004 | WF-004 | Open Shopping Cart by clicking cart icon on Product Detail page | User logged in as <role>, Product Detail page is open for <product> | 1. On the Product Detail page for <product>, click the cart icon in the header/navigation | Navigates to the Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to add product that is already in the cart (duplicate add) | User is logged in, <product> already exists in the user's shopping cart | 1. Navigate to the Product Detail page for <product><br>2. If the action button displays 'Add to cart', click the 'Add to cart' button | Action is blocked: an inline error message appears adjacent to the action button indicating the product is already in the cart; the Shopping Cart contents do not change (no duplicate item or increased quantity); the page remains on the Product Detail for <product> | high |
| TC-006 | WF-003 | Back to products button does not navigate to Product Inventory | User is logged in, User is on the Product Detail page for <product> | 1. Click the 'Back to products' button | Navigation is blocked: the page remains on the Product Detail for <product>; a visible global or inline error banner appears indicating navigation to the Product Inventory failed; no return to the Product Inventory page occurs | medium |
| TC-007 | WF-004 | Clicking the cart icon fails to open the Shopping Cart | User is logged in, User is on the Product Detail page for <product> | 1. Click the cart icon in the page header | Navigation is blocked: the page remains on the Product Detail for <product>; a visible global error banner or toast appears indicating the Shopping Cart could not be opened; no navigation to the Shopping Cart page occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Very long product name and description rendering | A product exists whose name is a very long string (200+ characters) and whose description is a very long string (2000+ characters) | 1. Navigate to the Product Detail page for the product with the very long name/description<br>2. Observe the product name area<br>3. Observe the product description area<br>4. Verify visibility and usability of the Add to cart and Back to products buttons | The Product Detail page displays the full product name and description (wrapped or scrollable) without visual overflow or overlap; Add to cart and Back to products buttons remain visible and usable. Page layout does not break and text is not truncated abruptly — succeeds | low |
| TC-009 (interaction_edge) | WF-001 | Rapid double-clicking Add to cart (debounce/dedup) | A product exists that is not currently in the cart and the Product Detail page is reachable | 1. Navigate to the Product Detail page for the product<br>2. Click the Add to cart button<br>3. Immediately (within one second) click the Add to cart button again<br>4. Click the cart icon to open the Shopping Cart page | Only one unit of the product is added to the cart (no duplicate entries). The cart icon's quantity indicator increments by 1; the Shopping Cart page shows a single line item for the product with quantity 1; the Product Detail page's Add to cart button changes to 'Remove'. No duplicate entries are created — succeeds | medium |
| TC-010 (data_edge) |  | Product detail with missing/broken image URL | A product exists whose image URL is broken or returns 404 | 1. Navigate to the Product Detail page for the product with the broken image<br>2. Observe the image area<br>3. Observe that product name, description, price, Add to cart and Back to products buttons are present | A visible placeholder image or descriptive alt text is shown in place of the missing image; product name, description, price, Add to cart and Back to products buttons remain visible and usable. No JavaScript errors are shown to the user and page functionality remains available — succeeds | low |

---

## Shopping Cart

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <role>, Shopping Cart page is open with <item in cart> present and quantity shown as 1 | 1. On the Shopping Cart page, locate the row for <item in cart><br>2. Click the 'Remove' button for <item in cart> | Item removed from cart; cart updated — The Shopping Cart no longer displays <item in cart> and the cart item count/summary visibly updates to reflect the removed item | high |
| TC-002 | WF-002 | Continue shopping returns user to Product Inventory | User logged in as <role>, Shopping Cart page is open with at least one <item in cart> | 1. Click the 'Continue Shopping' button on the Shopping Cart page | Return to Product Inventory — The application displays the Product Inventory page (e.g., product listing or Product Inventory header is visible), confirming the user has been returned to Product Inventory | medium |
| TC-003 | WF-003 | Begin checkout from the Shopping Cart | User logged in as <role>, Shopping Cart page is open with at least one <item in cart> | 1. Click the 'Checkout' button on the Shopping Cart page | Begin checkout — The Checkout flow/page is displayed (e.g., checkout header or first checkout step is visible), indicating the checkout process has begun | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Shopping Cart page | User is not authenticated (not logged in) | 1. In a browser where the user is not logged in, navigate to the Shopping Cart page URL (/cart). | Browser redirects to the Login page; a Login form (visible Email and Password fields) is displayed and the Shopping Cart contents are not shown. Access to the Shopping Cart is blocked. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Very long product description displayed in cart | A product exists whose description length is greater than 200 characters, User is logged in (if required) and on the Product Inventory page | 1. On the Product Inventory page, locate the product with the very long description<br>2. Click the product's Add to Cart button<br>3. Click or navigate to the Shopping Cart page | Add to cart succeeds; Shopping Cart shows the item row. The product description in the cart row is displayed without breaking the page layout and shows a visible truncation indicator (e.g., ends with an ellipsis) instead of overflowing the row. | low |
| TC-006 (input_edge) |  | Product description with special characters and emoji | A product exists whose name/description contains special characters and emoji, User is on the Product Inventory page | 1. On the Product Inventory page, locate the product whose description contains special characters/emoji<br>2. Click the product's Add to Cart button<br>3. Navigate to the Shopping Cart page | Add to cart succeeds; Shopping Cart displays the item's description/name including the special characters and emoji exactly as entered (no HTML entities or encoding artifacts visible) in the cart row. | low |
| TC-007 (interaction_edge) | WF-001 | Rapid double-click Remove on a single cart item | Shopping Cart contains exactly one instance of a given item, User is on the Shopping Cart page | 1. Ensure the cart shows the single item row with a visible Remove button<br>2. Click the Remove button for that item<br>3. Immediately (within one second) click the same Remove button again | First removal succeeds: the item row disappears and the cart UI updates (item count/total updates). The immediate second click is blocked / ignored (no second removal occurs) and no duplicate item removal or error is shown; the cart remains consistent with a single removal having occurred. | medium |

---

## Checkout - Information

Total: **12** (positive: 5, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with all required fields filled proceeds to overview | User logged in as <role>, User is on the Checkout - Information page | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal/Zip Code field<br>4. Click the Continue button | Overview step is displayed. | high |
| TC-002 | WF-002 | Click Continue with First Name missing shows first-name error banner | User logged in as <role>, User is on the Checkout - Information page | 1. Leave the First Name field empty<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal/Zip Code field<br>4. Click the Continue button | An error banner is displayed with text: Error: First Name is required | medium |
| TC-003 | WF-003 | Click Continue with Last Name missing shows last-name error banner | User logged in as <role>, User is on the Checkout - Information page | 1. Enter <valid first name> in the First Name field<br>2. Leave the Last Name field empty<br>3. Enter <valid postal code> in the Postal/Zip Code field<br>4. Click the Continue button | An error banner is displayed with text: Error: Last Name is required | medium |
| TC-004 | WF-004 | Click Continue with Postal Code missing shows postal-code error banner | User logged in as <role>, User is on the Checkout - Information page | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Leave the Postal/Zip Code field empty<br>4. Click the Continue button | An error banner is displayed with text: Error: Postal Code is required | medium |
| TC-005 | WF-005 | Click Cancel returns user to the Shopping Cart | User logged in as <role>, User is on the Checkout - Information page | 1. Click the Cancel button | Shopping Cart page is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Continue with First Name blank shows required-first-name error | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Leave the First Name field blank<br>2. Enter a valid value in the Last Name field<br>3. Enter a valid value in the Postal Code field<br>4. Click the Continue button | An error banner displays: 'Error: First Name is required'. The form does not proceed to the overview step; the Checkout - Information page remains displayed. | high |
| TC-007 | WF-003 | Continue with Last Name blank shows required-last-name error | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Enter a valid value in the First Name field<br>2. Leave the Last Name field blank<br>3. Enter a valid value in the Postal Code field<br>4. Click the Continue button | An error banner displays: 'Error: Last Name is required'. The form does not proceed to the overview step; the Checkout - Information page remains displayed. | high |
| TC-008 | WF-004 | Continue with Postal Code blank shows required-postal-code error | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Enter a valid value in the First Name field<br>2. Enter a valid value in the Last Name field<br>3. Leave the Postal Code field blank<br>4. Click the Continue button | An error banner displays: 'Error: Postal Code is required'. The form does not proceed to the overview step; the Checkout - Information page remains displayed. | high |
| TC-009 |  | Continue with all required fields empty shows all required-field errors and blocks progression | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Postal Code field blank<br>4. Click the Continue button | Error banners display all three messages: 'Error: First Name is required', 'Error: Last Name is required', and 'Error: Postal Code is required'. The form does not proceed to the overview step; the Checkout - Information page remains displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) | WF-001 | Leading/trailing whitespace in First Name is trimmed and accepted | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Enter a value with leading and trailing whitespace in the First Name field<br>2. Enter a valid (non-empty) value in the Last Name field<br>3. Enter a valid (non-empty) value in the Postal Code field<br>4. Click the Continue button | Form submission succeeds; proceeds to the overview step; the overview displays the First Name without leading or trailing whitespace (whitespace trimmed in the displayed value). | medium |
| TC-011 (input_edge) | WF-003 | Whitespace-only input in Last Name treated as missing | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Enter a valid (non-empty) value in the First Name field<br>2. Enter a value consisting only of whitespace characters in the Last Name field<br>3. Enter a valid (non-empty) value in the Postal Code field<br>4. Click the Continue button | Submission is blocked; error banner displays "Error: Last Name is required". | medium |
| TC-012 (interaction_edge) | WF-001 | Rapid double-click of Continue after filling required fields | User is on the Checkout - Information page with the First Name, Last Name, and Postal Code fields visible | 1. Enter a valid (non-empty) value in the First Name field<br>2. Enter a valid (non-empty) value in the Last Name field<br>3. Enter a valid (non-empty) value in the Postal Code field<br>4. Click the Continue button<br>5. Immediately click the Continue button again (rapid second click) | Second submission attempt is blocked; only one navigation to the overview step occurs (form submission succeeds once; additional rapid clicks do not cause a second navigation or duplicate actions and no duplicate overview pages are created). | low |

---

## Checkout - Overview

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish completes the order and navigates to confirmation | User logged in as <role>, Cart contains <items> and is ready for checkout | 1. Navigate to the Checkout Overview page<br>2. Review the Order Summary and Totals section to confirm <cart items> are listed and Totals shows Item total, Tax, and Total<br>3. Verify payment information section displays <payment method> and shipping information section displays <shipping address><br>4. Click the Finish button | Completes the order and navigates to the confirmation page. | high |
| TC-002 | WF-002 | Cancel exits checkout and returns user from overview | User logged in as <role>, Cart contains <items> and is ready for checkout | 1. Navigate to the Checkout Overview page<br>2. Review the Order Summary to confirm <cart items> are listed<br>3. Click the Cancel button | Exits checkout. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Clicking Finish does not navigate to confirmation (order not completed) | User is on the Checkout - Overview page, User has at least one item in the cart (<user with items in cart>) | 1. Ensure the Checkout - Overview page is visible showing order summary, totals, payment and shipping information<br>2. Click the 'Finish' button | No navigation occurs; the confirmation page is NOT displayed; the order is NOT completed; an error banner appears at the top of the page indicating '<order completion failed message>' and the Finish action is blocked | high |
| TC-004 | WF-002 | Clicking Cancel does not exit checkout (cancel action blocked) | User is on the Checkout - Overview page, User has at least one item in the cart (<user with items in cart>) | 1. Ensure the Checkout - Overview page is visible showing order summary, totals, payment and shipping information<br>2. Click the 'Cancel' button | User remains on the Checkout - Overview page; checkout is NOT exited; a visible error banner appears at the top of the page indicating '<checkout exit failed message>' and the Cancel action is blocked | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Finish to check duplicate submission handling | Cart contains at least one item, Payment information is set and visible on the Overview step, Shipping information is set and visible on the Overview step, User is on the Checkout - Overview page | 1. Click the Finish button<br>2. Immediately click the Finish button again (within one second of the first click) | First click succeeds: order completes and the confirmation page is shown. Second click is blocked / error shown: no second confirmation is shown and the UI remains on or returns to the single confirmation page (no duplicate order confirmation is visible). | medium |
| TC-006 (interaction_edge) | WF-001 | Use browser Back after Finish then attempt to Finish again (re-submission edge) | Cart contains at least one item, Payment information is set and visible on the Overview step, Shipping information is set and visible on the Overview step, User is on the Checkout - Overview page | 1. Click the Finish button<br>2. On the confirmation page, click the browser Back button<br>3. On the Checkout - Overview page, click the Finish button again | First click succeeds: order completes and confirmation page is shown. After navigating back, the second click is blocked / error shown: the application prevents creating a duplicate order (the UI either redirects back to the existing confirmation page or shows a visible message that resubmission is blocked). No duplicate confirmation is visible. | medium |
| TC-007 (input_edge) |  | Very long shipping address displayed on Overview (display/truncation/wrapping behavior) | Cart contains at least one item, User has entered a shipping address containing a very long free-text string (very long, e.g., >200 characters) during earlier checkout steps, Payment information is set and visible on the Overview step, User navigates to the Checkout - Overview page | 1. Observe the shipping address as displayed in the Overview page order summary/totals section<br>2. Click the Finish button | The Overview displays the very long shipping address (either wrapped across multiple lines or truncated with an ellipsis) with a visible UI indication (wrapped or truncated). No input validation error is shown for the long address. Clicking Finish succeeds: order completes and the confirmation page is shown. | low |

---

## Checkout - Confirmation

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Confirmation page displays success message and Back Home button | User logged in as <role>, User has completed checkout | 1. Open the Checkout Confirmation page<br>2. Observe the page header and body<br>3. Verify the success message and primary actions are visible | Page displays "Thank you for your order!" and a visible 'Back Home' button is present on the Checkout Confirmation page | high |
| TC-002 | WF-001 | Clicking Back Home returns to Product Inventory and clears the cart | User logged in as <role>, User has completed checkout and is on the Checkout Confirmation page with items previously in the cart | 1. Open the Checkout Confirmation page<br>2. Click the 'Back Home' button | Navigates to Product Inventory and clears the cart. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Back Home click does not navigate away from Confirmation page | User is on the Checkout Confirmation page after completing an order; confirmation message is visible; cart currently contains <items> | 1. Click the 'Back Home' button on the Confirmation page | The action is blocked: the UI remains on the Checkout Confirmation page; the success message (e.g. 'Thank you for your order!') remains visible; Product Inventory page is NOT displayed; the cart badge still shows a <non-zero count> (cart was not cleared). | high |
| TC-004 | WF-001 | Back Home navigates to Product Inventory but cart is not cleared | User is on the Checkout Confirmation page after completing an order; confirmation message is visible; cart currently contains <items> | 1. Click the 'Back Home' button on the Confirmation page<br>2. Observe the landing page after the click | Partial failure: Product Inventory page is displayed, but the cart was NOT cleared — the cart badge shows a <non-zero count> and previously ordered items remain in the cart. The on_success effect ('clears the cart') did not occur. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Single Back Home click navigates to Product Inventory and clears cart | User has items in cart, User completed checkout and is on the Confirmation page showing the success message | 1. Click the "Back Home" button on the Confirmation page | Navigation to Product Inventory succeeds; Product Inventory page is displayed; cart badge/count shows 0 items and the cart contents view shows no items (cart cleared); the Confirmation page is no longer visible | medium |
| TC-006 (interaction_edge) |  | Rapid double-click of Back Home results in single successful navigation and cart cleared once | User has items in cart, User completed checkout and is on the Confirmation page showing the success message | 1. Click the "Back Home" button on the Confirmation page<br>2. Immediately click the "Back Home" button again before navigation completes | First click navigates to Product Inventory and succeeds; second click is ignored or has no adverse effect (no duplicate navigation or error shown); cart badge/count shows 0 items and cart contents are empty after navigation | low |
| TC-007 (interaction_edge) |  | Back Home clicked from multiple open confirmation tabs: first clears cart, subsequent clicks navigate with empty cart | User has items in cart, User completed checkout and opened the Confirmation page in two separate browser tabs (Tab A and Tab B), both showing the success message | 1. In Tab A, click the "Back Home" button<br>2. In Tab B, click the "Back Home" button | First click (Tab A) navigates to Product Inventory and succeeds; cart badge/count becomes 0 and cart contents are cleared; second click (Tab B) also navigates to Product Inventory and succeeds but shows an already-empty cart (cart remains 0 items); no errors are shown and no items are re-added to the cart | low |

---

## Logout

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User clicks Logout and is returned to Login; protected pages become inaccessible | User logged in as <role>, User is on a protected page (e.g., inventory or cart) | 1. Click the Logout button in the application header | Ends the session and returns the user to the login page. After logout, protected pages (inventory, detail, cart, checkout) are not accessible without logging in again. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated direct access to a protected page is blocked | User is not authenticated (no active session) | 1. In the browser address bar, navigate to the Inventory page URL (protected page) | User is redirected to the Login page; the Login form is displayed and the Inventory content is not rendered; no authenticated session is created (protected page remains inaccessible). | high |
| TC-003 |  | Attempt to invoke Logout endpoint when not logged in | User is not authenticated (no active session) | 1. In the browser address bar, navigate to the Logout endpoint/URL (invoke logout) while not logged in | Application shows or redirects to the Login page (Login form visible); no server error is shown; no session was ended because none existed (action is effectively blocked). | medium |
| TC-004 | WF-001 | Using browser Back after logout does not reveal protected content | User is authenticated (logged in as <role>) | 1. Log in as <role><br>2. Navigate to the Inventory page (protected)<br>3. Click the Logout control<br>4. After logout completes and Login page is shown, click the browser Back button | After pressing Back the Inventory page content is not displayed; the Login page is shown (or user is redirected to Login) and no protected content is visible; the user remains unauthenticated (session remains ended). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Browser Back after Logout should not reveal protected page | User is logged in, A protected page (inventory/detail/cart/checkout) is open in the current tab | 1. Click the Logout button<br>2. Wait for the app to return to the login page<br>3. Click the browser Back button | Attempt to navigate back to the protected page is blocked / error shown: the app shows the login page and protected page content is not displayed | medium |
| TC-006 (interaction_edge) | WF-001 | Refresh a protected page in a second tab after logging out in the first tab | User is logged in, Protected page is open in Tab B, An active session exists in Tab A | 1. In Tab A click the Logout button<br>2. In Tab B click the browser Refresh button / Reload | Refresh of the protected page is blocked / error shown: Tab B is redirected to the login page and protected content is not accessible without logging in again | medium |
| TC-007 (state_edge) | WF-001 | Rapid repeated clicks on Logout do not create inconsistent session state | User is logged in, A protected page is open | 1. Click the Logout button<br>2. Immediately click the Logout button again | First logout succeeds: user is redirected to the login page; the second click has no adverse effect and no additional sessions or errors are created (user remains on login page) | medium |

---

## Reset App State

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset clears cart and resets UI states without logging out | User logged in as <role>, Cart contains one or more <items>; cart badge is visible; items that are in the cart display the 'Remove' button state | 1. On the app main screen, click the 'Reset App State' control<br>2. Wait for the UI to refresh | Cart list shows no items; the cart badge is no longer visible; product tiles that previously displayed 'Remove' now display the 'Add' button state; the user remains logged in (account avatar or account menu remains visible). | high |
| TC-002 |  | After Reset the user stays logged in and can add items again | User logged in as <role>, Cart contains one or more <items> before reset; add/remove buttons reflect added items | 1. On the app main screen, click the 'Reset App State' control<br>2. Wait for the UI to refresh<br>3. Click 'Add' on a product tile to add it to the cart | User remains logged in after reset and is able to add items: the selected product appears in the cart list and the cart badge becomes visible again reflecting the added item(s). | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user attempts to invoke Reset App State | User is not authenticated (not logged in) | 1. Navigate to the application page that contains the Reset App State control<br>2. Click the 'Reset App State' control | Navigation is redirected to the Login page; the Reset action is blocked (no cart clearing or UI state reset). The cart contents remain unchanged (<cart contents> remains visible) and the user is not logged in. | high |
| TC-004 | WF-001 | User with a role that lacks permission cannot see or use Reset App State | User is authenticated as <unauthorized role> (a role that should not perform Reset App State) | 1. Sign in as <unauthorized role><br>2. Navigate to the application page that normally contains the Reset App State control<br>3. Inspect the page for the presence of the 'Reset App State' control | The 'Reset App State' control is not visible or is disabled for <unauthorized role>; no Reset action can be performed. The cart and UI state remain unchanged (cart badge and add/remove button states are unchanged). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid repeated clicks on Reset App State button | User is logged in and visible in the UI (profile avatar or sign-out link present), Cart contains at least one item and the cart badge shows a non-zero count, Reset App State control/button is visible | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again (within 1 second) | Reset action succeeds: cart is cleared (cart list empty) and cart badge shows zero; no duplicate errors or multiple-clear side-effects are shown; add/remove button states reset to default; user remains logged in (profile avatar and sign-out link remain visible) | medium |
| TC-006 (interaction_edge) | WF-001 | Click Reset App State while on the in-progress checkout page | User is logged in and visible in the UI (profile avatar or sign-out link present), User is on the checkout page with items in the cart and the checkout form (Place order or equivalent) visible | 1. Click the Reset App State button | Reset action succeeds: cart is cleared and cart badge shows zero; checkout UI reflects empty cart (checkout form shows a 'cart is empty' message or the Place order button is disabled/inactive); user remains logged in (profile avatar and sign-out link remain visible) | medium |
| TC-007 (interaction_edge) | WF-001 | Reset App State in one browser tab updates another open tab without manual refresh | User is logged in and visible in the UI (profile avatar or sign-out link present), Two browser tabs are open to the app under the same user account (Tab A and Tab B), Both tabs show the cart with at least one item and a non-zero cart badge | 1. In Tab A, click the Reset App State button<br>2. In Tab B, observe the cart UI without performing a manual refresh | Reset action in Tab A succeeds: cart is cleared in Tab A and cart badge shows zero; Tab B updates automatically (cart list empty and cart badge shows zero) without manual refresh; user remains logged in in both tabs (profile avatar and sign-out link remain visible) | medium |

---
