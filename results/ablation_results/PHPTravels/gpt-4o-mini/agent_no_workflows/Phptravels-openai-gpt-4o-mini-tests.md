# Test Cases — Phptravels

Generated: 2026-06-09T11:07:00.725136Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 314 | 77 | 127 | 110 | 159 | 110 | 45 |

## Home Page & Search

Total: **29** (positive: 4, negative: 18, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for Hotels with valid inputs | User logged in as <User> | 1. Click on the 'Hotels' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check In Date field<br>4. Enter <valid check-out date> in the Check Out Date field<br>5. Enter <valid number of rooms> in the Number of Rooms field<br>6. Enter <valid number of adults> in the Adults field<br>7. Click the Search button | User is redirected to the corresponding results listing page | high |
| TC-002 |  | Search for Flights with valid inputs | User logged in as <User> | 1. Click on the 'Flights' tab<br>2. Select 'Round-trip' from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Enter <valid departure date> in the Departure Date field<br>6. Enter <valid return date> in the Return Date field<br>7. Enter <valid number of adults> in the Adults field<br>8. Click the Search button | User is redirected to the corresponding results listing page | high |
| TC-003 |  | Search for Tours with valid inputs | User logged in as <User> | 1. Click on the 'Tours' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid start date> in the Start Date field<br>4. Enter <valid end date> in the End Date field<br>5. Click the Search button | User is redirected to the corresponding results listing page | high |
| TC-004 |  | Search for Cars with valid inputs | User logged in as <User> | 1. Click on the 'Cars' tab<br>2. Enter <valid pick-up location> in the Pick Up Location field<br>3. Enter <valid drop-off location> in the Drop Off Location field<br>4. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>6. Click the Search button | User is redirected to the corresponding results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Destination field blank in Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 |  | Leave the Check_In_Date field blank in Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Check_In_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-007 |  | Leave the Check_Out_Date field blank in Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Check_Out_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-008 |  | Leave the Number_of_Rooms field blank in Hotels tab |  | 1. Navigate to the Hotels tab<br>2. Leave the Number_of_Rooms field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-009 |  | Leave the Adults field blank in Guest_Count |  | 1. Navigate to the Hotels tab<br>2. Leave the Adults field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-010 |  | Leave the Trip_Type field blank in Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Trip_Type field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Trip_Type field indicating it is required | high |
| TC-011 |  | Leave the Departure_City field blank in Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Departure_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_City field indicating it is required | high |
| TC-012 |  | Leave the Arrival_City field blank in Flights tab |  | 1. Navigate to the Flights tab<br>2. Leave the Arrival_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Arrival_City field indicating it is required | high |
| TC-013 |  | Leave the Departure_Date field blank in Travel_Dates |  | 1. Navigate to the Flights tab<br>2. Leave the Departure_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-014 |  | Leave the Return_Date field blank in Travel_Dates |  | 1. Navigate to the Flights tab<br>2. Leave the Return_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Return_Date field indicating it is required | high |
| TC-015 |  | Leave the Destination field blank in Tours tab |  | 1. Navigate to the Tours tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-016 |  | Leave the Start_Date field blank in Travel_Date_Range |  | 1. Navigate to the Tours tab<br>2. Leave the Start_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Start_Date field indicating it is required | high |
| TC-017 |  | Leave the End_Date field blank in Travel_Date_Range |  | 1. Navigate to the Tours tab<br>2. Leave the End_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the End_Date field indicating it is required | high |
| TC-018 |  | Leave the Pick_Up_Location field blank in Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Pick_Up_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-019 |  | Leave the Drop_Off_Location field blank in Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Drop_Off_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-020 |  | Leave the Pick_Up_Date_Time field blank in Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Pick_Up_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-021 |  | Leave the Drop_Off_Date_Time field blank in Cars tab |  | 1. Navigate to the Cars tab<br>2. Leave the Drop_Off_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |
| TC-022 |  | Attempt to search without filling any required fields |  | 1. Navigate to any tab<br>2. Leave all required fields blank<br>3. Click Search | Inline validation errors appear on all required fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 (boundary) |  | Check-In_Date equals Check-Out_Date | User is on the Hotels tab | 1. Enter 'New York' in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter '1' in the Number_of_Rooms field<br>5. Enter '2' in the Adults field | Search button is enabled and allows submission; user is redirected to results listing page | medium |
| TC-024 (boundary) |  | Check-Out_Date is one day before Check-In_Date | User is on the Hotels tab | 1. Enter 'New York' in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter yesterday's date in the Check_Out_Date field<br>4. Enter '1' in the Number_of_Rooms field<br>5. Enter '2' in the Adults field | Inline error appears on Check-Out_Date field indicating the date must be after Check-In_Date | medium |
| TC-025 (boundary) |  | Number_of_Rooms is zero | User is on the Hotels tab | 1. Enter 'New York' in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter tomorrow's date in the Check_Out_Date field<br>4. Enter '0' in the Number_of_Rooms field<br>5. Enter '2' in the Adults field | Inline error appears on Number_of_Rooms field indicating it must be greater than zero | medium |
| TC-026 (boundary) |  | Passenger_Count exceeds maximum allowed | User is on the Flights tab | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'Los Angeles' in the Departure_City field<br>3. Enter 'New York' in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter tomorrow's date in the Return_Date field<br>6. Enter '10' in the Adults field | Inline error appears on Adults field indicating the maximum number of passengers is exceeded | medium |
| TC-027 (input_edge) |  | Enter a very long string in the Destination field | User is on the Hotels tab | 1. Enter a string of 300 characters in the Destination field | Inline error appears indicating the input exceeds the maximum allowed length | low |
| TC-028 (input_edge) |  | Enter special characters in the Pick_Up_Location field | User is on the Cars tab | 1. Enter '@#$%^&*' in the Pick_Up_Location field | Inline error appears indicating invalid characters in the Pick_Up_Location field | low |
| TC-029 (interaction_edge) |  | Rapid submission after redirect | User has successfully submitted a search | 1. Press the browser back button after being redirected to the results listing page | User is shown a blank search form; no duplicate submission occurs | medium |

---

## User Registration

Total: **17** (positive: 1, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful registration with valid details | User logged in as <Guest> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid unique email> in the Email field<br>4. Enter <valid password> in the Password field<br>5. Enter <same valid password> in the Confirm Password field<br>6. Enter <valid mobile number> in the Mobile Number field<br>7. Enter <valid address> in the Address field<br>8. Enter <valid country> in the Country field<br>9. Check the Terms and Conditions checkbox<br>10. Click Submit Registration | creates account and redirects to dashboard or prompts for email verification | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave First Name blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave Last Name blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave Email blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave Password blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Leave Confirm Password blank and submit |  | 1. Leave the Confirm_Password field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-007 |  | Leave Mobile Number blank and submit |  | 1. Leave the Mobile_Number field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Mobile_Number field indicating it is required | high |
| TC-008 |  | Leave Address blank and submit |  | 1. Leave the Address field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Address field indicating it is required | high |
| TC-009 |  | Leave Country blank and submit |  | 1. Leave the Country field blank<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Country field indicating it is required | high |
| TC-010 |  | Leave Terms and Conditions unchecked and submit |  | 1. Leave the Terms_and_Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit Registration | Inline validation error appears on the Terms_and_Conditions field indicating it is required | high |
| TC-011 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit Registration | Inline validation error appears on the Email field indicating it must be a valid email format | medium |
| TC-012 |  | Submit with non-matching passwords |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit Registration | Inline validation error appears indicating the passwords do not match | medium |
| TC-013 |  | Submit with duplicate email |  | 1. Enter <duplicate email> in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit Registration | Inline validation error appears on the Email field indicating it must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Email format validation at boundary |  | 1. Enter 'user@domain.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; account is created and user is redirected to dashboard | medium |
| TC-015 (boundary) |  | Email uniqueness validation at boundary | An account with 'user@domain.com' already exists | 1. Enter 'user@domain.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Email field displays an error indicating the email must be unique | medium |
| TC-016 (input_edge) |  | Long text in Address field |  | 1. Enter a string of 200+ characters in the Address field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; address is saved correctly or truncated with a visible indicator | low |
| TC-017 (input_edge) |  | Leading/trailing whitespace in First Name field |  | 1. Enter '  John  ' in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## User Login

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User logged in as <User>, Social login is not used | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to dashboard or previous page | high |
| TC-002 |  | Successful login with Remember Me option | User logged in as <User>, Social login is not used | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Check the Remember Me checkbox<br>4. Click Login | redirects to dashboard or previous page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Leave the Password field blank and submit |  | 1. Fill the Email field with <valid email><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-005 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill the Password field with <valid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | medium |
| TC-006 |  | Submit with incorrect credentials |  | 1. Fill the Email field with <valid email><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | high |
| TC-007 |  | Attempt to login after multiple consecutive failed attempts without CAPTCHA |  | 1. Fill the Email field with <valid email><br>2. Fill the Password field with <invalid password><br>3. Click Login<br>4. Repeat steps 1-3 multiple times | CAPTCHA verification is required before further login attempts | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter an invalid email format |  | 1. Enter 'invalid-email' in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message is shown indicating invalid email format; password field is cleared | medium |
| TC-009 (input_edge) |  | Enter a very long email address |  | 1. Enter a string of 200 characters in the Email field<br>2. Enter a valid password in the Password field<br>3. Click Login | Error message is shown indicating email exceeds maximum length | low |
| TC-010 (input_edge) |  | Enter special characters in the password field |  | 1. Enter a valid email in the Email field<br>2. Enter '!@#$%^&*()' in the Password field<br>3. Click Login | Error message is shown indicating invalid password format; password field is cleared | low |
| TC-011 (interaction_edge) |  | Rapid consecutive login attempts with invalid credentials |  | 1. Enter a valid email in the Email field<br>2. Enter an invalid password in the Password field<br>3. Click Login<br>4. Repeat steps 1-3 three times rapidly | After multiple failed attempts, CAPTCHA verification is displayed | medium |

---

## Forgot Password

Total: **12** (positive: 2, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit valid email to reset password | User logged in as <User>, Email exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is shown that 'sends reset link to email' | high |
| TC-002 |  | Change password with matching confirmation | User navigates to the password reset page using the reset link | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | User is redirected to login page with a success message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it must be a valid email address | medium |
| TC-005 |  | Submit the password reset form with New_Password and Confirm_Password fields blank |  | 1. Leave the New_Password field blank<br>2. Leave the Confirm_Password field blank<br>3. Click Change Password | Inline validation error appears on the New_Password field indicating it is required | high |
| TC-006 |  | Submit the password reset form with mismatched passwords |  | 1. Enter <valid password> in the New_Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Click Change Password | Error message shows if passwords do not match | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Submit with valid email exactly at character limit |  | 1. Enter a valid email address with maximum allowed length in the Email field<br>2. Click Reset Password | Reset link is sent to the email; confirmation message is shown | medium |
| TC-008 (boundary) |  | Submit with email that does not exist in the system |  | 1. Enter an email address that does not exist in the system in the Email field<br>2. Click Reset Password | Error message is shown indicating email not found; form remains editable | medium |
| TC-009 (input_edge) |  | Enter email with leading and trailing whitespace |  | 1. Enter '   test@example.com   ' in the Email field<br>2. Click Reset Password | Leading/trailing whitespace is trimmed; reset link is sent to 'test@example.com' | low |
| TC-010 (input_edge) |  | Enter very long email address |  | 1. Enter a very long email address (over 254 characters) in the Email field<br>2. Click Reset Password | Error message is shown indicating invalid email format | low |
| TC-011 (input_edge) |  | Submit with empty password fields |  | 1. Enter a new password in the New Password field<br>2. Leave the Confirm Password field empty<br>3. Click Change Password | Error message is shown indicating passwords do not match; form remains editable | medium |
| TC-012 (input_edge) |  | Enter passwords that do not match |  | 1. Enter 'Password123' in the New Password field<br>2. Enter 'Password1234' in the Confirm Password field<br>3. Click Change Password | Error message is shown indicating passwords do not match; form remains editable | medium |

---

## Hotels Search & Listing

Total: **17** (positive: 5, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful hotel search with valid inputs | User logged in as <Guest> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' in the Guest Count section<br>6. Enter <number of adults> in the Adults field<br>7. Click 'Add Row' in the Guest Count section<br>8. Enter <number of children> in the Children field<br>9. Click the Search button | User is redirected to the listing page | high |
| TC-002 |  | Dynamic filter application for price range | User logged in as <Guest> | 1. Click on the Price Range filter<br>2. Adjust the price range slider to <valid range><br>3. Observe the hotel listings | The hotel listings update to reflect the selected price range | medium |
| TC-003 |  | Dynamic filter application for star rating | User logged in as <Guest> | 1. Click on the Star Rating filter<br>2. Select <valid star rating> from the options<br>3. Observe the hotel listings | The hotel listings update to show only hotels with the selected star rating | medium |
| TC-004 |  | Dynamic filter application for hotel type | User logged in as <Guest> | 1. Click on the Hotel Type dropdown<br>2. Select <valid hotel type><br>3. Observe the hotel listings | The hotel listings update to show only hotels of the selected type | medium |
| TC-005 |  | Reset all filters | User logged in as <Guest>, Filters have been applied | 1. Click the Reset all control in the active filters summary<br>2. Observe the hotel listings | All filters are cleared and full unfiltered results are restored | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill in Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-007 |  | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill in Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-008 |  | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill in Destination, Check_In_Date, Number_of_Rooms, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-009 |  | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill in Destination, Check_In_Date, Check_Out_Date, and Guest_Count with valid values<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-010 |  | Leave the Adults field blank in Guest_Count and submit |  | 1. Leave the Adults field blank in Guest_Count<br>2. Fill in Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms with valid values<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-011 |  | Submit with all required fields empty |  | 1. Leave all required fields (Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults) blank<br>2. Click Search | Inline validation errors appear on the Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Check-In Date equals Check-Out Date | User has filled in the Destination and Number of Rooms fields | 1. Enter today's date in the Check-In Date field<br>2. Enter today's date in the Check-Out Date field<br>3. Fill in the Guest Count with at least one adult<br>4. Click Search | Search succeeds and user is redirected to the listing page | medium |
| TC-013 (boundary) |  | Check-Out Date is one day before Check-In Date | User has filled in the Destination and Number of Rooms fields | 1. Enter tomorrow's date in the Check-In Date field<br>2. Enter today's date in the Check-Out Date field<br>3. Fill in the Guest Count with at least one adult<br>4. Click Search | Search is blocked; error message displayed indicating Check-Out Date must be after Check-In Date | medium |
| TC-014 (boundary) |  | Number of Rooms at minimum allowed value | User has filled in the Destination, Check-In Date, and Check-Out Date fields | 1. Enter 1 in the Number of Rooms field<br>2. Fill in the Guest Count with at least one adult<br>3. Click Search | Search succeeds and user is redirected to the listing page | medium |
| TC-015 (boundary) |  | Guest Count exceeds maximum allowed entries | User has filled in the Destination, Check-In Date, Check-Out Date, and Number of Rooms fields | 1. Add maximum allowed entries for Adults in Guest Count<br>2. Attempt to add one more entry for Adults<br>3. Click Search | Search is blocked; error message displayed indicating maximum guest count exceeded | medium |
| TC-016 (input_edge) |  | Enter long text in Destination field |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Fill in the Check-In Date, Check-Out Date, Number of Rooms, and Guest Count fields<br>3. Click Search | Search is blocked; error message displayed indicating the Destination field is too long | low |
| TC-017 (input_edge) |  | Enter special characters in Destination field |  | 1. Enter special characters (e.g., @#$%^&*) in the Destination field<br>2. Fill in the Check-In Date, Check-Out Date, Number of Rooms, and Guest Count fields<br>3. Click Search | Search succeeds and user is redirected to the listing page | low |

---

## Hotel Details & Booking

Total: **16** (positive: 1, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful hotel booking | User logged in as <User>, Selected hotel is <Hotel Name>, Room type is <Room Type>, Stay dates are <Start Date> to <End Date>, Guest count is <Number> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Phone Number> in the Phone Number field<br>5. Optionally enter <Special Requests> in the Special Requests field<br>6. Click Book Now | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Selected Hotel field blank and submit |  | 1. Leave the Selected Hotel field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Selected Hotel field indicating it is required | high |
| TC-003 |  | Leave the Room Type field blank and submit |  | 1. Leave the Room Type field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Room Type field indicating it is required | high |
| TC-004 |  | Leave the Stay Dates field blank and submit |  | 1. Leave the Stay Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay Dates field indicating it is required | high |
| TC-005 |  | Leave the Guest Count field blank and submit |  | 1. Leave the Guest Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest Count field indicating it is required | high |
| TC-006 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First Name field indicating it is required | high |
| TC-007 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-008 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-010 |  | Attempt to book without being logged in |  | 1. Fill all required fields with valid data<br>2. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Enter minimum allowed guest count | User is logged in, Room type and stay dates are selected | 1. Enter 1 in the Guest Count field<br>2. Fill all other required fields<br>3. Click Book Now | Form submits successfully; proceeds to payment page | medium |
| TC-012 (boundary) |  | Enter one unit below minimum guest count | User is logged in, Room type and stay dates are selected | 1. Enter 0 in the Guest Count field<br>2. Fill all other required fields<br>3. Click Book Now | Guest Count displays an error indicating the value is below the minimum allowed | medium |
| TC-013 (data_edge) |  | Enter today's date in Stay Dates | User is logged in, Room type and guest count are selected | 1. Enter today's date in the Stay Dates field<br>2. Fill all other required fields<br>3. Click Book Now | Form submits successfully; proceeds to payment page | medium |
| TC-014 (data_edge) |  | Enter a far future date in Stay Dates | User is logged in, Room type and guest count are selected | 1. Enter a date 5 years in the future in the Stay Dates field<br>2. Fill all other required fields<br>3. Click Book Now | Form submits successfully; proceeds to payment page | medium |
| TC-015 (input_edge) |  | Enter a very long first name | User is logged in, Room type and stay dates are selected | 1. Enter a string of 200 characters in the First Name field<br>2. Fill all other required fields<br>3. Click Book Now | Form submits successfully; proceeds to payment page or shows truncation error | low |
| TC-016 (input_edge) |  | Enter special characters in Last Name | User is logged in, Room type and stay dates are selected | 1. Enter special characters in the Last Name field<br>2. Fill all other required fields<br>3. Click Book Now | Form submits successfully; proceeds to payment page or shows specific error | low |

---

## Flights Search & Listing

Total: **16** (positive: 4, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for flights with valid inputs | User logged in as <User> | 1. Select 'Round-trip' from the Trip Type dropdown<br>2. Enter <valid departure city> in the Departure City field<br>3. Enter <valid arrival city> in the Arrival City field<br>4. Enter <valid travel dates> in the Travel Dates field<br>5. Enter '2' in the Adults field under Passenger Count<br>6. Select 'Economy' from the Cabin Class dropdown<br>7. Click Search Flights | User is redirected to listing page | high |
| TC-002 |  | Select a flight from the listing | User logged in as <User>, User is on the listing page | 1. Click Select on the first flight result | Flight details are displayed for the selected flight | medium |
| TC-003 |  | Sort flights by Price | User logged in as <User>, User is on the listing page | 1. Select 'Price' from the Sorting Options dropdown | Flights are sorted by price in ascending order | medium |
| TC-004 |  | Apply a filter for number of stops | User logged in as <User>, User is on the listing page | 1. Select <valid number of stops> from the Number of Stops dropdown | Only flights matching the selected number of stops are displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave all required fields blank and submit the search form |  | 1. Leave the Trip Type field blank<br>2. Leave the Departure City field blank<br>3. Leave the Arrival City field blank<br>4. Leave the Travel Dates field blank<br>5. Leave the Passenger Count fields (Adults, Children, Infants) blank<br>6. Leave the Cabin Class field blank<br>7. Click on Search Flights | Form does not submit; error shown on Trip Type, Departure City, Arrival City, Travel Dates, Passenger Count, and Cabin Class fields indicating they are required | high |
| TC-006 |  | Submit the search form with an invalid date |  | 1. Select One-way from the Trip Type dropdown<br>2. Enter <invalid date format> in the Travel Dates field<br>3. Fill in valid values for Departure City, Arrival City, Passenger Count, and Cabin Class<br>4. Click on Search Flights | Form does not submit; error shown on Travel Dates field indicating it must be a valid date | medium |
| TC-007 |  | Submit the search form with a negative passenger count |  | 1. Select One-way from the Trip Type dropdown<br>2. Enter <negative number> in the Adults field of Passenger Count<br>3. Fill in valid values for Departure City, Arrival City, Travel Dates, and Cabin Class<br>4. Click on Search Flights | Form does not submit; error shown on Adults field indicating passenger count must be a positive number | medium |
| TC-008 |  | Attempt to search flights without selecting a trip type |  | 1. Leave the Trip Type field blank<br>2. Fill in valid values for Departure City, Arrival City, Travel Dates, Passenger Count, and Cabin Class<br>3. Click on Search Flights | Form does not submit; error shown on Trip Type field indicating it is required | high |
| TC-009 |  | Attempt to search flights with invalid cabin class |  | 1. Select One-way from the Trip Type dropdown<br>2. Fill in valid values for Departure City, Arrival City, Travel Dates, and Passenger Count<br>3. Enter <invalid cabin class> in the Cabin Class field<br>4. Click on Search Flights | Form does not submit; error shown on Cabin Class field indicating it must be a valid option | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Test maximum passenger count for adults |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter exactly the maximum allowed number of adults in the Adults field<br>6. Click 'Search Flights' | Redirects to the listing page showing available flights | medium |
| TC-011 (boundary) |  | Test exceeding maximum passenger count for adults |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter one more than the maximum allowed number of adults in the Adults field<br>6. Click 'Search Flights' | Form submission is blocked; error message shown indicating the maximum passenger count exceeded | medium |
| TC-012 (boundary) |  | Test minimum passenger count for adults |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter the minimum allowed number of adults in the Adults field<br>6. Click 'Search Flights' | Redirects to the listing page showing available flights | medium |
| TC-013 (boundary) |  | Test exceeding minimum passenger count for adults |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Enter one less than the minimum allowed number of adults in the Adults field<br>6. Click 'Search Flights' | Form submission is blocked; error message shown indicating the minimum passenger count not met | medium |
| TC-014 (input_edge) |  | Test long text in Departure_City field |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter a very long string (200+ characters) in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Click 'Search Flights' | Form submission is blocked; error message shown indicating invalid input in Departure_City field | low |
| TC-015 (input_edge) |  | Test special characters in Arrival_City field |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter '@Los Angeles!' in the Arrival_City field<br>3. Enter 'New York' in the Departure_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Click 'Search Flights' | Form submission is blocked; error message shown indicating invalid characters in Arrival_City field | low |
| TC-016 (interaction_edge) |  | Test rapid re-submission after successful search |  | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Click 'Search Flights'<br>6. After redirecting to the listing page, quickly click 'Search Flights' again | User is redirected to the listing page without a duplicate search being executed | low |

---

## Flight Booking

Total: **13** (positive: 2, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful flight booking with valid traveler details | User logged in as <Traveler>, All required fields are empty | 1. Click 'Add Traveler' to add a new traveler<br>2. Select 'Mr' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid expiry date> in the Passport Expiry field<br>8. Enter <valid email> in the Lead Passenger Email field<br>9. Enter <valid phone number> in the Lead Passenger Phone field<br>10. Click Continue | User is redirected to the payment page | high |
| TC-002 |  | Inline error displayed for missing required fields | User logged in as <Traveler>, All required fields are empty | 1. Click Continue | Inline errors are displayed for all required fields | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave all required fields blank and submit |  | 1. Leave the Title field blank<br>2. Leave the First_Name field blank<br>3. Leave the Last_Name field blank<br>4. Leave the Date_of_Birth field blank<br>5. Leave the Passport_Number field blank<br>6. Leave the Passport_Expiry field blank<br>7. Leave the Lead_Passenger_Email field blank<br>8. Leave the Lead_Passenger_Phone field blank<br>9. Click Continue | Inline validation errors appear on all required fields indicating they are required; form does not submit | high |
| TC-004 |  | Leave the Title field blank for a traveler and submit |  | 1. Leave the Title field blank for the traveler<br>2. Fill in all other required fields for the traveler<br>3. Fill in all required fields for the Lead Passenger<br>4. Click Continue | Inline validation error appears on the Title field indicating it is required; form does not submit | high |
| TC-005 |  | Enter an invalid email format and submit |  | 1. Fill in all required fields correctly<br>2. Enter <invalid email format> in the Lead_Passenger_Email field<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Email field indicating it must be a valid email address; form does not submit | medium |
| TC-006 |  | Enter a past date for Passport Expiry and submit |  | 1. Fill in all required fields correctly<br>2. Enter <past date> in the Passport_Expiry field<br>3. Click Continue | Inline validation error appears on the Passport_Expiry field indicating it must be a future date; form does not submit | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Add maximum allowed travelers to the booking form | User is on the flight booking page | 1. Add exactly the maximum allowed number of travelers to the Travelers group | Form submits successfully; all traveler details are displayed correctly. | medium |
| TC-008 (boundary) |  | Attempt to add one more traveler beyond the maximum allowed | User has filled the maximum allowed travelers | 1. Attempt to add one more traveler to the Travelers group | Adding traveler is blocked; an inline error message is displayed indicating the maximum limit has been reached. | medium |
| TC-009 (boundary) |  | Enter today's date in the Date of Birth field | User is filling out the booking form | 1. Enter today's date in the Date of Birth field | Inline error displayed indicating the date of birth cannot be today. | medium |
| TC-010 (boundary) |  | Enter a date in the Passport Expiry field that is today | User is filling out the booking form | 1. Enter today's date in the Passport Expiry field | Form submits successfully; passport expiry date is recorded as today. | medium |
| TC-011 (input_edge) |  | Enter a very long string in the First Name field | User is filling out the booking form | 1. Enter a string of 200+ characters in the First Name field | Inline error displayed indicating the input exceeds the maximum length allowed. | low |
| TC-012 (input_edge) |  | Enter special characters in the Last Name field | User is filling out the booking form | 1. Enter special characters in the Last Name field | Inline error displayed indicating invalid characters in the Last Name field. | low |
| TC-013 (input_edge) |  | Enter a value with leading and trailing whitespace in the Lead Passenger Email field | User is filling out the booking form | 1. Enter '   example@test.com   ' in the Lead Passenger Email field | Whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Tours Search & Listing

Total: **15** (positive: 1, negative: 10, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for tours with valid inputs | User logged in as <User> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select <Tour_Type> from the Tour Type dropdown<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid budget range> in the Budget Range field<br>6. Click Search | User is redirected to the listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Destination field blank and submit the search form |  | 1. Leave the Destination field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-003 |  | Leave the Travel Dates field blank and submit the search form |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-004 |  | Leave the Duration field blank and submit the search form |  | 1. Leave the Duration field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Duration field indicating it is required | high |
| TC-005 |  | Leave the Budget Range field blank and submit the search form |  | 1. Leave the Budget Range field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Budget Range field indicating it is required | high |
| TC-006 |  | Leave all required fields blank and submit the search form |  | 1. Leave the Destination field blank<br>2. Leave the Travel Dates field blank<br>3. Leave the Duration field blank<br>4. Leave the Budget Range field blank<br>5. Click Search | Form does not submit; multiple inline validation errors appear indicating required fields | high |
| TC-007 |  | Leave the Destination Filter field blank and submit the sidebar filter form |  | 1. Leave the Destination Filter field blank<br>2. Fill all other required fields<br>3. Click Apply Filters | Inline validation error appears on the Destination Filter field indicating it is required | high |
| TC-008 |  | Leave the Price Range Filter field blank and submit the sidebar filter form |  | 1. Leave the Price Range Filter field blank<br>2. Fill all other required fields<br>3. Click Apply Filters | Inline validation error appears on the Price Range Filter field indicating it is required | high |
| TC-009 |  | Leave the Duration Filter field blank and submit the sidebar filter form |  | 1. Leave the Duration Filter field blank<br>2. Fill all other required fields<br>3. Click Apply Filters | Inline validation error appears on the Duration Filter field indicating it is required | high |
| TC-010 |  | Leave the Departure Dates Filter field blank and submit the sidebar filter form |  | 1. Leave the Departure Dates Filter field blank<br>2. Fill all other required fields<br>3. Click Apply Filters | Inline validation error appears on the Departure Dates Filter field indicating it is required | high |
| TC-011 |  | Leave all required fields blank and submit the sidebar filter form |  | 1. Leave the Destination Filter field blank<br>2. Leave the Price Range Filter field blank<br>3. Leave the Duration Filter field blank<br>4. Leave the Departure Dates Filter field blank<br>5. Click Apply Filters | Form does not submit; multiple inline validation errors appear indicating required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) |  | Enter minimum duration value in the Duration field |  | 1. Enter <minimum duration> in the Duration field<br>2. Fill all other required fields<br>3. Click Search | Form submits successfully; user is redirected to the listing page | medium |
| TC-013 (boundary) |  | Enter one unit below minimum duration in the Duration field |  | 1. Enter <one unit below minimum duration> in the Duration field<br>2. Fill all other required fields<br>3. Click Search | Duration field displays an error indicating the value is below the minimum allowed | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Destination field |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Fill all other required fields<br>3. Click Search | Form submits successfully; user is redirected to the listing page or the input is truncated with a visible indicator | low |
| TC-015 (input_edge) |  | Enter special characters in the Budget Range field |  | 1. Enter special characters in the Budget Range field<br>2. Fill all other required fields<br>3. Click Search | Budget Range field displays an error indicating invalid characters | low |

---

## Tour Details & Booking

Total: **13** (positive: 1, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful booking with valid details | User logged in as <Authenticated User> | 1. Select a valid <departure date> from the available dates<br>2. Enter <number of travelers> in the Number of Travelers field<br>3. Click 'Add Row' to enter traveler names<br>4. Enter <traveler name> in the new row<br>5. Enter <contact details> in the Contact Details field<br>6. Click 'Book Now' | User is redirected to booking confirmation | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Departure Date field blank |  | 1. Leave the Departure_Date field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-003 |  | Leave the Number of Travelers field blank |  | 1. Leave the Number_of_Travelers field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Number_of_Travelers field indicating it is required | high |
| TC-004 |  | Leave the Contact Details field blank |  | 1. Leave the Contact_Details field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Contact_Details field indicating it is required | high |
| TC-005 |  | Leave the Name field in Traveler Names blank |  | 1. Leave the Name field in Traveler_Names blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Unauthenticated user attempts to book a tour |  | 1. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Test departure date as today | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Enter a valid number in the Number_of_Travelers field<br>3. Fill in all required fields<br>4. Click Book Now | Booking proceeds to confirmation page | medium |
| TC-008 (boundary) |  | Test departure date as yesterday | User is authenticated | 1. Select yesterday's date in the Departure_Date field<br>2. Enter a valid number in the Number_of_Travelers field<br>3. Fill in all required fields<br>4. Click Book Now | Booking is blocked; error shown indicating departure date must be today or later | medium |
| TC-009 (boundary) |  | Add maximum number of travelers | User is authenticated | 1. Enter maximum allowed number of travelers in the Number_of_Travelers field<br>2. Fill in all required fields including traveler names<br>3. Click Book Now | Booking proceeds to confirmation page | medium |
| TC-010 (boundary) |  | Attempt to add one more traveler than allowed | User is authenticated | 1. Enter maximum allowed number of travelers + 1 in the Number_of_Travelers field<br>2. Fill in all required fields<br>3. Click Book Now | Booking is blocked; error shown indicating too many travelers | medium |
| TC-011 (input_edge) |  | Enter long name for traveler | User is authenticated | 1. Fill in the Name field for a traveler with a long string (200+ characters)<br>2. Fill in all other required fields<br>3. Click Book Now | Booking is blocked; error shown indicating name exceeds character limit | low |
| TC-012 (input_edge) |  | Enter special characters in traveler name | User is authenticated | 1. Enter special characters in the Name field for a traveler<br>2. Fill in all other required fields<br>3. Click Book Now | Booking is blocked; error shown indicating invalid characters in name | low |
| TC-013 (input_edge) |  | Enter leading/trailing whitespace in traveler name | User is authenticated | 1. Enter a name with leading/trailing whitespace in the Name field for a traveler<br>2. Fill in all other required fields<br>3. Click Book Now | Leading/trailing whitespace is trimmed; saved value shown in confirmation page has no extra spaces | low |

---

## Cars Search & Listing

Total: **17** (positive: 7, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Search for cars with valid inputs | User logged in as <User> | 1. Enter <valid pick-up location> in the Pick Up Location field<br>2. Enter <valid drop-off location> in the Drop Off Location field<br>3. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>4. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>5. Enter <valid driver age> in the Driver Age field<br>6. Click Search | The page redirects to listing page | high |
| TC-002 |  | Filter car listings by Car Type | User logged in as <User>, User is on the car listing page | 1. Select 'SUV' from the Car Type dropdown | Only SUV listings are displayed; unrelated car types are no longer visible | medium |
| TC-003 |  | Filter car listings by Transmission | User logged in as <User>, User is on the car listing page | 1. Select 'Automatic' from the Transmission dropdown | Only listings with Automatic transmission are displayed; unrelated listings are no longer visible | medium |
| TC-004 |  | Filter car listings by Fuel Policy | User logged in as <User>, User is on the car listing page | 1. Select <valid fuel policy> from the Fuel Policy dropdown | Only listings matching the selected fuel policy are displayed; unrelated listings are no longer visible | medium |
| TC-005 |  | Filter car listings by Rental Company | User logged in as <User>, User is on the car listing page | 1. Select <valid rental company> from the Rental Company dropdown | Only listings from the selected rental company are displayed; unrelated listings are no longer visible | medium |
| TC-006 |  | Filter car listings by Price Range | User logged in as <User>, User is on the car listing page | 1. Enter <valid price range> in the Price Range field | Only listings within the specified price range are displayed; unrelated listings are no longer visible | medium |
| TC-007 |  | Book a car from the listing | User logged in as <User>, User is on the car listing page | 1. Click Book Now on a car listing | The page redirects to the booking page for the selected car | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Leave the Pick Up Location blank and submit |  | 1. Leave the Pick_Up_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-009 |  | Leave the Drop Off Location blank and submit |  | 1. Leave the Drop_Off_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-010 |  | Leave the Pick Up Date Time blank and submit |  | 1. Leave the Pick_Up_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-011 |  | Leave the Drop Off Date Time blank and submit |  | 1. Leave the Drop_Off_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |
| TC-012 |  | Leave the Driver Age blank and submit |  | 1. Leave the Driver_Age field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Driver_Age field indicating it is required | high |
| TC-013 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Form does not submit; errors shown on all required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Pick-Up Date and Drop-Off Date are the same | User is on the car rental search form | 1. Enter a valid Pick-Up Location in the Pick_Up_Location field<br>2. Enter a valid Drop-Off Location in the Drop_Off_Location field<br>3. Enter today's date in the Pick_Up_Date_Time field<br>4. Enter today's date in the Drop_Off_Date_Time field<br>5. Enter a valid age in the Driver_Age field<br>6. Click Search | Redirects to the listing page with search results for rentals available for today | medium |
| TC-015 (boundary) |  | Drop-Off Date is before Pick-Up Date | User is on the car rental search form | 1. Enter a valid Pick-Up Location in the Pick_Up_Location field<br>2. Enter a valid Drop-Off Location in the Drop_Off_Location field<br>3. Enter tomorrow's date in the Pick_Up_Date_Time field<br>4. Enter today's date in the Drop_Off_Date_Time field<br>5. Enter a valid age in the Driver_Age field<br>6. Click Search | Search is blocked; error message indicates that Drop-Off Date must be after Pick-Up Date | medium |
| TC-016 (boundary) |  | Driver Age at minimum valid age | User is on the car rental search form | 1. Enter a valid Pick-Up Location in the Pick_Up_Location field<br>2. Enter a valid Drop-Off Location in the Drop_Off_Location field<br>3. Enter the minimum valid age in the Driver_Age field<br>4. Enter valid dates in the Pick_Up_Date_Time and Drop_Off_Date_Time fields<br>5. Click Search | Redirects to the listing page with search results for rentals available | medium |
| TC-017 (boundary) |  | Driver Age below minimum valid age | User is on the car rental search form | 1. Enter a valid Pick-Up Location in the Pick_Up_Location field<br>2. Enter a valid Drop-Off Location in the Drop_Off_Location field<br>3. Enter an age below the minimum valid age in the Driver_Age field<br>4. Enter valid dates in the Pick_Up_Date_Time and Drop_Off_Date_Time fields<br>5. Click Search | Search is blocked; error message indicates that the Driver Age is not valid | medium |

---

## Car Booking

Total: **18** (positive: 3, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful car booking with all valid inputs | User logged in as <Driver> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click 'Add Row' to add an add-on<br>8. Select GPS checkbox<br>9. Select <valid insurance plan> from the Insurance Plan dropdown<br>10. Check the Terms Acceptance checkbox<br>11. Click Confirm Booking | User is redirected to payment | high |
| TC-002 |  | Error displayed for invalid email format | User logged in as <Driver> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid country> from the License Issue Country dropdown<br>5. Enter <invalid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click Confirm Booking | Invalid fields display inline errors and block progression | high |
| TC-003 |  | Error displayed for missing required fields | User logged in as <Driver> | 1. Click Confirm Booking | Invalid fields display inline errors and block progression | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Driver Full Name field blank and submit |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-005 |  | Leave the Age field blank and submit |  | 1. Leave the Age field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-006 |  | Leave the License Number field blank and submit |  | 1. Leave the License Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-007 |  | Leave the License Issue Country field blank and submit |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-008 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-009 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-010 |  | Leave the Insurance Plan field unselected and submit |  | 1. Leave the Insurance Plan field unselected<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating it is required | high |
| TC-011 |  | Leave the Terms Acceptance checkbox unchecked and submit |  | 1. Leave the Terms Acceptance checkbox unchecked<br>2. Fill all other required fields<br>3. Click Confirm Booking | Inline validation error appears on the Terms Acceptance field indicating it is required | high |
| TC-012 |  | Submit with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Confirm Booking | Inline validation errors appear on all required fields indicating they are required; form does not submit | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | Enter minimum age value |  | 1. Enter <minimum allowed age> in the <Age> field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; proceeds to payment | medium |
| TC-014 (boundary) |  | Enter one unit below minimum age value |  | 1. Enter <one unit below minimum age> in the <Age> field<br>2. Fill all other required fields<br>3. Click Confirm Booking | <Age> displays an error indicating the value is below the minimum allowed | medium |
| TC-015 (boundary) |  | Add maximum allowed entries to Add Ons |  | 1. Add exactly <maximum allowed entries> to the <Add_Ons> section<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; proceeds to payment | medium |
| TC-016 (boundary) |  | Attempt to add one more entry to Add Ons |  | 1. Add <maximum allowed entries + 1> to the <Add_Ons> section<br>2. Fill all other required fields<br>3. Click Confirm Booking | Add_Ons displays an error indicating the maximum number of entries has been exceeded | medium |
| TC-017 (input_edge) |  | Enter long text in Driver Full Name |  | 1. Enter a very long string (200+ characters) in the <Driver_Full_Name> field<br>2. Fill all other required fields<br>3. Click Confirm Booking | Form submits successfully; the saved value shows the long name correctly | low |
| TC-018 (input_edge) |  | Enter special characters in License Number |  | 1. Enter special characters in the <License_Number> field<br>2. Fill all other required fields<br>3. Click Confirm Booking | <License_Number> displays an error indicating invalid characters | low |

---

## Visa Services

Total: **17** (positive: 3, negative: 6, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View visa requirements for selected nationality and destination country | User logged in as <User> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Click 'View Requirements' | Visa requirements for <valid nationality> traveling to <valid destination country> are displayed, including visa type, processing time, required documents, and fees. | high |
| TC-002 |  | Submit visa application with valid data | User logged in as <User> | 1. Click on 'Apply for Visa'<br>2. Enter <full name> in the Full Name field<br>3. Enter <passport number> in the Passport Number field<br>4. Enter <valid expiry date> in the Passport Expiry Date field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Select <valid nationality> from the Nationality dropdown<br>7. Enter <valid email> in the Email field<br>8. Enter <valid phone number> in the Phone field<br>9. Enter <purpose of visit> in the Purpose of Visit field<br>10. Enter <valid intended travel dates> in the Intended Travel Dates field<br>11. Enter <duration of stay> in the Duration of Stay field<br>12. Upload a valid document in the Document Upload section<br>13. Click 'Submit Application' | A success notification is displayed; the application is submitted successfully. | high |
| TC-003 |  | Track application status after submission | User logged in as <User>, Application has been submitted | 1. Click on 'Track Application Status' | The application status is displayed, showing the current status of the visa application. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Select a valid Destination Country<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-005 |  | Leave the Destination Country dropdown blank and submit |  | 1. Select a valid Nationality<br>2. Leave the Destination Country dropdown blank<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-006 |  | Leave all required fields in the Visa Application Form blank and submit |  | 1. Leave the Full Name field blank<br>2. Leave the Passport Number field blank<br>3. Leave the Passport Expiry Date field blank<br>4. Leave the Date of Birth field blank<br>5. Leave the Nationality dropdown blank<br>6. Leave the Email field blank<br>7. Leave the Phone field blank<br>8. Leave the Purpose of Visit field blank<br>9. Leave the Intended Travel Dates field blank<br>10. Leave the Duration of Stay field blank<br>11. Leave the Document Upload field blank<br>12. Click Submit | Form does not submit; error shown on Full Name, Passport Number, Passport Expiry Date, Date of Birth, Nationality, Email, Phone, Purpose of Visit, Intended Travel Dates, Duration of Stay, and Document Upload fields | high |
| TC-007 |  | Enter an invalid email format in the Email field |  | 1. Fill all other required fields with valid data<br>2. Enter <invalid email format> in the Email field<br>3. Click Submit | Email field displays an error: 'Must be a valid email address' | medium |
| TC-008 |  | Enter a past date in the Passport Expiry Date field |  | 1. Fill all other required fields with valid data<br>2. Enter <past date> in the Passport Expiry Date field<br>3. Click Submit | Passport Expiry Date field displays an error: 'Expiry date must be in the future' | medium |
| TC-009 |  | Leave the Document Upload field empty and submit |  | 1. Fill all other required fields with valid data<br>2. Leave the Document Upload field blank<br>3. Click Submit | Inline validation error appears on the Document Upload field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) |  | Enter a valid Passport Expiry Date as today | User is on the Visa Application Form | 1. Enter today's date in the Passport Expiry Date field | Form submits successfully; entity is created with today's date in the Passport Expiry Date field | medium |
| TC-011 (boundary) |  | Enter a Passport Expiry Date as yesterday | User is on the Visa Application Form | 1. Enter yesterday's date in the Passport Expiry Date field | Passport Expiry Date displays an error indicating the date must be in the future | medium |
| TC-012 (boundary) |  | Enter a valid Intended Travel Dates as today | User is on the Visa Application Form | 1. Enter today's date in the Intended Travel Dates field | Form submits successfully; entity is created with today's date in the Intended Travel Dates field | medium |
| TC-013 (boundary) |  | Enter a Intended Travel Dates as yesterday | User is on the Visa Application Form | 1. Enter yesterday's date in the Intended Travel Dates field | Intended Travel Dates displays an error indicating the date must be in the future | medium |
| TC-014 (data_edge) |  | Upload a file exactly at the maximum size limit | User is on the Visa Application Form | 1. Upload a file that is exactly at the maximum size limit for Document Upload | File upload succeeds with a visible success indicator | medium |
| TC-015 (data_edge) |  | Upload a file that exceeds the maximum size limit | User is on the Visa Application Form | 1. Upload a file that is one unit over the maximum size limit for Document Upload | File upload is blocked; error shown indicating the file size exceeds the limit | medium |
| TC-016 (input_edge) |  | Enter a very long Full Name | User is on the Visa Application Form | 1. Enter a string longer than 200 characters in the Full Name field | Full Name field displays an error indicating the input exceeds the maximum allowed length | low |
| TC-017 (input_edge) |  | Enter a special character in the Phone field | User is on the Visa Application Form | 1. Enter a string with special characters in the Phone field | Phone field displays an error indicating invalid characters | low |

---

## User Dashboard

Total: **20** (positive: 10, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | View Booking Details | User logged in as <User>, User has at least one booking | 1. Navigate to My Bookings section<br>2. Click View Details on a booking row | Booking details are displayed for the selected booking | high |
| TC-002 | WF-001 | Cancel a Booking | User logged in as <User>, User has a booking with cancellation policy permitting cancellation | 1. Navigate to My Bookings section<br>2. Click Cancel on a booking row | The booking status updates to 'Cancelled' and a success notification is displayed | high |
| TC-003 | WF-002 | Modify a Booking | User logged in as <User>, User has a booking with modification policy permitting modification | 1. Navigate to My Bookings section<br>2. Click Modify on a booking row | The modification form for the booking is displayed | high |
| TC-004 |  | Download Confirmation | User logged in as <User>, User has a booking | 1. Navigate to My Bookings section<br>2. Click Confirmations under Download Options on a booking row | The confirmation file download is triggered in the browser | medium |
| TC-005 |  | Edit Profile Information | User logged in as <User> | 1. Navigate to My Profile section<br>2. Click Edit | The profile edit form is displayed | medium |
| TC-006 |  | View Wallet Credits | User logged in as <User> | 1. Navigate to Wallet Credits section | Available credit balance and transaction history are displayed | medium |
| TC-007 |  | View Wishlist | User logged in as <User> | 1. Navigate to Wishlist section | Saved items are displayed in the Wishlist | medium |
| TC-008 |  | Submit a Review | User logged in as <User>, User has completed a booking | 1. Navigate to Reviews section<br>2. Enter a rating and review<br>3. Click Submit | The review is submitted successfully and displayed in the Reviews section | medium |
| TC-009 |  | Change Notification Preferences | User logged in as <User> | 1. Navigate to Settings section<br>2. Change Notification Preferences<br>3. Click Save | Notification preferences are updated successfully and a success message is displayed | medium |
| TC-010 |  | Logout from Dashboard | User logged in as <User> | 1. Click Logout button | User is logged out and redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Attempt to cancel a booking when cancellation policy does not permit | Booking type and cancellation policy do not permit cancellation | 1. Navigate to My Bookings<br>2. Click on Cancel for a booking | Cancellation action is blocked; no cancellation occurs; an error message is displayed indicating cancellation is not permitted. | high |
| TC-012 |  | Attempt to modify a booking when cancellation policy does not permit | Booking type and cancellation policy do not permit modification | 1. Navigate to My Bookings<br>2. Click on Modify for a booking | Modification action is blocked; no modification occurs; an error message is displayed indicating modification is not permitted. | high |
| TC-013 |  | Leave the Personal Information field blank and submit |  | 1. Navigate to My Profile<br>2. Leave the Personal Information field blank<br>3. Click Edit | Inline validation error appears on the Personal Information field indicating it is required. | high |
| TC-014 |  | Leave the Rating field blank and submit a review |  | 1. Navigate to Reviews<br>2. Leave the Rating field blank<br>3. Fill in the Review field<br>4. Click Submit | Inline validation error appears on the Rating field indicating it is required. | high |
| TC-015 |  | Leave the Review field blank and submit a review |  | 1. Navigate to Reviews<br>2. Fill in the Rating field<br>3. Leave the Review field blank<br>4. Click Submit | Inline validation error appears on the Review field indicating it is required. | high |
| TC-016 |  | Attempt to logout without being logged in | User is not logged in | 1. Attempt to click Logout | Logout action is blocked; user remains on the current page; no logout occurs. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (input_edge) |  | Enter a long string in the Personal Information field | User is on the My Profile section | 1. Click on the Edit button<br>2. Enter a string of 200+ characters in the Personal Information field | Input is accepted or truncated with a visible indicator | low |
| TC-018 (input_edge) |  | Enter special characters in the Review field | User is on the Reviews section | 1. Enter special characters in the Review field | Input is accepted or a specific error is shown | low |
| TC-019 (input_edge) |  | Enter leading/trailing whitespace in the Change Password field | User is on the Settings section | 1. Enter a value with leading and trailing spaces in the Change Password field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-020 (input_edge) |  | Enter zero in the Rating field | User is on the Reviews section | 1. Enter '0' in the Rating field | Form submits successfully and the saved record displays '0' | medium |

---

## Booking Management

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Modify booking details successfully | User logged in as <User>, Booking type and cancellation policy permit modification | 1. Click the Modify button<br>2. Change the travel dates<br>3. Add special requests<br>4. Update traveler information<br>5. Click Save | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 |  | Open cancellation confirmation flow | User logged in as <User>, User must explicitly confirm | 1. Click the Cancel button | opens cancellation confirmation flow | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Attempt to modify booking without meeting preconditions | booking type and cancellation policy do not permit modification | 1. Click on the Modify button | Modification action is blocked; no changes are made to the booking | high |
| TC-004 |  | Attempt to cancel booking without explicit confirmation |  | 1. Click on the Cancel button | Cancellation confirmation flow does not proceed; cancellation is not processed | high |
| TC-005 |  | Attempt to modify booking while availability is not met | booking type and cancellation policy permit modification | 1. Click on the Modify button | Modification action is blocked; no changes are made to the booking due to unavailability | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long string in the Full Service Information field |  | 1. Navigate to the Booking Detail View<br>2. Enter a string of 200+ characters in the Full Service Information field | The system accepts the input and displays the full string in the detail view | low |
| TC-007 (input_edge) |  | Enter special characters in the Traveler Details field |  | 1. Navigate to the Booking Detail View<br>2. Enter special characters in the Traveler Details field | The system accepts the input and displays the special characters in the detail view | low |
| TC-008 (input_edge) |  | Enter a value with leading and trailing whitespace in the Confirmation Number field |  | 1. Navigate to the Booking Detail View<br>2. Enter a value with leading and trailing spaces in the Confirmation Number field | Leading/trailing whitespace is trimmed; saved value shown in the detail view has no extra spaces | low |

---

## Payment Processing

Total: **20** (positive: 5, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit payment using Credit/Debit Card | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Credit/Debit Card' from the Payment Method dropdown<br>2. Enter <Cardholder Name> in the Cardholder Name field<br>3. Enter <valid card number> in the Card Number field<br>4. Enter <valid expiration date> in the Expiration Date field<br>5. Enter <valid CVV> in the CVV field<br>6. Click 'Submit Payment' | redirects to booking confirmation page with reference number | high |
| TC-002 |  | Submit payment using PayPal | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'PayPal' from the Payment Method dropdown<br>2. Click 'Submit Payment' | redirects to booking confirmation page with reference number | high |
| TC-003 |  | Submit payment using Bank Transfer | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Bank Transfer' from the Payment Method dropdown<br>2. Click 'Submit Payment' | redirects to booking confirmation page with reference number | high |
| TC-004 |  | Submit payment using Wallet/Credits | User logged in as <Customer>, Booking summary is displayed with price breakdown | 1. Select 'Wallet/Credits' from the Payment Method dropdown<br>2. Click 'Submit Payment' | redirects to booking confirmation page with reference number | high |
| TC-005 |  | Retry payment after failure | User logged in as <Customer>, Booking summary is displayed with price breakdown, Previous payment attempt has failed | 1. Click 'Retry Payment' | allows user to retry payment without losing booking details | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Leave Payment_Method blank and submit |  | 1. Leave the Payment_Method field blank<br>2. Fill all other required fields<br>3. Click Submit Payment | Inline validation error appears on the Payment_Method field indicating it is required | high |
| TC-007 |  | Leave Cardholder_Name blank when Credit/Debit Card is selected |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Cardholder_Name field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-008 |  | Leave Card_Number blank when Credit/Debit Card is selected |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Card_Number field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-009 |  | Leave Expiration_Date blank when Credit/Debit Card is selected |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the Expiration_Date field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-010 |  | Leave CVV blank when Credit/Debit Card is selected |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Leave the CVV field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the CVV field indicating it is required | high |
| TC-011 |  | Enter non-numeric value in Card_Number field |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <non-numeric value> in the Card_Number field<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it must be a number | medium |
| TC-012 |  | Enter invalid date in Expiration_Date field |  | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <invalid date> in the Expiration_Date field<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it must be a valid date | medium |
| TC-013 |  | Attempt to submit payment without selecting a payment method |  | 1. Leave the Payment_Method dropdown unselected<br>2. Fill all other required fields<br>3. Click Submit Payment | Form does not submit; Payment_Method is highlighted and an error is shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) |  | Enter valid card number (exactly 16 digits) | Select 'Credit/Debit Card' as Payment Method | 1. Enter a valid 16-digit card number in the Card_Number field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-015 (boundary) |  | Enter card number with 15 digits (one unit below valid) | Select 'Credit/Debit Card' as Payment Method | 1. Enter a 15-digit card number in the Card_Number field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displayed indicating 'Invalid card number' | medium |
| TC-016 (boundary) |  | Enter a valid expiration date (today's date) | Select 'Credit/Debit Card' as Payment Method | 1. Enter today's date in the Expiration_Date field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-017 (boundary) |  | Enter an expiration date from yesterday (one unit below valid) | Select 'Credit/Debit Card' as Payment Method | 1. Enter yesterday's date in the Expiration_Date field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displayed indicating 'Card has expired' | medium |
| TC-018 (input_edge) |  | Enter a very long cardholder name | Select 'Credit/Debit Card' as Payment Method | 1. Enter a cardholder name with 200+ characters in the Cardholder_Name field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displayed indicating 'Name exceeds maximum length' | low |
| TC-019 (input_edge) |  | Enter a card number with special characters | Select 'Credit/Debit Card' as Payment Method | 1. Enter '1234-5678-9012-3456' in the Card_Number field<br>2. Fill in all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displayed indicating 'Invalid card number' | low |
| TC-020 (interaction_edge) |  | Rapid re-submission after successful payment | Payment is successfully processed | 1. Click Submit Payment<br>2. After redirection to the booking confirmation page, press the browser back button | The payment form is shown blank; no second payment is processed | medium |

---

## Currency & Language Selection

Total: **13** (positive: 8, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Select USD as the currency | User logged in as <Authenticated User> | 1. Select 'USD' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-002 |  | Select EUR as the currency | User logged in as <Authenticated User> | 1. Select 'EUR' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-003 |  | Select GBP as the currency | User logged in as <Authenticated User> | 1. Select 'GBP' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-004 |  | Select JPY as the currency | User logged in as <Authenticated User> | 1. Select 'JPY' from the Currency dropdown | All prices displayed across the site update in real-time | high |
| TC-005 |  | Select English as the language | User logged in as <Authenticated User> | 1. Select 'English' from the Language dropdown | The entire site interface switches to English | high |
| TC-006 |  | Select Arabic as the language | User logged in as <Authenticated User> | 1. Select 'Arabic' from the Language dropdown | The entire site interface switches to Arabic | high |
| TC-007 |  | Select Spanish as the language | User logged in as <Authenticated User> | 1. Select 'Spanish' from the Language dropdown | The entire site interface switches to Spanish | high |
| TC-008 |  | Select French as the language | User logged in as <Authenticated User> | 1. Select 'French' from the Language dropdown | The entire site interface switches to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to select a currency when no selection is made |  | 1. Leave the Currency Selector dropdown blank<br>2. Click to submit the selection | Form does not submit; Currency Selector is highlighted indicating a selection is required | high |
| TC-010 |  | Attempt to select a language when no selection is made |  | 1. Leave the Language Selector dropdown blank<br>2. Click to submit the selection | Form does not submit; Language Selector is highlighted indicating a selection is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Select a currency option from the dropdown |  | 1. Open the Currency Selector dropdown<br>2. Select 'USD' from the options | All prices displayed across the site update in real-time to reflect the selected currency | medium |
| TC-012 (input_edge) |  | Select a language option from the dropdown |  | 1. Open the Language Selector dropdown<br>2. Select 'Spanish' from the options | The entire site interface switches to Spanish, including navigation labels and content | medium |
| TC-013 (input_edge) |  | Test special characters in language selection |  | 1. Open the Language Selector dropdown<br>2. Enter special characters in the search field (e.g., '@#$%') | The dropdown remains functional; no error is shown, and the user can still select a language | low |

---

## Search & Filters

Total: **15** (positive: 8, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Apply price range filter | User logged in as <User Role> | 1. Adjust the Price Range slider to the desired range | The results grid updates dynamically to show listings within the selected price range; the Dynamic Result Count displays the number of matching listings. | high |
| TC-002 |  | Select star ratings filter | User logged in as <User Role> | 1. Check the '4 Stars' checkbox under Star Ratings | The results grid updates dynamically to show listings with 4-star ratings; the Dynamic Result Count displays the number of matching listings. | high |
| TC-003 |  | Remove a specific active filter | User logged in as <User Role>, At least one filter is active | 1. Click the remove button next to an active filter | The results grid updates dynamically to reflect the removal of the filter; the Dynamic Result Count updates accordingly. | medium |
| TC-004 |  | Reset all filters | User logged in as <User Role>, At least one filter is active | 1. Click the Reset All Filters button | All filters are cleared; the results grid displays all available listings; the Dynamic Result Count shows the total number of listings. | high |
| TC-005 |  | Switch to Hotels tab and apply filters | User logged in as <User Role> | 1. Click on the Hotels tab<br>2. Check the 'Facilities/Amenities' checkbox<br>3. Select a value from the Hotel Type dropdown | The results grid updates dynamically to show hotel listings that match the selected filters; the Dynamic Result Count displays the number of matching listings. | high |
| TC-006 |  | Switch to Flights tab and apply filters | User logged in as <User Role> | 1. Click on the Flights tab<br>2. Check the 'Airlines' checkbox<br>3. Adjust the Departure Time Range slider | The results grid updates dynamically to show flight listings that match the selected filters; the Dynamic Result Count displays the number of matching listings. | high |
| TC-007 |  | Switch to Tours tab and apply filters | User logged in as <User Role> | 1. Click on the Tours tab<br>2. Select a value from the Tour Type dropdown<br>3. Adjust the Duration slider | The results grid updates dynamically to show tour listings that match the selected filters; the Dynamic Result Count displays the number of matching listings. | high |
| TC-008 |  | Switch to Cars tab and apply filters | User logged in as <User Role> | 1. Click on the Cars tab<br>2. Select a value from the Car Type dropdown<br>3. Select a value from the Transmission dropdown | The results grid updates dynamically to show car listings that match the selected filters; the Dynamic Result Count displays the number of matching listings. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to apply filters without any selections |  | 1. Leave all filter options unselected<br>2. Click on the Apply Filters button | No filters are applied; the results remain unchanged and the Active Filters section displays 'No active filters' | high |
| TC-010 |  | Attempt to reset filters when no filters are applied |  | 1. Ensure no filters are currently applied<br>2. Click on the Reset All Filters button | No action occurs; the Active Filters section remains unchanged and displays 'No active filters' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) |  | Test Price Range slider at minimum value |  | 1. Set the Price Range slider to the minimum value | Price Range slider accepts the minimum value and updates the results accordingly | medium |
| TC-012 (boundary) |  | Test Price Range slider at maximum value |  | 1. Set the Price Range slider to the maximum value | Price Range slider accepts the maximum value and updates the results accordingly | medium |
| TC-013 (input_edge) |  | Enter a long string in dropdown fields |  | 1. Open the Hotel Type dropdown<br>2. Enter a string longer than the maximum allowed length | Dropdown field shows an error indicating the input exceeds the maximum length | low |
| TC-014 (input_edge) |  | Enter special characters in dropdown fields |  | 1. Open the Fuel Policy dropdown<br>2. Enter special characters | Dropdown field shows an error indicating invalid characters | low |
| TC-015 (interaction_edge) |  | Rapidly adjust filters and observe results |  | 1. Set a filter for Hotels<br>2. Quickly change the filter for Flights<br>3. Observe the results | Results update dynamically without delay, reflecting the latest filter settings | medium |

---

## Reviews & Ratings

Total: **15** (positive: 4, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Submit a review successfully | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter <Overall Experience Rating> in the Overall Experience Rating field<br>3. Enter <Cleanliness Rating> in the Cleanliness field<br>4. Enter <Service Rating> in the Service field<br>5. Enter <Location Rating> in the Location field<br>6. Enter <Written Feedback> in the Written Feedback field<br>7. Click Submit Review | A success notification is displayed; the message 'review submitted' is shown | high |
| TC-002 |  | Filter reviews by rating | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Detail Page Reviews Section<br>2. Select <Rating_Filter> from the Rating Filter dropdown<br>3. Click Apply Filter | Only reviews with the selected rating are displayed; unrelated reviews are no longer visible | medium |
| TC-003 |  | Filter reviews by date | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Detail Page Reviews Section<br>2. Select <Date_Filter> from the Date Filter dropdown<br>3. Click Apply Filter | Only reviews from the selected date range are displayed; unrelated reviews are no longer visible | medium |
| TC-004 |  | Filter reviews by traveler type | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Detail Page Reviews Section<br>2. Select <Traveler_Type_Filter> from the Traveler Type Filter dropdown<br>3. Click Apply Filter | Only reviews from the selected traveler type are displayed; unrelated reviews are no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Overall Experience Rating blank and submit review | user is authenticated, user has completed a booking | 1. Leave the Overall Experience Rating field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Form does not submit; Overall Experience Rating is highlighted with an error indicating it is required | high |
| TC-006 |  | Leave Written Feedback blank and submit review | user is authenticated, user has completed a booking | 1. Leave the Written Feedback field blank<br>2. Fill in all other required fields<br>3. Click Submit Review | Form does not submit; Written Feedback is highlighted with an error indicating it is required | high |
| TC-007 |  | Attempt to submit review without authentication | user is not authenticated | 1. Fill in all required fields<br>2. Click Submit Review | Form does not submit; user is redirected to the login page | high |
| TC-008 |  | Attempt to submit review without completing a booking | user is authenticated, user has not completed a booking | 1. Fill in all required fields<br>2. Click Submit Review | Form does not submit; error message indicating booking completion is required is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) |  | Add maximum allowed entries to Individual Reviews | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Add exactly <maximum allowed entries> reviews in the Individual Reviews section | Form submits successfully; all <maximum allowed entries> reviews are saved. | medium |
| TC-010 (boundary) |  | Attempt to add one more review than allowed | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Add exactly <maximum allowed entries> reviews in the Individual Reviews section<br>3. Attempt to add one more review | Submission is blocked; visible error indicates the maximum number of reviews has been reached. | medium |
| TC-011 (data_edge) |  | Enter today's date in Stay_Date field | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter today's date in the Stay_Date field | Form submits successfully; Stay_Date is recorded as today's date. | medium |
| TC-012 (data_edge) |  | Enter a date in Stay_Date field that is in the future | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter a date in the Stay_Date field that is in the future | Submission is blocked; visible error indicates the stay date cannot be in the future. | medium |
| TC-013 (input_edge) |  | Enter a very long string in Written_Feedback field | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter a string of 200+ characters in the Written_Feedback field | Form submits successfully; feedback is saved correctly or truncated with a visible indicator. | low |
| TC-014 (input_edge) |  | Enter special characters in Reviewer_Name field | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter special characters in the Reviewer_Name field | Form submits successfully; Reviewer_Name is saved correctly or an error is shown. | low |
| TC-015 (input_edge) |  | Enter a value with leading/trailing whitespace in Written_Feedback field | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter a value with leading and trailing spaces in the Written_Feedback field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Offers & Deals

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User subscribes to the newsletter with a valid email | User logged in as <User> | 1. Enter <valid email> in the Newsletter Subscription field<br>2. Click 'Submit' | The page shows 'Thank you for subscribing to our newsletter!' | high |
| TC-002 |  | User filters offers by service type | User logged in as <User> | 1. Select 'Hotels' from the Service Type Filter dropdown | Only hotel offers are displayed on the page; flight and package offers are no longer visible. | medium |
| TC-003 |  | User clicks Book Now button on a deal card | User logged in as <User> | 1. Click the Book Now button on a featured deal card | The page redirects to the booking flow with the promotional code applied. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Newsletter Subscription field blank and submit |  | 1. Leave the Newsletter Subscription field blank<br>2. Click the Book Now button | Inline validation error appears on the Newsletter Subscription field indicating it is required | high |
| TC-005 |  | Enter an invalid email format in the Newsletter Subscription field |  | 1. Enter <invalid email format> in the Newsletter Subscription field<br>2. Click the Book Now button | Newsletter Subscription field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Enter a very long email address in the Newsletter Subscription field |  | 1. Enter a string of 200 characters in the Newsletter Subscription field | Form displays an error indicating the email address is too long | low |
| TC-007 (input_edge) |  | Enter special characters in the Newsletter Subscription field |  | 1. Enter 'user!@example.com' in the Newsletter Subscription field | Form submits successfully; the email is accepted without error | low |
| TC-008 (input_edge) |  | Enter an email with leading and trailing whitespace in the Newsletter Subscription field |  | 1. Enter '   user@example.com   ' in the Newsletter Subscription field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | User successfully logs out | User logged in as <User Role> | 1. Click Logout button | redirects the user to the home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to access a protected page after logout |  | 1. Click the Logout button | User is redirected to the login page when attempting to access a protected page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) |  | Rapid logout attempts | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is ignored; user remains on the home page | low |
| TC-004 (interaction_edge) |  | Access protected page after logout | User is logged in, User clicks Logout | 1. Click the Logout button<br>2. Attempt to navigate to a protected page | User is redirected to the login page | medium |

---
