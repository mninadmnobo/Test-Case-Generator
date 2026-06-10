# Correctness Verification: SwagLab (gpt-5-mini — Few-Shot Per Module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/SwagLab/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/SwagLab.md`  
**Total Generated Test Cases:** 82  
**Modules Covered:** Login (12), Product Inventory (12), Product Detail (10), Shopping Cart (8), Checkout - Information (8), Checkout - Overview (7), Checkout - Confirmation (7), Logout (8), Reset App State (10)

---

## Error Analysis

### A. Precondition Errors

**Total:** 3

- **TC IDs:** Product Detail TC-030 *(backend product detail API simulated to return 500)*, Product Detail TC-031 *(browser set to offline mode)*, Logout TC-070 *(authenticated action attempted with stale session token)*
- *Reasoning:*
  - **Product Detail TC-030 & TC-031:** Same infrastructure mock concerns as seen in the zero-shot configuration. The preconditions require simulating server failures or offline network conditions that are not described in the SwagLab functional spec. While the tests are valid from an engineering standpoint, expected results hallucinate specific error messages not grounded in the spec.
  - **Logout TC-070:** Precondition says "Tester has captured the previous session cookie or token." This is a security/penetration-testing precondition requiring test infrastructure outside the application's scope. SwagLab's functional spec describes session termination from the UI perspective only, not API-level stale token behavior.

---

### B. Test Steps Errors

**Total:** 1

- **TC IDs:** Logout TC-070 *(submit POST request to checkout endpoint with old session token)*
- *Reasoning:*
  - **Logout TC-070:** Steps say "Using a REST client or browser devtools, send an API request that requires authentication (for example POST /cart/add) including the old session cookie/token." This is an API-level penetration test step, not a functional UI test step. SwagLab's functional description describes only the UI-level user interactions. This test requires direct API access not described in the functional spec.

---

### C. Expected Result Errors

**Total:** 3

- **TC IDs:** Product Detail TC-030 *(specific error: 'Failed to load product details')*, Product Detail TC-031 *(specific offline error message)*, Logout TC-070 *(server returns 401 response)*
- *Reasoning:*
  - **Product Detail TC-030:** Expected result says "An informative error message is displayed (e.g., 'Failed to load product details')." SwagLab's functional description does not specify error messages for server failures — this is a hallucinated error string.
  - **Product Detail TC-031:** Expected result says "User is notified of network/offline error (e.g., 'Unable to update cart while offline')." Again, SwagLab's spec describes no offline behavior or specific error messages.
  - **Logout TC-070:** Expected result says "Server rejects the request (401/302 to login or equivalent)." This describes HTTP response codes — a backend behavior not described in the functional specification. The spec only describes UI-level outcomes (redirect to login page).

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| TC-030 | Product Detail | Precondition + Expected Result |
| TC-031 | Product Detail | Precondition + Expected Result |
| TC-070 | Logout | Precondition + Steps + Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 82
- **Total Test Cases with Errors:** 3 *(each counted once, despite some having multiple error types)*
- **Total Correct Test Cases:** 79

**Overall Success Rate: 79 / 82 (96.34%)**

---

## Thesis Analysis

The GPT-5-mini Few-Shot Per Module approach achieved a **96.34% correctness rate** across 82 test cases — the second highest correctness score among all SwagLab configurations, and the highest count among the few-shot configurations.

All three errors in this configuration follow the same pattern: the model generates **infrastructure/API-level tests** (server errors, offline modes, stale token attacks) that are valid software engineering tests but exceed the scope of the functional specification. Unlike GPT-4o-mini's few-shot errors (which hallucinated non-existent features), GPT-5-mini's errors are more sophisticated — they test real failure scenarios but assume specific error messages and API behaviors that the functional spec does not document.

This reflects the "mimic" behavior of few-shot prompting combined with GPT-5-mini's superior reasoning: the model faithfully mimics the example structure but its stronger capabilities allow it to extrapolate into security and infrastructure testing territory. The few-shot constraint did not significantly limit GPT-5-mini's output volume (82 TCs vs 105 in zero-shot), unlike GPT-4o-mini where few-shot caused a drastic reduction from 54 to 38 TCs. This confirms that GPT-5-mini is less susceptible to the "tunnel vision" effect of few-shot prompting.
