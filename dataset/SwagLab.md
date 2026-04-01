# SwagLab

## Website URL

<https://www.saucedemo.com/>

## Navigation

Swag Labs is an e-commerce testing application. Users start on the sign-in page (Username, Password, Login). After login, they land on the Product Inventory page with a persistent header containing the hamburger menu (left), "Swag Labs" title (center), and shopping cart icon with an item-count badge (right). The hamburger menu contains: ① All Items, ② About (Sauce Labs website), ③ Logout, and ④ Reset App State. From inventory, users can open Product Detail by clicking a product name/image, add/remove items from the cart, navigate to the cart, and complete checkout through three steps (Information → Overview → Confirmation).

## Functional Description

### 1. Login

The login page contains a Username field, a Password field, and a Login button. The page also lists accepted test usernames (for example: standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user) and the shared password secret_sauce. When the user submits valid credentials, the system authenticates and redirects to the Product Inventory page. If credentials are invalid or required fields are empty, the system shows an error banner (for example: "Epic sadface: Username is required.", "Epic sadface: Password is required.", "Epic sadface: Username and password do not match any user in this service."); locked_out_user shows "Epic sadface: Sorry, this user has been locked out." Login state should remain consistent after refresh, and direct navigation back to the login page while authenticated should resolve to the active session or the home page.

### 2. Product Inventory

After login, the Product Inventory page lists all products with name, description, price, and an "Add to cart" button. A sort dropdown allows sorting by name (A–Z, Z–A) and price (low–high, high–low). Clicking a product name or image opens the Product Detail page. Clicking "Add to cart" adds the item and changes the button to "Remove"; the cart badge count updates accordingly. Clicking "Remove" reverses the action. The page should preserve sort and cart state across refresh, and persona-based rendering issues or performance delays should still allow the core inventory flow to function when possible.

### 3. Product Detail

The Product Detail page shows the selected product’s image, name, description, and price, along with an "Add to cart" / "Remove" button that reflects the current cart state. A "Back to products" button returns to the Product Inventory page. The cart icon remains available to navigate to the Shopping Cart. Cart state should remain synchronized when moving between inventory and detail views, and repeated add/remove actions should not create duplicate items.

### 4. Shopping Cart

The Shopping Cart page lists items added to the cart with quantity (shown as 1), description, and a "Remove" button per item. Users can click "Continue Shopping" to return to Product Inventory or click "Checkout" to begin checkout. Cart contents should persist across navigation and browser refresh, and the cart badge should always reflect the current number of items without duplication.

### 5. Checkout - Information

Checkout starts with a form that collects First Name, Last Name, and Zip/Postal Code. Clicking "Continue" validates required fields and proceeds to the overview step. Clicking "Cancel" returns to the Shopping Cart. Missing required fields display an error banner such as "Error: First Name is required", "Error: Last Name is required", or "Error: Postal Code is required". Partial submissions, unusual names, and browser navigation during checkout should fail gracefully without losing the cart.

### 6. Checkout - Overview

The overview step shows an order summary of cart items and a totals section (Item total, Tax, Total), along with payment and shipping information. Clicking "Finish" completes the order and navigates to the confirmation page. Clicking "Cancel" exits checkout. Totals should remain accurate for tax and price calculations, and repeated finish actions should not create duplicate orders.

### 7. Checkout - Confirmation

The confirmation page displays a success message (for example: "Thank you for your order!") and provides a "Back Home" button that returns to Product Inventory and clears the cart. The confirmed order should leave the cart empty and the session state consistent for the next browsing flow.

### 8. Navigation Menu

The hamburger menu opens a side panel with navigation actions: All Items, About, Logout, and Reset App State. The menu can be closed using the X button. These actions should continue to work correctly after browser navigation and refresh.

### 9. Logout

Logout ends the session and returns the user to the login page. After logout, protected pages (inventory, detail, cart, checkout) are not accessible without logging in again. Logout should clear any user-specific cart state and prevent access through the browser back button or direct URL entry.

### 10. Reset App State

Reset App State clears the cart and resets in-app state (for example, cart badge and add/remove button states) without logging the user out. The action should preserve the authenticated session while restoring the inventory and cart UI to a clean state.
