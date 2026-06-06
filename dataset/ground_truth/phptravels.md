# PHPTravels Test Cases

**Website URL:** https://phptravels.com/demo
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Home Page And Search](#1-home-page-and-search)
2. [Registration](#2-registration)
3. [Login](#3-login)
4. [Forgot Password](#4-forgot-password)
5. [Hotels Search And Listing](#5-hotels-search-and-listing)
6. [Hotel Details And Booking](#6-hotel-details-and-booking)
7. [Flights Search And Booking](#7-flights-search-and-booking)
8. [Tours Search And Booking](#8-tours-search-and-booking)
9. [Cars Search And Booking](#9-cars-search-and-booking)
10. [Visa Services](#10-visa-services)
11. [User Dashboard And Booking Management](#11-user-dashboard-and-booking-management)
12. [Payment Processing](#12-payment-processing)
13. [Currency And Language Selection](#13-currency-and-language-selection)
14. [Search And Filters](#14-search-and-filters)
15. [Reviews And Ratings](#15-reviews-and-ratings)
16. [Offers And Deals](#16-offers-and-deals)
17. [Logout](#17-logout)

---

## 1. Home Page And Search

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-001 | Home page navigation elements displayed | None | 1. Navigate to the PHPTravels home page | Top navigation, currency selector, language selector, login/signup links, and search widget are visible | High |
| HOME-002 | Hotel search from home page | None | 1. Select the Hotels tab<br>2. Enter destination<br>3. Select valid check-in and check-out dates<br>4. Set guests and rooms<br>5. Click "Search" | User is redirected to the hotel listing page with matching search criteria summary | High |
| HOME-003 | Flight search from home page | None | 1. Select the Flights tab<br>2. Enter origin and destination<br>3. Select valid dates and class<br>4. Click "Search" | User is redirected to the flight listing page with results matching the search criteria | High |
| HOME-004 | Tour search from home page | None | 1. Select the Tours tab<br>2. Enter destination<br>3. Select travel date<br>4. Click "Search" | User is redirected to the tour listing page with matching results | Medium |
| HOME-005 | Car search from home page | None | 1. Select the Cars tab<br>2. Enter pick-up and drop-off data<br>3. Select valid date and time values<br>4. Click "Search" | User is redirected to the car listing page with matching results | Medium |
| HOME-006 | Featured content sections displayed | None | 1. Scroll through the home page | Featured hotels, popular destinations, and promotional sections are visible | Medium |
| HOME-012 | Verify footer links | None | 1. Scroll to footer<br>2. Click a link | Link redirects correctly | Low |
| HOME-013 | Verify social media links | None | 1. Click social media icon | Opens correct social page | Low |
| HOME-014 | App download links | None | 1. Click App Store / Play Store link | Redirects to respective store | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-007 | Hotel search with required fields missing | None | 1. Select Hotels tab<br>2. Leave destination or required dates empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-008 | Flight search with required fields missing | None | 1. Select Flights tab<br>2. Leave origin or destination empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-009 | Invalid hotel date range | None | 1. Select Hotels tab<br>2. Choose check-out before check-in<br>3. Click "Search" | Search is blocked or date validation feedback is displayed | High |
| HOME-015 | Search with past dates | None | 1. Enter past dates in search | Validation error prevents search | High |
| HOME-016 | Search with special characters | None | 1. Enter special characters in destination | No results found or validation message | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-010 | One-way flight disables return date | None | 1. Select Flights tab<br>2. Choose "One Way" | Return date field becomes disabled or inactive | Medium |
| HOME-011 | Same-day search values | None | 1. Perform search using the earliest allowed same-day date values | Search handles the earliest valid date boundary consistently | Low |
| HOME-017 | Maximum guests | None | 1. Enter max allowed adults | Form accepts value | Low |
| HOME-018 | Maximum rooms | None | 1. Enter max allowed rooms | Form accepts value | Low |
| HOME-019 | Maximum search query length | None | 1. Paste very long string in destination | Input is truncated or handled gracefully | Low |
| HOME-020 | Rapid tab switching | Home | 1. Click Hotels, Flights, Tours rapidly | UI stabilizes correctly | Low |
| HOME-021 | Concurrent search submission | None | 1. Click Search on two tabs simultaneously | Handled gracefully without session corruption | Medium |
| HOME-022 | Search with XSS payload | None | 1. Enter `<script>alert(1)</script>` | Input is sanitized | High |
| HOME-023 | Network timeout during search | None | 1. Trigger search and drop connection | Displays timeout error | Medium |
| HOME-024 | Emoji characters in destination | None | 1. Search with ✈️ hotel | Processed normally or validated | Low |
| HOME-025 | Very rapid double-click on Search | None | 1. Double click search button | Debounces to single request | High |

---

## 2. Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Registration page elements displayed | None | 1. Navigate to the signup page | Required fields, mobile number country code selector, terms checkbox, and "Sign Up" button are visible | High |
| REG-002 | Successful registration | Email address is not already registered | 1. Enter valid required data<br>2. Accept terms and conditions<br>3. Click "Sign Up" | Account is created and success message or post-registration redirect is shown | High |
| REG-003 | Country code selector works | None | 1. Open mobile country code selector<br>2. Select another country code | Selected country code is applied to the mobile number field | Medium |
| REG-011 | Optional fields | None | 1. Fill only required fields | Registration succeeds | Medium |
| REG-012 | Newsletter opt-in | None | 1. Check newsletter box during signup | User is subscribed | Low |
| REG-013 | Password visibility toggle | None | 1. Click eye icon on password | Password becomes visible | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-004 | First name empty | None | 1. Leave first name empty<br>2. Fill other required fields<br>3. Submit form | Validation error is displayed for first name | High |
| REG-005 | Invalid email format | None | 1. Enter invalid email format<br>2. Fill other required fields<br>3. Submit form | Validation error indicates email format is invalid | High |
| REG-006 | Password mismatch | None | 1. Enter password<br>2. Enter different confirm password<br>3. Submit form | Validation error indicates passwords do not match | High |
| REG-007 | Duplicate email | Existing user with same email already exists | 1. Enter already-registered email<br>2. Fill other valid data<br>3. Submit form | Registration is blocked and duplicate-email error is displayed | High |
| REG-008 | Terms and conditions unchecked | None | 1. Fill valid registration data<br>2. Leave terms unchecked<br>3. Submit form | Registration is blocked and user is prompted to accept terms | High |
| REG-014 | Password without numbers | None | 1. Enter letters only password | Validation error | High |
| REG-015 | Password without special char | None | 1. Enter password lacking special chars | Validation error | High |
| REG-016 | Invalid phone number | None | 1. Enter letters in phone field | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-009 | Minimum password length boundary | None | 1. Enter password at the minimum accepted length<br>2. Fill other valid data<br>3. Submit form | Registration succeeds or validates consistently at the minimum boundary | Low |
| REG-010 | Mobile number with selected country code | None | 1. Select country code<br>2. Enter valid number at expected length boundary | Number is accepted in the expected format | Low |
| REG-017 | Max length first name | None | 1. Enter 50 char first name | Accepted | Low |
| REG-018 | Max length email | None | 1. Enter very long email | Handled gracefully | Low |
| REG-019 | Registration timeout | None | 1. Wait 30 mins before submit | Handled without crash | Low |
| REG-020 | Leading/trailing whitespace in email | None | 1. Enter email with spaces | Spaces trimmed on save | Medium |
| REG-021 | Unicode characters in name | None | 1. Enter Cyrillic/Arabic names | Processed properly | Low |
| REG-022 | SQL injection in Name field | None | 1. Enter `' OR 1=1 --` | Safely escaped | High |
| REG-023 | Rapid resubmission | None | 1. Click Register twice | Debounced and duplicate error shown | Medium |
| REG-024 | Password differs only by whitespace | None | 1. Append space to confirm password | Mismatch error | High |

---

## 3. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login | Registered user exists | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click "Login" | User is redirected to the dashboard or prior protected page | High |
| LOGIN-002 | Remember Me login | Registered user exists | 1. Enter valid credentials<br>2. Check "Remember Me"<br>3. Click "Login" | Session remains active according to remember-me behavior | Medium |
| LOGIN-003 | Login page alternate options displayed | None | 1. Navigate to login page | Forgot password link, signup link, and any enabled social login buttons are visible | Medium |
| LOGIN-009 | Social Login - Google | Google account | 1. Click Google login | Redirects to Google auth | Medium |
| LOGIN-010 | Social Login - Facebook | Facebook account | 1. Click Facebook login | Redirects to FB auth | Medium |
| LOGIN-011 | Password masking | None | 1. Type password | Input is masked with dots/asterisks | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-004 | Invalid email or password | None | 1. Enter invalid email or password<br>2. Click "Login" | Error message is displayed and login does not succeed | High |
| LOGIN-005 | Empty email | None | 1. Leave email empty<br>2. Enter password<br>3. Click "Login" | Validation or login error is displayed | High |
| LOGIN-006 | Empty password | None | 1. Enter email<br>2. Leave password empty<br>3. Click "Login" | Validation or login error is displayed | High |
| LOGIN-012 | SQL injection attempt | None | 1. Enter SQL string in email | Rejected | High |
| LOGIN-013 | XSS attempt | None | 1. Enter script tag in email | Rejected safely | High |
| LOGIN-014 | Whitespace in email | None | 1. Enter valid email with trailing space | Space trimmed, logs in | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Email retained after failed login | None | 1. Enter email<br>2. Enter invalid password<br>3. Click "Login" | Email remains populated while password is cleared | Medium |
| LOGIN-008 | Multiple failed login attempts | None | 1. Submit invalid credentials repeatedly | Site consistently handles repeated failures and may activate additional protection such as CAPTCHA | Low |
| LOGIN-015 | Long password input | None | 1. Enter 100 char password | Handled without crashing | Low |
| LOGIN-016 | Long email input | None | 1. Enter 100 char email | Handled without crashing | Low |
| LOGIN-017 | Concurrent login | None | 1. Login on 2 devices | Session managed | Low |
| LOGIN-018 | CAPTCHA appearance threshold | None | 1. Fail exactly N times | CAPTCHA appears | High |
| LOGIN-019 | Invalid CAPTCHA input | None | 1. Enter wrong CAPTCHA | Blocked | High |
| LOGIN-020 | Rapid consecutive fails | None | 1. Automate 10 fails in 1s | Rate limited | Medium |
| LOGIN-021 | Unicode email format | None | 1. Login with valid unicode email | Succeeds | Low |
| LOGIN-022 | Back button after login | None | 1. Login then press back | Remains logged in | Medium |

---

## 4. Forgot Password

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-001 | Request password reset with existing email | Registered user exists | 1. Open Forgot Password page<br>2. Enter registered email<br>3. Click submit | Confirmation message indicates reset email was sent | High |
| FP-002 | Reset password with valid link | Valid reset link is available | 1. Open reset password page from email link<br>2. Enter valid new password<br>3. Confirm password<br>4. Submit | Password is changed and user is returned to login with success feedback | High |
| FP-007 | Return to login link | None | 1. Click "Back to Login" | Redirects to login | Low |
| FP-008 | Resend link | Requested reset | 1. Click "Resend Email" | New email dispatched | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-003 | Unknown email address | None | 1. Enter non-existent email on Forgot Password page<br>2. Submit | Error message indicates no account exists for that email | High |
| FP-004 | Empty email field | None | 1. Leave email field empty<br>2. Submit | Validation error is displayed | High |
| FP-005 | Reset password mismatch | Valid reset link is available | 1. Enter new password<br>2. Enter different confirm password<br>3. Submit | Password reset is blocked and mismatch error is displayed | High |
| FP-009 | Invalid email format | None | 1. Enter "test@test" | Format validation | High |
| FP-010 | Unregistered valid format | None | 1. Enter unregistered email | Generic success or "not found" | Medium |
| FP-011 | SQL injection on forgot password | None | 1. Enter SQL payload | Rejected | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-006 | Expired reset link | Expired reset link is available | 1. Open expired reset link | Link is rejected and user is prompted to request a new reset email | Medium |
| FP-012 | Rate limiting reset requests | None | 1. Request reset 10 times | Blocked temporarily | Medium |
| FP-013 | Very long email | None | 1. Enter max length email | Handled properly | Low |
| FP-014 | Case sensitivity email | None | 1. Enter capitalized email | Handled properly | Low |
| FP-015 | Exact 24 hour link expiration | Link generated | 1. Use link precisely at 24.0 hours | Validates or expires per policy | High |
| FP-016 | One unit past expiration | Link generated | 1. Use link at 24.01 hours | Blocked | High |
| FP-017 | Link reuse attempt | Link used | 1. Navigate back and use again | Blocked | High |
| FP-018 | Mismatch by one character | Reset form | 1. Confirm pass differs by 1 char | Blocked | Medium |
| FP-019 | Missing new password | Reset form | 1. Submit empty new password | Blocked | High |

---

## 5. Hotels Search And Listing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-001 | Hotel listing page displays search summary and results count | Valid hotel search has been submitted | 1. View hotel listing page | Search summary, total results count, filters, and sorting controls are visible | High |
| HOTEL-002 | Hotel cards display expected content | Valid hotel search has been submitted | 1. View hotel listing page | Each hotel card shows image, name, location, rating, price, and action button | High |
| HOTEL-003 | Sort hotels by price | Valid hotel search has been submitted | 1. Change sort to "Price: Low to High" or "Price: High to Low" | Hotel results reorder according to selected sort | Medium |
| HOTEL-004 | Filter hotels by star rating or facilities | Valid hotel search has been submitted | 1. Apply star or facility filters | Hotel results update to match selected filters | High |
| HOTEL-005 | Open hotel details from listing | Valid hotel search has been submitted | 1. Click hotel name or "View Details" | Hotel details page opens | High |
| HOTEL-010 | Pagination | Multiple pages | 1. Click page 2 | Next page of results loads | Medium |
| HOTEL-011 | Map view | Valid search | 1. Click map view toggle | Map with pins is displayed | Medium |
| HOTEL-012 | Change currency on listing | Valid search | 1. Change currency | Prices update instantly | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-006 | Search with non-matching destination | None | 1. Search for destination with no available properties | Empty-state or no-results feedback is shown | Medium |
| HOTEL-007 | Invalid hotel date range from listing edit | Listing page is open with editable search summary | 1. Set check-out before check-in<br>2. Apply search | Validation prevents invalid search update | High |
| HOTEL-013 | Search non-existent city | None | 1. Search "Atlantis" | "No results found" displayed | Medium |
| HOTEL-014 | Filter combination yielding zero | Valid search | 1. Select conflicting filters | "No results" shown | Low |
| HOTEL-015 | Invalid date modification | Listing open | 1. Modify to past date | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-008 | Price range slider minimum and maximum bounds | Hotel listing page is open | 1. Drag slider to minimum and maximum ends | Result set updates correctly at both range extremes | Low |
| HOTEL-009 | Clear all hotel filters | One or more filters are active | 1. Click "Clear All Filters" | Filters reset and full unfiltered listing returns | Medium |
| HOTEL-016 | Max price filter | Valid search | 1. Set max price to highest possible | Updates correctly | Low |
| HOTEL-017 | Min price filter | Valid search | 1. Set min price to 0 | Updates correctly | Low |
| HOTEL-018 | Max checkin date | Valid search | 1. Set checkin to max allowed year | Updates correctly | Low |
| HOTEL-019 | Non-numeric min price input | Valid search | 1. Enter letters in min price | Resets or validates | Medium |
| HOTEL-020 | Rapid toggle filters | Valid search | 1. Click 5 filters rapidly | Debounces without locking UI | Medium |
| HOTEL-021 | Same day check in and out | Valid search | 1. Set out date = in date | Handled correctly | Low |
| HOTEL-022 | Remove disabled filter | Valid search | 1. Attempt to remove filter when none active | Button disabled | Low |
| HOTEL-023 | Price slider handles crossed | Valid search | 1. Drag left handle past right | Prevented by UI | High |

---

## 6. Hotel Details And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-001 | Hotel details page content displayed | Hotel details page is open | 1. Review hotel details page | Gallery, description, map link, amenities, room availability, reviews, and policies are visible | High |
| HBOOK-002 | View room availability and select room | Hotel details page is open and rooms are available | 1. Review room options<br>2. Click "Select" or "Book Now" on an available room | Booking form opens for the chosen room | High |
| HBOOK-003 | Submit valid hotel booking form | Room selection form is open | 1. Enter valid guest information<br>2. Review price breakdown<br>3. Click booking continuation button | User proceeds to payment step | High |
| HBOOK-004 | Reviews section displayed on hotel details page | Hotel details page is open | 1. Scroll to reviews area | Aggregate rating and individual reviews are visible | Medium |
| HBOOK-008 | View photo gallery | Details page | 1. Click on gallery image | Gallery modal opens | Medium |
| HBOOK-009 | View map location | Details page | 1. Click map link | Map view opens at correct location | Medium |
| HBOOK-010 | Add to wishlist | Details page | 1. Click heart icon | Hotel added to wishlist | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-005 | Required guest details missing | Hotel booking form is open | 1. Leave required guest fields empty<br>2. Submit booking form | Validation errors are displayed and form is not submitted | High |
| HBOOK-006 | Sold-out room cannot be booked | Hotel details page includes sold-out inventory | 1. Attempt to select a sold-out room | Booking action is blocked and room remains unavailable | Medium |
| HBOOK-011 | Invalid date change in details | Details page | 1. Change to past date | Validation error | High |
| HBOOK-012 | Excessive guest count | Details page | 1. Select 100 guests | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-007 | Special requests text boundary | Hotel booking form is open | 1. Enter special requests at maximum practical length<br>2. Continue booking | Text is accepted or validated consistently at the boundary | Low |
| HBOOK-013 | Minimum stay requirement | Details page | 1. Select 1 night | Acceptable if no limit | Low |
| HBOOK-014 | Maximum stay length | Details page | 1. Select 30+ nights | Form accepts value | Low |
| HBOOK-015 | Max room capacity | Details page | 1. Add max adults and kids | Price calculates correctly | Low |
| HBOOK-016 | Book unauthenticated | Details page | 1. Click Book Now without login | Redirected to login | High |
| HBOOK-017 | Submit without room selected | Details page | 1. Attempt to submit booking | Blocked via UI | Medium |
| HBOOK-018 | Extremely long guest name | Booking form | 1. Paste huge name | Handled gracefully | Low |
| HBOOK-019 | Special characters in requests | Booking form | 1. Enter emoji and symbols | Saved correctly | Low |
| HBOOK-020 | Non-numeric guest count | Booking form | 1. Enter text in guest count | Prevented by field | High |

---

## 7. Flights Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-001 | Flight listing displays itinerary cards | Valid flight search has been submitted | 1. View flight listing page | Airline, times, stops, price, and selection controls are displayed for each result | High |
| FLIGHT-002 | Flight filters work | Valid flight search has been submitted | 1. Apply airline, stops, or departure-time filters | Flight results update to match selected filters | High |
| FLIGHT-003 | View flight details from listing | Valid flight search has been submitted | 1. Click "View Details" | Expanded or detailed fare information is displayed | Medium |
| FLIGHT-004 | Proceed to flight booking with valid passenger data | Flight has been selected | 1. Enter valid passenger details<br>2. Accept terms if required<br>3. Continue | User proceeds to payment step | High |
| FLIGHT-005 | Round-trip search shows outbound and return selections | Valid round-trip search has been submitted | 1. Review results | Outbound and return itineraries are displayed | Medium |
| FLIGHT-010 | Multi-city flight search | Valid search | 1. Select multi-city | Options expand for multiple segments | High |
| FLIGHT-011 | Sort flights by duration | Flight listing | 1. Sort by duration | Results sorted shortest to longest | Medium |
| FLIGHT-012 | Change class on listing | Flight listing | 1. Change from Economy to Business | Results and prices update | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-006 | Required passenger field missing | Flight booking form is open | 1. Leave a required passenger field empty<br>2. Continue | Validation error is displayed | High |
| FLIGHT-007 | Passport expiry too soon | Flight booking form is open for travel requiring passport | 1. Enter passport expiry less than six months from travel date<br>2. Continue | Validation error indicates passport validity is insufficient | High |
| FLIGHT-008 | Invalid passport number format | Flight booking form is open | 1. Enter invalid passport format<br>2. Continue | Validation error is displayed | Medium |
| FLIGHT-013 | Search with identical origin and destination | Search widget | 1. Same origin and dest | Validation error | High |
| FLIGHT-014 | Origin city not served | Search widget | 1. Enter obscure city | "No flights found" | Medium |
| FLIGHT-015 | Past departure date | Search widget | 1. Enter past date | Date picker prevents or validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-009 | One-way trip boundary on booking flow | Valid one-way flight search has been submitted | 1. Complete one-way flight selection<br>2. Continue to booking | Booking flow proceeds without requiring return leg data | Low |
| FLIGHT-016 | Maximum passengers | Search widget | 1. Enter 9 adults | Supported up to max allowed | Low |
| FLIGHT-017 | Same day return | Search widget | 1. Depart and return same day | Works correctly | Low |
| FLIGHT-018 | Open jaw flights | Search widget | 1. Enter open jaw routing | Processed correctly | Low |
| FLIGHT-019 | Zero passengers | Search widget | 1. Set adults to 0 | Validation error | High |
| FLIGHT-020 | Sort by non-sortable column | Flight listing | 1. Try to sort by Airline Name | Handled properly | Medium |
| FLIGHT-021 | Return date before departure date | Search widget | 1. Enter invalid return | Blocked | High |
| FLIGHT-022 | Passport expiry exactly on boundary | Booking form | 1. Date is exactly 6 months out | Processed | Low |
| FLIGHT-023 | Rapid expand clicks | Flight listing | 1. Click Details on 3 flights rapidly | UI manages state properly | Medium |

---

## 8. Tours Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-001 | Tour listing cards displayed | Valid tour search has been submitted | 1. View tours listing page | Tour cards show image, title, destination, duration, price, and rating | High |
| TOUR-002 | Filter tours by destination or type | Valid tour search has been submitted | 1. Apply destination or tour-type filters | Tours list updates to match selected filters | Medium |
| TOUR-003 | Tour details page displays itinerary and inclusions | Tour details page is open | 1. Review tour details page | Itinerary, inclusions, exclusions, departure dates, and pricing are visible | High |
| TOUR-004 | Book tour with valid traveler information | Tour details page is open and departure date is available | 1. Select departure date<br>2. Enter traveler details<br>3. Click "Book Now" | User proceeds to payment step | High |
| TOUR-008 | Tour photo gallery | Tour details | 1. Open gallery | Gallery images display correctly | Low |
| TOUR-009 | Included/Excluded services | Tour details | 1. View inclusions/exclusions | Detailed lists are visible | Medium |
| TOUR-010 | Submit inquiry | Tour details | 1. Fill inquiry form | Inquiry is submitted successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-005 | Lead traveler details missing | Tour booking form is open | 1. Leave required traveler fields empty<br>2. Submit | Validation errors are displayed | High |
| TOUR-006 | Unavailable departure date selected | Tour has unavailable dates | 1. Attempt to select an unavailable departure date | Booking cannot continue with unavailable departure | Medium |
| TOUR-011 | Zero travelers | Tour booking | 1. Enter 0 adults | Validation error | High |
| TOUR-012 | Invalid phone number in inquiry | Tour details | 1. Submit inquiry with bad phone | Validation error | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-007 | Adult and child count recalculates total | Tour booking form is open | 1. Adjust adult and child counts at minimum or maximum tested values | Total price recalculates consistently | Low |
| TOUR-013 | Maximum travelers allowed | Tour booking | 1. Select max group size | System accepts booking | Low |
| TOUR-014 | Same day booking | Tour details | 1. Book tour for today | Warning if cutoff time passed | Medium |
| TOUR-015 | Max duration filter | Tour listing | 1. Set duration to max | Handled properly | Low |
| TOUR-016 | Travelers sum exceeds UI rows | Tour booking | 1. Enter 5 adults but remove a row | Blocked | High |
| TOUR-017 | Unauthenticated tour booking | Tour details | 1. Click Book Now | Redirect to login | High |
| TOUR-018 | Budget Min equals Budget Max | Search widget | 1. Set identical budget bounds | Exact search works | Low |
| TOUR-019 | Extremely long destination query | Search widget | 1. Paste huge string | Handled | Low |
| TOUR-020 | Removing all traveler entries | Tour booking | 1. Delete all passenger rows | Blocked on submit | High |

---

## 9. Cars Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-001 | Car listing cards displayed | Valid car search has been submitted | 1. View car listing page | Vehicle image, category, features, rental company, and pricing are visible | High |
| CAR-002 | Compare cars | Valid car search has been submitted | 1. Select compare option for multiple cars | Comparison view or comparison data is displayed | Medium |
| CAR-003 | Add insurance and extras to booking | Car booking form is open | 1. Select insurance or extras<br>2. Review total | Total price updates to include selected options | High |
| CAR-004 | Book car with valid driver information | Car booking form is open | 1. Enter valid driver details<br>2. Accept terms<br>3. Continue | User proceeds to payment step | High |
| CAR-009 | Pick-up/Drop-off map | Car listing | 1. View map for car | Map location shown | Medium |
| CAR-010 | Filter by transmission | Car listing | 1. Select Automatic/Manual | Listing updates | High |
| CAR-011 | View detailed specs | Car details | 1. Click car details | Specs like doors, baggage displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-005 | Required driver information missing | Car booking form is open | 1. Leave required driver fields empty<br>2. Continue | Validation errors are displayed | High |
| CAR-006 | Driver below minimum age | Car booking form is open | 1. Enter age below minimum policy threshold<br>2. Continue | Booking is blocked or age surcharge/policy message is shown | High |
| CAR-007 | Terms and conditions unchecked | Car booking form is open | 1. Fill valid data<br>2. Leave terms unchecked<br>3. Continue | Booking does not proceed and terms validation is shown | High |
| CAR-012 | Drop-off before pick-up | Car search | 1. Select invalid dates | Validation error | High |
| CAR-013 | Payment with invalid wallet balance | Car booking | 1. Select wallet with 0 balance | Error shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-008 | Same pick-up and drop-off location | Car booking form is open | 1. Set same pick-up and drop-off location<br>2. Continue | Booking flow handles same-location return consistently | Low |
| CAR-014 | Long term rental limit | Car search | 1. Book for 60 days | Processed or limited by policy | Low |
| CAR-015 | Very young driver fee | Car booking | 1. Enter age 21 | Surcharge applied correctly | Medium |
| CAR-016 | Max age driver limit | Car booking | 1. Enter age 99 | Handled properly | Low |
| CAR-017 | Same day pick up and drop off | Car search | 1. Set dates to same day | Accepted | Low |
| CAR-018 | Non-numeric driver age | Car booking | 1. Enter text for age | Validation error | High |
| CAR-019 | Book Now without search precondition | Car listing | 1. Access listing directly | UI handles properly | Medium |
| CAR-020 | Rapid Accept Terms toggle | Car booking | 1. Check and uncheck rapidly | State resolves | Low |
| CAR-021 | Invalid Pick Up Time format | Car search | 1. Enter invalid time | Blocked | High |

---

## 10. Visa Services

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-001 | Visa requirements form displayed | None | 1. Open the Visa page | Nationality selector, Destination selector, and requirement lookup action are visible | High |
| VISA-002 | Check visa requirements for selected route | None | 1. Select nationality<br>2. Select destination<br>3. Click "Check Requirements" or equivalent action | Visa requirement details, processing time, validity, required documents, and fees are displayed | High |
| VISA-003 | Submit visa application when application form is available | Visa application form is enabled and user has required documents | 1. Complete visa application fields<br>2. Upload required documents<br>3. Submit application | Visa application is submitted and application status or confirmation is displayed | Medium |
| VISA-008 | Download visa form | Visa details | 1. Click download form | PDF downloads | Medium |
| VISA-009 | Track application | Visa page | 1. Enter application ID | Status displays | High |
| VISA-010 | View FAQ | Visa page | 1. Expand FAQ accordion | Content expands | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-004 | Nationality not selected | None | 1. Leave nationality empty<br>2. Select destination<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-005 | Destination not selected | None | 1. Select nationality<br>2. Leave destination empty<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-006 | Missing required visa application fields | Visa application form is enabled | 1. Leave one or more required applicant fields empty<br>2. Submit application | Validation errors are displayed and application is not submitted | Medium |
| VISA-011 | Invalid track ID | Visa page | 1. Enter fake ID | "Not found" error | Medium |
| VISA-012 | Upload invalid document format | Visa app | 1. Upload .exe file | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-007 | Document upload at allowed size limit | Visa application form is enabled | 1. Upload a supported document at the maximum allowed size<br>2. Submit application | Document is accepted at the allowed boundary | Low |
| VISA-013 | Max document size limit | Visa app | 1. Upload exactly max size | File accepted | Low |
| VISA-014 | Multiple document upload | Visa app | 1. Upload max allowed docs | All files attach | Low |
| VISA-015 | Extremely long applicant name | Visa app | 1. Paste very long name | Accepted up to db limit | Low |
| VISA-016 | Non-numeric duration of stay | Visa app | 1. Enter text | Validation error | High |
| VISA-017 | Date of birth is today | Visa app | 1. Set DOB to today | Edge case acceptance | Low |
| VISA-018 | Date of birth in future | Visa app | 1. Set DOB to tomorrow | Blocked | High |
| VISA-019 | Rapid resubmission | Visa app | 1. Press Back and submit | Handled correctly | Medium |
| VISA-020 | Long special character filename | Visa app | 1. Upload complex filename | Preserved correctly | Low |

---

## 11. User Dashboard And Booking Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-001 | Dashboard sections displayed | Logged in as authenticated user | 1. Open dashboard | My Bookings, My Profile, Wallet, Wishlist, Reviews, and Settings sections are available | High |
| UDB-002 | View booking details | Logged in and at least one booking exists | 1. Open My Bookings<br>2. Click "View Details" | Booking detail page opens with status, traveler data, and pricing breakdown | High |
| UDB-003 | Modify eligible booking | Logged in and modifiable booking exists | 1. Open booking details<br>2. Click "Modify"<br>3. Change eligible details<br>4. Confirm changes | Booking updates successfully and confirmation is shown | High |
| UDB-004 | Cancel eligible booking | Logged in and cancellable booking exists | 1. Open booking details<br>2. Click "Cancel"<br>3. Confirm cancellation | Booking status changes to cancelled and refund details are displayed | High |
| UDB-005 | Remove item from wishlist | Logged in and wishlist is not empty | 1. Open Wishlist<br>2. Click "Remove" on an item | Item is removed from wishlist | Medium |
| UDB-006 | Update profile details | Logged in | 1. Open My Profile<br>2. Update editable fields<br>3. Save | Profile information is updated successfully | Medium |
| UDB-011 | View wallet balance history | Wallet | 1. Open wallet history | Transactions display | Medium |
| UDB-012 | Download invoice | Bookings | 1. Click invoice | PDF invoice downloads | High |
| UDB-013 | Upload profile picture | Profile | 1. Upload valid image | Picture updates | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-007 | Modify non-eligible booking | Logged in and non-modifiable booking exists | 1. Open booking details for restricted booking<br>2. Attempt modification | Modification is blocked and policy feedback is displayed | Medium |
| UDB-008 | Cancel non-eligible booking | Logged in and non-cancellable booking exists | 1. Open booking details for restricted booking<br>2. Attempt cancellation | Cancellation is blocked and applicable policy is displayed | Medium |
| UDB-009 | Invalid profile email update | Logged in | 1. Enter invalid email format in profile<br>2. Save | Validation error is displayed | Medium |
| UDB-014 | Update password with wrong old password | Profile | 1. Enter wrong old password | Validation error | High |
| UDB-015 | Upload large profile picture | Profile | 1. Upload 10MB image | Size limit error | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-010 | Cancellation policy threshold boundary | Logged in and booking has a free-cancellation deadline | 1. Attempt cancellation near the policy cut-off time | Refund amount and policy messaging match the applicable boundary rules | Low |
| UDB-016 | Maximum wishlist items | Wishlist | 1. Add 100 items | Successfully adds or hits limit | Low |
| UDB-017 | Delete last booking | Bookings | 1. Cancel only booking | List shows empty state | Low |
| UDB-018 | Huge profile bio | Profile | 1. Add max char bio | Updates properly | Low |
| UDB-019 | Cancel a Cancelled booking | Bookings | 1. Attempt cancel on cancelled | Wrong state blocked | High |
| UDB-020 | Download confirmation for Cancelled | Bookings | 1. Try to download | Disabled | Medium |
| UDB-021 | Race condition Cancel/Modify | Bookings | 1. Click both rapidly | State resolves safely | High |
| UDB-022 | Modify travel dates to today | Bookings | 1. Set dates to today | Accepted if valid | Low |
| UDB-023 | Zero refund amount cancellation | Bookings | 1. Cancel non-refundable | Handles $0 properly | Medium |

---

## 12. Payment Processing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-001 | Payment summary displayed | User is on payment page | 1. Review payment page | Booking summary, price breakdown, payment methods, and terms checkbox are visible | High |
| PAY-002 | Apply valid promo code | Valid promo code exists | 1. Enter valid promo code<br>2. Click "Apply" | Discount is applied and total updates | Medium |
| PAY-003 | Successful card payment | User is on payment page and uses valid card | 1. Select card payment<br>2. Enter valid cardholder, card number, expiry, and CVV<br>3. Accept terms<br>4. Click "Pay Now" | Payment succeeds and booking confirmation page is displayed | High |
| PAY-004 | Successful wallet payment | User has enough wallet balance | 1. Select wallet or credits payment<br>2. Confirm payment | Payment succeeds and booking confirmation page is displayed | Medium |
| PAY-005 | Confirmation page displayed after successful payment | Payment was successful | 1. Review confirmation page | Booking reference and follow-up actions such as invoice or voucher download are visible | High |
| PAY-013 | Cancel payment gateway | Payment | 1. Redirect to gateway<br>2. Cancel | Returns to checkout with warning | Medium |
| PAY-014 | Download receipt | Success page | 1. Click download receipt | PDF downloads correctly | High |
| PAY-015 | Change payment method | Payment | 1. Select different method | Form fields update accordingly | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-006 | Invalid card number | User is on payment page | 1. Enter invalid card number<br>2. Submit payment | Card validation error is displayed | High |
| PAY-007 | Expired card | User is on payment page | 1. Enter past expiry date<br>2. Submit payment | Expiry validation error is displayed | High |
| PAY-008 | Invalid CVV | User is on payment page | 1. Enter invalid CVV length or format<br>2. Submit payment | CVV validation error is displayed | High |
| PAY-009 | Terms unchecked | User is on payment page | 1. Fill valid payment data<br>2. Leave terms unchecked<br>3. Submit payment | Payment does not proceed and terms validation is displayed | High |
| PAY-010 | Payment declined or insufficient funds | User is on payment page | 1. Submit payment with failing payment source | Error message is displayed with retry or alternate-payment options | High |
| PAY-016 | Apply invalid promo | Payment | 1. Enter fake promo | Validation error | Medium |
| PAY-017 | Promo code on unsupported item | Payment | 1. Apply code for flight on hotel | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-011 | CVV length boundary by card type | User is on payment page | 1. Enter 3-digit CVV for standard card or 4-digit CVV for AmEx-like card | CVV is accepted only when length matches card type rules | Medium |
| PAY-012 | Promo code expiry boundary | Promo code is near expiration | 1. Apply promo code at validity boundary | Promo code is accepted or rejected consistently based on actual validity window | Low |
| PAY-018 | Exact zero balance payment | Wallet | 1. Booking cost equals wallet | Completes without external gateway | Low |
| PAY-019 | Max limit card transaction | Payment | 1. Book extremely expensive item | Processed or handled by gateway limits | Low |
| PAY-020 | Multiple consecutive payments | Payment | 1. Make 3 payments in a row | Handled properly | Low |
| PAY-021 | Invoice access before payment | Payment | 1. Try to download invoice early | Blocked | High |
| PAY-022 | Leading whitespace in Card Number | Payment | 1. Enter spaces | Trimmed | Low |
| PAY-023 | Extremely long cardholder name | Payment | 1. Enter 100 char name | Handled safely | Low |
| PAY-024 | Retry after gateway decline | Payment | 1. Fail then resubmit | Processed properly | High |
| PAY-025 | Submit with no payment method | Payment | 1. Deselect all | Validation error | High |

---

## 13. Currency And Language Selection

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-001 | Currency selector updates displayed prices | None | 1. Change currency from the top navigation | Prices across the current page update to the selected currency | High |
| PREF-002 | Language selector updates interface text | None | 1. Change language from the top navigation | Interface text updates to the selected language | High |
| PREF-003 | Arabic or RTL language applies RTL layout | RTL language option is available | 1. Select Arabic or another RTL language | Page layout and text direction switch to RTL where applicable | Medium |
| PREF-008 | Currency format updates | Any page | 1. Change currency | Symbol and formatting change (e.g., $100 vs 100€) | Medium |
| PREF-009 | Search history language | Search | 1. Change language | Search history translates if applicable | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-005 | Unsupported preference value cannot be applied | None | 1. Attempt to select unavailable currency or language option | Invalid selection is not applied | Low |
| PREF-010 | Invalid language code in URL | URL bar | 1. Append ?lang=xx | Defaults to English | Low |
| PREF-011 | Invalid currency code in URL | URL bar | 1. Append ?curr=XXX | Defaults to default currency | Low |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-006 | Currency preference persists across page navigation | None | 1. Change currency<br>2. Navigate to another page | Selected currency remains active across navigation | Medium |
| PREF-007 | Authenticated preference persists after relogin | Logged in as user | 1. Change language or currency<br>2. Log out and log back in | Stored preference remains applied if profile persistence is supported | Low |
| PREF-012 | Switch language mid-booking | Booking | 1. Change lang on checkout | Session remains intact | Medium |
| PREF-013 | Rapid toggle language | Header | 1. Switch language quickly back and forth | UI handles switching | Low |
| PREF-014 | Cookie vs Profile scopes | Settings | 1. Switch auth/unauth | Resolves properly | Medium |
| PREF-015 | RTL layout with unsaved form | Forms | 1. Enter text then switch to Arabic | Form text persists | High |
| PREF-016 | Multi-tab preference sync | Browser | 1. Change in Tab 1, reload Tab 2 | Synced | Medium |
| PREF-017 | Unauthenticated Profile Preference block | URLs | 1. Access profile prefs direct | Redirect to login | High |

---

## 14. Search And Filters

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-001 | Filter sidebar controls displayed on listing pages | User is on a hotels, flights, tours, or cars listing page | 1. Review the listing page sidebar | Filter groups and sort controls are visible | High |
| FILTER-002 | Result count updates after applying filter | User is on a listing page with available filters | 1. Apply one or more filters | Result count updates to reflect the filtered result set | High |
| FILTER-003 | Active filter tag can be removed | One or more filters are active | 1. Remove an active filter tag | Corresponding filter is cleared and results refresh | Medium |
| FILTER-004 | Clear all filters resets listing | One or more filters are active | 1. Click "Clear All Filters" | All active filters are cleared and listing resets to the default state | Medium |
| FILTER-005 | Sorting control reorders results | User is on a listing page | 1. Select a different sort option | Result ordering updates according to the selected sort | Medium |
| FILTER-008 | Sort by Rating | Listing | 1. Sort by top rated | Highest rated show first | High |
| FILTER-009 | Text search filter | Listing | 1. Type in search bar | Results filter dynamically | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-006 | Filter combination returns no results | User is on a listing page | 1. Apply a restrictive combination of filters | Empty-state or zero-results feedback is displayed | Medium |
| FILTER-010 | Invalid text search | Listing | 1. Type symbols | No results found | Low |
| FILTER-011 | Filter error recovery | Listing | 1. Turn off network<br>2. Filter | Shows network error | Low |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-007 | Price or time range filter at extreme bounds | User is on a listing page with range sliders | 1. Move a range slider to the minimum or maximum boundary | Results update correctly at the selected extreme | Low |
| FILTER-012 | Select all filters | Listing | 1. Select every filter option | Very specific or no results | Low |
| FILTER-013 | Rapid filter clicking | Listing | 1. Click filters fast | UI handles requests properly | Low |
| FILTER-014 | Extremely long filter text | Listing | 1. Type long query | Results filter or handled | Low |
| FILTER-015 | Invalid Time Range End | Filter | 1. End time before start time | Rejected by UI | High |
| FILTER-016 | Zero-width range slider | Filter | 1. Move handles to exact same value | Processed | Medium |
| FILTER-017 | Cross slider handles | Filter | 1. Left handle past right | Blocked | High |
| FILTER-018 | Product specific filter validation | Filter | 1. Flights filter applied to Hotels | Handled safely | Low |
| FILTER-019 | Back button removes filters | Browser | 1. Apply then press back | Resets filters | Medium |

---

## 15. Reviews And Ratings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-001 | Aggregate ratings displayed on listing cards | User is on a hotel, tour, or car listing page | 1. Review listing cards | Rating score, label, and review count are displayed | High |
| REVIEW-002 | Review breakdown displayed on detail page | Hotel, tour, or car detail page is open | 1. Scroll to the reviews section | Aggregate score, category breakdown, and individual reviews are visible | High |
| REVIEW-003 | Submit review for completed booking | Logged in user has an eligible completed booking | 1. Open review submission flow<br>2. Enter valid ratings and comment<br>3. Submit review | Review is submitted successfully or queued for moderation | High |
| REVIEW-004 | Sort reviews | Detail page has multiple reviews | 1. Change review sort option | Review list updates according to selected order | Medium |
| REVIEW-008 | Edit review | My Reviews | 1. Click edit<br>2. Update | Review is updated | Medium |
| REVIEW-009 | Delete review | My Reviews | 1. Click delete | Review is removed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-005 | Review comment below minimum length | Logged in user is on review submission form | 1. Enter comment shorter than the minimum length<br>2. Submit review | Validation error is displayed | Medium |
| REVIEW-006 | Ineligible user attempts to submit review | Logged in user does not have a completed booking for the item | 1. Attempt to access or submit review form | Review submission is blocked | Medium |
| REVIEW-010 | Review with profanity | Review form | 1. Submit swear words | Filtered or blocked | High |
| REVIEW-011 | Empty rating | Review form | 1. Don't select stars | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-007 | Maximum allowed photo upload count | Logged in user is on review submission form | 1. Upload the maximum allowed number of photos<br>2. Submit review | Upload is accepted at the allowed boundary | Low |
| REVIEW-012 | Max review length | Review form | 1. Paste huge text | Blocked or truncated | Low |
| REVIEW-013 | Long photo upload | Review form | 1. Add very high res image | Resized or rejected gracefully | Low |
| REVIEW-014 | Rapid review submission | Review form | 1. Submit review fast | Handles debouncing | Low |
| REVIEW-015 | Post stay email link access | Auth | 1. Click email link unauth | Requires login | High |
| REVIEW-016 | Specific category rating missing | Review form | 1. Leave specific star empty | Validation error | Medium |
| REVIEW-017 | Same day review filter | Filter | 1. Start and end date equal | Handled properly | Low |
| REVIEW-018 | Far future date filter | Filter | 1. Filter reviews in future | Shows empty | Low |
| REVIEW-019 | Emoji and Unicode in feedback | Review form | 1. Use emojis | Preserved | Low |

---

## 16. Offers And Deals

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-001 | Offers page content displayed | None | 1. Open Offers page | Hero banner, category filters, destination controls, and offer cards are visible | High |
| OFFER-002 | Filter offers by category | Offers page is open | 1. Select a category tab or filter | Visible offers update to match selected category | Medium |
| OFFER-003 | Offer Book Now action applies deal | Valid offer exists | 1. Click "Book Now" on an offer | Offer is applied and user is redirected to relevant booking or listing flow | High |
| OFFER-004 | Newsletter subscription with valid email | Offers page is open | 1. Enter valid email<br>2. Click "Subscribe" | Subscription confirmation message is displayed | Medium |
| OFFER-008 | Share offer | Offers | 1. Click share | Share dialog opens | Low |
| OFFER-009 | Copy promo code | Offers | 1. Click copy code | Copied to clipboard | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-005 | Newsletter subscription with invalid email | Offers page is open | 1. Enter invalid email<br>2. Click "Subscribe" | Validation error is displayed | Medium |
| OFFER-006 | Expired offer cannot be applied | Expired offer exists | 1. Attempt to use expired offer | Offer is rejected or clearly marked as unavailable | Medium |
| OFFER-010 | Redeemed offer | Offers | 1. Try to use 1-time offer again | Validation error | High |
| OFFER-011 | Deal link manipulation | URL | 1. Change deal ID | 404 or redirect | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-007 | Offer validity date boundary | Offer expires today or at a known cut-off time | 1. Attempt to use the offer near expiration time | Offer acceptance or rejection matches the documented validity boundary | Low |
| OFFER-012 | Very large discount | Admin | 1. Create 99% off | Works as expected | Low |
| OFFER-013 | Multiple offers on page | Offers | 1. Load page with 100 offers | Paginates or loads efficiently | Low |
| OFFER-014 | Same day offer bounds | Filter | 1. Apply same day limit | Handled correctly | Low |
| OFFER-015 | Newsletter unicode email | Offers | 1. Invalid unicode email | Rejected | Medium |
| OFFER-016 | Long destination query filter | Filter | 1. 200+ char destination | Truncated safely | Low |
| OFFER-017 | Rapid apply promo clicks | Offers | 1. Click Book Now twice | Single application | High |
| OFFER-018 | Pre-filled search redirect cache | Redirect | 1. Back button returns | Preserves state | Medium |

---

## 17. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Logout from user dropdown | User is logged in | 1. Open user menu<br>2. Click "Logout" | Session ends and the home page shows Login and Signup links again | High |
| LOGOUT-003 | Logout from all devices | Profile | 1. Click 'Logout everywhere' | Other sessions terminated | Medium |
| LOGOUT-004 | Clear cookies | Browser | 1. Clear site data | User is logged out | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-002 | Access protected page after logout | User has logged out | 1. Attempt to open dashboard or booking-management URL | User is redirected to login page and cannot access protected content | High |
| LOGOUT-005 | Inactive session | Browser | 1. Leave open 24hrs | Auto logs out | Medium |
| LOGOUT-006 | Back button after logout | Browser | 1. Logout<br>2. Press back | Forced to login | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-007 | Rapid login/logout | Navbar | 1. Click in/out fast | Handled without crashing | Low |
| LOGOUT-008 | Mid-flight network request termination | Network | 1. Click logout while loading | Request aborts | High |
| LOGOUT-009 | Hidden unauthenticated button | Navbar | 1. Verify logout missing | Button omitted | Low |

---

## Test Summary

| Module | Total Tests | High Priority | Medium Priority | Low Priority |
|--------|-------------|---------------|-----------------|--------------|
| Home Page And Search | 25 | 9 | 7 | 9 |
| Registration | 24 | 12 | 4 | 8 |
| Login | 22 | 8 | 8 | 6 |
| Forgot Password | 19 | 10 | 5 | 4 |
| Hotels Search And Listing | 23 | 8 | 8 | 7 |
| Hotel Details And Booking | 20 | 8 | 6 | 6 |
| Flights Search And Booking | 23 | 10 | 7 | 6 |
| Tours Search And Booking | 20 | 7 | 7 | 6 |
| Cars Search And Booking | 21 | 10 | 6 | 5 |
| Visa Services | 20 | 8 | 6 | 6 |
| User Dashboard And Booking Management | 23 | 8 | 10 | 5 |
| Payment Processing | 25 | 13 | 6 | 6 |
| Currency And Language Selection | 17 | 4 | 6 | 7 |
| Search And Filters | 19 | 6 | 6 | 7 |
| Reviews And Ratings | 19 | 6 | 7 | 6 |
| Offers And Deals | 18 | 4 | 8 | 6 |
| Logout | 9 | 4 | 2 | 3 |
| **TOTAL** | **347** | **135** | **109** | **103** |
