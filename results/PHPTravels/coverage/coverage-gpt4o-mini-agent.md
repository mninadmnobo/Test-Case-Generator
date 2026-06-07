# Test Coverage Report

**Ground Truth:** PHPTravels GT v1.0  
**Generated Suite:** openai/gpt-4o-mini — 318 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 178 |
| GT cases covered by GEN | 81 |
| GT cases not covered by GEN | 97 |
| **Overall coverage** | **45.5%** |
| GEN cases with no GT counterpart (extras) | ~237 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 9 | 8 | 1 | **88.9%** |
| Registration | 10 | 6 | 4 | **60.0%** |
| Login | 12 | 6 | 6 | **50.0%** |
| Forgot Password | 13 | 8 | 5 | **61.5%** |
| Hotels Search And Listing | 12 | 4 | 8 | **33.3%** |
| Hotel Details And Booking | 10 | 5 | 5 | **50.0%** |
| Flights Search And Booking | 15 | 3 | 12 | **20.0%** |
| Tours Search And Booking | 10 | 3 | 7 | **30.0%** |
| Cars Search And Booking | 11 | 4 | 7 | **36.4%** |
| Visa Services | 11 | 5 | 6 | **45.5%** |
| User Dashboard And Booking Management | 12 | 6 | 6 | **50.0%** |
| Payment Processing | 11 | 6 | 5 | **54.5%** |
| Currency And Language Selection | 8 | 3 | 5 | **37.5%** |
| Search And Filters | 10 | 3 | 7 | **30.0%** |
| Reviews And Ratings | 9 | 4 | 5 | **44.4%** |
| Offers And Deals | 10 | 4 | 6 | **40.0%** |
| Logout | 5 | 3 | 2 | **60.0%** |
| **Total** | **178** | **81** | **97** | **45.5%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Home Page And Search (1 missing)
- HOME-025 Very rapid double-click on Search

### Registration (4 missing)
- REG-007 Duplicate email
- REG-020 Leading/trailing whitespace in email
- REG-023 Rapid resubmission
- REG-024 Password differs only by whitespace

### Login (6 missing)
- LOGIN-003 Login page alternate options displayed
- LOGIN-009 Social Login - Google
- LOGIN-010 Social Login - Facebook
- LOGIN-014 Whitespace in email
- LOGIN-018 CAPTCHA appearance threshold
- LOGIN-019 Invalid CAPTCHA input

### Forgot Password (5 missing)
- FP-013 Very long email
- FP-015 Exact 24 hour link expiration
- FP-016 One unit past expiration
- FP-017 Link reuse attempt
- FP-018 Mismatch by one character

### Hotels Search And Listing (8 missing)
- HOTEL-001 Hotel listing page displays search summary and results count
- HOTEL-002 Hotel cards display expected content
- HOTEL-003 Sort hotels by price
- HOTEL-004 Filter hotels by star rating or facilities
- HOTEL-013 Search non-existent city
- HOTEL-009 Clear all hotel filters
- HOTEL-019 Non-numeric min price input
- HOTEL-022 Remove disabled filter

### Hotel Details And Booking (5 missing)
- HBOOK-001 Hotel details page content displayed
- HBOOK-002 View room availability and select room
- HBOOK-007 Special requests text boundary
- HBOOK-019 Special characters in requests
- HBOOK-020 Non-numeric guest count

### Flights Search And Booking (12 missing)
- FLIGHT-001 Flight listing displays itinerary cards
- FLIGHT-002 Flight filters work
- FLIGHT-003 View flight details from listing
- FLIGHT-011 Sort flights by duration
- FLIGHT-007 Passport expiry too soon
- FLIGHT-008 Invalid passport number format
- FLIGHT-013 Search with identical origin and destination
- FLIGHT-017 Same day return
- FLIGHT-020 Sort by non-sortable column
- FLIGHT-021 Return date before departure date
- FLIGHT-022 Passport expiry exactly on boundary
- FLIGHT-023 Rapid expand clicks

### Tours Search And Booking (7 missing)
- TOUR-001 Tour listing cards displayed
- TOUR-002 Filter tours by destination or type
- TOUR-003 Tour details page displays itinerary and inclusions
- TOUR-011 Zero travelers
- TOUR-016 Travelers sum exceeds UI rows
- TOUR-018 Budget Min equals Budget Max
- TOUR-020 Removing all traveler entries

### Cars Search And Booking (7 missing)
- CAR-001 Car listing cards displayed
- CAR-003 Add insurance and extras to booking
- CAR-010 Filter by transmission
- CAR-007 Terms and conditions unchecked
- CAR-018 Non-numeric driver age
- CAR-019 Book Now without search precondition
- CAR-020 Rapid Accept Terms toggle

