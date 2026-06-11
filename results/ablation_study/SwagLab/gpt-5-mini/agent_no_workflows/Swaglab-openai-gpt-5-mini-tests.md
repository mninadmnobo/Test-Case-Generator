# Test Cases — Swaglab

Generated: 2026-06-10T18:47:05.492401Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 94 | 32 | 24 | 38 | 38 | 44 | 12 |

## Login

Total: **13** (positive: 3, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with standard_user redirects to Product Inventory | User not authenticated | 1. Open the Login page<br>2. Enter standard_user in the Username field<br>3. Enter secret_sauce in the Password field<br>4. Click the Login button | redirects to Product Inventory page | high |
| TC-002 |  | Successful login with performance_glitch_user redirects to Product Inventory | User not authenticated | 1. Open the Login page<br>2. Enter performance_glitch_user in the Username field<br>3. Enter secret_sauce in the Password field<br>4. Click the Login button | redirects to Product Inventory page | medium |
| TC-003 |  | Login page displays accepted test usernames and shared password | User not authenticated | 1. Open the Login page<br>2. Observe the credentials/help area on the page | The page displays the accepted usernames: standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user; and the shared password 'secret_sauce' is shown | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Username required - leave Username blank and submit | Login page is open | 1. Leave the Username field blank<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Inline validation error appears on the Username field indicating "Epic sadface: Username is required."; the form does not submit; no redirect to the Product Inventory page. | high |
| TC-005 |  | Password required - leave Password blank and submit | Login page is open | 1. Enter standard_user in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | Inline validation error appears on the Password field indicating "Epic sadface: Password is required."; the form does not submit; no redirect to the Product Inventory page. | high |
| TC-006 |  | All required fields empty - submit with both Username and Password blank | Login page is open | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Username field displays inline error "Epic sadface: Username is required." and Password field displays inline error "Epic sadface: Password is required."; the form does not submit; no redirect to the Product Inventory page. | high |
| TC-007 |  | Invalid username - username not in accepted_usernames with correct shared password | Login page is open | 1. Enter <username not in accepted_usernames> in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Error banner displays "Epic sadface: Username and password do not match any user in this service."; the form does not submit; no redirect to the Product Inventory page. | high |
| TC-008 |  | Invalid password - accepted username with non-shared password | Login page is open | 1. Enter standard_user in the Username field<br>2. Enter <password not equal to secret_sauce> in the Password field<br>3. Click the Login button | Error banner displays "Epic sadface: Username and password do not match any user in this service."; the form does not submit; no redirect to the Product Inventory page. | high |
| TC-009 |  | Locked out user - locked_out_user cannot log in even with shared password | Login page is open | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Error banner displays "Epic sadface: Sorry, this user has been locked out."; the form does not submit; user remains on the Login page and is not redirected to the Product Inventory page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) |  | Very long Username (>200 chars) with valid shared password | Login page is loaded | 1. Enter a very long string (>200 characters) in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; an error banner displays: "Epic sadface: Username and password do not match any user in this service." (the long Username is not in the accepted_usernames list) | medium |
| TC-011 (input_edge) |  | Username containing emoji / non‑ASCII characters with valid shared password | Login page is loaded | 1. Enter a Username value containing emoji and non-ASCII Unicode characters (e.g. characters outside ASCII) in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; an error banner displays: "Epic sadface: Username and password do not match any user in this service." (the Unicode/emoji Username is not in the accepted_usernames list) | medium |
| TC-012 (input_edge) |  | Username with leading and trailing whitespace and valid shared password | Login page is loaded | 1. Enter the accepted Username value surrounded by leading and trailing whitespace in the Username field (e.g. " <accepted_username> ")<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Login is blocked; an error banner displays: "Epic sadface: Username and password do not match any user in this service." (username + whitespace does not match an accepted_username exactly) | medium |
| TC-013 (interaction_edge) |  | After successful login, press browser Back and submit with empty fields | Login page is loaded | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button<br>4. Observe redirect to the Product Inventory page<br>5. Press the browser Back button<br>6. Click the Login button without entering any values | After pressing Back the Login form is displayed blank; the subsequent submit is blocked and both required field errors are shown: "Epic sadface: Username is required." and "Epic sadface: Password is required." | medium |

---

## Product Inventory

