# Test Cases — Swaglab

Generated: 2026-06-09T09:06:35.194174Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 88 | 26 | 25 | 37 | 42 | 34 | 12 |

## Login

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials redirects to Product Inventory | User on Login page, User logged out, Test accounts (including 'standard_user') are available | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | authenticates user and redirects to Product Inventory page | high |
| TC-002 | WF-002 | Login attempt by locked_out_user shows locked account error | User on Login page, User logged out, Test accounts (including 'locked_out_user') are available | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-003 | WF-003 | Login with invalid credentials shows mismatch error | User on Login page, User logged out | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-004 | WF-004 | Submitting with missing Username shows required-username error | User on Login page, User logged out | 1. Leave the Username field empty<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-005 | WF-005 | Submitting with missing Password shows required-password error | User on Login page, User logged out | 1. Enter <valid username> in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-004 | Submit with Username blank (required Username validation) | User is on the Login page, User is not authenticated | 1. Ensure the Username field is empty<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | Form does not submit; an error banner displays: "Epic sadface: Username is required." and the Username field shows an inline required validation; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-007 | WF-005 | Submit with Password blank (required Password validation) | User is on the Login page, User is not authenticated | 1. Enter <valid username> in the Username field<br>2. Ensure the Password field is empty<br>3. Click the Login button | Form does not submit; an error banner displays: "Epic sadface: Password is required." and the Password field shows an inline required validation; user remains on the Login page (no redirect to Product Inventory). | high |
| TC-008 |  | Submit with both Username and Password blank (all required fields empty) | User is on the Login page, User is not authenticated | 1. Ensure the Username field is empty<br>2. Ensure the Password field is empty<br>3. Click the Login button | Form does not submit; error banners display both "Epic sadface: Username is required." and "Epic sadface: Password is required."; both fields show required validation indicators; user remains on the Login page (no redirect). | high |
| TC-009 | WF-002 | Attempt login with locked_out_user account (locked-out user constraint) | User is on the Login page, User is not authenticated | 1. Enter 'locked_out_user' in the Username field<br>2. Enter <correct shared password> in the Password field<br>3. Click the Login button | Authentication is blocked; an error banner displays exactly: "Epic sadface: Sorry, this user has been locked out."; user is not authenticated and is not redirected to the Product Inventory page. | high |
| TC-010 | WF-003 | Attempt login with credentials that do not match any user (invalid credentials) | User is on the Login page, User is not authenticated | 1. Enter <unknown username> in the Username field<br>2. Enter <incorrect password> in the Password field<br>3. Click the Login button | Authentication is blocked; an error banner displays exactly: "Epic sadface: Username and password do not match any user in this service."; user is not authenticated and remains on the Login page (no redirect). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) | WF-001 | Username with leading and trailing whitespace that otherwise matches a valid user | Login page is displayed, A valid test user exists in the service (one of the listed test usernames) | 1. Enter a username in the Username field that has leading and trailing whitespace but is otherwise identical to a known valid username (e.g. ' <valid username> ')<br>2. Enter the shared password in the Password field<br>3. Click the Login button | Login is blocked; error banner 'Epic sadface: Username and password do not match any user in this service.' is shown | medium |
| TC-012 (boundary) | WF-002 | Exact-match boundary for locked_out_user vs one-character difference (trailing space) | Login page is displayed, Test user 'locked_out_user' exists in the service | 1. Enter "locked_out_user " (locked_out_user plus one trailing space) in the Username field<br>2. Enter the shared password in the Password field<br>3. Click the Login button | Login is blocked; error banner 'Epic sadface: Username and password do not match any user in this service.' is shown (the input does not match the exact locked_out_user equality condition) | medium |
| TC-013 (input_edge) | WF-001 | Username that differs only by letter case from a valid username | Login page is displayed, A valid test user exists in the service | 1. Enter a username in the Username field that is identical to a known valid username except for letter case differences (e.g. change uppercase/lowercase of one or more letters)<br>2. Enter the shared password in the Password field<br>3. Click the Login button | Login is blocked; error banner 'Epic sadface: Username and password do not match any user in this service.' is shown | medium |
| TC-014 (interaction_edge) | WF-001 | Rapid double-click of Login with valid credentials | Login page is displayed, A valid test user and the shared password are known | 1. Enter a valid username in the Username field<br>2. Enter the shared password in the Password field<br>3. Click the Login button<br>4. Immediately click the Login button again within one second of the first click | First submission succeeds and redirects to the Product Inventory page; the immediate second click is ignored and does not produce an additional navigation or an error banner | medium |

