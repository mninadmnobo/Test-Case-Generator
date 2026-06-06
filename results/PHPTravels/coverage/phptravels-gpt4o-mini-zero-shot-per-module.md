# PHPTravels - GPT-4o-Mini Zero-Shot Per Module Test Case Generation Report

**Target application:** PHPTravels
**Ground Truth Test Cases:** 347
**Generated Test Cases:** 133
**Model:** `openai/gpt-4o-mini`
**Approach:** Zero-Shot Per Module

---

## Coverage Definition
- **Missing Coverage:** Ground truth test cases that were not generated.
- **Partial Coverage:** Test cases that partially cover the ground truth logic but miss critical details (e.g., negative scenarios or specific edge cases).
- **Extra Coverage:** Generated test cases that were not explicitly in the ground truth but represent valid scenarios.

---

## Executive Summary
| Module | Ground Truth | Generated | Coverage | Missing | Extra |
|---|---|---|---|---|---|
| 1. Home Page And Search | 25 | 5 | ❌ Poor | 20 | 0 |
| 2. Registration | 24 | 8 | ❌ Poor | 16 | 0 |
| 3. Login | 22 | 6 | ❌ Poor | 16 | 0 |
| 4. Forgot Password | 19 | 5 | ❌ Poor | 14 | 0 |
| 5. Hotels Search And Listing | 23 | 8 | ❌ Poor | 15 | 0 |
| 6. Hotel Details And Booking | 20 | 6 | ❌ Poor | 14 | 0 |
| 7. Flights Search And Booking | 23 | 6 | ❌ Poor | 17 | 0 |
| 8. Tours Search And Booking | 20 | 13 | ⚠️ Partial | 7 | 0 |
| 9. Cars Search And Booking | 21 | 12 | ⚠️ Partial | 9 | 0 |
| 10. Visa Services | 20 | 8 | ❌ Poor | 12 | 0 |
| 11. User Dashboard And Booking Management | 23 | 16 | ⚠️ Partial | 7 | 0 |
| 12. Payment Processing | 25 | 7 | ❌ Poor | 18 | 0 |
| 13. Currency And Language Selection | 17 | 8 | ⚠️ Partial | 9 | 0 |
| 14. Search And Filters | 19 | 7 | ❌ Poor | 12 | 0 |
| 15. Reviews And Ratings | 19 | 6 | ❌ Poor | 13 | 0 |
| 16. Offers And Deals | 18 | 8 | ❌ Poor | 10 | 0 |
| 17. Logout | 9 | 4 | ⚠️ Partial | 5 | 0 |
| **Total** | **347** | **133** | **0 Good, 5 Partial, 12 Poor** | **214** | **0** |

---

## Module-by-Module Analysis

### 1. Home Page And Search
**Ground Truth Tests:** 25 | **Generated Tests:** 5 | **Coverage:** ❌ Poor

- Very basic generic inputs for 4 tabs.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOME-001 | Home page navigation | Missed rendering validation. |
| HOME-006 | Featured sections | Missed rendering validation. |
| HOME-007 | Invalid fields | Missed negative formats. |
| HOME-008 | Boundary logic | Missed limits. |
| HOME-009 | Temporal logic | Missed temporal validation. |
| HOME-010 | Extreme dates | Missed constraints. |
| HOME-011 | Passenger bounds | Missed numerical logic. |
| HOME-012 | Verify footer links | Skipped static links. |
| HOME-013 | Verify social media | Skipped social links. |
| HOME-014 | App download links | Skipped external download links. |
| HOME-016 | Maximum inputs | Missed character limits. |
| HOME-019 | Special characters | Missed format checks. |
| HOME-020 | Tab switching UI update | Missed UI control testing. |
| HOME-021 | Concurrent search | Missed concurrency check. |
| HOME-022 | Search with XSS payload | Missed security logic. |
| HOME-023 | Network timeout | Missed negative network logic. |
| HOME-025 | Rapid double-click on search | Missed UI debouncing. |

