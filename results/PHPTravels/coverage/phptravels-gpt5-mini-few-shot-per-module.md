# PHPTravels - GPT-5-Mini Few Shot Per Module Test Case Generation Report

**Target application:** PHPTravels
**Ground Truth Test Cases:** 347
**Generated Test Cases:** 289
**Model:** `openai/gpt-5-mini`
**Approach:** Few-Shot Per Module

---

## Coverage Definition
- **Missing Coverage:** Ground truth test cases that were not generated.
- **Partial Coverage:** Test cases that partially cover the ground truth logic but miss critical details (e.g., negative scenarios or specific edge cases).
- **Extra Coverage:** Generated test cases that were not explicitly in the ground truth but represent valid scenarios.

---

## Executive Summary
| Module | Ground Truth | Generated | Coverage | Missing | Extra |
|---|---|---|---|---|---|
| 1. Home Page And Search | 25 | 14 | ⚠️ Partial | 15 | 4 |
| 2. Registration | 24 | 13 | ⚠️ Partial | 11 | 0 |
| 3. Login | 22 | 12 | ⚠️ Partial | 10 | 0 |
| 4. Forgot Password | 19 | 14 | ⚠️ Partial | 5 | 0 |
| 5. Hotels Search And Listing | 23 | 19 | ✅ Good | 4 | 0 |
| 6. Hotel Details And Booking | 20 | 14 | ⚠️ Partial | 6 | 0 |
| 7. Flights Search And Booking | 23 | 26 | ✅ Good | 0 | 3 |
| 8. Tours Search And Booking | 20 | 32 | ✅ Good | 0 | 12 |
| 9. Cars Search And Booking | 21 | 27 | ✅ Good | 1 | 7 |
| 10. Visa Services | 20 | 12 | ⚠️ Partial | 8 | 0 |
| 11. User Dashboard And Booking Management | 23 | 32 | ✅ Good | 0 | 9 |
| 12. Payment Processing | 25 | 14 | ⚠️ Partial | 11 | 0 |
| 13. Currency And Language Selection | 17 | 11 | ⚠️ Partial | 6 | 0 |
| 14. Search And Filters | 19 | 16 | ✅ Good | 3 | 0 |
| 15. Reviews And Ratings | 19 | 12 | ⚠️ Partial | 7 | 0 |
| 16. Offers And Deals | 18 | 14 | ✅ Good | 4 | 0 |
| 17. Logout | 9 | 7 | ✅ Good | 2 | 0 |
| **Total** | **347** | **289** | **8 Good, 9 Partial** | **93** | **35** |

---

## Module-by-Module Analysis

### 1. Home Page And Search
**Ground Truth Tests:** 25 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Hotel search with valid criteria (TC-001 ≈ HOME-002) ✅
- Flight search with valid criteria (TC-005, TC-006 ≈ HOME-003) ✅
- Tour search with valid criteria (TC-009 ≈ HOME-004) ✅
- Car search with valid criteria (TC-012 ≈ HOME-005) ✅
- Required field missing validation (TC-002, TC-007, TC-010 ≈ HOME-007, HOME-008) ✅
- Invalid time/date bounds (TC-003, TC-004, TC-008, TC-011, TC-013 ≈ HOME-009, HOME-011) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOME-001 | Home page navigation elements displayed | Few-Shot ignored static structural UI rendering. |
| HOME-006 | Featured content sections displayed | Ignored static marketing blocks. |
| HOME-012 | Verify footer links | Skipped static links. |
| HOME-013 | Verify social media links | Skipped social links. |
| HOME-014 | App download links | Skipped external download links. |
| HOME-015 | Search with past dates | Missed past date explicitly. |
| HOME-016 | Search with special characters | Missed character injection. |
| HOME-017 | Maximum guests | Missed bounds testing on dropdowns. |
| HOME-018 | Maximum rooms | Missed bounds testing on dropdowns. |
| HOME-019 | Maximum search query length | Missed bounds on input length. |
| HOME-021 | Concurrent search submission | Missed concurrency. |
| HOME-022 | Search with XSS payload | Missed security injections. |
| HOME-023 | Network timeout during search | Missed negative network behaviors. |
| HOME-024 | Emoji characters in destination | Missed Unicode bounds. |
| HOME-025 | Very rapid double-click on Search | Missed debouncing bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Explicit tab switching UI update verification (TC-014).
- Single-day tour exact bounds (TC-011).

