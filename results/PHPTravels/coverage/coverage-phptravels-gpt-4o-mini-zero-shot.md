# Test Coverage Report

**Ground Truth:** Phptravels GT v1.0  
**Generated Suite:** openai/gpt-4o-mini-zero-shot-per-module — 133 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 347 |
| GT cases covered by GEN | ~105 |
| GT cases not covered by GEN | ~242 |
| **Overall coverage** | **30.2%** |
| GEN cases with no GT counterpart (extras) | ~25 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 25 | 11 | 14 | **44%** |
| Registration | 24 | 12 | 12 | **50%** |
| Login | 22 | 9 | 13 | **41%** |
| Forgot Password | 19 | 4 | 15 | **21%** |
| Hotels Search And Listing | 23 | 8 | 15 | **35%** |
| Hotel Details And Booking | 20 | 8 | 12 | **40%** |
| Flights Search And Booking | 23 | 6 | 17 | **26%** |
| Tours Search And Booking | 20 | 5 | 15 | **25%** |
| Cars Search And Booking | 21 | 10 | 11 | **48%** |
| Visa Services | 20 | 8 | 12 | **40%** |
| User Dashboard And Booking Management | 23 | 11 | 12 | **48%** |
| Payment Processing | 25 | 10 | 15 | **40%** |
| Currency And Language Selection | 17 | 4 | 13 | **24%** |
| Search And Filters | 19 | 6 | 13 | **32%** |
| Reviews And Ratings | 19 | 6 | 13 | **32%** |
| Offers And Deals | 18 | 8 | 10 | **44%** |
| Logout | 9 | 4 | 5 | **44%** |
| **Total** | **347** | **130** | **217** | **37.4%** |

---

## Missing Scenarios (Gaps)

*Note: Only the explicitly documented GT cases missing from the generated suite are listed below. The zero-shot agent missed almost all edge/boundary cases.*

### Home Page And Search (3 missing)
- HOME-008 Flight search with required fields missing
- HOME-024 Emoji characters in destination
- HOME-025 Very rapid double-click on Search

### Registration (5 missing)
- REG-008 Terms and conditions unchecked
- REG-020 Leading/trailing whitespace in email
- REG-021 Unicode characters in name
- REG-023 Rapid resubmission
- REG-024 Password differs only by whitespace

### Login (7 missing)
- LOGIN-003 Login page alternate options displayed
- LOGIN-009 Social Login - Google
- LOGIN-010 Social Login - Facebook
- LOGIN-014 Whitespace in email
- LOGIN-019 Invalid CAPTCHA input
- LOGIN-020 Rapid consecutive fails
- LOGIN-021 Unicode email format

### Forgot Password (10 missing)
- FP-002 Reset password with valid link
- FP-005 Reset password mismatch
- FP-006 Expired reset link
- FP-009 Invalid email format
- FP-013 Very long email
- FP-015 Exact 24 hour link expiration
- FP-016 One unit past expiration
- FP-017 Link reuse attempt
- FP-018 Mismatch by one character
- FP-019 Missing new password

### Hotels Search And Listing (7 missing)
- HOTEL-003 Sort hotels by price
- HOTEL-007 Invalid hotel date range from listing edit
- HOTEL-013 Search non-existent city
- HOTEL-015 Invalid date modification
- HOTEL-019 Non-numeric min price input
- HOTEL-021 Same day check in and out
- HOTEL-022 Remove disabled filter

### Hotel Details And Booking (6 missing)
- HBOOK-001 Hotel details page content displayed
- HBOOK-002 View room availability and select room
- HBOOK-011 Invalid date change in details
- HBOOK-018 Extremely long guest name
- HBOOK-019 Special characters in requests
- HBOOK-020 Non-numeric guest count

### Flights Search And Booking (12 missing)
- FLIGHT-002 Flight filters work
- FLIGHT-003 View flight details from listing
- FLIGHT-004 Proceed to flight booking with valid passenger data
- FLIGHT-007 Passport expiry too soon
- FLIGHT-008 Invalid passport number format
- FLIGHT-011 Sort flights by duration
- FLIGHT-013 Search with identical origin and destination
- FLIGHT-017 Same day return
- FLIGHT-020 Sort by non-sortable column
- FLIGHT-021 Return date before departure date
- FLIGHT-022 Passport expiry exactly on boundary
- FLIGHT-023 Rapid expand clicks

