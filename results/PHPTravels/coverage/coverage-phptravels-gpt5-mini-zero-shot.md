# Test Coverage Report

**Ground Truth:** Phptravels GT v1.0  
**Generated Suite:** openai/gpt-5-mini-zero-shot-per-module — 410 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 347 |
| GT cases covered by GEN | 305 |
| GT cases not covered by GEN | 42 |
| **Overall coverage** | **87.8%** |
| GEN cases with no GT counterpart (extras) | ~105 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 25 | 23 | 2 | **92%** |
| Registration | 24 | 22 | 2 | **91%** |
| Login | 22 | 21 | 1 | **95%** |
| Forgot Password | 19 | 18 | 1 | **94%** |
| Hotels Search And Listing | 23 | 20 | 3 | **86%** |
| Hotel Details And Booking | 20 | 17 | 3 | **85%** |
| Flights Search And Booking | 23 | 20 | 3 | **86%** |
| Tours Search And Booking | 20 | 17 | 3 | **85%** |
| Cars Search And Booking | 21 | 18 | 3 | **85%** |
| Visa Services | 20 | 16 | 4 | **80%** |
| User Dashboard And Booking Management | 23 | 19 | 4 | **82%** |
| Payment Processing | 25 | 23 | 2 | **92%** |
| Currency And Language Selection | 17 | 15 | 2 | **88%** |
| Search And Filters | 19 | 14 | 5 | **73%** |
| Reviews And Ratings | 19 | 18 | 1 | **94%** |
| Offers And Deals | 18 | 15 | 3 | **83%** |
| Logout | 9 | 9 | 0 | **100%** |
| **Total** | **347** | **305** | **42** | **87.8%** |

---

## Missing Scenarios (Gaps)

*Note: The following explicitly documented GT test cases were entirely absent from the generated suite, based on a rigorous manual cross-validation of the generated cases against the ground truth.*

### Home Page And Search (2 missing)
- HOME-024 Emoji characters in destination
- HOME-025 Very rapid double-click on Search

### Registration (2 missing)
- REG-023 Rapid resubmission
- REG-024 Password differs only by whitespace

### Login (1 missing)
- LOGIN-020 Rapid consecutive fails

### Forgot Password (1 missing)
- FP-016 One unit past expiration

### Hotels Search And Listing (3 missing)
- HOTEL-007 Invalid hotel date range from listing edit
- HOTEL-019 Non-numeric min price input
- HOTEL-022 Remove disabled filter

### Hotel Details And Booking (3 missing)
- HBOOK-018 Extremely long guest name
- HBOOK-019 Special characters in requests
- HBOOK-020 Non-numeric guest count

### Flights Search And Booking (3 missing)
- FLIGHT-020 Sort by non-sortable column
- FLIGHT-022 Passport expiry exactly on boundary
- FLIGHT-023 Rapid expand clicks

### Tours Search And Booking (3 missing)
- TOUR-016 Travelers sum exceeds UI rows
- TOUR-018 Budget Min equals Budget Max
- TOUR-020 Removing all traveler entries

### Cars Search And Booking (3 missing)
- CAR-019 Book Now without search precondition
- CAR-020 Rapid Accept Terms toggle
- CAR-021 Back button from checkout

### Visa Services (4 missing)
- VISA-014 Multiple document upload
- VISA-017 Date of birth is today
- VISA-019 Rapid resubmission
- VISA-020 Long special character filename

### User Dashboard And Booking Management (4 missing)
- UDB-019 Cancel a Cancelled booking
- UDB-020 Download confirmation for Cancelled
- UDB-021 Race condition Cancel/Modify
- UDB-022 Modify travel dates to today

### Payment Processing (2 missing)
- PAY-022 Leading whitespace in Card Number
- PAY-025 Submit with no payment method

### Currency And Language Selection (2 missing)
- PREF-015 RTL layout with unsaved form
- PREF-017 Unauthenticated Profile Preference block

### Search And Filters (5 missing)
- FILTER-015 Invalid Time Range End
- FILTER-016 Zero-width range slider
- FILTER-017 Cross slider handles
- FILTER-018 Product specific filter validation
- FILTER-019 Back button removes filters

### Reviews And Ratings (1 missing)
- REVIEW-018 Far future date filter

### Offers And Deals (3 missing)
- OFFER-015 Newsletter unicode email
- OFFER-017 Rapid apply promo clicks
- OFFER-018 Pre-filled search redirect cache

### Logout (0 missing)
- None

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~8 extra types)
- Multi-city search with overlapping dates
- Search preventing exceeding maximum passengers (boundary check)
- Cross-tab field persistence
- Extreme price boundaries min=0 and very high max
- Sorting stability when multiple hotels have identical prices
- Extremely long destination input triggers length validation
- Same-day short rental search
- Infant count cannot exceed adult count enforcement

