# Correctness Verification: PHPTravels (gpt-5-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/PHPTravels/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/PHPTravels.md`  
**Total Generated Test Cases:** 289  
**Modules Covered:** Home Page And Search, Registration, Login, Forgot Password, Hotels Search And Listing, Hotel Details And Booking, Flights Search And Booking, Tours Search And Booking, Cars Search And Booking, Visa Services, User Dashboard And Booking Management, Payment Processing, Currency And Language Selection, Search And Filters, Reviews And Ratings, Offers And Deals, Logout

---

## Error Analysis

### A. Precondition Errors

**Total:** 2

- **TC IDs:** Registration TC-011 *(Social Login)*, Login TC-012 *(Social Login)*
- *Reasoning:*
  - Preconditions require the user to have an active Google/Facebook account to test SSO integration. SSO is not part of the documented PHPTravels auth flow.

---

### B. Test Steps Errors

**Total:** 2

- **TC IDs:** Search And Filters TC-010, TC-011 *(Sort by Distance)*
- *Reasoning:*
  - Instructs the user to select "Sort by Distance from Airport". The spec details price and star-rating filters, but not point-of-interest distance sorting.

---

### C. Expected Result Errors

**Total:** 2

- **TC IDs:** Payment Processing TC-010 *(Split Payments)*, Visa Services TC-012 *(Auto-approval)*
- *Reasoning:*
  - **Payment TC-010:** Asserts users can pay partially with a card and partially with points.
  - **Visa TC-012:** Asserts immediate "Auto-approved" status for specific nationalities, violating the stated manual review workflow.

---

## Unique Incorrect Test Cases

Unique TCs with at least one error (deduplicated):

| TC ID | Module | Error Types |
|---|---|---|
| Registration TC-011 | Registration | Precondition |
| Login TC-012 | Login | Precondition |
| Search And Filters TC-010 | Search And Filters | Test Steps |
| Search And Filters TC-011 | Search And Filters | Test Steps |
| Payment Processing TC-010 | Payment Processing | Expected Result |
| Visa Services TC-012 | Visa Services | Expected Result |

---

## Success Rate Calculation

- **Total Generated Test Cases:** 289
- **Total Test Cases with Errors:** 6
- **Total Correct Test Cases:** 283

**Overall Success Rate: 283 / 289 (97.92%)**

---

## Thesis Analysis

The GPT-5-mini Few-Shot Per Module approach achieved a strong **97.92% correctness rate** across 289 generated cases. While highly accurate, it lacked the creative depth to match the scale of the Agent approach (which generated 100+ more correct tests), confirming that static prompting limits coverage scope.
