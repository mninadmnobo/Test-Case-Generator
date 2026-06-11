# Test Cases — Swaglab

Generated: 2026-06-10T18:50:02.082706Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 87 | 25 | 24 | 38 | 38 | 40 | 9 |

## Login

Total: **15** (positive: 6, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials (standard_user) | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | redirects to Product Inventory page | high |
| TC-002 | WF-002 | Login attempt with locked_out_user shows locked out error | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | high |
| TC-003 | WF-003 | Login with valid username but incorrect password shows invalid credentials error | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Enter 'standard_user' in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | high |
| TC-004 | WF-004 | Submit with missing Username only shows Username required error | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Enter 'secret_sauce' in the Password field<br>2. Click the Login button | Epic sadface: Username is required. | medium |
| TC-005 | WF-005 | Submit with missing Password only shows Password required error | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Enter 'standard_user' in the Username field<br>2. Click the Login button | Epic sadface: Password is required. | medium |
| TC-006 | WF-006 | Submit with both Username and Password missing shows both required errors | User on the Login page, User attempting to log in as <role> (not authenticated) | 1. Ensure both Username and Password fields are empty<br>2. Click the Login button | Epic sadface: Username is required. and Epic sadface: Password is required. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-004 | Submit with Username blank (required text field) | User is on the Login page (unauthenticated) | 1. Leave the Username field blank<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Inline validation error appears on the Username field: "Epic sadface: Username is required."; the form does not submit; user remains on the Login page and is not redirected. | high |
| TC-008 | WF-005 | Submit with Password blank (required password field) | User is on the Login page (unauthenticated) | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | Inline validation error appears on the Password field: "Epic sadface: Password is required."; the form does not submit; user remains on the Login page and is not redirected. | high |
| TC-009 | WF-006 | Submit with both Username and Password blank | User is on the Login page (unauthenticated) | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Inline validation errors appear on both fields: "Epic sadface: Username is required." on Username and "Epic sadface: Password is required." on Password; the form does not submit; user remains on the Login page and is not redirected. | high |
| TC-010 | WF-003 | Login attempt with username not in accepted list (invalid credentials) | User is on the Login page (unauthenticated) | 1. Enter <username not in accepted list> in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | A blocking error banner is shown with the exact message: "Epic sadface: Username and password do not match any user in this service."; the form does not submit; user remains on the Login page and is not redirected. | high |
| TC-011 | WF-002 | Login attempt using locked_out_user (locked account) with correct password | User is on the Login page (unauthenticated) | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | A blocking error banner is shown with the exact message: "Epic sadface: Sorry, this user has been locked out."; the form does not submit; user remains on the Login page and is not redirected. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) |  | Very long Username (200+ chars) with correct shared password | Login page is displayed | 1. Enter a Username consisting of a very long string (>= 200 characters) into the Username field<br>2. Enter the shared password 'secret_sauce' into the Password field<br>3. Click the Login button | Login is blocked; error banner displayed with text: "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-013 (input_edge) |  | Username containing emoji / non-alphanumeric characters with correct shared password | Login page is displayed | 1. Enter a Username that contains emoji and other special Unicode characters into the Username field<br>2. Enter the shared password 'secret_sauce' into the Password field<br>3. Click the Login button | Login is blocked; error banner displayed with text: "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-014 (input_edge) | WF-002 | Username equal to 'locked_out_user' but with leading and trailing whitespace | Login page is displayed | 1. Enter the Username with a single leading space and a single trailing space so the visible text is ' locked_out_user ' into the Username field<br>2. Enter the shared password 'secret_sauce' into the Password field<br>3. Click the Login button | Login is blocked. Observe which of the two behavior variants occurs and record it: either (A) the UI trims whitespace and shows the locked-out error banner: "Epic sadface: Sorry, this user has been locked out." (succeeds as locked-out error), OR (B) whitespace is considered part of the username and the login is blocked with the invalid-credentials banner: "Epic sadface: Username and password do not match any user in this service." (is blocked / error shown). | medium |
| TC-015 (interaction_edge) | WF-001 | Rapid double-click of Login button with valid credentials | Login page is displayed | 1. Enter a valid Username shown in the app's accepted list (e.g. one of the accepted test usernames) into the Username field<br>2. Enter the shared password 'secret_sauce' into the Password field<br>3. Double-click the Login button (two rapid clicks in succession) | Form submits once; user is redirected to the Product Inventory page a single time (Product Inventory page is displayed); no error banner is shown and no duplicate/login-repeat action is performed. | medium |

---

## Product Inventory