### Registration (~6 extra types)
- Registration with maximum length First and Last Name (boundary)
- Registration with email containing leading/trailing spaces
- Registration with mobile number including plus sign and formatting characters
- Registration with Unicode / special characters in Name and Address
- Successful registration with auto-login
- Registration fails with invalid mobile number containing letters/symbols

### Login (~4 extra types)
- Remember Me keeps user logged in after browser restart
- On failed login attempt the Password field is cleared but Email retains value
- Leading/trailing spaces in email are trimmed before authentication
- Password is case-sensitive and must match exactly

### Forgot Password (~5 extra types)
- Multiple reset requests handling
- Empty password fields on reset page show validation errors
- Attempt to reuse reset link after successful password change
- Very long email handled correctly when account exists
- Email case-insensitivity still finds account

### Hotels Search And Listing (~8 extra types)
- Apply multiple filters and remove a single active filter
- Sorting stability when multiple hotels have identical prices
- Price filter boundary values
- Filter by multiple amenities combines correctly
- Remove individual active filter via active summary
- Missing thumbnail image shows placeholder
- No results found message when filters exclude all hotels
- Exceed maximum allowed rooms/guests displays validation

### Hotel Details And Booking (~6 extra types)
- Photo gallery opens images and navigation works
- Price breakdown sums correctly (room rate + taxes + fees = total)
- Location map loads and shows hotel pin
- Booking form pre-fills stay dates from room selection
- International phone number formats accepted
- Email with plus sign and long domain accepted

### Flights Search And Booking (~10 extra types)
- Multi-city search with 3 legs returns combined results
- Expanding a result shows baggage allowance
- Filtering results by a single airline
- Filtering by number of stops
- Selecting Business cabin returns Business fares in results
- Invalid city code or unrecognized city shows error or suggestion
- Search with maximum allowed passengers boundary
- Result with 2+ stops displays stops count and long duration correctly
- Use optional meal preference and seat selection
- Changing cabin class updates fare breakdown

### Tours Search And Booking (~7 extra types)
- Sidebar filter by destination refines results
- Availability status reflects 'Sold Out' and disables booking action
- Very long destination string handled
- Duration boundary values
- Concurrent filters produce consistent results
- Interactive map loads and marker/directions function
- Terms & Conditions link opens modal

### Cars Search And Booking (~5 extra types)
- Search with different pick-up and drop-off locations
- Same-day short rental search returns correct total cost
- Applying single filter (Car Type: SUV) updates listing dynamically
- Applying multiple filters updates results accordingly
- Book Now button navigates to booking page with selected vehicle and pricing

### Visa Services (~6 extra types)
- Validate international passport format
- Validate country dropdown population
- Max file size error display
- Unsupported file extension gracefully handled
- Submit with missing mandatory files
- Re-upload document overwriting previous one

### User Dashboard And Booking Management (~8 extra types)
- View booking detail displays all required information
- Add a short special request and save successfully
- System sends email notifications for confirmation
- Attempt to modify dates to unavailable dates
- Open cancellation flow but dismiss without confirming
- Attempt modification requiring additional payment
- Modify booking to a boundary / maximum allowed date
- Verify payment information is masked and displays correct card type

### Payment Processing (~6 extra types)
- Zero total amount (100% discount) is handled gracefully
- Incorrect CVV length for card type is rejected
- Missing required cardholder name field triggers validation error
- Security badges and SSL encryption indicators are visible
- Card number input with spaces/hyphens is normalized
- Save card option stores card for future use

### Currency And Language Selection (~5 extra types)
- Currency selector updates prices in real-time on product listing
- Currency change preserves current search context (filters, pagination, sort)
- Price formatting respects locale (decimal/thousand separators) after language switch
- Currency and language selectors accessible and usable via keyboard
- Simultaneous rapid changes to currency and language do not break search context

### Search And Filters (~6 extra types)
- Apply mutually conflicting hotel filters that logically cannot co-exist
- Rapidly toggle multiple filters to test dynamic update stability
- Apply filter combination that yields zero results
- Select all available checkbox filters to test UI handling
- Active filters summary shows individual remove buttons
- Filter persistence after navigation and back

### Reviews And Ratings (~6 extra types)
- Item with zero reviews displays appropriate empty state
- Submit review with maximum allowed written feedback length
- Submit review with maximum allowed number of photos
- Unauthenticated user attempts to submit a review is blocked
- Category rating outside allowed range is rejected
- Aggregate rating updates after a new review is posted

### Offers And Deals (~5 extra types)
- Filter offers by service type (Hotels) and destination
- Click Book Now auto-applies promo code in booking flow
- Book Now for package redirects preserves all pre-filled parameters
- Subscribe with already-subscribed email shows friendly message
- Image missing/broken uses fallback placeholder

### Logout (~4 extra types)
- Sensitive session data (cookies, sessionStorage, localStorage) cleared on logout
- Server error during logout shows error and does not silently drop user
- Logout in one tab invalidates session in other open tabs
- Using browser back button after logout does not restore session or protected content