#### 🧠 Business Logic Comparison
**Core Logic:** Comprehensive search initiation (Hotels, Flights, Tours, Cars) validating required fields, structural UI components, and boundary limits.
- **[Captured]** Search routing (Hotels, Flights, Tours, Cars).
- **[Captured]** Required field validation (missing dates, origin).
- **[Captured]** Temporal validation (invalid date ranges, same-day stays).
- **[Missed]** Static links and deep structural rendering.
- **[Missed]** Security bounds (XSS), Network bounds (Timeout), Extreme limits (Emoji, Max chars).
- **[Extra]** Tab switching state verification.

---

### 2. Registration
**Ground Truth Tests:** 24 | **Generated Tests:** 13 | **Coverage:** ⚠️ Partial

- Successful registration variants (TC-015, TC-016 ≈ REG-002) ✅
- Password mismatch edge cases (TC-017 ≈ REG-006) ✅
- Missing required fields (TC-018 ≈ REG-004) ✅
- Invalid formats (TC-019, TC-022 ≈ REG-005, REG-016) ✅
- Duplicate email handling (TC-020 ≈ REG-007) ✅
- Missing terms and conditions (TC-021 ≈ REG-008) ✅
- Boundary validations (TC-023, TC-024, TC-025, TC-026, TC-027 ≈ REG-009, REG-010, REG-017, REG-018) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REG-001 | Registration page elements displayed | Skipped static UI element assertion. |
| REG-003 | Country code selector works | Missed explicit interaction with mobile code modal. |
| REG-011 | Optional fields | Missed submitting with only minimum viable inputs. |
| REG-012 | Newsletter opt-in | Skipped optional newsletter interaction. |
| REG-013 | Password visibility toggle | Skipped password icon control. |
| REG-014 | Password without numbers | Missed explicit format policy bounds. |
| REG-015 | Password without special char | Missed explicit format policy bounds. |
| REG-019 | Registration timeout | Missed session timeout behavior. |
| REG-020 | Leading/trailing whitespace | Missed input trimming logic. |
| REG-022 | SQL injection in Name field | Missed security logic. |
| REG-023 | Rapid resubmission | Missed debouncing logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Account creation enforcing strict format validation, policy acceptance, and field boundaries.
- **[Captured]** Registration flow processing and auto-login hooks.
- **[Captured]** Input bounds (very long inputs, short passwords, invalid phones).
- **[Missed]** Security and Network bounds (SQL Injection, timeouts, debouncing).
- **[Missed]** UI toggles (Password visibility, Country code modal).
- **[Extra]** None.

---

### 3. Login
**Ground Truth Tests:** 22 | **Generated Tests:** 12 | **Coverage:** ⚠️ Partial

