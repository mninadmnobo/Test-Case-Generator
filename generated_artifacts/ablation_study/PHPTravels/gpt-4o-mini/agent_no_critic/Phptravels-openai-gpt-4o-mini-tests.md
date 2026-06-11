# Test Cases — Phptravels

Generated: 2026-06-10T20:41:17.343965Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 301 | 57 | 132 | 112 | 157 | 107 | 35 |

## Home Page & Search

Total: **21** (positive: 4, negative: 8, edge: 9)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Hotels with valid inputs | User logged in as <Role> | 1. Click on the Hotels tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check In Date field<br>4. Enter <valid check-out date> in the Check Out Date field<br>5. Enter <valid number of rooms> in the Number of Rooms field<br>6. Enter <valid number of adults> in the Adults field<br>7. Click Search | redirects to corresponding results listing page | high |
| TC-002 | WF-002 | Search for Flights with valid inputs | User logged in as <Role> | 1. Click on the Flights tab<br>2. Select <valid trip type> from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Enter <valid departure date> in the Departure Date field<br>6. Enter <valid return date> in the Return Date field<br>7. Enter <valid number of adults> in the Adults field<br>8. Select <valid cabin class> from the Cabin Class dropdown<br>9. Click Search | redirects to corresponding results listing page | high |
| TC-003 | WF-003 | Search for Tours with valid inputs | User logged in as <Role> | 1. Click on the Tours tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid start date> in the Start Date field<br>4. Enter <valid end date> in the End Date field<br>5. Click Search | redirects to corresponding results listing page | high |
| TC-004 | WF-004 | Search for Cars with valid inputs | User logged in as <Role> | 1. Click on the Cars tab<br>2. Enter <valid pick-up location> in the Pick Up Location field<br>3. Enter <valid drop-off location> in the Drop Off Location field<br>4. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>6. Click Search | redirects to corresponding results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Destination field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill in the Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 | WF-001 | Leave all required fields empty and submit |  | 1. Click on the Hotels tab<br>2. Leave all required fields blank<br>3. Click Search | Inline validation errors appear on all required fields indicating they are required | high |
| TC-007 | WF-002 | Leave the Departure City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure City field blank<br>3. Fill in the Arrival_City, Trip_Type, Travel_Dates, Passenger_Count, and Cabin_Class fields<br>4. Click Search | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-008 | WF-002 | Leave all required fields empty and submit |  | 1. Click on the Flights tab<br>2. Leave all required fields blank<br>3. Click Search | Inline validation errors appear on all required fields indicating they are required | high |
| TC-009 | WF-003 | Leave the Destination field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Destination field blank<br>3. Fill in the Start_Date and End_Date fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-010 | WF-003 | Leave all required fields empty and submit |  | 1. Click on the Tours tab<br>2. Leave all required fields blank<br>3. Click Search | Inline validation errors appear on all required fields indicating they are required | high |
| TC-011 | WF-004 | Leave the Pick-Up Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick-Up Location field blank<br>3. Fill in the Drop_Off_Location, Pick_Up_Date_Time, and Drop_Off_Date_Time fields<br>4. Click Search | Inline validation error appears on the Pick-Up Location field indicating it is required | high |
| TC-012 | WF-004 | Leave all required fields empty and submit |  | 1. Click on the Cars tab<br>2. Leave all required fields blank<br>3. Click Search | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Check-In Date equals Check-Out Date | User is on the Hotels tab | 1. Enter a destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-014 (boundary) | WF-001 | Check-In Date one day before Check-Out Date | User is on the Hotels tab | 1. Enter a destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter tomorrow's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-015 (boundary) | WF-001 | Check-Out Date one day before Check-In Date | User is on the Hotels tab | 1. Enter a destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Inline error appears indicating Check-Out Date must be after Check-In Date | medium |
| TC-016 (boundary) | WF-002 | Departure Date equals Return Date | User is on the Flights tab | 1. Select 'One-way' in the Trip_Type dropdown<br>2. Enter a valid city in the Departure_City field<br>3. Enter a valid city in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter today's date in the Return_Date field<br>6. Enter a valid number in the Adults field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-017 (boundary) | WF-002 | Departure Date one day before Return Date | User is on the Flights tab | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter a valid city in the Departure_City field<br>3. Enter a valid city in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter tomorrow's date in the Return_Date field<br>6. Enter a valid number in the Adults field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-018 (boundary) | WF-002 | Return Date one day before Departure Date | User is on the Flights tab | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter a valid city in the Departure_City field<br>3. Enter a valid city in the Arrival_City field<br>4. Enter tomorrow's date in the Departure_Date field<br>5. Enter today's date in the Return_Date field<br>6. Enter a valid number in the Adults field | Inline error appears indicating Return Date must be after Departure Date | medium |
| TC-019 (boundary) | WF-003 | Start Date equals End Date | User is on the Tours tab | 1. Enter a destination in the Destination field<br>2. Enter today's date in the Start_Date field<br>3. Enter today's date in the End_Date field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-020 (boundary) | WF-003 | Start Date one day before End Date | User is on the Tours tab | 1. Enter a destination in the Destination field<br>2. Enter today's date in the Start_Date field<br>3. Enter tomorrow's date in the End_Date field | Form submits successfully; user is redirected to the results listing page | medium |
| TC-021 (boundary) | WF-003 | End Date one day before Start Date | User is on the Tours tab | 1. Enter a destination in the Destination field<br>2. Enter tomorrow's date in the Start_Date field<br>3. Enter today's date in the End_Date field | Inline error appears indicating End Date must be after Start Date | medium |

---

## User Registration

