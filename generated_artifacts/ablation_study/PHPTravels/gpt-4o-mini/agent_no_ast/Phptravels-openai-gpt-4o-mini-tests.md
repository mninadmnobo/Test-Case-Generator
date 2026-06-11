# Test Cases — Phptravels

Generated: 2026-06-10T20:34:50.837723Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 235 | 65 | 97 | 73 | 125 | 55 | 49 |

## Home Page & Search

Total: **16** (positive: 4, negative: 4, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Hotels with valid inputs | User logged in as <role> | 1. Click on the Hotels tab<br>2. Enter <destination> in the Destination field<br>3. Enter <check-in date> in the Check-in field<br>4. Enter <check-out date> in the Check-out field<br>5. Select <number of rooms> from the Number of Rooms dropdown<br>6. Enter <number of adults> in the Adults field<br>7. Enter <number of children> in the Children field<br>8. Click the Search button | Redirected to Hotels results listing page | high |
| TC-002 | WF-002 | Search for Flights with valid inputs | User logged in as <role> | 1. Click on the Flights tab<br>2. Select <trip type> from the Trip Type dropdown<br>3. Enter <departure city> in the Departure City field<br>4. Enter <arrival city> in the Arrival City field<br>5. Enter <departure date> in the Departure Date field<br>6. Enter <return date> in the Return Date field<br>7. Select <number of adults> in the Adults field<br>8. Select <number of children> in the Children field<br>9. Select <number of infants> in the Infants field<br>10. Select <cabin class> from the Cabin Class dropdown<br>11. Click the Search button | Redirected to Flights results listing page | high |
| TC-003 | WF-003 | Search for Tours with valid inputs | User logged in as <role> | 1. Click on the Tours tab<br>2. Enter <destination> in the Destination field<br>3. Enter <start date> in the Start Date field<br>4. Enter <end date> in the End Date field<br>5. Click the Search button | Redirected to Tours results listing page | high |
| TC-004 | WF-004 | Search for Cars with valid inputs | User logged in as <role> | 1. Click on the Cars tab<br>2. Enter <pick-up location> in the Pick-up Location field<br>3. Enter <drop-off location> in the Drop-off Location field<br>4. Enter <pick-up date and time> in the Pick-up Date and Time field<br>5. Enter <drop-off date and time> in the Drop-off Date and Time field<br>6. Click the Search button | Redirected to Cars results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to search hotels with required fields empty |  | 1. Click on the Hotels tab<br>2. Leave the destination field blank<br>3. Leave the check-in date field blank<br>4. Leave the check-out date field blank<br>5. Leave the number of rooms field blank<br>6. Leave the guest count fields (adults and children) blank<br>7. Click the Search button | Inline validation errors appear on the destination, check-in date, check-out date, number of rooms, and guest count fields indicating they are required | high |
| TC-006 | WF-002 | Attempt to search flights with required fields empty |  | 1. Click on the Flights tab<br>2. Leave the trip type field blank<br>3. Leave the departure city field blank<br>4. Leave the arrival city field blank<br>5. Leave the travel dates field blank<br>6. Leave the passenger count fields (adults, children, infants) blank<br>7. Leave the cabin class field blank<br>8. Click the Search button | Inline validation errors appear on the trip type, departure city, arrival city, travel dates, passenger count, and cabin class fields indicating they are required | high |
| TC-007 | WF-003 | Attempt to search tours with required fields empty |  | 1. Click on the Tours tab<br>2. Leave the destination field blank<br>3. Leave the travel date range field blank<br>4. Click the Search button | Inline validation errors appear on the destination and travel date range fields indicating they are required | high |
| TC-008 | WF-004 | Attempt to search cars with required fields empty |  | 1. Click on the Cars tab<br>2. Leave the pick-up location field blank<br>3. Leave the drop-off location field blank<br>4. Leave the pick-up date and time field blank<br>5. Leave the drop-off date and time field blank<br>6. Click the Search button | Inline validation errors appear on the pick-up location, drop-off location, pick-up date and time, and drop-off date and time fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Search Hotels with maximum guest count |  | 1. Click on the Hotels tab<br>2. Enter a destination<br>3. Enter check-in date<br>4. Enter check-out date<br>5. Enter maximum number of rooms<br>6. Enter maximum guest count (adults and children) | Form submits successfully; redirected to Hotels results listing page | medium |
| TC-010 (boundary) | WF-001 | Search Hotels with one unit over maximum guest count |  | 1. Click on the Hotels tab<br>2. Enter a destination<br>3. Enter check-in date<br>4. Enter check-out date<br>5. Enter maximum number of rooms<br>6. Enter guest count (adults and children) exceeding the limit by one | Search button is blocked; inline error shown for guest count | medium |
| TC-011 (boundary) | WF-002 | Search Flights with maximum passenger count |  | 1. Click on the Flights tab<br>2. Select trip type<br>3. Enter departure city<br>4. Enter arrival city<br>5. Enter travel dates<br>6. Enter maximum passenger count (adults, children, infants) | Form submits successfully; redirected to Flights results listing page | medium |
| TC-012 (boundary) | WF-002 | Search Flights with one unit over maximum passenger count |  | 1. Click on the Flights tab<br>2. Select trip type<br>3. Enter departure city<br>4. Enter arrival city<br>5. Enter travel dates<br>6. Enter passenger count exceeding the limit by one | Search button is blocked; inline error shown for passenger count | medium |
| TC-013 (boundary) | WF-003 | Search Tours with valid travel date range |  | 1. Click on the Tours tab<br>2. Enter destination<br>3. Enter valid travel date range | Form submits successfully; redirected to Tours results listing page | medium |
| TC-014 (boundary) | WF-003 | Search Tours with invalid travel date range |  | 1. Click on the Tours tab<br>2. Enter destination<br>3. Enter travel date range where end date is before start date | Search button is blocked; inline error shown for travel date range | medium |
| TC-015 (boundary) | WF-004 | Search Cars with valid pick-up and drop-off dates |  | 1. Click on the Cars tab<br>2. Enter pick-up location<br>3. Enter drop-off location<br>4. Enter valid pick-up date and time<br>5. Enter valid drop-off date and time | Form submits successfully; redirected to Cars results listing page | medium |
| TC-016 (boundary) | WF-004 | Search Cars with invalid pick-up and drop-off dates |  | 1. Click on the Cars tab<br>2. Enter pick-up location<br>3. Enter drop-off location<br>4. Enter pick-up date and time in the past<br>5. Enter drop-off date and time before pick-up date and time | Search button is blocked; inline error shown for pick-up and drop-off dates | medium |

---

## User Registration

Total: **18** (positive: 2, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with automatic login | User logged in as <New User> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid password> in the Password field<br>5. Enter <valid password> in the Confirm Password field<br>6. Enter <valid mobile number> in the Mobile Number field<br>7. Select <country code> from the Country Code dropdown<br>8. Enter <Address> in the Address field<br>9. Select <Country> from the Country dropdown<br>10. Check the Terms and Conditions checkbox<br>11. Click Submit | Account created; user logged in and redirected to dashboard | high |
| TC-002 | WF-002 | Successful registration with email verification | User logged in as <New User> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <unique valid email> in the Email field<br>4. Enter <valid password> in the Password field<br>5. Enter <valid password> in the Confirm Password field<br>6. Enter <valid mobile number> in the Mobile Number field<br>7. Select <country code> from the Country Code dropdown<br>8. Enter <Address> in the Address field<br>9. Select <Country> from the Country dropdown<br>10. Check the Terms and Conditions checkbox<br>11. Click Submit | Account created; verification email sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-005 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-006 |  | Leave the Password field blank |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Leave the Confirm Password field blank |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-008 |  | Leave the Mobile Number field blank |  | 1. Leave the Mobile Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mobile Number field indicating it is required | high |
| TC-009 |  | Leave the Address field blank |  | 1. Leave the Address field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Address field indicating it is required | high |
| TC-010 |  | Leave the Country field blank |  | 1. Leave the Country field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Country field indicating it is required | high |
| TC-011 |  | Leave the Terms and Conditions checkbox unchecked |  | 1. Leave the Terms and Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Terms and Conditions field indicating it must be accepted | high |
| TC-012 |  | Enter an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Email field displays an error: 'Must be a valid email address' | medium |
| TC-013 |  | Enter mismatched passwords |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Confirm Password field indicating passwords do not match | medium |
| TC-014 |  | Submit with an already registered email |  | 1. Enter <already registered email> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Email field displays an error: 'Email already in use' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (input_edge) |  | Enter a very long first name |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; inline error indicates the first name is too long | low |
| TC-016 (input_edge) |  | Enter special characters in the Last Name |  | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; inline error indicates invalid characters in the last name | low |
| TC-017 (input_edge) |  | Enter leading and trailing whitespace in the Email field |  | 1. Enter '   user@example.com   ' in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved email shown on detail page has no extra spaces | low |
| TC-018 (input_edge) |  | Enter a zero in the Mobile Number field |  | 1. Enter '0' in the Mobile Number field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; inline error indicates mobile number cannot be zero | low |

---

## User Login

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | Redirect to dashboard or previously accessed page | high |
| TC-002 | WF-002 | Login with invalid credentials | User logged in as <User> | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | Show error message and clear password field | high |
| TC-003 | WF-003 | Login after multiple failed attempts requiring CAPTCHA | User logged in as <User>, User has made multiple failed login attempts | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | Show CAPTCHA verification | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Enter <valid password> in the Password field<br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Enter <valid email> in the Email field<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | Error is displayed indicating invalid credentials and the Password field is cleared | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Enter <valid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Error is displayed indicating invalid credentials and the Password field is cleared | medium |
| TC-008 | WF-003 | Attempt login after multiple failed attempts without CAPTCHA verification |  | 1. Enter <valid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login<br>4. Repeat steps 1-3 multiple times | After multiple failed attempts, CAPTCHA verification is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Enter valid email format but with an invalid domain |  | 1. Enter 'user@invalid_domain' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click the Login button | Error message displays indicating invalid email domain; password field is cleared | medium |
| TC-010 (boundary) | WF-002 | Enter email with maximum allowed length |  | 1. Enter a valid email with maximum length in the Email field<br>2. Enter a valid password in the Password field<br>3. Click the Login button | Error message displays indicating invalid credentials; password field is cleared | medium |
| TC-011 (interaction_edge) | WF-003 | Attempt login after multiple failed attempts | User has failed to login 5 times consecutively | 1. Enter valid email in the Email field<br>2. Enter invalid password in the Password field<br>3. Click the Login button | CAPTCHA verification is shown to the user | medium |
| TC-012 (input_edge) |  | Enter email with special characters |  | 1. Enter 'user!#$%&'*+/=?^_`{|}~@example.com' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click the Login button | Error message displays indicating invalid email format; password field is cleared | low |

---

## Forgot Password

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit existing email for password reset | User logged in as <User>, Email <valid email> exists in the system | 1. Enter <valid email> in the Email field<br>2. Click the Reset Password button | Reset link sent; confirmation message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-003 | WF-002 | Submit an email that does not exist in the system |  | 1. Enter <nonexistent email> in the Email field<br>2. Click Reset Password | Error shown; form remains editable | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (boundary) | WF-001 | Submit email that exists in the system |  | 1. Enter a valid email address that exists in the system in the Email field<br>2. Click the Reset Password button | Reset link sent; confirmation message shown | medium |
| TC-005 (boundary) | WF-002 | Submit email that does not exist in the system |  | 1. Enter an invalid email address that does not exist in the system in the Email field<br>2. Click the Reset Password button | Error shown; form remains editable | medium |
| TC-006 (input_edge) |  | Enter a very long email address |  | 1. Enter a string longer than typical email length (200+ characters) in the Email field<br>2. Click the Reset Password button | Form submits successfully or shows an error indicating the email is too long | low |
| TC-007 (input_edge) |  | Enter email with special characters |  | 1. Enter an email address with special characters (e.g., !#$%&'*+/=?^_`{|}~) in the Email field<br>2. Click the Reset Password button | Form submits successfully or shows an error indicating invalid email format | low |

---

## Hotels Search & Listing

Total: **15** (positive: 8, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search hotels with specified criteria | User logged in as <Role> | 1. Enter <destination> in the Destination field<br>2. Select <check-in date> in the Check-in field<br>3. Select <check-out date> in the Check-out field<br>4. Enter <number of rooms> in the Rooms field<br>5. Enter <number of adults> in the Adults field<br>6. Enter <number of children> in the Children field<br>7. Click the Search button | Redirected to the listing page | high |
| TC-002 | WF-002 | Filter results by price range | User logged in as <Role>, Search hotels with specified criteria | 1. Adjust the price range slider to <desired range><br>2. Click the Apply Filter button | Results updated dynamically | medium |
| TC-003 | WF-003 | Sort results by price low to high | User logged in as <Role>, Search hotels with specified criteria | 1. Select 'Price: Low to High' from the Sort dropdown | Results sorted by price low to high | medium |
| TC-004 | WF-004 | Sort results by price high to low | User logged in as <Role>, Search hotels with specified criteria | 1. Select 'Price: High to Low' from the Sort dropdown | Results sorted by price high to low | medium |
| TC-005 | WF-005 | Sort results by star rating | User logged in as <Role>, Search hotels with specified criteria | 1. Select 'Star Rating' from the Sort dropdown | Results sorted by star rating | medium |
| TC-006 | WF-006 | Sort results by guest rating | User logged in as <Role>, Search hotels with specified criteria | 1. Select 'Guest Rating' from the Sort dropdown | Results sorted by guest rating | medium |
| TC-007 | WF-007 | Remove individual filter | User logged in as <Role>, Search hotels with specified criteria, Apply a price range filter | 1. Click the Remove button on the active price range filter | Filter removed and results updated | medium |
| TC-008 | WF-008 | Reset all filters | User logged in as <Role>, Search hotels with specified criteria, Apply multiple filters | 1. Click the Reset All Filters button | All filters reset and results updated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave all search fields blank and submit |  | 1. Leave the <Destination> field blank<br>2. Leave the <Check-in Date> field blank<br>3. Leave the <Check-out Date> field blank<br>4. Leave the <Number of Rooms> field blank<br>5. Leave the <Guest Count> field blank<br>6. Click Search | Inline validation error appears on the <Destination> field indicating it is required; form does not submit |  |
| TC-010 | WF-002 | Attempt to apply a filter without selecting a price range |  | 1. Open the filter sidebar<br>2. Leave the <Price Range> filter blank<br>3. Click Apply Filter | Inline validation error appears on the <Price Range> filter indicating it is required; results are not updated |  |
| TC-011 | WF-008 | Attempt to reset filters when no filters are applied |  | 1. Click Reset Filters | No filters to reset; results remain unchanged |  |
| TC-012 | WF-007 | Attempt to remove a filter when no filters are applied |  | 1. Click Remove Filter | No filters to remove; results remain unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapid re-submission after redirect | Search hotels with valid criteria | 1. Submit the hotel search form<br>2. After being redirected to the listing page, quickly press the browser back button | The hotel search form is shown blank, without pre-filled values | medium |
| TC-014 (input_edge) |  | Leading/trailing whitespace in destination field | Ensure the destination field is present | 1. Enter '  New York  ' in the destination field<br>2. Fill in other required fields<br>3. Submit the form | Leading/trailing whitespace is trimmed; 'New York' is displayed in the search results | low |
| TC-015 (input_edge) |  | Special characters in destination field | Ensure the destination field is present | 1. Enter '@#$%^&*()' in the destination field<br>2. Fill in other required fields<br>3. Submit the form | An error is shown indicating that the destination is invalid | low |

---

## Hotel Details & Booking

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book a room successfully with valid details | User logged in as <Role>, Room type is selected with valid stay dates and guest count | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Enter <optional special requests> in the Special Requests field<br>6. Click Book Now | Proceeds to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to book a room while logged out | User is not logged in | 1. Navigate to the hotel details page<br>2. Select a room<br>3. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User is logged in, User has selected a room and filled out the booking form | 1. Click Book Now<br>2. After successful submission, press the browser back button | The booking form is shown blank, not pre-filled with previous data. | medium |
| TC-004 (input_edge) |  | Long text in Special Requests | User is logged in, User has selected a room and filled out the booking form | 1. Enter a very long string (200+ characters) in the Special Requests field | The form either accepts the input or truncates it with a visible indicator. | low |
| TC-005 (input_edge) |  | Leading/trailing whitespace in First Name | User is logged in, User has selected a room and filled out the booking form | 1. Enter '   John   ' in the First Name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Flights Search & Listing

Total: **11** (positive: 1, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid flight search form | User logged in as <Role> | 1. Select 'Round-trip' as the trip type<br>2. Enter <departure city> in the Departure City field<br>3. Enter <arrival city> in the Arrival City field<br>4. Select <valid departure date> from the Departure Date calendar<br>5. Select <valid return date> from the Return Date calendar<br>6. Enter <number of adults> in the Adults field<br>7. Enter <number of children> in the Children field<br>8. Enter <number of infants> in the Infants field<br>9. Select 'Economy' from the Cabin Class dropdown<br>10. Click the Submit button | Redirected to the listing page with search results | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the trip type blank and submit |  | 1. Leave the Trip Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Trip Type field indicating it is required | high |
| TC-003 | WF-001 | Leave the departure city blank and submit |  | 1. Leave the Departure City field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-004 | WF-001 | Leave the arrival city blank and submit |  | 1. Leave the Arrival City field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Arrival City field indicating it is required | high |
| TC-005 | WF-001 | Leave the travel dates blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-006 | WF-001 | Leave the passenger count blank and submit |  | 1. Leave the Passenger Count field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Passenger Count field indicating it is required | high |
| TC-007 | WF-001 | Leave the cabin class blank and submit |  | 1. Leave the Cabin Class field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Cabin Class field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Submit flight search form with maximum passenger count |  | 1. Select 'Round-trip' as trip type<br>2. Enter 'New York' as departure city<br>3. Enter 'Los Angeles' as arrival city<br>4. Select today's date as departure date<br>5. Select a return date one week from today<br>6. Enter maximum allowed number of adults in the passenger count<br>7. Click Submit | Redirected to the listing page with search results for maximum adults | medium |
| TC-009 (boundary) | WF-001 | Submit flight search form with one unit over maximum passenger count |  | 1. Select 'Round-trip' as trip type<br>2. Enter 'New York' as departure city<br>3. Enter 'Los Angeles' as arrival city<br>4. Select today's date as departure date<br>5. Select a return date one week from today<br>6. Enter maximum allowed number of adults plus one in the passenger count<br>7. Click Submit | Form submission is blocked; error message displayed indicating passenger count exceeds limit | medium |
| TC-010 (input_edge) |  | Enter long text in departure city |  | 1. Select 'Round-trip' as trip type<br>2. Enter a very long string (200+ characters) in the departure city field<br>3. Enter 'Los Angeles' as arrival city<br>4. Select today's date as departure date<br>5. Select a return date one week from today<br>6. Enter 1 in the adult passenger count<br>7. Click Submit | Form submission is blocked; error message displayed indicating the departure city is too long | low |
| TC-011 (input_edge) |  | Enter special characters in arrival city |  | 1. Select 'Round-trip' as trip type<br>2. Enter '@Los Angeles!' as arrival city<br>3. Enter 'New York' as departure city<br>4. Select today's date as departure date<br>5. Select a return date one week from today<br>6. Enter 1 in the adult passenger count<br>7. Click Submit | Form submission is blocked; error message displayed indicating invalid characters in the arrival city | low |

---

## Flight Booking

Total: **11** (positive: 1, negative: 7, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit booking form with valid data | User logged in as <Role> | 1. Enter 'Mr' in the Title field<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid date of birth> in the Date of Birth field<br>5. Enter <valid passport number> in the Passport Number field<br>6. Enter <valid passport expiry> in the Passport Expiry field<br>7. Enter <valid email> in the Email field<br>8. Enter <valid phone number> in the Phone field<br>9. Click Continue | Redirects to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the first name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the First Name field indicating it is required | high |
| TC-003 |  | Leave the last name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-004 |  | Leave the email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the phone field blank and submit |  | 1. Leave the Phone field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Phone field indicating it is required | high |
| TC-006 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Continue | Email field displays an error: 'Must be a valid email address' | medium |
| TC-007 |  | Enter a past date in the date of birth field and submit |  | 1. Enter <past date> in the Date of Birth field<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Date of Birth field indicating it is invalid | medium |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Continue | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (input_edge) |  | Enter a very long first name |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields<br>3. Click Continue | Form submission is blocked; inline error shown indicating the first name exceeds the maximum length | low |
| TC-010 (input_edge) |  | Enter special characters in the last name |  | 1. Enter special characters (e.g., @#$%^&*) in the Last Name field<br>2. Fill all other required fields<br>3. Click Continue | Form submission is blocked; inline error shown indicating invalid characters in the last name | low |
| TC-011 (input_edge) |  | Enter leading and trailing whitespace in the email field |  | 1. Enter '   example@example.com   ' in the Email field<br>2. Fill all other required fields<br>3. Click Continue | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Tours Search & Listing

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid tours search form | User logged in as <Role> | 1. Enter <destination> in the Destination field<br>2. Select <start date> in the Start Date field<br>3. Select <end date> in the End Date field<br>4. Select <tour type> from the Tour Type dropdown<br>5. Enter <duration> in the Duration field<br>6. Enter <budget range> in the Budget Range field<br>7. Click Submit | Redirected to the listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave all fields in the tours search form blank and submit |  | 1. Leave the <Destination> field blank<br>2. Leave the <Travel Dates> field blank<br>3. Leave the <Tour Type> field blank<br>4. Leave the <Duration> field blank<br>5. Leave the <Budget Range> field blank<br>6. Click Submit | Form does not submit; error shown on all required fields indicating they are required | high |
| TC-003 | WF-001 | Enter invalid data in the Budget Range field and submit |  | 1. Enter <invalid budget format> in the <Budget Range> field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; <Budget Range> field displays an error: 'Must be a valid budget range' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (input_edge) | WF-001 | Enter a very long destination name |  | 1. Enter a string of 200+ characters in the Destination field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; destination field displays the full input without truncation | low |
| TC-005 (input_edge) | WF-001 | Enter special characters in the budget field |  | 1. Enter '$$$' in the Budget field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; an error message indicates invalid characters in the Budget field | low |
| TC-006 (input_edge) | WF-001 | Enter a budget value with leading/trailing whitespace |  | 1. Enter ' 1000 ' in the Budget field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in the listing page displays '1000' | low |

---

## Tour Details & Booking

Total: **6** (positive: 2, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book Now as an authenticated user | User logged in as <Authenticated User> | 1. Select a departure date from the available options<br>2. Enter <number of adults> in the adults field<br>3. Enter <number of children> in the children field<br>4. Click 'Book Now' | Booking form displayed with total cost breakdown | high |
| TC-002 | WF-002 | Book Now as an unauthenticated user |  | 1. Select a departure date from the available options<br>2. Enter <number of adults> in the adults field<br>3. Enter <number of children> in the children field<br>4. Click 'Book Now' | Redirected to login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Unauthenticated user attempts to book a tour |  | 1. Navigate to the tour details page<br>2. Select a departure date<br>3. Specify the number of travelers<br>4. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-002 | Book Now as an unauthenticated user | User is not logged in | 1. Navigate to the tour details page<br>2. Select a departure date<br>3. Specify the number of travelers<br>4. Click Book Now | User is redirected to the login page | medium |
| TC-005 (interaction_edge) | WF-001 | Book Now as an authenticated user | User is logged in | 1. Navigate to the tour details page<br>2. Select a departure date<br>3. Specify the number of travelers<br>4. Click Book Now | Booking form is displayed with total cost breakdown | medium |
| TC-006 (input_edge) |  | Enter a very long name in traveler names field | Booking form is displayed | 1. Enter a string of 200+ characters in the traveler names field | The system either accepts the input or truncates it with a visible indicator | low |

---

## Cars Search & Listing

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit car rental search form with valid inputs | User logged in as <Role> | 1. Enter <pick-up location> in the Pick-up Location field<br>2. Enter <drop-off location> in the Drop-off Location field<br>3. Select <pick-up date and time> in the Pick-up Date and Time field<br>4. Select <drop-off date and time> in the Drop-off Date and Time field<br>5. Enter <driver age> in the Driver Age field<br>6. Click Submit on the search form | Redirected to the listing page with vehicle categories | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave all fields in the car rental search form blank |  | 1. Leave the pick-up location field blank<br>2. Leave the drop-off location field blank<br>3. Leave the pick-up date field blank<br>4. Leave the drop-off date field blank<br>5. Leave the driver age field blank<br>6. Click Submit | Form does not submit; inline validation errors appear on all required fields indicating they are required | high |
| TC-003 | WF-001 | Submit the car rental search form with invalid date formats |  | 1. Enter <invalid date format> in the pick-up date field<br>2. Enter <invalid date format> in the drop-off date field<br>3. Enter <valid location> in the pick-up location field<br>4. Enter <valid location> in the drop-off location field<br>5. Enter <valid age> in the driver age field<br>6. Click Submit | Form does not submit; inline validation errors appear on the pick-up and drop-off date fields indicating invalid date format | medium |
| TC-004 | WF-001 | Submit the car rental search form with an invalid driver age |  | 1. Enter <valid location> in the pick-up location field<br>2. Enter <valid location> in the drop-off location field<br>3. Enter <valid date> in the pick-up date field<br>4. Enter <valid date> in the drop-off date field<br>5. Enter <invalid driver age> in the driver age field<br>6. Click Submit | Form does not submit; inline validation error appears on the driver age field indicating it must be a valid age | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) | WF-001 | Enter a very long pick-up location |  | 1. Enter a string of 200+ characters in the pick-up location field<br>2. Fill in the drop-off location, pick-up date, drop-off date, and driver age<br>3. Click Submit | Form submits successfully; the pick-up location is displayed correctly on the listing page | low |
| TC-006 (input_edge) | WF-001 | Enter special characters in the drop-off location |  | 1. Enter '!@#$%^&*()' in the drop-off location field<br>2. Fill in the pick-up location, pick-up date, drop-off date, and driver age<br>3. Click Submit | Form submits successfully; the drop-off location is displayed correctly on the listing page | low |
| TC-007 (input_edge) | WF-001 | Enter leading and trailing whitespace in the pick-up location |  | 1. Enter '   New York   ' in the pick-up location field<br>2. Fill in the drop-off location, pick-up date, drop-off date, and driver age<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Car Booking

Total: **12** (positive: 1, negative: 8, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm Booking with valid input | User logged in as <Role> | 1. Enter <full name> in the Driver Full Name field<br>2. Enter <age> in the Age field<br>3. Enter <license number> in the License Number field<br>4. Select <license issue country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Select <insurance plan> from the Insurance Plan options<br>8. Check the GPS add-on option<br>9. Check the Child Seat add-on option<br>10. Check the Additional Driver add-on option<br>11. Accept the terms and conditions<br>12. Click Confirm Booking | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the driver full name blank |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 | WF-001 | Leave the age field blank |  | 1. Leave the Age field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-004 | WF-001 | Leave the license number field blank |  | 1. Leave the License Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-005 | WF-001 | Leave the license issue country field blank |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-006 | WF-001 | Leave the email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 | WF-001 | Leave the phone number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-008 | WF-001 | Enter an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Email field displays an error: 'Must be a valid email address' | medium |
| TC-009 | WF-001 | Enter an age below the minimum requirement |  | 1. Enter <age below minimum> in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it does not meet the minimum age requirement | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (input_edge) |  | Enter a very long name in the driver full name field |  | 1. Enter a string of 200+ characters in the Driver Full Name field | The form displays an error indicating the name is too long | low |
| TC-011 (input_edge) |  | Enter special characters in the email field |  | 1. Enter 'user@domain!#.com' in the Email field | The form displays an error indicating invalid email format | low |
| TC-012 (input_edge) |  | Enter leading and trailing whitespace in the phone number field |  | 1. Enter '   1234567890   ' in the Phone Number field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Visa Services

Total: **16** (positive: 3, negative: 10, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View visa requirements for selected nationality and destination | User logged in as <Role> | 1. Select <Nationality> from the Nationality dropdown<br>2. Select <Destination Country> from the Destination Country dropdown<br>3. Click 'View Requirements' | Visa requirements displayed for selected nationality and destination | high |
| TC-002 | WF-002 | Submit visa application with valid details | User logged in as <Role>, Visa requirements are displayed | 1. Enter <Full Name> in the Full Name field<br>2. Enter <Passport Number> in the Passport Number field<br>3. Enter <Passport Expiry Date> in the Passport Expiry Date field<br>4. Enter <Date of Birth> in the Date of Birth field<br>5. Select <Nationality> from the Nationality dropdown<br>6. Enter <Email> in the Email field<br>7. Enter <Phone> in the Phone field<br>8. Select <Purpose of Visit> from the Purpose of Visit dropdown<br>9. Enter <Intended Travel Dates> in the Intended Travel Dates field<br>10. Enter <Duration of Stay> in the Duration of Stay field<br>11. Upload <valid passport copy> in the Document Upload section<br>12. Upload <valid photographs> in the Document Upload section<br>13. Click 'Submit Application' | Application submitted; confirmation message shown | high |
| TC-003 | WF-003 | Track application status after submission | User logged in as <Role>, Application has been submitted | 1. Navigate to the Bookings section of the dashboard<br>2. Click on 'Track Application Status' | Application status displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the full name field blank and submit |  | 1. Leave the Full Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Full Name field indicating it is required | high |
| TC-005 |  | Leave the passport number field blank and submit |  | 1. Leave the Passport Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Passport Number field indicating it is required | high |
| TC-006 |  | Leave the passport expiry date field blank and submit |  | 1. Leave the Passport Expiry Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Passport Expiry Date field indicating it is required | high |
| TC-007 |  | Leave the date of birth field blank and submit |  | 1. Leave the Date of Birth field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Date of Birth field indicating it is required | high |
| TC-008 |  | Leave the email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 |  | Leave the phone field blank and submit |  | 1. Leave the Phone field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Phone field indicating it is required | high |
| TC-010 |  | Leave the purpose of visit field blank and submit |  | 1. Leave the Purpose of Visit field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Purpose of Visit field indicating it is required | high |
| TC-011 |  | Leave the intended travel dates field blank and submit |  | 1. Leave the Intended Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Intended Travel Dates field indicating it is required | high |
| TC-012 |  | Leave the duration of stay field blank and submit |  | 1. Leave the Duration of Stay field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Duration of Stay field indicating it is required | high |
| TC-013 |  | Upload an invalid file type in the document upload section |  | 1. Select an invalid file type for upload<br>2. Click Submit | Inline validation error appears indicating the file type is not allowed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (input_edge) |  | Enter a very long name in the full name field |  | 1. Enter a string of 200+ characters in the Full Name field | Form submits successfully; saved value displayed in detail page shows the full name as entered or truncated with an indicator | low |
| TC-015 (input_edge) |  | Enter special characters in the email field |  | 1. Enter a string with special characters in the Email field | Email field displays an error indicating invalid format | low |
| TC-016 (input_edge) |  | Enter leading and trailing whitespace in the phone field |  | 1. Enter a phone number with leading and trailing spaces in the Phone field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## User Dashboard

Total: **29** (positive: 13, negative: 13, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Booking Details | User logged in as <Role>, User has at least one booking | 1. Click 'View Details' on a booking | Booking details displayed | high |
| TC-002 | WF-002 | Cancel Booking | User logged in as <Role>, User has a booking that can be cancelled | 1. Click 'Cancel' on a booking<br>2. Confirm cancellation | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify Booking | User logged in as <Role>, User has a booking that can be modified | 1. Click 'Modify' on a booking | Booking modification form displayed | high |
| TC-004 | WF-004 | Download Confirmation | User logged in as <Role>, User has a booking with a confirmation available | 1. Click 'Download' on a booking confirmation | Confirmation document downloaded | high |
| TC-005 | WF-005 | Edit Profile | User logged in as <Role> | 1. Click 'Edit' in My Profile section | Profile edit form displayed | high |
| TC-006 | WF-006 | View Wallet/Credits | User logged in as <Role> | 1. Click 'View' in Wallet/Credits section | Wallet/Credits information displayed | high |
| TC-007 | WF-007 | View Wishlist | User logged in as <Role> | 1. Click 'View' in Wishlist section | Wishlist displayed | high |
| TC-008 | WF-008 | Rate and Review Booking | User logged in as <Role>, User has a completed booking | 1. Click 'Rate and Review' on a completed booking<br>2. Submit a review | Review submitted; success message shown | high |
| TC-009 | WF-009 | Change Password | User logged in as <Role> | 1. Click 'Change Password' in Settings<br>2. Enter new password<br>3. Confirm new password<br>4. Submit | Password changed; success message shown | high |
| TC-010 | WF-010 | Update Notification Preferences | User logged in as <Role> | 1. Click 'Update Preferences' in Settings<br>2. Change notification settings<br>3. Submit | Notification preferences updated; success message shown | high |
| TC-011 | WF-011 | Change Default Currency | User logged in as <Role> | 1. Click 'Change Currency' in Settings<br>2. Select a new default currency<br>3. Submit | Default currency changed; success message shown | high |
| TC-012 | WF-012 | Change Default Language | User logged in as <Role> | 1. Click 'Change Language' in Settings<br>2. Select a new default language<br>3. Submit | Default language changed; success message shown | high |
| TC-013 | WF-013 | Logout | User logged in as <Role> | 1. Click 'Logout' | Session ended; user logged out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 | WF-001 | Attempt to view booking details without a valid booking reference |  | 1. Navigate to My Bookings<br>2. Click on View Details for a booking with an invalid reference | Error displayed indicating 'Invalid booking reference' | high |
| TC-015 | WF-002 | Attempt to cancel a booking that is already cancelled |  | 1. Navigate to My Bookings<br>2. Click on Cancel for a booking with status 'Cancelled' | Error displayed indicating 'Cannot cancel a booking that is already cancelled' | high |
| TC-016 | WF-003 | Attempt to modify a booking that is already cancelled |  | 1. Navigate to My Bookings<br>2. Click on Modify for a booking with status 'Cancelled' | Error displayed indicating 'Cannot modify a booking that is already cancelled' | high |
| TC-017 | WF-004 | Attempt to download confirmation for a booking that does not exist |  | 1. Navigate to My Bookings<br>2. Click on Download for a booking with an invalid reference | Error displayed indicating 'Booking not found' | high |
| TC-018 | WF-005 | Attempt to edit profile without being logged in |  | 1. Navigate to My Profile<br>2. Click on Edit | Redirected to login page | high |
| TC-019 | WF-006 | Attempt to view wallet/credits without being logged in |  | 1. Navigate to Wallet/Credits | Redirected to login page | high |
| TC-020 | WF-007 | Attempt to view wishlist without being logged in |  | 1. Navigate to Wishlist | Redirected to login page | high |
| TC-021 | WF-008 | Attempt to submit a review for a booking that does not exist |  | 1. Navigate to Reviews<br>2. Attempt to submit a review for a non-existent booking | Error displayed indicating 'Booking not found' | high |
| TC-022 | WF-009 | Attempt to change password without providing the current password |  | 1. Navigate to Settings<br>2. Click on Change Password<br>3. Leave the current password field blank<br>4. Enter a new password<br>5. Click Submit | Error displayed indicating 'Current password is required' | high |
| TC-023 | WF-010 | Attempt to update notification preferences without being logged in |  | 1. Navigate to Settings<br>2. Click on Update Preferences | Redirected to login page | high |
| TC-024 | WF-011 | Attempt to change default currency without being logged in |  | 1. Navigate to Settings<br>2. Click on Change Currency | Redirected to login page | high |
| TC-025 | WF-012 | Attempt to change default language without being logged in |  | 1. Navigate to Settings<br>2. Click on Change Language | Redirected to login page | high |
| TC-026 | WF-013 | Attempt to logout while already logged out |  | 1. Click on Logout | Error displayed indicating 'You are not logged in' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 (input_edge) |  | Enter a very long string in the profile name field | User is logged into the dashboard | 1. Navigate to My Profile<br>2. Click Edit<br>3. Enter a string longer than 200 characters in the name field | Profile edit form displays an error indicating the name exceeds the maximum allowed length | low |
| TC-028 (input_edge) |  | Enter special characters in the profile name field | User is logged into the dashboard | 1. Navigate to My Profile<br>2. Click Edit<br>3. Enter special characters in the name field | Profile edit form displays an error indicating invalid characters in the name field | low |
| TC-029 (input_edge) |  | Enter leading and trailing whitespace in the profile name field | User is logged into the dashboard | 1. Navigate to My Profile<br>2. Click Edit<br>3. Enter '   John Doe   ' in the name field<br>4. Save changes | Saved value shown in profile detail page has no leading or trailing spaces | low |

---

## Booking Management

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details | User logged in as <Role>, Booking is in a modifiable state | 1. Click the Modify button<br>2. Change the travel dates to <new dates><br>3. Add special requests: <special requests><br>4. Update traveler information with <new traveler details><br>5. Click Save | Booking details updated; success message shown | high |
| TC-002 | WF-002 | Cancel booking | User logged in as <Role>, Booking is in a cancellable state | 1. Click the Cancel button<br>2. Click Confirm on the cancellation confirmation dialog | Cancellation processed; refund initiated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to modify booking details without required fields |  | 1. Click on the Modify button<br>2. Leave all fields blank<br>3. Click Submit | Form does not submit; error shown indicating required fields must be filled | high |
| TC-004 | WF-002 | Attempt to cancel booking without confirming cancellation |  | 1. Click on the Cancel button<br>2. Leave the confirmation unchecked<br>3. Click Confirm | Cancellation is not processed; error shown indicating confirmation is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid re-submission of modified booking details | User is on the booking detail page with a Modify button available | 1. Click the Modify button<br>2. Change travel dates and submit the modification<br>3. Immediately click the Modify button again | Second modification attempt is blocked; the user remains on the modification page with a message indicating the modification is in progress. | medium |
| TC-006 (interaction_edge) | WF-002 | Cancel booking after modification | User has modified booking details successfully | 1. Click the Cancel button after modifying the booking<br>2. Confirm the cancellation | Cancellation processed; refund initiated and confirmation message shown. | medium |
| TC-007 (input_edge) |  | Long confirmation number input | User is on the booking detail page | 1. Enter a confirmation number with 200 characters in the confirmation field | Confirmation number input is accepted or truncated with a visible indicator. | low |
| TC-008 (input_edge) |  | Special characters in traveler details | User is on the booking detail page | 1. Enter special characters in the traveler details field | Traveler details input is accepted or a specific error is shown. | low |

---

## Payment Processing

Total: **17** (positive: 4, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with Credit/Debit Card | User logged in as <Role>, Booking summary is displayed with price breakdown | 1. Enter <cardholder name> in the Cardholder Name field<br>2. Enter <valid card number> in the Card Number field<br>3. Enter <valid expiration date> in the Expiration Date field<br>4. Enter <valid CVV> in the CVV field<br>5. Check the option to save the card for future use<br>6. Click Submit | User taken to booking confirmation page with reference number | high |
| TC-002 | WF-002 | Submit payment with PayPal | User logged in as <Role>, Booking summary is displayed with price breakdown | 1. Click on PayPal payment option<br>2. Enter <valid PayPal credentials><br>3. Click Submit | User taken to booking confirmation page with reference number | high |
| TC-003 | WF-003 | Submit payment with Bank Transfer | User logged in as <Role>, Booking summary is displayed with price breakdown | 1. Click on Bank Transfer payment option<br>2. Follow the instructions to complete the bank transfer<br>3. Click Submit | User taken to booking confirmation page with reference number | high |
| TC-004 | WF-004 | Submit payment with Wallet/Credits | User logged in as <Role>, Booking summary is displayed with price breakdown | 1. Click on Wallet/Credits payment option<br>2. Confirm the payment amount<br>3. Click Submit | User taken to booking confirmation page with reference number | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Submit payment with blank cardholder name |  | 1. Leave the Cardholder Name field blank<br>2. Fill in the Card Number, Expiration Date, and CVV<br>3. Click Submit | Inline validation error appears on the Cardholder Name field indicating it is required | high |
| TC-006 | WF-001 | Submit payment with blank card number |  | 1. Leave the Card Number field blank<br>2. Fill in the Cardholder Name, Expiration Date, and CVV<br>3. Click Submit | Inline validation error appears on the Card Number field indicating it is required | high |
| TC-007 | WF-001 | Submit payment with blank expiration date |  | 1. Leave the Expiration Date field blank<br>2. Fill in the Cardholder Name, Card Number, and CVV<br>3. Click Submit | Inline validation error appears on the Expiration Date field indicating it is required | high |
| TC-008 | WF-001 | Submit payment with blank CVV |  | 1. Leave the CVV field blank<br>2. Fill in the Cardholder Name, Card Number, and Expiration Date<br>3. Click Submit | Inline validation error appears on the CVV field indicating it is required | high |
| TC-009 | WF-001 | Submit payment with invalid card number format |  | 1. Enter <invalid card number format> in the Card Number field<br>2. Fill in the Cardholder Name, Expiration Date, and CVV<br>3. Click Submit | Error message displayed: 'Invalid card number' | medium |
| TC-010 | WF-001 | Submit payment with expired card |  | 1. Enter <valid cardholder name> in the Cardholder Name field<br>2. Enter <valid card number> in the Card Number field<br>3. Enter <expired date> in the Expiration Date field<br>4. Enter <valid CVV> in the CVV field<br>5. Click Submit | Error message displayed: 'Card declined' | medium |
| TC-011 | WF-002 | Submit payment with PayPal without logging in |  | 1. Click on PayPal payment option<br>2. Click Submit | User is redirected to PayPal login page | medium |
| TC-012 | WF-003 | Submit payment with Bank Transfer without sufficient funds |  | 1. Select Bank Transfer payment option<br>2. Click Submit | Error message displayed: 'Insufficient funds' | medium |
| TC-013 | WF-004 | Submit payment with Wallet/Credits exceeding balance |  | 1. Select Wallet/Credits payment option<br>2. Enter <amount exceeding wallet balance> in the payment amount field<br>3. Click Submit | Error message displayed: 'Insufficient balance in wallet' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (input_edge) | WF-001 | Enter a very long cardholder name |  | 1. Enter a very long string (200+ characters) in the Cardholder Name field<br>2. Fill in valid card number, expiration date, and CVV<br>3. Click Submit | Form submission is blocked; inline error message indicates the name exceeds the maximum length | low |
| TC-015 (input_edge) | WF-001 | Enter special characters in cardholder name |  | 1. Enter special characters (e.g., @#$%^&) in the Cardholder Name field<br>2. Fill in valid card number, expiration date, and CVV<br>3. Click Submit | Form submission is blocked; inline error message indicates invalid characters in the Cardholder Name | low |
| TC-016 (input_edge) | WF-001 | Enter whitespace in cardholder name |  | 1. Enter leading and trailing whitespace in the Cardholder Name field<br>2. Fill in valid card number, expiration date, and CVV<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown on the confirmation page has no extra spaces | low |
| TC-017 (input_edge) | WF-001 | Enter zero in the CVV field |  | 1. Enter '0' in the CVV field<br>2. Fill in valid cardholder name, card number, and expiration date<br>3. Click Submit | Form submission is blocked; inline error message indicates CVV must be a valid number | low |

---

## Currency & Language Selection

Total: **8** (positive: 4, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Select a currency and verify price updates | User logged in as <Authenticated User> | 1. Select <currency> from the currency dropdown | All prices displayed across the site update to reflect the selected <currency> | high |
| TC-002 |  | Select a language and verify interface change | User logged in as <Authenticated User> | 1. Select <language> from the language dropdown | The entire site interface switches to <language>, including navigation labels, form labels, and content | high |
| TC-003 |  | Select a currency as an unauthenticated user | User is not logged in | 1. Select <currency> from the currency dropdown | All prices displayed across the site update to reflect the selected <currency> | medium |
| TC-004 |  | Select a language as an unauthenticated user | User is not logged in | 1. Select <language> from the language dropdown | The entire site interface switches to <language>, including navigation labels, form labels, and content | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user attempts to change currency or language | User is not logged in | 1. Attempt to change currency<br>2. Attempt to change language | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long string in the language selector |  | 1. Open the language selector<br>2. Enter a string of 200+ characters | The input is either accepted or truncated with a visible indicator | low |
| TC-007 (input_edge) |  | Enter special characters in the currency selector |  | 1. Open the currency selector<br>2. Enter special characters like @#$%^&*() | The input is either accepted or a specific error is shown | low |
| TC-008 (input_edge) |  | Enter a value with leading and trailing whitespace in the language selector |  | 1. Open the language selector<br>2. Enter a value with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved value shown in the detail page has no extra spaces | low |

---

## Search & Filters

Total: **13** (positive: 8, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Apply price range filter | User logged in as <User Role> | 1. Adjust the price range slider to select a range<br>2. Observe the results grid | Results update dynamically to reflect listings within the selected price range; result count updates accordingly | high |
| TC-002 |  | Apply star rating filter | User logged in as <User Role> | 1. Select a star rating from the ratings filter<br>2. Observe the results grid | Results update dynamically to show only listings with the selected star rating; result count updates accordingly | high |
| TC-003 |  | Apply hotel-specific filters | User logged in as <User Role> | 1. Select a hotel type from the hotel type filter<br>2. Select amenities from the facilities/amenities filter<br>3. Observe the results grid | Results update dynamically to reflect only hotels matching the selected type and amenities; result count updates accordingly | high |
| TC-004 |  | Apply flight-specific filters | User logged in as <User Role> | 1. Select an airline from the airlines filter<br>2. Adjust the number of stops filter<br>3. Observe the results grid | Results update dynamically to show only flights matching the selected airline and number of stops; result count updates accordingly | high |
| TC-005 |  | Apply tour-specific filters | User logged in as <User Role> | 1. Select a tour type from the tour type filter<br>2. Adjust the duration filter<br>3. Observe the results grid | Results update dynamically to reflect only tours matching the selected type and duration; result count updates accordingly | high |
| TC-006 |  | Apply car-specific filters | User logged in as <User Role> | 1. Select a car type from the car type filter<br>2. Select a transmission type from the transmission filter<br>3. Observe the results grid | Results update dynamically to show only cars matching the selected type and transmission; result count updates accordingly | high |
| TC-007 |  | Remove individual active filter | User logged in as <User Role>, At least one filter is active | 1. Click the remove button next to an active filter<br>2. Observe the results grid | Results update dynamically to reflect the removal of the filter; result count updates accordingly | high |
| TC-008 |  | Reset all filters | User logged in as <User Role>, At least one filter is active | 1. Click the 'Reset all filters' control<br>2. Observe the results grid | All filters are cleared; results update to show all available listings; result count updates accordingly | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to apply filters without any selections |  | 1. Leave all filter options unselected<br>2. Click Apply Filters | No filters are applied; the results grid remains unchanged |  |
| TC-010 |  | Attempt to reset filters when none are applied |  | 1. Ensure no filters are currently applied<br>2. Click Reset all filters | No changes occur; the results grid remains unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long string in the search field |  | 1. Enter a string longer than 200 characters in the search field | The input is either accepted or truncated with a visible indicator | low |
| TC-012 (input_edge) |  | Enter special characters in the search field |  | 1. Enter special characters (e.g., @#$%^&*) in the search field | The input is accepted or a specific error message is shown | low |
| TC-013 (input_edge) |  | Enter a value with leading and trailing whitespace |  | 1. Enter '   sample text   ' in the search field | Leading/trailing whitespace is trimmed; saved value shown in the results has no extra spaces | low |

---

## Reviews & Ratings

Total: **5** (positive: 0, negative: 2, edge: 3)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Unauthenticated user attempts to submit a review |  | 1. Navigate to the review submission page<br>2. Attempt to submit a review without logging in | User is redirected to the login page | high |
| TC-002 |  | User attempts to submit a review without completing a booking | User is authenticated but has not completed a booking | 1. Navigate to the review submission page<br>2. Attempt to submit a review | User receives an error message indicating that a booking is required to submit a review | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (input_edge) |  | Submit a very long review comment | User is authenticated and has completed a booking | 1. Navigate to the review submission page<br>2. Enter a review comment with 200+ characters | Review submission is accepted or truncated with a visible indicator | low |
| TC-004 (input_edge) |  | Submit a review with special characters | User is authenticated and has completed a booking | 1. Navigate to the review submission page<br>2. Enter a review comment with special characters (e.g., !@#$%^&*()) | Review submission is accepted or a specific error is shown | low |
| TC-005 (input_edge) |  | Submit a review with leading/trailing whitespace | User is authenticated and has completed a booking | 1. Navigate to the review submission page<br>2. Enter a review comment with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Offers & Deals

Total: **9** (positive: 4, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book Now with standard promotion | User logged in as <Role> | 1. Click on a standard promotion deal<br>2. Click 'Book Now' button | Redirected to booking flow with promotional code applied | high |
| TC-002 | WF-002 | Book Now with last-minute offer | User logged in as <Role> | 1. Click on a last-minute offer deal<br>2. Click 'Book Now' button | Redirected to booking flow with promotional code applied | high |
| TC-003 | WF-003 | Book Now with seasonal package | User logged in as <Role> | 1. Click on a seasonal package deal<br>2. Click 'Book Now' button | Redirected to booking flow with promotional code applied | high |
| TC-004 | WF-004 | Subscribe to newsletter | User logged in as <Role> | 1. Enter <valid email> in the newsletter subscription field<br>2. Click 'Submit' button | Email submitted for future exclusive deals | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to subscribe to newsletter without providing an email |  | 1. Leave the email subscription field blank<br>2. Click Submit | Inline validation error appears on the email subscription field indicating it is required | high |
| TC-006 |  | Attempt to book now without selecting any offer |  | 1. Click Book Now without selecting any promotional offer | No action occurs; user remains on the Offers page without redirection | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-004 | Submit newsletter subscription with long email address |  | 1. Enter a long email address (200+ characters) in the newsletter subscription field<br>2. Click Submit | Email submission is blocked; an error message indicates the email address is too long | low |
| TC-008 (input_edge) | WF-004 | Submit newsletter subscription with special characters |  | 1. Enter an email address with special characters (e.g., 'test!@example.com') in the newsletter subscription field<br>2. Click Submit | Email submission is blocked; an error message indicates invalid email format | low |
| TC-009 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User is on the Offers page | 1. Click Book Now on a standard promotion<br>2. After being redirected to the booking flow, press the browser back button | User is redirected to the Offers page without pre-filled values; the form is blank | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <role> | 1. Click Logout | Session terminated; redirected to home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to access a protected page after logout |  | 1. Logout the user<br>2. Attempt to access a protected page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click Logout<br>2. Immediately click Logout again before the redirect completes | Second logout attempt is ignored; user remains on the home page without error | medium |
| TC-004 (input_edge) |  | Access protected page after logout | User is logged in, User clicks Logout | 1. Click Logout<br>2. Attempt to access a protected page | User is redirected to the login page with no access to the protected content | medium |

---
