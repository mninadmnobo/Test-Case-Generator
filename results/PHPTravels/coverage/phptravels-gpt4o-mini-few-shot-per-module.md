# PHPTravels - GPT-4o-Mini Few-Shot Per Module Test Case Generation Report (Regenerated)

**Target application:** PHPTravels
**Ground Truth Test Cases:** 347
**Generated Test Cases:** 215
**Model:** `openai/gpt-4o-mini`
**Approach:** Few-Shot Per Module (with modified Exhaustive prompt)

---

## Coverage Definition
- **Missing Coverage:** Ground truth test cases that were not generated.
- **Partial Coverage:** Test cases that partially cover the ground truth logic but miss critical details (e.g., negative scenarios or specific edge cases).
- **Extra Coverage:** Generated test cases that were not explicitly in the ground truth but represent valid scenarios.

---

## Executive Summary
| Module | Ground Truth | Generated | Coverage | Missing | Extra |
|---|---|---|---|---|---|
| 1. Home Page And Search | 25 | 13 | ❌ Poor | 12 | 0 |
| 2. Registration | 24 | 8 | ❌ Poor | 16 | 0 |
| 3. Login | 22 | 10 | ⚠️ Partial | 12 | 0 |
| 4. Forgot Password | 19 | 10 | ⚠️ Partial | 9 | 0 |
| 5. Hotels Search And Listing | 23 | 16 | ⚠️ Partial | 7 | 0 |
| 6. Hotel Details And Booking | 20 | 9 | ❌ Poor | 11 | 0 |
| 7. Flights Search And Booking | 23 | 19 | ✅ Good | 4 | 0 |
| 8. Tours Search And Booking | 20 | 18 | ✅ Good | 2 | 0 |
| 9. Cars Search And Booking | 21 | 16 | ⚠️ Partial | 5 | 0 |
| 10. Visa Services | 20 | 8 | ❌ Poor | 12 | 0 |
| 11. User Dashboard And Booking Management | 23 | 28 | ✅ Good | 2 | 7 |
| 12. Payment Processing | 25 | 13 | ⚠️ Partial | 12 | 0 |
| 13. Currency And Language Selection | 17 | 9 | ⚠️ Partial | 8 | 0 |
| 14. Search And Filters | 19 | 10 | ⚠️ Partial | 9 | 0 |
| 15. Reviews And Ratings | 19 | 9 | ⚠️ Partial | 10 | 0 |
| 16. Offers And Deals | 18 | 11 | ⚠️ Partial | 7 | 0 |
| 17. Logout | 9 | 8 | ✅ Good | 1 | 0 |
| **Total** | **347** | **215** | **4 Good, 9 Partial, 4 Poor** | **139** | **7** |

---

## Module-by-Module Analysis

### 1. Home Page And Search
**Ground Truth Tests:** 25 | **Generated Tests:** 13 | **Coverage:** ❌ Poor

- Basic search flows covered across tabs.
- Some invalid temporal bound logic (check-out before check-in).
- Missing destination checks.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOME-001 | Navigation rendering | Missed UI rendering tests. |
| HOME-006 | Featured content | Missed promotional content. |
| HOME-008 | Invalid characters in search | Missed negative character limit tests. |
| HOME-009 | Search date in past | Missed specific temporal bound. |
| HOME-012 | Verify footer links | Skipped static links. |
| HOME-013 | Verify social media links | Skipped social links. |
| HOME-014 | App download links | Skipped external download links. |
| HOME-016 | Maximum length inputs | Missed character limits on destination. |
| HOME-020 | Tab switching UI update | Missed UI control testing. |
| HOME-021 | Concurrent search submission | Missed concurrency check. |
| HOME-022 | Search with XSS payload | Missed security logic. |
| HOME-023 | Network timeout | Missed negative network logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Home page provides primary search widgets, interactive tabs, and static promotional content.
- **[Captured]** Primary search flows.
- **[Missed]** All static content rendering, navigation, and extreme boundary security.
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
- **[Captured]** Valid paths and basic blank constraints.
- **[Missed]** All password complexity logic and external UI features.
- **[Extra]** None.

---

### 3. Login
**Ground Truth Tests:** 22 | **Generated Tests:** 10 | **Coverage:** ⚠️ Partial

- Standard login and empty states.
- Rapid failures triggering constraints.
- Remember me toggle test.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGIN-004 | Incorrect password specifically | Generically bundled. |
| LOGIN-005 | Incorrect email specifically | Generically bundled. |
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
- **[Captured]** Basic credential logic.
- **[Missed]** Social logins, Injection vectors, and precise edge testing.
- **[Extra]** None.

---

### 4. Forgot Password
**Ground Truth Tests:** 19 | **Generated Tests:** 10 | **Coverage:** ⚠️ Partial

