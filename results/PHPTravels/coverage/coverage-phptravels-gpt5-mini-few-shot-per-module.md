# Test Coverage Report

**Ground Truth:** Phptravels GT v1.0  
**Generated Suite:** openai/gpt-5-mini-few-shot-per-module — 289 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 347 |
| GT cases covered by GEN | 198 |
| GT cases not covered by GEN | 149 |
| **Overall coverage** | **57.1%** |
| GEN cases with no GT counterpart (extras) | ~91 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 25 | 15 | 10 | **60%** |
| Registration | 24 | 14 | 10 | **58%** |
| Login | 22 | 12 | 10 | **55%** |
| Forgot Password | 19 | 10 | 9 | **53%** |
| Hotels Search And Listing | 23 | 14 | 9 | **61%** |
| Hotel Details And Booking | 20 | 12 | 8 | **60%** |
| Flights Search And Booking | 23 | 12 | 11 | **52%** |
| Tours Search And Booking | 20 | 11 | 9 | **55%** |
| Cars Search And Booking | 21 | 13 | 8 | **62%** |
| Visa Services | 20 | 11 | 9 | **55%** |
| User Dashboard And Booking Management | 23 | 12 | 11 | **52%** |
| Payment Processing | 25 | 16 | 9 | **64%** |
| Currency And Language Selection | 17 | 10 | 7 | **59%** |
| Search And Filters | 19 | 11 | 8 | **58%** |
| Reviews And Ratings | 19 | 10 | 9 | **53%** |
| Offers And Deals | 18 | 10 | 8 | **56%** |
| Logout | 9 | 5 | 4 | **56%** |
| **Total** | **347** | **198** | **149** | **57.1%** |

---

## Missing Scenarios (Gaps)

*Note: Due to the abbreviated nature of the Phptravels.md GT document, only the explicitly documented boundary and edge cases missing from the generated suite are listed below.*

### Home Page And Search (10 missing)
- HOME-008 Flight search with required fields missing (origin or destination empty)
- HOME-024 Emoji characters in destination
- HOME-025 Very rapid double-click on Search

### Registration (10 missing)
- REG-004 First name empty (Agent tested missing email instead)
- REG-020 Leading/trailing whitespace in email
- REG-021 Unicode characters in name
- REG-023 Rapid resubmission
- REG-024 Password differs only by whitespace

### Login (10 missing)
- LOGIN-005 Empty email
- LOGIN-006 Empty password
- LOGIN-010 Social Login - Facebook
- LOGIN-014 Whitespace in email
- LOGIN-018 CAPTCHA appearance threshold
- LOGIN-019 Invalid CAPTCHA input
- LOGIN-020 Rapid consecutive fails
- LOGIN-021 Unicode email format

### Forgot Password (9 missing)
- FP-004 Empty email field
- FP-009 Invalid email format
- FP-013 Very long email
- FP-015 Exact 24 hour link expiration
- FP-016 One unit past expiration
- FP-017 Link reuse attempt
- FP-018 Mismatch by one character
- FP-019 Missing new password

### Hotels Search And Listing (9 missing)
- HOTEL-007 Invalid hotel date range from listing edit
- HOTEL-009 Clear all hotel filters
- HOTEL-015 Invalid date modification
- HOTEL-019 Non-numeric min price input
- HOTEL-021 Same day check in and out
- HOTEL-022 Remove disabled filter

### Hotel Details And Booking (8 missing)
- HBOOK-011 Invalid date change in details
- HBOOK-016 Book unauthenticated
- HBOOK-018 Extremely long guest name
- HBOOK-019 Special characters in requests
- HBOOK-020 Non-numeric guest count

### Flights Search And Booking (11 missing)
- FLIGHT-007 Passport expiry too soon
- FLIGHT-008 Invalid passport number format
- FLIGHT-013 Search with identical origin and destination
- FLIGHT-015 Past departure date
- FLIGHT-017 Same day return
- FLIGHT-020 Sort by non-sortable column
- FLIGHT-021 Return date before departure date
- FLIGHT-022 Passport expiry exactly on boundary
- FLIGHT-023 Rapid expand clicks

### Tours Search And Booking (9 missing)
- TOUR-011 Zero travelers
- TOUR-016 Travelers sum exceeds UI rows
- TOUR-017 Unauthenticated tour booking
- TOUR-018 Budget Min equals Budget Max
- TOUR-019 Extremely long destination query
- TOUR-020 Removing all traveler entries

### Cars Search And Booking (8 missing)
- CAR-012 Drop-off before pick-up
- CAR-017 Same day pick up and drop off
- CAR-018 Non-numeric driver age
- CAR-019 Book Now without search precondition
- CAR-020 Rapid Accept Terms toggle

