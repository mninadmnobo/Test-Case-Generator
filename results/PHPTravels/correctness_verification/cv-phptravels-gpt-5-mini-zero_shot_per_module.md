# Correctness Verification: PHPTravels (gpt-5-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/PHPTravels/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/PHPTravels.md`  
**Total Generated Test Cases:** 410  
**Modules Covered:** Home Page And Search, Registration, Login, Forgot Password, Hotels Search And Listing, Hotel Details And Booking, Flights Search And Booking, Tours Search And Booking, Cars Search And Booking, Visa Services, User Dashboard And Booking Management, Payment Processing, Currency And Language Selection, Search And Filters, Reviews And Ratings, Offers And Deals, Logout

---

## Error Analysis

### A. Precondition Errors

**Total:** 14

- **TC IDs:** Hotels Search TC-021, TC-022 *(B2B Agent Pricing)*; Flights Search TC-020, TC-021 *(Multi-city max legs)*; Tours Search TC-018, TC-019 *(Custom Tour Creation)*; User Dashboard TC-019 to TC-024 *(Sub-user management)*; Payment TC-018, TC-019 *(Wallet funds)*
- *Reasoning:*
  - The zero-shot model aggressively hallucinated advanced travel agency features (B2B portals, custom tour authoring, corporate sub-users, and digital wallets) not present in the B2C functional description.

---

### B. Test Steps Errors

**Total:** 10

- **TC IDs:** Hotel Details TC-015 to TC-019 *(Interactive maps routing)*; Reviews And Ratings TC-016 to TC-020 *(Image uploads in reviews)*
- *Reasoning:*
  - Assumes interactive routing features on hotel maps and photo uploads for reviews, neither of which are defined in the functional specs.

---

### C. Expected Result Errors

**Total:** 6

- **TC IDs:** Cars Search TC-015 to TC-017 *(Insurance add-ons)*; Visa Services TC-018 to TC-020 *(Live chat support triggers)*
- *Reasoning:*
  - Expected results dictate the appearance of complex up-sells (insurance) and automatic live-chat prompts, misinterpreting the specific constraints of the PHPTravels interface.

---

## Unique Incorrect Test Cases

*(Truncated list of 30 unique incorrect TCs covering B2B pricing, Sub-users, Wallet funds, Map routing, Image uploads, Insurance up-sells, and Live chat)*

---

## Success Rate Calculation

- **Total Generated Test Cases:** 410
- **Total Test Cases with Errors:** 30
- **Total Correct Test Cases:** 380

**Overall Success Rate: 380 / 410 (92.68%)**

---

## Thesis Analysis

The GPT-5-mini Zero-Shot Per Module approach generated a massive **410 test cases**, but its lack of iterative self-correction resulted in a significantly lower **92.68% correctness rate**. The model succumbed heavily to "domain drift," hallucinating 30 enterprise/B2B travel features. Ultimately, it generated fewer valid test cases (380) than the Agent approach (390), proving that raw generation volume without agentic grounding is counterproductive in complex domains.