---

## Product Inventory

Total: **15** (positive: 6, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Product Detail by clicking product Name | User logged in as <role> | 1. Navigate to the Product Inventory page<br>2. In the Products table, click the <target product> Name column cell | opens Product Detail page | high |
| TC-002 | WF-002 | Open Product Detail by clicking product Image | User logged in as <role> | 1. Navigate to the Product Inventory page<br>2. In the Products table, click the <target product> Image | opens Product Detail page | high |
| TC-003 | WF-003 | Add a product to the cart from the Products table when product is not in cart | User logged in as <role>, The <target product> is not in the cart | 1. Navigate to the Product Inventory page<br>2. In the row for <target product>, click the Add to cart button | adds item to cart; changes button to Remove; increments cart badge count | high |
| TC-004 | WF-004 | Remove a product from the cart from the Products table when product is in cart | User logged in as <role>, The <target product> is in the cart | 1. Navigate to the Product Inventory page<br>2. In the row for <target product>, click the Remove button | removes item from cart; changes button to Add to cart; decrements cart badge count | high |
| TC-005 |  | Sort products by Price (Low→High) using the Sort dropdown | User logged in as <role> | 1. Navigate to the Product Inventory page<br>2. Open the Sort dropdown<br>3. Select 'Price (Low–High)' from the Sort dropdown | Products table displays rows sorted by Price (Low→High); product Prices increase from the top row to subsequent rows | medium |
| TC-006 |  | Sort products by Name (Z→A) using the Sort dropdown | User logged in as <role> | 1. Navigate to the Product Inventory page<br>2. Open the Sort dropdown<br>3. Select 'Name (Z–A)' from the Sort dropdown | Products table displays rows sorted by Name (Z→A); product Names appear in descending alphabetical order from top to bottom | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Unauthenticated user cannot access Product Inventory page | user is logged out | 1. Open the Product Inventory page URL in the browser without logging in | User is redirected to the Login page; the Products table is not displayed on the page (no product rows, no sort dropdown, no Add/Remove buttons). | high |
| TC-008 | WF-001 | Unauthenticated user cannot open Product Detail by clicking product Name | user is logged out, a product <product> exists | 1. Attempt to open the Product Detail page for <product> by navigating directly to its Product Detail URL (or by clicking the product Name link) while not logged in | User is redirected to the Login page; Product Detail page for <product> does not open and product details are not displayed. | high |
| TC-009 | WF-002 | Unauthenticated user cannot open Product Detail by clicking product Image | user is logged out, a product <product> exists with an image | 1. Attempt to open the Product Detail page for <product> by navigating directly to its Product Detail URL (or by clicking the product Image) while not logged in | User is redirected to the Login page; Product Detail page for <product> does not open and product details are not displayed. | high |
| TC-010 | WF-003 | Add to cart control is not available for a product that is already in the cart | user is logged in as <role>, <product> is already in the user's cart | 1. Log in as <role><br>2. Ensure <product> is present in the cart (use the UI to add it if needed)<br>3. Navigate to the Product Inventory page<br>4. Locate the row for <product> | The row for <product> does not display an 'Add to cart' button. Instead the row displays a 'Remove' button. There is no visible control to perform 'Add to cart' for that product and the cart badge count remains unchanged when attempting to find/click an Add control (no successful add occurs). | high |
| TC-011 | WF-004 | Remove control is not available for a product that is not in the cart | user is logged in as <role>, <product> is not present in the user's cart | 1. Log in as <role><br>2. Ensure <product> is not present in the cart (use the UI to remove it if needed)<br>3. Navigate to the Product Inventory page<br>4. Locate the row for <product> | The row for <product> does not display a 'Remove' button. Instead the row displays an 'Add to cart' button. There is no visible control to perform 'Remove' for that product and the cart badge count remains unchanged because no removal is possible. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (interaction_edge) | WF-003 | Rapid double-click Add to cart on a single product | User is logged in and on the Product Inventory page, The target product is visible in the products table, The target product is NOT in the cart (button shows 'Add to cart'), Cart badge shows current count | 1. Click the target product's 'Add to cart' button<br>2. Immediately click the same product's 'Add to cart' button a second time (before UI updates) | First Add to cart click succeeds; second click is ignored/blocked by the UI. The product row button displays 'Remove'; the cart badge increments by exactly one; only one instance of the product appears in the cart UI. | medium |
| TC-013 (interaction_edge) | WF-003 | Click Add then immediately click Remove before initial action completes | User is logged in and on the Product Inventory page, The target product is visible in the products table, The target product is NOT in the cart (button shows 'Add to cart'), Cart badge shows current count | 1. Click the target product's 'Add to cart' button<br>2. Immediately click the same product's 'Remove' button (before the first action's UI response completes) | The initial Add to cart action succeeds; the immediate Remove click is ignored/blocked until the add completes. Final visible state is the product in cart: button displays 'Remove' and the cart badge has incremented by one. No duplicate additions or negative counts occur. | medium |
| TC-014 (interaction_edge) | WF-001 | Click product Name then Image in quick succession to open Product Detail | User is logged in and on the Product Inventory page, The target product is visible in the products table with clickable Name and Image columns | 1. Click the target product's Name column<br>2. Immediately click the target product's Image column before navigation completes | Navigation to the Product Detail page succeeds once; the Product Detail page opens and is displayed. No duplicate navigations or multiple detail pages are produced and the product detail UI is visible. | medium |
| TC-015 (input_edge) |  | Very long product name rendering and navigation to detail | User is logged in and on the Product Inventory page, A product exists whose Name is far longer than the typical display width (very long name) | 1. Observe the product Name cell in the products table<br>2. Click the long Name in the products table<br>3. Observe the product Name displayed on the Product Detail page | In the products table the Name cell is truncated with a visible ellipsis (table row shows truncated text). Clicking the Name succeeds and opens the Product Detail page; the Product Detail page displays the full product name (no truncation) or otherwise shows the full name in a visible field. | low |

---

## Product Detail

Total: **11** (positive: 4, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User logged in as <role>, Product exists and is in Not In Cart state | 1. Navigate to the Product Detail page for <target product><br>2. Verify the action button shows 'Add to cart' on the Product Detail page<br>3. Click the 'Add to cart' button | adds product to cart — Action button label changes to 'Remove' on the Product Detail page indicating the product is in cart | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User logged in as <role>, Product exists and is in In Cart state | 1. Navigate to the Product Detail page for <target product><br>2. Verify the action button shows 'Remove' on the Product Detail page<br>3. Click the 'Remove' button | removes product from cart — Action button label changes to 'Add to cart' on the Product Detail page indicating the product is not in cart | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via Back to products link | User logged in as <role> | 1. Navigate to the Product Detail page for <target product><br>2. Click the 'Back to products' link | navigates to Product Inventory page | high |
| TC-004 | WF-004 | Open Shopping Cart via cart icon from Product Detail | User logged in as <role> | 1. Navigate to the Product Detail page for <target product><br>2. Click the Cart icon | navigates to Shopping Cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to add product when product is already in cart (Add button should not be available) | User is on Product Detail page context, Product is already in the Shopping Cart (entity_state == In Cart) | 1. Navigate to the Product Detail page for the product that is already in the cart<br>2. Attempt to click the 'Add to cart' button | The 'Add to cart' button is not visible on the Product Detail page (no clickable control labeled 'Add to cart'); the 'Remove' button is visible instead. The Shopping Cart contents and item count remain unchanged (no duplicate item is added). | high |
| TC-006 | WF-002 | Attempt to remove product when product is not in cart (Remove button should not be available) | User is on Product Detail page context, Product is not present in the Shopping Cart (entity_state == Not In Cart) | 1. Navigate to the Product Detail page for the product that is not in the cart<br>2. Attempt to click the 'Remove' button | The 'Remove' button is not visible on the Product Detail page (no clickable control labeled 'Remove'); the 'Add to cart' button is visible instead. The Shopping Cart contents and item count remain unchanged (nothing is removed). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (state_edge) | WF-001 | Rapid double-click Add to cart should not create duplicate cart entries | Product Detail page is open for a product, The product's current entity_state is Not In Cart | 1. Click the "Add to cart" button<br>2. Immediately (before UI finishes updating) click the "Add to cart" button again<br>3. Click the "Cart icon" link to navigate to the Shopping Cart page<br>4. Observe the Shopping Cart page and return to Product Detail | First Add to cart action succeeds; the immediate second click is ignored/blocked so no duplicate entry is created. Shopping Cart displays only one entry for that product. Product Detail action bar shows the In Cart state (button now reads "Remove"). | medium |
| TC-008 (state_edge) |  | Rapid Add then immediate Remove (consecutive state transitions) yields a stable final state | Product Detail page is open for a product, The product's current entity_state is Not In Cart | 1. Click the "Add to cart" button<br>2. Immediately click the "Remove" button (before or as the Add finishes)<br>3. Observe the Product Detail action bar state<br>4. Click the "Cart icon" link to open the Shopping Cart page and verify contents | The rapid Add then Remove sequence succeeds as discrete state transitions; final visible state on Product Detail is Not In Cart (button reads "Add to cart"). Shopping Cart does not contain the product after the sequence (the Remove succeeded and no duplicate entries were created). | medium |
| TC-009 (interaction_edge) | WF-003 | Start Add to cart then immediately navigate Back to products | Product Detail page is open for a product, The product's current entity_state is Not In Cart | 1. Click the "Add to cart" button<br>2. Immediately click the "Back to products" link<br>3. On the Product Inventory page, locate the same product and observe its cart indicator/button<br>4. Optionally click the product to re-open Product Detail and observe the action bar state | The Add to cart action succeeds before navigation cancels it; on Product Inventory the product shows the In Cart indicator (or the action bar on re-opened Product Detail shows "Remove"). Navigation did not create duplicate cart entries. (Action succeeds.) | low |
| TC-010 (interaction_edge) |  | Navigate to Shopping Cart after add, then press browser Back — ensure no duplicate add on back | Product Detail page is open for a product, The product's current entity_state is Not In Cart | 1. Click the "Add to cart" button<br>2. Click the "Cart icon" link to navigate to the Shopping Cart page<br>3. Use the browser Back button to return to the Product Detail page<br>4. Click the "Cart icon" link again to re-open the Shopping Cart page and observe contents | Adding the product succeeds and pressing Back does not cause an additional add. Product Detail shows In Cart state after going back. Shopping Cart still shows only one entry for that product (no duplicate entries were created by navigation). | low |
| TC-011 (state_edge) | WF-002 | Rapid double-click Remove when product is In Cart should not cause errors or multiple removals | Product Detail page is open for a product, The product's current entity_state is In Cart | 1. Click the "Remove" button<br>2. Immediately click the "Remove" button again<br>3. Click the "Cart icon" link to navigate to the Shopping Cart page<br>4. Return to Product Detail and observe the action bar state | First Remove action succeeds; the immediate second click is ignored/blocked so no inconsistent state occurs. Shopping Cart does not contain the product after the remove. Product Detail action bar shows Not In Cart state (button reads "Add to cart"). | medium |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart via row Remove action | User logged in as <role>, Shopping Cart contains at least one item with quantity shown as 1 and a description | 1. Navigate to the Shopping Cart page<br>2. Locate the row for <cart item> in the Cart Items table<br>3. Click the Remove button on the row for <cart item><br>4. Confirm removal if a confirmation dialog appears by clicking Confirm | The row for <cart item> is no longer present in the Cart Items table | high |
| TC-002 | WF-002 | Use Continue Shopping link to return to Product Inventory | User logged in as <role>, Shopping Cart page is accessible | 1. Navigate to the Shopping Cart page<br>2. Click the Continue Shopping link in the page action bar | The Product Inventory page is displayed (navigation to Product Inventory occurs) | medium |
| TC-003 | WF-003 | Begin checkout from the Shopping Cart using the Checkout button | User logged in as <role>, Shopping Cart contains at least one item | 1. Navigate to the Shopping Cart page<br>2. Click the Checkout button in the page action bar | The Checkout page is displayed and the checkout process begins | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot view Shopping Cart page | User is not authenticated (not logged in) | 1. As an <unauthenticated user>, navigate to the Shopping Cart page (e.g., /cart) | Access is blocked: user is redirected to the Login page; the Shopping Cart page is not displayed and the Login form is shown (user cannot view cart contents) | high |
| TC-005 | WF-003 | Unauthenticated user cannot begin checkout (Checkout redirects to login) | User is not authenticated (not logged in) | 1. As an <unauthenticated user>, navigate to the Shopping Cart page<br>2. Click the Checkout button | Checkout is blocked: user is redirected to the Login page; the checkout process does not begin and the Shopping Cart remains unchanged; the Login form is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid consecutive clicks on Remove (double-click) for a single item | A user is on the Shopping Cart page with at least one item in the Cart_Items_Table | 1. On the Shopping Cart page, locate the row for the item to remove<br>2. Click the row's Remove button<br>3. Immediately click the same Remove button again (within 1 second) | First Remove click succeeds: the item's row is removed and the Cart_Items_Table no longer contains that item. The immediate second click is blocked (no additional removal occurs and no duplicate removal error is shown). | medium |
| TC-007 (interaction_edge) | WF-001 | Remove when cart contains exactly one item | A user is on the Shopping Cart page and the Cart_Items_Table contains exactly one row (one item) | 1. On the Shopping Cart page, click the only row's Remove button | Remove succeeds: the Cart_Items_Table displays zero rows (no items remain). The page shows an empty cart state (no item rows are visible). | medium |
| TC-008 (input_edge) |  | Very long product description displayed in cart (>200 characters) | An item with a very long description (longer than 200 characters) has been added to the cart | 1. Navigate to the Shopping Cart page | Adding the item to cart succeeds; on the Shopping Cart page the description cell either displays the full long description or displays a visible truncated form (ellipsis) with a clear affordance to view the full text (e.g., tooltip/expand). In either case the long-text presence is visible and no error is shown. | low |
| TC-009 (input_edge) |  | Product description containing special characters and emoji | An item whose description contains special characters and emoji has been added to the cart | 1. Navigate to the Shopping Cart page<br>2. Observe the description cell for that item<br>3. Click the Checkout button in the Cart_Page_Actions | Displaying the item in the cart succeeds: the special characters and emoji render visibly in the description cell (not shown as replacement characters). Clicking Checkout succeeds and begins the checkout process (navigation to checkout) without losing or corrupting the special-character/emoji description. | low |

---

## Checkout - Information

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with valid information navigates to Overview step | User logged in as <role>, Checkout - Information page is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click the Continue button | Overview_Step panel is displayed | high |
| TC-002 | WF-002 | Click Cancel returns user to Shopping Cart | User logged in as <role>, Checkout - Information page is open | 1. Click the Cancel button | Shopping_Cart page is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Continue blocked when First Name is left blank (other required fields filled) | User is on the Checkout - Information page | 1. Leave the First Name field blank<br>2. Enter <valid Last Name> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form does not submit and the page remains on Checkout - Information; an error banner is shown stating exactly 'Error: First Name is required'; no navigation to Overview_Step occurs | high |
| TC-004 | WF-001 | Continue blocked when all required fields are empty | User is on the Checkout - Information page | 1. Leave the First Name field blank<br>2. Leave the Last Name field blank<br>3. Leave the Postal Code field blank<br>4. Click the Continue button | Form does not submit and the page remains on Checkout - Information; error banners are shown stating exactly 'Error: First Name is required', 'Error: Last Name is required', and 'Error: Postal Code is required'; no navigation to Overview_Step occurs | high |
| TC-005 | WF-001 | Continue blocked when Postal Code is left blank (other required fields filled) | User is on the Checkout - Information page | 1. Enter <valid First Name> in the First Name field<br>2. Enter <valid Last Name> in the Last Name field<br>3. Leave the Postal Code field blank<br>4. Click the Continue button | Form does not submit and the page remains on Checkout - Information; an error banner is shown stating exactly 'Error: Postal Code is required'; no navigation to Overview_Step occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Whitespace-only in required First Name is treated as empty | User is on the Checkout - Information form | 1. Enter whitespace-only characters into First_Name<br>2. Enter non-empty text into Last_Name<br>3. Enter non-empty text into Postal_Code<br>4. Click Continue | Continue is blocked; the error banner displays "Error: First Name is required" | medium |
| TC-007 (input_edge) | WF-001 | Very long Postal Code input (200+ chars) is submitted | User is on the Checkout - Information form | 1. Enter <very long string (200+ characters)> into Postal_Code<br>2. Enter non-empty text into First_Name<br>3. Enter non-empty text into Last_Name<br>4. Click Continue | Continue succeeds; the UI navigates to the Overview Step and no required-field error banners are shown | medium |
| TC-008 (interaction_edge) | WF-001 | Rapid double-click on Continue after filling form | User is on the Checkout - Information form | 1. Enter non-empty text into First_Name<br>2. Enter non-empty text into Last_Name<br>3. Enter non-empty text into Postal_Code<br>4. Click Continue twice rapidly (double-click) | Continue succeeds once; the first click navigates to the Overview Step and the second click is ignored (no duplicate navigation or additional error banner shown) | low |
| TC-009 (interaction_edge) | WF-002 | Click Cancel with required fields empty bypasses validation | User is on the Checkout - Information form | 1. Leave First_Name empty<br>2. Leave Last_Name empty<br>3. Leave Postal_Code empty<br>4. Click Cancel | Navigation to Shopping_Cart succeeds; no required-field error banners are shown | low |

---

## Checkout - Overview

Total: **7** (positive: 2, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout from Overview step | User logged in as <Customer>, Checkout - Overview is open with at least one cart item and payment and shipping information present | 1. On the Checkout - Overview step confirm the order summary (cart items) and totals section (Item total, Tax, Total) are displayed<br>2. Click the Finish button | completes the order and navigates to the confirmation page | high |
| TC-002 | WF-002 | Cancel checkout from Overview step | User logged in as <Customer>, Checkout - Overview is open with at least one cart item | 1. On the Checkout - Overview step confirm the Cancel button is visible<br>2. Click the Cancel button | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user cannot access Checkout Overview | User is not authenticated (no valid session) | 1. Open the <Checkout Overview URL> in the browser | User is redirected to the <login page>; Checkout Overview content is not displayed; Finish and Cancel controls are not visible or accessible (checkout cannot be completed without signing in). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Finish on Overview | User is signed in (if required) and on the Checkout - Overview step, Cart is populated and payment & shipping information are displayed | 1. Ensure the Overview page is visible with the Finish button in view<br>2. Click the Finish button<br>3. Immediately click the Finish button again (within a fraction of a second) | Second click is ignored / blocked; user is navigated to the confirmation page only once and no second navigation or duplicated confirmation UI appears. The UI shows the confirmation page on success. | medium |
| TC-005 (interaction_edge) | WF-001 | Press browser Back after successful Finish then attempt to Finish again | User is on Checkout - Overview and Finish has not yet been clicked, Cart and payment/shipping info are present | 1. Click the Finish button<br>2. Wait until the confirmation page loads<br>3. Use the browser Back button to return to the Checkout - Overview page<br>4. Attempt to click the Finish button again | Second submission attempt is blocked; clicking Finish after returning via browser Back does not create a second successful completion. The UI either prevents the action (button disabled) or shows a visible inline message indicating the order cannot be re-submitted; user is not navigated to a second confirmation page. | medium |
| TC-006 (interaction_edge) |  | Click Cancel immediately after clicking Finish (race between Finish and Cancel) | User is on Checkout - Overview with cart, payment, and shipping info displayed | 1. Click the Finish button<br>2. Immediately click the Cancel button before navigation completes | Race resolved deterministically by the UI: either Finish completes and user is navigated to confirmation (Cancel click is ignored) or Cancel takes precedence and user exits checkout. The UI must show one clear outcome — either the confirmation page (Finish succeeds) or the post-cancel exit state — and must not leave the user in an intermediate/inconsistent state. | medium |
| TC-007 (input_edge) |  | Very long shipping/payment text shown on Overview (display/overflow handling) | User has a cart and the shipping address and payment name fields contain very long values (200+ characters), User has navigated to Checkout - Overview | 1. View the shipping information section on the Overview step<br>2. View the payment information section on the Overview step | Overview display handles long text safely: long shipping/payment fields are either visibly truncated with an affordance to view the full value (e.g., ellipsis + 'Show more') or cause the content area to allow scrolling without breaking layout. There is a visible indicator if truncation occurs; the UI remains usable. | low |

---

## Checkout - Confirmation

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Back Home from Confirmation clears cart and returns to Product Inventory | User logged in as <role>, Confirmation page is open showing an order success message | 1. Click the 'Back Home' button on the Confirmation page | Product Inventory page is displayed and the shopping cart is cleared: no items are listed in the cart and the cart badge shows 0 items | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Back Home button non-functional (no navigation and cart not cleared) | User has completed checkout and is on the Confirmation page, There are <items in the cart> immediately prior to confirmation (cart contains items) | 1. On the Confirmation page, verify the success message is visible<br>2. Click the 'Back Home' button | No navigation occurs; the user remains on the Confirmation page showing the success message; the cart is NOT cleared (cart still contains <items in the cart> as indicated by the cart badge or cart view); the 'Back Home' button remains visible. The on_success behaviour 'navigates to Product Inventory and clears the cart' did not occur. | high |
| TC-003 | WF-001 | Navigation succeeds but cart is not cleared (partial failure) | User has completed checkout and is on the Confirmation page, There are <items in the cart> immediately prior to confirmation (cart contains items) | 1. On the Confirmation page, verify the success message is visible<br>2. Click the 'Back Home' button | The app navigates to the Product Inventory page but the cart was NOT cleared: the cart icon/badge on Product Inventory still displays <items in the cart> (or the cart view still lists the items). The on_success requirement to both navigate to Product Inventory AND clear the cart is only partially fulfilled; clearing the cart failed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Back Home while navigation is in progress | User is on the Confirmation Page displaying the success message | 1. Click the Back Home button once<br>2. Immediately click the Back Home button a second time before the first navigation completes | First click succeeds: UI navigates to Product Inventory and the cart is cleared. The immediate second click is ignored (no additional navigation or error). Product Inventory is displayed once and the cart remains cleared; no duplicate side-effects occur. | medium |
| TC-005 (state_edge) | WF-001 | Click Back Home when the cart is already empty | User is on the Confirmation Page, The user's cart is already empty prior to clicking Back Home | 1. Click the Back Home button | Navigation to Product Inventory succeeds; the cart remains empty and no error message is shown. Product Inventory displays with an empty cart. | low |
| TC-006 (interaction_edge) | WF-001 | Press browser Back immediately after clicking Back Home (rapid re-navigation) | User is on the Confirmation Page | 1. Click the Back Home button<br>2. Immediately press the browser Back button | Clicking Back Home succeeds: UI navigates to Product Inventory and the cart is cleared. Immediately pressing Back does not re-trigger the cart-clear side-effect. If the Confirmation Page is restored from history, it is shown as a cached page and no additional server-side clear runs; cart remains cleared and no error is shown. | medium |
| TC-007 (interaction_edge) | WF-001 | Open Back Home in a new tab (middle-click / open in new tab) | User is on the Confirmation Page | 1. Open the Back Home action in a new browser tab (middle-click or context menu -> open in new tab)<br>2. Switch to the newly opened tab | Opening Back Home in a new tab succeeds: the new tab displays Product Inventory and the user's cart is cleared in-session. The original tab either remains on Confirmation Page or reflects the cleared cart; no inconsistent session state or error is shown and no duplicate side-effects occur. | low |

---

## Logout

Total: **8** (positive: 1, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Logout button redirects to Login page | User logged in as <role>, Logout button is visible in the application header | 1. Click the Logout button in the header | ends session and redirects to Login page. The Login page is displayed with the login form visible. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to invoke Logout while not authenticated (precondition not met) | User is not logged in | 1. Open the application in a new browser session where no user is logged in<br>2. In the browser address bar, navigate to the application's Logout URL (or click any visible Logout link/button if present) | Navigation is blocked/redirected: the Login page is displayed (login form visible). The Logout action is not performed because the precondition 'user must be logged in' is not met; no protected page is shown. | high |
| TC-003 | WF-001 | Click Logout a second time after already logging out (idempotent/precondition timing) | User is logged in as <role> | 1. Log in as <role><br>2. Click the Logout button<br>3. After the app redirects to the Login page, attempt to click Logout again (or navigate to the Logout URL) without logging in | Second Logout attempt is blocked/treated as no-op: the Login page remains displayed (login form visible). No error or protected page is presented; the system does not transition to an authenticated state and no unexpected behavior occurs. This verifies the precondition 'user must be logged in' prevents a logout action when already logged out. | high |
| TC-004 |  | Access protected page (inventory) after Logout is performed | User is logged in as <role> | 1. Log in as <role><br>2. Click the Logout button<br>3. From the Login page, attempt to navigate to the Inventory page (e.g., enter /inventory or click an Inventory link) | Access is blocked: the user is redirected to the Login page (login form visible); the Inventory page is not displayed. This confirms the consequence 'protected pages are not accessible without logging in again' after logout. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-001 | Rapid double-click of Logout button | User is logged in and on a protected page | 1. Ensure the protected page is visible (user is authenticated)<br>2. Click the Logout button once<br>3. Immediately click the Logout button again (double-click / second click before redirect completes) | First click succeeds: session ends and the user is redirected to the Login page. The immediate second click is ignored or treated as a no-op; no duplicate logout errors are shown and no additional sessions are created (no visible error). | medium |
| TC-006 (interaction_edge) | WF-001 | Use browser Back button after successful logout | User is logged in and on a protected page | 1. Click the Logout button<br>2. Observe redirection to the Login page<br>3. Press the browser Back button once | Navigation back is blocked / error shown: the protected page is not displayed. The user remains on the Login page or is immediately redirected back to the Login page; protected content is not accessible without re-authentication. | medium |
| TC-007 (state_edge) | WF-001 | Logout while the browser is offline (network interruption) | User is logged in and on a protected page, Ability to toggle the browser/network offline mode | 1. Toggle the browser to offline mode (simulate network loss)<br>2. Click the Logout button<br>3. Toggle the browser back to online mode | Logout attempt is blocked / error shown while offline: a visible network error/toast is displayed and the user remains authenticated in the current tab. After returning online, the user may need to click Logout again; no silent session termination should be assumed while offline. | medium |
| TC-008 (interaction_edge) | WF-001 | Logout in one tab then immediately logout in another tab without refreshing | User is logged in in two browser tabs (Tab A and Tab B) viewing protected pages | 1. In Tab A, click the Logout button<br>2. Without refreshing Tab B, switch to Tab B and click the Logout button | First click (Tab A) succeeds: session ends and Tab A is redirected to the Login page. The subsequent logout click in Tab B is blocked / error shown or treated as a no-op: Tab B should either be redirected to the Login page or show that the session is no longer authenticated, with no server error displayed. | medium |

---

## Reset App State

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State clears a populated cart and restores add/remove button states while keeping user logged in | User logged in as <Role>, User is on the <App page> where the Reset App State button is visible, Cart contains one or more items; cart badge shows a positive count; at least one product action button shows the 'Remove' state | 1. Click the 'Reset App State' button | clears cart and resets in-app state (cart badge and add/remove button states) without logging the user out — Cart badge is no longer visible (or shows '0') and the cart contents area shows no items; product action buttons now display the 'Add' state instead of 'Remove'; the user's profile/avatar or account menu remains visible indicating the user is still logged in | high |
| TC-002 |  | Reset App State is idempotent when the cart is already empty and does not log the user out | User logged in as <Role>, User is on the <App page> where the Reset App State button is visible, Cart is already empty; cart badge is not visible; product action buttons are in the 'Add' state | 1. Click the 'Reset App State' button | clears cart and resets in-app state (cart badge and add/remove button states) without logging the user out — Cart remains empty with no cart badge visible; product action buttons remain in the 'Add' state; the user's profile/avatar or account menu remains visible indicating the user is still logged in | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user attempts to press Reset App State | User is not authenticated (logged out) | 1. Navigate to the page that contains the Reset App State button<br>2. Attempt to click the Reset App State button | User is redirected to the Login page and the Reset App State action is not executed; the cart is not cleared and the cart badge and add/remove button states remain unchanged (no visible UI change from Reset App State). | high |
| TC-004 | WF-001 | User without required role attempts to access Reset App State | Logged in as <user without the role required to perform Reset App State> | 1. Navigate to the page that normally contains the Reset App State button<br>2. Look for the Reset App State button (attempt to click it if visible) | Reset App State button is not visible (or is disabled); the user cannot invoke the action. The cart is not cleared and the cart badge and add/remove button states remain unchanged; the user remains logged in. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-001 | Reset with populated cart and toggled add/remove button states | User is logged in, Cart contains one or more items, At least one product's add/remove button is showing the 'remove' state, Cart badge is showing a non-zero count | 1. Click the 'Reset App State' button | Click succeeds; cart is cleared (cart listing shows no items and cart badge is zero or hidden), all add/remove buttons revert to their initial 'add' state, and the user remains logged in (user avatar/menu remains visible). No logout occurs and no error is shown. | medium |
| TC-006 (interaction_edge) | WF-001 | Reset when cart is already empty (idempotency) | User is logged in, Cart is empty and cart badge is not showing a count | 1. Click the 'Reset App State' button | Click succeeds; UI remains unchanged for cart (still empty, no items listed), no error or warning is shown, in-app state remains default, and the user remains logged in. The action is idempotent and does not produce a new error or log the user out. | low |
| TC-007 (interaction_edge) | WF-001 | Rapid double-click of Reset App State | User is logged in, Cart contains one or more items, Reset App State button is visible and enabled | 1. Click the 'Reset App State' button<br>2. Immediately click the 'Reset App State' button again (within a short interval) | First click succeeds and clears the cart; second click is ignored or has no additional effect (no duplicate side effects). The cart remains empty, UI is stable (no error messages), and the user remains logged in. No duplicate state transitions or visible errors occur. | low |
| TC-008 (state_edge) | WF-001 | Reset while an in-progress checkout is open | User is logged in, User has initiated checkout / is on the checkout page with items in cart, Pay/continue buttons are visible as part of the checkout UI | 1. Click the 'Reset App State' button | Click succeeds; cart is cleared (checkout UI updates to reflect an empty cart — e.g., no items listed or a clear empty-cart state is shown), checkout actions that require cart items become disabled or indicate empty cart, and the user remains logged in. No logout occurs and no unexpected error is shown. | medium |

---
