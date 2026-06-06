# PHPTravels - GPT-4o-Mini Agent Test Case Generation Report

**Target application:** PHPTravels
**Ground Truth Test Cases:** 347
**Generated Test Cases:** 322
**Model:** `openai/gpt-4o-mini`
**Approach:** Agent

---

## Coverage Definition
- **Missing Coverage:** Ground truth test cases that were not generated.
- **Partial Coverage:** Test cases that partially cover the ground truth logic but miss critical details (e.g., negative scenarios or specific edge cases).
- **Extra Coverage:** Generated test cases that were not explicitly in the ground truth but represent valid scenarios.

---

## Executive Summary
| Module | Ground Truth | Generated | Coverage | Missing | Extra |
|---|---|---|---|---|---|
| 1. Home Page And Search | 25 | 26 | ⚠️ Partial | 10 | 11 |
| 2. Registration | 24 | 17 | ⚠️ Partial | 11 | 4 |
| 3. Login | 22 | 12 | ⚠️ Partial | 9 | 0 |
| 4. Forgot Password | 19 | 16 | ✅ Good | 4 | 1 |
| 5. Hotels Search And Listing | 23 | 14 | ⚠️ Partial | 7 | 0 |
| 6. Hotel Details And Booking | 20 | 15 | ⚠️ Partial | 6 | 1 |
| 7. Flights Search And Booking | 23 | 28 | ✅ Good | 2 | 7 |
| 8. Tours Search And Booking | 20 | 28 | ✅ Good | 3 | 11 |
| 9. Cars Search And Booking | 21 | 26 | ✅ Good | 2 | 7 |
| 10. Visa Services | 20 | 20 | ⚠️ Partial | 4 | 4 |
| 11. User Dashboard And Booking Management | 23 | 28 | ✅ Good | 1 | 6 |
| 12. Payment Processing | 25 | 19 | ⚠️ Partial | 8 | 2 |
| 13. Currency And Language Selection | 17 | 14 | ⚠️ Partial | 7 | 4 |
| 14. Search And Filters | 19 | 24 | ✅ Good | 3 | 8 |
| 15. Reviews And Ratings | 19 | 16 | ⚠️ Partial | 4 | 1 |
| 16. Offers And Deals | 18 | 10 | ⚠️ Partial | 6 | 0 |
| 17. Logout | 9 | 5 | ✅ Good | 2 | 0 |
| **Total** | **347** | **322** | **7 Good, 10 Partial** | **89** | **67** |

---

## Module-by-Module Analysis

### 1. Home Page And Search
**Ground Truth Tests:** 25 | **Generated Tests:** 26 | **Coverage:** ⚠️ Partial

- Valid searches across products (TC-001, TC-002, TC-003, TC-004 ≈ HOME-002, HOME-003, HOME-004, HOME-005) ✅
- Missing/Invalid parameters (TC-005 to TC-020 ≈ HOME-007, HOME-008) ✅
- Temporal bound checks (TC-021, TC-022, TC-023, TC-024 ≈ HOME-009, HOME-010, HOME-011) ✅
- String limitations (TC-025, TC-026 ≈ HOME-016, HOME-019) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOME-001 | Home page navigation elements | Skipped top-level nav assertions. |
| HOME-006 | Featured content sections displayed | Skipped promotional modules. |
| HOME-012 | Verify footer links | Skipped static links. |
| HOME-013 | Verify social media links | Skipped social links. |
| HOME-014 | App download links | Skipped external download links. |
| HOME-020 | Tab switching UI update | Missed UI control testing. |
| HOME-021 | Concurrent search submission | Missed concurrency check. |
| HOME-022 | Search with XSS payload | Missed security logic. |
| HOME-023 | Network timeout | Missed negative network logic. |
| HOME-025 | Rapid double-click on search | Missed UI debouncing. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Deconstructed missing-field checks into an excessive amount of granular individual field tests (TC-005 to TC-020).