### Visa Services (6 missing)
- VISA-009 Track application
- VISA-014 Multiple document upload
- VISA-017 Date of birth is today
- VISA-018 Date of birth in future
- VISA-019 Rapid resubmission
- VISA-020 Long special character filename

### User Dashboard And Booking Management (6 missing)
- UDB-001 Dashboard sections displayed
- UDB-019 Cancel a Cancelled booking
- UDB-020 Download confirmation for Cancelled
- UDB-021 Race condition Cancel/Modify
- UDB-022 Modify travel dates to today
- UDB-023 Zero refund amount cancellation

### Payment Processing (5 missing)
- PAY-014 Download receipt
- PAY-010 Payment declined or insufficient funds
- PAY-021 Invoice access before payment
- PAY-022 Leading whitespace in Card Number
- PAY-024 Retry after gateway decline

### Currency And Language Selection (5 missing)
- PREF-006 Currency preference persists across page navigation
- PREF-007 Authenticated preference persists after relogin
- PREF-014 Cookie vs Profile scopes
- PREF-015 RTL layout with unsaved form
- PREF-017 Unauthenticated Profile Preference block

### Search And Filters (7 missing)
- FILTER-001 Filter sidebar controls displayed on listing pages
- FILTER-003 Active filter tag can be removed
- FILTER-015 Invalid Time Range End
- FILTER-016 Zero-width range slider
- FILTER-017 Cross slider handles
- FILTER-018 Product specific filter validation
- FILTER-019 Back button removes filters

### Reviews And Ratings (5 missing)
- REVIEW-004 Sort reviews
- REVIEW-005 Review comment below minimum length
- REVIEW-015 Post stay email link access
- REVIEW-017 Same day review filter
- REVIEW-018 Far future date filter

### Offers And Deals (6 missing)
- OFFER-002 Filter offers by category
- OFFER-005 Newsletter subscription with invalid email
- OFFER-007 Offer validity date boundary
- OFFER-016 Long destination query filter
- OFFER-017 Rapid apply promo clicks
- OFFER-018 Pre-filled search redirect cache

### Logout (2 missing)
- LOGOUT-007 Rapid login/logout
- LOGOUT-008 Mid-flight network request termination

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~18 extra types)
- Heavy negative testing around leaving required search fields blank across all tabs.
- Date ordering boundaries (Check-Out one day before Check-In).

### Registration (~11 extra types)
- Extensive blank field permutations (First Name, Last Name, Mobile Number blank).
- Granular email format and password matching bounds testing.

### Login (~6 extra types)
- Basic negative permutations for missing passwords, formats, and empty strings.

### Forgot Password (~8 extra types)
- Negative input edge cases for Confirm Password missing/mismatching.

### Hotels Search And Listing (~10 extra types)
- Combinations of leaving guest count, check-in, and check-out fields blank explicitly.

### Hotel Details And Booking (~10 extra types)
- Exhaustive empty field permutations for booking details (Stay Dates, Phone Number, Names).

### Flights Search And Booking (~25 extra types)
- Heavy missing field variations across search form and passenger forms.
- Maximum passenger count boundary constraints (hitting and exceeding limit).

### Tours Search And Booking (~25 extra types)
- Exhaustive blank submission attempts for booking fields.
- Minimum required input tests for various date and numeric bounds.

### Cars Search And Booking (~22 extra types)
- Variations on missing license numbers, countries, and email fields.
- Legal driving age boundary variations.

### Visa Services (~15 extra types)
- Heavy blank testing for dropdown fields (Nationality, Country) and applicant details.

### User Dashboard And Booking Management (~22 extra types)
- Attempting dashboard actions with invalid references.
- Missing UI/flow state validations (e.g. download invoice when no bookings exist).

### Payment Processing (~13 extra types)
- Detailed field permutations for missing CVV, Expiry, and Name.
- Supported vs unsupported payment type variations.

### Currency And Language Selection (~11 extra types)
- Exhaustive list of explicit currency/language selection variations (JPY, GBP, Spanish, French).

### Search And Filters (~21 extra types)
- Trying to apply filters without making a selection (e.g., Star ratings blank).

### Reviews And Ratings (~12 extra types)
- Leaving exact reviewer details blank (Country, Name, Dates).
- Surpassing maximum allowed entries for Category Ratings.

### Offers And Deals (~6 extra types)
- Edge case submission lengths for email strings.

### Logout (~2 extra types)
- Attempt to logout when already logged out.