- Successful login without CAPTCHA (TC-028 ≈ LOGIN-001) ✅
- Remember Me check (TC-029 ≈ LOGIN-002) ✅
- Post login redirect bounds (TC-030 ≈ LOGIN-022) ✅
- Alternate options (TC-031, TC-032 ≈ LOGIN-003, LOGIN-009) ✅
- Invalid/Missing credentials (TC-033, TC-034, TC-035 ≈ LOGIN-004, LOGIN-005) ✅
- CAPTCHA threshold check (TC-036 ≈ LOGIN-018) ✅
- String bounds and Unicode (TC-037, TC-038, TC-039 ≈ LOGIN-014, LOGIN-015, LOGIN-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGIN-007 | Email retained after failed login | Missed convenience state UI check. |
| LOGIN-010 | Social Login - Facebook | Only checked Google social login explicitly. |
| LOGIN-011 | Password masking | Skipped native browser input typing masks. |
| LOGIN-012 | SQL injection attempt | Missed database security check. |
| LOGIN-013 | XSS attempt | Missed rendering security check. |
| LOGIN-016 | Long email input | Tested password bounds but explicitly missed max email. |
| LOGIN-017 | Concurrent login | Missed simultaneous session boundaries. |
| LOGIN-019 | Invalid CAPTCHA input | Triggered CAPTCHA but failed to verify inputting a bad one. |
| LOGIN-020 | Rapid consecutive fails | Missed rate limiting. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure session initiation with alternate auth methods, strict invalid handling, and explicit security boundaries.
- **[Captured]** Login routing and alternate session hook (Remember me).
- **[Captured]** Validation error triggering and basic CAPTCHA activation.
- **[Captured]** String manipulation (unicode inputs, trailing spaces).
- **[Missed]** Advanced security constraints (SQL injection, XSS, rate limiting, bad CAPTCHA).
- **[Extra]** None.

---

### 4. Forgot Password
**Ground Truth Tests:** 19 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Request password reset (TC-040 ≈ FP-001) ✅
- Complete reset (TC-041 ≈ FP-002) ✅
- New password overrides old (TC-042 ≈ FP-002 logic) ✅
- Invalid/missing email (TC-044, TC-047, TC-049 ≈ FP-003, FP-004, FP-009) ✅
- Expired/tampered bounds (TC-045, TC-051 ≈ FP-006) ✅
- Password mismatch (TC-046 ≈ FP-005) ✅
- Security injections (TC-048 ≈ FP-011) ✅
- Boundary sizes and reuse (TC-050, TC-052, TC-053 ≈ FP-013, FP-017) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FP-007 | Return to login link | Skipped static UI link testing. |
| FP-008 | Resend link | Missed the resend action. |
| FP-012 | Rate limiting reset requests | Handled "latest token" but missed rate blocking. |
| FP-014 | Case sensitivity email | Missed capitalization formatting tests. |
| FP-019 | Missing new password | Tested mismatch, but missed leaving fields empty completely. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Password recovery lifecycle handling valid/invalid emails, reset link expiration, mismatch validation, and explicit security bounds.
- **[Captured]** Reset requests, token generation, token expiration boundaries.
- **[Captured]** Database constraints (SQL injection, duplicate link usage).
- **[Captured]** Input bounds (very long email, empty email).
- **[Missed]** Basic UI flows (Resend button, return to login link).
- **[Extra]** None.

---

### 5. Hotels Search And Listing
**Ground Truth Tests:** 23 | **Generated Tests:** 19 | **Coverage:** ✅ Good

- Listing display and filtering (TC-054, TC-056, TC-057, TC-059 ≈ HOTEL-001, HOTEL-004) ✅
- Room interactions (TC-055, TC-058 ≈ HOTEL-002, HOTEL-005) ✅
- Sorting options (TC-060, TC-071 ≈ HOTEL-003) ✅
- Negative cases (TC-061, TC-062, TC-063, TC-064, TC-065 ≈ HOTEL-007, HOTEL-014, HOTEL-015) ✅
- Boundary dates and loads (TC-066, TC-067, TC-068, TC-069, TC-070, TC-072 ≈ HOTEL-018, HOTEL-019, HOTEL-020, HOTEL-021) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HOTEL-011 | Map view | Missed map interaction. |
| HOTEL-012 | Change currency on listing | Missed currency toggling. |
| HOTEL-022 | Remove disabled filter | Missed UI button state. |
| HOTEL-023 | Price slider handles crossed | Missed checking physics constraint on dual slider. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Dynamic property catalog with multi-dimensional filtering, temporal validation, and UI interaction states.
- **[Captured]** Listing page sorting, active filter removal, and placeholder image resilience.
- **[Captured]** Form constraints (zero guests, impossible dates, missing inputs).
- **[Captured]** Boundary values (same-day stay, 180-day stay, rapid toggling).
- **[Missed]** Slider handle physics and specialized view controls (Maps/Currency).
- **[Extra]** None.

---

### 6. Hotel Details And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Details display (TC-073, TC-085 ≈ HBOOK-001) ✅
- Room selection and booking (TC-074, TC-075 ≈ HBOOK-002, HBOOK-003) ✅
- Optional fields (TC-076, TC-082 ≈ HBOOK-007) ✅
- Authentication precondition (TC-077 ≈ HBOOK-016) ✅
- Input validations (TC-078, TC-079, TC-080 ≈ HBOOK-005, HBOOK-020) ✅
- Boundaries and limits (TC-081, TC-083, TC-084, TC-086 ≈ HBOOK-013, HBOOK-015) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| HBOOK-008 | View photo gallery | Missed gallery interaction. |
| HBOOK-009 | View map location | Missed map link interaction. |
| HBOOK-010 | Add to wishlist | Missed wishlist functionality. |
| HBOOK-011 | Invalid date change in details | Skipped validating date updates on the detail page itself. |
| HBOOK-017 | Submit without room selected | Missed form submission constraint checking. |
| HBOOK-019 | Special characters in requests | Checked length bounds but missed character sanitization bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Deep property data presentation and booking progression with strict room availability and passenger limits.
- **[Captured]** Booking progression (auth required, pricing updates, mandatory fields).
- **[Captured]** Form validations (invalid phone, invalid email, maximum length limits).
- **[Captured]** Business rules (max occupancy limit, zero-night stay bounds).
- **[Missed]** Peripheral interaction hooks (Map view, Gallery modal, Wishlist).
- **[Extra]** None.

---

### 7. Flights Search And Booking
**Ground Truth Tests:** 23 | **Generated Tests:** 26 (Combined) | **Coverage:** ✅ Good

- One-way, Round-trip, Multi-city (Listing TC-087, TC-088, TC-089 ≈ FLIGHT-005, FLIGHT-010) ✅
- Itinerary details and filters (Listing TC-090, TC-091, TC-092, TC-100 ≈ FLIGHT-001, FLIGHT-002, FLIGHT-003) ✅
- Invalid parameters and logic checks (Listing TC-094 to TC-099 ≈ FLIGHT-014, FLIGHT-015, FLIGHT-016, FLIGHT-017) ✅
- Booking workflow (Booking TC-101, TC-102, TC-103, TC-104, TC-105 ≈ FLIGHT-004) ✅
- Negative passenger information (Booking TC-106, TC-109, TC-110 ≈ FLIGHT-006, FLIGHT-008) ✅
- Passport validity and extreme bounds (Booking TC-107, TC-108, TC-111, TC-112 ≈ FLIGHT-007, FLIGHT-022) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| None | All critical flows mapped perfectly. | N/A |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Infants greater than adults limit checking (Listing TC-097).
- Proceeding with explicit maximum length name values (Booking TC-110).
- Saving contact details persistence across steps (Booking TC-104).

#### 🧠 Business Logic Comparison
**Core Logic:** Complex flight routing (Round-trip, One-way, Multi-city) with extensive filtering, passenger detail validation, and strict boundary logic.
- **[Captured]** Core routing (Round-trip, Multi-city) and UI rendering (filters, bag data).
- **[Captured]** Logical constraints (infants vs adults ratio, max passengers).
- **[Captured]** Documentation bounds (passport expiration boundaries, future DOBs).
- **[Missed]** None.
- **[Extra]** Infant ratio bounds logic.

---

### 8. Tours Search And Booking
**Ground Truth Tests:** 20 | **Generated Tests:** 32 (Combined) | **Coverage:** ✅ Good

- Search controls and sliders (Search TC-113 to TC-119 ≈ TOUR-001, TOUR-002) ✅
- Invalid boundaries on search (Search TC-120 to TC-126 ≈ TOUR-018, TOUR-019) ✅
- Detail rendering (Booking TC-127, TC-141, TC-143, TC-144 ≈ TOUR-003, TOUR-008) ✅
- Core booking progression (Booking TC-128, TC-129, TC-130, TC-138 ≈ TOUR-004, TOUR-017) ✅
- Booking validation and constraints (Booking TC-131 to TC-137, TC-139, TC-140, TC-142 ≈ TOUR-005, TOUR-006, TOUR-011, TOUR-013, TOUR-014) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| None | All flows deeply mapped. | N/A |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Day-trip boundary bounds checking on duration calculation.
- Expanding/collapsing itinerary UI logic sections explicitly.
- Unauthenticated redirect loop persistence.

#### 🧠 Business Logic Comparison
**Core Logic:** Tour package presentation with itinerary details, date-based availability checking, and dynamic price recalculation.
- **[Captured]** Full tour detail view interaction (Map, Itinerary accordion, Reviews).
- **[Captured]** Financial recalculations based on changing traveler compositions.
- **[Captured]** Booking state bounds (Auth required, missing required terms, unavailable dates).
- **[Captured]** Boundary values (Huge group sizing, zero travelers, exact budgets).
- **[Missed]** None.
- **[Extra]** Deep UX logic on accordion expansion and auth redirects.

---

### 9. Cars Search And Booking
**Ground Truth Tests:** 21 | **Generated Tests:** 27 (Combined) | **Coverage:** ✅ Good

- Search and display (Search TC-145, TC-146 ≈ CAR-001, CAR-008) ✅
- Filter execution (Search TC-147, TC-148, TC-158 ≈ CAR-010) ✅
- Math and logic bounds (Search TC-150, TC-152, TC-153, TC-154, TC-155, TC-156, TC-157 ≈ CAR-012, CAR-015, CAR-017) ✅
- Booking submission (Booking TC-159 to TC-163 ≈ CAR-003, CAR-004) ✅
- Missing/Invalid data (Booking TC-164 to TC-168, TC-170, TC-171 ≈ CAR-005, CAR-006, CAR-007) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| CAR-013 | Payment with invalid wallet balance | Missed integration logic with wallet during car checkout. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- International license issue country alphanumeric formatting verification.
- Validating the mathematical price calculation logic (Rate * Days = Total).

#### 🧠 Business Logic Comparison
**Core Logic:** Vehicle rental catalog with add-on options (insurance), explicit pick-up/drop-off validation, and strict age-based policy enforcement.
- **[Captured]** Add-on and insurance pricing recalculations.
- **[Captured]** Underage limits and specific boundary limits (exact 21 age, past dates).
- **[Captured]** Required fields (Missing names, Unchecked terms).
- **[Missed]** Cross-module wallet payment test.
- **[Extra]** Explicit multi-day math total checking.

---

### 10. Visa Services
**Ground Truth Tests:** 20 | **Generated Tests:** 12 | **Coverage:** ⚠️ Partial

- Requirements view (TC-172, TC-176 ≈ VISA-001, VISA-002) ✅
- Form submission and attachments (TC-173, TC-174, TC-183 ≈ VISA-003, VISA-014) ✅
- Tracking logic (TC-175 ≈ VISA-009) ✅
- Formatting bounds (TC-177, TC-178, TC-179, TC-180, TC-181, TC-182 ≈ VISA-006, VISA-007, VISA-015, VISA-017) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| VISA-008 | Download visa form | Missed specific PDF action. |
| VISA-010 | View FAQ | Missed static UI accordion. |
| VISA-011 | Invalid track ID | Missed negative search bounds. |
| VISA-012 | Upload invalid document format | Tested size, missed unsupported extensions specifically. |
| VISA-016 | Non-numeric duration of stay | Missed negative type enforcement. |
| VISA-018 | Date of birth in future | Missed negative time bounds. |
| VISA-019 | Rapid resubmission | Missed debouncing. |
| VISA-020 | Long special character filename | Missed OS-level file string bounds. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- "No visa required" exemption message handling (TC-176).

#### 🧠 Business Logic Comparison
**Core Logic:** Visa requirement lookup mapping nationalities to destinations, processing application uploads with strict file limits, and status tracking.
- **[Captured]** Core lookup logic and Visa Exemption messaging.
- **[Captured]** Form submission with heavy document sizing limits.
- **[Captured]** Validation of dates, emails, and phone inputs.
- **[Missed]** Static links (FAQ, Forms).
- **[Missed]** Deep negative bounds (invalid track IDs, fake extensions, future DOB).
- **[Extra]** Exemption logic.

---

### 11. User Dashboard And Booking Management
**Ground Truth Tests:** 23 | **Generated Tests:** 32 (Combined) | **Coverage:** ✅ Good

- Display and basic links (Dashboard TC-184, TC-188, TC-189 ≈ UDB-001, UDB-002, UDB-011) ✅
- Action executions (Dashboard TC-185, TC-186, TC-187, TC-190, TC-191 ≈ UDB-003, UDB-004, UDB-006, UDB-012) ✅
- Profile / Negative cases (Dashboard TC-193 to TC-203 ≈ UDB-007, UDB-008, UDB-009, UDB-014, UDB-018) ✅
- Deep modifications (Booking TC-204 to TC-208 ≈ UDB-003) ✅
- Policy rules and limits (Booking TC-209 to TC-215 ≈ UDB-007, UDB-010, UDB-023) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| None | All critical scenarios robustly captured. | N/A |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Dashboard pagination logic with extreme number of records (TC-199).
- Modifying a booking on the exact boundary day before departure (TC-213).
- Tracking unconfirmed cancellation flows to ensure DB states remain intact (TC-212).

#### 🧠 Business Logic Comparison
**Core Logic:** Authenticated user portal managing profile data, wallet history, and enforcing strict temporal and policy rules for booking modifications.
- **[Captured]** Dashboard view, PDF downloading, and profile updating.
- **[Captured]** Complex booking modification workflows (changing dates, adding requests).
- **[Captured]** Refund handling limits (zero refund amounts, invalid refund rules).
- **[Captured]** Policy enforcement (modifying restricted bookings, cancelling past cutoffs).
- **[Extra]** Deep DB-state integrity checks (abandoning cancellation midway).

---

### 12. Payment Processing
**Ground Truth Tests:** 25 | **Generated Tests:** 14 | **Coverage:** ⚠️ Partial

- Valid Payment Gateways (TC-216, TC-217, TC-218, TC-219, TC-220 ≈ PAY-003, PAY-004) ✅
- Invalid card bounds (TC-221, TC-222, TC-223, TC-224, TC-225 ≈ PAY-006, PAY-007, PAY-008, PAY-010) ✅
- System limits and formatting (TC-226, TC-227, TC-228, TC-229 ≈ PAY-023, PAY-024) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PAY-002 | Apply valid promo code | Ignored promo integration entirely. |
| PAY-009 | Terms unchecked | Missed the mandatory checkbox logic. |
| PAY-013 | Cancel payment gateway | Missed external gateway abortion. |
| PAY-014 | Download receipt | Missed post-payment receipt logic. |
| PAY-015 | Change payment method | Missed dynamic form toggles. |
| PAY-016 | Apply invalid promo | Ignored promo integration. |
| PAY-017 | Promo code on unsupported item | Ignored promo integration. |
| PAY-018 | Exact zero balance payment | Missed edge case math. |
| PAY-020 | Multiple consecutive payments | Missed rate limiting. |
| PAY-021 | Invoice access before payment | Missed precondition limits. |
| PAY-025 | Submit with no payment method | Missed empty state validation. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Secure checkout gateway handling multiple payment forms, promo code validation, and explicit financial boundary logic.
- **[Captured]** Direct card handling, Wallet, and Bank Transfer flows.
- **[Captured]** Strong financial bounds (Luhn check, expired cards, mismatched CVVs).
- **[Captured]** Network failure recovery and retry resilience.
- **[Missed]** Promo logic (entirely skipped in this module).
- **[Missed]** Post-payment UI actions (downloading receipt, cancelling gateway).
- **[Extra]** None.

---

### 13. Currency And Language Selection
**Ground Truth Tests:** 17 | **Generated Tests:** 11 | **Coverage:** ⚠️ Partial

- Update interactions and UI limits (TC-230, TC-231, TC-232, TC-233, TC-234 ≈ PREF-001, PREF-002, PREF-003, PREF-006, PREF-012) ✅
- Missing/Invalid fallback routes (TC-235, TC-236, TC-237, TC-238, TC-239, TC-240 ≈ PREF-005, PREF-008, PREF-013) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| PREF-009 | Search history language | Missed specific translation context. |
| PREF-010 | Invalid language code in URL | Missed parameter injection limits. |
| PREF-014 | Cookie vs Profile scopes | Touched on it but missed explicit divergence testing. |
| PREF-015 | RTL layout with unsaved form | Missed deep state form persistence bounds. |
| PREF-016 | Multi-tab preference sync | Missed cross-tab logic. |
| PREF-017 | Unauthenticated Profile Preference block | Missed auth redirect constraint. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Global UI state toggling persisting user preferences across navigation and sessions.
- **[Captured]** Currency/Language updates across public and logged-in states.
- **[Captured]** RTL switching behavior and dynamic recalculations mid-checkout.
- **[Captured]** Missing translation fallbacks and zero-decimal currency bounds (JPY).
- **[Missed]** Cross-tab synchronicity, explicit URL code validation, form state limits.
- **[Extra]** None.

---

### 14. Search And Filters
**Ground Truth Tests:** 19 | **Generated Tests:** 16 | **Coverage:** ✅ Good

- Standard execution logic (TC-241, TC-242, TC-243, TC-244 ≈ FILTER-001, FILTER-002, FILTER-005) ✅
- Clearing interactions (TC-245, TC-246, TC-247 ≈ FILTER-003, FILTER-004) ✅
- Multiple and combinations bounds (TC-248, TC-249, TC-250, TC-255, TC-256 ≈ FILTER-006, FILTER-012) ✅
- Invalid parameters (TC-251, TC-252, TC-253, TC-254 ≈ FILTER-007, FILTER-015, FILTER-017) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| FILTER-008 | Sort by Rating | Missed explicit rating sort. |
| FILTER-009 | Text search filter | Missed dynamic text search bar. |
| FILTER-011 | Filter error recovery | Missed network disconnect logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Universal sorting and filtering mechanisms across all listings with empty-state recovery and extreme value testing.
- **[Captured]** All core filter interactions (sliders, checkboxes, clearing).
- **[Captured]** Empty states and maximum combinations (select all filters UI overflow).
- **[Captured]** Logic breaks (min > max, negative durations, reversed time arrays).
- **[Missed]** Dynamic text searching and network failure resilience.
- **[Extra]** None.

---

### 15. Reviews And Ratings
**Ground Truth Tests:** 19 | **Generated Tests:** 12 | **Coverage:** ⚠️ Partial

- Execution display (TC-257, TC-258 ≈ REVIEW-001, REVIEW-002) ✅
- Form submission and auth constraints (TC-259, TC-261, TC-262, TC-263 ≈ REVIEW-003, REVIEW-006, REVIEW-015) ✅
- Logic and boundary validation (TC-260, TC-264, TC-265, TC-266, TC-267, TC-268 ≈ REVIEW-004, REVIEW-007, REVIEW-011, REVIEW-012, REVIEW-018) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| REVIEW-008 | Edit review | Missed CRUD actions. |
| REVIEW-009 | Delete review | Missed CRUD actions. |
| REVIEW-010 | Review with profanity | Missed content moderation. |
| REVIEW-014 | Rapid review submission | Missed debouncing checks. |
| REVIEW-016 | Specific category rating missing | Tested overall rating missing, but skipped sub-ratings. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- Uploading non-image files into the photo submission dialog (TC-265).

#### 🧠 Business Logic Comparison
**Core Logic:** User feedback submission and aggregation strictly requiring completed bookings, minimum character limits, and profanity filtering.
- **[Captured]** Review listing rendering and filtering.
- **[Captured]** Submission bounds (missing ratings, unauthenticated blocks, ineligible user blocks).
- **[Captured]** Extreme boundaries (max photos, max text, future review dates).
- **[Missed]** Modifying reviews, moderation (profanity), and UI debouncing.
- **[Extra]** Filetype validation logic on uploads.

---

### 16. Offers And Deals
**Ground Truth Tests:** 18 | **Generated Tests:** 14 | **Coverage:** ✅ Good

- Discovery logic (TC-269, TC-270 ≈ OFFER-001, OFFER-002) ✅
- Application paths (TC-271, TC-272 ≈ OFFER-003) ✅
- Formats and limits (TC-273, TC-274, TC-275, TC-276, TC-277, TC-278, TC-279, TC-280, TC-281, TC-282 ≈ OFFER-004, OFFER-005, OFFER-007, OFFER-012, OFFER-014, OFFER-016) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| OFFER-008 | Share offer | Missed share widget. |
| OFFER-009 | Copy promo code | Missed copy-to-clipboard widget. |
| OFFER-011 | Deal link manipulation | Missed URL tampering constraints. |
| OFFER-017 | Rapid apply promo clicks | Missed UI debouncing limits. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Promotional discovery engine verifying offer validity states, newsletter subscription formats, and single-use redemption constraints.
- **[Captured]** Display and application (promo code injection, URL redirects).
- **[Captured]** Validity checks (expired deals, illogical date searches).
- **[Captured]** Form constraints (empty emails, max long destinations).
- **[Captured]** Extreme discount boundaries (0% and 100% off rendering limits).
- **[Missed]** Social sharing and clipboard interactions.
- **[Extra]** None.

---

### 17. Logout
**Ground Truth Tests:** 9 | **Generated Tests:** 7 | **Coverage:** ✅ Good

- General routing (TC-283, TC-284 ≈ LOGOUT-001) ✅
- Protected routes handling (TC-285, TC-286, TC-287 ≈ LOGOUT-002, LOGOUT-006) ✅
- Logic and rapid boundaries (TC-288, TC-289 ≈ LOGOUT-007, LOGOUT-008) ✅

#### ❌ Missing Scenarios Table
| GT ID | Missing Scenario | Reason |
|-------|-----------------|--------|
| LOGOUT-003 | Logout from all devices | Missed global session termination tool. |
| LOGOUT-005 | Inactive session | Missed automatic timeout logic. |

#### ➕ Extra Scenarios (in Generated, not in GT)
- None.

#### 🧠 Business Logic Comparison
**Core Logic:** Complete session termination clearing all state, preventing protected page access, and managing idle/multi-device states.
- **[Captured]** Explicit logout paths (desktop header, mobile menu).
- **[Captured]** Access prevention limits (back button, direct URL navigation).
- **[Captured]** Race condition checks (mid-flight requests, rapid double clicks).
- **[Missed]** Global multi-device termination and idle timeouts.
- **[Extra]** None.

---

## Overall Findings

### Missing Coverage Summary
| Module | Missing Tests | Critical Gaps |
|--------|---------------|---------------|
| 1. Home Page | 15 | Static links, structural rendering, and security boundaries. |
| 2. Registration | 11 | Optional controls, security boundaries, and UI toggles. |
| 3. Login | 10 | Rate limiting, advanced CAPTCHA logic, and security injections. |
| 10. Visa | 8 | FAQ links, PDF downloads, and negative form formatting. |
| 12. Payment | 11 | Complete omission of promo-code handling during checkout. |
| 15. Reviews | 7 | Modifying reviews, deleting reviews, and profanity filtering. |

### Conclusion
The **GPT-5-Mini Few-Shot Per Module** model generated **289** tests and mapped functionally to most of the system. However, it was strictly constrained by its prompt, leaning heavily toward standard input validations (missing fields, invalid dates) while **systematically missing complex UI interactions** (like Maps, Photo Galleries, or Copy-to-Clipboard buttons) and deep security bounds (XSS, SQL Injection). Compared to the Agent approach (which actively discovered boundary conditions through reflection), the Few-Shot model performed statically but maintained excellent business logic precision for the core booking math and form rules.