Total: **13** (positive: 1, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid details | User logged in as <New User>, User has not registered before | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid password> in the Password field<br>5. Enter <valid password> in the Confirm Password field<br>6. Check the Terms and Conditions checkbox<br>7. Click Submit | Account is created and redirects to dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Leave the Confirm Password field blank and submit |  | 1. Leave the Confirm_Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-007 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Email field displays an error: 'Must be a valid email format' | medium |
| TC-008 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields<br>4. Click Submit | Confirm_Password field displays an error: 'must match Password' | medium |
| TC-009 |  | Attempt to submit without verifying email |  | 1. Fill all required fields with valid data<br>2. Click Submit | Form does not submit; user is prompted to verify email before gaining access | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Email with valid format at the uniqueness boundary | User has an existing account with a specific email | 1. Enter 'test@example.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline error displays 'Email must be unique' | medium |
| TC-011 (input_edge) |  | Long text in First Name field |  | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline error displays indicating the input exceeds maximum length | low |
| TC-012 (input_edge) |  | Special characters in Last Name field |  | 1. Enter '@#$%^&*()' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Inline error displays indicating invalid characters in Last Name | low |
| TC-013 (input_edge) |  | Leading and trailing whitespace in Password field |  | 1. Enter '   mypassword   ' in the Password field<br>2. Enter '   mypassword   ' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## User Login

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User>, Valid credentials are available | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to dashboard or previous page | high |
| TC-002 | WF-002 | Login with invalid credentials | User logged in as <User>, Invalid credentials are available | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | shows error message | high |
| TC-003 | WF-003 | Login with CAPTCHA verification after multiple failed attempts | User logged in as <User>, Multiple consecutive failed attempts have occurred | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login<br>4. Enter <valid email> in the Email field<br>5. Enter <valid password> in the Password field<br>6. Click Login | redirects to dashboard or previous page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Fill the Email field with a valid email<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill the Password field with a valid password<br>3. Click Login | Error message shown indicating invalid email format; Password field is cleared | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Fill the Email field with a valid email<br>2. Fill the Password field with an incorrect password<br>3. Click Login | Error message shown indicating invalid credentials; Password field is cleared | high |
| TC-008 | WF-003 | Attempt to login without CAPTCHA after multiple failed attempts | multiple consecutive failed attempts | 1. Fill the Email field with a valid email<br>2. Fill the Password field with an incorrect password<br>3. Click Login | Error message shown indicating invalid credentials; Password field is cleared | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Attempt login with an email format that is just below the valid format | Email field is required, Password field is required | 1. Enter 'invalidemail' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message displays indicating invalid email format; password field is cleared | medium |
| TC-010 (boundary) | WF-002 | Attempt login with a password that is just below the minimum length requirement | Email field is required, Password field is required | 1. Enter a valid email in the Email field<br>2. Enter 'abc' in the Password field<br>3. Click Login | Error message displays indicating password is too short; password field is cleared | medium |
| TC-011 (interaction_edge) | WF-003 | Rapid consecutive login attempts with invalid credentials | Multiple consecutive failed attempts have occurred | 1. Enter a valid email in the Email field<br>2. Enter an invalid password in the Password field<br>3. Click Login<br>4. Immediately click Login again with the same invalid password | Error message displays after the first attempt; CAPTCHA verification is triggered after multiple failed attempts | medium |
| TC-012 (input_edge) |  | Enter a very long email address | Email field is required | 1. Enter a very long email address (over 255 characters) in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message displays indicating email exceeds maximum length; password field is cleared | low |
| TC-013 (input_edge) |  | Enter special characters in the email field | Email field is required | 1. Enter 'user!@example.com' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message displays indicating invalid email format; password field is cleared | low |

---

## Forgot Password

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send reset link to existing email | User logged in as <User>, Email exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is shown stating 'sends reset link to email' | high |
| TC-002 | WF-002 | Change password after clicking reset link | User clicked the reset link from their email | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | User is redirected to the login page with a success message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it must be a valid email address | high |
| TC-005 |  | Attempt to reset password with a non-existent email |  | 1. Enter <non-existent email> in the Email field<br>2. Click Reset Password | Error is shown indicating the email is not found; the form remains editable | high |
| TC-006 |  | Leave the New Password field blank and submit |  | 1. Leave the New Password field blank<br>2. Enter <valid password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-007 |  | Leave the Confirm Password field blank and submit |  | 1. Enter <valid password> in the New Password field<br>2. Leave the Confirm Password field blank<br>3. Click Change Password | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-008 |  | Submit with New Password and Confirm Password not matching |  | 1. Enter <valid password> in the New Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears indicating 'password must match Confirm_Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit email exactly matching an existing email in the system | Email exists in the system | 1. Enter a valid email address that exists in the system in the Email field<br>2. Click Reset Password | Reset link is sent to the email; confirmation message is shown | medium |
| TC-010 (boundary) | WF-001 | Submit email that does not exist in the system | Email does not exist in the system | 1. Enter an invalid email address that does not exist in the system in the Email field<br>2. Click Reset Password | Error is shown indicating the email is not found; form remains editable | medium |
| TC-011 (input_edge) |  | Enter a very long email address |  | 1. Enter a very long email address in the Email field (over 254 characters)<br>2. Click Reset Password | Error is shown indicating the email format is invalid or exceeds length limit | low |
| TC-012 (input_edge) |  | Enter email with leading and trailing whitespace |  | 1. Enter '   user@example.com   ' in the Email field<br>2. Click Reset Password | Leading/trailing whitespace is trimmed; confirmation message is shown if email exists | low |
| TC-013 (boundary) | WF-002 | Submit matching passwords on the Password Reset Page |  | 1. Enter a new password in the New Password field<br>2. Enter the same password in the Confirm Password field<br>3. Click Change Password | Redirects to login page with success message | medium |
| TC-014 (boundary) | WF-002 | Submit non-matching passwords on the Password Reset Page |  | 1. Enter a new password in the New Password field<br>2. Enter a different password in the Confirm Password field<br>3. Click Change Password | Error is shown indicating passwords do not match; form remains editable | medium |

---

## Hotels Search & Listing

Total: **17** (positive: 2, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for hotels with valid input | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <valid number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' to add guest count<br>6. Enter <valid number of adults> in the Adults field<br>7. Enter <valid number of children> in the Children field (optional)<br>8. Click Search | redirects to listing page | high |
| TC-002 | WF-002 | Book a hotel from the listing page | User logged in as <Role>, User is on the listing page | 1. Click Book Now on the first hotel card | Hotel booking initiated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 | WF-001 | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-005 | WF-001 | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-006 | WF-001 | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-007 | WF-001 | Leave all required fields blank and submit |  | 1. Leave the Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms fields blank<br>2. Fill Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms fields indicating they are required | high |
| TC-008 | WF-001 | Enter an invalid date in Check_In_Date field |  | 1. Enter <invalid date format> in the Check_In_Date field<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it must be a valid date | medium |
| TC-009 | WF-001 | Enter an invalid date in Check_Out_Date field |  | 1. Enter <invalid date format> in the Check_Out_Date field<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it must be a valid date | medium |
| TC-010 | WF-001 | Enter a negative number in Number_of_Rooms field |  | 1. Enter <negative number> in the Number_of_Rooms field<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it must be a positive number | medium |
| TC-011 | WF-001 | Attempt to search with Check_Out_Date before Check_In_Date |  | 1. Fill Destination with valid value<br>2. Enter <future date> in Check_In_Date field<br>3. Enter <past date> in Check_Out_Date field<br>4. Fill Number_of_Rooms and Guest_Count with valid values<br>5. Click Search | Inline validation error appears indicating Check_Out_Date must be after Check_In_Date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Check-in date is the same as check-out date |  | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-013 (boundary) | WF-001 | Check-out date is one day before check-in date |  | 1. Enter a valid destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submission is blocked; error message displayed indicating check-out date must be after check-in date | medium |
| TC-014 (boundary) | WF-001 | Add maximum allowed entries in the guest count repeating group |  | 1. Enter a valid destination in the Destination field<br>2. Enter a valid check-in date in the Check_In_Date field<br>3. Enter a valid check-out date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add maximum allowed entries in the Guest_Count repeating group<br>6. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-015 (boundary) | WF-001 | Attempt to add one more entry than allowed in the guest count repeating group |  | 1. Enter a valid destination in the Destination field<br>2. Enter a valid check-in date in the Check_In_Date field<br>3. Enter a valid check-out date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add maximum allowed entries + 1 in the Guest_Count repeating group<br>6. Click Search | Form submission is blocked; error message displayed indicating maximum guest count exceeded | medium |
| TC-016 (input_edge) |  | Enter a very long destination name |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Enter a valid check-in date in the Check_In_Date field<br>3. Enter a valid check-out date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submission is blocked; error message displayed indicating destination name is too long | low |
| TC-017 (input_edge) |  | Enter special characters in the destination field |  | 1. Enter special characters in the Destination field<br>2. Enter a valid check-in date in the Check_In_Date field<br>3. Enter a valid check-out date in the Check_Out_Date field<br>4. Enter a valid number of rooms in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submits successfully; user is redirected to the listing page | low |

---

## Hotel Details & Booking

Total: **13** (positive: 1, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking after filling the form | User logged in as <Role> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Enter <valid stay dates> in the Stay Dates field<br>6. Enter <valid guest count> in the Guest Count field<br>7. Click Book Now | Redirects to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Phone Number field blank |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-006 |  | Leave the Stay Dates field blank |  | 1. Leave the Stay_Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay_Dates field indicating it is required | high |
| TC-007 |  | Leave the Guest Count field blank |  | 1. Leave the Guest_Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest_Count field indicating it is required | high |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Book Now | Form does not submit; error shown on First_Name, Last_Name, Email, Phone_Number, Stay_Dates, and Guest_Count fields | high |
| TC-009 |  | Attempt to book without being logged in |  | 1. Ensure the user is logged out<br>2. Fill all required fields<br>3. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Enter minimum guest count | User is logged in | 1. Enter '1' in the Guest Count field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Form submits successfully; proceeds to payment page | medium |
| TC-011 (boundary) | WF-001 | Enter one unit below minimum guest count | User is logged in | 1. Enter '0' in the Guest Count field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Guest Count displays an error indicating the value is below the minimum allowed | medium |
| TC-012 (input_edge) |  | Enter long text in Special Requests |  | 1. Enter a string of 200+ characters in the Special Requests field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Form submits successfully; the Special Requests field shows the long text correctly | low |
| TC-013 (input_edge) |  | Enter special characters in First Name |  | 1. Enter '@John#' in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Book Now | Form submits successfully; the First Name field shows '@John#' correctly | low |

---

## Flights Search & Listing

Total: **12** (positive: 2, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for flights with valid inputs | User logged in as <Role> | 1. Enter 'New York' in the Departure City field<br>2. Enter 'Los Angeles' in the Arrival City field<br>3. Select 'Round-trip' from the Trip Type dropdown<br>4. Enter <valid travel date> in the Travel Dates field<br>5. Click 'Add Row' in the Passenger Count section<br>6. Enter '2' in the Adults field<br>7. Click 'Add Row' again in the Passenger Count section<br>8. Enter '1' in the Children field<br>9. Select 'Economy' from the Cabin Class dropdown<br>10. Click 'Search Flights' | redirects to listing page | high |
| TC-002 | WF-002 | Select a flight from the listing | User logged in as <Role>, User is on the flights listing page | 1. Click 'Select' on the first flight result | Flight selected for booking | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave all required fields blank and submit the search form |  | 1. Leave the Trip_Type field blank<br>2. Leave the Departure_City field blank<br>3. Leave the Arrival_City field blank<br>4. Leave the Travel_Dates field blank<br>5. Leave the Passenger_Count fields (Adults, Children, Infants) blank<br>6. Leave the Cabin_Class field blank<br>7. Click on Search Flights | Form does not submit; error shown on Trip_Type, Departure_City, Arrival_City, Travel_Dates, Passenger_Count, and Cabin_Class fields indicating they are required | high |
| TC-004 | WF-001 | Leave the Trip_Type field blank and submit the search form |  | 1. Leave the Trip_Type field blank<br>2. Fill in valid values for all other fields<br>3. Click on Search Flights | Form does not submit; error shown on Trip_Type field indicating it is required | high |
| TC-005 | WF-001 | Enter an invalid date in the Travel_Dates field |  | 1. Select a valid Trip_Type<br>2. Fill in valid Departure_City and Arrival_City<br>3. Enter <invalid date format> in the Travel_Dates field<br>4. Fill in valid Passenger_Count<br>5. Select a valid Cabin_Class<br>6. Click on Search Flights | Form does not submit; error shown on Travel_Dates field indicating it must be a valid date | medium |
| TC-006 | WF-001 | Enter a negative number in the Adults field of Passenger_Count |  | 1. Select a valid Trip_Type<br>2. Fill in valid Departure_City and Arrival_City<br>3. Enter a valid date in the Travel_Dates field<br>4. Enter <negative number> in the Adults field of Passenger_Count<br>5. Fill in valid values for Children and Infants<br>6. Select a valid Cabin_Class<br>7. Click on Search Flights | Form does not submit; error shown on Adults field indicating it must be a non-negative number | medium |
| TC-007 | WF-002 | Attempt to select a flight without any flights listed |  | 1. Navigate to the Flights Listing page with no flights available<br>2. Click on Select button for a flight | No action occurs; error shown indicating no flights are available to select | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Test maximum passenger count entries | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Add exactly 1 Adult, 1 Child, and 1 Infant in the Passenger Count section<br>6. Select 'Economy' from the Cabin Class dropdown<br>7. Click 'Search Flights' | Redirects to listing page with search results displayed | medium |
| TC-009 (boundary) | WF-001 | Test exceeding maximum passenger count entries | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Add 2 Adults, 2 Children, and 2 Infants in the Passenger Count section<br>6. Select 'Economy' from the Cabin Class dropdown<br>7. Click 'Search Flights' | Search is blocked; visible error shown indicating maximum passenger count exceeded | medium |
| TC-010 (input_edge) |  | Test long text input in Departure City field | User is on the Flights Search Form | 1. Enter a string of 200+ characters in the Departure City field | Field displays an error indicating the input exceeds the maximum allowed length | low |
| TC-011 (input_edge) |  | Test special characters in Arrival City field | User is on the Flights Search Form | 1. Enter special characters (e.g., @#$%^&*) in the Arrival City field | Field displays an error indicating invalid characters | low |
| TC-012 (interaction_edge) |  | Test rapid re-submission after redirect | User has successfully submitted the search form | 1. Press the browser back button after being redirected to the listing page | User is redirected to the Flights Search Form without pre-filled data | medium |

---

## Flight Booking

Total: **16** (positive: 1, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit booking form with valid data | User logged in as <Role> | 1. Select 'Mr' from the Title dropdown<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter a valid date in the Date of Birth field<br>5. Enter <valid passport number> in the Passport Number field<br>6. Enter a valid date in the Passport Expiry field<br>7. Enter <valid email> in the Lead Passenger Email field<br>8. Enter <valid phone number> in the Lead Passenger Phone field<br>9. Click Continue | User proceeds to payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Title field blank and submit |  | 1. Leave the Title field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Title field indicating it is required | high |
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Date of Birth field blank and submit |  | 1. Leave the Date_of_Birth field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Date_of_Birth field indicating it is required | high |
| TC-006 |  | Leave the Passport Number field blank and submit |  | 1. Leave the Passport_Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Passport_Number field indicating it is required | high |
| TC-007 |  | Leave the Passport Expiry field blank and submit |  | 1. Leave the Passport_Expiry field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Passport_Expiry field indicating it is required | high |
| TC-008 |  | Leave the Lead Passenger Email field blank and submit |  | 1. Leave the Lead_Passenger_Email field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Email field indicating it is required | high |
| TC-009 |  | Leave the Lead Passenger Phone field blank and submit |  | 1. Leave the Lead_Passenger_Phone field blank<br>2. Fill all other required fields with valid data<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Phone field indicating it is required | high |
| TC-010 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Continue | Form does not submit; all required fields display inline validation errors | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Enter a valid date of birth exactly on the minimum age limit |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter 'John' in the First_Name field<br>3. Enter 'Doe' in the Last_Name field<br>4. Enter a date of birth that is exactly the minimum age required<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter a valid Passport_Expiry date that is after the date of birth<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Proceeds to payment page | medium |
| TC-012 (boundary) | WF-001 | Enter a date of birth one day before the minimum age limit |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter 'John' in the First_Name field<br>3. Enter 'Doe' in the Last_Name field<br>4. Enter a date of birth that is one day before the minimum age required<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter a valid Passport_Expiry date that is after the date of birth<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Inline error displayed for Date_of_Birth; progression is blocked | medium |
| TC-013 (boundary) | WF-001 | Enter a valid Passport_Expiry date that is exactly today |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter 'John' in the First_Name field<br>3. Enter 'Doe' in the Last_Name field<br>4. Enter a valid Date_of_Birth<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter today's date in the Passport_Expiry field<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Proceeds to payment page | medium |
| TC-014 (boundary) | WF-001 | Enter a Passport_Expiry date that is one day before today |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter 'John' in the First_Name field<br>3. Enter 'Doe' in the Last_Name field<br>4. Enter a valid Date_of_Birth<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter a date that is one day before today in the Passport_Expiry field<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Inline error displayed for Passport_Expiry; progression is blocked | medium |
| TC-015 (input_edge) |  | Enter a very long string in First_Name field |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter a string of 200+ characters in the First_Name field<br>3. Enter 'Doe' in the Last_Name field<br>4. Enter a valid Date_of_Birth<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter a valid Passport_Expiry date<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Inline error displayed for First_Name; progression is blocked | low |
| TC-016 (input_edge) |  | Enter special characters in Last_Name field |  | 1. Select 'Mr' from the Title dropdown<br>2. Enter '@#$%' in the Last_Name field<br>3. Enter 'John' in the First_Name field<br>4. Enter a valid Date_of_Birth<br>5. Enter 'A12345678' in the Passport_Number field<br>6. Enter a valid Passport_Expiry date<br>7. Enter 'john.doe@example.com' in the Lead_Passenger_Email field<br>8. Enter '1234567890' in the Lead_Passenger_Phone field<br>9. Click Continue | Inline error displayed for Last_Name; progression is blocked | low |

---

## Tours Search & Listing

Total: **15** (positive: 1, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for tours with valid inputs | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select 'Adventure' from the Tour Type dropdown<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid budget range> in the Budget Range field<br>6. Click Search | User is redirected to the listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-003 | WF-001 | Leave the Travel Dates field blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-004 | WF-001 | Leave the Tour Type field blank and submit |  | 1. Leave the Tour Type field blank<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Tour Type field indicating it is required | high |
| TC-005 | WF-001 | Leave the Duration field blank and submit |  | 1. Leave the Duration field blank<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Duration field indicating it is required | high |
| TC-006 | WF-001 | Leave the Budget Range field blank and submit |  | 1. Leave the Budget Range field blank<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Budget Range field indicating it is required | high |
| TC-007 | WF-001 | Submit the form with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Search | Form does not submit; error shown on Destination, Travel Dates, Tour Type, Duration, and Budget Range fields | high |
| TC-008 |  | Enter an invalid date in the Travel Dates field |  | 1. Enter <invalid date format> in the Travel Dates field<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it must be a valid date | medium |
| TC-009 |  | Enter a non-numeric value in the Duration field |  | 1. Enter <non-numeric value> in the Duration field<br>2. Fill in all other required fields<br>3. Click Search | Inline validation error appears on the Duration field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Enter minimum valid duration in the Duration field |  | 1. Enter <minimum allowed value> in the Duration field<br>2. Fill all other required fields<br>3. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-011 (boundary) | WF-001 | Enter one unit below minimum valid duration in the Duration field |  | 1. Enter <one unit below minimum> in the Duration field<br>2. Fill all other required fields<br>3. Click Search | Form submission is blocked; an error message is shown indicating the duration is below the minimum allowed | medium |
| TC-012 (boundary) | WF-001 | Enter a valid date in the Travel Dates field |  | 1. Enter today's date in the Travel Dates field<br>2. Fill all other required fields<br>3. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-013 (boundary) | WF-001 | Enter a date that is one day before today in the Travel Dates field |  | 1. Enter yesterday's date in the Travel Dates field<br>2. Fill all other required fields<br>3. Click Search | Form submission is blocked; an error message is shown indicating the travel date must be today or later | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Destination field |  | 1. Enter a string of 200+ characters in the Destination field<br>2. Fill all other required fields<br>3. Click Search | Form submission is blocked; an error message is shown indicating the destination is too long | low |
| TC-015 (input_edge) |  | Enter special characters in the Budget Range field |  | 1. Enter special characters in the Budget Range field<br>2. Fill all other required fields<br>3. Click Search | Form submission is blocked; an error message is shown indicating invalid characters | low |

---

## Tour Details & Booking

Total: **11** (positive: 1, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking with valid traveler details | User logged in as <authenticated user>, Departure date is available | 1. Select a valid <departure date> from the available options<br>2. Click 'Add Row' under Number of Travelers<br>3. Enter <number of adults> in the Adults field<br>4. Enter <number of children> in the Children field<br>5. Click 'Add Row' under Traveler Details<br>6. Enter <traveler name> in the Name field<br>7. Enter <contact details> in the Contact Details field<br>8. Click 'Book Now' | User is redirected to the booking confirmation page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the Departure Date blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Fill in the Number_of_Travelers with valid data<br>3. Fill in the Traveler_Details with valid data<br>4. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-003 | WF-001 | Leave all required fields blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Leave the Number_of_Travelers section blank<br>3. Leave the Traveler_Details section blank<br>4. Click Book Now | Form does not submit; error shown on Departure_Date, Number_of_Travelers, and Traveler_Details fields | high |
| TC-004 | WF-001 | Unauthenticated user attempts to book a tour |  | 1. Attempt to click Book Now without logging in | User is redirected to the login page | high |
| TC-005 | WF-001 | Enter a non-numeric value in the Adults field |  | 1. Fill in the Departure_Date with a valid date<br>2. Fill in the Number_of_Travelers with a non-numeric value in the Adults field<br>3. Fill in the Traveler_Details with valid data<br>4. Click Book Now | Inline validation error appears on the Adults field indicating it must be a number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Select a departure date that is today | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the Number_of_Travelers<br>3. Click Book Now | Booking proceeds to confirmation page as the departure date is valid | medium |
| TC-007 (boundary) | WF-001 | Add maximum number of adult travelers | User is authenticated | 1. Add maximum allowed number of Adults in Number_of_Travelers<br>2. Click Book Now | Booking proceeds to confirmation page with the correct number of adults displayed | medium |
| TC-008 (boundary) | WF-001 | Add one more adult traveler than allowed | User is authenticated | 1. Add maximum allowed number of Adults + 1 in Number_of_Travelers<br>2. Click Book Now | Booking is blocked with an error indicating the maximum number of travelers has been exceeded | medium |
| TC-009 (input_edge) | WF-001 | Enter a very long name in Traveler Details | User is authenticated | 1. Enter a name with 200+ characters in the Name field<br>2. Fill in other required fields<br>3. Click Book Now | Form submits successfully; name is displayed correctly in the confirmation page | low |
| TC-010 (input_edge) | WF-001 | Enter special characters in Contact Details | User is authenticated | 1. Enter special characters in the Contact_Details field<br>2. Fill in other required fields<br>3. Click Book Now | Form submits successfully; contact details are displayed correctly in the confirmation page | low |
| TC-011 (interaction_edge) | WF-001 | Rapid re-submission after booking confirmation | User is authenticated | 1. Click Book Now<br>2. After confirmation, click back in the browser | User is redirected to a blank booking form, no duplicate booking is created | low |

---

## Cars Search & Listing

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for cars with valid inputs | User logged in as <Role> | 1. Enter <valid pick-up location> in the Pick Up Location field<br>2. Enter <valid drop-off location> in the Drop Off Location field<br>3. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>4. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>5. Enter <valid driver age> in the Driver Age field<br>6. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | Book a vehicle from the listing | User logged in as <Role>, User is on the listing page with available vehicles | 1. Click Book Now on a vehicle listing | Booking confirmed; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Pick Up Location blank and submit |  | 1. Leave the Pick Up Location blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick Up Location field indicating it is required | high |
| TC-004 |  | Leave the Drop Off Location blank and submit |  | 1. Leave the Drop Off Location blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop Off Location field indicating it is required | high |
| TC-005 |  | Leave the Pick Up Date Time blank and submit |  | 1. Leave the Pick Up Date Time blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick Up Date Time field indicating it is required | high |
| TC-006 |  | Leave the Drop Off Date Time blank and submit |  | 1. Leave the Drop Off Date Time blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop Off Date Time field indicating it is required | high |
| TC-007 |  | Leave the Driver Age blank and submit |  | 1. Leave the Driver Age blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Driver Age field indicating it is required | high |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Form does not submit; error shown on Pick Up Location, Drop Off Location, Pick Up Date Time, Drop Off Date Time, and Driver Age fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Pick Up Date Time is set to today | User is on the car rental search form | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Redirects to the listing page; search results displayed for today | medium |
| TC-010 (boundary) | WF-001 | Drop Off Date Time is set to the same day as Pick Up Date Time | User is on the car rental search form | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter the same date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Redirects to the listing page; search results displayed for the same day | medium |
| TC-011 (boundary) | WF-001 | Driver Age is set to the minimum legal age | User is on the car rental search form | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter the minimum legal age in the Driver Age field<br>6. Click Search | Redirects to the listing page; search results displayed for the minimum age | medium |
| TC-012 (boundary) | WF-001 | Driver Age is set to one year below the minimum legal age | User is on the car rental search form | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter one year below the minimum legal age in the Driver Age field<br>6. Click Search | Search is blocked; error message displayed indicating age restriction | medium |
| TC-013 (input_edge) |  | Leading and trailing whitespace in Pick Up Location | User is on the car rental search form | 1. Enter '   Valid Location   ' in the Pick Up Location field<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Leading/trailing whitespace is trimmed; search results displayed for 'Valid Location' | low |
| TC-014 (input_edge) |  | Special characters in Drop Off Location | User is on the car rental search form | 1. Enter a valid Pick Up Location<br>2. Enter '@#$%^&*()' in the Drop Off Location field<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Search is blocked; error message displayed indicating invalid characters in location | low |

---

## Car Booking

Total: **13** (positive: 1, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm Booking with all valid fields | User logged in as <Role> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid license issue country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click 'Add Row' to add optional add-ons<br>8. Check the GPS checkbox<br>9. Select <valid insurance plan> from the Insurance Plan dropdown<br>10. Accept the terms and conditions<br>11. Click Confirm Booking | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave the Driver Full Name field blank |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 | WF-001 | Leave the Age field blank |  | 1. Leave the Age field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-004 | WF-001 | Leave the License Number field blank |  | 1. Leave the License Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-005 | WF-001 | Leave the License Issue Country field blank |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-006 | WF-001 | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 | WF-001 | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-008 | WF-001 | Select an invalid Insurance Plan |  | 1. Select an invalid Insurance Plan<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating it is required | high |
| TC-009 | WF-001 | Submit the form with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Confirm Booking | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Enter minimum age in the Age field |  | 1. Enter <minimum allowed value> in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; proceeds to payment | medium |
| TC-011 (boundary) | WF-001 | Enter one unit below minimum age in the Age field |  | 1. Enter <one unit below minimum> in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Age field displays an error indicating the value is below the minimum allowed | medium |
| TC-012 (boundary) | WF-001 | Add maximum allowed entries to the Add_Ons repeating group |  | 1. Add <maximum allowed entries> rows to the Add_Ons repeating group<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; proceeds to payment | medium |
| TC-013 (boundary) | WF-001 | Attempt to add one entry beyond the maximum allowed in the Add_Ons repeating group |  | 1. Add <maximum allowed entries + 1> rows to the Add_Ons repeating group<br>2. Fill all other required fields<br>3. Click Confirm Booking | Add_Ons section displays an error indicating maximum entries exceeded | medium |

---

## Visa Services

Total: **21** (positive: 3, negative: 13, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Visa Requirements Form with valid nationality and destination | User logged in as <Role> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Click Submit | Visa requirements displayed based on selected nationality and destination country | high |
| TC-002 | WF-002 | Submit Visa Application Form with valid personal and travel details | User logged in as <Role> | 1. Fill in Full Name with <valid full name><br>2. Enter Passport Number as <valid passport number><br>3. Select Passport Expiry Date as <valid expiry date><br>4. Select Date of Birth as <valid birth date><br>5. Fill in Nationality with <valid nationality><br>6. Enter Email as <valid email><br>7. Enter Phone as <valid phone number><br>8. Fill in Purpose of Visit with <valid purpose><br>9. Select Intended Travel Dates as <valid travel dates><br>10. Enter Duration of Stay as <valid duration><br>11. Upload a valid passport copy<br>12. Click Submit | Application submitted successfully; confirmation message shown | high |
| TC-003 | WF-003 | Track Application Status | User logged in as <Role> | 1. Click Track Application Status | Application status displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave the Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Select a Destination Country<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-005 | WF-001 | Leave the Destination Country dropdown blank and submit |  | 1. Select a Nationality<br>2. Leave the Destination Country dropdown blank<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-006 | WF-002 | Leave the Full Name field blank and submit the Visa Application Form |  | 1. Leave the Full Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Full Name field | high |
| TC-007 | WF-002 | Leave the Passport Number field blank and submit the Visa Application Form |  | 1. Leave the Passport Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Passport Number field | high |
| TC-008 | WF-002 | Leave the Passport Expiry Date field blank and submit the Visa Application Form |  | 1. Leave the Passport Expiry Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Passport Expiry Date field | high |
| TC-009 | WF-002 | Leave the Date of Birth field blank and submit the Visa Application Form |  | 1. Leave the Date of Birth field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Date of Birth field | high |
| TC-010 | WF-002 | Leave the Nationality field blank and submit the Visa Application Form |  | 1. Leave the Nationality field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Nationality field | high |
| TC-011 | WF-002 | Leave the Email field blank and submit the Visa Application Form |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Email field | high |
| TC-012 | WF-002 | Leave the Phone field blank and submit the Visa Application Form |  | 1. Leave the Phone field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Phone field | high |
| TC-013 | WF-002 | Leave the Purpose of Visit field blank and submit the Visa Application Form |  | 1. Leave the Purpose of Visit field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Purpose of Visit field | high |
| TC-014 | WF-002 | Leave the Intended Travel Dates field blank and submit the Visa Application Form |  | 1. Leave the Intended Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Intended Travel Dates field | high |
| TC-015 | WF-002 | Leave the Duration of Stay field blank and submit the Visa Application Form |  | 1. Leave the Duration of Stay field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Duration of Stay field | high |
| TC-016 | WF-002 | Leave the Document Upload field blank and submit the Visa Application Form |  | 1. Leave the Document Upload field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Application is not created; error shown on Document Upload field | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-002 | Enter today's date in the Passport Expiry Date field | User is on the Visa Application Form | 1. Enter a valid full name in the Full Name field<br>2. Enter a valid passport number in the Passport Number field<br>3. Enter today's date in the Passport Expiry Date field<br>4. Enter a valid date of birth in the Date of Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose of Visit field<br>9. Enter a valid intended travel date in the Intended Travel Dates field<br>10. Enter a valid duration of stay in the Duration of Stay field<br>11. Upload a required document in the Document Upload section<br>12. Click Submit | Application submitted successfully; confirmation message shown | medium |
| TC-018 (boundary) | WF-002 | Enter yesterday's date in the Passport Expiry Date field | User is on the Visa Application Form | 1. Enter a valid full name in the Full Name field<br>2. Enter a valid passport number in the Passport Number field<br>3. Enter yesterday's date in the Passport Expiry Date field<br>4. Enter a valid date of birth in the Date of Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose of Visit field<br>9. Enter a valid intended travel date in the Intended Travel Dates field<br>10. Enter a valid duration of stay in the Duration of Stay field<br>11. Upload a required document in the Document Upload section<br>12. Click Submit | Error shown indicating that the passport expiry date must be in the future | medium |
| TC-019 (boundary) | WF-002 | Enter a date far in the future in the Intended Travel Dates field | User is on the Visa Application Form | 1. Enter a valid full name in the Full Name field<br>2. Enter a valid passport number in the Passport Number field<br>3. Enter a valid passport expiry date in the Passport Expiry Date field<br>4. Enter a valid date of birth in the Date of Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose of Visit field<br>9. Enter a date far in the future in the Intended Travel Dates field<br>10. Enter a valid duration of stay in the Duration of Stay field<br>11. Upload a required document in the Document Upload section<br>12. Click Submit | Application submitted successfully; confirmation message shown | medium |
| TC-020 (boundary) | WF-002 | Upload a file exactly at the size limit in the Document Upload section | User is on the Visa Application Form | 1. Enter a valid full name in the Full Name field<br>2. Enter a valid passport number in the Passport Number field<br>3. Enter a valid passport expiry date in the Passport Expiry Date field<br>4. Enter a valid date of birth in the Date of Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose of Visit field<br>9. Enter a valid intended travel date in the Intended Travel Dates field<br>10. Enter a valid duration of stay in the Duration of Stay field<br>11. Upload a file exactly at the size limit in the Document Upload section<br>12. Click Submit | Application submitted successfully; confirmation message shown | medium |
| TC-021 (boundary) | WF-002 | Upload a file one byte over the size limit in the Document Upload section | User is on the Visa Application Form | 1. Enter a valid full name in the Full Name field<br>2. Enter a valid passport number in the Passport Number field<br>3. Enter a valid passport expiry date in the Passport Expiry Date field<br>4. Enter a valid date of birth in the Date of Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose of Visit field<br>9. Enter a valid intended travel date in the Intended Travel Dates field<br>10. Enter a valid duration of stay in the Duration of Stay field<br>11. Upload a file one byte over the size limit in the Document Upload section<br>12. Click Submit | Error shown indicating that the file exceeds the maximum allowed size | medium |

---

## User Dashboard

Total: **22** (positive: 8, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Booking Details | User logged in as <Role>, User has at least one booking | 1. Click 'View Details' on a booking row | Booking details displayed | high |
| TC-002 | WF-002 | Cancel Booking | User logged in as <Role>, User has a booking where booking type and cancellation policy permit | 1. Click 'Cancel' on a booking row<br>2. Confirm cancellation | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify Booking | User logged in as <Role>, User has a booking where booking type and cancellation policy permit | 1. Click 'Modify' on a booking row<br>2. Make changes to the booking<br>3. Submit the changes | Booking modified; success message shown | high |
| TC-004 | WF-004 | Download Confirmations | User logged in as <Role>, User has bookings to download confirmations for | 1. Click 'Download Confirmations' | Confirmations downloaded | medium |
| TC-005 | WF-005 | Download Invoices | User logged in as <Role>, User has bookings to download invoices for | 1. Click 'Download Invoices' | Invoices downloaded | medium |
| TC-006 | WF-006 | Download Vouchers | User logged in as <Role>, User has bookings to download vouchers for | 1. Click 'Download Vouchers' | Vouchers downloaded | medium |
| TC-007 | WF-007 | Edit Profile | User logged in as <Role> | 1. Click 'Edit' in My Profile section<br>2. Make changes to profile information<br>3. Submit the changes | Profile edited; success message shown | high |
| TC-008 | WF-008 | Logout | User logged in as <Role> | 1. Click 'End Session' | Session ended; user logged out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to cancel a booking when the booking type and cancellation policy do not permit | Booking type and cancellation policy do not permit | 1. Navigate to My Bookings<br>2. Select a booking that cannot be canceled<br>3. Click Cancel | Error shown indicating cancellation is not permitted due to booking type and cancellation policy | high |
| TC-010 |  | Attempt to modify a booking when the booking type and cancellation policy do not permit | Booking type and cancellation policy do not permit | 1. Navigate to My Bookings<br>2. Select a booking that cannot be modified<br>3. Click Modify | Error shown indicating modification is not permitted due to booking type and cancellation policy | high |
| TC-011 |  | Attempt to submit a review with empty rating and review text |  | 1. Navigate to Reviews<br>2. Leave Rating blank<br>3. Leave Review Text blank<br>4. Click Submit | Inline validation error appears on the Rating field indicating it is required; Inline validation error appears on the Review Text field indicating it is required | high |
| TC-012 |  | Attempt to edit profile without any changes |  | 1. Navigate to My Profile<br>2. Click Edit<br>3. Leave all fields unchanged<br>4. Click Save | Form does not submit; no changes made to the profile | medium |
| TC-013 |  | Attempt to access the dashboard without being logged in |  | 1. Attempt to access User Dashboard | User is redirected to the login page | high |
| TC-014 |  | Attempt to change password with an empty new password field |  | 1. Navigate to Settings<br>2. Leave Change Password field blank<br>3. Click Save | Inline validation error appears on the Change Password field indicating it is required | high |
| TC-015 |  | Attempt to logout while already logged out |  | 1. Attempt to click End Session | Error shown indicating user is not logged in | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-002 | Cancel booking with valid conditions | Booking type and cancellation policy permit | 1. Navigate to My Bookings<br>2. Select a booking that can be cancelled<br>3. Click on Cancel | Booking cancelled; success message shown | medium |
| TC-017 (boundary) | WF-002 | Attempt to cancel booking when conditions are not met | Booking type and cancellation policy do not permit | 1. Navigate to My Bookings<br>2. Select a booking that cannot be cancelled<br>3. Click on Cancel | Cancellation is blocked; error message shown indicating cancellation is not permitted | medium |
| TC-018 (boundary) | WF-003 | Modify booking with valid conditions | Booking type and cancellation policy permit | 1. Navigate to My Bookings<br>2. Select a booking that can be modified<br>3. Click on Modify | Booking modified; success message shown | medium |
| TC-019 (boundary) | WF-003 | Attempt to modify booking when conditions are not met | Booking type and cancellation policy do not permit | 1. Navigate to My Bookings<br>2. Select a booking that cannot be modified<br>3. Click on Modify | Modification is blocked; error message shown indicating modification is not permitted | medium |
| TC-020 (input_edge) |  | Enter long review text |  | 1. Navigate to Reviews<br>2. Enter a review text longer than 200 characters | Review is accepted or truncated with a visible indicator | low |
| TC-021 (input_edge) |  | Enter special characters in review text |  | 1. Navigate to Reviews<br>2. Enter special characters in the Review_Text field | Special characters are accepted or a specific error is shown | low |
| TC-022 (input_edge) |  | Enter leading/trailing whitespace in review text |  | 1. Navigate to Reviews<br>2. Enter a review text with leading and trailing spaces | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Booking Management

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details | User logged in as <Role>, booking type and cancellation policy permit modification | 1. Click the Modify button | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 | WF-002 | Open cancellation confirmation flow | User logged in as <Role>, user must explicitly confirm before cancellation is processed | 1. Click the Cancel button | opens cancellation confirmation flow | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to modify booking without meeting preconditions | booking type and cancellation policy do not permit modification | 1. Click Modify_Button | Modification is blocked; no changes are allowed to the booking. | high |
| TC-004 | WF-002 | Attempt to cancel booking without explicit confirmation | user does not confirm cancellation | 1. Click Cancel_Button | Cancellation is blocked; user is not redirected to the cancellation confirmation flow. | high |
| TC-005 |  | Attempt to modify booking when subject to availability and applicable fees are not met | subject to availability and applicable fees are not met | 1. Click Modify_Button | Modification is blocked; no changes are allowed to the booking. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Attempt to modify booking when availability is at the limit | booking type and cancellation policy permit modification | 1. Attempt to modify the booking with the maximum number of changes allowed<br>2. Click Modify_Button | Modification is allowed; changes are successfully applied. | medium |
| TC-007 (boundary) | WF-001 | Attempt to modify booking when availability exceeds limit | booking type and cancellation policy permit modification | 1. Attempt to modify the booking beyond the maximum number of changes allowed<br>2. Click Modify_Button | Modification is blocked; an error message indicates changes exceed the limit. | medium |
| TC-008 (boundary) | WF-002 | Cancel booking without explicit confirmation | user must explicitly confirm before cancellation is processed | 1. Click Cancel_Button | Cancellation is blocked; a message prompts for explicit confirmation. | medium |
| TC-009 (boundary) | WF-002 | Cancel booking with explicit confirmation | user must explicitly confirm before cancellation is processed | 1. Click Cancel_Button<br>2. Confirm cancellation in the confirmation flow | Cancellation is processed; refund is initiated to the original payment method. | medium |

---

## Payment Processing

Total: **22** (positive: 6, negative: 9, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Payment with Credit/Debit Card | User logged in as <Role>, Payment_Method is set to 'Credit/Debit Card' | 1. Enter <Cardholder_Name> in the Cardholder Name field<br>2. Enter <Card_Number> in the Card Number field<br>3. Enter <Expiration_Date> in the Expiration Date field<br>4. Enter <CVV> in the CVV field<br>5. Click Submit Payment | redirects to booking confirmation page | high |
| TC-002 | WF-002 | Submit Payment with PayPal | User logged in as <Role>, Payment_Method is set to 'PayPal' | 1. Click Submit Payment | redirects to booking confirmation page | high |
| TC-003 | WF-003 | Submit Payment with Bank Transfer | User logged in as <Role>, Payment_Method is set to 'Bank Transfer' | 1. Click Submit Payment | redirects to booking confirmation page | high |
| TC-004 | WF-004 | Submit Payment with Wallet/Credits | User logged in as <Role>, Payment_Method is set to 'Wallet/Credits' | 1. Click Submit Payment | redirects to booking confirmation page | high |
| TC-005 | WF-005 | Download Invoice after Payment Success | User logged in as <Role>, Payment is successful | 1. Click Download Invoice | Invoice downloaded | medium |
| TC-006 | WF-006 | Download Voucher after Payment Success | User logged in as <Role>, Payment is successful | 1. Click Download Voucher | Voucher downloaded | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave Cardholder Name blank when Payment Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Leave the Cardholder_Name field blank<br>3. Fill in Card_Number, Expiration_Date, and CVV<br>4. Click Submit Payment | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-008 |  | Leave Card Number blank when Payment Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name, leave Card_Number blank<br>3. Fill in Expiration_Date and CVV<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-009 |  | Leave Expiration Date blank when Payment Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name, Card_Number, leave Expiration_Date blank<br>3. Fill in CVV<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-010 |  | Leave CVV blank when Payment Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in Cardholder_Name, Card_Number, Expiration_Date, leave CVV blank<br>3. Click Submit Payment | Inline validation error appears on the CVV field indicating it is required | high |
| TC-011 |  | Submit Payment without filling any required fields |  | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Leave all required fields (Cardholder_Name, Card_Number, Expiration_Date, CVV) blank<br>3. Click Submit Payment | Form does not submit; error shown on Cardholder_Name, Card_Number, Expiration_Date, and CVV fields indicating they are required | high |
| TC-012 |  | Attempt to submit payment without successful payment | payment must be unsuccessful | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Fill in all required fields with valid data<br>3. Click Submit Payment | Form does not submit; error message displays describing the issue | high |
| TC-013 | WF-007 | Attempt to retry payment when previous payment was successful | entity_state is Payment_Success | 1. Click Retry Payment | No action occurs; error message displays indicating payment cannot be retried | medium |
| TC-014 | WF-005 | Attempt to download invoice when payment has failed | entity_state is Payment_Failure | 1. Click Download Invoice | No action occurs; error message displays indicating invoice cannot be downloaded | medium |
| TC-015 | WF-006 | Attempt to download voucher when payment has failed | entity_state is Payment_Failure | 1. Click Download Voucher | No action occurs; error message displays indicating voucher cannot be downloaded | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-001 | Test card number at minimum length | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter exactly <minimum length card number> in the Card_Number field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submits successfully; payment processing initiated | medium |
| TC-017 (boundary) | WF-001 | Test card number at maximum length | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter exactly <maximum length card number> in the Card_Number field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submits successfully; payment processing initiated | medium |
| TC-018 (boundary) | WF-001 | Test expiration date as today | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter today's date in the Expiration_Date field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submits successfully; payment processing initiated | medium |
| TC-019 (boundary) | WF-001 | Test expiration date as yesterday | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter yesterday's date in the Expiration_Date field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submission is blocked; error message displays 'Expiration date must be in the future' | medium |
| TC-020 (input_edge) | WF-001 | Enter long cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter a very long string (200+ characters) in the Cardholder_Name field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submission is blocked; error message displays 'Cardholder name exceeds maximum length' | low |
| TC-021 (input_edge) | WF-001 | Enter special characters in cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method dropdown<br>2. Enter special characters in the Cardholder_Name field<br>3. Fill all other required fields with valid data<br>4. Click Submit Payment | Form submission is blocked; error message displays 'Invalid characters in cardholder name' | low |
| TC-022 (interaction_edge) | WF-001 | Rapid re-submission after payment success | Payment has been successfully processed | 1. Click Submit Payment<br>2. After redirection to booking confirmation page, press the browser back button | User is redirected to the payment form, which is blank (not pre-filled) | medium |

---

## Currency & Language Selection

Total: **14** (positive: 8, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select USD as currency | User logged in as <Role> | 1. Select 'USD' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-002 | WF-002 | Select EUR as currency | User logged in as <Role> | 1. Select 'EUR' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-003 | WF-003 | Select GBP as currency | User logged in as <Role> | 1. Select 'GBP' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-004 | WF-004 | Select JPY as currency | User logged in as <Role> | 1. Select 'JPY' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-005 | WF-005 | Select English as language | User logged in as <Role> | 1. Select 'English' from the Language dropdown | The entire site interface switches to English | high |
| TC-006 | WF-006 | Select Arabic as language | User logged in as <Role> | 1. Select 'Arabic' from the Language dropdown | The entire site interface switches to Arabic | high |
| TC-007 | WF-007 | Select Spanish as language | User logged in as <Role> | 1. Select 'Spanish' from the Language dropdown | The entire site interface switches to Spanish | high |
| TC-008 | WF-008 | Select French as language | User logged in as <Role> | 1. Select 'French' from the Language dropdown | The entire site interface switches to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to select a currency without making a selection |  | 1. Leave the Currency Selector blank<br>2. Click Select | Inline validation error appears on the Currency Selector field indicating it is required | high |
| TC-010 |  | Attempt to select a language without making a selection |  | 1. Leave the Language Selector blank<br>2. Click Select | Inline validation error appears on the Language Selector field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid currency selection | User is on the currency selection page | 1. Select USD from the Currency Selector<br>2. Immediately select EUR from the Currency Selector | Prices are updated in real-time to reflect EUR without any delay or error message | medium |
| TC-012 (interaction_edge) | WF-005 | Rapid language selection | User is on the language selection page | 1. Select English from the Language Selector<br>2. Immediately select Arabic from the Language Selector | The site interface switches to Arabic without any delay or error message | medium |
| TC-013 (input_edge) |  | Special characters in currency selection | User is on the currency selection page | 1. Attempt to input special characters in the Currency Selector | Currency selection remains unchanged; no special characters are accepted | low |
| TC-014 (input_edge) |  | Special characters in language selection | User is on the language selection page | 1. Attempt to input special characters in the Language Selector | Language selection remains unchanged; no special characters are accepted | low |

---

## Search & Filters

Total: **20** (positive: 6, negative: 6, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters for Hotels | User logged in as <Role> | 1. Expand the Filter Section<br>2. Select 'Wi-Fi' from the Facilities/Amenities checkbox<br>3. Select 'Luxury' from the Hotel Type dropdown<br>4. Select 'All Inclusive' from the Board Basis dropdown<br>5. Enter <valid location> in the Location Area search field | Results update dynamically based on selected filters | high |
| TC-002 | WF-002 | Apply filters for Flights | User logged in as <Role> | 1. Expand the Filter Section<br>2. Select 'Airline A' from the Airlines checkbox<br>3. Select 'Non-stop' from the Number of Stops dropdown<br>4. Adjust the Departure Time Range slider | Results update dynamically based on selected filters | high |
| TC-003 | WF-003 | Apply filters for Tours | User logged in as <Role> | 1. Expand the Filter Section<br>2. Select 'Adventure' from the Tour Type dropdown<br>3. Adjust the Duration slider<br>4. Select a date range in the Departure Dates field | Results update dynamically based on selected filters | high |
| TC-004 | WF-004 | Apply filters for Cars | User logged in as <Role> | 1. Expand the Filter Section<br>2. Select 'SUV' from the Car Type dropdown<br>3. Select 'Automatic' from the Transmission dropdown<br>4. Select 'Full to Full' from the Fuel Policy dropdown<br>5. Select 'Company A' from the Rental Company dropdown | Results update dynamically based on selected filters | high |
| TC-005 | WF-005 | Remove individual filter | User logged in as <Role>, At least one filter is applied | 1. Click the remove button for the 'Wi-Fi' filter | Active filters updated; results refreshed | medium |
| TC-006 | WF-006 | Reset all filters | User logged in as <Role>, At least one filter is applied | 1. Click the Reset All Filters button | All filters cleared; results refreshed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Attempt to apply filters for Hotels without selecting any options |  | 1. Open the Hotels tab<br>2. Leave all filter options blank<br>3. Click View_Details | Form does not submit; no filters applied; error shown indicating that at least one filter must be selected | high |
| TC-008 | WF-002 | Attempt to apply filters for Flights without selecting any options |  | 1. Open the Flights tab<br>2. Leave all filter options blank<br>3. Click View_Details | Form does not submit; no filters applied; error shown indicating that at least one filter must be selected | high |
| TC-009 | WF-003 | Attempt to apply filters for Tours without selecting any options |  | 1. Open the Tours tab<br>2. Leave all filter options blank<br>3. Click View_Details | Form does not submit; no filters applied; error shown indicating that at least one filter must be selected | high |
| TC-010 | WF-004 | Attempt to apply filters for Cars without selecting any options |  | 1. Open the Cars tab<br>2. Leave all filter options blank<br>3. Click View_Details | Form does not submit; no filters applied; error shown indicating that at least one filter must be selected | high |
| TC-011 | WF-005 | Attempt to remove a filter when no filters are active |  | 1. Ensure no filters are currently applied<br>2. Click on any Remove button for active filters | No action occurs; error shown indicating that there are no active filters to remove | medium |
| TC-012 | WF-006 | Attempt to reset filters when no filters are active |  | 1. Ensure no filters are currently applied<br>2. Click Reset_All_Filters | No action occurs; error shown indicating that there are no filters to reset | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Test price range slider at minimum value |  | 1. Set the Price Range slider to the minimum value | Results update dynamically showing listings within the minimum price range | medium |
| TC-014 (boundary) | WF-001 | Test price range slider just above minimum value |  | 1. Set the Price Range slider to one unit above the minimum value | Results update dynamically showing listings within the adjusted price range | medium |
| TC-015 (boundary) | WF-001 | Test price range slider at maximum value |  | 1. Set the Price Range slider to the maximum value | Results update dynamically showing listings within the maximum price range | medium |
| TC-016 (boundary) | WF-001 | Test price range slider just above maximum value |  | 1. Set the Price Range slider to one unit above the maximum value | Results are blocked from updating; no listings shown for the invalid price range | medium |
| TC-017 (input_edge) | WF-001 | Enter special characters in Location Area search |  | 1. Enter special characters in the Location Area search field | Inline error shown indicating invalid input | low |
| TC-018 (input_edge) | WF-001 | Enter leading/trailing whitespace in Location Area search |  | 1. Enter leading and trailing spaces in the Location Area search field | Leading/trailing whitespace is trimmed; saved value shown in the results grid has no extra spaces | low |
| TC-019 (interaction_edge) | WF-005 | Rapidly remove individual filters | At least one filter is applied | 1. Click the remove button for the first active filter<br>2. Immediately click the remove button for the second active filter | Active filters are updated; results refreshed without showing previously removed filters | medium |
| TC-020 (interaction_edge) | WF-006 | Rapidly reset all filters | At least one filter is applied | 1. Click the Reset All Filters button<br>2. Immediately click the Reset All Filters button again | All filters are cleared; results refreshed without showing any filters applied | medium |

---

## Reviews & Ratings

Total: **9** (positive: 1, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a review successfully | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter <Overall Experience Rating> in the Overall Experience Rating field<br>3. Enter <Cleanliness Rating> in the Cleanliness field<br>4. Enter <Service Rating> in the Service field<br>5. Enter <Location Rating> in the Location field<br>6. Enter <Written Feedback> in the Written Feedback field<br>7. Click Submit Review | A success notification shows 'review submitted' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to submit a review without authentication | user is not authenticated | 1. Navigate to the Submit Review form<br>2. Fill in the Overall Experience Rating, Category Ratings, and Written Feedback<br>3. Click Submit Review | Form does not submit; user is redirected to the login page indicating authentication is required | high |
| TC-003 | WF-001 | Attempt to submit a review without completing a booking | user is authenticated, user has not completed a booking | 1. Navigate to the Submit Review form<br>2. Fill in the Overall Experience Rating, Category Ratings, and Written Feedback<br>3. Click Submit Review | Form does not submit; error message displayed indicating booking completion is required | high |
| TC-004 |  | Leave Overall Experience Rating blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Overall Experience Rating blank<br>3. Fill in Category Ratings and Written Feedback<br>4. Click Submit Review | Inline validation error appears on the Overall Experience Rating field indicating it is required | high |
| TC-005 |  | Leave Written Feedback blank and submit |  | 1. Navigate to the Submit Review form<br>2. Fill in Overall Experience Rating and Category Ratings<br>3. Leave Written Feedback blank<br>4. Click Submit Review | Inline validation error appears on the Written Feedback field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Submit review with maximum allowed ratings and comments | user must be authenticated, user must have completed a booking | 1. Enter maximum allowed value in the Overall Experience Rating field<br>2. Enter maximum allowed values in the Category Ratings fields for Cleanliness, Service, and Location<br>3. Enter maximum length string in the Written Feedback field<br>4. Click Submit Review | Review is submitted successfully; confirmation message displayed | medium |
| TC-007 (boundary) | WF-001 | Submit review with one rating below minimum | user must be authenticated, user must have completed a booking | 1. Enter one unit below minimum value in the Overall Experience Rating field<br>2. Fill all other required fields with valid data<br>3. Click Submit Review | Submission is blocked; error message displayed indicating rating is below minimum allowed | medium |
| TC-008 (input_edge) |  | Enter long text in Written Feedback field | user must be authenticated, user must have completed a booking | 1. Enter a string of 200+ characters in the Written Feedback field<br>2. Click Submit Review | Form submits successfully; feedback is truncated to maximum allowed length | low |
| TC-009 (input_edge) |  | Enter special characters in Reviewer Name field | user must be authenticated, user must have completed a booking | 1. Enter special characters in the Reviewer Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit Review | Submission is blocked; error message displayed indicating invalid characters in Reviewer Name | low |

---

## Offers & Deals

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book Now action applies promotional code or redirects | User logged in as <Role> | 1. Select 'Hotels' from the Service Type Filter dropdown<br>2. Enter <valid destination> in the Destination Filter<br>3. Select <valid travel date> in the Travel Dates Filter<br>4. Enter <valid email> in the Newsletter Subscription field<br>5. Click the Book Now button for a selected offer | applies promotional code automatically or redirects to pre-filled search | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Newsletter Subscription field blank and submit |  | 1. Leave the Newsletter Subscription field blank<br>2. Fill all other filters (Service Type, Destination, Travel Dates)<br>3. Click Book Now | Inline validation error appears on the Newsletter Subscription field indicating it is required | high |
| TC-003 |  | Enter an invalid email format in the Newsletter Subscription field |  | 1. Enter <invalid email format> in the Newsletter Subscription field<br>2. Fill all other filters (Service Type, Destination, Travel Dates)<br>3. Click Book Now | Inline validation error appears on the Newsletter Subscription field indicating 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (boundary) | WF-001 | Select a valid travel date | User is on the Offers page | 1. Select a date in the Travel Dates Filter | Booking process succeeds with promotional code applied | medium |
| TC-005 (boundary) | WF-001 | Select an invalid travel date (past date) | User is on the Offers page | 1. Enter a past date in the Travel Dates Filter | Booking process is blocked; error message displayed indicating the date must be in the future | medium |
| TC-006 (input_edge) |  | Enter a very long email address for newsletter subscription | User is on the Offers page | 1. Enter a long email address in the Newsletter Subscription field | Form submits successfully; email is saved correctly without truncation | low |
| TC-007 (input_edge) |  | Enter special characters in the destination filter | User is on the Offers page | 1. Enter special characters in the Destination Filter | Form submits successfully; search results are displayed based on valid destination query | low |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click Logout_Button | terminates current session and redirects to home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to access a protected page after logout |  | 1. Click Logout<br>2. Attempt to access a protected page | User is redirected to the login page; session is not active | high |
| TC-003 |  | Click Logout button when already logged out |  | 1. Ensure user is logged out<br>2. Click Logout button | No action occurs; user remains on the current page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is blocked; user remains on the home page without any session termination action. |  |
| TC-005 (interaction_edge) | WF-001 | Access protected page after logout | User is logged in, User clicks Logout | 1. Click the Logout button<br>2. Attempt to access a protected page | User is redirected to the login page after attempting to access the protected page. |  |

---
