# Test Cases — Swaglab

Generated: 2026-06-09T09:11:53.951991Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 78 | 24 | 21 | 33 | 34 | 35 | 9 |

## Login

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials redirects to Product Inventory | User is not authenticated and Login page is open | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | authenticates and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Submit with Username blank (Password provided) | User is on the Login page, User is not authenticated | 1. Leave the Username field blank<br>2. Enter <shared password> in the Password field<br>3. Click the Login button | Inline validation error appears on the Username field: 'Epic sadface: Username is required.'; form is not submitted; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-003 |  | Submit with Password blank (Username provided) | User is on the Login page, User is not authenticated | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | Inline validation error appears on the Password field: 'Epic sadface: Password is required.'; form is not submitted; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-004 |  | Submit with both Username and Password blank | User is on the Login page, User is not authenticated | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Inline validation errors appear on both fields: Username shows 'Epic sadface: Username is required.' and Password shows 'Epic sadface: Password is required.'; form is not submitted; user remains on the Login page. | high |
| TC-005 |  | Login attempt with locked_out_user is blocked and shows locked-out message | User is on the Login page, User is not authenticated | 1. Enter locked_out_user in the Username field<br>2. Enter <shared password secret_sauce> in the Password field<br>3. Click the Login button | Page displays the error banner: 'Epic sadface: Sorry, this user has been locked out.'; authentication does not occur; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-006 |  | Login attempt with valid username and incorrect password shows credential mismatch error | User is on the Login page, User is not authenticated | 1. Enter <valid username> in the Username field<br>2. Enter <incorrect password> in the Password field<br>3. Click the Login button | Page displays the error banner: 'Epic sadface: Username and password do not match any user in this service.'; authentication does not occur; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-007 |  | Unauthenticated access to Product Inventory redirects to Login page | User is not authenticated | 1. Navigate directly to the Product Inventory page URL without logging in | Browser is redirected to the Login page; Product Inventory content is not shown and user must authenticate to access it (no access granted). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Username with leading and trailing whitespace | Login page is displayed, Spec reference: accepted_credentials require Username to match one of the listed usernames exactly | 1. In the Username field, enter <standard_user> with a leading space and a trailing space<br>2. In the Password field, enter <shared secret_sauce> exactly<br>3. Click the Login button | Login is blocked; error banner shows: "Epic sadface: Username and password do not match any user in this service." (the whitespace causes the username not to match the accepted_credentials list) | medium |
| TC-009 (input_edge) |  | Password with trailing newline or surrounding whitespace | Login page is displayed, Spec reference: accepted_credentials require Password to equal <shared secret_sauce> exactly | 1. In the Username field, enter <standard_user> exactly<br>2. In the Password field, enter <shared secret_sauce> with one trailing whitespace character (or an embedded newline)<br>3. Click the Login button | Login is blocked; error banner shows: "Epic sadface: Username and password do not match any user in this service." (the password does not exactly match the shared secret) | medium |
| TC-010 (input_edge) |  | Extremely long Username and Password (200+ characters) | Login page is displayed, Spec reference: Username and Password fields exist with exact-match credential logic | 1. In the Username field, enter a very long string (200+ characters)<br>2. In the Password field, enter a very long string (200+ characters)<br>3. Click the Login button | Login is blocked; error banner shows: "Epic sadface: Username and password do not match any user in this service." OR an inline validation indicator appears rejecting/truncating input — a visible error must be shown preventing login (test asserts a failure to authenticate due to oversized input) | medium |
| TC-011 (interaction_edge) |  | Rapid back-button after successful login — login page should not allow automatic re-submit | Login page is displayed, Valid credentials are known: <standard_user> and <shared secret_sauce> | 1. In the Username field, enter <standard_user> exactly<br>2. In the Password field, enter <shared secret_sauce> exactly<br>3. Click the Login button<br>4. Wait until the Product Inventory page loads (redirect completes)<br>5. Press the browser Back button once | After pressing Back, the browser shows the Login page blank (no pre-filled credentials) and any attempt to submit immediately is blocked; clicking Login without entering fields shows the required-field error banner: "Epic sadface: Username is required." or "Epic sadface: Password is required.", i.e., the previous successful login does not cause an automatic second successful submit | low |

---

## Product Inventory

