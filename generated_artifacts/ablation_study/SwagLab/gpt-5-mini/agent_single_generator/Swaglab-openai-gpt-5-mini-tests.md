# Test Cases — Swaglab

Generated: 2026-06-09T09:19:08.597373Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 125 | 42 | 40 | 43 | 66 | 50 | 9 |

## Login

Total: **13** (positive: 2, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with standard_user | User on Login page, User not authenticated | 1. Enter Username: standard_user<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Authenticates user and redirects to Product Inventory page | high |
| TC-002 | WF-001 | Successful login with performance_glitch_user | User on Login page, User not authenticated | 1. Enter Username: performance_glitch_user<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Authenticates user and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Attempt login with missing Username | User on Login page, User not authenticated | 1. Leave Username empty<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Username is required. | high |
| TC-004 | WF-003 | Attempt login with missing Password | User on Login page, User not authenticated | 1. Enter Username: standard_user<br>2. Leave Password empty<br>3. Click the Login button | Epic sadface: Password is required. | high |
| TC-005 | WF-004 | Attempt login with both Username and Password missing | User on Login page, User not authenticated | 1. Leave Username empty<br>2. Leave Password empty<br>3. Click the Login button | Epic sadface: Username is required.; Epic sadface: Password is required. | high |
| TC-006 | WF-005 | Attempt login with invalid credentials (unknown username) | User on Login page, User not authenticated | 1. Enter Username: unknown_user<br>2. Enter Password: wrong_password<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | high |
| TC-007 | WF-006 | Login attempt with locked_out_user and correct password | User on Login page, User not authenticated | 1. Enter Username: locked_out_user<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | high |
| TC-008 | WF-007 | Login attempt with locked_out_user and missing Password | User on Login page, User not authenticated | 1. Enter Username: locked_out_user<br>2. Leave Password empty<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out.; Epic sadface: Password is required. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | N/A | Username with leading and trailing spaces | User on Login page, User not authenticated | 1. Enter Username: ' standard_user ' (leading and trailing spaces included)<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-010 | N/A | Username case sensitivity check | User on Login page, User not authenticated | 1. Enter Username: Standard_User (different case)<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-011 | N/A | Password case sensitivity check | User on Login page, User not authenticated | 1. Enter Username: standard_user<br>2. Enter Password: Secret_Sauce (different case)<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-012 | N/A | Extremely long username input (boundary) | User on Login page, User not authenticated | 1. Enter Username: 256-character string (e.g., 'a' repeated 256 times)<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-013 | N/A | SQL injection attempt in Username field | User on Login page, User not authenticated | 1. Enter Username: "' OR '1'='1"<br>2. Enter Password: secret_sauce<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. Application does not crash or reveal stack traces. | medium |

---

## Product Inventory

Total: **19** (positive: 8, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Sort products by Name: A–Z (ascending) | User logged in as standard user, Products_Table populated with multiple products having distinct names | 1. Navigate to Product Inventory page<br>2. Open Sort_Dropdown<br>3. Select option 'Name: A–Z' | Products_Table is sorted ascending by Name (A to Z); first row shows lexicographically smallest product name visible on screen | high |
| TC-002 | WF-002 | Sort products by Name: Z–A (descending) | User logged in as standard user, Products_Table populated with multiple products having distinct names | 1. Navigate to Product Inventory page<br>2. Open Sort_Dropdown<br>3. Select option 'Name: Z–A' | Products_Table is sorted descending by Name (Z to A); first row shows lexicographically largest product name visible on screen | high |
| TC-003 | WF-003 | Sort products by Price: Low–High | User logged in as standard user, Products_Table populated with multiple products having distinct prices | 1. Navigate to Product Inventory page<br>2. Open Sort_Dropdown<br>3. Select option 'Price: Low–High' | Products_Table is sorted by Price ascending (lowest price at top); first row shows product with lowest price visible on screen | high |
| TC-004 | WF-004 | Sort products by Price: High–Low | User logged in as standard user, Products_Table populated with multiple products having distinct prices | 1. Navigate to Product Inventory page<br>2. Open Sort_Dropdown<br>3. Select option 'Price: High–Low' | Products_Table is sorted by Price descending (highest price at top); first row shows product with highest price visible on screen | high |
| TC-007 | WF-005 | Open Product Detail by clicking product Name | User logged in as standard user, Products_Table populated with at least one product | 1. Navigate to Product Inventory page<br>2. Click the product Name link in a row | Navigates to Product Detail page for that product; Product Detail page visible with product-specific information | high |
| TC-008 | WF-005 | Open Product Detail by clicking product Image | User logged in as standard user, Products_Table populated with products that include an Image | 1. Navigate to Product Inventory page<br>2. Click the product Image in a row | Navigates to Product Detail page for that product; Product Detail page visible with product-specific information | high |
| TC-010 | WF-006 | Add single item to cart from Products_Table | User logged in as standard user, Products_Table contains a product with Add to cart button (in_cart == false), Cart_Badge shows N (N may be 0) | 1. Navigate to Product Inventory page<br>2. Click 'Add to cart' button for the chosen product | 'Add to cart' button changes to 'Remove' for that product; in_cart state becomes true; Cart_Badge increments to N+1 and displays updated count | high |
| TC-011 | WF-007 | Remove single item from cart from Products_Table | User logged in as standard user, Products_Table contains a product already in cart with Remove button (in_cart == true), Cart_Badge shows M (M >= 1) | 1. Navigate to Product Inventory page<br>2. Click 'Remove' button for the chosen product | 'Remove' button changes to 'Add to cart' for that product; in_cart state becomes false; Cart_Badge decrements to M-1 and displays updated count | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-005 | Clicking non-interactive area does not navigate to Product Detail | User logged in as standard user, Products_Table populated | 1. Navigate to Product Inventory page<br>2. Click within the row but not on Name or Image (e.g., click Description or empty area) | No navigation occurs; user remains on Product Inventory page and no Product Detail page is opened | medium |
| TC-012 | WF-006 | Attempt to 'Add to cart' when item already in cart (duplicate add) | User logged in as standard user, Products_Table contains a product already in cart (button shows 'Remove') | 1. Navigate to Product Inventory page<br>2. Click the 'Add to cart' button area for a product that currently shows 'Remove' (attempt duplicate action) | No 'Add to cart' action available because button displays 'Remove'; clicking 'Remove' removes item (separate flow). System prevents adding duplicate entries; Cart_Badge count remains unchanged from current value unless Remove is explicitly clicked | high |
| TC-013 | WF-007 | Attempt to 'Remove' when item not in cart | User logged in as standard user, Products_Table contains a product not in cart (button shows 'Add to cart') | 1. Navigate to Product Inventory page<br>2. Click the 'Remove' button area for a product that currently shows 'Add to cart' (attempt invalid remove) | No 'Remove' action present because button displays 'Add to cart'; clicking the 'Add to cart' button will add the item instead. System does not decrement Cart_Badge or remove item since it is not in cart | high |
| TC-019 | WF-006 | Add to cart when not logged in is blocked (authorization precondition) | User is logged out, Products_Table accessible (e.g., public view) or user attempts to access Inventory page | 1. Navigate to Product Inventory page while logged out<br>2. Attempt to click 'Add to cart' for any product | Action is blocked: user is prompted to log in or an authentication modal appears; no change to Cart_Badge occurs and button state remains unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Sort selection persists while navigating away and back to page | User logged in as standard user, Products_Table populated | 1. Navigate to Product Inventory page<br>2. Select 'Name: A–Z' in Sort_Dropdown<br>3. Click a product to go to Product Detail page<br>4. Use browser Back or Inventory nav to return to Product Inventory page | Sort_Dropdown still shows 'Name: A–Z' and Products_Table remains sorted A–Z (or sorting persisted per app spec), visible rows remain in sorted order | medium |
| TC-006 | WF-001 | Sort stability with identical names (tie-breaker by Price or stable order) | User logged in as standard user, Products_Table contains multiple products with identical Name values and varying prices | 1. Navigate to Product Inventory page<br>2. Select 'Name: A–Z' in Sort_Dropdown | Products with identical Name appear grouped together; within group ordering is stable (e.g., deterministic by Price or original insertion order) and consistent across repeated sorts | medium |
| TC-014 | WF-006 | Add multiple distinct items updates Cart_Badge correctly | User logged in as standard user, Products_Table populated with at least 5 items all not in cart, Cart_Badge shows 0 | 1. Navigate to Product Inventory page<br>2. Click 'Add to cart' for 5 different products sequentially | Each clicked product's button changes to 'Remove' and in_cart becomes true; Cart_Badge increments by 1 for each add and finally displays 5 | medium |
| TC-015 | WF-006 | Rapid toggle Add/Remove does not create duplicate entries and keeps Cart_Badge consistent | User logged in as standard user, Products_Table contains at least one product not in cart, Cart_Badge shows initial count P | 1. Navigate to Product Inventory page<br>2. Rapidly click 'Add to cart' then 'Remove' then 'Add to cart' on the same product within 2 seconds (repeat 3 cycles)<br>3. Observe Cart_Badge and product button state after each click | No duplicate entries created; button toggles between 'Add to cart' and 'Remove' appropriately; Cart_Badge increments/decrements by 1 per action and final Cart_Badge equals P+1 if final state is in_cart true or P if final state false; no negative or >expected counts occur | medium |
| TC-016 | WF-003 | Sort with zero, very large and negative prices present (price value edge cases) | User logged in as standard user, Products_Table contains products with prices: 0.00, 0.01, very large (e.g., 9999999.99), and (if system allows) negative price -5.00 | 1. Navigate to Product Inventory page<br>2. Select 'Price: Low–High'<br>3. Observe ordering; then select 'Price: High–Low' and observe ordering | Low–High places negative prices first (if allowed) then 0.00 then ascending to large values; High–Low reverses order; UI displays prices correctly and sorts numerically rather than lexicographically | medium |
| TC-017 | WF-001 | Sorting names with mixed case is case-insensitive or follows defined behavior | User logged in as standard user, Products_Table contains names: 'apple', 'Banana', 'Apricot', 'banana' | 1. Navigate to Product Inventory page<br>2. Select 'Name: A–Z'<br>3. Observe the order of mixed-case names | Products_Table sorts names in a consistent, defined manner (case-insensitive expected): 'apple', 'Apricot', 'Banana', 'banana' or otherwise documented stable order; no unexpected interleaving occurs | medium |
| TC-018 | WF-005 | Clicking Name navigates to Product Detail for long product names (UI truncation / ellipsis) | User logged in as standard user, Products_Table contains a product with a very long Name (exceeds visible width and is truncated with ellipsis) | 1. Navigate to Product Inventory page<br>2. Click the visible truncated product Name (clickable area) | Navigation occurs to Product Detail page for that product despite truncation; Product Detail page shows full product name | medium |

---

## Product Detail

Total: **14** (positive: 4, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User on Product Detail page for Product A, Product A state == Not in Cart | 1. Verify the action bar displays a button labeled 'Add to cart'.<br>2. Click the 'Add to cart' button. | Action bar updates to display a 'Remove' button (product state transitions to In Cart) and the Product Detail page remains visible | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User on Product Detail page for Product B, Product B state == In Cart | 1. Verify the action bar displays a button labeled 'Remove'.<br>2. Click the 'Remove' button. | Action bar updates to display an 'Add to cart' button (product state transitions to Not in Cart) and the Product Detail page remains visible | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via 'Back to products' link | User on Product Detail page for any product | 1. Click the 'Back to products' link/button in the Product Detail page. | Application navigates to the Product Inventory page and Product Detail is no longer visible | high |
| TC-004 | WF-004 | Open Shopping Cart via Cart Icon | User on Product Detail page for any product | 1. Click the Cart Icon link on Product Detail page. | Application navigates to the Shopping Cart page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to 'Add to cart' when product is already in cart (button should not attempt duplicate add) | User on Product Detail page for Product C, Product C state == In Cart | 1. Verify the action bar displays a 'Remove' button (not 'Add to cart').<br>2. Attempt to click an 'Add to cart' button (if present due to UI bug) or attempt to trigger add via keyboard shortcut. | No 'Add to cart' action is performed; action bar remains showing 'Remove' and no duplicate add occurs | high |
| TC-006 | WF-002 | Attempt to 'Remove' when product is not in cart | User on Product Detail page for Product D, Product D state == Not in Cart | 1. Verify the action bar displays 'Add to cart' (not 'Remove').<br>2. Attempt to click a 'Remove' button (if present due to UI bug). | No 'Remove' action is performed; action bar remains showing 'Add to cart' and no error or negative change occurs | medium |
| TC-007 | WF-001 | Add to cart fails due to network error and shows inline error | User on Product Detail page for Product E, Product E state == Not in Cart, Simulate network failure / API returns error on add request | 1. Click the 'Add to cart' button.<br>2. Wait for the add action response (simulate network error). | An inline error message is displayed (e.g. 'Could not add to cart. Try again.') and the action bar remains showing 'Add to cart' | high |
| TC-008 | WF-003 | Back to products link is broken or missing (UI error) | User on Product Detail page for any product, Back to products link is missing or its href is invalid | 1. Click the 'Back to products' link/button. | Either no navigation occurs and an inline error or no-op is observed, or user remains on Product Detail page; missing link is visible in UI audit | high |
| TC-009 | WF-004 | Cart icon link is broken or not clickable | User on Product Detail page for any product, Cart Icon is present but not clickable due to UI/JS error | 1. Click the Cart Icon. | No navigation to Shopping Cart occurs and an inline error or no-op is observed; Cart Icon must be reported as non-functional | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-001 | Rapid repeated clicks on 'Add to cart' result in single add (debounce/guard) | User on Product Detail page for Product F, Product F state == Not in Cart | 1. Rapidly click the 'Add to cart' button multiple times (5-10 clicks) within 1-2 seconds.<br>2. Observe the action bar and any UI feedback. | Only one state transition occurs and the action bar settles to display 'Remove'; no duplicate UI transitions or duplicate items are created in a single product slot | high |
| TC-011 | WF-001 | Product with extremely long name and description displays without breaking layout | User on Product Detail page for Product G, Product G has name length >= 500 characters and description length >= 2000 characters | 1. Open Product Detail page for Product G.<br>2. Inspect how product name and description render on various viewport widths. | Name and description either wrap or are ellipsized according to design; price and action bar remain visible and usable; page layout does not break | medium |
| TC-012 | WF-001 | Product missing image shows placeholder | User on Product Detail page for Product H, Product H has no image available (image URL 404 or null) | 1. Open Product Detail page for Product H.<br>2. Observe the product image area. | A placeholder image or clear empty-state graphic is displayed in place of the product image and the rest of the details and action bar remain visible | medium |
| TC-013 | WF-001 | Product price edge cases: zero, negative, very large values display correctly | User on Product Detail page for Product I (price = 0), Product J (price < 0), Product K (price very large e.g., 999999999.99) | 1. Open Product Detail page for Product I and inspect displayed price.<br>2. Open Product Detail page for Product J and inspect displayed price and any validation/warning.<br>3. Open Product Detail page for Product K and inspect displayed price formatting. | Prices are rendered with consistent formatting (e.g., currency symbol, decimals). For zero price, display 'Free' or '$0.00' as per spec; negative prices should show a clear validation or prefix (e.g., '-$X' or an admin error indicator); very large values are formatted with separators and do not break layout | medium |
| TC-014 | WF-001,WF-002 | Product state updated externally (added/removed from another tab) reflects on Product Detail when refocused/refresh | User has Product Detail page for Product L open in Tab A, User can modify cart in Tab B | 1. In Tab B, add Product L to cart (so state becomes In Cart).<br>2. Return to Tab A (Product Detail) and either focus the tab or refresh the page.<br>3. Observe the action bar state.<br>4. In Tab B, remove Product L from cart (state becomes Not in Cart).<br>5. Return to Tab A and refresh/focus and observe the action bar state. | After focus/refresh, Product Detail action bar correctly reflects external changes: when added externally it shows 'Remove'; when removed externally it shows 'Add to cart' | high |

---

## Shopping Cart

Total: **15** (positive: 4, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove single item from cart (happy path) | User logged in as Shopper, Cart contains exactly 1 item visible in Cart_Items_Table | 1. Open Shopping Cart page<br>2. Locate the single item row in Cart_Items_Table<br>3. Click the row's Remove button | Item row is removed from the table and the shopping cart shows an empty state message (e.g., 'Your cart is empty') on the current screen; Checkout button is disabled or hidden | high |
| TC-002 | WF-001 | Remove one item from multiple items (happy path) | User logged in as Shopper, Cart contains 3 distinct items visible in Cart_Items_Table | 1. Open Shopping Cart page<br>2. Identify the middle item row<br>3. Click that row's Remove button | Selected item row is removed from the table; remaining two item rows stay visible and the cart item count visible in header (if present) decrements by 1 on the current screen | high |
| TC-007 | WF-002 | Click Continue Shopping navigates to Product Inventory (happy path) | User logged in as Shopper, Shopping Cart page is open | 1. On Shopping Cart page, click the Continue Shopping link | Browser navigates to Product Inventory and the Product Inventory page is visible (product list displayed) on the current screen | high |
| TC-010 | WF-003 | Begin checkout with items in cart (happy path) | User logged in as Shopper, Cart contains at least 1 item | 1. Open Shopping Cart page<br>2. Click the Checkout button | Checkout process begins and the user is navigated to the first checkout screen (e.g., shipping/address entry) visible on the current screen | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Remove item with simulated network failure (negative) | User logged in as Shopper, Cart contains at least 1 item, Simulate network failure or API error for remove-item endpoint | 1. Open Shopping Cart page<br>2. Click the Remove button for any item row | Removal does not occur; item row remains visible and a visible error message or toast is shown on the current screen (e.g., 'Unable to remove item. Please try again.') | high |
| TC-004 | WF-001 | Rapid double-click Remove (negative / idempotency) | User logged in as Shopper, Cart contains at least 1 item | 1. Open Shopping Cart page<br>2. Rapidly click the same row's Remove button twice in quick succession | Item is removed only once; no duplicate errors or UI corruption; second click is ignored or disabled and no additional rows are removed on the current screen | medium |
| TC-008 | WF-002 | Continue Shopping link broken / 404 (negative) | User logged in as Shopper, Shopping Cart page is open, Simulate Product Inventory endpoint returning 404 or navigation failure | 1. Click the Continue Shopping link | Navigation does not succeed; visible error or fallback appears on the current screen (e.g., 404 page or error toast 'Unable to load Product Inventory') | medium |
| TC-011 | WF-003 | Attempt checkout with empty cart (negative) | User logged in as Shopper, Cart is empty | 1. Open Shopping Cart page<br>2. Attempt to click the Checkout button | Checkout is blocked: either Checkout button is disabled/unresponsive, or a visible message appears on the current screen (e.g., 'Your cart is empty') and no checkout navigation occurs | high |
| TC-015 | WF-001 | Actions when user session is expired (negative / security) | User was previously logged in as Shopper but session is expired, Shopping Cart page is open (session expired while on page) | 1. Click Remove on any item row<br>2. Click Continue Shopping link<br>3. Click Checkout button | Any of these actions redirect the user to the Login page or show a visible authentication error on the current screen (e.g., 'Please sign in'); no item removals or checkout progress occurs until authentication is completed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Remove last item shows empty cart and disables Checkout (edge) | User logged in as Shopper, Cart contains exactly 1 item | 1. Open Shopping Cart page<br>2. Click Remove on the last item row | Item row removed and page shows explicit empty cart state (e.g., 'Your cart is empty'); Checkout button is disabled or not clickable on the current screen | high |
| TC-006 | WF-001 | Remove item with very long description and special characters (edge) | User logged in as Shopper, Cart contains an item whose description is extremely long (e.g., >1000 chars) and includes special characters | 1. Open Shopping Cart page<br>2. Locate the long-description item row<br>3. Click the row's Remove button | Item row is removed and UI does not break or overflow; other rows remain visible; any truncated display remains visually intact on the current screen | medium |
| TC-009 | WF-002 | Continue Shopping keyboard accessibility (edge / positive) | User logged in as Shopper, Shopping Cart page is open, Continue Shopping link is focusable | 1. Tab focus to the Continue Shopping link<br>2. Press Enter / Space | Keyboard activation navigates to Product Inventory; Product Inventory page becomes visible on the current screen | medium |
| TC-012 | WF-003 | Begin checkout under slow network (edge) | User logged in as Shopper, Cart contains at least 1 item, Simulate high latency on checkout initiation endpoint | 1. Open Shopping Cart page<br>2. Click the Checkout button | Loading indicator or spinner is visible while checkout initializes; once the request completes the checkout page loads on the current screen; no duplicate navigations occur | medium |
| TC-013 | WF-001 | Cart with very large number of items (performance edge) | User logged in as Shopper, Cart contains a large number of items (e.g., 1000 rows) | 1. Open Shopping Cart page<br>2. Scroll to an arbitrary middle row<br>3. Click Remove on that row | Specified item row is removed and UI remains responsive; table continues to scroll correctly and other rows remain intact on the current screen; removal completes within an acceptable time threshold (e.g., <2s) | medium |
| TC-014 | WF-001 | Long description truncation and tooltip behavior when removing (edge) | User logged in as Shopper, Cart contains an item with a product name longer than visible column width | 1. Open Shopping Cart page<br>2. Hover over truncated product description to reveal tooltip (if implemented)<br>3. Click Remove on that row | Tooltip shows full description on hover (if supported); after clicking Remove, the item row is removed and tooltip no longer appears; table layout remains consistent on the current screen | low |

---

## Checkout - Information

Total: **13** (positive: 5, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with valid typical values proceeds to Overview | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "John"<br>2. Enter Last Name = "Doe"<br>3. Enter Zip/Postal Code = "12345"<br>4. Click the Continue button | User is redirected to the Overview step (Checkout Overview page is displayed) and the order summary is visible | high |
| TC-002 | WF-002 | Cancel returns user to Shopping Cart | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Click the Cancel button | User is returned to the Shopping Cart page and the cart contents are visible | high |
| TC-008 | WF-001 | Minimum length (1-character) values accepted | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "A"<br>2. Enter Last Name = "B"<br>3. Enter Zip/Postal Code = "1"<br>4. Click the Continue button | User is redirected to the Overview step (Checkout Overview page is displayed) | medium |
| TC-010 | WF-001 | Alphanumeric postal code accepted (e.g., Canadian style) and proceeds | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "Anna"<br>2. Enter Last Name = "Smith"<br>3. Enter Zip/Postal Code = "A1B 2C3"<br>4. Click the Continue button | User is redirected to the Overview step (Checkout Overview page is displayed) | medium |
| TC-013 | WF-002 | Click Cancel after entering values returns to Shopping Cart and preserves cart | User is on Checkout - Information page, User has at least one item in the Shopping Cart, User has entered values into First Name, Last Name, and Zip/Postal Code fields | 1. Click the Cancel button | User is returned to the Shopping Cart page and the cart contents are visible; Checkout - Information is closed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Continue with missing First Name shows required error | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Leave First Name blank<br>2. Enter Last Name = "Doe"<br>3. Enter Zip/Postal Code = "12345"<br>4. Click the Continue button | Checkout - Information remains displayed and an error banner 'Error: First Name is required' is shown; other fields retain their entered values | high |
| TC-004 | WF-001 | Continue with missing Last Name shows required error | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "John"<br>2. Leave Last Name blank<br>3. Enter Zip/Postal Code = "12345"<br>4. Click the Continue button | Checkout - Information remains displayed and an error banner 'Error: Last Name is required' is shown; other fields retain their entered values | high |
| TC-005 | WF-001 | Continue with missing Zip/Postal Code shows required error | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "John"<br>2. Enter Last Name = "Doe"<br>3. Leave Zip/Postal Code blank<br>4. Click the Continue button | Checkout - Information remains displayed and an error banner 'Error: Postal Code is required' is shown; other fields retain their entered values | high |
| TC-006 | WF-001 | Continue with all required fields missing shows all error banners | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Leave First Name blank<br>2. Leave Last Name blank<br>3. Leave Zip/Postal Code blank<br>4. Click the Continue button | Checkout - Information remains displayed and error banners 'Error: First Name is required', 'Error: Last Name is required', and 'Error: Postal Code is required' are all shown | high |
| TC-007 | WF-001 | Whitespace-only input treated as missing and shows required errors | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "   " (spaces only)<br>2. Enter Last Name = "   " (spaces only)<br>3. Enter Zip/Postal Code = "   " (spaces only)<br>4. Click the Continue button | Checkout - Information remains displayed and error banners for missing fields are shown (at minimum: 'Error: First Name is required', 'Error: Last Name is required', 'Error: Postal Code is required') | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Very long names (255 characters) accepted and proceeds to Overview | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = 255-character string (e.g., 'A' repeated 255 times)<br>2. Enter Last Name = 255-character string (e.g., 'B' repeated 255 times)<br>3. Enter Zip/Postal Code = "12345"<br>4. Click the Continue button | If no max-length validation is present, user is redirected to the Overview step (Checkout Overview page is displayed). If the system enforces a max-length validation, an appropriate validation error is displayed and the page remains on Checkout - Information | low |
| TC-011 | WF-001 | Postal code with dash (e.g., '12345-6789') accepted | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "Mark"<br>2. Enter Last Name = "Lee"<br>3. Enter Zip/Postal Code = "12345-6789"<br>4. Click the Continue button | User is redirected to the Overview step (Checkout Overview page is displayed) if the format is accepted; otherwise a postal code validation error is displayed and the page remains on Checkout - Information | low |
| TC-012 | WF-001 | Non-Latin characters in names accepted (Unicode support) | User is on Checkout - Information page, User has at least one item in the Shopping Cart | 1. Enter First Name = "Иван"<br>2. Enter Last Name = "李"<br>3. Enter Zip/Postal Code = "12345"<br>4. Click the Continue button | User is redirected to the Overview step (Checkout Overview page is displayed) if Unicode names are supported; otherwise a validation error is shown and the page remains on Checkout - Information | low |

---

## Checkout - Overview

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout (happy path) navigates to confirmation | User logged in as Customer, Cart contains one or more purchasable items, Valid payment method is present, Valid shipping address is set, Overview step is displayed | 1. On the Overview step, verify order summary, totals, payment and shipping info are visible<br>2. Click the 'Finish' button | Completes order and redirects to Order Confirmation page showing order number, 'Thank you' message and order summary | high |
| TC-002 | WF-002 | Cancel checkout exits checkout and returns to shopping context | User logged in as Customer, User is on the Overview step with items in cart | 1. On the Overview step, click the 'Cancel' button | Exits checkout and navigates back to shopping context (e.g., Shopping Cart or Product listing); the user is no longer in checkout flow and Overview screen is closed | high |
| TC-007 | WF-001 | Overview displays correct totals calculation (item total + tax = total) | User logged in as Customer, Cart contains known items with deterministic prices (e.g., Item A $10 x2, Item B $5 x1), Tax rules known for the test environment, Overview step displayed | 1. On Overview, calculate expected item total from visible line items<br>2. Calculate expected tax per configured rate<br>3. Verify displayed Item total, Tax and Total match the expected calculation | Displayed 'Item total', 'Tax' and 'Total' values match the expected calculation and are consistent with line item amounts | high |
| TC-008 | WF-001 | Overview displays payment and shipping summary correctly (masked payment, formatted address) | User logged in as Customer, Payment method on file (e.g., card ending 1234), Shipping address present, Overview step displayed | 1. On Overview, locate Payment information section and Shipping information section<br>2. Verify payment is masked (e.g., 'Visa •••• 1234') and shipping address is correctly formatted/truncated if long | Payment shows masked details (no full card number), shipping address is displayed in expected format; both sections are visible and readable on the Overview screen | medium |
| TC-013 | WF-002 | Cancel preserves cart contents after exiting checkout | User logged in as Customer, Cart contains multiple items, On Overview step | 1. Click 'Cancel' on the Overview step<br>2. Navigate to Shopping Cart or other shopping context | User is out of checkout and returned to shopping context; cart contents remain intact and unchanged (items and quantities preserved) | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Finish blocked when no payment method is available | User logged in as Customer, Cart contains items, No payment method is set or payment method is invalid, Overview step is displayed | 1. On Overview, confirm payment section shows 'No payment method' or similar<br>2. Click the 'Finish' button | Order is not completed; UI remains on Overview and a visible validation/error message is shown (e.g., 'Payment method required' or 'Please select a payment method') and 'Finish' does not complete the order | high |
| TC-004 | WF-001 | Finish blocked when shipping address missing | User logged in as Customer, Cart contains items, No shipping address is set, Overview step is displayed | 1. On Overview, confirm shipping section indicates missing address<br>2. Click the 'Finish' button | Order is not completed; Overview remains visible and a clear validation/error message is shown (e.g., 'Shipping address required') preventing completion until address is added | high |
| TC-005 | WF-001 | Finish prevented when displayed totals differ from server calculation | User logged in as Customer, Overview displays item prices and totals, Server-side price or tax changed causing mismatch with displayed totals | 1. On Overview, verify displayed totals<br>2. Click the 'Finish' button (simulate server recalculation/mismatch)<br>3. Observe system response | System blocks completion and displays a visible warning or modal indicating prices changed and shows updated totals; user remains on Overview and must acknowledge or refresh to proceed | medium |
| TC-006 | WF-001 | Handle network/server error when finishing order | User logged in as Customer, Cart valid, payment and shipping set, Overview step displayed, Simulate network error or server 5xx on submit | 1. On Overview, click the 'Finish' button<br>2. Simulate a network/server failure response from order submission endpoint | Order is not completed; Overview remains visible and a clear error notification is displayed (e.g., 'Unable to complete order. Please try again later.'); 'Finish' becomes available for retry or a retry control is shown | medium |
| TC-012 | WF-001 | Prevent duplicate orders when 'Finish' is double-clicked | User logged in as Customer, Cart valid, payment and shipping set, Overview step displayed | 1. On Overview, rapidly double-click the 'Finish' button (simulate quick repeated submissions) | Only a single order is created; UI shows processing state and disables further submissions after the first click (or deduplicates server-side) and user is redirected once to the Order Confirmation page without duplicate orders | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Overview handles very large number of items (performance and rendering) | User logged in as Customer, Cart populated with a very large number of items (e.g., 500 items), Overview step displayed | 1. Navigate to Overview with the large cart<br>2. Observe rendering, scroll behavior, and totals display | Order summary displays all items (via scroll/pagination) without layout breakage; totals are shown and page remains responsive (renders within acceptable time, e.g., under 3 seconds in test environment) | medium |
| TC-010 | WF-001 | Overview handles extremely long item names without layout break | User logged in as Customer, Cart contains an item with an extremely long name (e.g., 1000 characters), Overview step displayed | 1. Open Overview<br>2. Inspect how the long item name is rendered in the item list | Long item name is truncated or wrapped per UI design (no overflow that breaks layout); visual truncation (ellipsis) or wrap is applied and the rest of UI remains intact (no overlap), full name accessible via hover or expand if such UI exists | low |
| TC-011 | WF-001 | Zero-priced item included in totals correctly | User logged in as Customer, Cart contains at least one item with price $0.00 and other paid items, Overview step displayed | 1. On Overview, identify the zero-priced item in order summary<br>2. Verify item shows $0.00 and totals include that item correctly | Zero-priced item is shown with price $0.00 and order Item total, Tax and Total reflect correct arithmetic (zero-priced items do not alter totals incorrectly) | medium |
| TC-014 | WF-001 | Tax rounding boundary is displayed correctly on Overview | User logged in as Customer, Cart contains items whose tax calculation results in fractional cents (e.g., tax = $0.005), Overview step displayed | 1. On Overview, inspect the Tax value shown<br>2. Verify rounding behavior conforms to expected rule (e.g., round to nearest cent) | Tax displayed is rounded to currency precision consistently (e.g., $0.01) and Item total + Tax equals displayed Total after rounding | medium |

---

## Checkout - Confirmation

Total: **14** (positive: 5, negative: 3, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirmation page displays success message and Back Home button | User is an authenticated shopper, User completed checkout and was redirected to the Confirmation page | 1. Navigate to the Confirmation page after a successful checkout<br>2. Observe the page content | A success message is visible on the Confirmation page (for example: "Thank you for your order!") and a visible, enabled "Back Home" button is present | high |
| TC-002 | WF-001 | Clicking Back Home returns to Product Inventory and clears the cart | User is an authenticated shopper, Cart contains items prior to checkout, User is on the Confirmation page after completing checkout | 1. On the Confirmation page, click the "Back Home" button | User is redirected to the Product Inventory page and the cart is cleared (cart icon shows 0 items or an empty cart view is shown) | high |
| TC-003 | WF-001 | Activate Back Home via keyboard (Enter) navigates to inventory and clears cart | User is an authenticated shopper, User is on the Confirmation page, Back Home button is focused via Tab or programmatically | 1. Focus the "Back Home" button (Tab until focused)<br>2. Press Enter key | User is redirected to the Product Inventory page and the cart is cleared; focus lands appropriately on inventory page (visible inventory items) | high |
| TC-004 | WF-001 | Activate Back Home via keyboard (Space) navigates to inventory and clears cart | User is an authenticated shopper, User is on the Confirmation page, Back Home button is focused | 1. Focus the "Back Home" button<br>2. Press Spacebar | User is redirected to the Product Inventory page and the cart is cleared | high |
| TC-011 | WF-001 | Mobile viewport: Back Home functions on narrow screens | User is on the Confirmation page on a mobile device or emulator (small viewport), User completed checkout | 1. On the mobile/viewport-sized Confirmation page, locate and tap the "Back Home" button | User is redirected to the Product Inventory page optimized for the mobile viewport and the cart is cleared (cart icon shows 0 items) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Server failure while clearing cart: show error and prevent navigation | User completed checkout and is on the Confirmation page, Simulate server-side failure when attempting to clear server-side cart (e.g., API returns 500) | 1. Click the "Back Home" button while server-side cart-clear endpoint is failing | User remains on the Confirmation page and a visible error message appears such as "Unable to clear cart. Please try again." The cart still shows previous items until the issue is resolved | high |
| TC-007 | WF-001 | Browser with JavaScript disabled: Back Home fallback behavior | User completed checkout and is on the Confirmation page, Browser JavaScript is disabled | 1. Attempt to use the Back Home control (click visible button or link) with JavaScript disabled | If a non-JavaScript fallback link is present it navigates to Product Inventory; if no fallback exists, clicking the control does nothing and an instruction or visible fallback message should be shown (e.g., "Enable JavaScript to continue" or provide a visible link). The system must not silently fail without user feedback | medium |
| TC-013 | WF-001 | Multiple tabs: clicking Back Home in one tab clears cart in other tabs | User has two browser tabs open with the app and both are on or can reach the Confirmation page, Cart had items prior to checkout and user completed checkout in tab A | 1. In tab A, click the "Back Home" button<br>2. Switch to tab B (which still displayed the old cart state)<br>3. Refresh tab B or interact with the cart indicator | Cart state is synchronized: tab B reflects the cleared cart (cart shows 0 items) after refresh or on synchronous update. The app should not show conflicting cart contents between tabs; if a race condition occurs, an appropriate error or reconciliation should be displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Double-click Back Home does not produce duplicate navigation or duplicate order effects | User completed checkout and is on the Confirmation page, Cart contained items prior to checkout | 1. Rapidly double-click the "Back Home" button | Single navigation to Product Inventory occurs (no duplicate navigation overlays) and the cart is cleared exactly once (cart shows 0 items); no duplicate orders are created | medium |
| TC-008 | WF-001 | Click Back Home when cart is already empty | User completed checkout and the cart is already empty (e.g., previous cleanup), User is on the Confirmation page | 1. Click the "Back Home" button | User is redirected to the Product Inventory page and no error occurs; cart remains empty and inventory is visible | medium |
| TC-009 | WF-001 | Large cart prior to checkout: ensure Back Home clears large item counts | User placed a very large number of items into the cart and completed checkout, User is on the Confirmation page | 1. Click the "Back Home" button | User is redirected to the Product Inventory page and the cart is cleared (cart count shows 0); no timeout or partial-clear state is observed | medium |
| TC-010 | WF-001 | Back Home accessibility: visible focus, ARIA, and keyboard reachability | User is on the Confirmation page, Accessibility audit tools available | 1. Tab through the page elements until the Back Home button receives focus<br>2. Verify that a visible focus indicator appears<br>3. Inspect the DOM for accessible attributes (e.g., aria-label, role) for the Back Home control | Back Home is reachable by keyboard, has a visible focus indicator, and includes appropriate accessibility attributes such as an accessible name/aria-label (visible as 'Back Home' or equivalent) | low |
| TC-012 | WF-001 | Browser back button after using Back Home does not restore cleared cart | User completed checkout and clicked "Back Home" to return to Product Inventory (cart cleared), User is on the Product Inventory page | 1. From Product Inventory, press the browser Back button | If browser navigates back to the Confirmation page, the cart remains cleared (cart count shows 0) and no items are restored into the cart; if the app restores previous UI state, cart must still show empty and not contain previously cleared items | medium |
| TC-014 | WF-001 | Long localized success message does not overlap Back Home or break layout | User is on the Confirmation page, Application locale set to one with an unusually long success string | 1. Load the Confirmation page with the long localized success message<br>2. Observe layout and the Back Home button position | Long success message is fully visible or properly truncated with ellipses and accessible (e.g., tooltip), and the "Back Home" button remains visible and usable without layout overlap | low |

---

## Logout

Total: **15** (positive: 6, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Logout from Inventory page (header button) | User logged in as Standard User, Current page: Inventory (protected) | 1. Verify the Logout button is visible in the header<br>2. Click the Logout button | User is immediately redirected to the Login page showing username/password fields and Login button; Logout button is no longer visible; attempting to navigate to any protected page redirects to Login | high |
| TC-002 | WF-001 | Logout from Product Detail page | User logged in as Standard User, Current page: Product Detail (protected) | 1. Verify the Logout button is visible in the header<br>2. Click the Logout button | User is redirected to the Login page with login form visible; protected pages (including Product Detail) require login to be accessed again | high |
| TC-003 | WF-001 | Logout from Cart page | User logged in as Standard User, Current page: Cart (protected) | 1. Confirm cart contents are visible<br>2. Click the Logout button | Session ends and user is redirected to Login page; cart contents are not accessible until login; Logout button no longer visible | high |
| TC-004 | WF-001 | Logout from Checkout page (end active checkout session) | User logged in as Standard User, Current page: Checkout (protected), active checkout in progress | 1. Click the Logout button during checkout<br>2. Observe redirection and session state | User is redirected to Login page; checkout page is not accessible without login and any in-progress checkout actions require re-login; Logout button no longer visible | high |
| TC-005 | WF-001 | Logout via keyboard activation (Enter/Space) for accessibility | User logged in as Standard User, Logout button is in focusable state | 1. Focus the Logout button using keyboard (Tab)<br>2. Press Enter (or Space) to activate the button | Logout action is performed and user is redirected to Login page; Logout button removed from UI; keyboard activation functions identically to mouse click | medium |
| TC-006 | WF-001 | Logout in one tab invalidates session in another tab (multi-tab sync) | User logged in as Standard User in two browser tabs (Tab A and Tab B), Both tabs show protected pages | 1. In Tab A, click Logout<br>2. Switch to Tab B and attempt to navigate or interact with a protected page (e.g., click a product or refresh) | Tab A redirects to Login page; Tab B either automatically redirects to Login on next navigation/refresh or shows Login page when a protected resource is requested; protected pages are inaccessible until re-login | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Logout button visibility when user is not logged in | User is not logged in (on Login page) | 1. Navigate to the Login page<br>2. Check header and application chrome for presence of Logout button | Logout button is not visible or is disabled; no logout action is available to unauthenticated users | medium |
| TC-008 | WF-001 | Access protected page by URL after logout | User was logged in and has just clicked Logout and been redirected to Login | 1. In the browser address bar enter the URL for a protected page (e.g., /inventory) after logout<br>2. Press Enter to navigate | Application redirects to Login page and does not present the protected page content; URL may remain the protected URL but Login form must be visible and access to protected data blocked | high |
| TC-009 | WF-001 | Browser Back button after logout should not reveal protected content | User logged in and on a protected page, User clicks Logout and is on Login page | 1. While on the Login page after logout, press the browser Back button<br>2. Observe the content shown | Protected content is not displayed from cache; either the browser navigates to a non-protected page or the app re-validates session and redirects/shows the Login page; protected actions require login | high |
| TC-010 | WF-001 | Logout attempt during simulated network failure | User logged in as Standard User, Simulate network offline or API failure prior to clicking Logout | 1. Simulate network failure (e.g., offline mode or block logout endpoint)<br>2. Click Logout<br>3. Observe UI behavior and session state | User is presented with an error message indicating logout failed OR the client clears local session and shows Login page depending on implementation; critical expectation: no protected API calls should succeed without re-login (if client attempted logout and failed, user may remain logged in until retry). The UI must not silently leave the user in an ambiguous authenticated state. | medium |
| TC-011 | WF-001 | API access with old session token after logout should be rejected (401) and UI should require login | User logged in as Standard User, Capture current session token, User clicks Logout and is redirected to Login | 1. Using a REST/API tool or browser console, send a request to a protected API endpoint (e.g., GET /api/inventory) using the previously captured token after logout<br>2. Observe server response and UI behavior if the request is made from the app | Server responds with 401 Unauthorized (or equivalent) and the app redirects the user to Login page if the request was initiated from the client; old token cannot access protected resources | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Rapid repeated clicks on Logout button (debounce/throttle) | User logged in as Standard User, Current page: any protected page with Logout visible | 1. Rapidly click the Logout button multiple times (e.g., 5-10 clicks within 1 second)<br>2. Observe navigation and any error messages | Only a single logout operation is performed (single redirect to Login); UI does not show duplicate error dialogs or leave multiple pending redirects; application remains stable | medium |
| TC-013 | WF-001 | Logout with tampered/invalid session token stored in cookie/localStorage | User logged in as Standard User, Manually modify session token value in cookie/localStorage to an invalid value | 1. With the tampered token in place, click Logout<br>2. Observe server response and client behavior | Server rejects invalid token if presented; client should clear local session state and display Login page; protected pages remain inaccessible without valid login | medium |
| TC-014 | WF-001 | Logout in one tab updates UI state in other open tabs (UI synchronization) | User logged in in multiple tabs (Tab A and Tab B), Both tabs have app UI visible | 1. In Tab A, click Logout<br>2. Without refreshing Tab B, attempt to interact with Tab B (e.g., click a protected link or refresh)<br>3. Observe Tab B behavior | Tab A redirects to Login page; Tab B either detects logout via storage event or on next interaction/refresh shows Login page and hides Logout button; protected actions require re-login | medium |
| TC-015 | WF-001 | Logout when session is at immediate expiry boundary | User logged in as Standard User, Session is nearing automatic expiry (simulate or wait until last few seconds) | 1. At the boundary moment, click Logout<br>2. Observe whether logout completes and redirect occurs or if session expiry interferes | Logout completes and user is redirected to Login page; session is not left in a partial or inconsistent state; protected pages are inaccessible without re-login | low |

---

## Reset App State

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset clears a populated cart and resets UI states | User logged in as standard user, App main screen open, Cart contains 3 distinct items, Cart badge shows '3', Product list shows correct 'Remove' states for items already added | 1. Verify cart shows 3 items and cart badge = 3<br>2. Tap the 'Reset App State' button | Cart list is empty (no items listed), cart badge is hidden or shows '0', all product list add/remove buttons are reset to default 'Add' state, user remains logged in and stays on the same screen (no logout or redirect), no error message shown | high |
| TC-002 | WF-001 | Reset when cart already empty does nothing harmful | User logged in as standard user, App main screen open, Cart is already empty, Cart badge hidden or shows '0' | 1. Confirm the cart is empty<br>2. Tap the 'Reset App State' button | Cart remains empty, cart badge remains hidden or '0', product list buttons remain in default 'Add' state, user remains logged in and stays on the same screen, no error or crash occurs | medium |
| TC-003 | WF-001 | Reset is repeatable after adding items again | User logged in as standard user, App main screen open, Cart initially empty | 1. Add two items to the cart using product 'Add' buttons<br>2. Verify cart badge updates to '2' and product buttons show 'Remove' where appropriate<br>3. Tap 'Reset App State' button<br>4. Verify cart cleared as in TC-001<br>5. Add one item to cart again and verify cart badge = 1 and product button = 'Remove'<br>6. Tap 'Reset App State' button again | After each reset the cart becomes empty and UI resets to default states; repeated resets behave identically and do not log out the user or cause errors | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Reset button not available or prompts for login for unauthenticated users | User is not logged in (guest), App main screen open | 1. Observe presence/state of 'Reset App State' button for guest user<br>2. If button is visible, tap the 'Reset App State' button | Either the 'Reset App State' button is not visible/disabled for unauthenticated users, or tapping it prompts the guest to log in (showing login dialog or redirect to login) and does not clear any authenticated user-specific state; the app must not crash | medium |
| TC-005 | WF-001 | Reset is disabled during an active checkout flow | User logged in as standard user, User has initiated checkout (checkout flow screen open / payment in progress), App main screen or checkout screen visible | 1. While checkout is active, locate the 'Reset App State' button<br>2. Attempt to tap the 'Reset App State' button | If reset is restricted during checkout, the button is disabled or tapping it shows a clear message indicating reset is not allowed during checkout; cart and checkout state remain unchanged and user remains logged in; no silent partial clears occur | low |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Reset handles very large cart (performance/boundary) | User logged in as standard user, App main screen open, Cart contains a very large number of items (e.g., 10,000 simulated items or the app's documented upper limit) | 1. Confirm cart item count is very large (e.g., 10,000) and cart badge reflects count<br>2. Tap the 'Reset App State' button<br>3. Observe UI responsiveness and completion time | Cart is cleared (no items listed) and cart badge hidden or shows '0' within acceptable performance limits (no UI freeze/crash); add/remove button states are reset; user remains logged in and app remains responsive | high |
| TC-007 | WF-001 | Reset is idempotent under rapid repeated clicks | User logged in as standard user, App main screen open, Cart contains multiple items (e.g., 5 items) | 1. Verify cart contains items and cart badge shows count<br>2. Rapidly tap the 'Reset App State' button multiple times (double-click and a rapid 5-click sequence)<br>3. Observe UI and final state after interactions | The reset operation is idempotent: cart ends up cleared with no duplicate or inconsistent UI state; no crashes or error dialogs; cart badge hidden or '0'; product buttons reset to 'Add'; user remains logged in | high |
| TC-008 | WF-001 | Reset during concurrent background add (race condition) | User logged in as standard user, App main screen open, An automated background process or second client can add items concurrently (test harness available to simulate concurrent adds) | 1. Start a background add operation that will add items to cart with a slight delay<br>2. Immediately tap 'Reset App State' while background adds are in-flight<br>3. Wait for background add to complete<br>4. Inspect final cart contents and UI state | App remains stable and does not crash; final cart state is consistent (either empty if reset supersedes adds, or contains items added after reset but without duplicated UI errors); cart badge and product button states reflect the final actual cart contents; user remains logged in | medium |

---