Total: **18** (positive: 7, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Open Product Detail page by clicking Product Name | User logged in as <User>, Product Inventory page is reachable, Product list contains <product> | 1. Open the Product Inventory page<br>2. Click the Product_Name link for <product> | navigates to Product Detail page | high |
| TC-002 |  | Open Product Detail page by clicking Product Image | User logged in as <User>, Product Inventory page is reachable, Product list contains <product> | 1. Open the Product Inventory page<br>2. Click the Product_Image link for <product> | navigates to Product Detail page | high |
| TC-003 |  | Open Product Detail page using 'View Details' row action | User logged in as <User>, Product Inventory page is reachable, Product list contains <product> | 1. Open the Product Inventory page<br>2. Click the row action 'View Details' for <product> | navigates to Product Detail page | high |
| TC-004 |  | Add a product to cart toggles button label to 'Remove' and increments Cart badge | User logged in as <User>, Product <product> is in NotInCart state, Cart_Badge.value is 0 | 1. Open the Product Inventory page<br>2. Click 'Add to cart' on the Product_Row_Action_Bar for <product> | Button label toggles to 'Remove' for <product>; Cart_Badge shows '1' | high |
| TC-005 |  | Remove a product from cart toggles button label to 'Add to cart' and decrements Cart badge | User logged in as <User>, Product <product> is in InCart state, Cart_Badge.value is 1 | 1. Open the Product Inventory page<br>2. Click 'Remove' on the Product_Row_Action_Bar for <product> | Button label toggles to 'Add to cart' for <product>; Cart_Badge shows '0' | high |
| TC-006 |  | Sort products by Price (Low–High) orders list ascending by price | User logged in as <User>, Product Inventory page is reachable, Product list contains at least two products with different prices | 1. Open the Product Inventory page<br>2. Select 'Price (Low–High)' from the Sort_Dropdown | Products list displays items ordered by Price ascending; the product with the lower price appears above the product with the higher price | medium |
| TC-007 |  | Sort products by Name (A–Z) orders list alphabetically | User logged in as <User>, Product Inventory page is reachable, Product list contains at least two products with distinct names | 1. Open the Product Inventory page<br>2. Select 'Name (A–Z)' from the Sort_Dropdown | Products list displays items in alphabetical order (A–Z); a product whose name is earlier alphabetically appears above one that is later | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Unauthenticated access to Product Inventory page is blocked | User is not logged in | 1. Open the Product Inventory page URL in the browser while not logged in | User is redirected to the Login page; the Product Inventory listing is not shown (no product rows, no Sort_Dropdown, no Cart_Badge). | high |
| TC-009 |  | Unauthenticated access to Product Detail page is blocked | User is not logged in, A product exists with a Detail page | 1. Open the Product Detail page URL for <a product> while not logged in<br>2. (Alternative UI) On the Product Inventory page, click the <Product_Name> link while not logged in | User is redirected to the Login page; the Product Detail page content is not displayed. | high |
| TC-010 |  | Attempt 'Remove' action when product state is NotInCart (wrong-state action) | User is logged in, There is a product currently in the NotInCart state | 1. Log in as a valid user<br>2. Open the Product Inventory page<br>3. Locate <a product currently in NotInCart state> in the product list<br>4. Attempt to click a 'Remove' button in that product's row (search for a 'Remove' control and click it if present) | No 'Remove' button is visible for that product row; clicking has no effect. Product state remains NotInCart; Cart_Badge.value remains unchanged. | high |
| TC-011 |  | Attempt 'Add to cart' action when product state is already InCart (wrong-state action) | User is logged in, There is a product currently in InCart state (e.g., added previously) | 1. Log in as a valid user<br>2. Open the Product Inventory page<br>3. Locate <a product currently in InCart state> in the product list<br>4. Attempt to click an 'Add to cart' button in that product's row (search for an 'Add to cart' control and click it if present) | No 'Add to cart' button is visible for that product row; clicking has no effect. Product state remains InCart; Cart_Badge.value remains unchanged. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (state_edge) |  | Rapid double-click 'Add to cart' on same product row | user must be logged in, Product Inventory page is loaded, Target product row is in NotInCart state (button label 'Add to cart'), Cart_Badge.value = <n> (record current value as baseline) | 1. On the Product Inventory page, locate the target product row<br>2. Click the 'Add to cart' button on that product row<br>3. Immediately click the 'Add to cart' button on the same product row a second time (within a short burst) | First click succeeds: Cart_Badge.value increments by 1 relative to baseline, the product row button label changes to 'Remove', and the product state updates to InCart. The second immediate click is ignored (does not increment Cart_Badge again); Cart_Badge.value remains incremented by 1 and the button remains 'Remove'. | medium |
| TC-013 (state_edge) |  | Rapid double-click 'Remove' on same product row (prevent double-decrement) | user must be logged in, Product Inventory page is loaded, Target product row is in InCart state (button label 'Remove'), Cart_Badge.value = <m> where <m> >= 1 | 1. On the Product Inventory page, locate the target product row<br>2. Click the 'Remove' button on that product row<br>3. Immediately click the 'Remove' button on the same product row a second time (within a short burst) | First click succeeds: Cart_Badge.value decrements by 1, the product row button label changes to 'Add to cart', and the product state updates to NotInCart. The second immediate click is ignored; Cart_Badge.value remains at the decremented value and does not go below zero. No negative badge value occurs. | medium |
| TC-014 (state_edge) |  | Rapidly add two different products to cart from the list | user must be logged in, Product Inventory page is loaded, Two distinct product rows A and B are in NotInCart state (button label 'Add to cart'), Cart_Badge.value = <baseline> | 1. On the Product Inventory page, locate product row A<br>2. Click 'Add to cart' on product row A<br>3. On the Product Inventory page, locate product row B<br>4. Click 'Add to cart' on product row B | Both clicks succeed: Cart_Badge.value increments by 2 relative to baseline, product row A and product row B button labels each change to 'Remove', and both product states update to InCart. No duplicate increments for the same row occur. | medium |
| TC-015 (interaction_edge) |  | Add to cart, navigate to Product Detail, then return — cart state persistence | user must be logged in, Product Inventory page is loaded, Target product row is in NotInCart state, Cart_Badge.value = <baseline> | 1. On the Product Inventory page, locate the target product row<br>2. Click the 'Add to cart' button on that product row<br>3. Click the product name link on the same row to navigate to the Product Detail page<br>4. Use the browser Back action (or application back control) to return to the Product Inventory page | The Add action succeeds before navigation: Cart_Badge.value increments by 1 relative to baseline and the product row button label is 'Remove'. After returning, the Product Inventory page shows the same product row with button label 'Remove' and Cart_Badge.value remains incremented by 1. No duplicate items are created and the product state remains InCart. | medium |
| TC-016 (state_edge) |  | Immediate Add then Remove on same product (rapid state flip-flop) | user must be logged in, Product Inventory page is loaded, Target product row is in NotInCart state, Cart_Badge.value = <baseline> | 1. On the Product Inventory page, locate the target product row<br>2. Click the 'Add to cart' button on that product row<br>3. Immediately click the 'Remove' button on the same product row | Both state transitions succeed sequentially: the Add to cart action increments Cart_Badge.value by 1 and changes the button to 'Remove'; the subsequent Remove action decrements Cart_Badge.value back to baseline and changes the button to 'Add to cart'. Final product state is NotInCart and Cart_Badge.value equals baseline. No intermediate negative or duplicate counts occur. | medium |
| TC-017 (input_edge) |  | Very long product name rendering in list and detail views (>200 characters) | user must be logged in, Product Inventory page is loaded, There exists a product whose Product_Name length > 200 characters | 1. On the Product Inventory page, locate the product row with the very long Product_Name<br>2. Observe how the Product_Name is rendered in the Products_List row<br>3. Click the Product_Name link to navigate to the Product Detail page | Rendering behavior is visible and usable: the Products_List row truncates the very long Product_Name with an on-screen indication (e.g., ellipsis) and does not break the table layout, and clicking the Product_Name link succeeds in navigating to the Product Detail page where the full Product_Name is displayed in full. No UI overlap or loss of the row occurs. | low |
| TC-018 (input_edge) |  | Product name/description containing emoji and Unicode characters | user must be logged in, Product Inventory page is loaded, There exists a product whose Product_Name or Description contains emoji and non-ASCII Unicode characters | 1. On the Product Inventory page, locate the product row with emoji / Unicode in Product_Name or Description<br>2. Observe the Product_Name and Description rendering in the row<br>3. Click the Product_Name link to navigate to the Product Detail page | Unicode and emoji render visibly without truncation or replacement characters; clicking the Product_Name link succeeds and navigates to the Product Detail page where the emoji and Unicode characters are displayed correctly. No errors are shown and Cart_Badge is unaffected by viewing. | low |

---

## Product Detail

Total: **12** (positive: 5, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View Product Detail displays image, name, description and price | User logged in as <Customer>, Product <product> exists in inventory | 1. Navigate to the Product Detail page for <product> | Product image, name, description, and price are visible on the Product Detail page | high |
| TC-002 |  | Add to cart button appears and switches to 'Remove' after clicking when product is not in cart | User logged in as <Customer>, Product <product> is Not In Cart | 1. Navigate to the Product Detail page for <product><br>2. Verify the 'Add to cart' button is visible<br>3. Click the 'Add to cart' button | Button label changes to 'Remove', indicating the product is in the cart | high |
| TC-003 |  | Remove button appears and switches to 'Add to cart' after clicking when product is in cart | User logged in as <Customer>, Product <product> is In Cart | 1. Navigate to the Product Detail page for <product><br>2. Verify the 'Remove' button is visible<br>3. Click the 'Remove' button | Button label changes to 'Add to cart', indicating the product is not in the cart | high |
| TC-004 |  | Back to products link redirects to Product Inventory page | User logged in as <Customer>, Product <product> exists in inventory | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Back to products' link | redirects to Product Inventory page | medium |
| TC-005 |  | Cart Icon navigates to Shopping Cart | User logged in as <Customer>, Product <product> exists in inventory | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Cart Icon' | navigates to Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to Remove when product is Not In Cart (Remove action not available) | User is on the Product Detail page for <product>, <product> is in state 'Not In Cart' (not present in the Shopping Cart) | 1. Open the Product Detail page for <product><br>2. Locate the action area where 'Add to cart' / 'Remove' button is shown<br>3. Look for a 'Remove' button<br>4. If a 'Remove' button is present, attempt to click the 'Remove' button | The 'Remove' button is not visible / not present on the page (the UI does not offer a Remove action when the product is 'Not In Cart'); attempting to invoke Remove is not possible; the Shopping Cart contents remain unchanged and <product> remains in state 'Not In Cart'. | high |
| TC-007 |  | Attempt to Add to cart when product is already In Cart (Add action not available) | User is on the Product Detail page for <product>, <product> is in state 'In Cart' (already present in the Shopping Cart) | 1. Open the Product Detail page for <product><br>2. Locate the action area where 'Add to cart' / 'Remove' button is shown<br>3. Look for an 'Add to cart' button<br>4. If an 'Add to cart' button is present, attempt to click the 'Add to cart' button | The 'Add to cart' button is not visible / not present on the page (the UI does not offer Add to cart when the product is already 'In Cart'); attempting to invoke Add to cart is not possible; the Shopping Cart contents remain unchanged (no duplicate entry is created) and <product> remains in state 'In Cart'. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (state_edge) |  | Rapid double-click Add to cart results in a single cart entry | User is on the Product Detail page for a product that is not in the cart (button shows "Add to cart"), Shopping Cart is empty of this product | 1. Click the "Add to cart" button<br>2. Immediately (within one second) click the "Add to cart" button again<br>3. Click the Cart Icon to navigate to the Shopping Cart page | The first Add action succeeds and the second rapid click is ignored; the product appears exactly once in the Shopping Cart list and the Product Detail button shows "Remove" when revisited (no duplicate entry). | medium |
| TC-009 (state_edge) |  | Rapid consecutive Add then Remove transitions end in consistent final state | User is on the Product Detail page for a product that is not in the cart (button shows "Add to cart"), Shopping Cart is empty of this product | 1. Click the "Add to cart" button<br>2. As soon as the button label changes to "Remove", click the "Remove" button<br>3. Click the Cart Icon to navigate to the Shopping Cart page | Sequential state transitions succeed; final state is Not In Cart: the product does not appear in the Shopping Cart and the Product Detail page shows "Add to cart" (no residual/inconsistent entry). | medium |
| TC-010 (interaction_edge) |  | Add to cart then immediately navigate Back to products before add confirmation completes | User is on the Product Detail page for a product that is not in the cart (button shows "Add to cart"), Shopping Cart is empty of this product | 1. Click the "Add to cart" button<br>2. Immediately click the "Back to products" link<br>3. From the Product Inventory page, click the Cart Icon to navigate to the Shopping Cart page | The Add action succeeds in background despite immediate navigation; the product appears in the Shopping Cart (single entry) and revisiting the Product Detail shows the button as "Remove". | medium |
| TC-011 (interaction_edge) |  | Return to Product Detail via browser back/forward and attempt second Add is blocked | User adds the product to cart successfully (Product Detail now shows "Remove"), User navigates back to Product Inventory, then uses browser Back to return to the Product Detail page | 1. On the Product Detail page (after a successful add), click the Back to products link<br>2. Use the browser Back control to return to the Product Detail page<br>3. Click the "Add to cart" button again | The original Add succeeds; the second Add attempt is blocked / error shown (no duplicate entry). Shopping Cart contains only the single originally added product and the Product Detail button remains in the correct state reflecting a single cart entry. | medium |
| TC-012 (interaction_edge) |  | Click Add to cart then refresh the Product Detail page immediately | User is on the Product Detail page for a product that is not in the cart (button shows "Add to cart"), Shopping Cart is empty of this product | 1. Click the "Add to cart" button<br>2. Immediately refresh/reload the Product Detail page<br>3. Click the Cart Icon to navigate to the Shopping Cart page | The Add action succeeds despite the refresh; the Shopping Cart shows the product (single entry) and the Product Detail page after reload shows the button as "Remove" (no duplicate entries or lost add). | low |

---

## Shopping Cart

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Remove an item from the cart via row Remove action | User logged in as <Customer>, Shopping Cart contains <cart item> | 1. Navigate to the Shopping Cart page<br>2. Locate the row for <cart item> in the Cart Items table<br>3. Click the Remove button for <cart item> | The Cart Items table no longer displays a row with description <cart item>; any remaining cart items remain listed | high |
| TC-002 |  | Use Continue Shopping to return to Product Inventory | User logged in as <Customer>, Shopping Cart may contain items | 1. Navigate to the Shopping Cart page<br>2. Click the 'Continue Shopping' link in the page action bar | Product Inventory page is displayed with the product listing visible (navigated to Product Inventory) | medium |
| TC-003 |  | Begin checkout by clicking Checkout on the cart page | User logged in as <Customer>, Shopping Cart contains <cart item> | 1. Navigate to the Shopping Cart page<br>2. Click the 'Checkout' button in the page action bar | The Checkout page is displayed indicating the checkout flow has begun | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Shopping Cart page | User is not authenticated | 1. In a new browser session where no user is signed in, navigate to the <Shopping Cart page URL> | The application prevents access to the Shopping Cart: the user is redirected to the Login page (Login page is displayed and prompts for credentials) and the Shopping Cart content is not shown; the cart is not accessible without signing in. | high |
| TC-005 |  | 'Continue Shopping' link does not navigate to Product Inventory (broken link) | User is authenticated, Shopping Cart contains at least one item | 1. Open the <Shopping Cart page URL> while signed in<br>2. Click the 'Continue Shopping' link in the Cart Page Actions | Clicking 'Continue Shopping' does not navigate to Product Inventory: the browser remains on the Shopping Cart page (URL remains <Shopping Cart page URL>), the Shopping Cart content remains visible, and no Product Inventory page is loaded (i.e., no navigation occurs). | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) |  | Double-click / repeated Remove on the same cart row (idempotence) | User is on the Shopping Cart page, Cart contains at least one item | 1. Locate the Cart_Items_Table row for a specific item<br>2. Click the row's Remove button<br>3. Immediately attempt to click the same row's Remove button again (within 1 second) | First Remove click succeeds: the item's row disappears from Cart_Items_Table and the visible row count decrements. Second attempt is blocked: the Remove control for that removed row is not present/clickable (no additional removal occurs) and no duplicate removal action is performed. | medium |
| TC-007 (interaction_edge) |  | Remove the last item, then attempt Checkout | User is on the Shopping Cart page, Cart contains exactly one item | 1. Click the Remove button for the lone item in the Cart_Items_Table<br>2. Click the Checkout button in the Cart_Page_Actions area | Remove click succeeds: the cart becomes empty and Cart_Items_Table shows no rows. Checkout click is blocked / error shown: Checkout does not begin; the UI indicates checkout cannot proceed for an empty cart (Checkout button disabled or a visible inline message explaining cart is empty). | medium |
| TC-008 (interaction_edge) |  | Rapid double-click Checkout to check duplicate checkout prevention | User is on the Shopping Cart page, Cart contains at least one item | 1. Click the Checkout button in the Cart_Page_Actions area<br>2. Immediately click the Checkout button again (within 1 second) | First Checkout click succeeds: the app begins checkout and navigates to the checkout flow. Second click is blocked: no second navigation or duplicate checkout flow is started; only one checkout process is initiated and only one navigation occurs. | medium |
| TC-009 (input_edge) |  | Very long product description rendering in cart (200+ characters) | A product with a description length of at least 200 characters exists in Product Inventory, That product has been added to the cart and user is on the Shopping Cart page | 1. Open the Shopping Cart page<br>2. Locate the description cell for the long-description item in Cart_Items_Table | Long-description handling succeeds: the Cart_Items_Table displays the item's description without breaking page layout. If the UI truncates the description, the cell shows a visible truncation indicator (ellipsis) and the full text is accessible via the UI affordance; if the UI wraps the text, no horizontal overflow or layout break occurs. | low |

---

## Checkout - Information

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Continue with all required fields filled navigates to Overview step | User logged in as <Customer>, Checkout - Information page is open with First Name, Last Name and Postal Code fields visible | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click the Continue button | Overview step is displayed (the Checkout Overview screen is visible to the user) | high |
| TC-002 |  | Cancel from Information step returns user to Shopping Cart | User logged in as <Customer>, Checkout - Information page is open | 1. Click the Cancel button | Shopping Cart page is displayed (user is returned to the Shopping Cart) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave representative required text field (First Name) blank and submit | User is on the Checkout - Information page | 1. Ensure the First Name field is blank<br>2. Enter <valid last name> into the Last Name field<br>3. Enter <valid postal/zip code> into the Postal Code field<br>4. Click the Continue button | Inline validation error appears on the First Name field indicating it is required; an error banner displays "Error: First Name is required"; the form does not proceed to the overview step and the user remains on the Checkout - Information page | high |
| TC-004 |  | Submit with all required fields empty | User is on the Checkout - Information page | 1. Ensure the First Name field is blank<br>2. Ensure the Last Name field is blank<br>3. Ensure the Postal Code field is blank<br>4. Click the Continue button | Inline validation errors appear on the First Name, Last Name, and Postal Code fields and an error banner displays the messages "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required"; the form does not proceed to the overview step and the user remains on the Checkout - Information page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (boundary) |  | Whitespace-only values in required fields are treated as empty and blocked | User is on the Checkout - Information form | 1. Focus the First_Name field<br>2. Enter <a single space character> in First_Name<br>3. Focus the Last_Name field<br>4. Enter <a single space character> in Last_Name<br>5. Focus the Postal_Code field<br>6. Enter <a single space character> in Postal_Code<br>7. Click the Continue button | Submission is blocked; an error banner and inline field errors are shown. The banner and/or inline messages include the exact text: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required" | medium |
| TC-006 (input_edge) |  | Very long First_Name and Last_Name (200+ characters) handling | User is on the Checkout - Information form | 1. Enter <very long string (200+ characters)> in First_Name<br>2. Enter <very long string (200+ characters)> in Last_Name<br>3. Enter <a non-empty value> in Postal_Code<br>4. Click the Continue button | Form submission succeeds; the app proceeds to the overview step and the overview displays the saved First_Name and Last_Name containing the full entered strings (no visible truncation). If the UI enforces a max-length instead, a visible inline error or truncation indicator is shown before navigation | medium |
| TC-007 (input_edge) |  | Special characters and emoji in name fields | User is on the Checkout - Information form | 1. Enter <special characters and emoji> in First_Name<br>2. Enter <special characters and emoji> in Last_Name<br>3. Enter <a non-empty value> in Postal_Code<br>4. Click the Continue button | Form submission succeeds; the app proceeds to the overview step and the overview displays the saved First_Name and Last_Name including the entered special characters/emoji (no stripping or replacement shown). If the system rejects those characters, an inline error is shown explaining the invalid characters | low |
| TC-008 (interaction_edge) |  | Rapid double-click of Continue results in a single transition to overview | User is on the Checkout - Information form, All required fields contain non-empty values | 1. Click the Continue button<br>2. Immediately (within 1 second) click the Continue button again | Only one navigation to the overview step occurs; the second click is ignored or blocked by the UI. The app proceeds to the overview step once (no visible duplicate navigation or duplicate processing shown) | low |

---

## Checkout - Overview

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Finish checkout from Overview navigates to Confirmation page | User logged in as <Customer>, <Cart contains items>, <Payment method saved>, <Shipping address saved> | 1. Open the Checkout Overview page<br>2. Verify the Order Summary, Totals, Payment and Shipping sections are visible<br>3. Click the Finish button | User is navigated to the Confirmation page; Checkout Overview page is no longer visible | high |
| TC-002 |  | Cancel exits checkout from Overview | User logged in as <Customer>, <Cart contains items>, <Payment method saved>, <Shipping address saved> | 1. Open the Checkout Overview page<br>2. Click the Cancel button | Checkout is exited and the Checkout Overview page is closed (Checkout Overview is no longer visible) | medium |
| TC-003 |  | Overview displays order summary, totals, payment and shipping information | User logged in as <Customer>, <Cart contains items>, <Payment method saved>, <Shipping address saved> | 1. Open the Checkout Overview page<br>2. Observe the Order Summary list, the Totals section, the Payment information section and the Shipping information section | Order Summary displays the items from <Cart>; Totals section shows 'Item total', 'Tax', and 'Total' labels; Payment information section is visible; Shipping information section is visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Checkout Overview | User is not authenticated | 1. As an unauthenticated user navigate to the Checkout Overview page URL | User is not allowed to view the Checkout Overview: the application redirects to the Login page (or shows a sign-in prompt); the overview content and the Finish button are not displayed and the user cannot complete checkout | high |
| TC-005 |  | Finish cannot complete an order after user exits checkout with Cancel | User has an active checkout session and is on the Checkout Overview | 1. On the Checkout Overview page, click the Cancel button<br>2. After checkout has been exited, attempt to click the Finish button (for example by navigating back to the Overview and clicking Finish) | Checkout has been exited and the Finish action is blocked: the Finish button is not present or is disabled after Cancel; clicking Finish does not navigate to the confirmation page and the order is not completed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) |  | Rapid double-click on Finish (duplicate submission race) | User is signed in, Cart contains at least one item, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Immediately click the Finish button again (before navigation completes) | First click succeeds: order completion occurs and the confirmation page is displayed. Second click is blocked / error shown: no second order completion occurs and only one navigation to the confirmation page happens (user sees a single confirmation page instance). | low |
| TC-007 (interaction_edge) |  | Browser Back after successful Finish then attempt to resubmit | User is signed in, Cart contains at least one item, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Wait until the confirmation page fully loads<br>3. Press the browser Back button<br>4. On the returned Overview page, click the Finish button again | Initial submit succeeds: order completion occurs and the confirmation page is displayed. Using browser Back does not create a second order; the second Finish click is blocked / error shown (no duplicate order is created) and the application prevents a second successful submission. | low |
| TC-008 (interaction_edge) |  | Race between Finish and Cancel clicks | User is signed in, Cart contains at least one item, User is on the Checkout - Overview step | 1. Click the Finish button<br>2. Immediately click the Cancel button (before navigation to confirmation completes) | Finish action succeeds: order completion occurs and the confirmation page is displayed. The subsequent Cancel click is blocked / ignored and does not cancel the completed order; user remains on or is taken to the confirmation page and no cancellation occurs. | low |