- Valid email and empty submission.
- Password change and mismatch checking.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FP-007 | Return to login link | Missed link test. |
| FP-008 | Resend link | Missed resend logic. |
| FP-009 | New password matches old | Missed password history constraint. |
| FP-010 | New password format fail | Missed complexity bounds. |
| FP-011 | SQL injection | Missed injection check. |
| FP-012 | Rate limiting reset requests | Missed abuse limitation logic. |
| FP-013 | Leading whitespace in email | Missed string formatting logic. |
| FP-014 | Special characters in email | Missed string formatting logic. |
| FP-015 | Used reset token | Missed single-use validation constraint. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Password recovery lifecycle handling valid/invalid emails, reset link expiration, mismatch validation, and explicit security bounds.
- **[Captured]** Basic reset flow.
- **[Missed]** Complexity bounds, rate limits, and injection limits.
- **[Extra]** None.

---

### 5. Hotels Search And Listing
**Ground Truth Tests:** 23 | **Generated Tests:** 16 | **Coverage:** ⚠️ Partial

- Standard searches and temporal bounds.
- Filtering by star ratings and price ranges.
- Sort functionalities.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOTEL-008 | Filter by property type | Missed category filters. |
| HOTEL-009 | Filter by amenities | Missed checkbox filters. |
| HOTEL-011 | Map view | Missed map interaction. |
| HOTEL-012 | Change currency on listing | Did not test currency toggle. |
| HOTEL-020 | Rapid toggle filters | Missed debouncing logic. |
| HOTEL-022 | Remove disabled filter | Missed disabled state checking. |
| HOTEL-023 | Price slider handles crossed | Missed slider bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Dynamic property catalog with multi-dimensional filtering, temporal validation, and UI interaction states.
- **[Captured]** Basic search, basic filtering limits, generic empty checks.
- **[Missed]** Specific visual UI logic (Maps), complex specific filters (Amenities).
- **[Extra]** None.

---

### 6. Hotel Details And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 9 | **Coverage:** ❌ Poor

- Execution of booking.
- Missing field constraints.
- Maximum length tracking.

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
| HBOOK-017 | Submit without room | Missed room selection state. |
| HBOOK-018 | Invalid email | Missed formatting logic. |
| HBOOK-019 | Special characters | Missed specific restrictions. |
| HBOOK-020 | Payment gateway redirect | Missed state transition check. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Deep property data presentation and booking progression with strict room availability and passenger limits.
- **[Captured]** Basic valid submission logic.
- **[Missed]** Deep validation bounds, interaction elements, and gateway transitions.
- **[Extra]** None.

---

### 7. Flights Search And Booking
**Ground Truth Tests:** 23 | **Generated Tests:** 19 (Combined) | **Coverage:** ✅ Good

- Combined search types (round-trip, one-way, multi-city).
- Invalid strings and passenger limits.
- Valid booking pathways.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FLIGHT-011 | Stops filter | Missed specific filter bounds. |
| FLIGHT-012 | Airline filter | Missed specific filter bounds. |
| FLIGHT-014 | Missing passenger inputs | Bundled generically. |
| FLIGHT-022 | Special characters | Missed string formatting. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complex flight routing (Round-trip, One-way, Multi-city) with extensive filtering, passenger detail validation, and strict boundary logic.
- **[Captured]** Strong coverage of booking constraints and passenger logic.
- **[Missed]** Specific advanced filter assertions.
- **[Extra]** None.

---

### 8. Tours Search And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 18 (Combined) | **Coverage:** ✅ Good

- Valid parameter searches.
- Extreme boundary value checking.
- Booking workflow.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| TOUR-008 | Gallery logic | Missed visual UI. |
| TOUR-009 | Map logic | Missed interactive UI. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Tour package presentation with itinerary details, date-based availability checking, and dynamic price recalculation.
- **[Captured]** Boundary values for limits, generic booking paths.
- **[Missed]** Only interactive external hooks.
- **[Extra]** None.

---

### 9. Cars Search And Booking
**Ground Truth Tests:** 21 | **Generated Tests:** 16 (Combined) | **Coverage:** ⚠️ Partial

- Filtering by car types and transmissions.
- Booking with valid and invalid bounds.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| CAR-010 | Advanced filter logic | Partially missed. |
| CAR-013 | Wallet invalid payment | Missed wallet integrations limit. |
| CAR-018 | Long name boundaries | Specific constraint missed. |
| CAR-019 | Special char bounds | Specific constraint missed. |
| CAR-020 | UI debouncing | Missed fast-click checking. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Vehicle rental catalog with add-on options (insurance), explicit pick-up/drop-off validation, and strict age-based policy enforcement.
- **[Captured]** Basic constraints and booking rules.
- **[Missed]** Wallet error checking, debouncing logic, and special formatting boundaries.
- **[Extra]** None.

---

### 10. Visa Services
**Ground Truth Tests:** 20 | **Generated Tests:** 8 | **Coverage:** ❌ Poor

