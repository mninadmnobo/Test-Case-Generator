# Test Cases — Phptravels

Generated: 2026-06-09T11:03:43.027481Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 302 | 59 | 133 | 110 | 154 | 101 | 34 |

## Home Page & Search

Total: **20** (positive: 4, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Hotels with valid inputs | User logged in as <Role> | 1. Click on the Hotels tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check In Date field<br>4. Enter <valid check-out date> in the Check Out Date field<br>5. Enter <valid number> in the Number of Rooms field<br>6. Enter <valid number> in the Adults field<br>7. Click the Search button | redirects to corresponding results listing page | high |
| TC-002 | WF-002 | Search for Flights with valid inputs | User logged in as <Role> | 1. Click on the Flights tab<br>2. Select 'Round-trip' from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Enter <valid departure date> in the Departure Date field<br>6. Enter <valid return date> in the Return Date field<br>7. Enter <valid number> in the Adults field<br>8. Select 'Economy' from the Cabin Class dropdown<br>9. Click the Search button | redirects to corresponding results listing page | high |
| TC-003 | WF-003 | Search for Tours with valid inputs | User logged in as <Role> | 1. Click on the Tours tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid start date> in the Start Date field<br>4. Enter <valid end date> in the End Date field<br>5. Click the Search button | redirects to corresponding results listing page | high |
| TC-004 | WF-004 | Search for Cars with valid inputs | User logged in as <Role> | 1. Click on the Cars tab<br>2. Enter <valid pick-up location> in the Pick Up Location field<br>3. Enter <valid drop-off location> in the Drop Off Location field<br>4. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>6. Click the Search button | redirects to corresponding results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Destination field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill in the Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count fields<br>4. Click the Search button | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 | WF-001 | Leave all required fields empty and submit |  | 1. Click on the Hotels tab<br>2. Leave all required fields blank<br>3. Click the Search button | Inline validation errors appear on the Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields indicating they are required | high |
| TC-007 | WF-002 | Leave the Departure City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure City field blank<br>3. Fill in the Arrival_City, Trip_Type, Departure_Date, and Adults fields<br>4. Click the Search button | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-008 | WF-002 | Leave all required fields empty and submit |  | 1. Click on the Flights tab<br>2. Leave all required fields blank<br>3. Click the Search button | Inline validation errors appear on the Departure City, Arrival City, Trip Type, Departure Date, and Adults fields indicating they are required | high |
| TC-009 | WF-003 | Leave the Destination field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Destination field blank<br>3. Fill in the Start_Date and End_Date fields<br>4. Click the Search button | Inline validation error appears on the Destination field indicating it is required | high |
| TC-010 | WF-003 | Leave all required fields empty and submit |  | 1. Click on the Tours tab<br>2. Leave all required fields blank<br>3. Click the Search button | Inline validation errors appear on the Destination, Start_Date, and End_Date fields indicating they are required | high |
| TC-011 | WF-004 | Leave the Pick Up Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick Up Location field blank<br>3. Fill in the Drop Off Location, Pick Up Date Time, and Drop Off Date Time fields<br>4. Click the Search button | Inline validation error appears on the Pick Up Location field indicating it is required | high |
| TC-012 | WF-004 | Leave all required fields empty and submit |  | 1. Click on the Cars tab<br>2. Leave all required fields blank<br>3. Click the Search button | Inline validation errors appear on the Pick Up Location, Drop Off Location, Pick Up Date Time, and Drop Off Date Time fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Check-In and Check-Out Dates are the same day |  | 1. Select the Hotels tab<br>2. Enter a valid destination in the Destination field<br>3. Enter today's date in the Check_In_Date field<br>4. Enter today's date in the Check_Out_Date field<br>5. Enter a valid number in the Number_of_Rooms field<br>6. Enter a valid number of adults in the Adults field | Search button is enabled and can be clicked; user can proceed to search results | medium |
| TC-014 (boundary) | WF-001 | Check-Out Date is one day before Check-In Date |  | 1. Select the Hotels tab<br>2. Enter a valid destination in the Destination field<br>3. Enter tomorrow's date in the Check_In_Date field<br>4. Enter today's date in the Check_Out_Date field<br>5. Enter a valid number in the Number_of_Rooms field<br>6. Enter a valid number of adults in the Adults field | Inline error appears indicating Check-Out Date must be after Check-In Date | medium |
| TC-015 (boundary) | WF-002 | Departure Date and Return Date are the same day |  | 1. Select the Flights tab<br>2. Enter a valid departure city in the Departure_City field<br>3. Enter a valid arrival city in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter today's date in the Return_Date field<br>6. Select a valid trip type in the Trip_Type field<br>7. Enter a valid number of adults in the Adults field | Search button is enabled and can be clicked; user can proceed to search results | medium |
| TC-016 (boundary) | WF-002 | Return Date is one day before Departure Date |  | 1. Select the Flights tab<br>2. Enter a valid departure city in the Departure_City field<br>3. Enter a valid arrival city in the Arrival_City field<br>4. Enter tomorrow's date in the Departure_Date field<br>5. Enter today's date in the Return_Date field<br>6. Select a valid trip type in the Trip_Type field<br>7. Enter a valid number of adults in the Adults field | Inline error appears indicating Return Date must be after Departure Date | medium |
| TC-017 (boundary) | WF-003 | Start Date and End Date are the same day |  | 1. Select the Tours tab<br>2. Enter a valid destination in the Destination field<br>3. Enter today's date in the Start_Date field<br>4. Enter today's date in the End_Date field | Search button is enabled and can be clicked; user can proceed to search results | medium |
| TC-018 (boundary) | WF-003 | End Date is one day before Start Date |  | 1. Select the Tours tab<br>2. Enter a valid destination in the Destination field<br>3. Enter tomorrow's date in the Start_Date field<br>4. Enter today's date in the End_Date field | Inline error appears indicating End Date must be after Start Date | medium |
| TC-019 (boundary) | WF-004 | Pick-Up and Drop-Off Date/Time are the same |  | 1. Select the Cars tab<br>2. Enter a valid pick-up location in the Pick_Up_Location field<br>3. Enter a valid drop-off location in the Drop_Off_Location field<br>4. Enter a valid date and time in the Pick_Up_Date_Time field<br>5. Enter the same date and time in the Drop_Off_Date_Time field | Search button is enabled and can be clicked; user can proceed to search results | medium |
| TC-020 (boundary) | WF-004 | Drop-Off Date/Time is one minute before Pick-Up Date/Time |  | 1. Select the Cars tab<br>2. Enter a valid pick-up location in the Pick_Up_Location field<br>3. Enter a valid drop-off location in the Drop_Off_Location field<br>4. Enter a valid date and time in the Pick_Up_Date_Time field<br>5. Enter the same date and one minute earlier in the Drop_Off_Date_Time field | Inline error appears indicating Drop-Off Date/Time must be after Pick-Up Date/Time | medium |

---

## User Registration

Total: **17** (positive: 2, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration without mobile number | User logged in as <Role> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Password> in the Password field<br>5. Enter <Password> in the Confirm Password field<br>6. Check the Terms and Conditions checkbox<br>7. Click Submit | Account is created and user is redirected to their dashboard | high |
| TC-002 | WF-002 | Successful registration with mobile number | User logged in as <Role> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Password> in the Password field<br>5. Enter <Password> in the Confirm Password field<br>6. Enter <Mobile Number> in the Mobile Number field<br>7. Select <Country Code> from the Country Code dropdown<br>8. Check the Terms and Conditions checkbox<br>9. Click Submit | Account is created and user is redirected to their dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave First Name blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-004 |  | Leave Last Name blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-005 |  | Leave Email blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-006 |  | Leave Password blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Leave Confirm Password blank and submit |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-008 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Confirm Password field indicating it must match Password | high |
| TC-009 |  | Enter invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email format | high |
| TC-010 |  | Enter duplicate email and submit |  | 1. Enter <duplicate email> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be unique | high |
| TC-011 |  | Leave Terms and Conditions unchecked and submit |  | 1. Leave the Terms and Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Terms and Conditions field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Email format boundary test | All required fields are filled, Password and Confirm Password match | 1. Enter a valid email format in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created with the valid email | medium |
| TC-013 (boundary) | WF-001 | Email uniqueness boundary test | An account with the same email already exists | 1. Enter the existing email in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Field-level error appears inline indicating email must be unique | medium |
| TC-014 (boundary) | WF-001 | Password confirmation match boundary test | All required fields are filled | 1. Enter a password in the Password field<br>2. Enter a different password in the Confirm Password field<br>3. Click Submit | Field-level error appears inline indicating passwords must match | medium |
| TC-015 (input_edge) | WF-001 | Long text in First Name field |  | 1. Enter a very long string (200+ characters) in the First Name field<br>2. Fill all other required fields<br>3. Click Submit | Field-level error appears inline indicating the input is too long or is truncated | low |
| TC-016 (input_edge) | WF-001 | Special characters in Last Name field |  | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Submit | Field-level error appears inline indicating invalid characters in the Last Name field | low |
| TC-017 (interaction_edge) | WF-002 | Rapid re-submission after successful registration | User has successfully registered | 1. Click Submit again after successful registration<br>2. Observe the behavior | User is redirected to their dashboard without creating a second account | low |

---

## User Login

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <Role> | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | redirects to dashboard or previous page | high |
| TC-002 | WF-002 | Login with invalid credentials | User logged in as <Role> | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | shows error message | high |
| TC-003 | WF-003 | Login after multiple failed attempts requiring CAPTCHA | User logged in as <Role>, multiple consecutive failed attempts occur | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button<br>4. Repeat steps 1-3 for multiple attempts<br>5. Enter <valid email> in the Email field<br>6. Enter <valid password> in the Password field<br>7. Click the Login button | redirects to dashboard or previous page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Fill the Email field with <valid email><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill the Password field with <valid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Fill the Email field with <valid email><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | medium |
| TC-008 | WF-003 | Attempt login after multiple failed attempts without CAPTCHA verification | multiple consecutive failed attempts occur | 1. Fill the Email field with <valid email><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Enter an invalid email format |  | 1. Enter 'invalid-email' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message is shown indicating invalid email format; password field is cleared | medium |
| TC-010 (boundary) | WF-002 | Enter an empty password |  | 1. Enter a valid email in the Email field<br>2. Leave the Password field empty<br>3. Click Login | Error message is shown indicating password is required; password field remains empty | medium |
| TC-011 (interaction_edge) | WF-003 | Login after multiple failed attempts requiring CAPTCHA | 3 consecutive failed login attempts | 1. Enter valid email in the Email field<br>2. Enter valid password in the Password field<br>3. Click Login | CAPTCHA verification is displayed before proceeding with login | medium |
| TC-012 (input_edge) |  | Enter a long email address |  | 1. Enter a string of 200+ characters in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message is shown indicating email exceeds maximum length or is truncated; password field remains filled | low |
| TC-013 (input_edge) |  | Enter special characters in the password field |  | 1. Enter a valid email in the Email field<br>2. Enter a password with special characters in the Password field<br>3. Click Login | Login succeeds or fails based on password validity; password field remains filled | low |

---

## Forgot Password

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset Password with existing email | User logged in as <User>, Email <valid email> exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is shown indicating that the reset link has been sent to email | high |
| TC-002 | WF-002 | Change Password after clicking reset link | User clicked the reset link from their email | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | Redirects to login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it must be a valid email address | medium |
| TC-005 |  | Submit with a non-existing email |  | 1. Enter <non-existing email> in the Email field<br>2. Click Reset Password | Error is shown indicating the email is not found; form remains editable | high |
| TC-006 |  | Leave the New Password field blank on the password reset page |  | 1. Leave the New Password field blank<br>2. Enter <valid password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-007 |  | Leave the Confirm Password field blank on the password reset page |  | 1. Enter <valid password> in the New Password field<br>2. Leave the Confirm Password field blank<br>3. Click Change Password | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-008 |  | Submit with mismatched passwords |  | 1. Enter <valid password> in the New Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears on the Confirm Password field indicating it must match New Password | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit with valid email format | Email exists in the system | 1. Enter a valid email address in the Email field<br>2. Click Reset Password | Reset link is sent to the email address; confirmation message is shown. | medium |
| TC-010 (boundary) | WF-001 | Submit with email not in the system | Email does not exist in the system | 1. Enter a non-registered email address in the Email field<br>2. Click Reset Password | An error is shown indicating the email is not found; form remains editable. | medium |
| TC-011 (input_edge) |  | Enter long email address |  | 1. Enter a very long email address (over 254 characters) in the Email field<br>2. Click Reset Password | An error is shown indicating the email format is invalid. | low |
| TC-012 (input_edge) |  | Enter email with special characters |  | 1. Enter an email address with special characters (e.g., 'user!#$%&'*+/=?^_`{|}~@example.com') in the Email field<br>2. Click Reset Password | Reset link is sent to the email address; confirmation message is shown. | low |
| TC-013 (boundary) | WF-002 | Submit with matching passwords |  | 1. Enter a new password in the New Password field<br>2. Enter the same password in the Confirm Password field<br>3. Click Change Password | Redirects to login page with a success message. | medium |
| TC-014 (boundary) | WF-002 | Submit with non-matching passwords |  | 1. Enter a new password in the New Password field<br>2. Enter a different password in the Confirm Password field<br>3. Click Change Password | An error is shown indicating the passwords do not match; form remains editable. | medium |

---

## Hotels Search & Listing

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for hotels with valid inputs | User logged in as <User> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <valid number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' in the Guest Count section<br>6. Enter <valid number of adults> in the Adults field<br>7. Enter <valid number of children> in the Children field<br>8. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | Book a hotel from the listing page | User logged in as <User>, User is on the listing page | 1. Click Book Now on the first hotel card | Booking confirmed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 | WF-001 | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-005 | WF-001 | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-006 | WF-001 | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-007 | WF-001 | Leave the Adults field blank in Guest Count and submit |  | 1. Leave the Adults field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and valid values for Children<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-008 | WF-001 | Submit with all required fields empty |  | 1. Leave all required fields (Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults) blank<br>2. Click Search | Inline validation errors appear on the Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Check-In Date is the same as Check-Out Date |  | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search succeeds and redirects to the listing page | medium |
| TC-010 (boundary) | WF-001 | Check-Out Date is one day before Check-In Date |  | 1. Enter a valid destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error message displayed indicating Check-Out Date must be after Check-In Date | medium |
| TC-011 (boundary) | WF-001 | Add maximum number of adults in Guest Count |  | 1. Enter a valid destination in the Destination field<br>2. Enter a valid Check_In_Date in the Check_In_Date field<br>3. Enter a valid Check_Out_Date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add the maximum allowed number of adults in the Guest_Count repeating group<br>6. Click Search | Search succeeds and redirects to the listing page with the specified number of adults | medium |
| TC-012 (boundary) | WF-001 | Add one more adult than the maximum allowed in Guest Count |  | 1. Enter a valid destination in the Destination field<br>2. Enter a valid Check_In_Date in the Check_In_Date field<br>3. Enter a valid Check_Out_Date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add one more adult than the maximum allowed in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error message displayed indicating the maximum number of adults exceeded | medium |
| TC-013 (input_edge) |  | Enter a very long destination name |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Enter a valid Check_In_Date in the Check_In_Date field<br>3. Enter a valid Check_Out_Date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error message displayed indicating the destination name is too long | low |
| TC-014 (input_edge) |  | Enter special characters in the destination field |  | 1. Enter special characters in the Destination field<br>2. Enter a valid Check_In_Date in the Check_In_Date field<br>3. Enter a valid Check_Out_Date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error message displayed indicating invalid characters in the destination field | low |

---

## Hotel Details & Booking

Total: **12** (positive: 1, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking proceeds to payment page | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Enter <stay dates> in the Stay Dates field<br>6. Enter <valid guest count> in the Guest Count field<br>7. Click Book Now | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-006 |  | Leave the Stay Dates field blank and submit |  | 1. Leave the Stay_Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay_Dates field indicating it is required | high |
| TC-007 |  | Leave the Guest Count field blank and submit |  | 1. Leave the Guest_Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest_Count field indicating it is required | high |
| TC-008 |  | Attempt to book without logging in |  | 1. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter exactly 1 in the Guest Count field | User is logged in | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter 'john.doe@example.com' in the Email field<br>4. Enter '1234567890' in the Phone Number field<br>5. Enter '2023-10-01 to 2023-10-05' in the Stay Dates field<br>6. Enter '1' in the Guest Count field<br>7. Click Book Now | Proceeds to payment page | medium |
| TC-010 (boundary) | WF-001 | Enter 0 in the Guest Count field | User is logged in | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter 'john.doe@example.com' in the Email field<br>4. Enter '1234567890' in the Phone Number field<br>5. Enter '2023-10-01 to 2023-10-05' in the Stay Dates field<br>6. Enter '0' in the Guest Count field<br>7. Click Book Now | Form submission is blocked; an error message is displayed indicating that the guest count must be greater than 0 | medium |
| TC-011 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Form submission is blocked; an error message is displayed indicating the maximum length for the First Name field | low |
| TC-012 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter '@#$%' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Form submission is blocked; an error message is displayed indicating invalid characters in the Last Name field | low |

---

## Flights Search & Listing

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search Flights with required fields | User logged in as <Role> | 1. Enter <Departure City> in the Departure City field<br>2. Enter <Arrival City> in the Arrival City field<br>3. Enter <valid travel date> in the Travel Dates field<br>4. Click 'Add Row' in the Passenger Count section<br>5. Enter <number of adults> in the Adults field<br>6. Click 'Search Flights' | User is redirected to the listing page | high |
| TC-002 | WF-002 | Select a flight from the listing | User logged in as <Role>, User is on the listing page | 1. Click 'Select' on a flight result | Flight selected for booking | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Departure City field blank and submit |  | 1. Leave the Departure City field blank<br>2. Fill in Arrival City with a valid city<br>3. Fill in Travel Dates with valid dates<br>4. Fill in Passenger Count with valid numbers<br>5. Click Search Flights | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-004 | WF-001 | Leave the Arrival City field blank and submit |  | 1. Fill in Departure City with a valid city<br>2. Leave the Arrival City field blank<br>3. Fill in Travel Dates with valid dates<br>4. Fill in Passenger Count with valid numbers<br>5. Click Search Flights | Inline validation error appears on the Arrival City field indicating it is required | high |
| TC-005 | WF-001 | Leave the Travel Dates field blank and submit |  | 1. Fill in Departure City with a valid city<br>2. Fill in Arrival City with a valid city<br>3. Leave the Travel Dates field blank<br>4. Fill in Passenger Count with valid numbers<br>5. Click Search Flights | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-006 | WF-001 | Leave the Adults field blank in Passenger Count and submit |  | 1. Fill in Departure City with a valid city<br>2. Fill in Arrival City with a valid city<br>3. Fill in Travel Dates with valid dates<br>4. Leave the Adults field blank in Passenger Count<br>5. Click Search Flights | Inline validation error appears on the Adults field indicating it is required | high |
| TC-007 | WF-001 | Submit the search form with all required fields empty |  | 1. Leave the Departure City field blank<br>2. Leave the Arrival City field blank<br>3. Leave the Travel Dates field blank<br>4. Leave the Adults field blank in Passenger Count<br>5. Click Search Flights | Form does not submit; multiple inline validation errors appear indicating required fields | high |
| TC-008 |  | Attempt to select a flight without any selection made |  | 1. Navigate to the Flights Listing page<br>2. Click Select on a flight without making a selection | No flight is selected; an error message appears indicating a selection is required | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Passenger count exactly at minimum (1 adult) |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Enter a valid date in the Travel_Dates field<br>5. Add 1 Adult in the Passenger_Count repeating group<br>6. Click Search Flights | Redirects to the listing page with search results displayed | medium |
| TC-010 (boundary) | WF-001 | Passenger count exceeds maximum (more than 9 adults) |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Enter a valid date in the Travel_Dates field<br>5. Add 10 Adults in the Passenger_Count repeating group<br>6. Click Search Flights | Submission is blocked; error shown indicating maximum passenger count exceeded | medium |
| TC-011 (data_edge) | WF-001 | Travel date set to today |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Set the Travel_Dates field to today's date<br>5. Add 1 Adult in the Passenger_Count repeating group<br>6. Click Search Flights | Redirects to the listing page with search results displayed for today's flights | medium |
| TC-012 (data_edge) | WF-001 | Travel date set to a far future date |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Set the Travel_Dates field to a date 1 year in the future<br>5. Add 1 Adult in the Passenger_Count repeating group<br>6. Click Search Flights | Redirects to the listing page with search results displayed for future flights | medium |
| TC-013 (input_edge) |  | Leading/trailing whitespace in Departure_City |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter '  New York ' in the Departure_City field<br>3. Enter a valid Arrival_City<br>4. Enter a valid date in the Travel_Dates field<br>5. Add 1 Adult in the Passenger_Count repeating group<br>6. Click Search Flights | Leading/trailing whitespace is trimmed; redirects to the listing page with search results displayed | low |
| TC-014 (input_edge) |  | Special characters in Arrival_City |  | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter 'Los Angeles@2023' in the Arrival_City field<br>3. Enter a valid Departure_City<br>4. Enter a valid date in the Travel_Dates field<br>5. Add 1 Adult in the Passenger_Count repeating group<br>6. Click Search Flights | Submission is blocked; error shown indicating invalid characters in Arrival_City | low |

---

## Flight Booking

Total: **15** (positive: 1, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit booking form with all required fields completed | User logged in as <Role> | 1. Click 'Add Row' to add a traveler<br>2. Select 'Mr' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid passport expiry date> in the Passport Expiry field<br>8. Enter <valid email> in the Lead Passenger Email field<br>9. Enter <valid phone number> in the Lead Passenger Phone field<br>10. Click Continue | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Date of Birth field blank |  | 1. Leave the Date_of_Birth field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Date_of_Birth field indicating it is required | high |
| TC-005 |  | Leave the Passport Number field blank |  | 1. Leave the Passport_Number field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Passport_Number field indicating it is required | high |
| TC-006 |  | Leave the Passport Expiry field blank |  | 1. Leave the Passport_Expiry field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Passport_Expiry field indicating it is required | high |
| TC-007 |  | Leave the Lead Passenger Email field blank |  | 1. Leave the Lead_Passenger_Email field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Email field indicating it is required | high |
| TC-008 |  | Leave the Lead Passenger Phone field blank |  | 1. Leave the Lead_Passenger_Phone field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Phone field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Continue | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | All required fields completed with valid data |  | 1. Add one traveler to the Travelers group<br>2. Select 'Mr' from the Title dropdown<br>3. Enter a valid First Name in the First_Name field<br>4. Enter a valid Last Name in the Last_Name field<br>5. Enter a valid Date of Birth in the Date_of_Birth field<br>6. Enter a valid Passport Number in the Passport_Number field<br>7. Enter a valid Passport Expiry date in the Passport_Expiry field<br>8. Enter a valid email in the Lead_Passenger_Email field<br>9. Enter a valid phone number in the Lead_Passenger_Phone field<br>10. Click Continue | Form submits successfully; proceeds to the payment page | medium |
| TC-011 (boundary) | WF-001 | Add maximum number of travelers to the Travelers group |  | 1. Add maximum allowed number of travelers to the Travelers group<br>2. Fill all required fields for each traveler<br>3. Enter a valid email in the Lead_Passenger_Email field<br>4. Enter a valid phone number in the Lead_Passenger_Phone field<br>5. Click Continue | Form submits successfully; proceeds to the payment page | medium |
| TC-012 (boundary) | WF-001 | Attempt to add one more traveler than allowed |  | 1. Add maximum allowed number of travelers to the Travelers group<br>2. Attempt to add one more traveler<br>3. Click Continue | Submission is blocked; inline error displayed indicating maximum number of travelers exceeded | medium |
| TC-013 (input_edge) | WF-001 | Enter a long string in the First_Name field |  | 1. Add one traveler to the Travelers group<br>2. Enter a long string (200+ characters) in the First_Name field<br>3. Fill all other required fields with valid data<br>4. Click Continue | Inline error displayed indicating the First_Name field exceeds maximum length | low |
| TC-014 (input_edge) | WF-001 | Enter special characters in the Last_Name field |  | 1. Add one traveler to the Travelers group<br>2. Enter special characters in the Last_Name field<br>3. Fill all other required fields with valid data<br>4. Click Continue | Inline error displayed indicating invalid characters in the Last_Name field | low |
| TC-015 (input_edge) | WF-001 | Enter leading/trailing whitespace in the Lead_Passenger_Email field |  | 1. Add one traveler to the Travelers group<br>2. Enter leading/trailing whitespace in the Lead_Passenger_Email field<br>3. Fill all other required fields with valid data<br>4. Click Continue | Inline error displayed indicating email format is invalid | low |

---

## Tours Search & Listing

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for tours with valid inputs | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select 'Adventure' from the Tour Type dropdown<br>4. Click Search | User is redirected to the listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the Destination field blank |  | 1. Leave the Destination field blank<br>2. Fill in the Travel Dates field with a valid date<br>3. Select a Tour Type<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-003 | WF-001 | Leave the Travel Dates field blank |  | 1. Fill in the Destination field with a valid destination<br>2. Leave the Travel Dates field blank<br>3. Select a Tour Type<br>4. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-004 | WF-001 | Leave the Tour Type field unselected |  | 1. Fill in the Destination field with a valid destination<br>2. Fill in the Travel Dates field with a valid date<br>3. Leave the Tour Type field unselected<br>4. Click Search | Inline validation error appears on the Tour Type field indicating it is required | high |
| TC-005 | WF-001 | Leave all required fields empty |  | 1. Leave the Destination field blank<br>2. Leave the Travel Dates field blank<br>3. Leave the Tour Type field unselected<br>4. Click Search | Form does not submit; errors shown on Destination, Travel Dates, and Tour Type fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Enter a valid destination and travel dates, select a tour type |  | 1. Enter a valid destination in the Destination field<br>2. Enter valid travel dates in the Travel Dates field<br>3. Select a tour type from the Tour Type dropdown<br>4. Click Search | Redirects to the listing page displaying available tours | medium |
| TC-007 (boundary) | WF-001 | Enter an empty destination field |  | 1. Leave the Destination field empty<br>2. Enter valid travel dates in the Travel Dates field<br>3. Select a tour type from the Tour Type dropdown<br>4. Click Search | Search is blocked; an error message indicates that the Destination field is required | medium |
| TC-008 (input_edge) | WF-001 | Enter a long string in the Destination field |  | 1. Enter a long string (200+ characters) in the Destination field<br>2. Enter valid travel dates in the Travel Dates field<br>3. Select a tour type from the Tour Type dropdown<br>4. Click Search | Search is blocked; an error message indicates that the input exceeds the maximum allowed length | low |
| TC-009 (input_edge) | WF-001 | Enter special characters in the Destination field |  | 1. Enter special characters (e.g., @#$%^&) in the Destination field<br>2. Enter valid travel dates in the Travel Dates field<br>3. Select a tour type from the Tour Type dropdown<br>4. Click Search | Search is blocked; an error message indicates invalid characters in the Destination field | low |

---

## Tour Details & Booking

Total: **10** (positive: 1, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking of a tour with traveler details | User logged in as <authenticated user>, User is on the Tour Details page | 1. Select a valid <departure date> from the available dates<br>2. Click 'Add Row' to specify the number of travelers<br>3. Enter <number of adults> in the Adults field<br>4. Optionally, enter <number of children> in the Children field<br>5. Click 'Add Row' to enter traveler details<br>6. Enter <traveler name> in the Name field<br>7. Enter <contact details> in the Contact Details field<br>8. Optionally, enter <special requirements> in the Special Requirements field<br>9. Click 'Book Now' | redirects to booking confirmation | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Departure Date blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Fill in all other required fields<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-003 |  | Leave the Name field blank for a traveler and submit |  | 1. Fill in all required fields except for the Name field in Traveler_Details<br>2. Click Book Now | Inline validation error appears on the Name field indicating it is required | high |
| TC-004 |  | Leave the Contact Details field blank for a traveler and submit |  | 1. Fill in all required fields except for the Contact_Details field in Traveler_Details<br>2. Click Book Now | Inline validation error appears on the Contact_Details field indicating it is required | high |
| TC-005 |  | Attempt to book without authentication |  | 1. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Select today's date as the departure date | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the Number_of_Travelers with at least one adult<br>3. Fill in all required Traveler_Details fields<br>4. Click Book Now | Redirects to booking confirmation | medium |
| TC-007 (boundary) | WF-001 | Select a departure date that is in the past | User is authenticated | 1. Select a date that is yesterday in the Departure_Date field<br>2. Fill in the Number_of_Travelers with at least one adult<br>3. Fill in all required Traveler_Details fields<br>4. Click Book Now | Form submission is blocked; an error message displays indicating the date must be today or in the future. | medium |
| TC-008 (input_edge) |  | Enter a very long name in the Traveler_Details | User is authenticated | 1. Fill in the Name field with a string longer than 200 characters<br>2. Fill in the Contact_Details field<br>3. Click Book Now | Form submission is blocked; an error message displays indicating the name exceeds the maximum length. | low |
| TC-009 (input_edge) |  | Enter special characters in the Contact_Details field | User is authenticated | 1. Fill in the Name field with a valid name<br>2. Fill in the Contact_Details field with special characters (e.g., !@#$%^&*)<br>3. Click Book Now | Form submission is blocked; an error message displays indicating invalid characters in the Contact_Details. | low |
| TC-010 (interaction_edge) | WF-001 | Rapid re-submission after successful booking | User is authenticated | 1. Complete the booking form and click Book Now<br>2. After redirection to booking confirmation, click the back button<br>3. Click Book Now again | The booking form is shown blank without pre-filled data. | low |

---

## Cars Search & Listing

Total: **15** (positive: 2, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for cars with valid inputs | User logged in as <Role> | 1. Enter <valid pick-up location> in the Pick Up Location field<br>2. Enter <valid drop-off location> in the Drop Off Location field<br>3. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>4. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>5. Enter <valid driver age> in the Driver Age field<br>6. Click Search | User is redirected to listing page | high |
| TC-002 | WF-002 | Book a vehicle from the listing | User logged in as <Role>, User is on the listing page with available vehicles | 1. Click Book Now on a vehicle listing | Booking confirmed; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Pick Up Location blank and submit |  | 1. Leave the Pick_Up_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-004 |  | Leave the Drop Off Location blank and submit |  | 1. Leave the Drop_Off_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-005 |  | Leave the Pick Up Date Time blank and submit |  | 1. Leave the Pick_Up_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-006 |  | Leave the Drop Off Date Time blank and submit |  | 1. Leave the Drop_Off_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |
| TC-007 |  | Leave the Driver Age blank and submit |  | 1. Leave the Driver_Age field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Driver_Age field indicating it is required | high |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Form does not submit; error shown on Pick_Up_Location, Drop_Off_Location, Pick_Up_Date_Time, Drop_Off_Date_Time, and Driver_Age fields | high |
| TC-009 |  | Enter an invalid date in the Pick Up Date Time field |  | 1. Enter <invalid date format> in the Pick_Up_Date_Time field<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating an invalid date format | medium |
| TC-010 |  | Enter an invalid date in the Drop Off Date Time field |  | 1. Enter <invalid date format> in the Drop_Off_Date_Time field<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating an invalid date format | medium |
| TC-011 |  | Enter a non-numeric value in the Driver Age field |  | 1. Enter <non-numeric value> in the Driver_Age field<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Driver_Age field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Pick-Up Date and Drop-Off Date are the same |  | 1. Enter 'Location A' in the Pick Up Location field<br>2. Enter 'Location B' in the Drop Off Location field<br>3. Enter today's date in the Pick Up Date Time field<br>4. Enter today's date in the Drop Off Date Time field<br>5. Enter '25' in the Driver Age field<br>6. Click Search | Redirects to listing page; search results displayed for the same day rental | medium |
| TC-013 (boundary) | WF-001 | Pick-Up Date is before Drop-Off Date |  | 1. Enter 'Location A' in the Pick Up Location field<br>2. Enter 'Location B' in the Drop Off Location field<br>3. Enter tomorrow's date in the Pick Up Date Time field<br>4. Enter today's date in the Drop Off Date Time field<br>5. Enter '25' in the Driver Age field<br>6. Click Search | Search is blocked; error message displayed indicating that the Drop Off Date must be after the Pick Up Date | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Pick Up Location field |  | 1. Enter a string of 200 characters in the Pick Up Location field<br>2. Enter 'Location B' in the Drop Off Location field<br>3. Enter today's date in the Pick Up Date Time field<br>4. Enter tomorrow's date in the Drop Off Date Time field<br>5. Enter '25' in the Driver Age field<br>6. Click Search | Form submits successfully; the long string is accepted and displayed in the search results | low |
| TC-015 (input_edge) |  | Enter leading and trailing spaces in the Drop Off Location field |  | 1. Enter '   Location A   ' in the Pick Up Location field<br>2. Enter '   Location B   ' in the Drop Off Location field<br>3. Enter today's date in the Pick Up Date Time field<br>4. Enter tomorrow's date in the Drop Off Date Time field<br>5. Enter '25' in the Driver Age field<br>6. Click Search | Leading/trailing whitespace is trimmed; saved value shown in search results has no extra spaces | low |

---

## Car Booking

Total: **16** (positive: 1, negative: 10, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm Booking with valid fields | User logged in as <Role> | 1. Enter <Driver Full Name> in the Driver Full Name field<br>2. Enter '25' in the Age field<br>3. Enter <License Number> in the License Number field<br>4. Enter <License Issue Country> in the License Issue Country field<br>5. Enter <valid email> in the Email field<br>6. Enter <Phone Number> in the Phone Number field<br>7. Click 'Add Row' to add optional add-ons<br>8. Check the GPS checkbox<br>9. Select 'Standard' from the Insurance Plan dropdown<br>10. Check the Terms Acceptance checkbox<br>11. Click Confirm Booking | Page shows 'proceeds to payment' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Driver Full Name field blank |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 |  | Leave the Age field blank |  | 1. Leave the Age field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-004 |  | Enter age below 18 |  | 1. Enter <age below 18> in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating 'must be 18 or older' | high |
| TC-005 |  | Leave the License Number field blank |  | 1. Leave the License Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-006 |  | Leave the License Issue Country field blank |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-007 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-008 |  | Enter invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is not a valid email address | high |
| TC-009 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-010 |  | Leave the Insurance Plan field unselected |  | 1. Leave the Insurance Plan field unselected<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating it is required | high |
| TC-011 |  | Leave the Terms Acceptance checkbox unchecked |  | 1. Leave the Terms Acceptance checkbox unchecked<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Terms Acceptance field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Test age exactly at minimum requirement |  | 1. Enter '18' in the Age field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully; user proceeds to payment | medium |
| TC-013 (boundary) | WF-001 | Test age one year below minimum requirement |  | 1. Enter '17' in the Age field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Age field displays an error indicating the user must be 18 or older | medium |
| TC-014 (input_edge) |  | Enter long text in Driver Full Name field |  | 1. Enter a string of 200+ characters in the Driver Full Name field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submission is blocked; inline error shown for Driver Full Name field | low |
| TC-015 (input_edge) |  | Enter special characters in License Number field |  | 1. Enter special characters in the License Number field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | License Number field displays an error indicating invalid input | low |
| TC-016 (interaction_edge) |  | Rapid re-submission after successful booking | User has successfully submitted the booking form | 1. Click Confirm Booking<br>2. Press the browser back button<br>3. Click Confirm Booking again | User is redirected to the payment page without a second booking being created | low |

---

## Visa Services

Total: **23** (positive: 3, negative: 14, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Visa Requirements Form with valid inputs | User logged in as <Role> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Click Submit | Visa requirements displayed based on nationality and destination country | high |
| TC-002 | WF-002 | Submit Visa Application Form with valid inputs | User logged in as <Role> | 1. Fill in Full Name with <valid full name><br>2. Enter Passport Number as <valid passport number><br>3. Select Passport Expiry Date as <valid expiry date><br>4. Select Date of Birth as <valid date of birth><br>5. Enter Nationality as <valid nationality><br>6. Enter Email as <valid email><br>7. Enter Phone as <valid phone number><br>8. Fill in Purpose of Visit with <valid purpose><br>9. Select Intended Travel Dates as <valid travel dates><br>10. Enter Duration of Stay as <valid duration><br>11. Upload a file from the Document Upload section<br>12. Click Submit | Application submitted; success message shown | high |
| TC-003 | WF-003 | Track Application Status | User logged in as <Role> | 1. Click on Track Application Status link | Application status displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Select a valid Destination Country<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-005 | WF-001 | Leave the Destination Country dropdown blank and submit |  | 1. Select a valid Nationality<br>2. Leave the Destination Country dropdown blank<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-006 | WF-002 | Leave the Full Name field blank and submit Visa Application Form |  | 1. Leave the Full Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Full Name is not provided; error shown on Full Name field | high |
| TC-007 | WF-002 | Leave the Passport Number field blank and submit Visa Application Form |  | 1. Leave the Passport Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Passport Number is not provided; error shown on Passport Number field | high |
| TC-008 | WF-002 | Leave the Passport Expiry Date field blank and submit Visa Application Form |  | 1. Leave the Passport Expiry Date field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Passport Expiry Date is not provided; error shown on Passport Expiry Date field | high |
| TC-009 | WF-002 | Leave the Date of Birth field blank and submit Visa Application Form |  | 1. Leave the Date of Birth field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Date of Birth is not provided; error shown on Date of Birth field | high |
| TC-010 | WF-002 | Leave the Nationality field blank and submit Visa Application Form |  | 1. Leave the Nationality field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Nationality is not provided; error shown on Nationality field | high |
| TC-011 | WF-002 | Leave the Email field blank and submit Visa Application Form |  | 1. Leave the Email field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Email is not provided; error shown on Email field | high |
| TC-012 | WF-002 | Leave the Phone field blank and submit Visa Application Form |  | 1. Leave the Phone field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Phone is not provided; error shown on Phone field | high |
| TC-013 | WF-002 | Leave the Purpose of Visit field blank and submit Visa Application Form |  | 1. Leave the Purpose of Visit field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Purpose of Visit is not provided; error shown on Purpose of Visit field | high |
| TC-014 | WF-002 | Leave the Intended Travel Dates field blank and submit Visa Application Form |  | 1. Leave the Intended Travel Dates field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Intended Travel Dates is not provided; error shown on Intended Travel Dates field | high |
| TC-015 | WF-002 | Leave the Duration of Stay field blank and submit Visa Application Form |  | 1. Leave the Duration of Stay field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Duration of Stay is not provided; error shown on Duration of Stay field | high |
| TC-016 | WF-002 | Leave the Document Upload section empty and submit Visa Application Form |  | 1. Leave the Document Upload section empty<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Document Upload is not provided; error shown on Document Upload section | high |
| TC-017 |  | Attempt to access Track Application Status without authentication |  | 1. Navigate to the Track Application Status page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-002 | Enter a valid passport expiry date that is today | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter today's date in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter a valid Intended Travel Date in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a valid passport copy in the Document_Upload section<br>12. Click Submit | Application submitted; success message shown | medium |
| TC-019 (boundary) | WF-002 | Enter a passport expiry date that is one day in the past | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter a date that is one day before today in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter a valid Intended Travel Date in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a valid passport copy in the Document_Upload section<br>12. Click Submit | Form submission is blocked; error message displayed indicating the passport expiry date must be in the future | medium |
| TC-020 (boundary) | WF-002 | Enter a valid intended travel date that is today | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter a valid Passport Expiry Date in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter today's date in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a valid passport copy in the Document_Upload section<br>12. Click Submit | Application submitted; success message shown | medium |
| TC-021 (boundary) | WF-002 | Enter an intended travel date that is one day in the past | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter a valid Passport Expiry Date in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter a date that is one day before today in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a valid passport copy in the Document_Upload section<br>12. Click Submit | Form submission is blocked; error message displayed indicating intended travel date must be today or in the future | medium |
| TC-022 (boundary) | WF-002 | Upload a document exactly at the maximum file size limit | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter a valid Passport Expiry Date in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter a valid Intended Travel Date in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a document that is exactly at the maximum file size limit in the Document_Upload section<br>12. Click Submit | Application submitted; success message shown | medium |
| TC-023 (boundary) | WF-002 | Upload a document that exceeds the maximum file size limit | User is on the Visa Application Form | 1. Enter a valid Full Name in the Full_Name field<br>2. Enter a valid Passport Number in the Passport_Number field<br>3. Enter a valid Passport Expiry Date in the Passport_Expiry_Date field<br>4. Enter a valid Date of Birth in the Date_of_Birth field<br>5. Enter a valid Nationality in the Nationality field<br>6. Enter a valid Email in the Email field<br>7. Enter a valid Phone number in the Phone field<br>8. Enter a valid Purpose of Visit in the Purpose_of_Visit field<br>9. Enter a valid Intended Travel Date in the Intended_Travel_Dates field<br>10. Enter a valid Duration of Stay in the Duration_of_Stay field<br>11. Upload a document that exceeds the maximum file size limit in the Document_Upload section<br>12. Click Submit | Form submission is blocked; error message displayed indicating the file exceeds the maximum size limit | medium |

---

## User Dashboard

Total: **22** (positive: 8, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View booking details | User logged in as <Role>, User has at least one booking | 1. Click 'View Details' on a booking entry | Booking details displayed | high |
| TC-002 | WF-002 | Cancel booking | User logged in as <Role>, User has a booking that can be cancelled | 1. Click 'Cancel' on a booking entry<br>2. Confirm cancellation if prompted | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify booking | User logged in as <Role>, User has a booking that can be modified | 1. Click 'Modify' on a booking entry<br>2. Make changes to the booking<br>3. Submit the changes | Booking modified; success message shown | high |
| TC-004 | WF-004 | Download confirmations | User logged in as <Role>, User has bookings | 1. Click 'Download Confirmations' | Confirmations downloaded | medium |
| TC-005 | WF-005 | Download invoices | User logged in as <Role>, User has bookings | 1. Click 'Download Invoices' | Invoices downloaded | medium |
| TC-006 | WF-006 | Download vouchers | User logged in as <Role>, User has bookings | 1. Click 'Download Vouchers' | Vouchers downloaded | medium |
| TC-007 | WF-007 | Edit profile | User logged in as <Role> | 1. Click 'Edit' in My Profile section<br>2. Make changes to profile information<br>3. Submit the changes | Profile edited; success message shown | high |
| TC-008 | WF-008 | Logout | User logged in as <Role> | 1. Click 'End Session' | Session ended; user logged out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to cancel a booking when booking type and cancellation policy do not permit | User has a booking that cannot be cancelled | 1. Navigate to My Bookings<br>2. Click Cancel on the booking | Cancellation action is blocked; no cancellation occurs; error message shown indicating cancellation is not permitted | high |
| TC-010 |  | Attempt to modify a booking when booking type and cancellation policy do not permit | User has a booking that cannot be modified | 1. Navigate to My Bookings<br>2. Click Modify on the booking | Modification action is blocked; no modification occurs; error message shown indicating modification is not permitted | high |
| TC-011 |  | Attempt to edit profile without any changes | User is on My Profile section | 1. Click Edit button without making any changes | Profile remains unchanged; no changes saved; error message shown indicating no changes were made | medium |
| TC-012 |  | Attempt to download confirmations without any bookings | User has no bookings | 1. Navigate to My Bookings<br>2. Click Download Confirmations | Download action is blocked; no confirmations downloaded; error message shown indicating no bookings available | medium |
| TC-013 |  | Attempt to download invoices without any bookings | User has no bookings | 1. Navigate to My Bookings<br>2. Click Download Invoices | Download action is blocked; no invoices downloaded; error message shown indicating no bookings available | medium |
| TC-014 |  | Attempt to download vouchers without any bookings | User has no bookings | 1. Navigate to My Bookings<br>2. Click Download Vouchers | Download action is blocked; no vouchers downloaded; error message shown indicating no bookings available | medium |
| TC-015 |  | Attempt to logout when session is already ended | User has already logged out | 1. Click End Session button | Logout action is blocked; user remains logged out; error message shown indicating session has already ended | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-002 | Attempt to cancel a booking with a cancellation policy that permits cancellation | User has a booking with a cancellation policy that permits cancellation | 1. Navigate to My Bookings section<br>2. Click on Cancel for the eligible booking | Booking cancelled; success message shown | medium |
| TC-017 (boundary) | WF-002 | Attempt to cancel a booking with a cancellation policy that does not permit cancellation | User has a booking with a cancellation policy that does not permit cancellation | 1. Navigate to My Bookings section<br>2. Click on Cancel for the ineligible booking | Cancellation is blocked; error message shown indicating cancellation policy restrictions | medium |
| TC-018 (boundary) | WF-003 | Attempt to modify a booking with a cancellation policy that permits modification | User has a booking with a cancellation policy that permits modification | 1. Navigate to My Bookings section<br>2. Click on Modify for the eligible booking | Booking modified; success message shown | medium |
| TC-019 (boundary) | WF-003 | Attempt to modify a booking with a cancellation policy that does not permit modification | User has a booking with a cancellation policy that does not permit modification | 1. Navigate to My Bookings section<br>2. Click on Modify for the ineligible booking | Modification is blocked; error message shown indicating modification policy restrictions | medium |
| TC-020 (input_edge) |  | Enter a very long string in the Review field | User has completed a booking | 1. Navigate to Reviews section<br>2. Enter a string longer than 200 characters in the Review field | Review submission is either accepted or truncated with a visible indicator | low |
| TC-021 (input_edge) |  | Enter special characters in the Review field | User has completed a booking | 1. Navigate to Reviews section<br>2. Enter special characters in the Review field | Special characters are accepted or a specific error message is shown | low |
| TC-022 (interaction_edge) |  | Rapidly click Cancel after a successful booking cancellation | User has cancelled a booking successfully | 1. Navigate to My Bookings section<br>2. Click Cancel multiple times rapidly for the same booking | Only one cancellation is processed; subsequent clicks are ignored or blocked | medium |

---

## Booking Management

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details successfully | User logged in as <Role>, booking type and cancellation policy permit modification | 1. Click the Modify button | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 | WF-002 | Cancel booking successfully | User logged in as <Role> | 1. Click the Cancel button<br>2. Confirm cancellation in the confirmation dialog | refund initiated to original payment method | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to modify booking without meeting preconditions | booking type and cancellation policy do not permit modification | 1. Click on the Modify_Button | Modification is not allowed; no changes are made to the booking details |  |
| TC-004 | WF-002 | Attempt to cancel booking without explicit confirmation |  | 1. Click on the Cancel_Button | Cancellation is not processed; user is prompted to confirm cancellation |  |
| TC-005 | WF-002 | Attempt to cancel booking without confirming cancellation |  | 1. Click on the Cancel_Button<br>2. Do not confirm cancellation | Cancellation is not processed; user remains on the booking detail view |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Attempt to modify booking when availability is exactly at the limit | booking type and cancellation policy permit modification | 1. Click on Modify_Button<br>2. Attempt to change travel dates to a date that is available<br>3. Add special requests or update traveler information as needed | Modification succeeds; changes are reflected in the booking details | medium |
| TC-007 (boundary) | WF-001 | Attempt to modify booking when availability is just beyond the limit | booking type and cancellation policy permit modification | 1. Click on Modify_Button<br>2. Attempt to change travel dates to a date that is not available<br>3. Add special requests or update traveler information as needed | Modification is blocked; a message indicates that the selected dates are not available | medium |
| TC-008 (boundary) | WF-002 | Cancel booking without explicit confirmation | User is on the booking detail view | 1. Click on Cancel_Button<br>2. Do not confirm the cancellation | Cancellation is blocked; a message indicates that confirmation is required | medium |
| TC-009 (boundary) | WF-002 | Cancel booking with explicit confirmation | User is on the booking detail view | 1. Click on Cancel_Button<br>2. Confirm the cancellation | Cancellation succeeds; refund is initiated to the original payment method | medium |

---

## Payment Processing

Total: **15** (positive: 2, negative: 6, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Payment with Credit/Debit Card | User logged in as <Role>, Payment must be successful | 1. Select 'Credit/Debit Card' from the Payment Method dropdown<br>2. Enter <Cardholder Name> in the Cardholder Name field<br>3. Enter <valid card number> in the Card Number field<br>4. Enter <valid expiration date> in the Expiration Date field<br>5. Enter <valid CVV> in the CVV field<br>6. Click 'Submit Payment' | redirects to booking confirmation page | high |
| TC-002 | WF-002 | Retry Payment after failed transaction | User logged in as <Role>, Payment must have failed | 1. Click 'Retry Payment'<br>2. Select 'Credit/Debit Card' from the Payment Method dropdown<br>3. Enter <Cardholder Name> in the Cardholder Name field<br>4. Enter <valid card number> in the Card Number field<br>5. Enter <valid expiration date> in the Expiration Date field<br>6. Enter <valid CVV> in the CVV field<br>7. Click 'Submit Payment' | allows user to retry payment without losing booking details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave Cardholder Name blank when Credit/Debit Card is selected | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Cardholder_Name field blank<br>3. Fill in all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-004 |  | Leave Card Number blank when Credit/Debit Card is selected | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Card_Number field blank<br>3. Fill in all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-005 |  | Leave Expiration Date blank when Credit/Debit Card is selected | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Expiration_Date field blank<br>3. Fill in all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-006 |  | Leave CVV blank when Credit/Debit Card is selected | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the CVV field blank<br>3. Fill in all other required fields<br>4. Click Submit Payment | Inline validation error appears on the CVV field indicating it is required | high |
| TC-007 | WF-001 | Attempt to submit payment when payment has failed | payment must have failed | 1. Click Submit Payment | Form does not submit; user remains on the payment page with an error message indicating payment failure | high |
| TC-008 | WF-002 | Attempt to retry payment when payment has not failed | payment must be successful | 1. Click Retry Payment | Form does not submit; user remains on the payment page with an error message indicating payment cannot be retried | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter a valid card number with exactly 16 digits | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number with exactly 16 digits in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page | medium |
| TC-010 (boundary) | WF-001 | Enter a card number with 15 digits | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a card number with 15 digits in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submission is blocked; error shown indicating invalid card number length | medium |
| TC-011 (boundary) | WF-001 | Enter an expiration date that is today's date | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number in the Card_Number field<br>3. Enter today's date in the Expiration_Date field<br>4. Fill in all other required fields<br>5. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page | medium |
| TC-012 (boundary) | WF-001 | Enter an expiration date that is yesterday's date | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number in the Card_Number field<br>3. Enter yesterday's date in the Expiration_Date field<br>4. Fill in all other required fields<br>5. Click Submit Payment | Form submission is blocked; error shown indicating the expiration date is invalid | medium |
| TC-013 (interaction_edge) | WF-002 | Retry payment after a failed transaction | A payment has failed | 1. Click Retry Payment after the payment failure message is displayed | User is allowed to retry payment without losing booking details | medium |
| TC-014 (input_edge) |  | Enter a very long cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a long cardholder name (200+ characters) in the Cardholder_Name field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submission is blocked; error shown indicating the cardholder name is too long | low |
| TC-015 (input_edge) |  | Enter special characters in cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter special characters (e.g., @#$%) in the Cardholder_Name field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submission is blocked; error shown indicating invalid characters in the cardholder name | low |

---

## Currency & Language Selection

Total: **14** (positive: 8, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select USD currency | User logged in as <Role> | 1. Select 'USD' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-002 | WF-002 | Select EUR currency | User logged in as <Role> | 1. Select 'EUR' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-003 | WF-003 | Select GBP currency | User logged in as <Role> | 1. Select 'GBP' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-004 | WF-004 | Select JPY currency | User logged in as <Role> | 1. Select 'JPY' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-005 | WF-005 | Select English language | User logged in as <Role> | 1. Select 'English' from the Language dropdown | The entire site interface switches to English | high |
| TC-006 | WF-006 | Select Arabic language | User logged in as <Role> | 1. Select 'Arabic' from the Language dropdown | The entire site interface switches to Arabic | high |
| TC-007 | WF-007 | Select Spanish language | User logged in as <Role> | 1. Select 'Spanish' from the Language dropdown | The entire site interface switches to Spanish | high |
| TC-008 | WF-008 | Select French language | User logged in as <Role> | 1. Select 'French' from the Language dropdown | The entire site interface switches to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to select a currency when no selection is made |  | 1. Leave the Currency Selector blank<br>2. Click Select | Form does not submit; Currency Selector is highlighted with an error indicating selection is required | high |
| TC-010 |  | Attempt to select a language when no selection is made |  | 1. Leave the Language Selector blank<br>2. Click Select | Form does not submit; Language Selector is highlighted with an error indicating selection is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid currency selection change | User is on the currency selection page | 1. Select USD from the Currency Selector<br>2. Immediately select EUR from the Currency Selector | Prices are updated to EUR without delay; previous USD prices are not shown | medium |
| TC-012 (interaction_edge) | WF-005 | Rapid language selection change | User is on the language selection page | 1. Select English from the Language Selector<br>2. Immediately select Arabic from the Language Selector | Site interface switches to Arabic without delay; previous English labels are not shown | medium |
| TC-013 (input_edge) |  | Special characters in language selection | User is on the language selection page | 1. Enter special characters in the Language Selector | Language Selector displays an error indicating invalid selection | low |
| TC-014 (input_edge) |  | Leading/trailing whitespace in currency selection | User is on the currency selection page | 1. Select ' USD ' from the Currency Selector | Leading/trailing whitespace is trimmed; selected currency displayed as 'USD' | low |

---

## Search & Filters

Total: **26** (positive: 10, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters for Hotels | User logged in as <role> | 1. Click on the Hotels tab<br>2. Select 'Free WiFi' and 'Pool' from the Facilities/Amenities checkboxes<br>3. Select 'Luxury' from the Hotel Type dropdown<br>4. Select 'Bed & Breakfast' from the Board Basis dropdown<br>5. Enter <valid location> in the Location Area search field | Results update dynamically based on selected filters | high |
| TC-002 | WF-002 | Apply filters for Flights | User logged in as <role> | 1. Click on the Flights tab<br>2. Select 'Airline A' and 'Airline B' from the Airlines checkboxes<br>3. Select '1 Stop' from the Number of Stops dropdown<br>4. Adjust the Departure Time Range slider | Results update dynamically based on selected filters | high |
| TC-003 | WF-003 | Apply filters for Tours | User logged in as <role> | 1. Click on the Tours tab<br>2. Select 'Adventure' from the Tour Type dropdown<br>3. Adjust the Duration slider<br>4. Select a date range for Departure Dates | Results update dynamically based on selected filters | high |
| TC-004 | WF-004 | Apply filters for Cars | User logged in as <role> | 1. Click on the Cars tab<br>2. Select 'SUV' from the Car Type dropdown<br>3. Select 'Automatic' from the Transmission dropdown<br>4. Select 'Full to Full' from the Fuel Policy dropdown<br>5. Enter <valid rental company> in the Rental Company search field | Results update dynamically based on selected filters | high |
| TC-005 | WF-005 | Remove individual filter | User logged in as <role>, At least one filter is applied | 1. Click the Remove Filter button next to an active filter | Active filters updated; results refresh accordingly | medium |
| TC-006 | WF-006 | Reset all filters | User logged in as <role>, At least one filter is applied | 1. Click the Reset all filters button | All filters cleared; results refresh to show all listings | medium |
| TC-007 | WF-007 | Sort results by Price: Low to High | User logged in as <role> | 1. Select 'Price: Low to High' from the sorting dropdown | Results sorted by price from low to high | medium |
| TC-008 | WF-008 | Sort results by Price: High to Low | User logged in as <role> | 1. Select 'Price: High to Low' from the sorting dropdown | Results sorted by price from high to low | medium |
| TC-009 | WF-009 | Sort results by Rating: High to Low | User logged in as <role> | 1. Select 'Rating: High to Low' from the sorting dropdown | Results sorted by rating from high to low | medium |
| TC-010 | WF-010 | Sort results by Most Popular | User logged in as <role> | 1. Select 'Most Popular' from the sorting dropdown | Results sorted by popularity | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 | WF-001 | Attempt to apply filters for Hotels without selecting any filters |  | 1. Open the Hotels tab<br>2. Leave all filter options blank<br>3. Click Apply Filters | No filters applied; results remain unchanged |  |
| TC-012 | WF-002 | Attempt to apply filters for Flights without selecting any filters |  | 1. Open the Flights tab<br>2. Leave all filter options blank<br>3. Click Apply Filters | No filters applied; results remain unchanged |  |
| TC-013 | WF-003 | Attempt to apply filters for Tours without selecting any filters |  | 1. Open the Tours tab<br>2. Leave all filter options blank<br>3. Click Apply Filters | No filters applied; results remain unchanged |  |
| TC-014 | WF-004 | Attempt to apply filters for Cars without selecting any filters |  | 1. Open the Cars tab<br>2. Leave all filter options blank<br>3. Click Apply Filters | No filters applied; results remain unchanged |  |
| TC-015 | WF-005 | Attempt to remove a filter when no filters are active |  | 1. Ensure no filters are active<br>2. Click the Remove Filter button | No action taken; no filters to remove |  |
| TC-016 | WF-006 | Attempt to reset all filters when no filters are active |  | 1. Ensure no filters are active<br>2. Click Reset all filters | No action taken; no filters to reset |  |
| TC-017 | WF-007 | Attempt to sort results without any filters applied |  | 1. Click on Sort by Price: Low to High | Results remain unchanged; no filters applied |  |
| TC-018 | WF-008 | Attempt to sort results without any filters applied |  | 1. Click on Sort by Price: High to Low | Results remain unchanged; no filters applied |  |
| TC-019 | WF-009 | Attempt to sort results without any filters applied |  | 1. Click on Sort by Rating: High to Low | Results remain unchanged; no filters applied |  |
| TC-020 | WF-010 | Attempt to sort results without any filters applied |  | 1. Click on Sort by Most Popular | Results remain unchanged; no filters applied |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Add maximum allowed filters for Hotels | User is on the Hotels tab | 1. Select 'Free WiFi' in Facilities & Amenities<br>2. Select 'Luxury' in Hotel Type<br>3. Select 'Bed & Breakfast' in Board Basis<br>4. Enter a valid location in Location Area | All filters are applied successfully; results update dynamically. | medium |
| TC-022 (boundary) | WF-001 | Attempt to add one more filter than allowed for Hotels | User is on the Hotels tab with maximum filters applied | 1. Attempt to add another filter in Facilities & Amenities | Adding another filter is blocked; no additional filter is applied. | medium |
| TC-023 (interaction_edge) | WF-005 | Rapid removal of active filters | User has multiple active filters applied | 1. Click 'Remove Filter' on the first active filter<br>2. Immediately click 'Remove Filter' on the second active filter | Active filters are updated correctly; results refresh accordingly. | medium |
| TC-024 (interaction_edge) | WF-006 | Reset all filters after applying some | User has applied several filters | 1. Click 'Reset all filters' | All filters are cleared; results refresh to show all listings. | medium |
| TC-025 (boundary) | WF-007 | Sort results using the first sorting option | User is on the results page | 1. Select 'Price: Low to High' from the sorting dropdown | Results are sorted by price from low to high. | medium |
| TC-026 (boundary) | WF-008 | Sort results using the second sorting option | User is on the results page | 1. Select 'Price: High to Low' from the sorting dropdown | Results are sorted by price from high to low. | medium |

---

## Reviews & Ratings

Total: **13** (positive: 2, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Review without Photos | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Reviews section on the Detail Page<br>2. Enter <Overall Rating> in the Overall Rating field<br>3. Click 'Add Row' in the Category Ratings section<br>4. Enter <Cleanliness Rating> in the Cleanliness field<br>5. Enter <Service Rating> in the Service field<br>6. Enter <Location Rating> in the Location field<br>7. Enter <Written Feedback> in the Written Feedback field<br>8. Click Submit Review | A success notification is displayed; the message 'Review submitted successfully' is shown | high |
| TC-002 | WF-002 | Submit Review with Photos | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Reviews section on the Detail Page<br>2. Enter <Overall Rating> in the Overall Rating field<br>3. Click 'Add Row' in the Category Ratings section<br>4. Enter <Cleanliness Rating> in the Cleanliness field<br>5. Enter <Service Rating> in the Service field<br>6. Enter <Location Rating> in the Location field<br>7. Enter <Written Feedback> in the Written Feedback field<br>8. Click 'Upload' to select a <valid photo file><br>9. Click Submit Review | A success notification is displayed; the message 'Review submitted successfully' is shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave Overall Rating blank and submit review | user must be authenticated, user must have completed a booking | 1. Leave the Overall Rating field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Inline validation error appears on the Overall Rating field indicating it is required | high |
| TC-004 |  | Leave Cleanliness rating blank and submit review | user must be authenticated, user must have completed a booking | 1. Leave the Cleanliness field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Inline validation error appears on the Cleanliness field indicating it is required | high |
| TC-005 |  | Leave Service rating blank and submit review | user must be authenticated, user must have completed a booking | 1. Leave the Service field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Inline validation error appears on the Service field indicating it is required | high |
| TC-006 |  | Leave Location rating blank and submit review | user must be authenticated, user must have completed a booking | 1. Leave the Location field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Inline validation error appears on the Location field indicating it is required | high |
| TC-007 |  | Submit review without authentication |  | 1. Attempt to access the review submission form<br>2. Click Submit Review | User is redirected to the login page | high |
| TC-008 |  | Submit review without completed booking | user must be authenticated | 1. Attempt to access the review submission form<br>2. Click Submit Review | User is blocked from submitting the review; error message displayed indicating booking completion is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit review with minimum overall rating | user must be authenticated, user must have completed a booking | 1. Enter <minimum allowed value> in the Overall_Rating field<br>2. Fill all required fields in Category_Ratings with <minimum allowed value><br>3. Click Submit | Form submits successfully; review is created with the minimum overall rating | medium |
| TC-010 (boundary) | WF-001 | Submit review with maximum category ratings | user must be authenticated, user must have completed a booking | 1. Enter <maximum allowed value> in the Overall_Rating field<br>2. Fill all required fields in Category_Ratings with <maximum allowed value><br>3. Click Submit | Form submits successfully; review is created with the maximum overall rating | medium |
| TC-011 (boundary) | WF-001 | Submit review with one category rating below minimum | user must be authenticated, user must have completed a booking | 1. Enter <minimum allowed value> in the Overall_Rating field<br>2. Fill Cleanliness in Category_Ratings with <minimum allowed value><br>3. Fill Service in Category_Ratings with <minimum allowed value><br>4. Fill Location in Category_Ratings with <one unit below minimum><br>5. Click Submit | Submission is blocked; an error is shown indicating the rating for Location is below the minimum allowed | medium |
| TC-012 (boundary) | WF-002 | Upload file at exact size limit | user must be authenticated, user must have completed a booking | 1. Enter <minimum allowed value> in the Overall_Rating field<br>2. Fill all required fields in Category_Ratings with <minimum allowed value><br>3. Upload a file that is exactly at the size limit<br>4. Click Submit | Form submits successfully; review is created with the uploaded file | medium |
| TC-013 (boundary) | WF-002 | Upload file over size limit | user must be authenticated, user must have completed a booking | 1. Enter <minimum allowed value> in the Overall_Rating field<br>2. Fill all required fields in Category_Ratings with <minimum allowed value><br>3. Upload a file that is one unit over the size limit<br>4. Click Submit | Submission is blocked; an error is shown indicating the file exceeds the size limit | medium |

---

## Offers & Deals

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book Now for a selected offer | User logged in as <Role> | 1. Select 'Hotels' from the Service Type Filter dropdown<br>2. Enter <valid destination> in the Destination Filter<br>3. Select <valid travel date> in the Travel Dates Filter<br>4. Enter <valid email> in the Newsletter Subscription field<br>5. Click the 'Book Now' button for a selected offer | applies promotional code automatically or redirects to pre-filled search | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Newsletter Subscription field blank and submit |  | 1. Leave the Newsletter Subscription field blank<br>2. Fill all other filters as needed<br>3. Click Book Now | Inline validation error appears on the Newsletter Subscription field indicating it is required | high |
| TC-003 |  | Enter an invalid email format in the Newsletter Subscription field |  | 1. Enter <invalid email format> in the Newsletter Subscription field<br>2. Fill all other filters as needed<br>3. Click Book Now | Newsletter Subscription field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (boundary) | WF-001 | Enter today's date in the Travel Dates Filter |  | 1. Select 'Hotels' from the Service_Type_Filter<br>2. Enter today's date in the Travel_Dates_Filter<br>3. Click Book Now | Redirects to a pre-filled search with discounted rates applied | medium |
| TC-005 (boundary) | WF-001 | Enter yesterday's date in the Travel Dates Filter |  | 1. Select 'Flights' from the Service_Type_Filter<br>2. Enter yesterday's date in the Travel_Dates_Filter<br>3. Click Book Now | Redirect is blocked; visible error indicating travel dates must be today or later | medium |
| TC-006 (input_edge) |  | Enter a very long string in the Destination_Filter |  | 1. Select 'Packages' from the Service_Type_Filter<br>2. Enter a string longer than 200 characters in the Destination_Filter | Input is either accepted or truncated with a visible indicator | low |
| TC-007 (input_edge) |  | Enter an email with leading and trailing whitespace in the Newsletter_Subscription field |  | 1. Enter '   example@example.com   ' in the Newsletter_Subscription field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click the Logout button | User is redirected to the home page and the session is terminated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to access a protected page after logout |  | 1. Click the Logout button | User is redirected to the login page when attempting to access a protected page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid consecutive logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is ignored; user remains on the home page without a new session termination | medium |
| TC-004 (interaction_edge) | WF-001 | Access protected page after logout | User is logged in, User clicks Logout | 1. Click the Logout button<br>2. Attempt to navigate to a protected page | User is redirected to the login page with a message indicating session termination | medium |

---
