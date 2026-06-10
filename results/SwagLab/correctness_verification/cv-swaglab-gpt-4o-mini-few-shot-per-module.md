# Correctness Verification: SwagLab (gpt-4o-mini — Few-Shot Per Module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/SwagLab/gpt-4o-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/SwagLab.md`  
**Total Generated Test Cases:** 38  
**Modules Covered:** Login (7), Product Inventory (4), Product Detail (4), Shopping Cart (5), Checkout - Information (6), Checkout - Overview (3), Checkout - Confirmation (3), Logout (3), Reset App State (3)

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Product Inventory TC-009 *(add to cart while not logged in, from Inventory page)*, Product Detail TC-014 *(add to cart while not logged in, from Detail page)*
- *Reasoning:*
  - **Product Inventory TC-009 & Product Detail TC-014:** Both preconditions state "User is not logged in" while the user is on the Product Inventory or Product Detail page respectively. In SwagLab, unauthenticated users cannot access the Product Inventory or Product Detail pages at all — they are redirected to the Login page. The precondition of being on an inventory/detail page while not authenticated is impossible per the functional description.

---

### B. Test Steps Errors

**Total:** 2

- **TC IDs:** Product Inventory TC-009 *(click Add to Cart while not logged in on Inventory page)*, Product Detail TC-014 *(click Add to Cart while not logged in on Detail page)*
- *Reasoning:*
  - **Product Inventory TC-009 & Product Detail TC-014:** Since unauthenticated users cannot reach these pages, the steps to click "Add to cart" on those pages while logged out are logically unreachable. The steps presuppose an impossible precondition.

---

### C. Expected Result Errors

**Total:** 3

- **TC IDs:** Product Inventory TC-009 *(must log in to add)*, Product Detail TC-014 *(prompted to log in)*, Shopping Cart TC-019 *(checkout error: cart is empty)*
- *Reasoning:*
  - **Product Inventory TC-009:** Expected result says "An error message is displayed indicating that the user must log in to add products to the cart." In SwagLab, the redirect to login happens before the user ever sees the inventory, not as a response to clicking Add to Cart.
  - **Product Detail TC-014:** Expected result says "User is prompted to log in before adding the product to the cart; remains on the Product Detail page." Again, the user would have been redirected to login long before reaching the product detail page. There is no "prompted to log in" experience on the detail page itself.
  - **Shopping Cart TC-019:** Expected result says "An error message is displayed indicating that the cart is empty; the user remains on the Shopping Cart page." SwagLab's functional spec does not define this specific behaviour — the Checkout button behaviour when cart is empty is unspecified. The stated expected result assumes behaviour not grounded in the spec.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| TC-009 | Product Inventory | Precondition + Steps + Expected Result |
| TC-014 | Product Detail | Precondition + Steps + Expected Result |
| TC-019 | Shopping Cart | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 38
- **Total Test Cases with Errors:** 3 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 35

**Overall Success Rate: 35 / 38 (92.11%)**

---

## Thesis Analysis

The GPT-4o-mini Few-Shot Per Module approach achieved the **highest correctness rate of 92.11%** among all GPT-4o-mini configurations. This is consistent with the known "tunnel vision" effect of few-shot prompting described in the thesis: by closely mimicking the structure of the provided examples, the model generated fewer test cases overall (only 38, the lowest count across all configurations) and stayed closer to well-defined, simple scenarios — reducing the surface area for hallucination.

However, this comes at the cost of **scope reduction**: the model missed many valid edge cases and coverage scenarios. The few errors that did appear share a common theme of **misunderstanding the authentication gate** — incorrectly assuming that unauthenticated users could be on protected pages. This is a fundamental misunderstanding of the application's access control model. The low count and constrained structure of few-shot outputs explain both the high correctness rate and the low coverage scores observed for this configuration.