Total: **12** (positive: 5, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open Product Detail from product name link | User logged in as <Customer>, Product Inventory page has at least one product displayed | 1. Navigate to the Product Inventory page<br>2. Click the product Name link for <visible product> in the Products table | The Product Detail page for <visible product> is displayed. | medium |
| TC-002 |  | Add a product to the cart from Products table | User logged in as <Customer>, <Product> is displayed in the Products Table with InCart == false | 1. Navigate to the Product Inventory page<br>2. Click the 'Add to cart' button for <Product> in the Products table | The product's row shows the 'Remove' button (replacing 'Add to cart'); the cart badge count increases by 1. | high |
| TC-003 |  | Remove a product from the cart from Products table | User logged in as <Customer>, <Product> is displayed in the Products Table with InCart == true, Cart badge shows the current count | 1. Navigate to the Product Inventory page<br>2. Click the 'Remove' button for <Product> in the Products table | The product's row shows the 'Add to cart' button (replacing 'Remove'); the cart badge count decreases by 1. | high |
| TC-004 |  | Sort products by Price (low–high) | User logged in as <Customer>, Product Inventory page displays multiple products with visible Price values | 1. Navigate to the Product Inventory page<br>2. Select 'Price (low–high)' from the Sort By dropdown | Products table displays rows ordered by Price (low–high); Price values are in ascending order from top to bottom. | medium |
| TC-005 |  | Sort products by Name (Z–A) | User logged in as <Customer>, Product Inventory page displays multiple products with visible Name values | 1. Navigate to the Product Inventory page<br>2. Select 'Name (Z–A)' from the Sort By dropdown | Products table displays rows ordered by Name (Z–A); product names are in descending alphabetical order from top to bottom. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Unauthenticated access to Product Inventory page is blocked | User is not logged in | 1. Navigate to the Product Inventory page URL / Inventory listing page | Navigation is blocked: user is redirected to the Login page; the Login form is displayed and no product list or product controls are visible. Product Inventory is not accessible without authentication. | high |
| TC-007 |  | Attempt to Add to cart when product state is already InCart (button should not be available) | User is logged in, A product row <product row> is already in the cart (InCart == true), Current cart badge count is <current cart badge count> | 1. Navigate to the Product Inventory page<br>2. Locate the row for <product row> which is preconditioned to be InCart == true<br>3. Inspect the row for an 'Add to cart' button<br>4. Attempt to click an 'Add to cart' button in that row if it is present | 'Add to cart' button is not displayed in the <product row> (the visible control is 'Remove'); clicking an 'Add to cart' button is not possible. The cart badge count remains <current cart badge count>; the product remains InCart and the 'Remove' button is visible. No add-to-cart action occurs. | high |
| TC-008 |  | Attempt to Remove when product state is NotInCart (Remove button should not be available) | User is logged in, A product row <product row> is not in the cart (InCart == false), Current cart badge count is <current cart badge count> | 1. Navigate to the Product Inventory page<br>2. Locate the row for <product row> which is preconditioned to be InCart == false<br>3. Inspect the row for a 'Remove' button<br>4. Attempt to click a 'Remove' button in that row if it is present | 'Remove' button is not displayed in the <product row> (the visible control is 'Add to cart'); clicking a 'Remove' button is not possible. The cart badge count remains <current cart badge count>; the product remains NotInCart and the 'Add to cart' button is visible. No remove action occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (state_edge) |  | Rapid double-click 'Add to cart' on a single product row | User is logged in, A product row exists with InCart == false, Cart badge shows the current count | 1. Navigate to the Product Inventory page<br>2. Locate the product row where InCart == false<br>3. Click the 'Add to cart' button for that product<br>4. Within 500ms of step 3, click the 'Add to cart' button again | First click succeeds: the button changes to 'Remove' and the cart badge increments by one. The second click is ignored (no additional increment); the button remains 'Remove' and the cart badge shows exactly one increment from the precondition value. | medium |
| TC-010 (state_edge) |  | Rapid add then immediate remove on same product row | User is logged in, A product row exists with InCart == false, Cart badge shows the current count | 1. Navigate to the Product Inventory page<br>2. Locate the product row where InCart == false<br>3. Click the 'Add to cart' button for that product<br>4. Within 500ms of step 3, click the 'Remove' button for the same product | Both transitions succeed: after step 3 the button changes to 'Remove' and the cart badge increments by one; after step 4 the button changes back to 'Add to cart' and the cart badge returns to the precondition value. No duplicate additions remain. | medium |
| TC-011 (data_edge) |  | Sort when multiple products have identical Price (identical sort keys) | User is logged in, At least two products exist that have identical Price values | 1. Navigate to the Product Inventory page<br>2. Open the Sort_By dropdown<br>3. Select 'Price (low–high)'<br>4. Observe the Products_Table rows and identify the two products with identical Price<br>5. Click the Name of one of the two products | Sorting succeeds: the table reorders without error and both products with identical Price are present. Clicking the Name navigates to that product's Product Detail page (navigation succeeds). Returning to the Product Inventory page (browser Back) shows the sorted table with both products still present. | low |
| TC-012 (interaction_edge) |  | Add to cart, open Product Detail, then use browser Back — verify persisted UI state and single increment | User is logged in, A product row exists with InCart == false, Cart badge shows the current count | 1. Navigate to the Product Inventory page<br>2. Click the 'Add to cart' button for the product (InCart transitions to true)<br>3. Click the product Name (or Image) to open the Product Detail page<br>4. On the Product Detail page, press the browser Back button to return to the Product Inventory page | Navigation and state persistence succeed: after returning, the product row displays the 'Remove' button (InCart == true) and the cart badge shows exactly one increment from the precondition value (no duplicate increments). Clicking the product Name again still opens the corresponding Product Detail page. | low |

---

## Product Detail

Total: **11** (positive: 5, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View product details and action button state | User logged in as <Customer>, <product> exists in the product catalog | 1. Navigate to the Product Detail page for <product> | Product image, product name, product description, and product price are visible on the Product Detail page; the action button displays the current cart state label ('Add to cart' or 'Remove'). | high |
| TC-002 |  | Add product to cart from Product Detail (Not In Cart → In Cart) | User logged in as <Customer>, <product> is Not In Cart | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Add to cart' button in the action bar | The 'Add to cart' button is replaced by a 'Remove' button on the Product Detail page, indicating the product is In Cart. | high |
| TC-003 |  | Remove product from cart from Product Detail (In Cart → Not In Cart) | User logged in as <Customer>, <product> is In Cart | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Remove' button in the action bar | The 'Remove' button is replaced by an 'Add to cart' button on the Product Detail page, indicating the product is Not In Cart. | high |
| TC-004 |  | Navigate back to Product Inventory using Back to products link | User logged in as <Customer> | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Back to products' link | Product Inventory page is displayed. | medium |
| TC-005 |  | Navigate to Shopping Cart using Cart icon | User logged in as <Customer> | 1. Navigate to the Product Detail page for <product><br>2. Click the Cart icon | Shopping Cart page is displayed. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to use 'Remove' action while product is Not In Cart | The product is currently in the 'Not In Cart' state (not present in the Shopping Cart) | 1. Open the Product Detail page for <product>.<br>2. Inspect the action area where 'Add to cart' / 'Remove' would appear.<br>3. Attempt to click the 'Remove' button (if it is displayed). | The 'Remove' button is not visible or is disabled while the product is in the 'Not In Cart' state. Clicking has no effect. The product remains in the 'Not In Cart' state; the Shopping Cart contents and cart count do not change; there is no navigation away from the Product Detail page. | high |
| TC-007 |  | Attempt to use 'Add to cart' action while product is In Cart | The product is currently in the 'In Cart' state (already present in the Shopping Cart) | 1. Open the Product Detail page for <product> that is already in the cart.<br>2. Inspect the action area where 'Add to cart' / 'Remove' would appear.<br>3. Attempt to click the 'Add to cart' button (if it is displayed). | The 'Add to cart' button is not visible or is disabled while the product is in the 'In Cart' state. Clicking has no effect. The product remains in the 'In Cart' state; the Shopping Cart contents and cart count do not change; there is no duplicate addition or navigation. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (state_edge) |  | Rapid double-click 'Add to cart' does not create duplicate cart entries | User is on Product Detail page for a product currently in state 'Not In Cart', Shopping Cart is empty of this product | 1. Observe the action button displays 'Add to cart'<br>2. Click the 'Add to cart' button<br>3. Immediately click the 'Add to cart' button again (rapid second click before UI updates)<br>4. Click the 'Cart icon' to navigate to the Shopping Cart page<br>5. Inspect the Shopping Cart page for entries of the product | The second rapid click is blocked; only one item for the product appears in the Shopping Cart and no duplicate entries are created; Product Detail shows state 'In Cart' (button now shows 'Remove'). This scenario succeeds when exactly one cart entry is present and the UI indicates the product is 'In Cart'. | medium |
| TC-009 (state_edge) |  | Immediate 'Remove' attempted while 'Add to cart' is in-flight is blocked and leaves consistent state | User is on Product Detail page for a product currently in state 'Not In Cart', Shopping Cart is empty of this product | 1. Observe the action button displays 'Add to cart'<br>2. Click the 'Add to cart' button<br>3. Immediately click the 'Remove' button position (attempt to remove before the UI updates to 'In Cart')<br>4. Wait for operations to complete and observe the final action button label on Product Detail<br>5. Click the 'Cart icon' and inspect the Shopping Cart page for presence/absence of the product | The immediate 'Remove' action is blocked while the 'Add to cart' is in-flight; only a single definitive outcome occurs (the add succeeds and the product is present once, with Product Detail showing 'Remove') and no duplicate or inconsistent states appear in the Shopping Cart. This scenario succeeds when the UI is consistent (product either present once or absent) and no duplicate entries are created; if the UI blocks the second action an inline disabled state or loading indicator is visible. | medium |
| TC-010 (interaction_edge) |  | Use 'Back to products' then browser Back without creating duplicate cart entries | User is on Product Detail page for a product currently in state 'Not In Cart', Shopping Cart is empty of this product | 1. Click the 'Add to cart' button<br>2. Click the 'Back to products' link<br>3. From the Product Inventory page, use the browser Back button to return to the Product Detail page<br>4. Observe the action button label on Product Detail<br>5. Click the 'Cart icon' and inspect the Shopping Cart page for entries of the product | Navigating away via 'Back to products' and then using the browser Back button does not trigger a second 'Add to cart' action; only one cart entry exists for the product and Product Detail shows state 'In Cart' (button 'Remove'). This scenario succeeds when no duplicate item appears in the Shopping Cart and the UI does not re-trigger add on navigation history actions. | low |
| TC-011 (input_edge) |  | Render product detail with very long description and special/unicode characters | There exists a product whose stored description contains a very long string (200+ characters) including special characters and emoji, User can navigate to that product's Product Detail page | 1. Navigate to the Product Detail page for the product with a very long description containing special characters and emoji<br>2. Observe how the description text is rendered on the Product Detail page<br>3. Verify presence or absence of truncation controls (e.g., 'show more') if applicable<br>4. Click the 'Back to products' link to ensure navigation still works | Rendering of a very long description with special/unicode characters succeeds: the Product Detail page loads without UI breakage; the full description is either displayed or visibly truncated with a clear 'show more' control; no rendering errors are shown and navigation via 'Back to products' still succeeds. | low |

---

## Shopping Cart

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Remove an item from the cart via row Remove button | User logged in as <Customer>, Shopping Cart page is open, Shopping Cart contains an item with description <item description> | 1. Click the Remove button on the row for <item description> in the Shopping Cart table | The Shopping Cart table no longer displays a row with description <item description>; other items (if any) remain visible in the table | high |
| TC-002 |  | Continue shopping returns user to Product Inventory | User logged in as <Customer>, Shopping Cart page is open | 1. Click the Continue Shopping link in the Shopping Cart action bar | The Product Inventory page is displayed | medium |
| TC-003 |  | Begin checkout from the Shopping Cart | User logged in as <Customer>, Shopping Cart page is open, Shopping Cart contains at least one item | 1. Click the Checkout button in the Shopping Cart action bar | The Checkout page is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Access Shopping Cart while unauthenticated | User is not logged in / unauthenticated | 1. Navigate to the Shopping Cart page (attempt to open the Shopping Cart URL) | Access is blocked: the user is redirected to the Login page or shown the authentication prompt (login form); the Shopping Cart contents are not displayed and no cart actions (Remove/Checkout/Continue Shopping) are available. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Rapid double-click on a row's Remove button | A product is present in the shopping cart (exactly one row) | 1. Navigate to the Shopping Cart page<br>2. Double-click the Remove button on the cart row within 1 second | Only one removal action succeeds: the row is removed once and the cart updates to show the item is gone (no duplicate removals). The second click is ignored or the Remove button is disabled immediately after the first click; no UI shows multiple removals or multiple success messages (if an inline success appears it appears only once). | medium |
| TC-006 (input_edge) |  | Very long product description displayed in cart (200+ characters) | A product whose description length is >= 200 characters has been added to the cart | 1. Navigate to the Shopping Cart page<br>2. Locate the Description cell for the long-description product row | The UI handles the long description without breaking layout: either the full description is rendered successfully within the table cell (succeeds) or the description is visibly truncated with a truncation indicator (e.g., '...') and a way to view the full text (tooltip/expand). There should be no visual overflow causing other rows or actions to become unusable. | low |
| TC-007 (input_edge) |  | Product name with leading and trailing whitespace in cart display | A product whose name includes leading and trailing whitespace has been added to the cart | 1. Navigate to the Shopping Cart page<br>2. Inspect the product name shown in the cart row | Leading and trailing whitespace is not shown in the cart listing: the displayed product name is trimmed (succeeds). There is no visible leading/trailing space in the product name cell; if the system instead rejects or flags such names, a visible inline validation or sanitization indicator is shown. | low |

---

## Checkout - Information

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Continue with all required fields filled proceeds to Overview | User logged in as <Customer>, Checkout - Information page is open with at least one item in the Shopping Cart | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click the Continue button | Overview step is displayed (proceeds to Overview step) | high |
| TC-002 |  | Clicking Cancel returns user to Shopping Cart | User logged in as <Customer>, Checkout - Information page is open with at least one item in the Shopping Cart | 1. Click the Cancel link | Shopping Cart page is displayed (redirects to Shopping Cart) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Continue blocked when First Name is blank (representative text-field required validation) | User is on the Checkout - Information page (Checkout Information form is displayed) | 1. Ensure the First Name field is empty<br>2. Enter <valid last name> into the Last Name field<br>3. Enter <valid postal code> into the Postal Code field<br>4. Click the Continue button | Form does not proceed to the Overview step; an error banner is displayed containing "Error: First Name is required" and the First Name field is indicated as invalid. No navigation to Overview occurs. | high |
| TC-004 |  | Continue blocked when all required fields are empty (aggregate required validation) | User is on the Checkout - Information page (Checkout Information form is displayed) | 1. Ensure the First Name field is empty<br>2. Ensure the Last Name field is empty<br>3. Ensure the Postal Code field is empty<br>4. Click the Continue button | Form does not proceed to the Overview step; an error banner is displayed containing all three messages: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required". No navigation to Overview occurs and the required fields are indicated as invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Very long text in all required fields | User is on the Checkout - Information page with the Checkout_Information_Form visible | 1. In the First Name field enter a very long string (200+ characters)<br>2. In the Last Name field enter a very long string (200+ characters)<br>3. In the Postal Code field enter a very long string (200+ characters)<br>4. Click the Continue button | Form submission succeeds; the UI proceeds to the Overview step; the Overview page displays the exact long text entered for First Name, Last Name, and Postal Code (no silent truncation without an indicator). | medium |
| TC-006 (input_edge) |  | Special characters and emoji in required fields | User is on the Checkout - Information page with the Checkout_Information_Form visible | 1. In the First Name field enter a string containing special characters and emoji (for example, symbols, punctuation, and emoji)<br>2. In the Last Name field enter a string containing special characters and emoji<br>3. In the Postal Code field enter a string containing special characters and emoji<br>4. Click the Continue button | Form submission succeeds; the UI proceeds to the Overview step; the Overview page displays the exact special characters and emoji entered for each field (no replacement with placeholders or removal). | medium |
| TC-007 (input_edge) |  | Whitespace-only inputs for required fields | User is on the Checkout - Information page with the Checkout_Information_Form visible | 1. In the First Name field enter a string composed only of whitespace characters (spaces/tabs)<br>2. In the Last Name field enter a string composed only of whitespace characters (spaces/tabs)<br>3. In the Postal Code field enter a string composed only of whitespace characters (spaces/tabs)<br>4. Click the Continue button | Submission is blocked / error shown: the form does not proceed to Overview; an error banner is displayed containing the messages: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required' (i.e., whitespace-only values are treated as missing). | medium |
| TC-008 (interaction_edge) |  | Rapid double-click of Continue to test duplicate submission handling | User is on the Checkout - Information page with the Checkout_Information_Form visible, All required fields are filled with valid non-empty values | 1. Click the Continue button twice in rapid succession (double-click)<br>2. Observe the navigation/result | First click succeeds and the UI proceeds to the Overview step; the second instantaneous click is ignored/blocked (no second navigation or duplicate action occurs) and the user remains on/arrives at the Overview page only once. | medium |

---

## Checkout - Overview

Total: **6** (positive: 2, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Finish checkout from Overview with visible order summary and totals | User logged in as <Customer>, Checkout - Overview step is open with <cart items>, <valid payment method>, and <shipping address> selected | 1. On the Checkout - Overview page, review the Order Summary: verify the list of cart items is visible<br>2. Verify the Totals section displays 'Item total', 'Tax', and 'Total' labels<br>3. Verify the Payment information section is visible<br>4. Verify the Shipping information section is visible<br>5. Click the Finish button | completes the order and navigates to the confirmation page | high |
| TC-002 |  | Cancel checkout from Overview returns user out of checkout | User logged in as <Customer>, Checkout - Overview step is open with <cart items>, <valid payment method>, and <shipping address> selected | 1. On the Checkout - Overview page, confirm the Order Summary, Totals ('Item total', 'Tax', 'Total'), Payment information, and Shipping information are visible<br>2. Click the Cancel button | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user cannot access Checkout Overview | User is not authenticated (not logged in) | 1. In a new browser session where the user is not logged in, navigate to the Checkout Overview page URL | Access is blocked: the user is redirected to the Login page and the Checkout Overview content (order summary, totals, payment and shipping information) is not displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (state_edge) |  | Rapid double-click of Finish to check duplicate order prevention | User has completed all prior checkout steps (shipping, payment) and is on the Overview step, Cart contains items and totals are displayed | 1. Verify the Overview step is visible with the Finish button<br>2. Click the Finish button<br>3. Immediately click the Finish button again (second click while first submission is processing) | First Finish click succeeds: the app navigates to the confirmation page. The immediate second click is blocked: Finish becomes disabled or the second click is ignored and no second navigation or duplicate order occurs (user sees only the single confirmation). | medium |
| TC-005 (interaction_edge) |  | Use browser Back after successful Finish then attempt to resubmit | User has completed all prior checkout steps (shipping, payment) and is on the Overview step, Cart contains items and totals are displayed | 1. Click the Finish button<br>2. Confirm the app navigates to the confirmation page<br>3. Press the browser Back button to return to the Overview step<br>4. On the returned Overview step, click the Finish button again | First Finish click succeeds: confirmation page is displayed. After using Back, attempting to resubmit is blocked: the second submission is prevented (Finish is disabled or an inline message prevents re-submission) and no duplicate confirmation or duplicate order is produced; the confirmation page remains the authoritative successful outcome. | medium |
| TC-006 (state_edge) |  | Click Cancel immediately after triggering Finish (race between finish and cancel) | User has completed all prior checkout steps (shipping, payment) and is on the Overview step, Cart contains items and totals are displayed | 1. Click the Finish button<br>2. Immediately click the Cancel button before navigation completes | Finish succeeds: the order completion proceeds and the app navigates to the confirmation page. The immediate Cancel click is blocked or ignored during processing: Cancel does not undo the completed action and the user still reaches the confirmation page (no cancellation of the completed order). | medium |

---

## Checkout - Confirmation

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Confirmation page shows success message after checkout | User logged in as <Customer> | 1. Open the Checkout - Confirmation page<br>2. Observe the page content | Confirmation page displays "Thank you for your order!" | medium |
| TC-002 |  | Click Back Home redirects to Product Inventory and clears the cart | User logged in as <Customer> | 1. Open the Checkout - Confirmation page<br>2. Click the Back Home button | navigates to Product Inventory and clears the cart; Product Inventory page is visible and the cart shows 0 items | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Back Home button fails to navigate to Product Inventory | User has completed checkout and is on the Confirmation page, Confirmation page displays the success message (e.g. "Thank you for your order!"), Cart currently contains <items that should be cleared when returning home> | 1. Click the "Back Home" button on the Confirmation page | Page does not navigate to Product Inventory; the user remains on the Confirmation page and the success message (e.g. "Thank you for your order!") is still visible; the cart is not cleared and still contains <items that should be cleared> (i.e., the on_success behavior 'navigates to Product Inventory and clears the cart' did not occur). | high |
| TC-004 |  | Back Home navigates but does not clear the cart | User has completed checkout and is on the Confirmation page, Confirmation page displays the success message (e.g. "Thank you for your order!"), Cart currently contains <items that should be cleared when returning home> | 1. Click the "Back Home" button on the Confirmation page<br>2. Observe the Product Inventory page and the site cart indicator | User is navigated to Product Inventory but the cart still shows the same <items that should be cleared> (cart not cleared); no indication that the cart was emptied. This violates the expected on_success behavior 'navigates to Product Inventory and clears the cart'. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Rapid double-click of 'Back Home' after confirmation | User has just completed checkout and is on the Confirmation page with the success message visible, Header cart indicator shows items prior to clicking Back Home | 1. Focus the browser on the Confirmation page where the success message is visible<br>2. Click the 'Back Home' button<br>3. Immediately click the 'Back Home' button again within one second | First navigation to Product Inventory succeeds and the header cart indicator shows zero (cart cleared); the second click does not produce an error or create a duplicate navigation event (no additional cart changes) — overall behavior succeeds | medium |
| TC-006 (interaction_edge) |  | Use browser Back after being redirected to Product Inventory | User has completed checkout and is on the Confirmation page with the success message visible, Cart was populated before checkout | 1. Click the 'Back Home' button on the Confirmation page<br>2. Wait until Product Inventory is displayed<br>3. Press the browser Back button once | Using the browser Back does not restore the cleared cart; the header cart indicator remains zero and no additional order is created — cart-clearing behavior succeeds and persists after Back navigation | medium |
| TC-007 (interaction_edge) |  | Click 'Back Home' from multiple browser tabs (race across tabs) | User completes checkout in Tab A and is on the Confirmation page with success message visible, User opens the same Confirmation page in Tab B (same session/state) | 1. In Tab A, click the 'Back Home' button<br>2. In Tab B (without reloading), click the 'Back Home' button | Navigations from both tabs succeed (each tab navigates to Product Inventory) and the header cart indicator shows zero in both tabs; no errors are shown and cart remains cleared — behavior succeeds | low |
| TC-008 (interaction_edge) |  | Attempt 'Back Home' while the client is offline | User is on the Confirmation page with success message visible, Network is interrupted (client offline) before attempting navigation | 1. Ensure the browser/network is set to offline<br>2. Click the 'Back Home' button while offline | Navigation is blocked and a visible network error is shown (inline error/toast); the user remains on the Confirmation page and cart-clearing navigation to Product Inventory does not complete — action is blocked / error shown | medium |

---

## Logout

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Click Logout from a protected page redirects to Login | User logged in as <User>, User is on a protected page: <inventory> | 1. Click the Logout button | The Login page is displayed and the login form is visible. | high |
| TC-002 |  | Logged-out user is redirected to Login when accessing protected pages | User logged out | 1. Navigate to the Inventory page<br>2. Observe that the Login page is displayed with the login form visible<br>3. Navigate to the Detail page<br>4. Observe that the Login page is displayed with the login form visible<br>5. Navigate to the Cart page<br>6. Observe that the Login page is displayed with the login form visible<br>7. Navigate to the Checkout page<br>8. Observe that the Login page is displayed with the login form visible | Each attempted navigation to a protected page (<inventory>, <detail>, <cart>, <checkout>) redirects to the Login page; the Login page with the login form is displayed after each attempt. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user cannot access protected pages (inventory) | User is not authenticated (no active session) | 1. In a browser session with no active login, navigate to the Inventory page (<inventory>) | The application blocks access: the user is redirected to the login page; Inventory content is not displayed; the Logout control is not visible. No protected data is accessible without authentication. | high |
| TC-004 |  | After clicking Logout the session ends and protected pages are not accessible | User is logged in with an active session | 1. Click the Logout button<br>2. Observe that the application returns to the login page<br>3. From the login page, navigate to the Cart page (<cart>) | Logout ends the session and blocks access: after step 1 the user is shown the login page; after step 3 the user is redirected to the login page and Cart content is not displayed. The protected page remains inaccessible until re-authentication (no protected content visible and no Logout control present). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Double-click Logout button rapidly | User is authenticated, User is on a protected page (e.g., inventory) where Logout button is visible | 1. Click the Logout button once<br>2. Immediately click the Logout button a second time before the redirect completes | First logout click succeeds: session ends and user is redirected to the login page. Second click has no additional effect and does not create an error or a second session; login page remains visible. | medium |
| TC-006 (interaction_edge) |  | Use browser Back immediately after logout | User is authenticated, User is on a protected page (e.g., detail) with browser history entry for that page | 1. Click the Logout button<br>2. After the application redirects to the login page, click the browser Back button once | Logout succeeds and session is ended. Navigation back to the protected page is blocked; the login page is shown (or the user is redirected to login) and protected content is not displayed. | medium |
| TC-007 (interaction_edge) |  | Open bookmarked/protected URL in a new tab after logout | User is authenticated in Tab A and has a bookmarked/protected page URL (e.g., checkout), Tab B is a new browser tab | 1. In Tab A, navigate to the protected page and ensure the URL is available/bookmarked<br>2. In Tab A, click the Logout button to end the session<br>3. In Tab B, open the bookmarked/protected URL directly (paste URL or open bookmark) | Logout succeeds in Tab A and session is ended. Opening the protected URL in Tab B is blocked; the login page is shown in Tab B and protected content is not displayed. | medium |
| TC-008 (state_edge) |  | Perform action in a second tab after logging out in the first tab | User is authenticated in both Tab A and Tab B (same session) and Tab B is on a protected page with available actions (e.g., Checkout button) | 1. In Tab A, click the Logout button to end the session<br>2. In Tab B, click a protected-action control (e.g., Checkout or Add to cart) that requires authentication | Logout in Tab A succeeds and session is ended. The action attempted in Tab B is blocked; the user is presented with the login page or an inline authentication-required message and the protected action does not complete. | medium |

---

## Reset App State

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Reset clears a populated cart and resets in-app UI while keeping user logged in | User logged in as <User>, Cart contains one or more items, One or more products in the product list show a 'Remove' button (item is in added state) | 1. Click the 'Reset App State' button | clears cart and resets in-app state (e.g., cart badge and add/remove button states) without logging the user out. Visibly: the cart badge no longer displays an item count; the Cart view shows no items (empty state) if opened; products that previously showed 'Remove' now show 'Add'; the user avatar or username remains visible indicating the user is still logged in. | high |
| TC-002 |  | Reset on an already-empty cart leaves UI in empty state and preserves login | User logged in as <User>, Cart is empty (no items and no cart count displayed) | 1. Click the 'Reset App State' button | clears cart and resets in-app state (e.g., cart badge and add/remove button states) without logging the user out. Visibly: the cart badge remains not showing a count; the Cart view continues to show the empty state with no items; the user avatar or username remains visible indicating the user is still logged in. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user cannot access the Reset App State control | User is not authenticated (not logged in) | 1. Open the application landing/page that normally contains the Reset App State control<br>2. Look for the 'Reset App State' button or link in the UI<br>3. If the button is not visible, attempt to navigate directly to the Reset App State endpoint/URL or invoke the control if reachable | The Reset App State control is not available to unauthenticated users: the 'Reset App State' button is not visible. If the control is directly requested, the user is redirected to the Login page (authentication required) and the app state (cart contents, badges, add/remove button states) remains unchanged. | high |
| TC-004 |  | Expired session blocks Reset App State and does not change cart/state | User had been authenticated but session has expired (user not currently authenticated) | 1. Log in as <user> and add <items> to the cart so the cart badge/count > 0<br>2. Allow the session to expire or simulate an expired session so the app treats the user as unauthenticated<br>3. Attempt to click the visible 'Reset App State' button | Action is blocked due to missing/expired session: user is redirected to the Login page (or an authentication required modal is shown). The cart contents and in-app state remain unchanged (cart badge and add/remove button states unchanged). No reset occurs while the session is expired. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Rapid consecutive clicks of Reset App State button | User is logged in, Cart contains at least one item, Some products show the 'remove' or 'added' in-app button state, App is online | 1. Click the 'Reset App State' button<br>2. Immediately click the 'Reset App State' button again (within one second) | First click succeeds: cart badge shows 0, cart contents view is empty, and add/remove button states are reset to default. Second (rapid) click also succeeds but is a no-op (no additional changes or errors). User remains logged in and no duplicate clears or error toasts appear. | medium |
| TC-006 (interaction_edge) |  | Attempt Reset App State while checkout/payment flow is in progress | User is logged in, Cart contains items, User has initiated checkout and a checkout modal or payment step is active | 1. With the checkout/payment modal open, click the 'Reset App State' button | Reset action is blocked / error shown: a visible inline message or modal prevents clearing the cart while checkout is in progress, the cart and add/remove button states remain unchanged, and the user remains logged in. The UI clearly indicates that reset cannot proceed during the active checkout. | medium |
| TC-007 (data_edge) |  | Click Reset App State while the app is offline (network unavailable) | User is logged in, Cart contains items, App is offline (simulate network disconnected) | 1. Put the device/browser into offline mode<br>2. Click the 'Reset App State' button | Reset succeeds locally: cart badge shows 0 and add/remove button states reset in the UI. A visible offline/pending-sync indicator is shown (e.g., toast or banner) indicating server sync is pending. No logout occurs. If the app requires server confirmation to complete reset, the UI must reflect that the local reset is pending sync rather than silently failing. | low |

---
