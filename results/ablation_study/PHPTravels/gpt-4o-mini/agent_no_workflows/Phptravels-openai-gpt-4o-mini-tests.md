# Test Cases — Phptravels

Generated: 2026-06-10T20:38:47.113660Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 329 | 75 | 143 | 111 | 162 | 120 | 39 |

## Home Page & Search

Total: **30** (positive: 4, negative: 18, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for Hotels with valid inputs | User logged in as <User> | 1. Click on the 'Hotels' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check In Date field<br>4. Enter <valid check-out date> in the Check Out Date field<br>5. Enter <valid number> in the Number of Rooms field<br>6. Click 'Add Row' in the Guest Count section<br>7. Enter <valid number> in the Adults field of the new row<br>8. Enter <valid number> in the Children field of the new row<br>9. Click 'Search' | redirects to the corresponding results listing page | high |
| TC-002 |  | Search for Flights with valid inputs | User logged in as <User> | 1. Click on the 'Flights' tab<br>2. Select 'Round-trip' from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Click 'Add Row' in the Travel Dates section<br>6. Enter <valid departure date> in the Departure Date field of the new row<br>7. Enter <valid return date> in the Return Date field of the new row<br>8. Click 'Add Row' in the Passenger Count section<br>9. Enter <valid number> in the Adults field of the new row<br>10. Click 'Search' | redirects to the corresponding results listing page | high |
| TC-003 |  | Search for Tours with valid inputs | User logged in as <User> | 1. Click on the 'Tours' tab<br>2. Enter <valid destination> in the Destination field<br>3. Click 'Add Row' in the Travel Date Range section<br>4. Enter <valid start date> in the Start Date field of the new row<br>5. Enter <valid end date> in the End Date field of the new row<br>6. Click 'Search' | redirects to the corresponding results listing page | high |
| TC-004 |  | Search for Cars with valid inputs | User logged in as <User> | 1. Click on the 'Cars' tab<br>2. Enter <valid pick-up location> in the Pick Up Location field<br>3. Enter <valid drop-off location> in the Drop Off Location field<br>4. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>6. Click 'Search' | redirects to the corresponding results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Destination field blank in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 |  | Leave the Check_In_Date field blank in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Check_In_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-007 |  | Leave the Check_Out_Date field blank in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Check_Out_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-008 |  | Leave the Number_of_Rooms field blank in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Number_of_Rooms field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-009 |  | Leave the Adults field blank in the Guest_Count group in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Adults field blank in the Guest_Count group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-010 |  | Leave the Children field blank in the Guest_Count group in the Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Children field blank in the Guest_Count group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Children field indicating it is required | high |
| TC-011 |  | Leave the Trip_Type field blank in the Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Trip_Type field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Trip_Type field indicating it is required | high |
| TC-012 |  | Leave the Departure_City field blank in the Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Departure_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_City field indicating it is required | high |
| TC-013 |  | Leave the Arrival_City field blank in the Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Arrival_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Arrival_City field indicating it is required | high |
| TC-014 |  | Leave the Departure_Date field blank in the Travel_Dates group in the Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Departure_Date field blank in the Travel_Dates group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-015 |  | Leave the Return_Date field blank in the Travel_Dates group in the Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Return_Date field blank in the Travel_Dates group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Return_Date field indicating it is required | high |
| TC-016 |  | Leave the Destination field blank in the Tours tab |  | 1. Navigate to the Tours tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-017 |  | Leave the Start_Date field blank in the Travel_Date_Range group in the Tours tab |  | 1. Navigate to the Tours tab<br>2. Leave the Start_Date field blank in the Travel_Date_Range group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Start_Date field indicating it is required | high |
| TC-018 |  | Leave the End_Date field blank in the Travel_Date_Range group in the Tours tab |  | 1. Navigate to the Tours tab<br>2. Leave the End_Date field blank in the Travel_Date_Range group<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the End_Date field indicating it is required | high |
| TC-019 |  | Leave the Pick_Up_Location field blank in the Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Pick_Up_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-020 |  | Leave the Drop_Off_Location field blank in the Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Drop_Off_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-021 |  | Leave the Pick_Up_Date_Time field blank in the Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Pick_Up_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-022 |  | Leave the Drop_Off_Date_Time field blank in the Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Drop_Off_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 (boundary) |  | Check-In Date equals Check-Out Date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one guest count entry with valid numbers for Adults and Children<br>6. Click Search | Search succeeds and redirects to the results listing page | medium |
| TC-024 (boundary) |  | Check-Out Date is one day before Check-In Date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one guest count entry with valid numbers for Adults and Children<br>6. Click Search | Search is blocked; inline error shows that Check-Out Date must be after Check-In Date | medium |
| TC-025 (boundary) |  | Add maximum number of guests in the repeating group | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter valid dates in the Check_In_Date and Check_Out_Date fields<br>3. Enter a valid number in the Number_of_Rooms field<br>4. Add maximum allowed entries for guest count with valid numbers for Adults and Children<br>5. Click Search | Search succeeds and redirects to the results listing page | medium |
| TC-026 (boundary) |  | Attempt to add one more guest entry beyond maximum | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter valid dates in the Check_In_Date and Check_Out_Date fields<br>3. Enter a valid number in the Number_of_Rooms field<br>4. Add maximum allowed entries for guest count with valid numbers for Adults and Children<br>5. Attempt to add one more guest count entry<br>6. Click Search | Search is blocked; inline error shows that maximum guest entries exceeded | medium |
| TC-027 (data_edge) |  | Enter today's date in the Travel Dates for Flights | User is on the Flights tab | 1. Select a valid Trip_Type from the dropdown<br>2. Enter valid cities in the Departure_City and Arrival_City fields<br>3. Add a travel date entry with today's date in the Departure_Date field<br>4. Add a travel date entry with a future date in the Return_Date field<br>5. Click Search | Search succeeds and redirects to the results listing page | medium |
| TC-028 (data_edge) |  | Enter a past date in the Travel Dates for Flights | User is on the Flights tab | 1. Select a valid Trip_Type from the dropdown<br>2. Enter valid cities in the Departure_City and Arrival_City fields<br>3. Add a travel date entry with yesterday's date in the Departure_Date field<br>4. Add a travel date entry with a future date in the Return_Date field<br>5. Click Search | Search is blocked; inline error shows that Departure_Date cannot be in the past | medium |
| TC-029 (input_edge) |  | Enter a very long string in the Destination field | User is on the Hotels tab | 1. Enter a string longer than 200 characters in the Destination field<br>2. Enter valid dates in the Check_In_Date and Check_Out_Date fields<br>3. Enter a valid number in the Number_of_Rooms field<br>4. Add at least one guest count entry with valid numbers for Adults and Children<br>5. Click Search | Search is blocked; inline error shows that input exceeds maximum length | low |
| TC-030 (input_edge) |  | Enter special characters in the Destination field | User is on the Hotels tab | 1. Enter special characters in the Destination field<br>2. Enter valid dates in the Check_In_Date and Check_Out_Date fields<br>3. Enter a valid number in the Number_of_Rooms field<br>4. Add at least one guest count entry with valid numbers for Adults and Children<br>5. Click Search | Search is blocked; inline error shows that input contains invalid characters | low |

---

## User Registration

Total: **16** (positive: 1, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful registration with valid details | User logged in as <New User> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Password> in the Password field<br>5. Enter <Password> in the Confirm Password field<br>6. Enter <Mobile Number> in the Mobile Number field<br>7. Select <Country Code> from the Country Code dropdown<br>8. Click the Terms and Conditions checkbox<br>9. Click Submit | creates account and redirects to dashboard or prompts for email verification | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave First Name blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave Last Name blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave Email blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave Password blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Leave Confirm Password blank and submit |  | 1. Leave the Confirm_Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-007 |  | Leave Mobile Number blank and submit |  | 1. Leave the Mobile_Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mobile_Number field indicating it is required | high |
| TC-008 |  | Enter invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating 'Must be a valid email format' | medium |
| TC-009 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Confirm_Password field indicating 'must match Password' | medium |
| TC-010 |  | Leave Terms and Conditions unchecked and submit |  | 1. Leave the Terms_and_Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Terms_and_Conditions field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Test email format with a valid email address |  | 1. Enter a valid email format in the Email field | Form submits successfully; account is created and user is redirected to the dashboard | medium |
| TC-012 (boundary) |  | Test email format with an invalid email address |  | 1. Enter an invalid email format in the Email field | Email field displays an error indicating the value is not a valid email format | medium |
| TC-013 (boundary) |  | Test password confirmation with matching passwords |  | 1. Enter a valid password in the Password field<br>2. Enter the same password in the Confirm Password field | Form submits successfully; account is created and user is redirected to the dashboard | medium |
| TC-014 (boundary) |  | Test password confirmation with non-matching passwords |  | 1. Enter a valid password in the Password field<br>2. Enter a different password in the Confirm Password field | Confirm Password field displays an error indicating the passwords do not match | medium |
| TC-015 (input_edge) |  | Test first name with leading and trailing whitespace |  | 1. Enter '  John  ' in the First Name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-016 (input_edge) |  | Test last name with special characters |  | 1. Enter 'Doe@123' in the Last Name field | Last Name field displays an error indicating the value contains invalid characters | low |

---

## User Login

Total: **13** (positive: 3, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <User>, Social login is not enabled | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to dashboard or previous page | high |
| TC-002 |  | Successful login with Remember Me checked | User logged in as <User>, Social login is not enabled | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Check the Remember Me checkbox<br>4. Click Login | redirects to dashboard or previous page | medium |
| TC-003 |  | Display of social login options when enabled | User logged in as <User>, Social login is enabled | 1. Open the login page | Google and Facebook login options are visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Fill the Email field with a valid email<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill the Password field with a valid password<br>3. Click Login | Error message is shown indicating invalid email format; Password field is cleared | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Fill the Email field with a valid email<br>2. Fill the Password field with an incorrect password<br>3. Click Login | Error message is shown; Password field is cleared | high |
| TC-008 |  | Attempt to login after multiple failed attempts without CAPTCHA |  | 1. Fill the Email field with a valid email<br>2. Fill the Password field with an incorrect password<br>3. Click Login<br>4. Repeat steps 1-3 multiple times | CAPTCHA verification is not required yet; Error message is shown | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Enter valid email format at the boundary |  | 1. Enter a valid email address in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Redirects to dashboard or previous page | medium |
| TC-010 (boundary) |  | Enter invalid email format just below valid |  | 1. Enter an invalid email address (missing '@') in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Shows error message and clears password field | medium |
| TC-011 (input_edge) |  | Enter long email address |  | 1. Enter a long email address (over 254 characters) in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Shows error message indicating invalid email format | low |
| TC-012 (input_edge) |  | Enter password with leading and trailing whitespace |  | 1. Enter '   validPassword   ' in the Password field<br>2. Enter a valid email address in the Email field<br>3. Click Login | Password field displays trimmed value; redirects to dashboard | low |
| TC-013 (interaction_edge) |  | Rapid consecutive login attempts |  | 1. Enter valid email and password<br>2. Click Login<br>3. Enter invalid email and password<br>4. Click Login<br>5. Enter valid email and password again quickly<br>6. Click Login | Shows error message for invalid credentials; password field is cleared | medium |

---

## Forgot Password

Total: **13** (positive: 2, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User requests password reset with existing email | User logged in as <User>, Email exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is shown stating 'sends reset link to email' | high |
| TC-002 |  | User resets password successfully | User clicked the reset link from email, User is on the Password Reset Page | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | Redirects to login page with a success message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Submit with an email that does not exist in the system |  | 1. Enter <nonexistent email> in the Email field<br>2. Click Reset Password | Error is shown indicating 'Email not found'; form remains editable | high |
| TC-005 |  | Leave the New Password field blank and submit |  | 1. Enter <valid email> and submit to receive reset link<br>2. Click the reset link in the email<br>3. Leave the New Password field blank<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-006 |  | Leave the Confirm Password field blank and submit |  | 1. Enter <valid email> and submit to receive reset link<br>2. Click the reset link in the email<br>3. Enter <valid password> in the New Password field<br>4. Leave the Confirm Password field blank<br>5. Click Change Password | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-007 |  | Enter mismatched passwords in New Password and Confirm Password fields |  | 1. Enter <valid email> and submit to receive reset link<br>2. Click the reset link in the email<br>3. Enter <valid password> in the New Password field<br>4. Enter <different password> in the Confirm Password field<br>5. Click Change Password | Error is shown indicating 'Passwords do not match'; form remains editable | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Submit with a valid email format that exists in the system | Email exists in the system | 1. Enter a valid email address in the Email field<br>2. Click Reset Password | Reset link is sent to the email; confirmation message is shown | medium |
| TC-009 (boundary) |  | Submit with an invalid email format |  | 1. Enter an invalid email format in the Email field<br>2. Click Reset Password | Error message is shown indicating the email format is invalid; form remains editable | medium |
| TC-010 (input_edge) |  | Enter a very long email address |  | 1. Enter a long email address (over 254 characters) in the Email field<br>2. Click Reset Password | Error message is shown indicating the email is too long; form remains editable | low |
| TC-011 (input_edge) |  | Enter an email address with leading and trailing whitespace |  | 1. Enter '   user@example.com   ' in the Email field<br>2. Click Reset Password | Leading and trailing whitespace is trimmed; reset link is sent to 'user@example.com' | low |
| TC-012 (boundary) |  | Submit with a valid email that does not exist in the system | Email does not exist in the system | 1. Enter a non-existing email address in the Email field<br>2. Click Reset Password | Error message is shown indicating the email was not found; form remains editable | medium |
| TC-013 (boundary) |  | Submit with a valid email format that exists in the system after 24 hours | Email exists in the system and reset link has expired | 1. Enter a valid email address in the Email field<br>2. Click Reset Password | Error message is shown indicating the reset link has expired; form remains editable | medium |

---

## Hotels Search & Listing

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for hotels with valid input | User logged in as <User> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <valid number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' to add guest count<br>6. Enter <valid number of adults> in the Adults field<br>7. Enter <valid number of children> in the Children field<br>8. Click Search | User is redirected to the listing page | high |
| TC-002 |  | Book a hotel from the listing | User logged in as <User>, User is on the listing page | 1. Click Book Now on the first hotel card | User is redirected to the booking page for the selected hotel | medium |
| TC-003 |  | Reset all filters | User logged in as <User>, User has applied filters on the listing page | 1. Click Reset all on the filters sidebar | All filters are cleared and the full list of hotels is displayed | medium |
| TC-004 |  | Sort hotels by price low to high | User logged in as <User>, User is on the listing page | 1. Select 'Price: Low to High' from the Sorting Options dropdown | Hotels are sorted by price from low to high | medium |
| TC-005 |  | Sort hotels by guest rating | User logged in as <User>, User is on the listing page | 1. Select 'Guest Rating' from the Sorting Options dropdown | Hotels are sorted by guest rating | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid values<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-007 |  | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid values<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-008 |  | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count fields with valid values<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-009 |  | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count fields with valid values<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-010 |  | Leave the Adults field blank in Guest_Count and submit |  | 1. Leave the Adults field blank in Guest_Count<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms fields with valid values<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields (Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, Adults) empty<br>2. Click Search | Form does not submit; error shown on Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Check-In Date equals Check-Out Date | User is on the Hotels Search Form | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-013 (boundary) |  | Check-Out Date is one day before Check-In Date | User is on the Hotels Search Form | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter yesterday's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form is blocked; error shown indicating that Check-Out Date must be after Check-In Date | medium |
| TC-014 (boundary) |  | Number of Rooms at minimum value | User is on the Hotels Search Form | 1. Enter a valid destination in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter 1 in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-015 (boundary) |  | Number of Rooms exceeds maximum allowed | User is on the Hotels Search Form | 1. Enter a valid destination in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter a number greater than the maximum allowed in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form is blocked; error shown indicating that the number of rooms exceeds the maximum allowed | medium |
| TC-016 (input_edge) |  | Leading/trailing whitespace in Destination field | User is on the Hotels Search Form | 1. Enter '  New York  ' in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Leading/trailing whitespace is trimmed; user is redirected to the listing page with 'New York' as the destination | low |
| TC-017 (input_edge) |  | Special characters in Destination field | User is on the Hotels Search Form | 1. Enter '@#$%^&*()' in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Form is blocked; error shown indicating that the destination is invalid | low |

---

## Hotel Details & Booking

Total: **14** (positive: 1, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful hotel booking | User logged in as <Guest>, Selected hotel and room type are visible, Stay dates are selected, Guest count is specified | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <valid phone number> in the Phone Number field<br>5. Click 'Book Now' | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Selected Hotel field blank |  | 1. Leave the Selected Hotel field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Selected Hotel field indicating it is required | high |
| TC-003 |  | Leave the Room Type field blank |  | 1. Leave the Room Type field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Room Type field indicating it is required | high |
| TC-004 |  | Leave the Stay Dates field blank |  | 1. Leave the Stay Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay Dates field indicating it is required | high |
| TC-005 |  | Leave the Guest Count field blank |  | 1. Leave the Guest Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest Count field indicating it is required | high |
| TC-006 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First Name field indicating it is required | high |
| TC-007 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-008 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-010 |  | Attempt to book without being logged in |  | 1. Ensure user is logged out<br>2. Fill all required fields<br>3. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Enter exactly 1 in the Guest Count field | User is logged in, Room type and stay dates are selected | 1. Enter 1 in the Guest Count field<br>2. Fill in all other required fields<br>3. Click Book Now | Form submits successfully; user is redirected to the payment page | medium |
| TC-012 (boundary) |  | Enter 0 in the Guest Count field | User is logged in, Room type and stay dates are selected | 1. Enter 0 in the Guest Count field<br>2. Fill in all other required fields<br>3. Click Book Now | Submission is blocked; an error message displays indicating that the guest count must be greater than 0 | medium |
| TC-013 (input_edge) |  | Enter a very long string in the First Name field | User is logged in, Room type and stay dates are selected | 1. Enter a string of 200 characters in the First Name field<br>2. Fill in all other required fields<br>3. Click Book Now | Form submission is blocked; an error message displays indicating the name is too long | low |
| TC-014 (input_edge) |  | Enter a special character in the Last Name field | User is logged in, Room type and stay dates are selected | 1. Enter '@#$%' in the Last Name field<br>2. Fill in all other required fields<br>3. Click Book Now | Submission is blocked; an error message displays indicating invalid characters in the name field | low |

---

## Flights Search & Listing

Total: **17** (positive: 2, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for flights with valid inputs | User logged in as <Traveler> | 1. Enter 'New York' in the Departure City field<br>2. Enter 'Los Angeles' in the Arrival City field<br>3. Select 'Round-trip' from the Trip Type dropdown<br>4. Enter a valid date in the Travel Dates field<br>5. Enter '2' in the Adults field under Passenger Count<br>6. Select 'Economy' from the Cabin Class dropdown<br>7. Click the Search Flights button | User is redirected to the listing page | high |
| TC-002 |  | Select a flight from the listing | User logged in as <Traveler>, User is on the flights listing page | 1. Click the Select button on the desired flight | Flight is selected | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Trip Type dropdown blank and submit |  | 1. Leave the Trip Type field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Trip Type field indicating it is required | high |
| TC-004 |  | Leave the Departure City blank and submit |  | 1. Leave the Departure City field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-005 |  | Leave the Arrival City blank and submit |  | 1. Leave the Arrival City field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Arrival City field indicating it is required | high |
| TC-006 |  | Leave the Travel Dates field blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-007 |  | Leave the Adults field blank and submit |  | 1. Leave the Adults field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Adults field indicating it is required | high |
| TC-008 |  | Leave the Cabin Class dropdown blank and submit |  | 1. Leave the Cabin Class field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Cabin Class field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search Flights | Inline validation errors appear on the Trip Type, Departure City, Arrival City, Travel Dates, Adults, and Cabin Class fields indicating they are required | high |
| TC-010 |  | Enter a non-numeric value in the Adults field and submit |  | 1. Enter <non-numeric value> in the Adults field<br>2. Fill all other required fields with valid data<br>3. Click Search Flights | Inline validation error appears on the Adults field indicating it must be a number | medium |
| TC-011 |  | Enter an invalid date in the Travel Dates field and submit |  | 1. Enter <invalid date> in the Travel Dates field<br>2. Fill all other required fields with valid data<br>3. Click Search Flights | Inline validation error appears on the Travel Dates field indicating it must be a valid date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Enter minimum passenger count for adults | User is on the Flights Search Form | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter '1' in the Adults field under Passenger_Count<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submits successfully; user is redirected to the listing page | medium |
| TC-013 (boundary) |  | Enter one unit below minimum passenger count for adults | User is on the Flights Search Form | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter '0' in the Adults field under Passenger_Count<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submission is blocked; inline error shown indicating 'At least 1 adult is required' | medium |
| TC-014 (boundary) |  | Enter maximum number of passengers | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter 'Chicago' in the Departure_City field<br>3. Enter 'Miami' in the Arrival_City field<br>4. Enter a future date in the Travel_Dates field<br>5. Enter '9' in the Adults field under Passenger_Count<br>6. Select 'Business' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submits successfully; user is redirected to the listing page | medium |
| TC-015 (boundary) |  | Enter one unit over maximum number of passengers | User is on the Flights Search Form | 1. Select 'Multi-city' from the Trip_Type dropdown<br>2. Enter 'San Francisco' in the Departure_City field<br>3. Enter 'Seattle' in the Arrival_City field<br>4. Enter a future date in the Travel_Dates field<br>5. Enter '10' in the Adults field under Passenger_Count<br>6. Select 'Premium Economy' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submission is blocked; inline error shown indicating 'Maximum of 9 passengers allowed' | medium |
| TC-016 (input_edge) |  | Enter a long string in the Departure_City field | User is on the Flights Search Form | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a long string of 200 characters in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter '1' in the Adults field under Passenger_Count<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submission is blocked; inline error shown indicating 'Invalid city name' | low |
| TC-017 (input_edge) |  | Enter special characters in the Arrival_City field | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter '@#$%' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter '1' in the Adults field under Passenger_Count<br>6. Select 'Business' from the Cabin_Class dropdown<br>7. Click Search Flights | Form submission is blocked; inline error shown indicating 'Invalid city name' | low |

---

## Flight Booking

Total: **18** (positive: 2, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit booking form with valid traveler details | User logged in as <Traveler>, All required fields are visible | 1. Click 'Add Row' to add a traveler<br>2. Select 'Mr' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid passport expiry date> in the Passport Expiry field<br>8. Enter <valid email> in the Lead Passenger Email field<br>9. Enter <valid phone number> in the Lead Passenger Phone field<br>10. Click Continue_Button | User is redirected to the payment page | high |
| TC-002 |  | Submit booking form with multiple travelers | User logged in as <Traveler>, All required fields are visible | 1. Click 'Add Row' to add a traveler<br>2. Select 'Mrs' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid passport expiry date> in the Passport Expiry field<br>8. Click 'Add Row' to add another traveler<br>9. Select 'Dr' from the Title dropdown<br>10. Enter <valid first name> in the First Name field<br>11. Enter <valid last name> in the Last Name field<br>12. Enter <valid date of birth> in the Date of Birth field<br>13. Enter <valid passport number> in the Passport Number field<br>14. Enter <valid passport expiry date> in the Passport Expiry field<br>15. Enter <valid email> in the Lead Passenger Email field<br>16. Enter <valid phone number> in the Lead Passenger Phone field<br>17. Click Continue_Button | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank |  | 1. Open the flight booking form<br>2. Leave the First_Name field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank |  | 1. Open the flight booking form<br>2. Leave the Last_Name field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Date of Birth field blank |  | 1. Open the flight booking form<br>2. Leave the Date_of_Birth field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Date_of_Birth field indicating it is required | high |
| TC-006 |  | Leave the Passport Number field blank |  | 1. Open the flight booking form<br>2. Leave the Passport_Number field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Passport_Number field indicating it is required | high |
| TC-007 |  | Leave the Passport Expiry field blank |  | 1. Open the flight booking form<br>2. Leave the Passport_Expiry field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Passport_Expiry field indicating it is required | high |
| TC-008 |  | Leave the Lead Passenger Email field blank |  | 1. Open the flight booking form<br>2. Leave the Lead_Passenger_Email field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Lead_Passenger_Email field indicating it is required | high |
| TC-009 |  | Leave the Lead Passenger Phone field blank |  | 1. Open the flight booking form<br>2. Leave the Lead_Passenger_Phone field blank<br>3. Fill all other required fields<br>4. Click Continue | Inline validation error appears on the Lead_Passenger_Phone field indicating it is required | high |
| TC-010 |  | Submit with all required fields empty |  | 1. Open the flight booking form<br>2. Leave all required fields empty<br>3. Click Continue | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Add maximum allowed entries to the Travelers group |  | 1. Add 10 entries to the Travelers group | Form submits successfully; 10 entries are displayed in the Travelers group | medium |
| TC-012 (boundary) |  | Attempt to add one more entry beyond the maximum allowed in the Travelers group |  | 1. Add 10 entries to the Travelers group<br>2. Attempt to add an 11th entry | Adding the 11th entry is blocked; an inline error is displayed indicating the maximum limit has been reached | medium |
| TC-013 (boundary) |  | Enter today's date in the Date of Birth field |  | 1. Enter today's date in the Date of Birth field | Form submits successfully; today's date is accepted | medium |
| TC-014 (boundary) |  | Enter a date in the Passport Expiry field that is one day before today's date |  | 1. Enter yesterday's date in the Passport Expiry field | Form submission is blocked; an inline error is displayed indicating the passport expiry date must be in the future | medium |
| TC-015 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string longer than 200 characters in the First Name field | An inline error is displayed indicating the input exceeds the maximum length | low |
| TC-016 (input_edge) |  | Enter a special character in the Last Name field |  | 1. Enter '@#$%' in the Last Name field | An inline error is displayed indicating invalid characters in the Last Name field | low |
| TC-017 (input_edge) |  | Enter a value with leading and trailing whitespace in the Lead Passenger Email field |  | 1. Enter '   example@example.com   ' in the Lead Passenger Email field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-018 (interaction_edge) |  | Rapid re-submission after redirect to payment page |  | 1. Complete the booking form with valid data<br>2. Click Continue<br>3. Press the browser back button | The booking form is shown blank; no pre-filled data is displayed | low |

---

## Tours Search & Listing

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for tours with valid inputs | User logged in as <User> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select <Tour_Type> from the Tour Type dropdown<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid budget range> in the Budget Range field<br>6. Click Search | User is redirected to the listing page | high |
| TC-002 |  | Search for tours without selecting Tour Type and Budget Range | User logged in as <User> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Leave Tour Type dropdown unselected<br>4. Enter <valid duration> in the Duration field<br>5. Leave Budget Range field empty<br>6. Click Search | User is redirected to the listing page | medium |
| TC-003 |  | Filter tours by Destination in the listing | User logged in as <User>, User is on the tours listing page | 1. Enter <valid destination> in the sidebar Destination filter<br>2. Click Apply Filters | Only tours matching <valid destination> are displayed; unrelated tours are no longer visible | medium |
| TC-004 |  | Sort tours by Price in the listing | User logged in as <User>, User is on the tours listing page | 1. Click on the Price column header to sort | Tours are sorted by price in ascending order | medium |
| TC-005 |  | View details of a tour from the listing | User logged in as <User>, User is on the tours listing page | 1. Click View on a tour card | User is redirected to the tour detail page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill in the Travel Dates, Duration fields with valid values<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-007 |  | Leave the Travel Dates field blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill in the Destination, Duration fields with valid values<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-008 |  | Leave the Duration field blank and submit |  | 1. Leave the Duration field blank<br>2. Fill in the Destination, Travel Dates fields with valid values<br>3. Click Search | Inline validation error appears on the Duration field indicating it is required | high |
| TC-009 |  | Submit the form with all required fields empty |  | 1. Leave the Destination, Travel Dates, Duration fields blank<br>2. Click Search | Form does not submit; error shown on Destination, Travel Dates, and Duration fields indicating they are required | high |
| TC-010 |  | Enter an invalid date in the Travel Dates field |  | 1. Enter <invalid date format> in the Travel Dates field<br>2. Fill in the Destination, Duration fields with valid values<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it must be a valid date | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Enter today's date in the Travel Dates field |  | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Travel Dates field<br>3. Fill in the Duration field<br>4. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-012 (boundary) |  | Enter a date one day before today in the Travel Dates field |  | 1. Enter a valid destination in the Destination field<br>2. Enter a date one day before today in the Travel Dates field<br>3. Fill in the Duration field<br>4. Click Search | Form submission is blocked; an error message is displayed indicating travel dates must be today or later | medium |
| TC-013 (input_edge) |  | Enter a very long string in the Destination field |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Fill in the Travel Dates field<br>3. Fill in the Duration field<br>4. Click Search | Form submission is blocked; an error message is displayed indicating the destination is too long | low |
| TC-014 (input_edge) |  | Enter special characters in the Destination field |  | 1. Enter special characters (e.g., @#$%^&) in the Destination field<br>2. Fill in the Travel Dates field<br>3. Fill in the Duration field<br>4. Click Search | Form submission is blocked; an error message is displayed indicating invalid characters in the destination | low |

---

## Tour Details & Booking

Total: **12** (positive: 1, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful booking with valid details | User logged in as <User> | 1. Select a valid <Departure Date><br>2. Click 'Add Row' to specify number of travelers<br>3. Enter <number of adults> in the Adults field<br>4. Enter <number of children> in the Children field<br>5. Click 'Add Row' to enter traveler details<br>6. Enter <valid traveler name> in the Name field<br>7. Enter <valid contact details> in the Contact Details field<br>8. Click 'Book Now' | redirects to booking confirmation | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Departure Date blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Fill in all other required fields<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-003 |  | Leave the Adults field blank and submit |  | 1. Fill in the Number_of_Travelers with at least one group<br>2. Leave the Adults field blank<br>3. Fill in the Children field<br>4. Click Book Now | Inline validation error appears on the Adults field indicating it is required | high |
| TC-004 |  | Leave the Children field blank and submit |  | 1. Fill in the Number_of_Travelers with at least one group<br>2. Fill in the Adults field<br>3. Leave the Children field blank<br>4. Click Book Now | Inline validation error appears on the Children field indicating it is required | high |
| TC-005 |  | Leave the Name field blank and submit |  | 1. Fill in the Number_of_Travelers with at least one group<br>2. Leave the Name field blank in Traveler_Details<br>3. Fill in the Contact_Details field<br>4. Click Book Now | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Leave the Contact Details field blank and submit |  | 1. Fill in the Number_of_Travelers with at least one group<br>2. Fill in the Name field<br>3. Leave the Contact_Details field blank<br>4. Click Book Now | Inline validation error appears on the Contact_Details field indicating it is required | high |
| TC-007 |  | Attempt to book without being logged in |  | 1. Fill in all required fields<br>2. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Add maximum number of travelers | User is logged in | 1. Navigate to the tour booking form<br>2. Select a departure date<br>3. Add maximum allowed entries in the Number of Travelers repeating group | Form submits successfully; total cost breakdown is displayed | medium |
| TC-009 (boundary) |  | Attempt to add one more traveler than allowed | User is logged in | 1. Navigate to the tour booking form<br>2. Select a departure date<br>3. Add maximum allowed entries in the Number of Travelers repeating group<br>4. Attempt to add one more entry | Adding another entry is blocked; an error message is displayed | medium |
| TC-010 (input_edge) |  | Enter long name in Traveler Details | User is logged in | 1. Navigate to the tour booking form<br>2. Select a departure date<br>3. Add a traveler<br>4. Enter a very long name in the Name field | Name field accepts the long input or shows a truncation indicator | low |
| TC-011 (input_edge) |  | Enter special characters in Contact Details | User is logged in | 1. Navigate to the tour booking form<br>2. Select a departure date<br>3. Add a traveler<br>4. Enter special characters in the Contact Details field | Contact Details field accepts the special characters or shows an error message | low |
| TC-012 (interaction_edge) |  | Rapid re-submission after booking | User is logged in | 1. Complete the tour booking form and click Book Now<br>2. After redirection to the booking confirmation page, press the browser back button | The booking form is shown blank; no duplicate booking is created | medium |

---

## Cars Search & Listing

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for available cars | User logged in as <Customer> | 1. Enter <valid pick-up location> in the Pick Up Location field<br>2. Enter <valid drop-off location> in the Drop Off Location field<br>3. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>4. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>5. Enter <valid driver age> in the Driver Age field<br>6. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-001 | Filter car listings by car type | User logged in as <Customer>, User is on the listing page | 1. Select 'SUV' from the Car Type dropdown<br>2. Observe the vehicle listings | Only SUV listings are displayed; other types are no longer visible | medium |
| TC-003 | WF-001 | Filter car listings by transmission type | User logged in as <Customer>, User is on the listing page | 1. Select 'Automatic' from the Transmission dropdown<br>2. Observe the vehicle listings | Only vehicles with Automatic transmission are displayed; others are no longer visible | medium |
| TC-004 | WF-001 | Filter car listings by fuel policy | User logged in as <Customer>, User is on the listing page | 1. Select 'Full to Full' from the Fuel Policy dropdown<br>2. Observe the vehicle listings | Only vehicles with Full to Full fuel policy are displayed; others are no longer visible | medium |
| TC-005 | WF-001 | Book a vehicle from the listing | User logged in as <Customer>, User is on the listing page | 1. Click the Book Now button on a vehicle listing | User is redirected to the booking page for the selected vehicle | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Pick-Up Location blank and submit |  | 1. Leave the Pick_Up_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-007 |  | Leave the Drop-Off Location blank and submit |  | 1. Leave the Drop_Off_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-008 |  | Leave the Pick-Up Date Time blank and submit |  | 1. Leave the Pick_Up_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-009 |  | Leave the Drop-Off Date Time blank and submit |  | 1. Leave the Drop_Off_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |
| TC-010 |  | Leave the Driver Age blank and submit |  | 1. Leave the Driver_Age field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Driver_Age field indicating it is required | high |
| TC-011 |  | Submit the search form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Form does not submit; error shown on all required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Pick Up Date Time is exactly today |  | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter a valid future date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Redirects to listing page with valid search results | medium |
| TC-013 (boundary) |  | Drop Off Date Time is exactly the same as Pick Up Date Time |  | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter today's date and time in the Pick Up Date Time field<br>4. Enter the same date and time in the Drop Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Redirects to listing page with valid search results | medium |
| TC-014 (boundary) |  | Driver Age is exactly 18 |  | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter a valid Pick Up Date Time<br>4. Enter a valid Drop Off Date Time<br>5. Enter 18 in the Driver Age field<br>6. Click Search | Redirects to listing page with valid search results | medium |
| TC-015 (boundary) |  | Driver Age is one unit below minimum age (17) |  | 1. Enter a valid Pick Up Location<br>2. Enter a valid Drop Off Location<br>3. Enter a valid Pick Up Date Time<br>4. Enter a valid Drop Off Date Time<br>5. Enter 17 in the Driver Age field<br>6. Click Search | Form submission is blocked; error message displayed indicating minimum age requirement | medium |
| TC-016 (input_edge) |  | Enter a very long string in the Pick Up Location field |  | 1. Enter a string of 200+ characters in the Pick Up Location field<br>2. Enter a valid Drop Off Location<br>3. Enter a valid Pick Up Date Time<br>4. Enter a valid Drop Off Date Time<br>5. Enter a valid Driver Age<br>6. Click Search | Form submission is blocked; error message displayed indicating input length exceeded | low |
| TC-017 (input_edge) |  | Enter special characters in the Drop Off Location field |  | 1. Enter special characters in the Drop Off Location field<br>2. Enter a valid Pick Up Location<br>3. Enter a valid Pick Up Date Time<br>4. Enter a valid Drop Off Date Time<br>5. Enter a valid Driver Age<br>6. Click Search | Form submission is blocked; error message displayed indicating invalid characters | low |

---

## Car Booking

Total: **16** (positive: 1, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit booking form with valid details | User logged in as <Customer> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click 'Add Row' to add optional add-ons<br>8. Check the GPS checkbox<br>9. Select <valid insurance plan> from the Insurance Plan dropdown<br>10. Check the Terms Acceptance checkbox<br>11. Click Confirm Booking | Page shows 'proceeds to payment' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Driver Full Name field blank and submit |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 |  | Leave the Age field blank and submit |  | 1. Leave the Age field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-004 |  | Leave the License Number field blank and submit |  | 1. Leave the License Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-005 |  | Leave the License Issue Country field blank and submit |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-006 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-008 |  | Leave the Insurance Plan field unselected and submit |  | 1. Leave the Insurance Plan field unselected<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating it is required | high |
| TC-009 |  | Leave the Terms Acceptance checkbox unchecked and submit |  | 1. Leave the Terms Acceptance checkbox unchecked<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Terms Acceptance field indicating it is required | high |
| TC-010 |  | Submit the form with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Confirm Booking | Inline validation errors appear on all required fields indicating they are required; form does not submit | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Age field boundary test |  | 1. Enter exactly 18 in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; user is directed to payment | medium |
| TC-012 (boundary) |  | Age field below minimum boundary test |  | 1. Enter 17 in the Age field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Age field displays an error indicating the value is below the minimum allowed | medium |
| TC-013 (boundary) |  | Add-Ons repeating group maximum entries test |  | 1. Add exactly 3 entries in the Add-Ons section<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; user is directed to payment | medium |
| TC-014 (boundary) |  | Add-Ons repeating group exceeding maximum entries test |  | 1. Add 4 entries in the Add-Ons section<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submission is blocked; inline error indicates maximum entries exceeded | medium |
| TC-015 (input_edge) |  | Long text in Driver Full Name field |  | 1. Enter a string of 200+ characters in the Driver Full Name field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submission is blocked; inline error indicates the name is too long | low |
| TC-016 (input_edge) |  | Leading/trailing whitespace in Email field |  | 1. Enter '   user@example.com   ' in the Email field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Visa Services

Total: **15** (positive: 3, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View visa requirements for selected nationality and destination country | User logged in as <User> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown | Visa requirements for <valid nationality> to <valid destination country> are displayed, including visa type, processing time, required documents, and fees. | high |
| TC-002 |  | Submit visa application form with valid details | User logged in as <User> | 1. Navigate to the Visa Application Form<br>2. Enter <full name> in the Full Name field<br>3. Enter <passport number> in the Passport Number field<br>4. Enter <passport expiry date> in the Passport Expiry Date field<br>5. Enter <date of birth> in the Date of Birth field<br>6. Select <valid nationality> in the Nationality field<br>7. Enter <valid email> in the Email field<br>8. Enter <valid phone number> in the Phone field<br>9. Enter <purpose of visit> in the Purpose of Visit field<br>10. Enter <intended travel dates> in the Intended Travel Dates field<br>11. Enter <duration of stay> in the Duration of Stay field<br>12. Upload a <valid file type> in the Document Upload section | A success notification is displayed; the application is submitted successfully. | high |
| TC-003 |  | Track application status | User logged in as <User>, Application has been submitted | 1. Click on the 'Track Application Status' link | redirects to bookings section of the dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Select a valid Destination Country<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-005 |  | Leave the Destination Country dropdown blank and submit |  | 1. Select a valid Nationality<br>2. Leave the Destination Country dropdown blank<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-006 |  | Leave all required fields in the Personal Information section blank and submit |  | 1. Leave Full Name blank<br>2. Leave Passport Number blank<br>3. Leave Passport Expiry Date blank<br>4. Leave Date of Birth blank<br>5. Leave Nationality blank<br>6. Leave Email blank<br>7. Leave Phone blank<br>8. Click Submit | Form does not submit; errors shown on Full Name, Passport Number, Passport Expiry Date, Date of Birth, Nationality, Email, and Phone fields indicating they are required | high |
| TC-007 |  | Leave all required fields in the Travel Details section blank and submit |  | 1. Leave Purpose of Visit blank<br>2. Leave Intended Travel Dates blank<br>3. Leave Duration of Stay blank<br>4. Click Submit | Form does not submit; errors shown on Purpose of Visit, Intended Travel Dates, and Duration of Stay fields indicating they are required | high |
| TC-008 |  | Leave the Document Upload section blank and submit |  | 1. Fill all other required fields<br>2. Leave Document Upload section blank<br>3. Click Submit | Form does not submit; inline validation error appears on the Document Upload field indicating it is required | high |
| TC-009 |  | Attempt to track application status without being logged in |  | 1. Click on Track Application Status link | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Passport expiry date is today | User is on the Visa Application Form | 1. Enter a valid full name in the Full_Name field<br>2. Enter a valid passport number in the Passport_Number field<br>3. Enter today's date in the Passport_Expiry_Date field<br>4. Enter a valid date of birth in the Date_of_Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose_of_Visit field<br>9. Enter a valid intended travel date in the Intended_Travel_Dates field<br>10. Enter a valid duration of stay in the Duration_of_Stay field<br>11. Upload a valid document in the Document_Upload section<br>12. Click Submit | Form submits successfully; application is created with today's date as the passport expiry date | medium |
| TC-011 (boundary) |  | Passport expiry date is one day past today | User is on the Visa Application Form | 1. Enter a valid full name in the Full_Name field<br>2. Enter a valid passport number in the Passport_Number field<br>3. Enter tomorrow's date in the Passport_Expiry_Date field<br>4. Enter a valid date of birth in the Date_of_Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose_of_Visit field<br>9. Enter a valid intended travel date in the Intended_Travel_Dates field<br>10. Enter a valid duration of stay in the Duration_of_Stay field<br>11. Upload a valid document in the Document_Upload section<br>12. Click Submit | Form is blocked; error shown indicating that the passport expiry date must be today or earlier | medium |
| TC-012 (boundary) |  | Intended travel date is today | User is on the Visa Application Form | 1. Enter a valid full name in the Full_Name field<br>2. Enter a valid passport number in the Passport_Number field<br>3. Enter a valid passport expiry date in the Passport_Expiry_Date field<br>4. Enter a valid date of birth in the Date_of_Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose_of_Visit field<br>9. Enter today's date in the Intended_Travel_Dates field<br>10. Enter a valid duration of stay in the Duration_of_Stay field<br>11. Upload a valid document in the Document_Upload section<br>12. Click Submit | Form submits successfully; application is created with today's date as the intended travel date | medium |
| TC-013 (boundary) |  | Intended travel date is one day in the past | User is on the Visa Application Form | 1. Enter a valid full name in the Full_Name field<br>2. Enter a valid passport number in the Passport_Number field<br>3. Enter a valid passport expiry date in the Passport_Expiry_Date field<br>4. Enter a valid date of birth in the Date_of_Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a valid email in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose_of_Visit field<br>9. Enter yesterday's date in the Intended_Travel_Dates field<br>10. Enter a valid duration of stay in the Duration_of_Stay field<br>11. Upload a valid document in the Document_Upload section<br>12. Click Submit | Form is blocked; error shown indicating that the intended travel date must be today or a future date | medium |
| TC-014 (input_edge) |  | Enter a very long name in the Full_Name field | User is on the Visa Application Form | 1. Enter a string of 200 characters in the Full_Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; saved value shown in detail page has the long name correctly displayed | low |
| TC-015 (input_edge) |  | Enter special characters in the Email field | User is on the Visa Application Form | 1. Enter a valid full name in the Full_Name field<br>2. Enter a valid passport number in the Passport_Number field<br>3. Enter a valid passport expiry date in the Passport_Expiry_Date field<br>4. Enter a valid date of birth in the Date_of_Birth field<br>5. Enter a valid nationality in the Nationality field<br>6. Enter a string with special characters in the Email field<br>7. Enter a valid phone number in the Phone field<br>8. Enter a valid purpose of visit in the Purpose_of_Visit field<br>9. Enter a valid intended travel date in the Intended_Travel_Dates field<br>10. Enter a valid duration of stay in the Duration_of_Stay field<br>11. Upload a valid document in the Document_Upload section<br>12. Click Submit | Form is blocked; error shown indicating that the email format is invalid | low |

---

## User Dashboard

Total: **33** (positive: 14, negative: 14, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View Booking Details | User logged in as <User>, User has at least one booking | 1. Click 'View Details' on a booking row | Booking details are displayed for the selected booking | high |
| TC-002 |  | Cancel Booking | User logged in as <User>, User has a booking where booking type and cancellation policy permit | 1. Click 'Cancel' on a booking row<br>2. Confirm cancellation | The booking is no longer visible in the My Bookings table | high |
| TC-003 |  | Modify Booking | User logged in as <User>, User has a booking where booking type and cancellation policy permit | 1. Click 'Modify' on a booking row<br>2. Make changes to the booking<br>3. Submit the changes | The modified booking details are updated and displayed in the My Bookings table | high |
| TC-004 |  | Download Confirmations | User logged in as <User>, User has bookings | 1. Select bookings<br>2. Click 'Download Confirmations' | Confirmation files are downloaded to the user's device | medium |
| TC-005 |  | Download Invoices | User logged in as <User>, User has bookings | 1. Select bookings<br>2. Click 'Download Invoices' | Invoice files are downloaded to the user's device | medium |
| TC-006 |  | Download Vouchers | User logged in as <User>, User has bookings | 1. Select bookings<br>2. Click 'Download Vouchers' | Voucher files are downloaded to the user's device | medium |
| TC-007 |  | Edit Profile | User logged in as <User> | 1. Click 'Edit' in My Profile section<br>2. Update profile information<br>3. Save changes | Profile information is updated and displayed correctly in My Profile section | medium |
| TC-008 |  | Add Item to Wishlist | User logged in as <User> | 1. Click 'Add Row' in Wishlist<br>2. Enter <Type> and <Details><br>3. Save the item | New item appears in the Wishlist with the entered Type and Details | medium |
| TC-009 |  | Submit Review | User logged in as <User>, User has completed a booking | 1. Click 'Add Row' in Reviews<br>2. Enter <Rating> and <Review><br>3. Submit the review | New review appears in the Reviews section with the entered Rating and Review | medium |
| TC-010 |  | Change Password | User logged in as <User> | 1. Enter new password in Change Password field<br>2. Confirm new password<br>3. Save changes | Password is changed successfully and a confirmation message is displayed | medium |
| TC-011 |  | Set Notification Preferences | User logged in as <User> | 1. Update Notification Preferences<br>2. Save changes | Notification preferences are updated successfully | medium |
| TC-012 |  | Set Default Currency | User logged in as <User> | 1. Select <Default Currency> from the dropdown<br>2. Save changes | Default currency is updated successfully and displayed correctly | medium |
| TC-013 |  | Set Default Language | User logged in as <User> | 1. Select <Default Language> from the dropdown<br>2. Save changes | Default language is updated successfully and displayed correctly | medium |
| TC-014 |  | Logout | User logged in as <User> | 1. Click 'Logout' button | User is redirected to the login page and a session end confirmation is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Leave Booking Reference blank and submit |  | 1. Leave the Booking Reference field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Booking Reference field indicating it is required | high |
| TC-016 |  | Leave Service Type blank and submit |  | 1. Leave the Service Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Service Type field indicating it is required | high |
| TC-017 |  | Leave Travel Dates blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-018 |  | Leave Status blank and submit |  | 1. Leave the Status field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Status field indicating it is required | high |
| TC-019 |  | Leave Type blank in Wishlist and submit |  | 1. Leave the Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Type field indicating it is required | high |
| TC-020 |  | Leave Details blank in Wishlist and submit |  | 1. Leave the Details field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Details field indicating it is required | high |
| TC-021 |  | Leave Rating blank in Reviews and submit |  | 1. Leave the Rating field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Rating field indicating it is required | high |
| TC-022 |  | Leave Review blank in Reviews and submit |  | 1. Leave the Review field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Review field indicating it is required | high |
| TC-023 |  | Leave Change Password blank and submit |  | 1. Leave the Change Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Change Password field indicating it is required | high |
| TC-024 |  | Leave Notification Preferences blank and submit |  | 1. Leave the Notification Preferences field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Notification Preferences field indicating it is required | high |
| TC-025 |  | Leave Default Currency blank and submit |  | 1. Leave the Default Currency field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Default Currency field indicating it is required | high |
| TC-026 |  | Leave Default Language blank and submit |  | 1. Leave the Default Language field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Default Language field indicating it is required | high |
| TC-027 |  | Attempt to Cancel a booking without meeting preconditions |  | 1. Click on Cancel for a booking where booking type and cancellation policy do not permit<br>2. Observe the response | Action is blocked; cancellation is not processed | medium |
| TC-028 |  | Attempt to Modify a booking without meeting preconditions |  | 1. Click on Modify for a booking where booking type and cancellation policy do not permit<br>2. Observe the response | Action is blocked; modification is not processed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 (boundary) |  | Add maximum allowed entries to Wishlist | User is logged in and on the User Dashboard | 1. Navigate to Wishlist<br>2. Add maximum allowed entries to the Wishlist | All entries are added successfully; the Wishlist displays the correct number of items. | medium |
| TC-030 (boundary) |  | Attempt to add one more entry to Wishlist beyond maximum | User is logged in and on the User Dashboard, Maximum entries are already added | 1. Navigate to Wishlist<br>2. Attempt to add one more entry to the Wishlist | Action is blocked; a visible error message indicates the maximum limit has been reached. | medium |
| TC-031 (input_edge) |  | Enter a long review text in Reviews | User is logged in and has completed a booking | 1. Navigate to Reviews<br>2. Enter a review with a very long text (200+ characters) | Review is accepted or truncated with a visible indicator. | low |
| TC-032 (input_edge) |  | Enter special characters in Review field | User is logged in and has completed a booking | 1. Navigate to Reviews<br>2. Enter special characters in the Review field | Review is accepted or a specific error message is shown. | low |
| TC-033 (interaction_edge) |  | Rapidly click Cancel on a booking | User is logged in and has a booking with a cancellable status | 1. Navigate to My Bookings<br>2. Click Cancel on a booking multiple times in quick succession | Only one cancellation is processed; subsequent clicks are ignored or show a blocking message. | medium |

---

## Booking Management

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details successfully | User logged in as <User>, booking type and cancellation policy permit modification | 1. Open the Booking Detail View<br>2. Click Modify | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 | WF-002 | Confirm cancellation of booking | User logged in as <User>, user must explicitly confirm cancellation | 1. Open the Booking Detail View<br>2. Click Cancel<br>3. Click Confirm Cancellation on the confirmation dialog | processes cancellation and initiates refund to original payment method | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to modify booking without meeting precondition | booking type and cancellation policy do not permit modification | 1. Click on the Modify button | Modification is blocked; no changes are made to the booking |  |
| TC-004 |  | Attempt to cancel booking without explicit confirmation | user does not confirm cancellation | 1. Click on the Cancel button<br>2. Do not click Confirm Cancellation | Cancellation is not processed; booking remains unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (input_edge) |  | Enter a very long string in the Confirmation Number field |  | 1. Navigate to the Booking Detail View<br>2. Enter a string of 200+ characters in the Confirmation Number field | Confirmation Number field accepts the input without error or is truncated with a visible indicator | low |
| TC-006 (input_edge) |  | Enter special characters in the Full Service Information field |  | 1. Navigate to the Booking Detail View<br>2. Enter special characters in the Full Service Information field | Full Service Information field accepts the input without error or shows a specific error message | low |
| TC-007 (interaction_edge) |  | Rapidly click Cancel after modifying booking | Booking type and cancellation policy permit modification | 1. Navigate to the Booking Detail View<br>2. Click Modify<br>3. Make changes to the booking<br>4. Click Cancel immediately after modification | Cancellation confirmation flow opens without any errors or unintended consequences | medium |
| TC-008 (interaction_edge) |  | Confirm cancellation multiple times |  | 1. Navigate to the Booking Detail View<br>2. Click Cancel<br>3. In the cancellation confirmation flow, click Confirm Cancellation<br>4. Click Confirm Cancellation again before the process completes | Second confirmation attempt is blocked; only one cancellation is processed | medium |

---

## Payment Processing

Total: **20** (positive: 5, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment using Credit/Debit Card | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Credit/Debit Card' from the Payment Method dropdown<br>2. Enter <Cardholder Name> in the Cardholder Name field<br>3. Enter <valid card number> in the Card Number field<br>4. Enter <valid expiration date> in the Expiration Date field<br>5. Enter <valid CVV> in the CVV field<br>6. Click 'Submit Payment' | User is redirected to booking confirmation page with reference number | high |
| TC-002 | WF-001 | Submit payment using PayPal | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'PayPal' from the Payment Method dropdown<br>2. Click 'Submit Payment' | User is redirected to booking confirmation page with reference number | high |
| TC-003 | WF-001 | Submit payment using Bank Transfer | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Bank Transfer' from the Payment Method dropdown<br>2. Click 'Submit Payment' | User is redirected to booking confirmation page with reference number | high |
| TC-004 | WF-001 | Submit payment using Wallet/Credits | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Wallet/Credits' from the Payment Method dropdown<br>2. Click 'Submit Payment' | User is redirected to booking confirmation page with reference number | high |
| TC-005 | WF-002 | Retry payment after failure | User logged in as <Customer>, Booking summary is displayed with price breakdown, Previous payment attempt has failed | 1. Select 'Credit/Debit Card' from the Payment Method dropdown<br>2. Enter <Cardholder Name> in the Cardholder Name field<br>3. Enter <valid card number> in the Card Number field<br>4. Enter <valid expiration date> in the Expiration Date field<br>5. Enter <valid CVV> in the CVV field<br>6. Click 'Retry Payment' | Payment is retried without losing booking details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Payment_Method dropdown blank and submit |  | 1. Leave the Payment_Method field blank<br>2. Fill all other required fields<br>3. Click Submit Payment | Inline validation error appears on the Payment_Method field indicating it is required | high |
| TC-007 |  | Select Credit/Debit Card and leave Cardholder_Name blank |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Cardholder_Name field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-008 |  | Select Credit/Debit Card and leave Card_Number blank |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Card_Number field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-009 |  | Select Credit/Debit Card and leave Expiration_Date blank |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Expiration_Date field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-010 |  | Select Credit/Debit Card and leave CVV blank |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the CVV field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the CVV field indicating it is required | high |
| TC-011 |  | Select Credit/Debit Card and enter invalid Card_Number format |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <invalid card number format> in the Card_Number field<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it must be a valid number | medium |
| TC-012 |  | Select Credit/Debit Card and enter an impossible Expiration_Date |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <impossible expiration date> in the Expiration_Date field<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it must be a valid date | medium |
| TC-013 |  | Select Credit/Debit Card and enter invalid CVV format |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <invalid CVV format> in the CVV field<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the CVV field indicating it must be a valid number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Enter valid card number at maximum length | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number with maximum allowed digits in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-015 (boundary) |  | Enter card number one digit below maximum length | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number with one digit less than the maximum allowed in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form is blocked; error shown indicating the card number is invalid | medium |
| TC-016 (boundary) |  | Enter expiration date as today's date | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter today's date in the Expiration_Date field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-017 (boundary) |  | Enter expiration date as yesterday's date | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter yesterday's date in the Expiration_Date field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form is blocked; error shown indicating the expiration date is invalid | medium |
| TC-018 (input_edge) |  | Enter long cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a very long name (200+ characters) in the Cardholder_Name field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form is blocked; error shown indicating the cardholder name exceeds maximum length | low |
| TC-019 (input_edge) |  | Enter special characters in cardholder name | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter special characters in the Cardholder_Name field<br>3. Fill in all other required fields<br>4. Click Submit Payment | Form is blocked; error shown indicating invalid characters in the cardholder name | low |
| TC-020 (interaction_edge) |  | Rapid resubmission after payment failure | Payment_Method is set to Credit/Debit Card, Previous payment attempt has failed | 1. Click Submit Payment after filling in all required fields<br>2. Observe payment failure message<br>3. Immediately click Submit Payment again | Form is blocked; user remains on the payment page with the previous error message visible | medium |

---

## Currency & Language Selection

Total: **8** (positive: 4, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Select a currency and verify price updates | User logged in as <Authenticated User> | 1. Select 'EUR' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-002 |  | Select a language and verify interface switch | User logged in as <Authenticated User> | 1. Select 'Spanish' from the Language dropdown | The entire site interface switches to Spanish | high |
| TC-003 |  | Select a currency as an unauthenticated user | User is not logged in | 1. Select 'GBP' from the Currency dropdown | All prices displayed across the site update in real-time | medium |
| TC-004 |  | Select a language as an unauthenticated user | User is not logged in | 1. Select 'Arabic' from the Language dropdown | The entire site interface switches to Arabic | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Attempt to select a currency when no currency is selected |  | 1. Leave the Currency Selector blank<br>2. Click to submit the selection | Inline validation error appears on the Currency Selector field indicating it is required | high |
| TC-006 |  | Attempt to select a language when no language is selected |  | 1. Leave the Language Selector blank<br>2. Click to submit the selection | Inline validation error appears on the Language Selector field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) |  | Select a currency option from the dropdown |  | 1. Open the currency selector dropdown<br>2. Select 'USD' from the options | All prices displayed across the site update in real-time to reflect the USD currency | medium |
| TC-008 (input_edge) |  | Select a language option from the dropdown |  | 1. Open the language selector dropdown<br>2. Select 'Spanish' from the options | The entire site interface switches to Spanish, including navigation labels and content | medium |

---

## Search & Filters

Total: **18** (positive: 7, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Apply star ratings filter for hotels | User logged in as <User> | 1. Expand the Filter Section<br>2. Check the '4 Stars' checkbox under Star Ratings | Results update dynamically to show only listings with 4 Stars; the result count reflects the number of matching listings. | high |
| TC-002 |  | Apply multiple hotel filters | User logged in as <User> | 1. Expand the Filter Section<br>2. Check the 'WiFi' checkbox under Facilities/Amenities<br>3. Select 'Luxury' from the Hotel Type dropdown<br>4. Select 'All Inclusive' from the Board Basis dropdown | Results update dynamically to show only luxury hotels with WiFi and All Inclusive options; the result count reflects the number of matching listings. | high |
| TC-003 |  | Apply flight filters | User logged in as <User> | 1. Expand the Filter Section<br>2. Check 'Airline A' and 'Airline B' checkboxes under Airlines<br>3. Select '1 Stop' from the Number of Stops dropdown | Results update dynamically to show only flights with Airline A or Airline B and 1 Stop; the result count reflects the number of matching listings. | high |
| TC-004 |  | Apply tour filters | User logged in as <User> | 1. Expand the Filter Section<br>2. Select 'Adventure' from the Tour Type dropdown | Results update dynamically to show only adventure tours; the result count reflects the number of matching listings. | high |
| TC-005 |  | Apply car filters | User logged in as <User> | 1. Expand the Filter Section<br>2. Select 'SUV' from the Car Type dropdown<br>3. Select 'Automatic' from the Transmission dropdown | Results update dynamically to show only SUVs with Automatic transmission; the result count reflects the number of matching listings. | high |
| TC-006 |  | Sort results by price low to high | User logged in as <User> | 1. Expand the Filter Section<br>2. Select 'Price: Low to High' from the Sorting Controls dropdown | Results update dynamically to show listings sorted from lowest to highest price; the result count reflects the number of matching listings. | medium |
| TC-007 |  | Reset all filters | User logged in as <User>, Filters have been applied | 1. Click the Reset All Filters button | All filters are cleared; the result count reflects the total number of available listings. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to submit filters with all fields empty |  | 1. Leave all filter fields blank<br>2. Click on the Search button | No filters applied; results remain unchanged |  |
| TC-009 |  | Select an invalid option in the Hotel Type dropdown |  | 1. Open the Hotels tab<br>2. Select an invalid option in the Hotel Type dropdown<br>3. Click on the Search button | Error shown: 'Invalid selection for Hotel Type' |  |
| TC-010 |  | Select an invalid option in the Number of Stops dropdown |  | 1. Open the Flights tab<br>2. Select an invalid option in the Number of Stops dropdown<br>3. Click on the Search button | Error shown: 'Invalid selection for Number of Stops' |  |
| TC-011 |  | Select an invalid option in the Tour Type dropdown |  | 1. Open the Tours tab<br>2. Select an invalid option in the Tour Type dropdown<br>3. Click on the Search button | Error shown: 'Invalid selection for Tour Type' |  |
| TC-012 |  | Select an invalid option in the Car Type dropdown |  | 1. Open the Cars tab<br>2. Select an invalid option in the Car Type dropdown<br>3. Click on the Search button | Error shown: 'Invalid selection for Car Type' |  |
| TC-013 |  | Attempt to apply filters with an invalid price range |  | 1. Set the Price Range slider to an invalid range<br>2. Click on the Search button | Error shown: 'Price range is invalid' |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Test removing all active filters | At least one filter is applied | 1. Click on the 'Reset All Filters' button | All active filters are removed; result count updates to reflect all available listings | medium |
| TC-015 (boundary) |  | Test applying maximum number of star ratings | No filters applied | 1. Check '1 Star' checkbox<br>2. Check '2 Stars' checkbox<br>3. Check '3 Stars' checkbox<br>4. Check '4 Stars' checkbox<br>5. Check '5 Stars' checkbox | All star ratings are selected; result count updates to reflect listings matching all selected ratings | medium |
| TC-016 (input_edge) |  | Test entering a long location area string | No filters applied | 1. Enter a string longer than 200 characters in the 'Location Area' search field | An error message is displayed indicating the input exceeds the maximum allowed length | low |
| TC-017 (input_edge) |  | Test entering special characters in the location area | No filters applied | 1. Enter special characters (e.g., @#$%^&*) in the 'Location Area' search field | An error message is displayed indicating invalid characters are not allowed | low |
| TC-018 (interaction_edge) |  | Test rapid re-submission of filters | Filters have been applied and results are displayed | 1. Click on the 'Remove' button for an active filter<br>2. Immediately click on the 'Remove' button for another active filter | Both filters are removed successfully; result count updates accordingly | medium |

---

## Reviews & Ratings

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display aggregate rating and total review count on listing page | User logged in as <Authenticated User> | 1. Navigate to the listing page | The aggregate rating score and total review count are displayed for each item | high |
| TC-002 |  | View individual reviews on detail page | User logged in as <Authenticated User>, User is on the detail page of an item | 1. Scroll to the Reviews section | Individual reviews are visible showing overall rating, category-specific ratings, reviewer name, reviewer country, review date, stay date, written comments, and guest-uploaded photos | high |
| TC-003 |  | Submit a review with star ratings and written feedback | User logged in as <Authenticated User>, User has completed a booking, User is on the detail page of an item | 1. Scroll to the Submit Review section<br>2. Enter <Overall Experience> in the Overall Experience field<br>3. Enter <Category Specific Ratings> in the Category Specific Ratings field<br>4. Enter <Written Feedback> in the Written Feedback field<br>5. Click Submit | A success notification is displayed; the new review appears in the Reviews section | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Overall Experience blank and submit review | User is authenticated and has completed a booking | 1. Navigate to the Submit Review section<br>2. Leave the Overall Experience field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Overall Experience field indicating it is required | high |
| TC-005 |  | Leave Written Feedback blank and submit review | User is authenticated and has completed a booking | 1. Navigate to the Submit Review section<br>2. Leave the Written Feedback field blank<br>3. Fill in all other required fields<br>4. Click Submit | Inline validation error appears on the Written Feedback field indicating it is required | high |
| TC-006 |  | Submit review with invalid date formats | User is authenticated and has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter <invalid date format> in the Review Date field<br>3. Enter <invalid date format> in the Stay Date field<br>4. Fill in all other required fields<br>5. Click Submit | Inline validation error appears on the Review Date field indicating an invalid date format and on the Stay Date field indicating an invalid date format | medium |
| TC-007 |  | Submit review without being authenticated |  | 1. Navigate to the Submit Review section<br>2. Attempt to submit a review | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Add maximum allowed entries to Individual Reviews | User is on the Detail Page | 1. Navigate to the Reviews Section<br>2. Add exactly the maximum allowed number of Individual Reviews | Form submits successfully; all Individual Reviews are displayed in the Reviews Section | medium |
| TC-009 (boundary) |  | Attempt to add one more Individual Review than allowed | User is on the Detail Page | 1. Navigate to the Reviews Section<br>2. Add maximum allowed number of Individual Reviews<br>3. Attempt to add one more Individual Review | Submission is blocked; visible error indicates maximum review limit reached | medium |
| TC-010 (data_edge) |  | Enter today's date for Review Date | User is submitting a review | 1. Fill in the Reviewer Name<br>2. Fill in the Reviewer Country<br>3. Enter today's date in the Review Date field<br>4. Fill in other required fields<br>5. Submit the review | Form submits successfully; review is displayed with today's date | medium |
| TC-011 (data_edge) |  | Enter yesterday's date for Stay Date | User is submitting a review | 1. Fill in the Reviewer Name<br>2. Fill in the Reviewer Country<br>3. Enter yesterday's date in the Stay Date field<br>4. Fill in other required fields<br>5. Submit the review | Form submits successfully; review is displayed with yesterday's stay date | medium |
| TC-012 (data_edge) |  | Upload a file exactly at the size limit | User is submitting a review | 1. Fill in the Reviewer Name<br>2. Fill in the Reviewer Country<br>3. Upload a file exactly at the size limit in the Guest Uploaded Photos field<br>4. Fill in other required fields<br>5. Submit the review | Form submits successfully; review is displayed with the uploaded photo | medium |
| TC-013 (data_edge) |  | Upload a file one byte over the size limit | User is submitting a review | 1. Fill in the Reviewer Name<br>2. Fill in the Reviewer Country<br>3. Upload a file one byte over the size limit in the Guest Uploaded Photos field<br>4. Fill in other required fields<br>5. Submit the review | Submission is blocked; visible error indicates file exceeds size limit | medium |

---

## Offers & Deals

Total: **15** (positive: 4, negative: 5, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Filter offers by service type, destination, and travel dates | User logged in as <User>, No filters applied | 1. Select 'Hotels' from the Service Type Filter dropdown<br>2. Enter <valid destination> in the Destination Filter<br>3. Select <valid travel date> in the Travel Dates Filter | Filtered offers are displayed based on selected service type, destination, and travel dates | high |
| TC-002 |  | Subscribe to newsletter with valid email | User logged in as <User> | 1. Enter <valid email> in the Newsletter Subscription field<br>2. Click 'Subscribe' | A success notification is displayed confirming subscription to the newsletter | medium |
| TC-003 |  | Click 'Book Now' on a deal | User logged in as <User>, Offers are displayed | 1. Click 'Book Now' on a deal card | User is redirected to a pre-filled search with the discounted rates applied | high |
| TC-004 |  | View Terms and Conditions for a deal | User logged in as <User>, Offers are displayed | 1. Click 'Terms and Conditions' on a deal card | Terms and Conditions modal is displayed with relevant details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Newsletter Subscription field blank and submit |  | 1. Leave the Newsletter Subscription field blank<br>2. Fill all other fields as needed<br>3. Click Submit | Inline validation error appears on the Newsletter Subscription field indicating it is required | high |
| TC-006 |  | Submit with all required fields empty |  | 1. Leave the Deal Title field blank<br>2. Leave the Discount Percentage field blank<br>3. Leave the Validity Period field blank<br>4. Leave the Newsletter Subscription field blank<br>5. Click Submit | Inline validation error appears on the Deal Title field indicating it is required; Inline validation error appears on the Discount Percentage field indicating it is required; Inline validation error appears on the Validity Period field indicating it is required; Inline validation error appears on the Newsletter Subscription field indicating it is required | high |
| TC-007 |  | Enter an invalid email format in the Newsletter Subscription field |  | 1. Enter <invalid email format> in the Newsletter Subscription field<br>2. Fill all other fields as needed<br>3. Click Submit | Newsletter Subscription field displays an error: 'Must be a valid email address' | medium |
| TC-008 |  | Enter a non-numeric value in the Discount Percentage field |  | 1. Enter <non-numeric value> in the Discount Percentage field<br>2. Fill all other required fields<br>3. Click Submit | Discount Percentage field displays an error: 'Must be a number' | medium |
| TC-009 |  | Attempt to book a deal without filling required fields |  | 1. Click Book Now on a deal without filling required fields<br>2. Observe the response | Form does not submit; required fields are highlighted | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter exactly 100% in the Discount Percentage field |  | 1. Navigate to the Offers page<br>2. Add a new deal with the Deal Title filled<br>3. Enter 100 in the Discount Percentage field<br>4. Fill Validity Period with a valid date<br>5. Click Submit | Deal is created successfully with Discount Percentage set to 100% | medium |
| TC-011 (boundary) |  | Enter exactly 0% in the Discount Percentage field |  | 1. Navigate to the Offers page<br>2. Add a new deal with the Deal Title filled<br>3. Enter 0 in the Discount Percentage field<br>4. Fill Validity Period with a valid date<br>5. Click Submit | Deal is created successfully with Discount Percentage set to 0% | medium |
| TC-012 (boundary) |  | Enter a negative value in the Discount Percentage field |  | 1. Navigate to the Offers page<br>2. Add a new deal with the Deal Title filled<br>3. Enter -1 in the Discount Percentage field<br>4. Fill Validity Period with a valid date<br>5. Click Submit | Submission is blocked; inline error shown indicating 'Discount Percentage must be a positive number' | medium |
| TC-013 (input_edge) |  | Enter a very long deal title |  | 1. Navigate to the Offers page<br>2. Add a new deal<br>3. Enter a string of 200 characters in the Deal Title field<br>4. Fill Discount Percentage with a valid number<br>5. Fill Validity Period with a valid date<br>6. Click Submit | Deal is created successfully with the long Deal Title displayed correctly | low |
| TC-014 (input_edge) |  | Enter special characters in the Deal Title field |  | 1. Navigate to the Offers page<br>2. Add a new deal<br>3. Enter '!@#$%^&*()' in the Deal Title field<br>4. Fill Discount Percentage with a valid number<br>5. Fill Validity Period with a valid date<br>6. Click Submit | Deal is created successfully with special characters in the Deal Title | low |
| TC-015 (input_edge) |  | Enter an email with leading and trailing whitespace in the Newsletter Subscription field |  | 1. Navigate to the Offers page<br>2. Enter '   user@example.com   ' in the Newsletter Subscription field<br>3. Click Subscribe | Email is trimmed and saved as 'user@example.com' without extra spaces | low |

---

## Logout

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs out | User logged in as <User Role> | 1. Click the Logout_Button | User is redirected to home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access a protected page after logout |  | 1. Click the Logout button | User is redirected to the login page when attempting to access a protected page | high |

---
