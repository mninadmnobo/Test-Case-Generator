# Correctness Verification: SwagLab (gpt-5-mini — Zero-Shot Per Module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/SwagLab/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/SwagLab.md`  
**Total Generated Test Cases:** 105  
**Modules Covered:** Login (16), Product Inventory (12), Product Detail (14), Shopping Cart (11), Checkout - Information (10), Checkout - Overview (12), Checkout - Confirmation (10), Logout (10), Reset App State (10)

---

## Error Analysis

### A. Precondition Errors

**Total:** 3

- **TC IDs:** Product Detail TC-035 *(backend API mocked to return HTTP 500)*, Product Detail TC-037 *(device/network set to offline mode)*, Shopping Cart TC-049 *(server-side delete API returning error via stub)*
- *Reasoning:*
  - **Product Detail TC-035:** Precondition states "Backend API for adding to cart is mocked to return HTTP 500." This is a test infrastructure/mock setup concern, not a valid application precondition describable in terms of the SwagLab functional spec. Functional correctness verification evaluates whether the test case is logically valid for the *real* application described — not mock infrastructure tests. However, since this is more of a scope concern than a hallucination of a non-existent feature, this is flagged as a precondition concern rather than a hard error.
  - **Product Detail TC-037:** Precondition states "Device/network is set to offline mode." Offline mode testing is valid in general, but SwagLab's functional description does not mention offline behavior. The expected result in this TC (a specific "offline notification" message) is grounded in a hallucinated behavior since no such response is described in the spec.
  - **Shopping Cart TC-049:** Precondition states "Server-side delete API is returning an error (simulated by test stub or network condition)." Same infrastructure mock concern — valid as an engineering test but the expected result assumes a specific error message not grounded in the SwagLab spec.

---

### B. Test Steps Errors

**Total:** 2

- **TC IDs:** Checkout - Overview TC-067 *(payment information is missing or invalid on Overview)*, Checkout - Overview TC-068 *(shipping information missing on Overview)*
- *Reasoning:*
  - **Checkout - Overview TC-067 & TC-068:** Steps describe blocking the Finish action when "Payment information is missing or invalid" and "Shipping information is missing." The SwagLab Checkout Overview page does not collect payment or shipping information — it only *displays* a pre-populated order summary. There is no payment input form on this page that can be "missing." The steps reference a non-existent form interaction.

---

### C. Expected Result Errors

**Total:** 5

- **TC IDs:** Product Detail TC-035 *(specific error message on 500)*, Product Detail TC-037 *(offline notification message)*, Shopping Cart TC-049 *(specific error on delete failure)*, Checkout - Overview TC-067 *(blocked by missing payment)*, Checkout - Overview TC-068 *(blocked by missing shipping)*
- *Reasoning:*
  - **Product Detail TC-035:** Expected result says "An error message is displayed (e.g., 'Unable to add to cart')." SwagLab's functional spec defines no such error message for API failures. This behavior is assumed/hallucinated.
  - **Product Detail TC-037:** Expected result says "User is notified of network/offline error (e.g., 'No internet connection')." SwagLab's spec does not describe offline behavior or error messaging for network failures.
  - **Shopping Cart TC-049:** Expected result says "An error message is displayed (e.g., 'Unable to remove item, please try again')." SwagLab's spec does not define this error message.
  - **Checkout - Overview TC-067 & TC-068:** Expected results describe blocking order completion due to missing payment/shipping data that the user can enter on that page. Since SwagLab's Overview step is a read-only summary (not a form), these expected outcomes are based on a misunderstanding of the checkout flow.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| TC-035 | Product Detail | Precondition + Expected Result |
| TC-037 | Product Detail | Precondition + Expected Result |
| TC-049 | Shopping Cart | Precondition + Expected Result |
| TC-067 | Checkout - Overview | Steps + Expected Result |
| TC-068 | Checkout - Overview | Steps + Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 105
- **Total Test Cases with Errors:** 5 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 100

**Overall Success Rate: 100 / 105 (95.24%)**

---

## Thesis Analysis

The GPT-5-mini Zero-Shot Per Module approach achieved a **95.24% correctness rate** while generating the highest total volume of all configurations (105 test cases). This is remarkable for a zero-shot approach — no examples were given, yet the model produced a logically sound, diverse test suite with only 5 errors across 9 modules.

The errors cluster into two themes:
1. **Server/network failure simulation tests** (TC-035, TC-037, TC-049): GPT-5-mini generated valid engineering-level failure tests but projected specific error message behaviors not documented in the SwagLab spec. These are not "hallucinations of features" but rather "hallucinations of undocumented behavior" for real failure scenarios.
2. **Checkout Overview form misunderstanding** (TC-067, TC-068): The model incorrectly treats the Overview page as a form with editable payment/shipping fields, mirroring the error seen in other configurations. This is the most common cross-configuration failure pattern for SwagLab.

The 95% correctness at 105 test cases demonstrates that GPT-5-mini's base intelligence allows it to generate high-quality tests even without agent scaffolding, validating the thesis's finding that "brains over tactics" — raw model capability matters most.