---

## Checkout - Confirmation

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Confirmation page shows success message and Back Home button | User logged in as <Customer> | 1. Open the Checkout - Confirmation page<br>2. Observe the page content | Confirmation page displays the success message 'Thank you for your order!' and the 'Back Home' button is visible | medium |
| TC-002 |  | Clicking Back Home redirects to Product Inventory and clears the cart | User logged in as <Customer>, Checkout - Confirmation page is displayed | 1. Click the 'Back Home' button on the Confirmation page<br>2. Wait for navigation to complete | Browser navigates to the Product Inventory page and the cart is cleared (cart displays no items / cart indicator shows empty) | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user attempts to access Confirmation page | User is not authenticated (logged out) | 1. Ensure the user is logged out<br>2. Enter the <confirmation page URL> in the browser address bar and navigate to it | Access is blocked: the user is redirected to the Login page and the Login page is displayed (login form visible). The Confirmation success message is NOT displayed and the cart remains unchanged. | high |
| TC-004 |  | Direct navigation to Confirmation page without completing an order | User is authenticated, No order has been completed in the current session (checkout not finished) | 1. Log in as a valid user<br>2. Navigate directly to the <confirmation page URL> | Access is blocked: the user is redirected to the Product Inventory page (Product Inventory page is displayed). The Confirmation success message is NOT shown and the cart is NOT cleared. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Rapid double-click of Back Home button | User has completed checkout and is on the Confirmation page showing the success message | 1. Click the 'Back Home' button (first click)<br>2. Click the 'Back Home' button again immediately (second click) | A single navigation to Product Inventory succeeds: Product Inventory page is displayed and the cart badge shows zero; no error is shown and the UI does not produce duplicate navigations or duplicate cart-clearing side effects. | medium |
| TC-006 (interaction_edge) |  | Click Back Home then press browser Back | User has completed checkout and is on the Confirmation page showing the success message | 1. Click the 'Back Home' button<br>2. Press the browser Back button | Navigation back to the Confirmation page succeeds (if available in history): the Confirmation page displays the success message; the cart remains cleared (cart badge shows zero) and no additional order or cart entries are created. | medium |
| TC-007 (interaction_edge) |  | Verify cart cleared persists across a new tab after Back Home | User has completed checkout and is on the Confirmation page showing the success message | 1. Click the 'Back Home' button<br>2. Open a new browser tab and navigate to the Product Inventory page | Product Inventory page in the new tab loads and shows the cart badge as zero, indicating the cart-clearing action succeeded and persists across tabs for the same session; original tab also shows cart badge zero. | medium |
| TC-008 (input_edge) |  | Confirmation message rendering with very long product name and special characters | An order has been completed that includes an item whose name contains a very long string with special characters and emoji, and the user is on the Confirmation page | 1. Observe the success message area on the Confirmation page | The success message renders the long text and special characters without breaking page layout: text is either fully visible or properly truncated with a visible UI affordance (e.g., ellipsis/tooltip) indicating truncation; rendering of special characters and emoji succeeds and no visual overflow or layout break is shown. | low |