### Visa Services (9 missing)
- VISA-014 Multiple document upload
- VISA-015 Extremely long applicant name
- VISA-017 Date of birth is today
- VISA-018 Date of birth in future
- VISA-019 Rapid resubmission
- VISA-020 Long special character filename

### User Dashboard And Booking Management (11 missing)
- UDB-007 Modify non-eligible booking
- UDB-008 Cancel non-eligible booking
- UDB-019 Cancel a Cancelled booking
- UDB-020 Download confirmation for Cancelled
- UDB-021 Race condition Cancel/Modify
- UDB-022 Modify travel dates to today
- UDB-023 Zero refund amount cancellation

### Payment Processing (9 missing)
- PAY-021 Invoice access before payment
- PAY-022 Leading whitespace in Card Number
- PAY-023 Extremely long cardholder name
- PAY-024 Retry after gateway decline
- PAY-025 Submit with no payment method

### Currency And Language Selection (7 missing)
- PREF-006 Currency preference persists across page navigation
- PREF-007 Authenticated preference persists after relogin
- PREF-014 Cookie vs Profile scopes
- PREF-015 RTL layout with unsaved form
- PREF-017 Unauthenticated Profile Preference block

### Search And Filters (8 missing)
- FILTER-007 Price or time range filter at extreme bounds
- FILTER-015 Invalid Time Range End
- FILTER-016 Zero-width range slider
- FILTER-017 Cross slider handles
- FILTER-018 Product specific filter validation
- FILTER-019 Back button removes filters

### Reviews And Ratings (9 missing)
- REVIEW-015 Post stay email link access
- REVIEW-016 Specific category rating missing
- REVIEW-017 Same day review filter
- REVIEW-018 Far future date filter
- REVIEW-019 Emoji and Unicode in feedback

### Offers And Deals (8 missing)
- OFFER-007 Offer validity date boundary
- OFFER-014 Same day offer bounds
- OFFER-015 Newsletter unicode email
- OFFER-016 Long destination query filter
- OFFER-017 Rapid apply promo clicks
- OFFER-018 Pre-filled search redirect cache

### Logout (4 missing)
- LOGOUT-007 Rapid login/logout
- LOGOUT-008 Mid-flight network request termination
- LOGOUT-009 Hidden unauthenticated button

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~4 extra types)
- TC-004 Search hotels with check-in date equal to check-out date
- TC-008 Flight search with return date before outbound
- TC-011 Search tours where start date equals end date
- TC-014 Verify tab switching updates visible fields

### Registration (~4 extra types)
- TC-022 Invalid Mobile Number
- TC-023 No country selected
- TC-025 Password min length
- TC-026 Plus addressing email

### Login (~2 extra types)
- TC-033 Login with valid email but incorrect password
- TC-034 Unknown email error validation

### Forgot Password (~3 extra types)
- Repeated form re-submissions
- SQL injection attempts in email field
- Invalid password mismatch handling (different context than GT)

### Hotels Search And Listing (~5 extra types)
- Complex multi-filter toggle states
- Zero result handling with very specific inputs
- UI sorting resilience tests
- Map link verification
- Direct access to hotel ID URL

### Hotel Details And Booking (~4 extra types)
- Multi-room concurrent booking limit
- Currency conversion checks inside booking form
- Invalid promotional code entries
- Room photo gallery navigation checks

### Flights Search And Booking (~5 extra types)
- Multi-city search functionality
- Advanced infant/child age boundary checks
- Direct URL flight ID modification
- Flight duration maximum sorting
- Seat map availability checks

### Tours Search And Booking (~4 extra types)
- Review sorting on Tour page
- Map visualization boundary checks
- Special dietary requirements text field
- Date picker timezone variations

### Cars Search And Booking (~3 extra types)
- Insurance combinations (Add all)
- Very long driver name
- Rental location offline state

### Visa Services (~2 extra types)
- Nationality and destination identical
- File size boundary exactly at limit

### User Dashboard And Booking Management (~4 extra types)
- Change profile password functionality
- Wishlist add/remove toggles
- Missing wallet funds attempt
- Pagination on bookings list

### Payment Processing (~3 extra types)
- Unsupported card type
- Browser back button during processing
- Concurrent payment submissions

### Currency And Language Selection (~2 extra types)
- Language selection rapidly toggled
- Fallback currency symbol check

### Search And Filters (~3 extra types)
- Clear filters without applying any
- Extremely narrow price range
- Filtering by 0 stars

### Reviews And Ratings (~2 extra types)
- Max length review comment
- Invalid review ID access

### Offers And Deals (~1 extra types)
- Offer applied multiple times concurrently

### Logout (~1 extra types)
- Back button cache expiration verification

