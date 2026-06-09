# Test Cases — Phptravels

Generated: 2026-06-09T11:10:09.896915Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 180 | 60 | 86 | 34 | 106 | 60 | 14 |

## Home Page & Search

Total: **13** (positive: 4, negative: 8, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search Hotels with valid input | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Hotels tab.<br>3. Fill in Destination, Check-In Date, Check-Out Date, Number of Rooms, and Guest Count.<br>4. Click on Search Button. | Redirects to the hotel results listing page. | high |
| TC-005 | WF-002 | Search Flights with valid input | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Flights tab.<br>3. Fill in Trip Type, Departure City, Arrival City, Departure Date, and Passenger Count.<br>4. Click on Search Button. | Redirects to the flight results listing page. | high |
| TC-008 | WF-003 | Search Tours with valid input | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Tours tab.<br>3. Fill in Destination, Start Date, and End Date.<br>4. Click on Search Button. | Redirects to the tour results listing page. | high |
| TC-011 | WF-004 | Search Cars with valid input | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Cars tab.<br>3. Fill in Pick-Up Location, Drop-Off Location, Pick-Up Date Time, and Drop-Off Date Time.<br>4. Click on Search Button. | Redirects to the car results listing page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Search Hotels with missing required fields | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Hotels tab.<br>3. Leave one or more required fields empty.<br>4. Click on Search Button. | Inline error messages appear for the empty required fields. | high |
| TC-003 | WF-001 | Search Hotels with invalid date range | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Hotels tab.<br>3. Fill in Destination, Check-In Date as tomorrow, Check-Out Date as yesterday, Number of Rooms, and Guest Count.<br>4. Click on Search Button. | Inline error message appears indicating that Check-Out Date must be after Check-In Date. | medium |
| TC-006 | WF-002 | Search Flights with missing required fields | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Flights tab.<br>3. Leave one or more required fields empty.<br>4. Click on Search Button. | Inline error messages appear for the empty required fields. | high |
| TC-007 | WF-002 | Search Flights with invalid date range | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Flights tab.<br>3. Fill in Trip Type, Departure City, Arrival City, Departure Date as tomorrow, Return Date as yesterday.<br>4. Click on Search Button. | Inline error message appears indicating that Return Date must be after Departure Date. | medium |
| TC-009 | WF-003 | Search Tours with missing required fields | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Tours tab.<br>3. Leave one or more required fields empty.<br>4. Click on Search Button. | Inline error messages appear for the empty required fields. | high |
| TC-010 | WF-003 | Search Tours with invalid date range | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Tours tab.<br>3. Fill in Destination, Start Date as tomorrow, End Date as yesterday.<br>4. Click on Search Button. | Inline error message appears indicating that End Date must be after Start Date. | medium |
| TC-012 | WF-004 | Search Cars with missing required fields | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Cars tab.<br>3. Leave one or more required fields empty.<br>4. Click on Search Button. | Inline error messages appear for the empty required fields. | high |
| TC-013 | WF-004 | Search Cars with invalid date/time | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Cars tab.<br>3. Fill in Pick-Up Location, Drop-Off Location, Pick-Up Date Time as tomorrow, Drop-Off Date Time as yesterday.<br>4. Click on Search Button. | Inline error message appears indicating that Drop-Off Date Time must be after Pick-Up Date Time. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Search Hotels with edge case for number of rooms | User logged in as Guest | 1. Navigate to Home Page.<br>2. Click on Hotels tab.<br>3. Fill in Destination, Check-In Date, Check-Out Date, Number of Rooms as 0, and Guest Count.<br>4. Click on Search Button. | Inline error message appears indicating that Number of Rooms must be at least 1. | medium |

---

## User Registration

Total: **8** (positive: 1, negative: 5, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid details | User is on the registration page, User is not already registered | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter a valid unique Email<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Account is created and user is redirected to the dashboard or prompted for email verification | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Registration fails with missing required fields | User is on the registration page | 1. Leave First Name empty<br>2. Leave Last Name empty<br>3. Leave Email empty<br>4. Leave Password empty<br>5. Leave Confirm Password empty<br>6. Leave Mobile Number empty<br>7. Leave Terms and Conditions checkbox unchecked<br>8. Click on Submit | Inline error messages appear for all required fields | high |
| TC-003 | WF-001 | Registration fails with invalid email format | User is on the registration page | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter an invalid Email format<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears for invalid email format | medium |
| TC-004 | WF-001 | Registration fails when passwords do not match | User is on the registration page | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter a valid unique Email<br>4. Enter a valid Password<br>5. Enter a different Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears indicating passwords do not match | medium |
| TC-005 | WF-001 | Registration fails with non-unique email | User is on the registration page, An account with the same email already exists | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter the existing Email<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears indicating email must be unique | high |
| TC-008 | WF-001 | Registration fails with invalid Mobile Number | User is on the registration page | 1. Enter valid First Name<br>2. Enter valid Last Name<br>3. Enter a valid unique Email<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter an invalid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears for invalid Mobile Number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Registration fails with too long First Name | User is on the registration page | 1. Enter a First Name longer than 50 characters<br>2. Enter valid Last Name<br>3. Enter a valid unique Email<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears for First Name exceeding character limit | medium |
| TC-007 | WF-001 | Registration fails with too long Last Name | User is on the registration page | 1. Enter valid First Name<br>2. Enter a Last Name longer than 50 characters<br>3. Enter a valid unique Email<br>4. Enter a valid Password<br>5. Enter the same Password in Confirm Password<br>6. Enter a valid Mobile Number<br>7. Check the Terms and Conditions checkbox<br>8. Click on Submit | Inline error message appears for Last Name exceeding character limit | medium |

---

## User Login

Total: **6** (positive: 2, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User is registered, User is on the login page | 1. Enter valid email in the Email field<br>2. Enter valid password in the Password field<br>3. Click on the Login button | User is redirected to the dashboard or the page they were previously trying to access | high |
| TC-005 | WF-001 | Login with Remember Me checked | User is registered, User is on the login page | 1. Enter valid email in the Email field<br>2. Enter valid password in the Password field<br>3. Check the Remember Me checkbox<br>4. Click on the Login button | User is redirected to the dashboard or the page they were previously trying to access, and the session is remembered for future logins | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Login with invalid credentials | User is on the login page | 1. Enter invalid email in the Email field<br>2. Enter invalid password in the Password field<br>3. Click on the Login button | An error message is displayed and the password field is cleared | high |
| TC-003 | WF-002 | Login with empty email field | User is on the login page | 1. Leave the Email field empty<br>2. Enter valid password in the Password field<br>3. Click on the Login button | An error message is displayed indicating that the Email field is required | medium |
| TC-004 | WF-002 | Login with empty password field | User is on the login page | 1. Enter valid email in the Email field<br>2. Leave the Password field empty<br>3. Click on the Login button | An error message is displayed indicating that the Password field is required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Login with multiple consecutive failed attempts | User is on the login page, User has attempted to log in with invalid credentials multiple times | 1. Enter invalid email in the Email field<br>2. Enter invalid password in the Password field<br>3. Click on the Login button<br>4. Repeat the above steps multiple times | CAPTCHA verification is displayed after multiple consecutive failed attempts | medium |

---

## Forgot Password

Total: **8** (positive: 2, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Reset Password with existing email | User logged in as Guest, Email exists in the system | 1. Enter valid email in the Email field<br>2. Click on Reset Password button | A reset link is sent to the email and a confirmation message is displayed. | high |
| TC-003 | WF-003 | Submit Change Password with valid new password | User accessed the password reset page via reset link, User has a valid new password | 1. Enter new password in the New Password field<br>2. Click on Change Password button | User is redirected to the login page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Submit Reset Password with email not found | User logged in as Guest, Email does not exist in the system | 1. Enter invalid email in the Email field<br>2. Click on Reset Password button | An error message is shown and the form remains editable. | high |
| TC-004 | WF-003 | Submit Change Password with empty new password | User accessed the password reset page via reset link | 1. Leave New Password field empty<br>2. Click on Change Password button | An error message is shown indicating that the new password is required. | medium |
| TC-005 | WF-001 | Submit Reset Password with invalid email format | User logged in as Guest | 1. Enter invalid email format in the Email field<br>2. Click on Reset Password button | An error message is shown indicating that the email format is invalid. | medium |
| TC-006 | WF-003 | Submit Change Password with password that does not meet criteria | User accessed the password reset page via reset link | 1. Enter a weak password in the New Password field<br>2. Click on Change Password button | An error message is shown indicating that the password does not meet the required criteria. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Submit Reset Password with email that is too long | User logged in as Guest | 1. Enter an email longer than 254 characters in the Email field<br>2. Click on Reset Password button | An error message is shown indicating that the email is too long. | low |
| TC-008 | WF-003 | Submit Change Password with new password of maximum length | User accessed the password reset page via reset link | 1. Enter a new password that is exactly 128 characters long in the New Password field<br>2. Click on Change Password button | User is redirected to the login page with a success message. | low |

---

## Hotels Search & Listing

Total: **8** (positive: 2, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for hotels with valid inputs | User logged in as Guest, User is on the Hotels Search page | 1. Enter a valid destination.<br>2. Select a valid check-in date.<br>3. Select a valid check-out date.<br>4. Enter a valid number of rooms.<br>5. Enter a valid guest count with adults and children. | User is redirected to the listing page with relevant hotel results displayed. | high |
| TC-007 | WF-002 | Book a hotel successfully | User logged in as Guest, User is on the hotel listing page | 1. Click on the 'Book Now' button for a selected hotel. | Booking is confirmed and user receives a confirmation message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Search for hotels with missing destination | User logged in as Guest, User is on the Hotels Search page | 1. Leave the destination field empty.<br>2. Select valid check-in and check-out dates.<br>3. Enter a valid number of rooms.<br>4. Enter a valid guest count. | An error message is displayed indicating that the destination is required. | high |
| TC-003 | WF-001 | Search for hotels with invalid check-out date | User logged in as Guest, User is on the Hotels Search page | 1. Enter a valid destination.<br>2. Select a valid check-in date.<br>3. Select a check-out date that is before the check-in date.<br>4. Enter a valid number of rooms.<br>5. Enter a valid guest count. | An error message is displayed indicating that the check-out date must be after the check-in date. | high |
| TC-004 | WF-001 | Search for hotels with zero rooms | User logged in as Guest, User is on the Hotels Search page | 1. Enter a valid destination.<br>2. Select valid check-in and check-out dates.<br>3. Enter 0 for the number of rooms.<br>4. Enter a valid guest count. | An error message is displayed indicating that the number of rooms must be at least 1. | high |
| TC-008 | WF-002 | Attempt to book a hotel without selecting a hotel | User logged in as Guest, User is on the hotel listing page | 1. Attempt to click on the 'Book Now' button without selecting a hotel. | An error message is displayed indicating that a hotel must be selected to proceed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Search for hotels with maximum guest count | User logged in as Guest, User is on the Hotels Search page | 1. Enter a valid destination.<br>2. Select valid check-in and check-out dates.<br>3. Enter a valid number of rooms.<br>4. Enter maximum allowed guest count (e.g., 10 adults). | User is redirected to the listing page with relevant hotel results displayed. | medium |
| TC-006 | WF-001 | Search for hotels with a future date | User logged in as Guest, User is on the Hotels Search page | 1. Enter a valid destination.<br>2. Select a check-in date that is 1 year in the future.<br>3. Select a check-out date that is 1 year and 1 day in the future.<br>4. Enter a valid number of rooms.<br>5. Enter a valid guest count. | User is redirected to the listing page with relevant hotel results displayed. | medium |

---

## Hotel Details & Booking

Total: **6** (positive: 2, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking with valid details | User logged in as Guest | 1. Select a hotel and room type<br>2. Enter stay dates<br>3. Enter guest count<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click on 'Book Now' | User is redirected to the payment page | high |
| TC-006 | WF-001 | Booking with special requests | User logged in as Guest | 1. Select a hotel and room type<br>2. Enter stay dates<br>3. Enter guest count<br>4. Fill in First Name, Last Name, Email, Phone Number, and Special Requests<br>5. Click on 'Book Now' | User is redirected to the payment page with special requests noted | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Booking without stay dates | User logged in as Guest | 1. Select a hotel and room type<br>2. Leave stay dates empty<br>3. Enter guest count<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click on 'Book Now' | Error message indicating stay dates are required | high |
| TC-003 | WF-001 | Booking with invalid email format | User logged in as Guest | 1. Select a hotel and room type<br>2. Enter stay dates<br>3. Enter guest count<br>4. Fill in First Name, Last Name, invalid Email format, and Phone Number<br>5. Click on 'Book Now' | Error message indicating invalid email format | medium |
| TC-004 | WF-001 | Booking with zero guest count | User logged in as Guest | 1. Select a hotel and room type<br>2. Enter stay dates<br>3. Enter guest count as 0<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click on 'Book Now' | Error message indicating guest count must be greater than zero | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Booking with maximum character length for names | User logged in as Guest | 1. Select a hotel and room type<br>2. Enter stay dates<br>3. Enter guest count<br>4. Fill in First Name and Last Name with maximum allowed characters<br>5. Fill in valid Email and Phone Number<br>6. Click on 'Book Now' | User is redirected to the payment page | low |

---

## Flights Search & Listing

Total: **7** (positive: 3, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for a one-way flight with valid details | User logged in as Traveler, User is on the Flights Search page | 1. Select 'One-way' from Trip Type dropdown<br>2. Enter 'New York' in Departure City<br>3. Enter 'Los Angeles' in Arrival City<br>4. Select a valid date from Travel Dates<br>5. Set Passenger Count to 1 Adult<br>6. Select 'Economy' from Cabin Class dropdown<br>7. Click on 'Search Flights' button | User is redirected to the listing page showing available flights | high |
| TC-002 | WF-001 | Search for a round-trip flight with valid details | User logged in as Traveler, User is on the Flights Search page | 1. Select 'Round-trip' from Trip Type dropdown<br>2. Enter 'Chicago' in Departure City<br>3. Enter 'Miami' in Arrival City<br>4. Select valid departure and return dates from Travel Dates<br>5. Set Passenger Count to 2 Adults and 1 Child<br>6. Select 'Business' from Cabin Class dropdown<br>7. Click on 'Search Flights' button | User is redirected to the listing page showing available flights | high |
| TC-006 | WF-002 | Select a flight from the listing | User logged in as Traveler, User is on the Flights Listing page | 1. View the list of available flights<br>2. Click on the 'Select' button for the first flight in the list | Flight is selected for booking and user is taken to the booking page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Search for flights with invalid dates | User logged in as Traveler, User is on the Flights Search page | 1. Select 'One-way' from Trip Type dropdown<br>2. Enter 'San Francisco' in Departure City<br>3. Enter 'Seattle' in Arrival City<br>4. Select a past date from Travel Dates<br>5. Set Passenger Count to 1 Adult<br>6. Select 'Economy' from Cabin Class dropdown<br>7. Click on 'Search Flights' button | Error message displayed indicating that the travel date cannot be in the past | high |
| TC-004 | WF-001 | Search for flights with no departure city | User logged in as Traveler, User is on the Flights Search page | 1. Select 'Multi-city' from Trip Type dropdown<br>2. Leave Departure City empty<br>3. Enter 'Toronto' in Arrival City<br>4. Select a valid date from Travel Dates<br>5. Set Passenger Count to 1 Adult<br>6. Select 'Premium Economy' from Cabin Class dropdown<br>7. Click on 'Search Flights' button | Error message displayed indicating that Departure City is required | high |
| TC-007 | WF-002 | Attempt to select a flight when no flights are available | User logged in as Traveler, User is on the Flights Listing page with no flights displayed | 1. Attempt to click on the 'Select' button for a flight that is not displayed | No action taken, and a message indicating no flights available is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Search for flights with maximum passenger count | User logged in as Traveler, User is on the Flights Search page | 1. Select 'Round-trip' from Trip Type dropdown<br>2. Enter 'London' in Departure City<br>3. Enter 'Paris' in Arrival City<br>4. Select valid departure and return dates from Travel Dates<br>5. Set Passenger Count to maximum allowed (e.g., 9 Adults)<br>6. Select 'First' from Cabin Class dropdown<br>7. Click on 'Search Flights' button | User is redirected to the listing page showing available flights for maximum passenger count | medium |

---

## Flight Booking

Total: **8** (positive: 1, negative: 7, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit with all required fields filled | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Submit with missing First Name | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Leave First Name empty<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for First Name, and progression is blocked | high |
| TC-003 | WF-003 | Submit with missing Last Name | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Leave Last Name empty<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for Last Name, and progression is blocked | high |
| TC-004 | WF-004 | Submit with missing Date of Birth | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Leave Date of Birth empty<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for Date of Birth, and progression is blocked | high |
| TC-005 | WF-005 | Submit with missing Passport Number | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Leave Passport Number empty<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for Passport Number, and progression is blocked | high |
| TC-006 | WF-006 | Submit with missing Passport Expiry | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Leave Passport Expiry empty<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for Passport Expiry, and progression is blocked | high |
| TC-007 | WF-007 | Submit with missing Lead Passenger Email | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Leave Lead Passenger Email empty<br>8. Enter Lead Passenger Phone as 1234567890<br>9. Click Continue | Inline error displayed for Lead Passenger Email, and progression is blocked | high |
| TC-008 | WF-008 | Submit with missing Lead Passenger Phone | User logged in as Customer, Booking form is displayed | 1. Fill in Title as Mr<br>2. Enter First Name as John<br>3. Enter Last Name as Doe<br>4. Enter Date of Birth as 1990-01-01<br>5. Enter Passport Number as A12345678<br>6. Enter Passport Expiry as 2030-01-01<br>7. Enter Lead Passenger Email as john.doe@example.com<br>8. Leave Lead Passenger Phone empty<br>9. Click Continue | Inline error displayed for Lead Passenger Phone, and progression is blocked | high |

---

## Tours Search & Listing

Total: **6** (positive: 2, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for tours with valid inputs | User logged in as Traveler, User is on the Tours Search page | 1. Enter a valid destination.<br>2. Select valid travel dates.<br>3. Choose a tour type from the dropdown.<br>4. Enter a valid duration.<br>5. Click on the Search button. | User is redirected to the listing page showing available tours. | high |
| TC-006 | WF-001 | Search for tours with budget range specified | User logged in as Traveler, User is on the Tours Search page | 1. Enter a valid destination.<br>2. Select valid travel dates.<br>3. Choose a tour type from the dropdown.<br>4. Enter a valid duration.<br>5. Specify a budget range.<br>6. Click on the Search button. | User is redirected to the listing page showing available tours within the specified budget range. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Search for tours with missing destination | User logged in as Traveler, User is on the Tours Search page | 1. Leave the destination field empty.<br>2. Select valid travel dates.<br>3. Choose a tour type from the dropdown.<br>4. Enter a valid duration.<br>5. Click on the Search button. | An error message is displayed indicating that the destination is required. | high |
| TC-003 | WF-001 | Search for tours with invalid travel dates | User logged in as Traveler, User is on the Tours Search page | 1. Enter a valid destination.<br>2. Select an invalid travel date (e.g., past date).<br>3. Choose a tour type from the dropdown.<br>4. Enter a valid duration.<br>5. Click on the Search button. | An error message is displayed indicating that the travel dates are invalid. | high |
| TC-005 | WF-001 | Search for tours with negative duration | User logged in as Traveler, User is on the Tours Search page | 1. Enter a valid destination.<br>2. Select valid travel dates.<br>3. Choose a tour type from the dropdown.<br>4. Enter a negative duration (-5 days).<br>5. Click on the Search button. | An error message is displayed indicating that the duration must be a positive number. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Search for tours with maximum duration | User logged in as Traveler, User is on the Tours Search page | 1. Enter a valid destination.<br>2. Select valid travel dates.<br>3. Choose a tour type from the dropdown.<br>4. Enter the maximum valid duration (e.g., 30 days).<br>5. Click on the Search button. | User is redirected to the listing page showing available tours for the maximum duration. | medium |

---

## Tour Details & Booking

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking with valid details | User logged in as traveler, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (2 adults, 1 child)<br>3. Fill in traveler details (names and contact details)<br>4. Click on 'Book Now' | Total cost breakdown is displayed | high |
| TC-007 | WF-001 | Booking with future departure date | User logged in as traveler, Tour details page is open | 1. Select a departure date that is 1 year in the future<br>2. Enter number of travelers (2 adults)<br>3. Fill in traveler details<br>4. Click on 'Book Now' | Total cost breakdown is displayed for the future date | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Booking with missing required fields | User logged in as traveler, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (1 adult)<br>3. Leave traveler name blank<br>4. Click on 'Book Now' | Error message indicating that name is required is displayed | high |
| TC-003 | WF-001 | Booking with invalid number of travelers | User logged in as traveler, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (negative number)<br>3. Click on 'Book Now' | Error message indicating that the number of travelers must be positive is displayed | medium |
| TC-004 | WF-002 | Redirect to login when not logged in | User not logged in, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (1 adult)<br>3. Click on 'Book Now' | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Booking with maximum number of travelers | User logged in as traveler, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (100 adults)<br>3. Fill in traveler details for all travelers<br>4. Click on 'Book Now' | Total cost breakdown is displayed for 100 travelers | medium |
| TC-006 | WF-001 | Booking with minimum number of travelers | User logged in as traveler, Tour details page is open | 1. Select a valid departure date<br>2. Enter number of travelers (1 adult)<br>3. Fill in traveler details<br>4. Click on 'Book Now' | Total cost breakdown is displayed for 1 traveler | medium |

---

## Cars Search & Listing

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful search for cars with valid inputs | User logged in as Customer, User is on the Cars Search & Listing page | 1. Enter valid Pick Up Location<br>2. Enter valid Drop Off Location<br>3. Select valid Pick Up Date Time<br>4. Select valid Drop Off Date Time<br>5. Enter valid Driver Age<br>6. Click on Search | User is redirected to the listing page with available cars displayed | high |
| TC-005 | WF-002 | Successful booking of a vehicle | User logged in as Customer, User is on the vehicle listing page | 1. Click on Book Now for a selected vehicle | Booking is confirmed and user receives a confirmation message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Search fails with missing Pick Up Location | User logged in as Customer, User is on the Cars Search & Listing page | 1. Leave Pick Up Location empty<br>2. Enter valid Drop Off Location<br>3. Select valid Pick Up Date Time<br>4. Select valid Drop Off Date Time<br>5. Enter valid Driver Age<br>6. Click on Search | Error message displayed indicating Pick Up Location is required | high |
| TC-003 | WF-001 | Search fails with invalid Driver Age | User logged in as Customer, User is on the Cars Search & Listing page | 1. Enter valid Pick Up Location<br>2. Enter valid Drop Off Location<br>3. Select valid Pick Up Date Time<br>4. Select valid Drop Off Date Time<br>5. Enter invalid Driver Age (e.g., 15)<br>6. Click on Search | Error message displayed indicating Driver Age must be at least 18 | high |
| TC-006 | WF-002 | Booking fails due to vehicle unavailability | User logged in as Customer, User is on the vehicle listing page | 1. Click on Book Now for a vehicle that is already booked | Error message displayed indicating the vehicle is not available for booking | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Search with future dates only | User logged in as Customer, User is on the Cars Search & Listing page | 1. Enter valid Pick Up Location<br>2. Enter valid Drop Off Location<br>3. Select Pick Up Date Time as tomorrow<br>4. Select Drop Off Date Time as two days from now<br>5. Enter valid Driver Age<br>6. Click on Search | User is redirected to the listing page with available cars displayed for future dates | medium |
| TC-007 | WF-001 | Search with maximum character limit in locations | User logged in as Customer, User is on the Cars Search & Listing page | 1. Enter a Pick Up Location with maximum allowed characters<br>2. Enter a Drop Off Location with maximum allowed characters<br>3. Select valid Pick Up Date Time<br>4. Select valid Drop Off Date Time<br>5. Enter valid Driver Age<br>6. Click on Search | User is redirected to the listing page with available cars displayed | medium |

---

## Car Booking

Total: **7** (positive: 2, negative: 4, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid booking form | User logged in as Customer, User on car booking page | 1. Fill in Driver Full Name with 'John Doe'<br>2. Fill in Age with '30'<br>3. Fill in License Number with 'ABC123456'<br>4. Fill in License Issue Country with 'USA'<br>5. Fill in Email with 'john.doe@example.com'<br>6. Fill in Phone Number with '1234567890'<br>7. Select Insurance Plan as 'Standard'<br>8. Click on 'Confirm Booking' | User is redirected to payment page | high |
| TC-006 | WF-002 | Accept terms and proceed to payment | User logged in as Customer, User has filled out booking form | 1. Click on 'Accept Terms' | User is redirected to payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit booking form with missing required fields | User logged in as Customer, User on car booking page | 1. Leave Driver Full Name empty<br>2. Leave Age empty<br>3. Leave License Number empty<br>4. Leave License Issue Country empty<br>5. Leave Email empty<br>6. Leave Phone Number empty<br>7. Click on 'Confirm Booking' | Inline errors displayed for all required fields, and user remains on booking form | high |
| TC-003 | WF-001 | Submit booking form with invalid email format | User logged in as Customer, User on car booking page | 1. Fill in Driver Full Name with 'John Doe'<br>2. Fill in Age with '30'<br>3. Fill in License Number with 'ABC123456'<br>4. Fill in License Issue Country with 'USA'<br>5. Fill in Email with 'john.doe.com'<br>6. Fill in Phone Number with '1234567890'<br>7. Select Insurance Plan as 'Standard'<br>8. Click on 'Confirm Booking' | Inline error displayed for invalid email format, and user remains on booking form | medium |
| TC-004 | WF-001 | Submit booking form with age under 18 | User logged in as Customer, User on car booking page | 1. Fill in Driver Full Name with 'John Doe'<br>2. Fill in Age with '17'<br>3. Fill in License Number with 'ABC123456'<br>4. Fill in License Issue Country with 'USA'<br>5. Fill in Email with 'john.doe@example.com'<br>6. Fill in Phone Number with '1234567890'<br>7. Select Insurance Plan as 'Standard'<br>8. Click on 'Confirm Booking' | Inline error displayed for age restriction, and user remains on booking form | medium |
| TC-007 | WF-002 | Attempt to accept terms without filling booking form | User logged in as Customer, User on car booking page | 1. Click on 'Accept Terms' | User remains on booking form with inline error for missing fields | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Submit booking form with maximum character limit for Driver Full Name | User logged in as Customer, User on car booking page | 1. Fill in Driver Full Name with a string of 100 characters<br>2. Fill in Age with '30'<br>3. Fill in License Number with 'ABC123456'<br>4. Fill in License Issue Country with 'USA'<br>5. Fill in Email with 'john.doe@example.com'<br>6. Fill in Phone Number with '1234567890'<br>7. Select Insurance Plan as 'Standard'<br>8. Click on 'Confirm Booking' | User is redirected to payment page | low |

---

## Visa Services

Total: **9** (positive: 2, negative: 6, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View visa requirements for valid nationality and destination country | User logged in as applicant, User is on the Visa Requirements page | 1. Select a valid nationality from the dropdown<br>2. Select a valid destination country from the dropdown<br>3. Click on Submit | Visa requirements displayed based on nationality and destination country | high |
| TC-004 | WF-002 | Submit a valid visa application form | User logged in as applicant, User is on the Visa Application Form page | 1. Fill in Full Name with valid data<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a future date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with a valid email address<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with a valid number<br>11. Upload a valid passport copy<br>12. Click on Submit | Application submitted; status can be tracked in dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view visa requirements with invalid nationality | User logged in as applicant, User is on the Visa Requirements page | 1. Select an invalid nationality from the dropdown<br>2. Select a valid destination country from the dropdown<br>3. Click on Submit | Error message displayed indicating invalid nationality | high |
| TC-003 | WF-001 | Attempt to view visa requirements with unselected nationality and destination | User logged in as applicant, User is on the Visa Requirements page | 1. Leave nationality dropdown unselected<br>2. Leave destination country dropdown unselected<br>3. Click on Submit | Error message displayed indicating both fields are required | high |
| TC-005 | WF-002 | Submit visa application form with missing required fields | User logged in as applicant, User is on the Visa Application Form page | 1. Leave Full Name blank<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a future date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with a valid email address<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with a valid number<br>11. Upload a valid passport copy<br>12. Click on Submit | Error message displayed indicating Full Name is required | high |
| TC-006 | WF-002 | Submit visa application form with invalid email format | User logged in as applicant, User is on the Visa Application Form page | 1. Fill in Full Name with valid data<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a future date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with invalid format (e.g., 'user@domain')<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with a valid number<br>11. Upload a valid passport copy<br>12. Click on Submit | Error message displayed indicating invalid email format | high |
| TC-007 | WF-002 | Submit visa application form with past passport expiry date | User logged in as applicant, User is on the Visa Application Form page | 1. Fill in Full Name with valid data<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a past date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with a valid email address<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with a valid number<br>11. Upload a valid passport copy<br>12. Click on Submit | Error message displayed indicating passport expiry date must be in the future | high |
| TC-009 | WF-002 | Upload an invalid file type in document upload | User logged in as applicant, User is on the Visa Application Form page | 1. Fill in Full Name with valid data<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a future date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with a valid email address<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with a valid number<br>11. Upload an invalid file type (e.g., .exe)<br>12. Click on Submit | Error message displayed indicating invalid file type uploaded | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-002 | Submit visa application form with zero duration of stay | User logged in as applicant, User is on the Visa Application Form page | 1. Fill in Full Name with valid data<br>2. Fill in Passport Number with valid data<br>3. Fill in Passport Expiry Date with a future date<br>4. Fill in Date of Birth with a valid date<br>5. Select Nationality from dropdown<br>6. Fill in Email with a valid email address<br>7. Fill in Phone with valid data (optional)<br>8. Fill in Purpose of Visit with valid data<br>9. Fill in Intended Travel Dates with valid date range<br>10. Fill in Duration of Stay with 0<br>11. Upload a valid passport copy<br>12. Click on Submit | Error message displayed indicating duration of stay must be greater than zero | high |

---

## User Dashboard

Total: **12** (positive: 5, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Booking Details with valid booking reference | User logged in as regular user, Booking exists with valid reference | 1. Navigate to My Bookings<br>2. Click on 'View Details' for a booking | Booking details displayed | high |
| TC-002 | WF-002 | Cancel Booking with valid conditions | User logged in as regular user, Booking exists with cancellation policy permit | 1. Navigate to My Bookings<br>2. Click on 'Cancel' for a booking | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify Booking with valid conditions | User logged in as regular user, Booking exists with modification policy permit | 1. Navigate to My Bookings<br>2. Click on 'Modify' for a booking | Booking modification initiated | high |
| TC-004 | WF-004 | Edit Profile without personal information | User logged in as regular user | 1. Navigate to My Profile<br>2. Click on 'Edit' | Profile editing interface opened | medium |
| TC-005 | WF-005 | Logout from the dashboard | User logged in as regular user | 1. Click on 'Logout' button | User logged out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Cancel Booking with invalid conditions | User logged in as regular user, Booking exists but cancellation policy does not permit | 1. Navigate to My Bookings<br>2. Click on 'Cancel' for a booking | Cancellation not permitted; error message shown | high |
| TC-007 | WF-003 | Modify Booking with invalid conditions | User logged in as regular user, Booking exists but modification policy does not permit | 1. Navigate to My Bookings<br>2. Click on 'Modify' for a booking | Modification not permitted; error message shown | high |
| TC-008 | WF-001 | View Booking Details with invalid booking reference | User logged in as regular user, No booking exists with the provided reference | 1. Navigate to My Bookings<br>2. Attempt to view details for an invalid booking reference | Error message displayed; booking not found | medium |
| TC-009 | WF-004 | Edit Profile with empty fields | User logged in as regular user | 1. Navigate to My Profile<br>2. Click on 'Edit'<br>3. Leave all fields empty and submit | Validation errors shown for required fields | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-001 | View Booking Details with no bookings | User logged in as regular user, No bookings exist | 1. Navigate to My Bookings | Message displayed indicating no bookings available | low |
| TC-011 | WF-002 | Cancel Booking with maximum allowed characters in reference | User logged in as regular user, Booking exists with valid reference at max character length | 1. Navigate to My Bookings<br>2. Click on 'Cancel' for a booking | Booking cancelled; success message shown | medium |
| TC-012 | WF-003 | Modify Booking with maximum allowed characters in service type | User logged in as regular user, Booking exists with valid service type at max character length | 1. Navigate to My Bookings<br>2. Click on 'Modify' for a booking | Booking modification initiated | medium |

---

## Booking Management

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details with valid inputs | User logged in as Customer, Booking type and cancellation policy permit modification | 1. Navigate to Booking Detail View<br>2. Click on Modify button<br>3. Enter valid travel dates<br>4. Add special requests<br>5. Update traveler information<br>6. Submit changes | Booking details modified successfully | high |
| TC-004 | WF-002 | Cancel booking with confirmation | User logged in as Customer, Booking exists | 1. Navigate to Booking Detail View<br>2. Click on Cancel button<br>3. Check the confirmation checkbox<br>4. Confirm cancellation | Opens cancellation confirmation flow and processes cancellation | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Modify booking details with invalid travel dates | User logged in as Customer, Booking type and cancellation policy permit modification | 1. Navigate to Booking Detail View<br>2. Click on Modify button<br>3. Enter invalid travel dates (past dates)<br>4. Submit changes | Error message displayed for invalid travel dates | high |
| TC-003 | WF-001 | Modify booking details without required fields | User logged in as Customer, Booking type and cancellation policy permit modification | 1. Navigate to Booking Detail View<br>2. Click on Modify button<br>3. Leave required fields empty<br>4. Submit changes | Error message displayed for missing required fields | medium |
| TC-005 | WF-002 | Cancel booking without confirmation checkbox checked | User logged in as Customer, Booking exists | 1. Navigate to Booking Detail View<br>2. Click on Cancel button<br>3. Leave confirmation checkbox unchecked<br>4. Attempt to confirm cancellation | Error message displayed for unconfirmed cancellation | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Modify booking details with maximum character limits | User logged in as Customer, Booking type and cancellation policy permit modification | 1. Navigate to Booking Detail View<br>2. Click on Modify button<br>3. Enter maximum character limit for special requests<br>4. Submit changes | Booking details modified successfully with maximum character limit | low |
| TC-007 | WF-001 | Modify booking details with minimum character limits | User logged in as Customer, Booking type and cancellation policy permit modification | 1. Navigate to Booking Detail View<br>2. Click on Modify button<br>3. Enter minimum character limit for special requests<br>4. Submit changes | Booking details modified successfully with minimum character limit | low |

---

## Payment Processing

Total: **19** (positive: 8, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Payment with valid Credit/Debit Card | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | high |
| TC-002 | WF-002 | Submit Payment with valid PayPal account | User logged in as Customer, Booking details are filled | 1. Select 'PayPal' from Payment_Method dropdown<br>2. Click on 'Submit Payment'<br>3. Complete PayPal authentication | Redirects to booking confirmation page with reference number | high |
| TC-003 | WF-003 | Submit Payment with valid Bank Transfer | User logged in as Customer, Booking details are filled | 1. Select 'Bank Transfer' from Payment_Method dropdown<br>2. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | high |
| TC-004 | WF-004 | Submit Payment with Wallet/Credits | User logged in as Customer, Booking details are filled | 1. Select 'Wallet/Credits' from Payment_Method dropdown<br>2. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | high |
| TC-005 | WF-005 | Retry Payment with valid Credit/Debit Card | User logged in as Customer, Booking details are filled, Previous payment attempt failed | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Retry Payment' | User can retry without losing booking details | medium |
| TC-006 | WF-006 | Retry Payment with valid PayPal account | User logged in as Customer, Booking details are filled, Previous payment attempt failed | 1. Select 'PayPal' from Payment_Method dropdown<br>2. Click on 'Retry Payment'<br>3. Complete PayPal authentication | User can retry without losing booking details | medium |
| TC-007 | WF-007 | Retry Payment with valid Bank Transfer | User logged in as Customer, Booking details are filled, Previous payment attempt failed | 1. Select 'Bank Transfer' from Payment_Method dropdown<br>2. Click on 'Retry Payment' | User can retry without losing booking details | medium |
| TC-008 | WF-008 | Retry Payment with Wallet/Credits | User logged in as Customer, Booking details are filled, Previous payment attempt failed | 1. Select 'Wallet/Credits' from Payment_Method dropdown<br>2. Click on 'Retry Payment' | User can retry without losing booking details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Submit Payment without Cardholder Name | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Leave Cardholder_Name empty<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Error message indicating Cardholder Name is required | high |
| TC-010 | WF-001 | Submit Payment without Card Number | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Leave Card_Number empty<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Error message indicating Card Number is required | high |
| TC-011 | WF-001 | Submit Payment with invalid Card Number | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with invalid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Error message indicating Card Number is invalid | high |
| TC-012 | TC-001 | Submit Payment with expired Card | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a past date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Error message indicating Card is expired | high |
| TC-013 | WF-001 | Submit Payment with missing CVV | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Leave CVV empty<br>6. Click on 'Submit Payment' | Error message indicating CVV is required | high |
| TC-014 | WF-001 | Submit Payment with invalid CVV | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with invalid code<br>6. Click on 'Submit Payment' | Error message indicating CVV is invalid | high |
| TC-015 | WF-001 | Submit Payment without selecting Payment Method | User logged in as Customer, Booking details are filled | 1. Leave Payment_Method dropdown unselected<br>2. Click on 'Submit Payment' | Error message indicating Payment Method is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 | WF-001 | Submit Payment with maximum length Cardholder Name | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with 255 characters<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | medium |
| TC-017 | WF-001 | Submit Payment with maximum length Card Number | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with 19 digits<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with valid 3 or 4 digit code<br>6. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | medium |
| TC-018 | WF-001 | Submit Payment with minimum length CVV | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with 3 digits<br>6. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | medium |
| TC-019 | WF-001 | Submit Payment with maximum length CVV | User logged in as Customer, Booking details are filled | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name with valid name<br>3. Fill in Card_Number with valid card number<br>4. Fill in Expiration_Date with a valid future date<br>5. Fill in CVV with 4 digits<br>6. Click on 'Submit Payment' | Redirects to booking confirmation page with reference number | medium |

---

## Currency & Language Selection

Total: **12** (positive: 8, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select USD as currency | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Select 'USD' from the options | All prices displayed across the site are updated to USD | high |
| TC-002 | WF-002 | Select EUR as currency | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Select 'EUR' from the options | All prices displayed across the site are updated to EUR | high |
| TC-003 | WF-003 | Select GBP as currency | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Select 'GBP' from the options | All prices displayed across the site are updated to GBP | high |
| TC-004 | WF-004 | Select JPY as currency | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Select 'JPY' from the options | All prices displayed across the site are updated to JPY | high |
| TC-005 | WF-005 | Select English as language | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Select 'English' from the options | The entire site interface is switched to English | high |
| TC-006 | WF-006 | Select Arabic as language | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Select 'Arabic' from the options | The entire site interface is switched to Arabic | high |
| TC-007 | WF-007 | Select Spanish as language | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Select 'Spanish' from the options | The entire site interface is switched to Spanish | high |
| TC-008 | WF-008 | Select French as language | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Select 'French' from the options | The entire site interface is switched to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Select invalid currency | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Attempt to select 'AUD' (not in options) | Selection is blocked, and an error message is displayed | medium |
| TC-010 | WF-005 | Select invalid language | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Attempt to select 'German' (not in options) | Selection is blocked, and an error message is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Select currency with no selection | User logged in as authenticated user | 1. Open the currency selector dropdown<br>2. Do not make a selection and close the dropdown | Prices remain unchanged and no error occurs | low |
| TC-012 | WF-005 | Select language with no selection | User logged in as authenticated user | 1. Open the language selector dropdown<br>2. Do not make a selection and close the dropdown | Site interface remains unchanged and no error occurs | low |

---

## Search & Filters

Total: **15** (positive: 7, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters with valid price range and star ratings | User logged in as <Role>, No filters applied | 1. Open the filter section<br>2. Set price range using the slider<br>3. Select star ratings<br>4. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | high |
| TC-002 | WF-002 | Apply filters for hotels with valid selections | User logged in as <Role>, No filters applied | 1. Open the Hotels tab<br>2. Select hotel type from dropdown<br>3. Check amenities<br>4. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | high |
| TC-003 | WF-003 | Apply filters for flights with valid selections | User logged in as <Role>, No filters applied | 1. Open the Flights tab<br>2. Select number of stops from dropdown<br>3. Set departure and arrival time ranges<br>4. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | high |
| TC-004 | WF-004 | Apply filters for tours with valid selections | User logged in as <Role>, No filters applied | 1. Open the Tours tab<br>2. Select tour type from dropdown<br>3. Set duration<br>4. Set departure dates<br>5. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | high |
| TC-005 | WF-005 | Apply filters for cars with valid selections | User logged in as <Role>, No filters applied | 1. Open the Cars tab<br>2. Select car type from dropdown<br>3. Select transmission type<br>4. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | high |
| TC-006 | WF-006 | Remove individual filter successfully | User logged in as <Role>, At least one filter applied | 1. Click on the remove button next to an active filter | The selected filter is removed and results update accordingly | medium |
| TC-007 | WF-007 | Reset all filters successfully | User logged in as <Role>, At least one filter applied | 1. Click on Reset All Filters button | All filters are reset and results revert to the original state | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Attempt to apply filters with invalid price range | User logged in as <Role>, No filters applied | 1. Open the filter section<br>2. Set price range to invalid values (e.g., max < min)<br>3. Click on Apply Filters | Error message displayed indicating invalid price range | high |
| TC-009 | WF-002 | Attempt to apply filters for hotels with no selections | User logged in as <Role>, No filters applied | 1. Open the Hotels tab<br>2. Do not select any filters<br>3. Click on Apply Filters | Error message displayed indicating that at least one filter must be selected | high |
| TC-010 | WF-003 | Attempt to apply filters for flights with invalid selections | User logged in as <Role>, No filters applied | 1. Open the Flights tab<br>2. Select an invalid number of stops<br>3. Click on Apply Filters | Error message displayed indicating invalid selection | high |
| TC-011 | WF-004 | Attempt to apply filters for tours with invalid duration | User logged in as <Role>, No filters applied | 1. Open the Tours tab<br>2. Set duration to a negative value<br>3. Click on Apply Filters | Error message displayed indicating invalid duration | high |
| TC-012 | WF-005 | Attempt to apply filters for cars with no selections | User logged in as <Role>, No filters applied | 1. Open the Cars tab<br>2. Do not select any filters<br>3. Click on Apply Filters | Error message displayed indicating that at least one filter must be selected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 | WF-001 | Edge case: Set price range to maximum allowed values | User logged in as <Role>, No filters applied | 1. Open the filter section<br>2. Set price range to maximum values<br>3. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | medium |
| TC-014 | WF-004 | Edge case: Set tour duration to maximum allowed value | User logged in as <Role>, No filters applied | 1. Open the Tours tab<br>2. Set duration to maximum allowed value<br>3. Click on Apply Filters | Results update dynamically with the applied filters and the result count is displayed | medium |
| TC-015 | WF-007 | Edge case: Reset filters when none are applied | User logged in as <Role>, No filters applied | 1. Click on Reset All Filters button | No change in results, confirmation message displayed | low |

---

## Reviews & Ratings

Total: **5** (positive: 1, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit review with all required fields filled | User logged in as Authenticated User, User has completed a booking | 1. Navigate to the Submit Review page<br>2. Select star ratings for Overall experience and individual categories (Cleanliness, Service, Location)<br>3. Enter written feedback<br>4. Click on Submit Review button | Review submitted successfully and confirmation message displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Submit review without star ratings | User logged in as Authenticated User, User has completed a booking | 1. Navigate to the Submit Review page<br>2. Leave star ratings blank<br>3. Enter written feedback<br>4. Click on Submit Review button | Error message displayed indicating that star ratings are required | high |
| TC-004 | WF-001 | Submit review with invalid characters in written feedback | User logged in as Authenticated User, User has completed a booking | 1. Navigate to the Submit Review page<br>2. Select star ratings for Overall experience and individual categories (Cleanliness, Service, Location)<br>3. Enter written feedback with invalid characters (e.g., emojis)<br>4. Click on Submit Review button | Error message displayed indicating that invalid characters are not allowed | medium |
| TC-005 | WF-001 | Submit review with no written feedback | User logged in as Authenticated User, User has completed a booking | 1. Navigate to the Submit Review page<br>2. Select star ratings for Overall experience and individual categories (Cleanliness, Service, Location)<br>3. Leave written feedback blank<br>4. Click on Submit Review button | Error message displayed indicating that written feedback is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Submit review with maximum characters in written feedback | User logged in as Authenticated User, User has completed a booking | 1. Navigate to the Submit Review page<br>2. Select star ratings for Overall experience and individual categories (Cleanliness, Service, Location)<br>3. Enter written feedback with maximum allowed characters<br>4. Click on Submit Review button | Review submitted successfully and confirmation message displayed | medium |

---

## Offers & Deals

Total: **5** (positive: 1, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid offer with newsletter subscription | User logged in as Customer, On Offers page | 1. Select 'Hotels' from Service_Type_Filter<br>2. Enter 'New York' in Destination_Filter<br>3. Select '2023-12-01' as Travel_Dates_Filter<br>4. Enter 'user@example.com' in Newsletter_Subscription<br>5. Click 'Book Now' | Promotional code is applied automatically or redirected to pre-filled search with discounted rates. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Submit offer without newsletter subscription | User logged in as Customer, On Offers page | 1. Select 'Flights' from Service_Type_Filter<br>2. Enter 'Los Angeles' in Destination_Filter<br>3. Select '2023-12-15' as Travel_Dates_Filter<br>4. Leave Newsletter_Subscription empty<br>5. Click 'Book Now' | Error message displayed indicating that newsletter subscription is required. | high |
| TC-003 | WF-001 | Submit offer with invalid email format | User logged in as Customer, On Offers page | 1. Select 'Packages' from Service_Type_Filter<br>2. Enter 'Miami' in Destination_Filter<br>3. Select '2023-11-20' as Travel_Dates_Filter<br>4. Enter 'invalid-email' in Newsletter_Subscription<br>5. Click 'Book Now' | Error message displayed indicating invalid email format. | medium |
| TC-005 | WF-001 | Submit offer with past travel date | User logged in as Customer, On Offers page | 1. Select 'Flights' from Service_Type_Filter<br>2. Enter 'Tokyo' in Destination_Filter<br>3. Select '2022-01-01' as Travel_Dates_Filter<br>4. Enter 'user@example.com' in Newsletter_Subscription<br>5. Click 'Book Now' | Error message displayed indicating that travel date cannot be in the past. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Submit offer with maximum character limit in newsletter subscription | User logged in as Customer, On Offers page | 1. Select 'Hotels' from Service_Type_Filter<br>2. Enter 'Paris' in Destination_Filter<br>3. Select '2023-12-25' as Travel_Dates_Filter<br>4. Enter 'a'.repeat(254) + '@example.com' in Newsletter_Subscription<br>5. Click 'Book Now' | Promotional code is applied automatically or redirected to pre-filled search with discounted rates. | low |

---

## Logout

Total: **5** (positive: 1, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful logout and session termination | User logged in as <Role> | 1. Click the Logout button | User is redirected to the home page and session data is cleared | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Access protected page after logout | User logged out | 1. Attempt to access a protected page | User is redirected to the login page | high |
| TC-003 | WF-001 | Logout button is not visible when user is logged out | User logged out | 1. Check for the presence of the Logout button | Logout button is not visible | medium |
| TC-004 | WF-001 | Attempt to logout when already logged out | User logged out | 1. Click the Logout button | No action taken, remains on the current page | low |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Check session data after logout | User logged in as <Role> | 1. Click the Logout button<br>2. Attempt to access session data | Session data is cleared and not accessible | medium |

---