- Requirement lookups.
- Missing field constraints.
- File upload constraints.

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
- **[Captured]** Basic file uploads.
- **[Missed]** Completely skipped the Status Tracking functionality.
- **[Extra]** None.

---

### 11. User Dashboard And Booking Management
**Ground Truth Tests:** 23 | **Generated Tests:** 28 (Combined) | **Coverage:** ✅ Good

- High density of generic tests on modifying and cancelling constraints.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| UDB-011 | Wishlist interaction | Specific check logic not fully covered. |
| UDB-021 | Invoice missing | Missed edge state. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Generic permutations of different non-eligible statuses for cancellation.

#### 🧠 Business Logic Comparison
**Core Logic:** Authenticated user portal managing profile data, wallet history, and enforcing strict temporal and policy rules for booking modifications.
- **[Captured]** Good coverage of cancellation and modification policies.
- **[Missed]** Minor UI boundary checks.
- **[Extra]** Heavy permutation logic on invalid updates.

---

### 12. Payment Processing
**Ground Truth Tests:** 25 | **Generated Tests:** 13 | **Coverage:** ⚠️ Partial

- Base gateways tested.
- Standard missing/expired card limits.

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

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure checkout gateway handling multiple payment forms, promo code validation, and explicit financial boundary logic.
- **[Captured]** Basic credit card failures.
- **[Missed]** All Promotional logic, rate limits, and receipt management.
- **[Extra]** None.

---

### 13. Currency And Language Selection
**Ground Truth Tests:** 17 | **Generated Tests:** 9 | **Coverage:** ⚠️ Partial

- Standard switching flows.
- Empty states.

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
| PREF-004 | Session persistence validation | Missed complex bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Global UI state toggling persisting user preferences across navigation and sessions.
- **[Captured]** Basic state toggles.
- **[Missed]** Complex deep-link URL integrations and tab synchronizations.
- **[Extra]** None.

---

### 14. Search And Filters
**Ground Truth Tests:** 19 | **Generated Tests:** 10 | **Coverage:** ⚠️ Partial

- Basic price limits.

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

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Universal sorting and filtering mechanisms across all listings with empty-state recovery and extreme value testing.
- **[Captured]** Basic constraints.
- **[Missed]** Advanced numerical boundaries, typeahead interactions, URL manipulations.
- **[Extra]** None.

---

### 15. Reviews And Ratings
**Ground Truth Tests:** 19 | **Generated Tests:** 9 | **Coverage:** ⚠️ Partial

- Submission limits.

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

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** User feedback submission and aggregation strictly requiring completed bookings, minimum character limits, and profanity filtering.
- **[Captured]** Generic missing checks.
- **[Missed]** Content CRUD constraints, moderation tools, rating averages.
- **[Extra]** None.

---

### 16. Offers And Deals
**Ground Truth Tests:** 18 | **Generated Tests:** 11 | **Coverage:** ⚠️ Partial

- Click-throughs and newsletters.

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

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Promotional discovery engine verifying offer validity states, newsletter subscription formats, and single-use redemption constraints.
- **[Captured]** Basic subscription validations.
- **[Missed]** Clipboards, single-use logic bounds, external URL parameters.
- **[Extra]** None.

---

### 17. Logout
**Ground Truth Tests:** 9 | **Generated Tests:** 8 | **Coverage:** ✅ Good

- Session expiration and clearing.

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGOUT-003 | Logout from all devices | Missed global logic limits. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complete session termination clearing all state, preventing protected page access, and managing idle/multi-device states.
- **[Captured]** Strong standard coverage.
- **[Missed]** Multi-device constraint.
- **[Extra]** None.

---

## Overall Findings

### Missing Coverage Summary
| Module | Missing Tests | Critical Gaps |
|--------|---------------|---------------|
| 1. Home Page | 12 | Missed static components and UI interactive widgets (Tabs). |
| 2. Registration | 16 | Skipped deep password format complexities and optional items. |
| 3. Login | 12 | Completely missed CAPTCHAs, external hooks (Socials), and security injections. |
| 12. Payment | 12 | Completely missed Promotional handling hooks. |
| 13. Currency | 8 | Missed synchronicity limits across tabs and cookies. |

### Conclusion
The **GPT-4o-Mini Few-Shot Per Module** approach generated **215** tests when explicitly instructed via prompt constraints to act exhaustively. Even with forced length guidelines, it achieved only **4 Good, 9 Partial, 4 Poor** coverage. 

It suffers from an inability to generate dense, multi-layered boundary cases in a single pass. The model captured standard form constraints (empty fields, long text strings) but comprehensively missed all deep state logic, security payloads, and UI interaction widgets. This indicates that modifying the few-shot prompt simply inflated the quantity of generic test cases rather than granting the model any deeper architectural insight.