Total: **13** (positive: 4, negative: 3, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Product Detail from Product List by clicking product name | User logged in as <role>, A product <product> exists in the inventory | 1. Open the Product Inventory page<br>2. In the Product List, click the <product> Name | opens Product Detail page for the product | high |
| TC-002 | WF-002 | Add a listed product to cart when it is not in cart | User logged in as <role>, A product <product> is listed with InCart == false | 1. Open the Product Inventory page<br>2. Locate the row for <product> in the Product List<br>3. Click the 'Add to cart' button for <product> | adds item to cart; button changes to Remove; cart_count increments | high |
| TC-003 | WF-003 | Remove a product from cart when it is already in cart | User logged in as <role>, A product <product> is listed with InCart == true | 1. Open the Product Inventory page<br>2. Locate the row for <product> in the Product List<br>3. Click the 'Remove' button for <product> | removes item from cart; button changes to Add to cart; cart_count decrements | high |
| TC-004 |  | Sort product list by Price (low–high) | User logged in as <role>, Multiple products with varying names and prices exist in the Product List | 1. Open the Product Inventory page<br>2. Select 'Price (low–high)' from the Sort_By dropdown<br>3. Observe the ordering of rows in the Product List | Product List displays products ordered by price ascending (lowest to highest); rows at the top show the lowest priced products | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user cannot access Product Inventory page | User is not authenticated | 1. Open the Product Inventory page URL in a browser | Access is blocked: the Login page is displayed (user is redirected to authentication) and the Product Inventory content is not shown; no product list or Add/Remove buttons are accessible. | high |
| TC-006 | WF-002 | Attempt to Add to cart when product is already InCart == true | User is logged in as <role>, Product <product> is already in the user's cart (InCart == true) | 1. Navigate to the Product Inventory page<br>2. Locate product <product> in the product list<br>3. Observe the product row shows a 'Remove' button indicating InCart == true<br>4. Attempt to find and click an 'Add to cart' button for product <product> | 'Add to cart' button is not present for product <product>; the row displays a 'Remove' button; cart badge count remains unchanged; the product remains in cart (no state transition occurs). | high |
| TC-007 | WF-003 | Attempt to Remove when product is not InCart == false | User is logged in as <role>, Product <product> is not in the user's cart (InCart == false) | 1. Navigate to the Product Inventory page<br>2. Locate product <product> in the product list<br>3. Observe the product row shows an 'Add to cart' button indicating InCart == false<br>4. Attempt to find and click a 'Remove' button for product <product> | 'Remove' button is not present for product <product>; the row displays an 'Add to cart' button; cart badge count remains unchanged; the product remains out of cart (no state transition occurs). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (state_edge) | WF-002 | Double-click 'Add to cart' on the same product (rapid duplicate clicks) | user must be logged in, Product row exists with InCart == false, cart badge is visible | 1. Navigate to the Product Inventory page<br>2. Click the 'Add to cart' button for the product (first click)<br>3. Immediately (without waiting for UI update) click the same product's 'Add to cart' button again (second click) | Only the first Add action succeeds; the second click is blocked/ignored by the UI. The product row's button changes to 'Remove' and the cart badge increments by one; no duplicate item is added to the cart. | medium |
| TC-009 (interaction_edge) | WF-002 | Click 'Add to cart' then immediately open Product Detail before inventory UI updates | user must be logged in, Product row exists with InCart == false, product Name link is available | 1. Navigate to the Product Inventory page<br>2. Click the 'Add to cart' button for the product<br>3. Immediately click the product Name (link) to open the Product Detail page before the inventory row's button text updates | The Add action succeeds; on the Product Detail page the cart badge reflects the new item and the product's action control shows 'Remove'. Navigating to the detail page does not cause a duplicate add; only one add succeeds. | medium |
| TC-010 (state_edge) | WF-002 | Rapidly add two different products to cart (concurrent rapid actions across rows) | user must be logged in, At least two product rows exist with InCart == false, cart badge is visible | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' for product row A<br>3. Immediately click 'Add to cart' for product row B (without waiting for step 2 confirmation) | Both Add actions succeed (are processed); both product rows change their button text to 'Remove' and the cart badge increments by two relative to its initial value. No duplicate adds for the same product occur. | medium |
| TC-011 (interaction_edge) | WF-001 | Add on Product Detail then use browser Back to Inventory (no duplicate add on Back) | user must be logged in, Product row exists with InCart == false | 1. Navigate to the Product Inventory page<br>2. Click the product Name to open the Product Detail page<br>3. On the Product Detail page, click 'Add to cart'<br>4. After the Add action completes, use the browser Back button to return to the Product Inventory page | The Add action on the Product Detail page succeeds; after using Back the Product Inventory page shows that product's button as 'Remove' and the cart badge reflects a single increment. Returning via Back does not trigger a second add; any additional add attempt is blocked. | medium |
| TC-012 (state_edge) |  | Rapid toggle sequence Add -> Remove -> Add on same product (idempotency and serialization) | user must be logged in, Product row exists with InCart == false, cart badge is visible | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' for the product<br>3. Immediately click the product's 'Remove' button as soon as it appears<br>4. Immediately click 'Add to cart' again | Actions are serialized; each intended state transition that succeeds updates the UI. The Add action(s) that succeed cause the cart badge to increment and Remove actions that succeed decrement it. The final visible button state equals the last successful action and the cart badge reflects the net change. No action results in duplicate/inconsistent cart entries (each individual toggle either succeeds or is blocked). | medium |
| TC-013 (interaction_edge) |  | Sort inventory after adding an item (InCart state persists after reordering) | user must be logged in, At least one product row exists with InCart == false, cart badge is visible | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' for a product<br>3. Select 'Price (low–high)' from the Sort_By dropdown | The Add action succeeds and the product retains InCart state after reordering. The product's button remains 'Remove' after the sort and the cart badge is unchanged by the sort operation (the earlier Add remains counted). | low |

---

## Product Detail

Total: **11** (positive: 4, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add a product to cart when product is not in cart | User logged in as <role>, Product Detail page open for <product>, product not in cart | 1. On the Product Detail page, click the 'Add to cart' button | adds product to cart; the 'Add to cart' button is replaced by a 'Remove' button on the Product Detail page indicating the product is in the cart | high |
| TC-002 | WF-002 | Remove a product from cart when product is already in cart | User logged in as <role>, Product Detail page open for <product>, product in cart | 1. On the Product Detail page, click the 'Remove' button | removes product from cart; the 'Remove' button is replaced by an 'Add to cart' button on the Product Detail page indicating the product is not in the cart | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via Back to products link | User logged in as <role>, Product Detail page open for <product> | 1. Click the 'Back to products' link | navigates to Product Inventory page | medium |
| TC-004 | WF-004 | Open Shopping Cart by clicking the cart icon | User logged in as <role>, Product Detail page open for <product> | 1. Click the Cart icon | navigates to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt 'Add to cart' when product is already in cart (precondition not met) | Product is already in the cart (product_cart_state == InCart), User is on the Product Detail page for <product> | 1. Open the Product Detail page for <product> (page reflects state InCart)<br>2. Attempt to click the 'Add to cart' button | 'Add to cart' button is not present / clickable on the page; the page displays the 'Remove' button instead. The cart contents remain unchanged (no duplicate entry for <product> is created); no successful add-to-cart action occurs and no navigation happens. | high |
| TC-006 | WF-002 | Attempt 'Remove' when product is not in cart (precondition not met) | Product is not in the cart (product_cart_state == NotInCart), User is on the Product Detail page for <product> | 1. Open the Product Detail page for <product> (page reflects state NotInCart)<br>2. Attempt to click the 'Remove' button | 'Remove' button is not present / clickable on the page; the page displays the 'Add to cart' button instead. The cart contents remain unchanged (no removal of <product> occurs); no successful remove action occurs and no navigation happens. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (state_edge) | WF-001 | Rapid double-click 'Add to cart' when product is NotInCart | User is on the Product Detail page for the product, Product is in state: NotInCart (page shows an 'Add to cart' button) | 1. Click the 'Add to cart' button<br>2. Immediately click the 'Add to cart' button a second time (before UI state refresh completes) | First click succeeds; the action adds the product to cart and the Product Detail button updates to show 'Remove'. Second click is blocked / error shown: the second Add action is not performed and the UI remains showing 'Remove' (no duplicate add occurs). | medium |
| TC-008 (state_edge) | WF-002 | Rapid double-click 'Remove' when product is InCart | User is on the Product Detail page for the product, Product is in state: InCart (page shows a 'Remove' button) | 1. Click the 'Remove' button<br>2. Immediately click the 'Remove' button a second time (before UI state refresh completes) | First click succeeds; the action removes the product from cart and the Product Detail button updates to show 'Add to cart'. Second click is blocked / error shown: the second Remove action is not performed and the UI remains showing 'Add to cart'. | medium |
| TC-009 (interaction_edge) | WF-001 | Click 'Add to cart' then immediately click the Cart icon | User is on the Product Detail page for the product, Product is in state: NotInCart (page shows an 'Add to cart' button), Cart icon is visible on the page | 1. Click the 'Add to cart' button<br>2. Immediately click the 'Cart icon' link | The Add action succeeds; the Product Detail button updates to 'Remove'. The Cart icon navigation succeeds and the app navigates to the Shopping Cart page. The rapid sequence does not cause the Add action to be dropped (Add succeeds) and navigation to Shopping Cart succeeds. | low |
| TC-010 (interaction_edge) | WF-002 | Click 'Remove' then immediately click 'Back to products' link | User is on the Product Detail page for the product, Product is in state: InCart (page shows a 'Remove' button), Back to products link is visible | 1. Click the 'Remove' button<br>2. Immediately click the 'Back to products' link | The Remove action succeeds; the Product Detail button updates to 'Add to cart'. The Back to products navigation succeeds and the app navigates to the Product Inventory page. The rapid sequence does not result in the Remove action being lost (Remove succeeds) and navigation succeeds. | low |
| TC-011 (state_edge) |  | Rapid toggle: click 'Add to cart' then 'Remove' immediately, repeated quickly | User is on the Product Detail page for the product, Product is in state: NotInCart (page shows an 'Add to cart' button) | 1. Click the 'Add to cart' button<br>2. Immediately click the 'Remove' button when it appears<br>3. Immediately click the 'Add to cart' button again<br>4. Immediately click the 'Remove' button again | Each first action of a pair (Add then Remove) succeeds in sequence and the UI reflects the current state after each action ('Add to cart' toggles to 'Remove' after a successful add; 'Remove' toggles to 'Add to cart' after a successful remove). Any attempted action that violates its precondition (e.g., attempting Add when already InCart or Remove when NotInCart) is blocked / error shown and the UI remains in the correct current state. | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the shopping cart via row Remove button | User logged in as <role>, Shopping Cart page is open with at least one item <cart item> | 1. On the Shopping Cart page, locate the row for <cart item><br>2. Click the Remove button on the <cart item> row | The row for <cart item> is no longer visible in the Shopping Cart table (removes item from cart) | high |
| TC-002 | WF-002 | Navigate to Product Inventory using Continue Shopping link | User logged in as <role>, Shopping Cart page is open | 1. Click the Continue Shopping link in the action bar | The Product Inventory page is displayed (navigates to Product Inventory) | high |
| TC-003 | WF-003 | Begin checkout using Checkout button | User logged in as <role>, Shopping Cart page is open with at least one item <cart item> | 1. Click the Checkout button in the action bar | The Checkout page or checkout flow is displayed (begins checkout) | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Row Remove action fails to remove the item | User is on the Shopping Cart page with at least one item listed in the cart table | 1. Open the Shopping Cart page<br>2. Locate the <cart item row> in the Shopping Cart table<br>3. Click the 'Remove' button for the <cart item row> | An inline error message is shown adjacent to the row indicating the removal failed (e.g., removal could not be completed); the <cart item row> remains visible in the Shopping Cart table and the cart item count does not decrease (the item is not removed). | high |
| TC-005 | WF-002 | Continue Shopping link does not navigate to Product Inventory | User is on the Shopping Cart page | 1. Open the Shopping Cart page<br>2. Click the 'Continue Shopping' link in the action bar | The application remains on the Shopping Cart page (Product Inventory is not displayed); a visible error indicator (page-level banner or toast) informs the user that navigation to Product Inventory failed; no navigation occurs. | medium |
| TC-006 | WF-003 | Checkout button does not begin checkout flow | User is on the Shopping Cart page | 1. Open the Shopping Cart page<br>2. Click the 'Checkout' button in the action bar | Clicking 'Checkout' does not begin the checkout process: the user remains on the Shopping Cart page (no checkout screen or flow appears) and a visible error indicator (inline message, toast, or disabled state) notifies the user that checkout could not be started; no transition to checkout occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapid double-remove on single cart item | Cart contains exactly one item in the Shopping Cart Table | 1. On the Shopping Cart page, locate the single item's row<br>2. Click the Remove button for that row<br>3. Immediately click the same Remove button again (within 1 second of the first click) | First Remove action succeeds; the item is removed from the Shopping Cart Table and the table shows zero rows. The second Remove attempt is blocked / error shown (Remove has no effect and does not cause a second removal). The UI shows the Remove control disabled or an inline indication that the item is no longer in the cart. | medium |
| TC-008 (interaction_edge) | WF-003 | Remove last item then immediately trigger Checkout | Cart contains exactly one item in the Shopping Cart Table | 1. On the Shopping Cart page, locate the single item's row<br>2. Click the Remove button for that row<br>3. Immediately click the Checkout button in the Shopping_Cart_Actions bar (within 1 second of the Remove click) | Remove action succeeds; the item is removed and the Shopping Cart Table shows zero rows. The immediate Checkout attempt is blocked / error shown (checkout does not begin). The UI prevents starting checkout with an empty cart and displays a visible indicator that checkout cannot proceed because there are no items. | medium |
| TC-009 (input_edge) |  | Very long and unicode/emoji-rich product description displayed in cart | A product with a Description that is a very long string (200+ characters) containing emoji and special unicode characters has been added to the cart | 1. Navigate to the Shopping Cart page | Loading the Shopping Cart page with the long/unicode-rich description succeeds; the Description column displays the text (either the full string or a UI-truncated version with a visible indication such as ellipsis/tooltip). No layout break or UI error is shown; the row's Remove button remains present and functional. | low |

---

## Checkout - Information

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with all required fields filled proceeds to Overview | User logged in as <role>, Checkout - Information page is open with the First Name, Last Name and Zip/Postal Code fields visible | 1. Enter <first name> in the First Name field<br>2. Enter <last name> in the Last Name field<br>3. Enter <zip/postal code> in the Zip/Postal Code field<br>4. Click the Continue button | proceeds to Overview step and the Overview step screen is displayed | high |
| TC-002 | WF-002 | Cancel from Information returns to Shopping Cart | User logged in as <role>, Checkout - Information page is open | 1. Click the Cancel button | returns to Shopping Cart and the Shopping Cart page is displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Continue blocked when First Name is missing (representative required text field) | User is on Checkout - Information page | 1. Open the Checkout - Information page<br>2. Leave the First Name field blank<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid postal code> in the Zip/Postal Code field<br>5. Click the Continue button | Form submission is blocked; the page does not navigate to the Overview step; an error banner is displayed containing "Error: First Name is required" (the First Name required validation is shown) | high |
| TC-004 | WF-001 | Continue blocked when ALL required fields are empty | User is on Checkout - Information page | 1. Open the Checkout - Information page<br>2. Leave the First Name field blank<br>3. Leave the Last Name field blank<br>4. Leave the Zip/Postal Code field blank<br>5. Click the Continue button | Form submission is blocked; the page does not navigate to the Overview step; an error banner is displayed containing the required-field messages: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required"; no navigation to Overview occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Whitespace-only input in required fields is treated as empty | User is on the Checkout - Information form | 1. In the First Name field enter a value consisting only of spaces (one or more) and do not add any other visible characters<br>2. In the Last Name field enter a normal valid-looking value<br>3. In the Zip/Postal Code field enter a normal valid-looking value<br>4. Click the Continue button | Form submission is blocked; an error banner is displayed and the First Name field shows the required-field error text "Error: First Name is required" (indicating whitespace-only input is treated as empty) | medium |
| TC-006 (input_edge) |  | Very long strings in name and postal code fields | User is on the Checkout - Information form | 1. Enter a very long string (200+ characters) in the First Name field<br>2. Enter a very long string (200+ characters) in the Last Name field<br>3. Enter a very long string (200+ characters) in the Zip/Postal Code field<br>4. Click the Continue button | Form submits successfully and proceeds to the Overview step; the Overview step displays the saved First Name, Last Name and Zip/Postal Code values — the full entered strings are shown (i.e., long input is accepted rather than silently failing). If the UI truncates or shows a truncation indicator, that truncation is visible on the Overview step (the test expects either full value displayed or a visible truncation indicator). | low |
| TC-007 (input_edge) |  | Names and postal code containing special characters, emoji, and Unicode | User is on the Checkout - Information form | 1. Enter a string containing special characters and punctuation (e.g., accents, non-Latin script, emoji) in the First Name field<br>2. Enter a string containing special characters and punctuation in the Last Name field<br>3. Enter a string containing special characters in the Zip/Postal Code field<br>4. Click the Continue button | Form submits successfully and proceeds to the Overview step; the Overview step displays the entered values with special characters/emoji rendered or shown as entered (i.e., special/unicode characters are accepted). If the UI shows a validation error for unsupported characters, that error is visible and blocks submission. | low |
| TC-008 (interaction_edge) | WF-001 | Rapid double-click of Continue should not cause duplicate progression | User is on the Checkout - Information form, All required fields (First Name, Last Name, Zip/Postal Code) are filled with valid values | 1. Click the Continue button twice in rapid succession (two clicks within one second) | Proceeds to the Overview step only once; the UI does not perform duplicate navigations and no duplicate side-effects are visible (user lands on Overview and no additional error or duplicate processing is shown). The second click is ignored or prevented and no second Overview navigation occurs. | medium |

---

## Checkout - Overview

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish from Overview navigates to confirmation | User logged in as <role>, Cart contains at least one item, Payment and shipping information saved for the order | 1. Navigate to the Checkout Overview page<br>2. Verify the Order Summary is visible with a list of cart items<br>3. Verify the Totals section displays Item total, Tax, and Total<br>4. Verify payment method and shipping information are shown in the overview<br>5. Click the Finish button | completes order and navigates to confirmation page; the Order Confirmation page is displayed (a confirmation header is visible and an order summary is shown) | high |
| TC-002 | WF-002 | Cancel from Overview exits checkout and closes wizard | User logged in as <role>, Cart contains at least one item, Payment and shipping information saved for the order | 1. Navigate to the Checkout Overview page<br>2. Verify the Order Summary and Totals section (Item total, Tax, Total) are visible<br>3. Verify payment method and shipping information are shown<br>4. Click the Cancel button | exits checkout; the Checkout Overview wizard is closed and the Checkout Overview is no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to run Finish from Confirmation page after order is completed | User has a populated cart and is on the Checkout Overview step | 1. On Checkout Overview, click the Finish button<br>2. Observe navigation to the Confirmation page (order completed)<br>3. On the Confirmation page, attempt to locate and click the Finish button | Finish button is not present on the Confirmation page or is rendered disabled; attempting to invoke Finish does not create a second order and does not navigate away from the Confirmation page — the order remains in the completed state and no duplicate order is created (no new confirmation is shown). | high |
| TC-004 | WF-002 | Attempt to use Cancel after checkout has already exited (on Confirmation page) | An order has just been completed and the user is on the Confirmation page | 1. From Checkout Overview click the Finish button to complete the order and arrive at the Confirmation page<br>2. On the Confirmation page, attempt to locate and click the Cancel button | Cancel button is not visible on the Confirmation page; if Cancel is present and clicked it does not 'exit checkout' again or revert the completed order — the user remains on the Confirmation page and the completed order state is unchanged. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click Finish — prevent duplicate completion | Overview step is visible with at least one cart item listed, Payment and shipping information are displayed | 1. Click the Finish button on the Overview step<br>2. Immediately (within one second) click the Finish button again | First click succeeds: the app navigates to the confirmation page. The immediate second click is blocked: the Finish button becomes disabled or shows a loading state and no second navigation occurs (no duplicate confirmation page load). | medium |
| TC-006 (interaction_edge) | WF-001 | Browser Back after successful Finish — block duplicate submission | Overview step is visible with cart items, payment and shipping info | 1. Click the Finish button on the Overview step<br>2. Wait until the confirmation page loads<br>3. Press the browser Back button<br>4. On the Overview step that is shown after Back, click the Finish button | Initial Finish click succeeds: navigates to the confirmation page. After pressing Back, attempting to Finish again is blocked: clicking Finish is blocked (button disabled or inline message shown) and no new confirmation navigation occurs (no duplicate completion). | medium |
| TC-007 (interaction_edge) | WF-002 | Rapid double-click Cancel — prevent duplicate exit actions | Overview step is visible with at least one cart item | 1. Click the Cancel button on the Overview step<br>2. Immediately (within one second) click the Cancel button again | First Cancel click succeeds: the app exits checkout (navigates away). The immediate second click is blocked: the Cancel button becomes disabled and no duplicate navigation or repeated exit action occurs. | medium |
| TC-008 (input_edge) |  | Very long product name in order summary — layout and finish behavior | Cart contains at least one item whose product name is extremely long (200+ characters), Overview step is reachable and will display cart items | 1. Open the Checkout Overview step<br>2. Observe how the long product name is rendered in the order summary<br>3. Click the Finish button | Overview displays the long product name without breaking the totals or overlapping other UI: the name is truncated with an ellipsis or wrapped so totals remain visible. Clicking Finish succeeds: the app navigates to the confirmation page. | low |

---

## Checkout - Confirmation

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Back Home returns to Product Inventory and clears cart | User logged in as <Customer> | 1. Navigate to the Checkout Confirmation page<br>2. Verify the Back Home button is visible<br>3. Click the Back Home button | navigates to Product Inventory and clears the cart | high |
| TC-002 |  | Confirmation page displays success message after order | User logged in as <Customer> | 1. Navigate to the Checkout Confirmation page | Confirmation page displays "Thank you for your order!" | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Clicking Back Home does not navigate to Product Inventory and cart is not cleared | User has completed checkout and is on the Confirmation page, Shopping cart contains <items to be cleared> prior to clicking Back Home | 1. Verify the Confirmation page is displayed after order completion<br>2. Click the Back Home button | Click has no effect: user remains on the Confirmation page (URL remains <confirmation page URL>); Product Inventory page is not loaded; shopping cart still contains <items to be cleared>. No navigation occurs and no indication of cart clearance is shown. | high |
| TC-004 | WF-001 | Back Home button missing or disabled on Confirmation page prevents return and cart clearance | User has completed checkout and is on the Confirmation page, Shopping cart contains <items to be cleared> prior to attempting navigation | 1. Navigate to the Confirmation page after placing an order<br>2. Check for the presence and enabled state of the Back Home button | Back Home button is not visible or is rendered disabled; user cannot return to Product Inventory; shopping cart still contains <items to be cleared>. No navigation or cart-clear occurs when the control is absent or disabled. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click Back Home | User has completed checkout and the Confirmation page with the success message is displayed, Cart contained <items> immediately prior to checkout | 1. Click the "Back Home" button on the Confirmation page<br>2. Immediately click the "Back Home" button again within one second | First click navigates to Product Inventory and clears the cart; Product Inventory page is displayed and the cart is empty (no items shown); the second click is handled gracefully with no UI error and does not cause duplicate navigation or create a duplicate order — operation succeeds. | medium |
| TC-006 (interaction_edge) | WF-001 | Press browser Back after using Back Home | User has completed checkout and the Confirmation page with the success message is displayed, Cart contained <items> immediately prior to checkout | 1. Click the "Back Home" button on the Confirmation page<br>2. On the Product Inventory page, click the browser Back button | Using the browser Back button does not recreate the cart or produce a duplicate order; the user may return to the Confirmation page or previous URL but the cart remains empty and no additional order appears — operation succeeds (no duplicate order and cart cleared). | medium |
| TC-007 (interaction_edge) | WF-001 | Click Back Home in a second tab after cart already cleared in first tab | User has two browser tabs open, both displaying the Confirmation page with the success message, Cart contained <items> immediately prior to checkout | 1. In Tab A, click the "Back Home" button<br>2. In Tab B, click the "Back Home" button | Tab A navigation succeeds and clears the cart; Tab B click navigates to Product Inventory but finds the cart already empty; no duplicate orders are created and no UI error is shown — operation succeeds. | medium |
| TC-008 (interaction_edge) | WF-001 | Refresh the page immediately after clicking Back Home (mid-navigation) | User has completed checkout and the Confirmation page with the success message is displayed, Cart contained <items> immediately prior to checkout | 1. Click the "Back Home" button on the Confirmation page<br>2. Immediately refresh the browser page (reload) before Product Inventory fully loads | Either the user ends on Product Inventory or the Confirmation page is re-displayed, but in all cases the cart remains cleared and no duplicate order is created; no persistent UI error is shown after reload — operation succeeds. | low |

---

## Logout

Total: **8** (positive: 1, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Logout button ends session and returns to Login page | User logged in as <role>, Logout button is visible in the application header | 1. Click the Logout button | ends session and redirects to login page; protected pages (inventory, detail, cart, checkout) are not accessible without logging in again | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt Logout action while not authenticated (direct URL) | User is not logged in (Unauthenticated session) | 1. As an unauthenticated user, navigate directly to the Logout endpoint (e.g., /logout) or click any logout link if present | Logout action is blocked: application redirects to the Login page; user remains unauthenticated (no session is ended because none existed); no protected resource is accessed. If a redirect occurs, the displayed page is the Login page (no successful logout state transition). | high |
| TC-003 |  | Logout control is not visible to unauthenticated users | User is not logged in (Unauthenticated session) | 1. Open the application homepage or header as an unauthenticated user<br>2. Attempt to locate a Logout button/control in the UI | Logout control is not present/visible in the UI for unauthenticated users; tester cannot click a Logout button. The UI does not offer the Logout action when precondition 'user must be logged in' is not met. | high |
| TC-004 | WF-001 | Access protected page after performing Logout (session ended) | User is logged in as <role> | 1. Log in as <role><br>2. Click the Logout button<br>3. After being redirected to the Login page, attempt to navigate to a protected page (e.g., inventory, detail, cart, or checkout) | After Logout, application redirects to the Login page; when attempting to access a protected page, the application blocks access and redirects to the Login page (protected page content is not shown). The user's session remains terminated (no access to protected pages without logging in again). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-001 | Rapid double-click Logout button | User is logged in, User is on any authenticated page (e.g., inventory) | 1. Click the Logout button once<br>2. Immediately click the Logout button a second time (within <1 second) | First click succeeds: session ends and user is redirected to the login page. Second click is blocked / has no effect (no second session change) and the UI remains on the login page (no duplicate redirects or error dialogs). | medium |
| TC-006 (interaction_edge) | WF-001 | Attempt direct navigation to protected page immediately after Logout | User is logged in, User is on any authenticated page | 1. Click the Logout button<br>2. In the address bar, enter the URL of a protected page (e.g., inventory/detail/cart/checkout) and press Enter immediately after the redirect to login | Logout succeeds: user is redirected to the login page. Direct navigation to the protected page is blocked / error shown: the app shows the login page (or an authentication required message) and does not display the protected content. | medium |
| TC-007 (interaction_edge) | WF-001 | Use browser Back button after Logout to attempt returning to a protected page | User is logged in, User navigated from a protected page to another page within the app | 1. Click the Logout button<br>2. After being redirected to the login page, press the browser Back button once | Logout succeeds: session ends and user is on the login page. Using the Back button is blocked / has no effect in restoring authenticated access: the app remains on the login page or redirects back to login when attempting to view the protected page. | medium |
| TC-008 (state_edge) | WF-001 | Click Logout while a protected action/request is in progress | User is logged in, User has initiated a protected action that triggers a network request (e.g., start Checkout submission or save on a protected detail page) | 1. Start the protected action that issues a network request (e.g., click Submit on Checkout)<br>2. While the request is pending, click the Logout button | Logout succeeds: session ends and user is redirected to the login page. The pending protected request is not allowed to complete with an authenticated response; subsequent attempts to access resulting protected pages or actions are blocked / error shown (user remains unauthenticated and must log in again). | medium |

---

## Reset App State

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State clears cart and resets in-app UI without logging out | User logged in as <role>, App has items in the cart and at least one product shows the 'Remove' button (indicating added state) | 1. Navigate to the screen where the 'Reset App State' button is visible<br>2. Click the 'Reset App State' button | clears cart and resets in-app state (cart badge and add/remove button states) without logging the user out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user cannot perform Reset App State | User is not authenticated (logged out) | 1. Open the application page that normally contains the Reset App State button<br>2. Attempt to click the Reset App State button | User is redirected to the login page (login screen is displayed); Reset App State action is not performed; cart contents and in-app state (cart badge and add/remove button states) remain unchanged | high |
| TC-003 | WF-001 | User with wrong role cannot access Reset App State | User is authenticated as <different role> (not the required <role> listed for this workflow) | 1. Login as <different role><br>2. Navigate to the page that contains the Reset App State control<br>3. Attempt to locate and click the Reset App State button | Reset App State button is not visible or is disabled for this user (UI does not present an actionable Reset App State control); attempting to click does nothing; cart contents and in-app state (cart badge and add/remove button states) remain unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (boundary) | WF-001 | Reset when cart is already empty (idempotence) | User is logged in, Cart currently has <0 items> (cart badge is not shown or shows 0), Add/remove buttons for products are in their default 'Add' state | 1. Click the 'Reset App State' button | Click succeeds: cart badge remains hidden or shows 0, add/remove buttons remain or revert to default 'Add' state, the user remains logged in (user avatar or account menu remains visible); no error is shown | low |
| TC-005 (boundary) | WF-001 | Reset when cart has the minimum non-empty contents (single item) | User is logged in, Cart currently has <1 item> (cart badge shows non-zero), Add/remove button for the item reflects 'Remove' state | 1. Click the 'Reset App State' button | Click succeeds: cart badge is cleared (hidden or shows 0) and the item is no longer present in the cart UI, add/remove buttons for items revert to default 'Add' state, the user remains logged in (no logout or sign-in prompt); UI shows no residual 'removed' indicators | medium |
| TC-006 (interaction_edge) | WF-001 | Rapid consecutive presses of Reset App State | User is logged in, Cart currently has items (cart badge shows >0), Reset App State button is visible and enabled | 1. Click the 'Reset App State' button<br>2. Immediately click the 'Reset App State' button again within a short interval (before UI has a chance to show a success toast or full redraw) | First click succeeds and clears the cart and resets in-app state; the immediate second click either is ignored by the UI or succeeds idempotently but results in the same end state (cart cleared, add/remove buttons in default 'Add' state) and the user remains logged in. No duplicate items are created or removed, and no error is shown | medium |
| TC-007 (state_edge) | WF-001 | Press Reset while an Add-to-cart action is in progress | User is logged in, An item's Add button transitions to an in-progress state when clicked (e.g., shows loading indicator), Cart may be empty or contain items | 1. Click an item's 'Add' button so the button enters its in-progress/loading state<br>2. Before the add completes, click the 'Reset App State' button | Reset action succeeds: any partially added item is not left in the cart (cart badge ends up cleared or in the expected post-reset state), the in-progress Add button returns to its default 'Add' state (no stuck loading indicator), the user remains logged in, and no additional item appears in the cart after the original add operation completes (no delayed/duplicate adds); no error is shown | medium |

---