#### 🧠 Business Logic Comparison
**Core Logic:** Comprehensive search initiation validating required fields, structural UI components, and boundary limits.
- **[Captured]** Granular individual required field checks across all tabs.
- **[Captured]** Temporal logic bounds.
- **[Missed]** Static non-interactive components, security boundaries, UI tabs validation.
- **[Extra]** Excessive granular empty field checking.

---

### 2. Registration
**Ground Truth Tests:** 24 | **Generated Tests:** 17 | **Coverage:** ⚠️ Partial

- Valid registrations (TC-001 ≈ REG-002) ✅
- Missing parameters (TC-002 to TC-008 ≈ REG-004, REG-008) ✅
- Invalid formats (TC-009, TC-011 ≈ REG-005, REG-016) ✅
- Mismatch limits (TC-010, TC-014, TC-015 ≈ REG-006) ✅
- Extreme boundaries (TC-012, TC-013, TC-016, TC-017 ≈ REG-017, REG-018, REG-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REG-001 | Registration page elements displayed | Skipped basic UI layout. |
| REG-003 | Country code selector works | Skipped interactive modal. |
| REG-012 | Newsletter opt-in | Skipped optional element. |
| REG-013 | Password visibility toggle | Skipped local browser toggle. |
| REG-014 | Password without numbers | Missed specific complexity. |
| REG-015 | Password without special char | Missed specific complexity. |
| REG-018 | Long password | Tested long names, missed password size. |
| REG-019 | Registration timeout | Missed session bound. |
| REG-022 | SQL injection | Missed security check. |
| REG-023 | Rapid resubmission | Missed debouncing. |
| REG-024 | Special characters password match | Missed encoding bounds on password fields. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Checking explicit format boundaries exactly on the validation threshold line (TC-012, TC-013).

#### 🧠 Business Logic Comparison
**Core Logic:** Account creation enforcing strict format validation, policy acceptance, and field boundaries.
- **[Captured]** Length bounds and specific edge validations.
- **[Captured]** Exhaustive singular-field empty checks.
- **[Missed]** Password complexity bounds, optional fields, security integrations.
- **[Extra]** Edge-adjacent formatting tests.

---

### 3. Login
**Ground Truth Tests:** 22 | **Generated Tests:** 12 | **Coverage:** ⚠️ Partial

- Login validation (TC-001 ≈ LOGIN-001) ✅
- Negative testing limits (TC-002, TC-003, TC-004, TC-007, TC-008, TC-009 ≈ LOGIN-004, LOGIN-005) ✅
- Formats (TC-005, TC-006 ≈ LOGIN-014) ✅
- Boundary checks (TC-010, TC-011, TC-012 ≈ LOGIN-015, LOGIN-020, LOGIN-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGIN-002 | Remember Me check | Skipped checkbox. |
| LOGIN-009 | Social Login - Google | Missed external hooks. |
| LOGIN-010 | Social Login - Facebook | Missed external hooks. |
| LOGIN-011 | Password masking | Skipped native browser input typing masks. |
| LOGIN-012 | SQL injection attempt | Missed database security check. |
| LOGIN-013 | XSS attempt | Missed rendering security check. |
| LOGIN-017 | Concurrent login | Missed simultaneous session boundaries. |
| LOGIN-018 | Failed login triggers CAPTCHA | Tested rapid failure (TC-012) but missed asserting CAPTCHA. |
| LOGIN-022 | Back button after login | Missed browser history boundaries. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure session initiation with alternate auth methods, strict invalid handling, and explicit security boundaries.
- **[Captured]** Form limits, empty checks, string boundaries.
- **[Missed]** Social logins, Remember me, CAPTCHA rendering, injection vectors.
- **[Extra]** None.

---

### 4. Forgot Password
**Ground Truth Tests:** 19 | **Generated Tests:** 16 | **Coverage:** ✅ Good

- Request flows (TC-001, TC-002 ≈ FP-001, FP-002) ✅
- Invalid/Empty inputs (TC-003, TC-004, TC-005, TC-011, TC-012 ≈ FP-003, FP-004, FP-009, FP-010) ✅
- New password boundaries (TC-006, TC-007, TC-008, TC-013, TC-014 ≈ FP-005, FP-019) ✅
- Token invalidation (TC-009, TC-010 ≈ FP-006, FP-015) ✅
- Whitespace/characters (TC-015, TC-016 ≈ FP-013, FP-014) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FP-007 | Return to login link | Missed link test. |
| FP-008 | Resend link | Missed resend logic. |
| FP-011 | SQL injection on forgot password | Missed injection check. |
| FP-012 | Rate limiting reset requests | Missed abuse limitation logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Testing formatting boundary confirmation rules heavily.

#### 🧠 Business Logic Comparison
**Core Logic:** Password recovery lifecycle handling valid/invalid emails, reset link expiration, mismatch validation, and explicit security bounds.
- **[Captured]** Token invalidity bounds, whitespace limits, format mismatches.
- **[Missed]** Rate limiting, resend functionality, database injection.
- **[Extra]** None.

---

### 5. Hotels Search And Listing
**Ground Truth Tests:** 23 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Standard checks and interactions (TC-001, TC-002 ≈ HOTEL-001, HOTEL-002) ✅
- Blank fields logic (TC-003 to TC-008 ≈ HOTEL-007, HOTEL-015) ✅
- Temporal limits (TC-009, TC-010 ≈ HOTEL-014, HOTEL-018) ✅
- Boundaries (TC-011, TC-012, TC-013, TC-014 ≈ HOTEL-016, HOTEL-019, HOTEL-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOTEL-003 | Sort hotels by Price | Missed Sorting logic. |
| HOTEL-004 | Filter hotels by Price | Missed Filtering logic entirely in this module. |
| HOTEL-011 | Map view | Missed map interaction. |
| HOTEL-012 | Change currency on listing | Did not test currency toggle on listing. |
| HOTEL-020 | Rapid toggle filters | Missed debouncing logic. |
| HOTEL-022 | Remove disabled filter | Missed disabled state checking. |
| HOTEL-023 | Price slider handles crossed | Missed slider bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Dynamic property catalog with multi-dimensional filtering, temporal validation, and UI interaction states.
- **[Captured]** Zero bounds testing on specific inputs.
- **[Missed]** All Filtering, Sorting, and advanced View (Map) testing was omitted from this module entirely.
- **[Extra]** None.

---

### 6. Hotel Details And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 15 | **Coverage:** ⚠️ Partial

- Execution (TC-001 ≈ HBOOK-001, HBOOK-003) ✅
- Authenticated checks (TC-002 ≈ HBOOK-016) ✅
- Empty restrictions (TC-003 to TC-008 ≈ HBOOK-005, HBOOK-017) ✅
- Temporal boundaries (TC-009, TC-010 ≈ HBOOK-011) ✅
- Numeric boundaries (TC-011, TC-012 ≈ HBOOK-012, HBOOK-013) ✅
- Format characters (TC-013, TC-014, TC-015 ≈ HBOOK-007, HBOOK-018, HBOOK-019) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HBOOK-008 | View photo gallery | Missed gallery interaction. |
| HBOOK-009 | View map location | Missed map interaction. |
| HBOOK-010 | Add to wishlist | Missed wishlist functionality. |
| HBOOK-014 | Max stay limit | Missed long-stay boundaries. |
| HBOOK-017 | Submit without room | Mapped via TC-003/004 but explicitly missed room selection state. |
| HBOOK-019 | Special characters in request | Tested names, missed special requests constraint block. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Explicit whitespace checks on Email fields.

#### 🧠 Business Logic Comparison
**Core Logic:** Deep property data presentation and booking progression with strict room availability and passenger limits.
- **[Captured]** Form progression validation and strict constraints on stays.
- **[Missed]** Visual/interaction elements (Maps, Galleries, Wishlists).
- **[Extra]** None.

---

### 7. Flights Search And Booking
**Ground Truth Tests:** 23 | **Generated Tests:** 28 (Combined) | **Coverage:** ✅ Good

- Routing and discovery (Listing TC-001, TC-002, TC-008, TC-009 ≈ FLIGHT-001, FLIGHT-003, FLIGHT-005, FLIGHT-009) ✅
- Empty field arrays (Listing TC-003 to TC-005 ≈ FLIGHT-014) ✅
- Invalid parameters (Listing TC-006, TC-007, TC-010 to TC-014 ≈ FLIGHT-015, FLIGHT-016, FLIGHT-017, FLIGHT-019, FLIGHT-021) ✅
- Booking workflow (Booking TC-001, TC-010, TC-011 ≈ FLIGHT-004) ✅
- Missing passenger limits (Booking TC-002 to TC-009 ≈ FLIGHT-006, FLIGHT-008) ✅
- Formatting bounds (Booking TC-012 to TC-014 ≈ FLIGHT-007, FLIGHT-022) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FLIGHT-011 | Stops filter | Missed stops UI tool. |
| FLIGHT-012 | Airline filter | Missed airline UI tool. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Detailed sequential testing of exactly reaching maximum passengers, then exceeding it.
- Explicit rapid double-click UI checks on 'Continue'.

#### 🧠 Business Logic Comparison
**Core Logic:** Complex flight routing (Round-trip, One-way, Multi-city) with extensive filtering, passenger detail validation, and strict boundary logic.
- **[Captured]** Deep string limits, temporal logic bounds, and form debouncing tests.
- **[Missed]** Filtering UI constraints natively in the module.
- **[Extra]** Passenger boundary increment logic testing.

---

### 8. Tours Search And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 28 (Combined) | **Coverage:** ✅ Good

- Search constraints (Search TC-001, TC-002, TC-014 ≈ TOUR-001) ✅
- Missing parameters check (Search TC-003 to TC-011 ≈ TOUR-018) ✅
- Boundaries (Search TC-012, TC-013 ≈ TOUR-019) ✅
- Booking logic (Booking TC-001, TC-002 ≈ TOUR-004, TOUR-017) ✅
- Empty constraints (Booking TC-003, TC-006, TC-007 ≈ TOUR-005) ✅
- Format logic (Booking TC-004, TC-005, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014 ≈ TOUR-006, TOUR-013, TOUR-014, TOUR-020) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| TOUR-002 | Filters logic | Missed filtering. |
| TOUR-008 | Gallery logic | Missed visual logic. |
| TOUR-009 | Map logic | Missed map link. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Intensive testing of minimal required boundaries across every individual input parameter.
- Rapid re-submission debouncing tests.

#### 🧠 Business Logic Comparison
**Core Logic:** Tour package presentation with itinerary details, date-based availability checking, and dynamic price recalculation.
- **[Captured]** Extensive constraint checking on form formats, inputs, dates, and names.
- **[Missed]** Visual hooks (Galleries, Maps) and filters.
- **[Extra]** Debouncing logic and granular minimum input tests.

---

### 9. Cars Search And Booking
**Ground Truth Tests:** 21 | **Generated Tests:** 26 (Combined) | **Coverage:** ✅ Good

- Search validation limits (Search TC-001, TC-002, TC-003 to TC-008 ≈ CAR-001, CAR-002, CAR-008) ✅
- Time constraints (Search TC-009, TC-010, TC-011, TC-012 ≈ CAR-012, CAR-014, CAR-015, CAR-016, CAR-017) ✅
- Booking pathways (Booking TC-001, TC-008, TC-014 ≈ CAR-003, CAR-004, CAR-020) ✅
- Fields and logic (Booking TC-002 to TC-007, TC-009 to TC-013 ≈ CAR-005, CAR-006, CAR-007, CAR-018, CAR-019) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| CAR-010 | Filter logic | Missed checking car filters natively. |
| CAR-013 | Wallet invalid payment | Missed wallet integrations. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Checking explicit "one unit below minimum age" bounds.
- UI debouncing checks across multiple phases of checkout.

#### 🧠 Business Logic Comparison
**Core Logic:** Vehicle rental catalog with add-on options (insurance), explicit pick-up/drop-off validation, and strict age-based policy enforcement.
- **[Captured]** Deep age policy bounds mapping, time constraint validation.
- **[Missed]** Wallet error checking limits, and filters.
- **[Extra]** Rapid click logic and age boundary limits (off by one).

---

### 10. Visa Services
**Ground Truth Tests:** 20 | **Generated Tests:** 20 | **Coverage:** ⚠️ Partial

- Valid pathways (TC-001, TC-002 ≈ VISA-001, VISA-002, VISA-003) ✅
- Empty formats (TC-003 to TC-013 ≈ VISA-006, VISA-007) ✅
- Boundaries and negative dates (TC-014 to TC-020 ≈ VISA-015, VISA-017, VISA-018) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| VISA-008 | Download visa form | Missed PDF download logic. |
| VISA-009 | Track visa status | Missed tracking UI. |
| VISA-010 | View FAQ | Missed FAQ integration. |
| VISA-011 | Invalid track ID | Missed tracking negative behavior. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Extensive individual required field verifications across all 10 properties.

#### 🧠 Business Logic Comparison
**Core Logic:** Visa requirement lookup mapping nationalities to destinations, processing application uploads with strict file limits, and status tracking.
- **[Captured]** Temporal limits (future dates, passport logic).
- **[Captured]** Detailed requirement checking logic.
- **[Missed]** Entire tracking system omitted.
- **[Extra]** Detailed blank field enumerations.

---

### 11. User Dashboard And Booking Management
**Ground Truth Tests:** 23 | **Generated Tests:** 28 (Combined) | **Coverage:** ✅ Good

- Core display limits (Dashboard TC-001, TC-012, TC-013 ≈ UDB-001, UDB-018, UDB-022) ✅
- CRUD operations (Dashboard TC-002 to TC-009, TC-014 to TC-016 ≈ UDB-003, UDB-004, UDB-006, UDB-012, UDB-014) ✅
- Negative testing limits (Dashboard TC-010, TC-011, TC-017 to TC-022 ≈ UDB-007, UDB-008, UDB-019) ✅
- Modification logic (Management TC-001 to TC-006 ≈ UDB-010, UDB-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| UDB-011 | Wishlist interaction | Missed wishlist functionality in dashboard. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Debouncing checks directly on modify and cancel request submission endpoints.
- Validating the cancellation confirmation explicit approval UI modal.

#### 🧠 Business Logic Comparison
**Core Logic:** Authenticated user portal managing profile data, wallet history, and enforcing strict temporal and policy rules for booking modifications.
- **[Captured]** Explicit policy boundary tests (modifying non-eligible, cancelling non-eligible).
- **[Captured]** Missing booking references limits.
- **[Missed]** Wishlists tracking.
- **[Extra]** UI rapid-click assertions on state transitions.

---

### 12. Payment Processing
**Ground Truth Tests:** 25 | **Generated Tests:** 19 | **Coverage:** ⚠️ Partial

- Standard gateways (TC-001 to TC-004 ≈ PAY-003, PAY-004) ✅
- Missing details (TC-005 to TC-010 ≈ PAY-006, PAY-025) ✅
- Formatting bounds (TC-011, TC-012, TC-013, TC-016, TC-017 ≈ PAY-007, PAY-008, PAY-010) ✅
- Extreme boundaries (TC-014, TC-015, TC-018, TC-019 ≈ PAY-022, PAY-023) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PAY-002 | Apply valid promo code | Promo code applying was missed. |
| PAY-013 | Cancel payment gateway | Missed gateway abort path. |
| PAY-014 | Download receipt | Missed post-payment receipt logic. |
| PAY-015 | Change payment method | Missed dynamic form toggles. |
| PAY-016 | Apply invalid promo | Missed promo interaction. |
| PAY-017 | Promo code on unsupported item | Missed promo interaction. |
| PAY-020 | Multiple consecutive payments | Missed rate limiting. |
| PAY-021 | Invoice access before payment | Missed logic bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Testing credit card length bounds down to the specific off-by-one digit logic constraint.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure checkout gateway handling multiple payment forms, promo code validation, and explicit financial boundary logic.
- **[Captured]** Validation logic for cards, expiration math (month in past), length bounds.
- **[Missed]** Promos, receipts, rate limits.
- **[Extra]** Off-by-one digit validation.

---

### 13. Currency And Language Selection
**Ground Truth Tests:** 17 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Selection boundaries (TC-001 to TC-008 ≈ PREF-001, PREF-002, PREF-003) ✅
- Logic bounds (TC-009, TC-010, TC-013, TC-014 ≈ PREF-005, PREF-008, PREF-015) ✅
- Speed boundaries (TC-011, TC-012 ≈ PREF-012) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PREF-009 | Search history language | Missed tracking context retention. |
| PREF-010 | Invalid language code in URL | Missed parameter logic. |
| PREF-011 | Invalid currency code in URL | Missed parameter logic. |
| PREF-013 | Change language mid checkout | Missed deep state UI updates. |
| PREF-014 | Cookie vs Profile scopes | Missed sync logic validation. |
| PREF-016 | Multi-tab sync | Missed cross-tab functionality. |
| PREF-017 | Unauthenticated Profile Preference block | Missed authorization constraint logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Explicit validation checking of leading/trailing whitespaces in currency ID strings.
- Empty state selection validation constraints.

#### 🧠 Business Logic Comparison
**Core Logic:** Global UI state toggling persisting user preferences across navigation and sessions.
- **[Captured]** Debouncing tests on dropdowns, special character sanitization.
- **[Missed]** Session sync constraints across tabs/profiles, URL limits.
- **[Extra]** Formatting string manipulation checks.

---

### 14. Search And Filters
**Ground Truth Tests:** 19 | **Generated Tests:** 24 | **Coverage:** ✅ Good

- Functional applications (TC-001 to TC-006 ≈ FILTER-001, FILTER-002) ✅
- Sort options (TC-007 to TC-010 ≈ FILTER-005) ✅
- Empty limits (TC-011 to TC-018 ≈ FILTER-003, FILTER-004) ✅
- Boundary checks (TC-019, TC-020, TC-021, TC-022, TC-023, TC-024 ≈ FILTER-006, FILTER-015, FILTER-016) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FILTER-009 | Text search filter | Missed dynamic text typeahead. |
| FILTER-011 | Filter error recovery | Missed network disconnect logic. |
| FILTER-019 | Sorting interaction with filters | Missed concurrency check. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Testing specific off-by-one unit interactions on slider boundaries.
- Attempting to reset filters while no filters are selected.

#### 🧠 Business Logic Comparison
**Core Logic:** Universal sorting and filtering mechanisms across all listings with empty-state recovery and extreme value testing.
- **[Captured]** Complex boundary tracking directly on sliders and dropdown interactions.
- **[Captured]** Exhaustive empty/missing logic.
- **[Missed]** Dynamic text, UI errors, sorting interplay.
- **[Extra]** Negative state resets and slider limits.

---

### 15. Reviews And Ratings
**Ground Truth Tests:** 19 | **Generated Tests:** 16 | **Coverage:** ⚠️ Partial

- Standard checks (TC-001 ≈ REVIEW-003) ✅
- Auth constraints (TC-002, TC-003 ≈ REVIEW-006, REVIEW-015) ✅
- Negative checks (TC-004 to TC-010 ≈ REVIEW-005, REVIEW-016) ✅
- Format logic boundaries (TC-011 to TC-016 ≈ REVIEW-007, REVIEW-011, REVIEW-012, REVIEW-019) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REVIEW-008 | Edit review | Missed modifying content. |
| REVIEW-009 | Delete review | Missed destroying content. |
| REVIEW-010 | Review with profanity | Missed explicit content moderation limits. |
| REVIEW-017 | Filter reviews in far future | Missed UI review list manipulation limits. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Dynamic boundary calculation of array limits on multiple category submissions.

#### 🧠 Business Logic Comparison
**Core Logic:** User feedback submission and aggregation strictly requiring completed bookings, minimum character limits, and profanity filtering.
- **[Captured]** Constraints logic for authentication, lengths, empty values, special characters.
- **[Missed]** Content CRUD limits and moderation tools.
- **[Extra]** Category object size limit bounding.

---

### 16. Offers And Deals
**Ground Truth Tests:** 18 | **Generated Tests:** 10 | **Coverage:** ⚠️ Partial

- Interaction limits (TC-001, TC-002, TC-004 ≈ OFFER-003) ✅
- Formatting bounds (TC-003, TC-005, TC-006, TC-007, TC-008 ≈ OFFER-004, OFFER-005, OFFER-014) ✅
- Temporal logic (TC-009, TC-010 ≈ OFFER-007, OFFER-016) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| OFFER-006 | Click specific deal | Missed discovery tools. |
| OFFER-008 | Share offer | Missed UI link generation tool. |
| OFFER-009 | Copy promo code | Missed UI clipboard tool. |
| OFFER-010 | Redeemed offer | Missed single-use checks. |
| OFFER-011 | Deal link manipulation | Missed URL boundaries. |
| OFFER-017 | Rapid apply promo clicks | Missed UI debouncing limits. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Promotional discovery engine verifying offer validity states, newsletter subscription formats, and single-use redemption constraints.
- **[Captured]** Email string formatting limits extensively.
- **[Missed]** Discovery workflows and interactive UI links (Clipboard, Socials).
- **[Extra]** None.

---

### 17. Logout
**Ground Truth Tests:** 9 | **Generated Tests:** 5 | **Coverage:** ✅ Good

- Session checks (TC-001, TC-002, TC-005 ≈ LOGOUT-001, LOGOUT-002, LOGOUT-006) ✅
- Logic hooks (TC-003, TC-004 ≈ LOGOUT-007, LOGOUT-008) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGOUT-003 | Logout from all devices | Missed global logic limits. |
| LOGOUT-005 | Inactive session | Missed session timeout tracking. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complete session termination clearing all state, preventing protected page access, and managing idle/multi-device states.
- **[Captured]** Multi-click debouncing and unprotected page redirects.
- **[Missed]** Global device logout logic limits.
- **[Extra]** None.

---

## Overall Findings

### Missing Coverage Summary
| Module | Missing Tests | Critical Gaps |
|--------|---------------|---------------|
| 1. Home Page | 10 | Missed static components and UI interactive widgets (Tabs). |
| 2. Registration | 11 | Skipped deep password format complexities and optional items. |
| 3. Login | 9 | Completely missed CAPTCHAs, external hooks (Socials), and security injections. |
| 12. Payment | 8 | Completely missed Promotional handling hooks. |
| 13. Currency | 7 | Missed synchronicity limits across tabs and cookies. |

### Conclusion
The **GPT-4o-Mini Agent** approach produced **322** tests but achieved only **7 Good, 10 Partial** coverage. It exhibited highly patterned, repetitive behavior by exhaustively asserting individual blank-field validations across every single form page (e.g., leaving First Name blank, then Last Name blank, then Email blank) instead of discovering deeper state-machine logic. As a result, while it effectively padded its test counts, it structurally ignored interactive components (Maps, Galleries, Clipboards), security contexts (SQLi, XSS, CAPTCHAs), and third-party integrations (Social logins, Promos). Its generated "Extra" tests were largely redundant permutation edge-cases rather than insightful boundary logic discoveries.