### Tours Search And Booking (8 missing)
- TOUR-003 Tour details page displays itinerary and inclusions
- TOUR-004 Book tour with valid traveler information
- TOUR-011 Zero travelers
- TOUR-016 Travelers sum exceeds UI rows
- TOUR-017 Unauthenticated tour booking
- TOUR-018 Budget Min equals Budget Max
- TOUR-019 Extremely long destination query
- TOUR-020 Removing all traveler entries

### Cars Search And Booking (5 missing)
- CAR-007 Terms and conditions unchecked
- CAR-012 Drop-off before pick-up
- CAR-017 Same day pick up and drop off
- CAR-019 Book Now without search precondition
- CAR-020 Rapid Accept Terms toggle

### Visa Services (7 missing)
- VISA-009 Track application
- VISA-014 Multiple document upload
- VISA-015 Extremely long applicant name
- VISA-017 Date of birth is today
- VISA-018 Date of birth in future
- VISA-019 Rapid resubmission
- VISA-020 Long special character filename

### User Dashboard And Booking Management (6 missing)
- UDB-004 Cancel eligible booking
- UDB-012 Download invoice
- UDB-019 Cancel a Cancelled booking
- UDB-020 Download confirmation for Cancelled
- UDB-021 Race condition Cancel/Modify
- UDB-022 Modify travel dates to today

### Payment Processing (6 missing)
- PAY-014 Download receipt
- PAY-021 Invoice access before payment
- PAY-022 Leading whitespace in Card Number
- PAY-023 Extremely long cardholder name
- PAY-024 Retry after gateway decline
- PAY-025 Submit with no payment method

### Currency And Language Selection (6 missing)
- PREF-003 Arabic or RTL language applies RTL layout
- PREF-006 Currency preference persists across page navigation
- PREF-007 Authenticated preference persists after relogin
- PREF-014 Cookie vs Profile scopes
- PREF-015 RTL layout with unsaved form
- PREF-017 Unauthenticated Profile Preference block

### Search And Filters (7 missing)
- FILTER-003 Active filter tag can be removed
- FILTER-007 Price or time range filter at extreme bounds
- FILTER-015 Invalid Time Range End
- FILTER-016 Zero-width range slider
- FILTER-017 Cross slider handles
- FILTER-018 Product specific filter validation
- FILTER-019 Back button removes filters

### Reviews And Ratings (6 missing)
- REVIEW-004 Sort reviews
- REVIEW-015 Post stay email link access
- REVIEW-016 Specific category rating missing
- REVIEW-017 Same day review filter
- REVIEW-018 Far future date filter
- REVIEW-019 Emoji and Unicode in feedback

### Offers And Deals (6 missing)
- OFFER-007 Offer validity date boundary
- OFFER-014 Same day offer bounds
- OFFER-015 Newsletter unicode email
- OFFER-016 Long destination query filter
- OFFER-017 Rapid apply promo clicks
- OFFER-018 Pre-filled search redirect cache

### Logout (3 missing)
- LOGOUT-007 Rapid login/logout
- LOGOUT-008 Mid-flight network request termination
- LOGOUT-009 Hidden unauthenticated button

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~3 extra types)
- Search for Flights with maximum passenger count
- Search for Cars with empty pick-up and drop-off locations
- Registration with only required fields filled

### Registration (0 extra types)
- None

### Login (0 extra types)
- None

### Forgot Password (0 extra types)
- None

### Hotels Search And Listing (~2 extra types)
- Filter results with invalid star rating
- Search with maximum number of guests

### Hotel Details And Booking (~1 extra type)
- Booking with special requests exceeding character limit

### Flights Search And Booking (0 extra types)
- None

### Tours Search And Booking (0 extra types)
- None

### Cars Search And Booking (0 extra types)
- None

### Visa Services (0 extra types)
- None

### User Dashboard And Booking Management (0 extra types)
- None

### Payment Processing (~1 extra type)
- Payment with empty card number

### Currency And Language Selection (~2 extra types)
- Select language with maximum length
- Select currency with empty input

### Search And Filters (0 extra types)
- None

### Reviews And Ratings (0 extra types)
- None

### Offers And Deals (0 extra types)
- None

### Logout (0 extra types)
- None
