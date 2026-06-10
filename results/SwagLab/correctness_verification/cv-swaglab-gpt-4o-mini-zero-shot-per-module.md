# Correctness Verification: SwagLab (gpt-4o-mini — Zero-Shot Per Module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/SwagLab/gpt-4o-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/SwagLab.md`  
**Total Generated Test Cases:** 54  
**Modules Covered:** Login (8), Product Inventory (8), Product Detail (6), Shopping Cart (7), Checkout - Information (7), Checkout - Overview (5), Checkout - Confirmation (5), Logout (4), Reset App State (4)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Product Detail TC-018 *(product is out of stock)*, Product Inventory TC-015 *(maximum cart limit is known)*
- *Reasoning:*
  - **Product Detail TC-018:** The precondition states "Product is out of stock." SwagLab's functional description does not mention any out-of-stock state. All products listed are always available for adding to cart. This is a hallucinated constraint.
  - **Product Inventory TC-015:** The precondition states "Maximum cart limit is known." SwagLab has no defined maximum cart capacity in the functional description. This assumes a constraint that does not exist in the system.

---

### B. Test Steps Errors

**Total:** 4

- **TC IDs:** Product Detail TC-018 *(add out-of-stock product)*, Product Detail TC-022 *(view empty fields: no image or name)*, Shopping Cart TC-026 *(remove non-existent item from empty cart)*, Reset App State TC-051 & TC-052 *(navigate to app settings)*
- *Reasoning:*
  - **Product Detail TC-018:** Steps say to click Add to Cart for an out-of-stock product — this cart state does not exist in SwagLab.
  - **Product Detail TC-022:** Steps reference a product with "no image or name" and expect "placeholder text or default image." SwagLab's functional description specifies all products have image, name, description, and price. A product with missing fields is a hallucinated scenario not grounded in the spec.
  - **Shopping Cart TC-026:** The step says "Attempt to click the 'Remove' button for a non-existent item" while the cart is empty. In SwagLab, if the cart is empty, there are no Remove buttons rendered on the Shopping Cart page. The scenario describes clicking a button that cannot exist.
  - **Reset App State TC-051 & TC-052:** Steps reference navigating to "app settings" — there is no "app settings" page in SwagLab. Reset App State is accessed via the hamburger menu, not a separate settings section. This is a hallucinated navigation step.

---

### C. Expected Result Errors

**Total:** 4

- **TC IDs:** Product Detail TC-018 *(error: product out of stock)*, Product Inventory TC-011 *(error when clicking Remove with no item in cart)*, Shopping Cart TC-026 *(error: no items to remove)*, Checkout - Overview TC-040 *(error: cart is empty)*
- *Reasoning:*
  - **Product Detail TC-018:** Expected result says "An error message is displayed indicating the product is out of stock." SwagLab does not have out-of-stock states or such error messages.
  - **Product Inventory TC-011:** Expected result says "An error message is displayed indicating that there are no products to remove." In SwagLab, if a product is not in the cart, the Remove button simply doesn't appear — no error message is generated.
  - **Shopping Cart TC-026:** Expected result says "An error message is displayed indicating that there are no items to remove." Same issue — SwagLab doesn't display such an error; the Remove button simply isn't present for empty carts.
  - **Checkout - Overview TC-040:** Expected result says "Error message is displayed indicating that the cart is empty." If you somehow reach the Overview with an empty cart, SwagLab doesn't show a specific error — there is no such defined behavior in the functional spec.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| TC-011 | Product Inventory | Expected Result |
| TC-015 | Product Inventory | Precondition |
| TC-018 | Product Detail | Precondition + Steps + Expected Result |
| TC-022 | Product Detail | Steps |
| TC-026 | Shopping Cart | Steps + Expected Result |
| TC-040 | Checkout - Overview | Expected Result |
| TC-051 | Reset App State | Steps |
| TC-052 | Reset App State | Steps |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 54
- **Total Test Cases with Errors:** 8 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 46

**Overall Success Rate: 46 / 54 (85.19%)**

---

## Thesis Analysis

The GPT-4o-mini Zero-Shot Per Module approach achieved an **85.19% correctness rate** across 54 generated test cases. The errors reveal a consistent pattern of the model injecting **typical e-commerce assumptions** (out-of-stock states, maximum cart limits, dedicated settings pages, "click Remove on empty cart" scenarios) that are not grounded in SwagLab's explicitly simple functional description.

Notably, two entire error clusters revolve around **non-existent system states** (out-of-stock, cart limits) and **non-existent UI flows** (app settings). Without an agent's iterative self-correction, the zero-shot model relies entirely on its training distribution — which often includes richer e-commerce systems. The result is a slightly higher error rate than the agent approach (85% vs 88%), confirming that the agent's critic loop helps catch some of these hallucinations during generation.
