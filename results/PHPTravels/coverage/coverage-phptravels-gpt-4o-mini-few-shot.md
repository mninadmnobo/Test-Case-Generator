# Test Coverage Report

**Ground Truth:** Phptravels GT v1.0  
**Generated Suite:** openai/gpt-4o-mini-few-shot-per-module — 250 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 347 |
| GT cases covered by GEN | ~142 |
| GT cases not covered by GEN | ~205 |
| **Overall coverage** | **40.9%** |
| GEN cases with no GT counterpart (extras) | ~40 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 25 | 12 | 13 | **48%** |
| Registration | 24 | 12 | 12 | **50%** |
| Login | 22 | 10 | 12 | **45%** |
| Forgot Password | 19 | 8 | 11 | **42%** |
| Hotels Search And Listing | 23 | 9 | 14 | **39%** |
| Hotel Details And Booking | 20 | 10 | 10 | **50%** |
| Flights Search And Booking | 23 | 9 | 14 | **39%** |
| Tours Search And Booking | 20 | 8 | 12 | **40%** |
| Cars Search And Booking | 21 | 9 | 12 | **43%** |
| Visa Services | 20 | 8 | 12 | **40%** |
| User Dashboard And Booking Management | 23 | 9 | 14 | **39%** |
| Payment Processing | 25 | 10 | 15 | **40%** |
| Currency And Language Selection | 17 | 7 | 10 | **41%** |
| Search And Filters | 19 | 7 | 12 | **37%** |
| Reviews And Ratings | 19 | 7 | 12 | **37%** |
| Offers And Deals | 18 | 4 | 14 | **22%** |
| Logout | 9 | 3 | 6 | **33%** |
| **Total** | **347** | **142** | **205** | **40.9%** |

---

## Missing Scenarios (Gaps)

*Note: The following explicitly documented GT test cases were absent from the generated suite. The few-shot prompt improved boundary testing but missed deep negative invariants.*

### Home Page And Search (4 missing)
- HOME-008 Flight search with required fields missing
- HOME-009 Invalid hotel date range
- HOME-024 Emoji characters in destination
- HOME-025 Very rapid double-click on Search

### Registration (4 missing)
- REG-020 Leading/trailing whitespace in email
- REG-021 Unicode characters in name
- REG-023 Rapid resubmission
- REG-024 Password differs only by whitespace

### Login (4 missing)
- LOGIN-009 Social Login - Google
- LOGIN-010 Social Login - Facebook
- LOGIN-019 Invalid CAPTCHA input
- LOGIN-020 Rapid consecutive fails

### Forgot Password (4 missing)
- FP-013 Very long email
- FP-015 Exact 24 hour link expiration
- FP-016 One unit past expiration
- FP-017 Link reuse attempt

### Hotels Search And Listing (5 missing)
- HOTEL-007 Invalid hotel date range from listing edit
- HOTEL-015 Invalid date modification
- HOTEL-019 Non-numeric min price input
- HOTEL-021 Same day check in and out
- HOTEL-022 Remove disabled filter

### Hotel Details And Booking (3 missing)
- HBOOK-011 Invalid date change in details
- HBOOK-018 Extremely long guest name
- HBOOK-019 Special characters in requests

### Flights Search And Booking (6 missing)
- FLIGHT-007 Passport expiry too soon
- FLIGHT-015 Past departure date
- FLIGHT-017 Same day return
- FLIGHT-020 Sort by non-sortable column
- FLIGHT-021 Return date before departure date
- FLIGHT-022 Passport expiry exactly on boundary

### Tours Search And Booking (5 missing)
- TOUR-016 Travelers sum exceeds UI rows
- TOUR-017 Unauthenticated tour booking
- TOUR-018 Budget Min equals Budget Max
- TOUR-019 Extremely long destination query
- TOUR-020 Removing all traveler entries

### Cars Search And Booking (4 missing)
- CAR-012 Drop-off before pick-up
- CAR-017 Same day pick up and drop off
- CAR-018 Non-numeric driver age
- CAR-019 Book Now without search precondition

### Visa Services (5 missing)
- VISA-014 Multiple document upload
- VISA-015 Extremely long applicant name
- VISA-017 Date of birth is today
- VISA-018 Date of birth in future
- VISA-019 Rapid resubmission

### User Dashboard And Booking Management (5 missing)
- UDB-007 Modify non-eligible booking
- UDB-008 Cancel non-eligible booking
- UDB-019 Cancel a Cancelled booking
- UDB-020 Download confirmation for Cancelled
- UDB-021 Race condition Cancel/Modify

### Payment Processing (4 missing)
- PAY-021 Invoice access before payment
- PAY-022 Leading whitespace in Card Number
- PAY-023 Extremely long cardholder name
- PAY-024 Retry after gateway decline

### Currency And Language Selection (4 missing)
- PREF-006 Currency preference persists across page navigation
- PREF-007 Authenticated preference persists after relogin
- PREF-015 RTL layout with unsaved form
- PREF-017 Unauthenticated Profile Preference block

### Search And Filters (4 missing)
- FILTER-007 Price or time range filter at extreme bounds
- FILTER-015 Invalid Time Range End
- FILTER-016 Zero-width range slider
- FILTER-017 Cross slider handles

### Reviews And Ratings (4 missing)
- REVIEW-005 Review comment below minimum length
- REVIEW-015 Post stay email link access
- REVIEW-016 Specific category rating missing
- REVIEW-018 Far future date filter

### Offers And Deals (4 missing)
- OFFER-007 Offer validity date boundary
- OFFER-014 Same day offer bounds
- OFFER-016 Long destination query filter
- OFFER-018 Pre-filled search redirect cache

### Logout (3 missing)
- LOGOUT-007 Rapid login/logout
- LOGOUT-008 Mid-flight network request termination
- LOGOUT-009 Hidden unauthenticated button

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~2 extra types)
- Check-in and check-out dates on the same day explicitly testing widget reset
- Flight maximum passenger count warning boundaries

### Registration (0 extra types)
- None

### Login (0 extra types)
- None

### Forgot Password (0 extra types)
- None

### Hotels Search And Listing (~2 extra types)
- Invalid number of rooms specified via manual override
- Invalid guest count inputs

### Hotel Details And Booking (~2 extra types)
- Special requests exceeding character limit constraints
- Stay date in the past via URL tampering

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

### Payment Processing (0 extra types)
- None

### Currency And Language Selection (0 extra types)
- None

### Search And Filters (0 extra types)
- None

### Reviews And Ratings (0 extra types)
- None

### Offers And Deals (0 extra types)
- None

### Logout (0 extra types)
- None