---

## Logout

Total: **11** (positive: 5, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Click Logout from Inventory page redirects to Login | User logged in as <User> | 1. Open the Inventory page<br>2. Click the Logout button | ends session and redirects to Login page | high |
| TC-002 |  | After logout, attempting to open Inventory page redirects to Login | User logged in as <User> | 1. Open any protected page (e.g., Inventory page)<br>2. Click the Logout button<br>3. Attempt to navigate to the Inventory page | redirects to Login page | medium |
| TC-003 |  | After logout, attempting to open Detail page redirects to Login | User logged in as <User> | 1. Open any protected page (e.g., Inventory page)<br>2. Click the Logout button<br>3. Attempt to navigate to the Detail page | redirects to Login page | medium |
| TC-004 |  | After logout, attempting to open Cart page redirects to Login | User logged in as <User> | 1. Open any protected page (e.g., Inventory page)<br>2. Click the Logout button<br>3. Attempt to navigate to the Cart page | redirects to Login page | medium |
| TC-005 |  | After logout, attempting to open Checkout page redirects to Login | User logged in as <User> | 1. Open any protected page (e.g., Inventory page)<br>2. Click the Logout button<br>3. Attempt to navigate to the Checkout page | redirects to Login page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Unauthenticated user attempts to access a protected page (Inventory) and is blocked | User is not logged in | 1. In a new browser session (no authentication), navigate to <Inventory page URL> | Browser is redirected to the Login page; Inventory page content is not displayed; no authenticated session is created | high |
| TC-007 |  | Unauthenticated user attempts to invoke Logout action (button absent or direct endpoint) and is blocked | User is not logged in | 1. In a new browser session (no authentication), open the application header/ navigation<br>2. Verify whether a 'Logout' control is visible<br>3. Directly navigate to <Logout endpoint> (attempt to invoke logout action by URL) | Step 2: 'Logout' control is not visible in the header when unauthenticated. Step 3: navigating to <Logout endpoint> redirects to the Login page; no session is ended (user remains unauthenticated) and no protected content is shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (state_edge) |  | Rapid / double-click Logout button | User is logged in, User is on a protected page (Inventory_Page or Detail_Page) | 1. Click the Logout button<br>2. Immediately click the Logout button again (second click within <1 second)<br>3. Observe the current page and any visible messages | Logout succeeds: session ends (Authenticated -> Unauthenticated) and the Login page is shown. The second click is ignored (no additional logout actions occur) and no error is shown; protected page content is not visible. | medium |
| TC-009 (interaction_edge) |  | Use browser Back after logout to access protected page | User is logged in, User has previously navigated to a protected page (Inventory_Page) | 1. Click the Logout button<br>2. After the app redirects to the Login page, press the browser Back button once<br>3. Observe the page shown after pressing Back | Navigation back to the protected page is blocked; Login page is shown (protected page content is not displayed). The user remains unauthenticated. | medium |
| TC-010 (interaction_edge) |  | Direct URL / bookmark access to protected page after logout | User is logged in | 1. Click the Logout button<br>2. In the browser address bar, enter the direct URL for a protected page (Inventory_Page) and press Enter<br>3. Observe which page loads | Direct navigation to the protected page is blocked; Login page is shown instead and protected content is not visible. The user remains unauthenticated. | medium |
| TC-011 (state_edge) |  | Open protected page in second tab, logout in first tab, then refresh second tab | User is logged in | 1. In Tab A, navigate to a protected page (Inventory_Page)<br>2. Open the same protected page in Tab B<br>3. In Tab A, click the Logout button<br>4. Switch to Tab B and click the browser Refresh/Reload button<br>5. Observe the page shown in Tab B after refresh | Refresh in Tab B is blocked from showing protected content; the Login page is shown in Tab B and the user remains unauthenticated. The state transition (Authenticated -> Unauthenticated) persists across tabs. | medium |

---

## Reset App State

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Reset with items in cart clears badge and resets add/remove buttons without logging out | User logged in as <User>, Cart contains <one or more items>, At least one product in the UI shows the 'Remove' action state | 1. Open the app page that contains the Reset App State button<br>2. Locate the 'Reset App State' button<br>3. Click the 'Reset App State' button | clears cart and resets in-app state (cart badge and add/remove button states); does not log the user out — the cart badge is no longer visible (or shows zero) and previously 'Remove' product action buttons now show 'Add'; the user's account menu/avatar remains visible indicating the user is still logged in | high |
| TC-002 |  | Reset when cart is already empty leaves UI in default state and user remains logged in | User logged in as <User>, Cart is empty, Product list shows 'Add' action state for items | 1. Open the app page that contains the Reset App State button<br>2. Locate the 'Reset App State' button<br>3. Click the 'Reset App State' button | clears cart and resets in-app state (cart badge and add/remove button states); does not log the user out — the cart badge remains not visible (no change from empty), product action buttons remain in the 'Add' state, and the user's account menu/avatar remains visible indicating the user is still logged in | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Unauthenticated user attempts to invoke Reset App State | User is logged out | 1. Open the application page that normally contains the 'Reset App State' control<br>2. Click the 'Reset App State' button (if visible) or attempt to invoke the reset action | The action is blocked: the app redirects to the Login page (Login form visible) or the 'Reset App State' control is not visible/accessible to unauthenticated users; the app does not perform any reset (cart badge and add/remove button states remain unchanged). | high |
| TC-004 |  | Reset App State must not log the user out (ensure logout side-effect is blocked) | User is logged in, Cart contains at least one item | 1. Sign in as a user<br>2. Add an item to the cart<br>3. Verify the cart badge shows <non-zero cart count><br>4. Click the 'Reset App State' button | The reset action is allowed to run but the undesired logout side-effect is blocked: cart badge becomes 0 and add/remove button states reset, AND the user remains signed in (account/avatar/menu remains visible, there is no redirect to the Login page). | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) |  | Rapid consecutive clicks on Reset App State | User is logged in, Cart contains at least one item (cart badge visible), At least one product's add/remove button is in the 'Remove' state | 1. Click the 'Reset App State' button<br>2. Immediately click the 'Reset App State' button again | First reset succeeds: cart contents list becomes empty and cart badge is cleared (no badge or zero displayed); add/remove buttons return to the 'Add' state. The second click is ignored (no additional state changes, no duplicate side effects, no error shown). The user remains logged in (profile/account icon still shows user and navigating to profile loads account details). | medium |
| TC-006 (interaction_edge) |  | Click Reset App State when cart is already empty | User is logged in, Cart is already empty (no cart badge visible) | 1. Verify cart is empty (no items listed)<br>2. Click the 'Reset App State' button | Reset action succeeds as a no-op: UI remains showing an empty cart and no cart badge; no error or warning is shown; add buttons remain in the default 'Add' state. The user remains logged in (no redirect to login). | low |
| TC-007 (state_edge) |  | Reset App State then navigate to profile to verify session persistence | User is logged in, Cart contains at least one item | 1. Click the 'Reset App State' button<br>2. Click the profile/account icon or 'Profile' link to open the user's profile page | Reset succeeds: cart is cleared and in-app state (cart badge and add/remove buttons) is reset. Navigating to the profile page shows the user's account details and does not require re-login (user remains authenticated). | medium |

---
