# Test Cases — Phptravels

Generated: 2026-06-09T11:00:56.556178Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 315 | 56 | 149 | 110 | 176 | 96 | 36 |

## Home Page & Search

Total: **28** (positive: 4, negative: 16, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Hotels with valid inputs | User logged in as <Role> | 1. Click on the 'Hotels' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check In Date field<br>4. Enter <valid check-out date> in the Check Out Date field<br>5. Enter <valid number of rooms> in the Number of Rooms field<br>6. Enter <valid number of adults> in the Adults field<br>7. Optionally, enter <valid number of children> in the Children field<br>8. Click the Search Button | redirects to the corresponding results listing page | high |
| TC-002 | WF-002 | Search for Flights with valid inputs | User logged in as <Role> | 1. Click on the 'Flights' tab<br>2. Select 'Round-trip' from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Enter <valid departure date> in the Departure Date field<br>6. Optionally, enter <valid return date> in the Return Date field<br>7. Enter <valid number of adults> in the Adults field<br>8. Optionally, enter <valid number of children> in the Children field<br>9. Optionally, enter <valid number of infants> in the Infants field<br>10. Select 'Economy' from the Cabin Class dropdown<br>11. Click the Search Button | redirects to the corresponding results listing page | high |
| TC-003 | WF-003 | Search for Tours with valid inputs | User logged in as <Role> | 1. Click on the 'Tours' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid start date> in the Start Date field<br>4. Enter <valid end date> in the End Date field<br>5. Click the Search Button | redirects to the corresponding results listing page | high |
| TC-004 | WF-004 | Search for Cars with valid inputs | User logged in as <Role> | 1. Click on the 'Cars' tab<br>2. Enter <valid pick-up location> in the Pick Up Location field<br>3. Enter <valid drop-off location> in the Drop Off Location field<br>4. Enter <valid pick-up date and time> in the Pick Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop Off Date Time field<br>6. Click the Search Button | redirects to the corresponding results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Destination field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill in Check_In_Date, Check_Out_Date, Number_of_Rooms, Adults, and Children<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 | WF-001 | Leave the Check_In_Date field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Check_In_Date field blank<br>3. Fill in Destination, Check_Out_Date, Number_of_Rooms, Adults, and Children<br>4. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-007 | WF-001 | Leave the Check_Out_Date field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Check_Out_Date field blank<br>3. Fill in Destination, Check_In_Date, Number_of_Rooms, Adults, and Children<br>4. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-008 | WF-001 | Leave the Number_of_Rooms field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Number_of_Rooms field blank<br>3. Fill in Destination, Check_In_Date, Check_Out_Date, Adults, and Children<br>4. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-009 | WF-001 | Leave the Adults field blank and submit |  | 1. Click on the Hotels tab<br>2. Fill in Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and leave Adults blank<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-010 | WF-002 | Leave the Trip_Type field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Trip_Type field blank<br>3. Fill in Departure_City, Arrival_City, Departure_Date, Adults, and Children<br>4. Click Search | Inline validation error appears on the Trip_Type field indicating it is required | high |
| TC-011 | WF-002 | Leave the Departure_City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure_City field blank<br>3. Fill in Trip_Type, Arrival_City, Departure_Date, Adults, and Children<br>4. Click Search | Inline validation error appears on the Departure_City field indicating it is required | high |
| TC-012 | WF-002 | Leave the Arrival_City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Arrival_City field blank<br>3. Fill in Trip_Type, Departure_City, Departure_Date, Adults, and Children<br>4. Click Search | Inline validation error appears on the Arrival_City field indicating it is required | high |
| TC-013 | WF-002 | Leave the Departure_Date field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure_Date field blank<br>3. Fill in Trip_Type, Departure_City, Arrival_City, Adults, and Children<br>4. Click Search | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-014 | WF-003 | Leave the Destination field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Destination field blank<br>3. Fill in Start_Date and End_Date<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-015 | WF-003 | Leave the Start_Date field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Start_Date field blank<br>3. Fill in Destination and End_Date<br>4. Click Search | Inline validation error appears on the Start_Date field indicating it is required | high |
| TC-016 | WF-003 | Leave the End_Date field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the End_Date field blank<br>3. Fill in Destination and Start_Date<br>4. Click Search | Inline validation error appears on the End_Date field indicating it is required | high |
| TC-017 | WF-004 | Leave the Pick_Up_Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick_Up_Location field blank<br>3. Fill in Drop_Off_Location, Pick_Up_Date_Time, and Drop_Off_Date_Time<br>4. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-018 | WF-004 | Leave the Drop_Off_Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Drop_Off_Location field blank<br>3. Fill in Pick_Up_Location, Pick_Up_Date_Time, and Drop_Off_Date_Time<br>4. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-019 | WF-004 | Leave the Pick_Up_Date_Time field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick_Up_Date_Time field blank<br>3. Fill in Pick_Up_Location, Drop_Off_Location, and Drop_Off_Date_Time<br>4. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-020 | WF-004 | Leave the Drop_Off_Date_Time field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Drop_Off_Date_Time field blank<br>3. Fill in Pick_Up_Location, Drop_Off_Location, and Pick_Up_Date_Time<br>4. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Check-in date is the same as check-out date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Set Check_In_Date to today's date<br>3. Set Check_Out_Date to today's date<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Search succeeds and redirects to the corresponding results listing page | medium |
| TC-022 (boundary) | WF-001 | Check-out date is one day before check-in date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Set Check_In_Date to tomorrow's date<br>3. Set Check_Out_Date to today's date<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Inline error shown for Check-Out Date indicating it must be after Check-In Date | medium |
| TC-023 (boundary) | WF-002 | Departure date is the same as return date | User is on the Flights tab | 1. Select 'One-way' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Set Departure_Date to today's date<br>5. Set Return_Date to today's date<br>6. Enter a valid number in the Adults field | Search succeeds and redirects to the corresponding results listing page | medium |
| TC-024 (boundary) | WF-002 | Return date is one day before departure date | User is on the Flights tab | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter a valid Departure_City<br>3. Enter a valid Arrival_City<br>4. Set Departure_Date to tomorrow's date<br>5. Set Return_Date to today's date<br>6. Enter a valid number in the Adults field | Inline error shown for Return Date indicating it must be after Departure Date | medium |
| TC-025 (boundary) | WF-003 | Start date is the same as end date for tours | User is on the Tours tab | 1. Enter a valid Destination<br>2. Set Start_Date to today's date<br>3. Set End_Date to today's date | Search succeeds and redirects to the corresponding results listing page | medium |
| TC-026 (boundary) | WF-003 | End date is one day before start date for tours | User is on the Tours tab | 1. Enter a valid Destination<br>2. Set Start_Date to tomorrow's date<br>3. Set End_Date to today's date | Inline error shown for End Date indicating it must be after Start Date | medium |
| TC-027 (boundary) | WF-004 | Pick-up date and time is the same as drop-off date and time | User is on the Cars tab | 1. Enter a valid Pick_Up_Location<br>2. Enter a valid Drop_Off_Location<br>3. Set Pick_Up_Date_Time to today's date and current time<br>4. Set Drop_Off_Date_Time to today's date and current time | Search succeeds and redirects to the corresponding results listing page | medium |
| TC-028 (boundary) | WF-004 | Drop-off date and time is one minute before pick-up date and time | User is on the Cars tab | 1. Enter a valid Pick_Up_Location<br>2. Enter a valid Drop_Off_Location<br>3. Set Pick_Up_Date_Time to tomorrow's date and current time<br>4. Set Drop_Off_Date_Time to today's date and current time | Inline error shown for Drop-Off Date indicating it must be after Pick-Up Date | medium |

---

## User Registration

Total: **20** (positive: 1, negative: 14, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit registration form with all required fields filled | User logged in as <Role> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Password> in the Password field<br>5. Enter <Password> in the Confirm Password field<br>6. Enter <Mobile Number> in the Mobile Number field<br>7. Select <Country Code> from the Country Code dropdown<br>8. Enter <Address> in the Address field<br>9. Enter <Country> in the Country field<br>10. Check the Terms and Conditions checkbox<br>11. Click Submit | creates account and redirects to dashboard or prompts for email verification | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Leave the Confirm Password field blank and submit |  | 1. Leave the Confirm_Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm_Password field indicating it is required | high |
| TC-007 |  | Leave the Mobile Number field blank and submit |  | 1. Leave the Mobile_Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mobile_Number field indicating it is required | high |
| TC-008 |  | Leave the Country Code field blank and submit |  | 1. Leave the Country_Code field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Country_Code field indicating it is required | high |
| TC-009 |  | Leave the Address field blank and submit |  | 1. Leave the Address field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Address field indicating it is required | high |
| TC-010 |  | Leave the Country field blank and submit |  | 1. Leave the Country field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Country field indicating it is required | high |
| TC-011 |  | Leave the Terms and Conditions checkbox unchecked and submit |  | 1. Leave the Terms_and_Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Terms_and_Conditions field indicating it is required | high |
| TC-012 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Submit | Inline validation error appears on the First_Name, Last_Name, Email, Password, Confirm_Password, Mobile_Number, Country_Code, Address, Country, and Terms_and_Conditions fields indicating they are required | high |
| TC-013 |  | Enter an invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email format | medium |
| TC-014 |  | Enter mismatched passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Confirm_Password field indicating it must match Password | medium |
| TC-015 |  | Enter a duplicate email and submit |  | 1. Enter <duplicate email> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be unique | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-001 | Submit with a valid email format that is unique |  | 1. Enter a valid unique email in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Account is created and user is redirected to the dashboard | medium |
| TC-017 (boundary) | WF-001 | Submit with an invalid email format |  | 1. Enter an invalid email format in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Field-level error appears inline indicating invalid email format | medium |
| TC-018 (input_edge) | WF-001 | Enter a very long First Name |  | 1. Enter a string longer than 200 characters in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Field-level error appears inline indicating the First Name is too long | low |
| TC-019 (input_edge) | WF-001 | Enter a special character in Last Name |  | 1. Enter a special character (e.g., @) in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Field-level error appears inline indicating invalid characters in Last Name | low |
| TC-020 (input_edge) | WF-001 | Enter leading/trailing whitespace in Mobile Number |  | 1. Enter leading and trailing spaces in the Mobile Number field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Mobile Number is trimmed; saved value shown in detail page has no extra spaces | low |

---

## User Login

Total: **14** (positive: 4, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <Role>, User is on the login page | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | redirects to dashboard or previous page | high |
| TC-002 | WF-003 | Social login with Google | User logged in as <Role>, User is on the login page, social login is enabled | 1. Click on Google login option | redirects to dashboard or previous page | medium |
| TC-003 | WF-004 | Social login with Facebook | User logged in as <Role>, User is on the login page, social login is enabled | 1. Click on Facebook login option | redirects to dashboard or previous page | medium |
| TC-004 | WF-005 | Login after multiple failed attempts requiring CAPTCHA | User logged in as <Role>, User is on the login page, multiple consecutive failed attempts occur | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login<br>4. Repeat steps 1-3 for multiple attempts<br>5. Enter <valid email> in the Email field<br>6. Enter <valid password> in the Password field<br>7. Click Login | redirects to dashboard or previous page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill in the Password field with a valid password<br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-006 |  | Leave the Password field blank and submit |  | 1. Fill in the Email field with a valid email address<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill in the Password field with a valid password<br>3. Click Login | Error message is shown indicating invalid credentials; Password field is cleared | medium |
| TC-008 |  | Submit with incorrect password |  | 1. Fill in the Email field with a valid email address<br>2. Enter <incorrect password> in the Password field<br>3. Click Login | Error message is shown indicating invalid credentials; Password field is cleared | medium |
| TC-009 | WF-005 | Attempt to login after multiple failed attempts without CAPTCHA |  | 1. Leave the Email field blank<br>2. Leave the Password field blank<br>3. Click Login | Error message is shown indicating invalid credentials; Password field is cleared | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-002 | Login with empty Email field |  | 1. Leave the Email field empty<br>2. Enter a valid password<br>3. Click Login | Error message is shown indicating that the Email field is required | medium |
| TC-011 (boundary) | WF-002 | Login with empty Password field |  | 1. Enter a valid email<br>2. Leave the Password field empty<br>3. Click Login | Error message is shown indicating that the Password field is required | medium |
| TC-012 (input_edge) | WF-003 | Login with very long email |  | 1. Enter a very long email address (over 254 characters) in the Email field<br>2. Enter a valid password<br>3. Click Login | Error message is shown indicating the email is invalid or exceeds character limit | low |
| TC-013 (interaction_edge) | WF-005 | Login after multiple failed attempts requiring CAPTCHA | multiple consecutive failed attempts have occurred | 1. Enter invalid credentials<br>2. Click Login<br>3. Enter invalid credentials again<br>4. Click Login<br>5. Enter invalid credentials again<br>6. Click Login | CAPTCHA verification is shown after multiple failed attempts | medium |
| TC-014 (input_edge) | WF-003 | Login with special characters in email |  | 1. Enter an email with special characters (e.g., '!#$%&'*+/=?^_`{|}~')<br>2. Enter a valid password<br>3. Click Login | Error message is shown indicating the email is invalid | low |

---

## Forgot Password

Total: **12** (positive: 2, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit email for password reset | User logged in as <User>, Email exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is displayed: 'sends reset link to email' | high |
| TC-002 | WF-002 | Change password after reset link | User navigates to the password reset page via reset link | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | User is redirected to the login page with a success message: 'password successfully changed' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Submit with empty email field |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 | WF-001 | Submit with non-existent email |  | 1. Enter <non-existent email> in the Email field<br>2. Click Reset Password | Form does not submit; error shown: 'email not found in the system'; Email field remains editable | high |
| TC-005 | WF-002 | Submit with empty new password field |  | 1. Leave the New Password field blank<br>2. Leave the Confirm Password field blank<br>3. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-006 | WF-002 | Submit with mismatched passwords |  | 1. Enter <valid password> in the New Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Change Password | Form does not submit; error shown: 'Passwords do not match'; New Password and Confirm Password fields remain editable | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Submit email that exists in the system |  | 1. Enter a valid email address that exists in the system in the Email field<br>2. Click Reset Password | Reset link is sent to the email; confirmation message is shown. | medium |
| TC-008 (boundary) | WF-001 | Submit email that does not exist in the system |  | 1. Enter an email address that does not exist in the system in the Email field<br>2. Click Reset Password | Error message 'email not found in the system' is shown; form remains editable. | medium |
| TC-009 (boundary) | WF-002 | Submit new password that meets the requirements |  | 1. Enter a valid new password in the New Password field<br>2. Enter the same password in the Confirm Password field<br>3. Click Change Password | Redirects to login page; message 'password successfully changed' is shown. | medium |
| TC-010 (boundary) | WF-002 | Submit new password and confirm with a different password |  | 1. Enter a valid new password in the New Password field<br>2. Enter a different password in the Confirm Password field<br>3. Click Change Password | Error message is shown; form remains editable. | medium |
| TC-011 (input_edge) |  | Enter long email address |  | 1. Enter a long email address (over 254 characters) in the Email field<br>2. Click Reset Password | Error message is shown indicating the email is invalid; form remains editable. | low |
| TC-012 (input_edge) |  | Enter email with special characters |  | 1. Enter an email address with special characters (e.g., '!#$%&'*+/=?^_`{|}~') in the Email field<br>2. Click Reset Password | Error message is shown indicating the email is invalid; form remains editable. | low |

---

## Hotels Search & Listing

Total: **15** (positive: 2, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for hotels with valid inputs | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <valid number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' to add guest count<br>6. Enter <valid number of adults> in the Adults field<br>7. Enter <valid number of children> in the Children field if applicable<br>8. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | Reset all filters in hotels listing | User logged in as <Role> | 1. Navigate to the hotels listing page<br>2. Click Reset all filters | Filters reset to default | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 |  | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-005 |  | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-006 |  | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-007 |  | Leave the Adults field blank in Guest_Count and submit |  | 1. Leave the Adults field blank in Guest_Count<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms with valid data<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave the Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields blank<br>2. Click Search | Form does not submit; error shown on Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields | high |
| TC-009 |  | Attempt to reset filters without any active filters |  | 1. Go to the Hotels Listing page<br>2. Click Reset all filters | No action occurs; filters remain unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Check-in date is the same as check-out date | User has entered a valid destination, User has selected a valid number of rooms, User has added at least one adult | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search succeeds and user is redirected to the listing page | medium |
| TC-011 (boundary) | WF-001 | Check-out date is one day before check-in date | User has entered a valid destination, User has selected a valid number of rooms, User has added at least one adult | 1. Enter a valid destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search is blocked; error displayed indicating check-out date must be after check-in date | medium |
| TC-012 (boundary) | WF-001 | Number of rooms is at minimum valid value | User has entered a valid destination, User has added at least one adult | 1. Enter a valid destination in the Destination field<br>2. Enter a valid date in the Check_In_Date field<br>3. Enter a valid date in the Check_Out_Date field<br>4. Enter 1 in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search succeeds and user is redirected to the listing page | medium |
| TC-013 (boundary) | WF-001 | Number of rooms exceeds maximum limit | User has entered a valid destination, User has added at least one adult | 1. Enter a valid destination in the Destination field<br>2. Enter a valid date in the Check_In_Date field<br>3. Enter a valid date in the Check_Out_Date field<br>4. Enter a number greater than the maximum allowed in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search is blocked; error displayed indicating the number of rooms exceeds the maximum allowed | medium |
| TC-014 (input_edge) |  | Enter a long destination string |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Enter a valid date in the Check_In_Date field<br>3. Enter a valid date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search is blocked; error displayed indicating the destination exceeds maximum length | low |
| TC-015 (input_edge) |  | Enter special characters in destination |  | 1. Enter special characters in the Destination field<br>2. Enter a valid date in the Check_In_Date field<br>3. Enter a valid date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click the Search button | Search is blocked; error displayed indicating invalid characters in the destination field | low |

---

## Hotel Details & Booking

Total: **16** (positive: 2, negative: 9, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Booking a hotel without special requests | User logged in as <Role> | 1. Select a hotel from the hotel list<br>2. Choose a room type<br>3. Enter <valid stay dates> in the Stay Dates field<br>4. Enter <valid guest count> in the Guest Count field<br>5. Enter <valid first name> in the First Name field<br>6. Enter <valid last name> in the Last Name field<br>7. Enter <valid email> in the Email field<br>8. Enter <valid phone number> in the Phone Number field<br>9. Click Book Now | User is redirected to the payment page | high |
| TC-002 | WF-002 | Booking a hotel with special requests | User logged in as <Role> | 1. Select a hotel from the hotel list<br>2. Choose a room type<br>3. Enter <valid stay dates> in the Stay Dates field<br>4. Enter <valid guest count> in the Guest Count field<br>5. Enter <valid first name> in the First Name field<br>6. Enter <valid last name> in the Last Name field<br>7. Enter <valid email> in the Email field<br>8. Enter <valid phone number> in the Phone Number field<br>9. Enter <optional special requests> in the Special Requests field<br>10. Click Book Now | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Selected Hotel field blank |  | 1. Leave the Selected Hotel field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Selected Hotel field indicating it is required | high |
| TC-004 |  | Leave the Room Type field blank |  | 1. Leave the Room Type field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Room Type field indicating it is required | high |
| TC-005 |  | Leave the Stay Dates field blank |  | 1. Leave the Stay Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay Dates field indicating it is required | high |
| TC-006 |  | Leave the Guest Count field blank |  | 1. Leave the Guest Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest Count field indicating it is required | high |
| TC-007 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First Name field indicating it is required | high |
| TC-008 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-009 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-010 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-011 |  | Attempt to book without being logged in |  | 1. Fill all required fields<br>2. Click Book Now | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Guest count at minimum valid value | User is logged in | 1. Select a hotel<br>2. Select a room type<br>3. Enter stay dates<br>4. Enter 1 in the Guest Count field<br>5. Fill First Name, Last Name, Email, and Phone Number<br>6. Click Book Now | Proceeds to payment page | medium |
| TC-013 (boundary) | WF-001 | Guest count one unit below minimum | User is logged in | 1. Select a hotel<br>2. Select a room type<br>3. Enter stay dates<br>4. Enter 0 in the Guest Count field<br>5. Fill First Name, Last Name, Email, and Phone Number<br>6. Click Book Now | Submission is blocked; error shown indicating that Guest Count must be at least 1 | medium |
| TC-014 (data_edge) | WF-001 | Stay dates set to today's date | User is logged in | 1. Select a hotel<br>2. Select a room type<br>3. Enter today's date in Stay Dates<br>4. Enter 1 in the Guest Count field<br>5. Fill First Name, Last Name, Email, and Phone Number<br>6. Click Book Now | Proceeds to payment page | medium |
| TC-015 (data_edge) | WF-001 | Stay dates set to a past date | User is logged in | 1. Select a hotel<br>2. Select a room type<br>3. Enter a past date in Stay Dates<br>4. Enter 1 in the Guest Count field<br>5. Fill First Name, Last Name, Email, and Phone Number<br>6. Click Book Now | Submission is blocked; error shown indicating that Stay Dates cannot be in the past | medium |
| TC-016 (input_edge) | WF-002 | Special requests with long text | User is logged in | 1. Select a hotel<br>2. Select a room type<br>3. Enter stay dates<br>4. Enter 1 in the Guest Count field<br>5. Fill First Name, Last Name, Email, and Phone Number<br>6. Enter a very long string (200+ characters) in Special Requests<br>7. Click Book Now | Proceeds to payment page; special requests are saved correctly | low |

---

## Flights Search & Listing

Total: **15** (positive: 2, negative: 8, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for flights with valid inputs | User logged in as <Role> | 1. Select 'Round-trip' from the Trip Type dropdown<br>2. Enter <valid departure city> in the Departure City field<br>3. Enter <valid arrival city> in the Arrival City field<br>4. Enter <valid travel dates> in the Travel Dates field<br>5. Click 'Add Row' in the Passenger Count section<br>6. Enter <number of adults> in the Adults field<br>7. Enter <number of children> in the Children field<br>8. Enter <number of infants> in the Infants field<br>9. Select 'Economy' from the Cabin Class dropdown<br>10. Click 'Search Flights' | User is redirected to the listing page | high |
| TC-002 | WF-002 | Select a flight result | User logged in as <Role>, User is on the listing page with flight results displayed | 1. Click 'Select' on the first flight result | Flight selected for booking | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Departure City blank |  | 1. Leave the Departure City field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Departure City field indicating it is required | high |
| TC-004 | WF-001 | Leave the Arrival City blank |  | 1. Leave the Arrival City field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Arrival City field indicating it is required | high |
| TC-005 | WF-001 | Leave the Travel Dates blank |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-006 | WF-001 | Leave the Passenger Count fields blank |  | 1. Leave all Passenger Count fields (Adults, Children, Infants) blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Adults field indicating it is required | high |
| TC-007 | WF-001 | Leave the Cabin Class blank |  | 1. Leave the Cabin Class field blank<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Cabin Class field indicating it is required | high |
| TC-008 | WF-001 | Submit with invalid date format in Travel Dates |  | 1. Enter <invalid date format> in the Travel Dates field<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Travel Dates field indicating it must be a valid date | medium |
| TC-009 | WF-001 | Submit with negative number in Passenger Count |  | 1. Enter <negative number> in the Adults field<br>2. Fill all other required fields<br>3. Click Search Flights | Inline validation error appears on the Adults field indicating it must be a non-negative number | medium |
| TC-010 | WF-001 | Select a flight when no results are displayed |  | 1. Click Select on a flight result when no results are displayed | No action occurs; no flight is selected | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Add maximum allowed entries for passenger count | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Add exactly the maximum number of entries for Adults, Children, and Infants in the Passenger_Count section<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click 'Search Flights' | User is redirected to the listing page with search results displayed | medium |
| TC-012 (boundary) | WF-001 | Attempt to add one more entry than maximum for passenger count | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter 'New York' in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Add one more entry than the maximum for Adults, Children, and Infants in the Passenger_Count section<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click 'Search Flights' | Submission is blocked; an error message indicates the maximum number of passengers has been exceeded | medium |
| TC-013 (input_edge) |  | Enter a very long string in the Departure_City field | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter a string longer than 200 characters in the Departure_City field<br>3. Enter 'Los Angeles' in the Arrival_City field<br>4. Enter today's date in the Travel_Dates field<br>5. Add one entry for Adults in the Passenger_Count section<br>6. Select 'Economy' from the Cabin_Class dropdown<br>7. Click 'Search Flights' | An error message is shown indicating the input exceeds the maximum allowed length | low |
| TC-014 (input_edge) |  | Enter special characters in the Arrival_City field | User is on the Flights Search Form | 1. Select 'Round-trip' from the Trip_Type dropdown<br>2. Enter '@#$%^&*()' in the Arrival_City field<br>3. Enter today's date in the Travel_Dates field<br>4. Add one entry for Adults in the Passenger_Count section<br>5. Select 'Economy' from the Cabin_Class dropdown<br>6. Click 'Search Flights' | An error message is shown indicating invalid characters in the Arrival_City field | low |
| TC-015 (interaction_edge) |  | Rapid re-submission after successful search | User has successfully submitted the Flights Search Form | 1. Click 'Search Flights'<br>2. Press the browser back button immediately after redirection to the listing page | The Flights Search Form is shown blank; no duplicate search is initiated | medium |

---

## Flight Booking

Total: **13** (positive: 1, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with all required fields completed | User logged in as <Role> | 1. Click 'Add Traveler' to add a new traveler<br>2. Select 'Mr' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid passport expiry date> in the Passport Expiry field<br>8. Enter <valid email> in the Lead Passenger Email field<br>9. Enter <valid phone number> in the Lead Passenger Phone field<br>10. Click Continue Button | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Continue with missing First Name |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the First_Name field indicating it is required; form does not submit |  |
| TC-003 | WF-003 | Continue with missing Last Name |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Last_Name field indicating it is required; form does not submit |  |
| TC-004 | WF-004 | Continue with missing Date of Birth |  | 1. Leave the Date_of_Birth field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Date_of_Birth field indicating it is required; form does not submit |  |
| TC-005 | WF-005 | Continue with missing Passport Number |  | 1. Leave the Passport_Number field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Passport_Number field indicating it is required; form does not submit |  |
| TC-006 | WF-006 | Continue with missing Passport Expiry |  | 1. Leave the Passport_Expiry field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Passport_Expiry field indicating it is required; form does not submit |  |
| TC-007 | WF-007 | Continue with missing Lead Passenger Email |  | 1. Leave the Lead_Passenger_Email field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Lead_Passenger_Email field indicating it is required; form does not submit |  |
| TC-008 | WF-008 | Continue with missing Lead Passenger Phone |  | 1. Leave the Lead_Passenger_Phone field blank<br>2. Fill all other required fields<br>3. Click Continue_Button | Inline validation error appears on the Lead_Passenger_Phone field indicating it is required; form does not submit |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Add maximum allowed entries to Travelers | User is on the flight booking page | 1. Add 10 entries to the Travelers repeating group<br>2. Fill all required fields for each traveler<br>3. Click Continue | Form submits successfully; user proceeds to payment page | medium |
| TC-010 (boundary) | WF-001 | Attempt to add one more entry beyond the maximum allowed in Travelers | User is on the flight booking page | 1. Add 10 entries to the Travelers repeating group<br>2. Attempt to add an 11th entry<br>3. Click Continue | Adding the 11th entry is blocked; inline error displayed for exceeding maximum entries | medium |
| TC-011 (input_edge) |  | Enter a very long string in Lead Passenger Phone | User is on the flight booking page | 1. Enter a string of 200+ characters in the Lead Passenger Phone field<br>2. Fill all other required fields<br>3. Click Continue | Form submits successfully; saved value shows the entered phone number | low |
| TC-012 (input_edge) |  | Enter special characters in Lead Passenger Email | User is on the flight booking page | 1. Enter 'user@domain!com' in the Lead Passenger Email field<br>2. Fill all other required fields<br>3. Click Continue | Inline error displayed indicating invalid email format | low |
| TC-013 (state_edge) |  | Rapid consecutive submissions with valid data | User is on the flight booking page | 1. Fill all required fields correctly<br>2. Click Continue<br>3. Immediately click Continue again after the first submission | Second submission attempt is blocked; user remains on the flight booking page | medium |

---

## Tours Search & Listing

Total: **12** (positive: 2, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search tours using the main search form | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select 'Adventure' from the Tour Type dropdown<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid budget range> in the Budget Range field<br>6. Click Search | redirects to listing page | high |
| TC-002 | WF-002 | Search tours using sidebar filters | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Select 'Cultural' from the Tour Type dropdown<br>3. Enter <valid price range> in the Price Range field<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid departure dates> in the Departure Dates field<br>6. Click Search | redirects to listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Destination field blank and submit the search form |  | 1. Leave the Destination field blank<br>2. Fill in the Travel Dates, Tour Type, Duration, and Budget Range fields<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 | WF-001 | Leave the Travel Dates field blank and submit the search form |  | 1. Leave the Travel Dates field blank<br>2. Fill in the Destination, Tour Type, Duration, and Budget Range fields<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-005 | WF-001 | Leave the Tour Type field blank and submit the search form |  | 1. Leave the Tour Type field blank<br>2. Fill in the Destination, Travel Dates, Duration, and Budget Range fields<br>3. Click Search | Inline validation error appears on the Tour Type field indicating it is required | high |
| TC-006 | WF-001 | Leave the Duration field blank and submit the search form |  | 1. Leave the Duration field blank<br>2. Fill in the Destination, Travel Dates, Tour Type, and Budget Range fields<br>3. Click Search | Inline validation error appears on the Duration field indicating it is required | high |
| TC-007 | WF-001 | Leave the Budget Range field blank and submit the search form |  | 1. Leave the Budget Range field blank<br>2. Fill in the Destination, Travel Dates, Tour Type, and Duration fields<br>3. Click Search | Inline validation error appears on the Budget Range field indicating it is required | high |
| TC-008 | WF-001 | Submit the search form with all required fields empty |  | 1. Leave all required fields (Destination, Travel Dates, Tour Type, Duration, Budget Range) blank<br>2. Click Search | Form does not submit; no search is performed; multiple validation errors are shown for required fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter a valid travel date exactly on the minimum allowed date |  | 1. Enter a valid destination in the Destination field<br>2. Enter the minimum allowed travel date in the Travel Dates field<br>3. Select a Tour Type from the dropdown<br>4. Enter a valid duration in the Duration field<br>5. Enter a valid budget range in the Budget Range field<br>6. Click Search | User is redirected to the listing page with search results displayed | medium |
| TC-010 (boundary) | WF-001 | Enter a travel date one day before the minimum allowed date |  | 1. Enter a valid destination in the Destination field<br>2. Enter the minimum allowed travel date minus one day in the Travel Dates field<br>3. Select a Tour Type from the dropdown<br>4. Enter a valid duration in the Duration field<br>5. Enter a valid budget range in the Budget Range field<br>6. Click Search | Form submission is blocked; an error message is displayed indicating the travel date is invalid | medium |
| TC-011 (input_edge) | WF-001 | Enter a very long string in the Destination field |  | 1. Enter a string longer than 200 characters in the Destination field<br>2. Enter a valid travel date in the Travel Dates field<br>3. Select a Tour Type from the dropdown<br>4. Enter a valid duration in the Duration field<br>5. Enter a valid budget range in the Budget Range field<br>6. Click Search | Form submission is blocked; an error message is displayed indicating the input exceeds the maximum length | low |
| TC-012 (input_edge) | WF-002 | Enter a special character in the Price Range field |  | 1. Enter a valid destination in the Destination field<br>2. Select a Tour Type from the dropdown<br>3. Enter a special character in the Price Range field<br>4. Enter a valid duration in the Duration field<br>5. Click Search | Form submission is blocked; an error message is displayed indicating invalid input in the Price Range field | low |

---

## Tour Details & Booking

Total: **10** (positive: 1, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-002 | Submit booking form with all required fields filled | User logged in as <User>, User is on the Tour Details page | 1. Select a valid <departure date> in the Departure Date field<br>2. Specify <number of adults> adults and <number of children> children in the Number of Travelers field<br>3. Click 'Add Traveler' to enter traveler names<br>4. Enter <traveler name> in the Name field for the first traveler<br>5. Click 'Add Traveler' to enter another traveler name<br>6. Enter <traveler name> in the Name field for the second traveler<br>7. Enter <contact details> in the Contact Details field<br>8. Click 'Book Now' | Booking confirmed; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Departure Date field blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-003 |  | Leave the Number of Travelers field blank and submit |  | 1. Leave the Number_of_Travelers field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Number_of_Travelers field indicating it must specify number of adults and children | high |
| TC-004 |  | Leave the Contact Details field blank and submit |  | 1. Leave the Contact_Details field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Contact_Details field indicating it is required | high |
| TC-005 |  | Submit the booking form without being logged in |  | 1. Fill all required fields<br>2. Click Book Now | User is redirected to the login page | high |
| TC-006 |  | Submit the booking form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Book Now | Inline validation error appears on the Departure_Date field indicating it is required; Inline validation error appears on the Number_of_Travelers field indicating it must specify number of adults and children; Inline validation error appears on the Contact_Details field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Enter the current date as the Departure Date | User is logged in | 1. Select today's date in the Departure Date field<br>2. Specify the number of travelers<br>3. Fill in traveler names<br>4. Enter contact details<br>5. Click Book Now | Booking is confirmed; success message shown | medium |
| TC-008 (boundary) | WF-002 | Enter a date that is one day in the past as the Departure Date | User is logged in | 1. Select yesterday's date in the Departure Date field<br>2. Specify the number of travelers<br>3. Fill in traveler names<br>4. Enter contact details<br>5. Click Book Now | Booking is blocked; error message shown indicating the date must be today or in the future | medium |
| TC-009 (boundary) | WF-002 | Add the maximum allowed entries to the Traveler Names repeating group | User is logged in | 1. Specify the number of travelers<br>2. Add the maximum number of traveler names to the repeating group<br>3. Enter contact details<br>4. Click Book Now | Booking is confirmed; success message shown | medium |
| TC-010 (boundary) | WF-002 | Attempt to add one more traveler name beyond the maximum allowed in the repeating group | User is logged in | 1. Specify the number of travelers<br>2. Add the maximum number of traveler names to the repeating group<br>3. Attempt to add one more traveler name<br>4. Click Book Now | Booking is blocked; error message shown indicating the maximum number of travelers has been reached | medium |

---

## Cars Search & Listing

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for cars with valid input | User logged in as <Role> | 1. Enter <valid pick-up location> in the Pick Up Location field<br>2. Enter <valid drop-off location> in the Drop Off Location field<br>3. Select <valid pick-up date and time> in the Pick Up Date Time field<br>4. Select <valid drop-off date and time> in the Drop Off Date Time field<br>5. Enter <valid driver age> in the Driver Age field<br>6. Click Search | redirects to listing page | high |
| TC-002 | WF-002 | Book a vehicle from the listing | User logged in as <Role>, User has searched for cars | 1. Click Book Now on the desired vehicle listing | Booking confirmed; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Pick Up Location field blank |  | 1. Leave the Pick_Up_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-004 |  | Leave the Drop Off Location field blank |  | 1. Leave the Drop_Off_Location field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-005 |  | Leave the Pick Up Date Time field blank |  | 1. Leave the Pick_Up_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-006 |  | Leave the Drop Off Date Time field blank |  | 1. Leave the Drop_Off_Date_Time field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |
| TC-007 |  | Leave the Driver Age field blank |  | 1. Leave the Driver_Age field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Driver_Age field indicating it is required | high |
| TC-008 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Form does not submit; error shown on Pick_Up_Location, Drop_Off_Location, Pick_Up_Date_Time, Drop_Off_Date_Time, and Driver_Age fields | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Pick-Up Date Time equals Drop-Off Date Time |  | 1. Enter a valid Pick-Up Location<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter the same date and time in the Drop-Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Redirects to the listing page with search results | medium |
| TC-010 (boundary) | WF-001 | Drop-Off Date Time is one minute before Pick-Up Date Time |  | 1. Enter a valid Pick-Up Location<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter the same date but one minute earlier in the Drop-Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Form submission is blocked; an error message is shown indicating that Drop-Off Date Time must be after Pick-Up Date Time | medium |
| TC-011 (boundary) | WF-001 | Driver Age at minimum valid age |  | 1. Enter a valid Pick-Up Location<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter a valid future date and time in the Drop-Off Date Time field<br>5. Enter the minimum valid Driver Age<br>6. Click Search | Redirects to the listing page with search results | medium |
| TC-012 (boundary) | WF-001 | Driver Age below minimum valid age |  | 1. Enter a valid Pick-Up Location<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter a valid future date and time in the Drop-Off Date Time field<br>5. Enter an age below the minimum valid Driver Age<br>6. Click Search | Form submission is blocked; an error message is shown indicating that Driver Age must be at least the minimum value | medium |
| TC-013 (input_edge) |  | Enter a very long string in the Pick-Up Location field |  | 1. Enter a string longer than 200 characters in the Pick-Up Location field<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter a valid future date and time in the Drop-Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Form submission is blocked; an error message is shown indicating that the input exceeds the maximum length | low |
| TC-014 (input_edge) |  | Enter special characters in the Pick-Up Location field |  | 1. Enter special characters in the Pick-Up Location field<br>2. Enter a valid Drop-Off Location<br>3. Enter today's date and time in the Pick-Up Date Time field<br>4. Enter a valid future date and time in the Drop-Off Date Time field<br>5. Enter a valid Driver Age<br>6. Click Search | Form submission is blocked; an error message is shown indicating invalid characters | low |

---

## Car Booking

Total: **16** (positive: 1, negative: 8, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm Booking with valid fields | User logged in as <Role> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Driver Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid license issue country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Select <Insurance Plan> from the Insurance Plan dropdown<br>8. Click 'Add Row' to add optional add-ons<br>9. Check the GPS checkbox<br>10. Check the Child Seat checkbox<br>11. Check the Additional Driver checkbox<br>12. Click Confirm Booking | User proceeds to payment | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Driver Full Name field blank |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 |  | Leave the Driver Age field blank |  | 1. Leave the Driver Age field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Driver Age field indicating it is required | high |
| TC-004 |  | Leave the License Number field blank |  | 1. Leave the License Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-005 |  | Leave the License Issue Country field blank |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-006 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-008 |  | Leave the Insurance Plan field unselected |  | 1. Leave the Insurance Plan field unselected<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating it is required | high |
| TC-009 | WF-001 | Submit the form with all required fields empty |  | 1. Leave all required fields empty<br>2. Click Confirm Booking | Inline validation errors appear on all required fields indicating they are required; form does not submit | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Driver age at minimum valid value |  | 1. Enter <minimum valid age> in the <Driver_Age> field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully; user proceeds to payment | medium |
| TC-011 (boundary) | WF-001 | Driver age below minimum valid value |  | 1. Enter <one unit below minimum valid age> in the <Driver_Age> field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | <Driver_Age> displays an error indicating the value is below the minimum allowed | medium |
| TC-012 (input_edge) |  | Enter long text in Driver Full Name |  | 1. Enter a very long string (200+ characters) in the <Driver_Full_Name> field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully; saved value shown in detail page is truncated or an error is displayed | low |
| TC-013 (input_edge) |  | Enter special characters in License Number |  | 1. Enter special characters in the <License_Number> field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | <License_Number> displays an error indicating invalid characters | low |
| TC-014 (interaction_edge) |  | Rapid re-submission after redirect | Booking has been confirmed successfully | 1. Click Confirm Booking<br>2. Press the browser back button | Booking form is shown blank (not pre-filled) | low |
| TC-015 (boundary) | WF-001 | Add maximum number of add-ons |  | 1. Select maximum allowed add-ons in the <Add_ons> repeating group<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully; user proceeds to payment | medium |
| TC-016 (boundary) | WF-001 | Add one more add-on than allowed |  | 1. Attempt to add one more add-on to the <Add_ons> repeating group than allowed<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submission is blocked; an error is shown indicating the maximum number of add-ons has been reached | medium |

---

## Visa Services

Total: **20** (positive: 2, negative: 12, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Visa Requirements Form with valid inputs | User logged in as <Role> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Click Submit | Visa requirements displayed based on nationality and destination country | high |
| TC-002 | WF-002 | Submit Visa Application Form with valid inputs | User logged in as <Role> | 1. Enter <full name> in the Full Name field<br>2. Enter <passport number> in the Passport Number field<br>3. Enter <valid expiry date> in the Passport Expiry Date field<br>4. Enter <valid date of birth> in the Date of Birth field<br>5. Select <valid nationality> from the Nationality dropdown<br>6. Enter <valid email> in the Email field<br>7. Enter <valid phone number> in the Phone field<br>8. Enter <purpose of visit> in the Purpose of Visit field<br>9. Enter <valid intended travel dates> in the Intended Travel Dates field<br>10. Enter <valid duration of stay> in the Duration of Stay field<br>11. Upload a <valid file type> in the Document Upload section<br>12. Click Submit | Application submitted; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Select a valid Destination Country<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-004 | WF-001 | Leave the Destination Country dropdown blank and submit |  | 1. Select a valid Nationality<br>2. Leave the Destination Country dropdown blank<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-005 | WF-002 | Leave the Full Name field blank and submit the Visa Application Form |  | 1. Leave the Full Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Full Name is not provided; error shown on Full Name field | high |
| TC-006 | WF-002 | Leave the Passport Number field blank and submit the Visa Application Form |  | 1. Leave the Passport Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Passport Number is not provided; error shown on Passport Number field | high |
| TC-007 | WF-002 | Leave the Passport Expiry Date field blank and submit the Visa Application Form |  | 1. Leave the Passport Expiry Date field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Passport Expiry Date is not provided; error shown on Passport Expiry Date field | high |
| TC-008 | WF-002 | Leave the Date of Birth field blank and submit the Visa Application Form |  | 1. Leave the Date of Birth field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Date of Birth is not provided; error shown on Date of Birth field | high |
| TC-009 | WF-002 | Leave the Email field blank and submit the Visa Application Form |  | 1. Leave the Email field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Email is not provided; error shown on Email field | high |
| TC-010 | WF-002 | Leave the Phone field blank and submit the Visa Application Form |  | 1. Leave the Phone field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Phone is not provided; error shown on Phone field | high |
| TC-011 | WF-002 | Leave the Purpose of Visit field blank and submit the Visa Application Form |  | 1. Leave the Purpose of Visit field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Purpose of Visit is not provided; error shown on Purpose of Visit field | high |
| TC-012 | WF-002 | Leave the Intended Travel Dates field blank and submit the Visa Application Form |  | 1. Leave the Intended Travel Dates field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Intended Travel Dates is not provided; error shown on Intended Travel Dates field | high |
| TC-013 | WF-002 | Leave the Duration of Stay field blank and submit the Visa Application Form |  | 1. Leave the Duration of Stay field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Duration of Stay is not provided; error shown on Duration of Stay field | high |
| TC-014 | WF-002 | Leave the Document Upload field blank and submit the Visa Application Form |  | 1. Leave the Document Upload field blank<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form does not submit; Document Upload is not provided; error shown on Document Upload field | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-002 | Enter maximum length for Passport Number | User is on the Visa Application Form | 1. Enter a valid Passport Number with maximum allowed length in the Passport_Number field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with the maximum length Passport Number | medium |
| TC-016 (boundary) | WF-002 | Enter one character less than required for Full Name | User is on the Visa Application Form | 1. Enter a valid Full Name with one character less than the minimum required in the Full_Name field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating the Full Name is too short | medium |
| TC-017 (boundary) | WF-002 | Enter today's date in Passport Expiry Date | User is on the Visa Application Form | 1. Enter today's date in the Passport_Expiry_Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with today's date as Passport Expiry Date | medium |
| TC-018 (boundary) | WF-002 | Enter a past date for Date of Birth | User is on the Visa Application Form | 1. Enter a past date in the Date_of_Birth field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with the past Date of Birth | medium |
| TC-019 (data_edge) | WF-002 | Upload a file exactly at the size limit | User is on the Visa Application Form, User has a file that meets the size limit | 1. Upload a file that is exactly at the size limit in the Document_Upload section<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with the file uploaded | medium |
| TC-020 (input_edge) | WF-002 | Enter a long string in the Purpose of Visit | User is on the Visa Application Form | 1. Enter a very long string (200+ characters) in the Purpose_of_Visit field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating the input exceeds maximum length | low |

---

## User Dashboard

Total: **27** (positive: 6, negative: 14, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Booking Details | User logged in as <Role>, Booking type and cancellation policy permit | 1. Navigate to My Bookings<br>2. Click View Details on a booking | Booking details displayed | high |
| TC-002 | WF-002 | Cancel Booking | User logged in as <Role>, Booking type and cancellation policy permit | 1. Navigate to My Bookings<br>2. Click Cancel on a booking | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify Booking | User logged in as <Role>, Booking type and cancellation policy permit | 1. Navigate to My Bookings<br>2. Click Modify on a booking | Booking modified; success message shown | high |
| TC-004 | WF-004 | Edit Profile Information | User logged in as <Role> | 1. Navigate to My Profile<br>2. Click Edit<br>3. Fill in <Personal Information><br>4. Submit the form | Profile information updated | high |
| TC-005 | WF-005 | Edit Settings | User logged in as <Role> | 1. Navigate to Settings<br>2. Click Edit<br>3. Change <Notification Preferences><br>4. Submit the form | Settings updated | medium |
| TC-006 | WF-006 | Logout | User logged in as <Role> | 1. Click Logout | User logged out | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Booking Reference field blank and submit |  | 1. Leave the Booking Reference field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Booking Reference field indicating it is required | high |
| TC-008 |  | Leave the Service Type field blank and submit |  | 1. Leave the Service Type field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Service Type field indicating it is required | high |
| TC-009 |  | Leave the Travel Dates field blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-010 |  | Leave the Status field blank and submit |  | 1. Leave the Status field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Status field indicating it is required | high |
| TC-011 |  | Leave the Personal Information field blank and submit |  | 1. Leave the Personal Information field blank<br>2. Click Edit | Inline validation error appears on the Personal Information field indicating it is required | high |
| TC-012 |  | Leave the Available Credit Balance field blank and submit |  | 1. Leave the Available Credit Balance field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Available Credit Balance field indicating it is required | high |
| TC-013 |  | Leave the Transaction History field blank and submit |  | 1. Leave the Transaction History field blank<br>2. Click Submit | Inline validation error appears on the Transaction History field indicating it is required | high |
| TC-014 |  | Leave the Saved Items field blank and submit |  | 1. Leave the Saved Items field blank<br>2. Click Submit | Inline validation error appears on the Saved Items field indicating it is required | high |
| TC-015 |  | Leave the Rating field blank and submit |  | 1. Leave the Rating field blank<br>2. Click Submit | Inline validation error appears on the Rating field indicating it is required | high |
| TC-016 |  | Attempt to Cancel a booking when booking type and cancellation policy do not permit |  | 1. Select a booking that cannot be cancelled<br>2. Click Cancel | Action is blocked; cancellation is not permitted | medium |
| TC-017 |  | Attempt to Modify a booking when booking type and cancellation policy do not permit |  | 1. Select a booking that cannot be modified<br>2. Click Modify | Action is blocked; modification is not permitted | medium |
| TC-018 |  | Attempt to Edit Profile Information without filling required fields |  | 1. Click Edit<br>2. Leave the Personal Information field blank<br>3. Click Save | Inline validation error appears on the Personal Information field indicating it is required | high |
| TC-019 |  | Attempt to Edit Settings without filling required fields |  | 1. Click Edit<br>2. Leave the Change Password field blank<br>3. Click Save | Inline validation error appears on the Change Password field indicating it is required | high |
| TC-020 |  | Attempt to Logout without being logged in |  | 1. Click Logout | User remains on the current page; logout action is not performed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-002 | Cancel booking with valid booking type and cancellation policy | User has a booking that can be cancelled | 1. Navigate to My Bookings section<br>2. Click Cancel on a booking with valid cancellation policy | Booking cancelled; success message shown | medium |
| TC-022 (boundary) | WF-002 | Attempt to cancel booking with invalid cancellation policy | User has a booking that cannot be cancelled | 1. Navigate to My Bookings section<br>2. Click Cancel on a booking with invalid cancellation policy | Cancellation is blocked; error message shown indicating cancellation is not permitted | medium |
| TC-023 (boundary) | WF-003 | Modify booking with valid booking type and cancellation policy | User has a booking that can be modified | 1. Navigate to My Bookings section<br>2. Click Modify on a booking with valid modification policy | Booking modified; success message shown | medium |
| TC-024 (boundary) | WF-003 | Attempt to modify booking with invalid modification policy | User has a booking that cannot be modified | 1. Navigate to My Bookings section<br>2. Click Modify on a booking with invalid modification policy | Modification is blocked; error message shown indicating modification is not permitted | medium |
| TC-025 (input_edge) |  | Enter long text in Personal Information field | User is on My Profile section | 1. Navigate to My Profile section<br>2. Enter a very long string (200+ characters) in the Personal Information field | Field accepts the input or shows a truncation/error message | low |
| TC-026 (input_edge) |  | Enter special characters in Personal Information field | User is on My Profile section | 1. Navigate to My Profile section<br>2. Enter special characters in the Personal Information field | Field accepts the input or shows a specific error message | low |
| TC-027 (interaction_edge) |  | Rapid re-submission after editing profile | User has successfully edited profile information | 1. Click Edit on My Profile section<br>2. Submit the changes<br>3. Immediately click Edit again | User is redirected to the My Profile section without pre-filled data from the previous submission | low |

---

## Booking Management

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details successfully | User logged in as <Role>, booking type and cancellation policy permit modification | 1. Click the Modify button | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 | WF-002 | Open cancellation confirmation flow | User logged in as <Role>, user must confirm cancellation before processing, booking type and cancellation policy permit cancellation | 1. Click the Cancel button | opens cancellation confirmation flow | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to modify booking when modification is not permitted | booking type and cancellation policy do not permit modification | 1. Click Modify_Button | Modification action is blocked; no changes are made to the booking | high |
| TC-004 | WF-002 | Attempt to cancel booking without confirming cancellation | user does not confirm cancellation | 1. Click Cancel_Button | Cancellation process is blocked; no cancellation occurs | high |
| TC-005 | WF-002 | Attempt to cancel booking when cancellation is not permitted | booking type and cancellation policy do not permit cancellation | 1. Click Cancel_Button<br>2. Confirm cancellation | Cancellation action is blocked; no cancellation occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-001 | Attempt to modify booking details when modification is permitted | booking type and cancellation policy permit modification | 1. Click the Modify button | Modification options are displayed, allowing changes to travel dates, special requests, or traveler information. | medium |
| TC-007 (boundary) | WF-002 | Attempt to cancel booking when cancellation is permitted | user must confirm cancellation before processing, booking type and cancellation policy permit cancellation | 1. Click the Cancel button<br>2. Confirm cancellation | Cancellation confirmation flow opens, displaying the applicable refund amount. | medium |
| TC-008 (boundary) | WF-002 | Attempt to cancel booking without confirming cancellation | booking type and cancellation policy permit cancellation | 1. Click the Cancel button | Cancellation is not processed; user remains on the booking detail view. | medium |
| TC-009 (interaction_edge) | WF-001 | Rapidly click Modify button multiple times | booking type and cancellation policy permit modification | 1. Click the Modify button<br>2. Immediately click the Modify button again | Modification options are displayed only once; no duplicate modification flows are initiated. | low |

---

## Payment Processing

Total: **20** (positive: 4, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Payment with Credit/Debit Card | User logged in as <Role>, Payment_Method is set to 'Credit/Debit Card' | 1. Enter <Cardholder_Name> in the Cardholder Name field<br>2. Enter <Card_Number> in the Card Number field<br>3. Enter <Expiration_Date> in the Expiration Date field<br>4. Enter <CVV> in the CVV field<br>5. Click Submit Payment | redirects to booking confirmation page with reference number | high |
| TC-002 | WF-002 | Submit Payment with PayPal | User logged in as <Role>, Payment_Method is set to 'PayPal' | 1. Click Submit Payment | redirects to booking confirmation page with reference number | high |
| TC-003 | WF-003 | Submit Payment with Bank Transfer | User logged in as <Role>, Payment_Method is set to 'Bank Transfer' | 1. Click Submit Payment | redirects to booking confirmation page with reference number | high |
| TC-004 | WF-004 | Submit Payment with Wallet/Credits | User logged in as <Role>, Payment_Method is set to 'Wallet/Credits' | 1. Click Submit Payment | redirects to booking confirmation page with reference number | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Payment_Method blank and submit |  | 1. Leave the Payment_Method field blank<br>2. Fill all other required fields<br>3. Click Submit Payment | Inline validation error appears on the Payment_Method field indicating it is required | high |
| TC-006 |  | Leave Cardholder_Name blank when Payment_Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Cardholder_Name field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-007 |  | Leave Card_Number blank when Payment_Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Card_Number field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-008 |  | Leave Expiration_Date blank when Payment_Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Expiration_Date field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-009 |  | Leave CVV blank when Payment_Method is Credit/Debit Card | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the CVV field blank<br>3. Fill all other required fields<br>4. Click Submit Payment | Inline validation error appears on the CVV field indicating it is required | high |
| TC-010 | WF-001 | Submit Payment with invalid Card_Number format | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Fill Cardholder_Name with valid name<br>3. Enter <invalid format> in the Card_Number field<br>4. Enter valid Expiration_Date and CVV<br>5. Click Submit Payment | Displays error message describing the issue | medium |
| TC-011 | WF-001 | Submit Payment with past Expiration_Date | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Fill Cardholder_Name with valid name<br>3. Enter valid Card_Number<br>4. Enter <past date> in the Expiration_Date field<br>5. Enter valid CVV<br>6. Click Submit Payment | Displays error message describing the issue | medium |
| TC-012 | WF-001 | Submit Payment with invalid CVV format | Payment_Method is set to Credit/Debit Card | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Fill Cardholder_Name with valid name<br>3. Enter valid Card_Number<br>4. Enter valid Expiration_Date<br>5. Enter <invalid format> in the CVV field<br>6. Click Submit Payment | Displays error message describing the issue | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Enter valid card number at the boundary of length | Payment_Method is set to Credit/Debit Card | 1. Enter a valid card number with exactly 16 digits in the Card_Number field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-014 (boundary) | WF-001 | Enter card number one digit short | Payment_Method is set to Credit/Debit Card | 1. Enter a valid card number with 15 digits in the Card_Number field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displays indicating the card number is invalid | medium |
| TC-015 (boundary) | WF-001 | Enter expiration date as today's date | Payment_Method is set to Credit/Debit Card | 1. Enter today's date in the Expiration_Date field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-016 (boundary) | WF-001 | Enter expiration date as yesterday's date | Payment_Method is set to Credit/Debit Card | 1. Enter yesterday's date in the Expiration_Date field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displays indicating the expiration date is invalid | medium |
| TC-017 (input_edge) | WF-001 | Enter a very long cardholder name | Payment_Method is set to Credit/Debit Card | 1. Enter a cardholder name with 200+ characters in the Cardholder_Name field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displays indicating the cardholder name exceeds maximum length | low |
| TC-018 (input_edge) | WF-001 | Enter special characters in cardholder name | Payment_Method is set to Credit/Debit Card | 1. Enter special characters (e.g., @#$%^&*) in the Cardholder_Name field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displays indicating invalid characters in the cardholder name | low |
| TC-019 (data_edge) | WF-001 | Enter a valid CVV at the boundary of length | Payment_Method is set to Credit/Debit Card | 1. Enter a valid CVV with exactly 3 digits in the CVV field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-020 (data_edge) | WF-001 | Enter CVV one digit short | Payment_Method is set to Credit/Debit Card | 1. Enter a CVV with 2 digits in the CVV field<br>2. Fill all other required fields<br>3. Click Submit Payment | Form submission is blocked; error message displays indicating the CVV is invalid | medium |

---

## Currency & Language Selection

Total: **14** (positive: 8, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select USD as currency | User logged in as <Role> | 1. Select 'USD' from the Currency dropdown | All prices displayed across the site are updated in USD | high |
| TC-002 | WF-002 | Select EUR as currency | User logged in as <Role> | 1. Select 'EUR' from the Currency dropdown | All prices displayed across the site are updated in EUR | high |
| TC-003 | WF-003 | Select GBP as currency | User logged in as <Role> | 1. Select 'GBP' from the Currency dropdown | All prices displayed across the site are updated in GBP | high |
| TC-004 | WF-004 | Select JPY as currency | User logged in as <Role> | 1. Select 'JPY' from the Currency dropdown | All prices displayed across the site are updated in JPY | high |
| TC-005 | WF-005 | Select English as language | User logged in as <Role> | 1. Select 'English' from the Language dropdown | The entire site interface switches to English | high |
| TC-006 | WF-006 | Select Arabic as language | User logged in as <Role> | 1. Select 'Arabic' from the Language dropdown | The entire site interface switches to Arabic | high |
| TC-007 | WF-007 | Select Spanish as language | User logged in as <Role> | 1. Select 'Spanish' from the Language dropdown | The entire site interface switches to Spanish | high |
| TC-008 | WF-008 | Select French as language | User logged in as <Role> | 1. Select 'French' from the Language dropdown | The entire site interface switches to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Attempt to select a currency without making a selection |  | 1. Open the Currency Selector dropdown<br>2. Leave the selection blank<br>3. Click Select | Form does not submit; no currency is selected; error shown on Currency Selector field indicating selection is required | high |
| TC-010 | WF-005 | Attempt to select a language without making a selection |  | 1. Open the Language Selector dropdown<br>2. Leave the selection blank<br>3. Click Select | Form does not submit; no language is selected; error shown on Language Selector field indicating selection is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Select USD as currency after previously selecting JPY | User has previously selected JPY as currency | 1. Select USD from the Currency Selector dropdown | All prices displayed across the site update in real-time to reflect USD; previous JPY selection is overridden without loss of search context. | medium |
| TC-012 (interaction_edge) | WF-005 | Select English as language after previously selecting Arabic | User has previously selected Arabic as language | 1. Select English from the Language Selector dropdown | The entire site interface switches to English, overriding the previous Arabic selection. | medium |
| TC-013 (input_edge) |  | Select a currency option that is not in the dropdown | User attempts to select a currency | 1. Attempt to enter 'AUD' in the Currency Selector | The Currency Selector does not accept 'AUD'; the dropdown options remain unchanged. | low |
| TC-014 (input_edge) |  | Select a language option that is not in the dropdown | User attempts to select a language | 1. Attempt to enter 'German' in the Language Selector | The Language Selector does not accept 'German'; the dropdown options remain unchanged. | low |

---

## Search & Filters

Total: **15** (positive: 6, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply Common Filters with Star Ratings | User logged in as <Role> | 1. Select '3 Stars' from the Star Ratings dropdown<br>2. Adjust the Price Range slider to the desired range | Results update dynamically with applied filters | high |
| TC-002 | WF-001 | Apply Hotel Filters | User logged in as <Role> | 1. Select 'Luxury' from the Hotel_Type dropdown<br>2. Select 'Free WiFi' from the Facilities_Amenities dropdown<br>3. Select 'All Inclusive' from the Board_Basis dropdown<br>4. Select 'City Center' from the Location_Area dropdown | Results update dynamically with applied filters | high |
| TC-003 | WF-001 | Apply Flight Filters | User logged in as <Role> | 1. Select 'Airline A' from the Airlines dropdown<br>2. Select 'Non-stop' from the Number_of_Stops dropdown | Results update dynamically with applied filters | high |
| TC-004 | WF-001 | Apply Tour Filters | User logged in as <Role> | 1. Select 'Cultural' from the Tour_Type dropdown<br>2. Adjust the Duration slider to the desired length | Results update dynamically with applied filters | high |
| TC-005 | WF-001 | Apply Car Filters | User logged in as <Role> | 1. Select 'SUV' from the Car_Type dropdown<br>2. Select 'Automatic' from the Transmission dropdown<br>3. Select 'Full to Full' from the Fuel_Policy dropdown | Results update dynamically with applied filters | high |
| TC-006 | WF-002 | Reset All Filters | User logged in as <Role>, Filters are applied | 1. Click the Reset All Filters button | All filters reset to default | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave the Price Range slider blank and submit |  | 1. Leave the Price Range slider blank<br>2. Select a Star Rating<br>3. Click Apply Filters | Form does not submit; Price Range is not set | high |
| TC-008 |  | Select an invalid option in Star Ratings dropdown |  | 1. Select an invalid option in the Star Ratings dropdown<br>2. Click Apply Filters | Form does not submit; Star Ratings dropdown displays an error: 'Invalid selection' | high |
| TC-009 |  | Attempt to apply filters without selecting any filters |  | 1. Leave all filter fields empty<br>2. Click Apply Filters | Form does not submit; no filters applied | high |
| TC-010 | WF-002 | Attempt to reset filters when no filters are applied |  | 1. Click Reset All Filters | No action occurs; all filters remain unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Add maximum allowed entries to Active Filters | User is on the search page with the filter section visible | 1. Add exactly <maximum allowed entries> to the Active Filters | Active Filters displays all added filters without error | medium |
| TC-012 (boundary) | WF-001 | Attempt to add one more entry to Active Filters | User is on the search page with the filter section visible | 1. Add exactly <maximum allowed entries> to the Active Filters<br>2. Attempt to add one more entry to the Active Filters | Adding the filter is blocked; error shown indicating the maximum limit has been reached | medium |
| TC-013 (interaction_edge) | WF-002 | Reset all filters after applying some | User has applied several filters | 1. Click the Reset All Filters button | All filters reset to default; no active filters are displayed | medium |
| TC-014 (input_edge) |  | Enter a very long string in the Filter Name | User is in the Active Filters section | 1. Enter a string longer than 200 characters in the Filter Name field | The input is either accepted or truncated with a visible indicator | low |
| TC-015 (input_edge) |  | Enter special characters in the Filter Name | User is in the Active Filters section | 1. Enter special characters (e.g., !@#$%^&*) in the Filter Name field | The input is accepted or a specific error is shown | low |

---

## Reviews & Ratings

Total: **12** (positive: 1, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a review with valid inputs | User logged in as <Authenticated User>, User has completed a booking | 1. Navigate to the Submit Review section<br>2. Enter <Overall Experience Rating> in the Overall Experience Rating field<br>3. Enter <Cleanliness Rating> in the Cleanliness field<br>4. Enter <Service Rating> in the Service field<br>5. Enter <Location Rating> in the Location field<br>6. Enter <Written Feedback> in the Written Feedback field<br>7. Click Submit Review | A success notification shows 'review submitted' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to submit a review without being authenticated | User is not authenticated | 1. Navigate to the Submit Review form<br>2. Fill in all fields with valid data<br>3. Click Submit Review | User is redirected to the login page; review is not submitted | high |
| TC-003 |  | Attempt to submit a review without completing a booking | User is authenticated, User has not completed a booking | 1. Navigate to the Submit Review form<br>2. Fill in all fields with valid data<br>3. Click Submit Review | User receives an error message indicating that a booking must be completed; review is not submitted | high |
| TC-004 |  | Leave Overall Experience Rating blank and submit | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review form<br>2. Leave the Overall Experience Rating field blank<br>3. Fill in all other fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Overall Experience Rating field indicating it is required; review is not submitted | high |
| TC-005 |  | Leave Written Feedback blank and submit | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review form<br>2. Leave the Written Feedback field blank<br>3. Fill in all other fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Written Feedback field indicating it is required; review is not submitted | high |
| TC-006 |  | Leave Cleanliness rating blank and submit | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review form<br>2. Leave the Cleanliness field blank<br>3. Fill in all other fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Cleanliness field indicating it is required; review is not submitted | high |
| TC-007 |  | Leave Service rating blank and submit | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review form<br>2. Leave the Service field blank<br>3. Fill in all other fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Service field indicating it is required; review is not submitted | high |
| TC-008 |  | Leave Location rating blank and submit | User is authenticated, User has completed a booking | 1. Navigate to the Submit Review form<br>2. Leave the Location field blank<br>3. Fill in all other fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Location field indicating it is required; review is not submitted | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit review with maximum rating value | user must be authenticated, user must have completed a booking | 1. Enter the maximum allowed value in the Overall Experience Rating field<br>2. Fill all category ratings with maximum allowed values<br>3. Enter valid written feedback<br>4. Click Submit Review | Review submitted successfully; confirmation message displayed | medium |
| TC-010 (boundary) | WF-001 | Submit review with one unit below minimum rating value | user must be authenticated, user must have completed a booking | 1. Enter one unit below the minimum allowed value in the Overall Experience Rating field<br>2. Fill all category ratings with valid values<br>3. Enter valid written feedback<br>4. Click Submit Review | Submission is blocked; error message displayed indicating rating is below minimum allowed | medium |
| TC-011 (input_edge) |  | Enter long written feedback | user must be authenticated, user must have completed a booking | 1. Enter a very long string (200+ characters) in the Written Feedback field<br>2. Fill all rating fields with valid values<br>3. Click Submit Review | Review is submitted successfully; feedback is displayed correctly without truncation | low |
| TC-012 (input_edge) |  | Enter special characters in written feedback | user must be authenticated, user must have completed a booking | 1. Enter special characters in the Written Feedback field<br>2. Fill all rating fields with valid values<br>3. Click Submit Review | Review is submitted successfully; feedback is displayed correctly with special characters | low |

---

## Offers & Deals

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit offer search without newsletter subscription | User logged in as <Role> | 1. Select 'Hotels' from the Service Type Filter dropdown<br>2. Enter <destination> in the Destination Filter<br>3. Enter <valid travel dates> in the Travel Dates Filter<br>4. Click 'Book Now' | applies promotional code automatically or redirects to pre-filled search | high |
| TC-002 | WF-002 | Submit offer search with newsletter subscription | User logged in as <Role> | 1. Select 'Flights' from the Service Type Filter dropdown<br>2. Enter <destination> in the Destination Filter<br>3. Enter <valid travel dates> in the Travel Dates Filter<br>4. Enter <valid email> in the Newsletter Subscription field<br>5. Click 'Book Now' | applies promotional code automatically or redirects to pre-filled search | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Submit the form without filling in the required Newsletter Subscription field |  | 1. Leave the Newsletter Subscription field blank<br>2. Fill in other fields as needed<br>3. Click Book Now | Form does not submit; Newsletter Subscription field displays an error: 'This field is required' | high |
| TC-004 |  | Submit the form with all fields empty |  | 1. Leave all fields blank<br>2. Click Book Now | Form does not submit; Newsletter Subscription field displays an error: 'This field is required' | high |
| TC-005 |  | Submit the form with an invalid email format in the Newsletter Subscription field |  | 1. Enter <invalid email format> in the Newsletter Subscription field<br>2. Fill in other fields as needed<br>3. Click Book Now | Form does not submit; Newsletter Subscription field displays an error: 'Must be a valid email address' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-002 | Enter valid email in Newsletter Subscription field |  | 1. Select 'Hotels' from the Service_Type_Filter dropdown<br>2. Enter 'New York' in the Destination_Filter<br>3. Enter today's date in the Travel_Dates_Filter<br>4. Enter a valid email address in the Newsletter_Subscription field<br>5. Click Book Now | Form submits successfully; promotional code is applied automatically | medium |
| TC-007 (boundary) | WF-002 | Submit without entering email in Newsletter Subscription field |  | 1. Select 'Flights' from the Service_Type_Filter dropdown<br>2. Enter 'Los Angeles' in the Destination_Filter<br>3. Enter tomorrow's date in the Travel_Dates_Filter<br>4. Leave the Newsletter_Subscription field empty<br>5. Click Book Now | Submission is blocked; an error message indicates that the Newsletter_Subscription field is required | medium |
| TC-008 (input_edge) |  | Enter a very long string in the Destination_Filter |  | 1. Select 'Packages' from the Service_Type_Filter dropdown<br>2. Enter a string longer than 200 characters in the Destination_Filter<br>3. Enter a valid date in the Travel_Dates_Filter<br>4. Enter a valid email address in the Newsletter_Subscription field<br>5. Click Book Now | Form submits successfully; the long string is accepted or truncated with a visible indicator | low |
| TC-009 (input_edge) |  | Enter special characters in the Destination_Filter |  | 1. Select 'Hotels' from the Service_Type_Filter dropdown<br>2. Enter special characters in the Destination_Filter<br>3. Enter a valid date in the Travel_Dates_Filter<br>4. Enter a valid email address in the Newsletter_Subscription field<br>5. Click Book Now | Form submits successfully; special characters are accepted or a specific error is shown | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click Logout button | terminates the current session, clears sensitive session data, and redirects to the home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to logout while not logged in | user must not be logged in | 1. Ensure the user is not logged in<br>2. Click the Logout button | Logout action is not performed; user remains on the current page and is not redirected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid consecutive logout attempts | User is logged in | 1. Click Logout<br>2. Immediately click Logout again | The first logout action succeeds, and the user is redirected to the home page; the second logout action is ignored as the session has already been terminated. | medium |
| TC-004 (interaction_edge) |  | Access protected page after logout | User is logged in, User clicks Logout | 1. Click Logout<br>2. Attempt to access a protected page | User is redirected to the login page with a visible prompt indicating that the session has expired. | medium |

---
