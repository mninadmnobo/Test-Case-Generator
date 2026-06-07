# Test Coverage Report

**Ground Truth:** PHPTravels GT v1.0  
**Generated Suite:** openai/gpt-5-mini — 394 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 178 |
| GT cases covered by GEN | 158 |
| GT cases not covered by GEN | 20 |
| **Overall coverage** | **88.8%** |
| GEN cases with no GT counterpart (extras) | ~236 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Home Page And Search | 9 | 7 | 2 | **77.8%** |
| Registration | 10 | 10 | 0 | **100.0%** |
| Login | 12 | 12 | 0 | **100.0%** |
| Forgot Password | 13 | 12 | 1 | **92.3%** |
| Hotels Search And Listing | 12 | 10 | 2 | **83.3%** |
| Hotel Details And Booking | 10 | 8 | 2 | **80.0%** |
| Flights Search And Booking | 15 | 10 | 5 | **66.7%** |
| Tours Search And Booking | 10 | 9 | 1 | **90.0%** |
| Cars Search And Booking | 11 | 11 | 0 | **100.0%** |
| Visa Services | 11 | 10 | 1 | **90.9%** |
| User Dashboard And Booking Management | 12 | 11 | 1 | **91.7%** |
| Payment Processing | 11 | 11 | 0 | **100.0%** |
| Currency And Language Selection | 8 | 8 | 0 | **100.0%** |
| Search And Filters | 10 | 9 | 1 | **90.0%** |
| Reviews And Ratings | 9 | 7 | 2 | **77.8%** |
| Offers And Deals | 10 | 9 | 1 | **90.0%** |
| Logout | 5 | 4 | 1 | **80.0%** |
| **Total** | **178** | **158** | **20** | **88.8%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Home Page And Search (2 missing)
- HOME-009 Invalid hotel date range
- HOME-025 Very rapid double-click on Search

### Forgot Password (1 missing)
- FP-013 Very long email

### Hotels Search And Listing (2 missing)
- HOTEL-013 Search non-existent city
- HOTEL-021 Same day check in and out

### Hotel Details And Booking (2 missing)
- HBOOK-001 Hotel details page content displayed
- HBOOK-018 Extremely long guest name

### Flights Search And Booking (5 missing)
- FLIGHT-011 Sort flights by duration
- FLIGHT-007 Passport expiry too soon
- FLIGHT-008 Invalid passport number format
- FLIGHT-013 Search with identical origin and destination
- FLIGHT-022 Passport expiry exactly on boundary

### Tours Search And Booking (1 missing)
- TOUR-003 Tour details page displays itinerary and inclusions

### Visa Services (1 missing)
- VISA-006 Missing required visa application fields

### User Dashboard And Booking Management (1 missing)
- UDB-001 Dashboard sections displayed

### Search And Filters (1 missing)
- FILTER-001 Filter sidebar controls displayed on listing pages

### Reviews And Ratings (2 missing)
- REVIEW-004 Sort reviews
- REVIEW-005 Review comment below minimum length

### Offers And Deals (1 missing)
- OFFER-007 Offer validity date boundary

### Logout (1 missing)
- LOGOUT-007 Rapid login/logout

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Home Page And Search (~7 extra types)
- Validation for non-numeric fields and travel end date
- Input trimming boundaries for pick-up locations

### Registration (~4 extra types)
- Email verification flow testing
- Attempting to submit form with all fields blank
- Password difference by trailing whitespace

### Login (~9 extra types)
- CAPTCHA edge cases around failed login thresholds
- Social login toggle behaviors

### Forgot Password (~6 extra types)
- Tampered or invalid reset link testing
- Very long password limits

### Hotels Search And Listing (~8 extra types)
- Active filter badge verification and controls
- Check-in to past date logic

### Hotel Details And Booking (~12 extra types)
- Detailed field validations (email format, empty fields, formatting)
- Populating data from selected room components

### Flights Search And Booking (~27 extra types)
- Round-trip date boundary constraints
- Expanded flight details interaction edge cases
- Deep passenger field validations and edge cases (DOB today, extreme bounds)

### Tours Search And Booking (~26 extra types)
- Tour specific filtering (departure dates, pricing logic, sorting)
- Travelers vs Adults/Children matrix boundary testing

### Cars Search And Booking (~22 extra types)
- Insurance, fuel policy, and extras toggles and selections
- Pick-up vs drop-off time format edge cases

### Visa Services (~4 extra types)
- Complex document upload scenarios (e.g., adding/removing multiple documents)

### User Dashboard And Booking Management (~42 extra types)
- Status-specific action validations (Pending vs Confirmed vs Cancelled)
- Edit/Save/Cancel interactions on profile properties

### Payment Processing (~9 extra types)
- Conditional UI toggling for Card vs PayPal
- Invoice and Voucher download coverage for distinct payment types

### Currency And Language Selection (~15 extra types)
- Deep scope checking for Cookies vs Profile state
- Active search preservation when switching settings

### Search And Filters (~22 extra types)
- Slider width constraints (identical values, crossed handles)
- Individual filter updates (star ratings, amenities)

### Reviews And Ratings (~11 extra types)
- Conditional category visibility behaviors
- Rapid review resubmission blocking

### Offers And Deals (~7 extra types)
- Promo code application edge cases
- Pre-filled search state preservation on back navigation

### Logout (~5 extra types)
- Duplicate click racing on logout
- Network in-flight termination during logout