*(Remaining generic positive cases omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Comprehensive search initiation validating required fields, structural UI components, and boundary limits.
- **[Captured]** Bare minimum form submissions.
- **[Missed]** All boundaries, components, and security limits.
- **[Extra]** None.

---

### 2. Registration
**Ground Truth Tests:** 24 | **Generated Tests:** 8 | **Coverage:** ❌ Poor

- Valid registration.
- Generic missing fields.
- Invalid email format and mismatching passwords.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REG-001 | Registration page elements displayed | Skipped UI checks. |
| REG-003 | Country code selector works | Missed modal logic. |
| REG-006 | Phone number invalid format | Missed specific boundary. |
| REG-008 | Unchecked Terms & Conditions | Missed boolean validation. |
| REG-012 | Newsletter opt-in | Missed optional inputs. |
| REG-013 | Password visibility toggle | Missed local browser logic. |
| REG-014 | Password without numbers | Missed password complexity. |
| REG-015 | Password without special char | Missed password complexity. |
| REG-016 | Password without uppercase | Missed password complexity. |
| REG-017 | Short password boundary | Missed minimum bounds. |
| REG-018 | Long password boundary | Missed maximum bounds. |
| REG-019 | Registration timeout | Missed session logic. |
| REG-021 | Extremely long name strings | Missed explicit name limits. |
| REG-022 | SQL injection | Missed security check. |
| REG-023 | Rapid resubmission | Missed UI debouncing. |
| REG-024 | Special characters password match | Missed encoding limits. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Account creation enforcing strict format validation, policy acceptance, and field boundaries.
- **[Captured]** Generic validations.
- **[Missed]** All specific complexity bounds.
- **[Extra]** None.

---

### 3. Login
**Ground Truth Tests:** 22 | **Generated Tests:** 6 | **Coverage:** ❌ Poor

- Standard valid/invalid checks.
- Empty states.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGIN-004 | Incorrect password specifically | Generically bundled. |
| LOGIN-005 | Incorrect email specifically | Generically bundled. |
| LOGIN-009 | Social Login - Google | Missed external hooks. |
| LOGIN-010 | Social Login - Facebook | Missed external hooks. |
| LOGIN-011 | Password masking | Missed input type checking. |
| LOGIN-012 | SQL injection attempt | Missed database security check. |
| LOGIN-013 | XSS attempt | Missed rendering security check. |
| LOGIN-014 | White spaces in credentials | Missed string formatting logic. |
| LOGIN-015 | Maximum length fields | Generic bounding issue. |
| LOGIN-017 | Concurrent login | Missed simultaneous session boundaries. |
| LOGIN-020 | Extremely long email | Missed specific crash limits. |
| LOGIN-021 | Case sensitivity in password | Missed character enforcement limits. |
| LOGIN-022 | Back button after login | Missed browser history bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure session initiation with alternate auth methods, strict invalid handling, and explicit security boundaries.
- **[Captured]** Very basic path validation.
- **[Missed]** Social logins, injection vectors, specific errors.
- **[Extra]** None.

---

### 4. Forgot Password
**Ground Truth Tests:** 19 | **Generated Tests:** 5 | **Coverage:** ❌ Poor

- Email checking limits.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FP-005 | Valid password reset link | Missed entirely. |
| FP-006 | Invalid password reset link | Missed entirely. |
| FP-007 | Return to login link | Missed link test. |
| FP-008 | Resend link | Missed resend logic. |
| FP-009 | New password matches old | Missed password history constraint. |
| FP-010 | New password format fail | Missed complexity bounds. |
| FP-011 | SQL injection | Missed injection check. |
| FP-012 | Rate limiting reset requests | Missed abuse limitation logic. |
| FP-013 | Leading whitespace in email | Missed string formatting logic. |
| FP-014 | Special characters in email | Missed string formatting logic. |
| FP-015 | Used reset token | Missed single-use validation constraint. |
| FP-019 | Maximum password length | Missed validation. |

*(Remaining cases omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Password recovery lifecycle handling valid/invalid emails, reset link expiration, mismatch validation, and explicit security bounds.
- **[Captured]** Email entry form.
- **[Missed]** The entire password reset linkage pathway (the second half of the module).
- **[Extra]** None.

---

### 5. Hotels Search And Listing
**Ground Truth Tests:** 23 | **Generated Tests:** 8 | **Coverage:** ❌ Poor

- Basic search flows and price filter.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOTEL-008 | Filter by property type | Missed category filters. |
| HOTEL-009 | Filter by amenities | Missed checkbox filters. |
| HOTEL-011 | Map view | Missed map interaction. |
| HOTEL-012 | Change currency on listing | Did not test currency toggle. |
| HOTEL-014 | Temporal limits | Missed bounds. |
| HOTEL-015 | Missing fields | Missed bounds. |
| HOTEL-016 | Boundary guests | Missed numerical validation. |
| HOTEL-018 | Negative date inputs | Missed dates. |
| HOTEL-019 | Name strings | Missed length limits. |
| HOTEL-020 | Rapid toggle filters | Missed debouncing logic. |
| HOTEL-021 | Special characters | Missed bounds. |
| HOTEL-022 | Remove disabled filter | Missed disabled state checking. |
| HOTEL-023 | Price slider handles crossed | Missed slider bounds. |

*(Remaining cases omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Dynamic property catalog with multi-dimensional filtering, temporal validation, and UI interaction states.
- **[Captured]** Bare minimum form submissions.
- **[Missed]** All complex UI views (Maps) and numerical boundaries.
- **[Extra]** None.

---

### 6. Hotel Details And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 6 | **Coverage:** ❌ Poor

- Execution of booking.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HBOOK-008 | View photo gallery | Missed gallery interaction. |
| HBOOK-009 | View map location | Missed map interaction. |
| HBOOK-010 | Add to wishlist | Missed wishlist functionality. |
| HBOOK-011 | Select past dates | Missed temporal limit. |
| HBOOK-012 | Zero guest count | Missed lower bounds. |
| HBOOK-013 | Excessive guest count | Missed upper bounds. |
| HBOOK-014 | Max stay limit | Missed duration bounds. |
| HBOOK-016 | Pre-filled data | Missed logic test. |
| HBOOK-017 | Submit without room | Missed room selection state. |
| HBOOK-018 | Invalid email | Missed formatting logic. |
| HBOOK-019 | Special characters | Missed specific restrictions. |
| HBOOK-020 | Payment gateway redirect | Missed state transition check. |

*(Remaining cases omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Deep property data presentation and booking progression with strict room availability and passenger limits.
- **[Captured]** Generic missing checks.
- **[Missed]** All dynamic elements (Galleries, Maps, State changes).
- **[Extra]** None.

---

### 7. Flights Search And Booking
**Ground Truth Tests:** 23 | **Generated Tests:** 6 | **Coverage:** ❌ Poor

- Extreme module collapse (produced 0 tests for Flight Booking explicitly).

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FLIGHT-004 | Book a flight | Entire booking suite missed. |
| FLIGHT-006 | Negative pass count | Missed numeric limit. |
| FLIGHT-007 | Missing passport | Missed specific field logic. |
| FLIGHT-008 | Missing names | Missed specific field logic. |
| FLIGHT-011 | Stops filter | Missed specific filter bounds. |
| FLIGHT-012 | Airline filter | Missed specific filter bounds. |
| FLIGHT-014 | Missing passenger inputs | Bundled generically. |
| FLIGHT-022 | Special characters | Missed string formatting. |

*(10+ additional cases omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complex flight routing (Round-trip, One-way, Multi-city) with extensive filtering, passenger detail validation, and strict boundary logic.
- **[Captured]** Basic search only.
- **[Missed]** The entire checkout module completely failed to generate.
- **[Extra]** None.

---

### 8. Tours Search And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 13 (Combined) | **Coverage:** ⚠️ Partial

- Standard checks.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| TOUR-008 | Gallery logic | Missed visual UI. |
| TOUR-009 | Map logic | Missed interactive UI. |
| TOUR-013 | Extreme dates | Missed bounds. |
| TOUR-014 | Price limits | Missed calculation limits. |
| TOUR-017 | Authenticated data load | Missed logic. |
| TOUR-018 | Missing fields | Generic bundles. |
| TOUR-020 | Negative numericals | Missed explicit error boundary. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Tour package presentation with itinerary details, date-based availability checking, and dynamic price recalculation.
- **[Captured]** Generic booking tests.
- **[Missed]** Galleries, interactive pricing updates.
- **[Extra]** None.

---

### 9. Cars Search And Booking
**Ground Truth Tests:** 21 | **Generated Tests:** 12 (Combined) | **Coverage:** ⚠️ Partial

- Basic parameter limits.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| CAR-010 | Advanced filter logic | Partially missed. |
| CAR-013 | Wallet invalid payment | Missed wallet integrations limit. |
| CAR-014 | Temporal overlap | Missed checking drop-off math. |
| CAR-015 | Future limit | Missed bound. |
| CAR-016 | Minimum age limit | Missed numerical bound. |
| CAR-017 | Maximum age limit | Missed numerical bound. |
| CAR-018 | Long name boundaries | Specific constraint missed. |
| CAR-019 | Special char bounds | Specific constraint missed. |
| CAR-020 | UI debouncing | Missed fast-click checking. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Vehicle rental catalog with add-on options (insurance), explicit pick-up/drop-off validation, and strict age-based policy enforcement.
- **[Captured]** Generic missing values.
- **[Missed]** Strict domain limits (Age, Math overlapping dates).
- **[Extra]** None.

---

### 10. Visa Services
**Ground Truth Tests:** 20 | **Generated Tests:** 8 | **Coverage:** ❌ Poor

- General formatting bounds.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| VISA-008 | Download visa form | Missed download feature. |
| VISA-009 | Track visa status | Missed tracking UI. |
| VISA-010 | View FAQ | Missed static info sections. |
| VISA-011 | Invalid track ID | Missed negative tracking logic. |
| VISA-012 | Empty track ID | Missed negative tracking logic. |
| VISA-013 | Long track ID | Missed length boundaries. |
| VISA-014 | Valid track ID | Missed positive tracking logic. |
| VISA-015 | Invalid document upload type | Missed validation constraint. |
| VISA-017 | Passport expire past | Missed temporal limit. |
| VISA-018 | Date formats | Missed formatting logic. |
| VISA-019 | Special chars | Missed specific bounds. |
| VISA-020 | Rapid resubmit | Missed UI debouncing. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Visa requirement lookup mapping nationalities to destinations, processing application uploads with strict file limits, and status tracking.
- **[Captured]** Generics.
- **[Missed]** Entire Tracking sub-module.
- **[Extra]** None.

---

### 11. User Dashboard And Booking Management
**Ground Truth Tests:** 23 | **Generated Tests:** 16 (Combined) | **Coverage:** ⚠️ Partial

- Standard CRUD paths.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| UDB-011 | Wishlist interaction | Specific check logic not fully covered. |
| UDB-014 | Invoice rendering | Missed UI bound. |
| UDB-018 | Name bounds | Missed character limits. |
| UDB-019 | Missing names | Missed updates logic. |
| UDB-021 | Invoice missing | Missed edge state. |
| UDB-022 | Empty dashboard state | Missed state render logic. |

*(Others omitted)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Authenticated user portal managing profile data, wallet history, and enforcing strict temporal and policy rules for booking modifications.
- **[Captured]** Basic edits.
- **[Missed]** Wishlist, invoices, complex states.
- **[Extra]** None.

---

### 12. Payment Processing
**Ground Truth Tests:** 25 | **Generated Tests:** 7 | **Coverage:** ❌ Poor

- Very basic CC limits.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PAY-002 | Apply valid promo code | Missed promotional paths. |
| PAY-008 | Future expiration logic | Missed specific date math. |
| PAY-009 | Invalid CVV | Bundled generically. |
| PAY-011 | Invalid Wallet Funds | Bundled. |
| PAY-013 | Cancel payment gateway | Missed gateway abort path. |
| PAY-014 | Download receipt | Missed post-payment receipt logic. |
| PAY-015 | Change payment method | Missed dynamic form toggles. |
| PAY-016 | Apply invalid promo | Missed promo interaction. |
| PAY-017 | Promo code on unsupported item | Missed promo interaction. |
| PAY-020 | Multiple consecutive payments | Missed rate limiting. |
| PAY-021 | Invoice access before payment | Missed logic bounds. |
| PAY-025 | Empty wallet transaction | Missed specific bounds. |

*(Remaining 6 tests omitted for brevity)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure checkout gateway handling multiple payment forms, promo code validation, and explicit financial boundary logic.
- **[Captured]** Valid paths.
- **[Missed]** Almost all gateway bounds, wallet logic, and promo limits.
- **[Extra]** None.

---

### 13. Currency And Language Selection
**Ground Truth Tests:** 17 | **Generated Tests:** 8 | **Coverage:** ⚠️ Partial

- Standard switching flows.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PREF-004 | Session persistence validation | Missed complex bounds. |
| PREF-008 | Invalid characters | Missed injection checks. |
| PREF-009 | Search history language | Missed tracking context retention. |
| PREF-010 | Invalid language code in URL | Missed parameter logic. |
| PREF-011 | Invalid currency code in URL | Missed parameter logic. |
| PREF-013 | Change language mid checkout | Missed deep state UI updates. |
| PREF-014 | Cookie vs Profile scopes | Missed sync logic validation. |
| PREF-016 | Multi-tab sync | Missed cross-tab functionality. |
| PREF-017 | Unauthenticated Profile Preference block | Missed authorization constraint logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Global UI state toggling persisting user preferences across navigation and sessions.
- **[Captured]** Standard toggles.
- **[Missed]** All deep state retention logic and session limits.
- **[Extra]** None.

---

### 14. Search And Filters
**Ground Truth Tests:** 19 | **Generated Tests:** 7 | **Coverage:** ❌ Poor

- Only very generic filters mapped.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FILTER-009 | Text search filter | Missed dynamic text typeahead. |
| FILTER-011 | Filter error recovery | Missed network disconnect logic. |
| FILTER-013 | Multi-category selection | Bundled generically. |
| FILTER-014 | Negative value checks | Missed numerical constraints. |
| FILTER-015 | Extremely large prices | Missed numerical boundaries. |
| FILTER-016 | Special character searches | Missed string parsing rules. |
| FILTER-017 | Rapid toggling | Missed UI debouncing. |
| FILTER-018 | URL parameter injection | Missed deep linking limits. |
| FILTER-019 | Sorting interaction with filters | Missed concurrency check. |

*(Remaining cases omitted)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Universal sorting and filtering mechanisms across all listings with empty-state recovery and extreme value testing.
- **[Captured]** Generic slider bounds.
- **[Missed]** High density sorting interactions and text parsing.
- **[Extra]** None.

---

### 15. Reviews And Ratings
**Ground Truth Tests:** 19 | **Generated Tests:** 6 | **Coverage:** ❌ Poor

- Limits on comments.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REVIEW-007 | Exceed character limits | Bundled generically. |
| REVIEW-008 | Edit review | Missed modifying content. |
| REVIEW-009 | Delete review | Missed destroying content. |
| REVIEW-010 | Review with profanity | Missed explicit content moderation limits. |
| REVIEW-011 | HTML payload review | Missed injection checks. |
| REVIEW-012 | Zero star rating | Missed bounds. |
| REVIEW-016 | Invalid dates | Missed constraints. |
| REVIEW-017 | Filter reviews in far future | Missed UI review list manipulation limits. |
| REVIEW-018 | Extremely large payload | Missed size limits. |
| REVIEW-019 | Rating math average | Missed numeric checking bounds. |

*(Remaining cases omitted)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** User feedback submission and aggregation strictly requiring completed bookings, minimum character limits, and profanity filtering.
- **[Captured]** Nothing more than basic form submissions.
- **[Missed]** All backend integration limits and moderation.
- **[Extra]** None.

---

### 16. Offers And Deals
**Ground Truth Tests:** 18 | **Generated Tests:** 8 | **Coverage:** ❌ Poor

- Generic clicks.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| OFFER-006 | Click specific deal | Bundled generically. |
| OFFER-008 | Share offer | Missed UI link generation tool. |
| OFFER-009 | Copy promo code | Missed UI clipboard tool. |
| OFFER-010 | Redeemed offer | Missed single-use checks. |
| OFFER-011 | Deal link manipulation | Missed URL boundaries. |
| OFFER-014 | Special characters newsletter | Missed string check. |
| OFFER-017 | Rapid apply promo clicks | Missed UI debouncing limits. |

*(Remaining cases omitted)*

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Promotional discovery engine verifying offer validity states, newsletter subscription formats, and single-use redemption constraints.
- **[Captured]** Generic emails.
- **[Missed]** Single-use checking and external sharing logic.
- **[Extra]** None.

---

### 17. Logout
**Ground Truth Tests:** 9 | **Generated Tests:** 4 | **Coverage:** ⚠️ Partial

- Session checks.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGOUT-003 | Logout from all devices | Missed global logic limits. |
| LOGOUT-006 | Network limits | Missed network integration tests. |
| LOGOUT-007 | Double click limits | Missed fast check. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complete session termination clearing all state, preventing protected page access, and managing idle/multi-device states.
- **[Captured]** Basic expiration.
- **[Missed]** Edge validation checks.
- **[Extra]** None.

---

## Overall Findings

### Zero-Shot Collapse and Hallucination Constraints
The **GPT-4o-Mini Zero-Shot Per Module** test case generator produced only **133 test cases**, which represents a severe shortfall compared to the 347 Ground Truth benchmark. 

Without the explicit pattern-matching guidance provided by few-shot examples or the logical reflection afforded by an Agentic loop, the Zero-Shot model relied purely on its pre-trained statistical average of what "software testing" looks like. It consistently generalized the testing of every single module into a generic 5-test block:
1. Valid inputs.
2. Missing required fields.
3. Maximum length fields.
4. Empty fields.
5. Invalid formats.

**Critical Failures Observed:**
- **Flight Booking Module Collapse:** The model entirely collapsed on the `Flight Booking` module. It generated the JSON wrapper for the module but hallucinated an empty array of test cases. This occurs in zero-shot generation when a smaller model loses attention to the complex specific steps of an intricate workflow (like passenger/passport assignments) and defaults to an empty response rather than attempting to reason through the complexity.
- **Surface-Level Generalization:** It completely ignored PHPTravels-specific logic boundaries. It missed all dynamic UI interactions (Galleries, Maps, Filtering interactions), cross-session logic (Wishlists, Multi-tab logout), and security hooks (XSS, SQLi). 
- **Extra Edge Cases:** The model generated **0 extra** edge cases. It exhibited absolutely no exploratory behavior or attempt to push system limits beyond explicitly defined bounds.

**Business Logic Gap:**
- The model skipped approximately 61% of the entire application logic.
- **[Captured]** Generic form submission limits.
- **[Missed]** All domain-specific travel booking logic (temporal bound assertions, room/passenger limit constraints, gateway cancellation policies).
- **[Extra]** None. 

### Final Model Comparison Context
When analyzing `GPT-4o-Mini` across the three approaches:
1. **Agent (322 tests):** The highest generation count, though it was highly repetitive and inflated by exhaustive single-field checking rather than deep logic.
2. **Few-Shot (215 tests):** Required explicit, forced prompt modifications to break past prompt overfitting; ultimately still failed to hit the deep state logic.
3. **Zero-Shot (133 tests):** Fell back to generic statistical averages, collapsing on complex modules and failing to capture the core domain logic.
