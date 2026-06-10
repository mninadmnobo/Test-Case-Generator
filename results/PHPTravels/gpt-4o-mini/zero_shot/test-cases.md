# Test Cases — 

Generated:   
Model:   

## PHPTravels

Total: **21** (positive: 7, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful hotel search | User is on the home page, User selects the Hotels tab | 1. Enter a valid destination<br>2. Select check-in and check-out dates<br>3. Specify number of rooms and guest count<br>4. Click the Search button | User is redirected to the hotel listing page with relevant results displayed | high |
| TC004 |  | Successful user registration | User is on the registration page | 1. Fill in all required fields with valid data<br>2. Check the Terms and Conditions checkbox<br>3. Click the Submit button | User account is created, and the user is redirected to the dashboard | high |
| TC007 |  | Successful user login | User has a registered account, User is on the login page | 1. Enter valid email and password<br>2. Click the Login button | User is redirected to their dashboard | high |
| TC010 |  | Successful flight search | User is on the home page, User selects the Flights tab | 1. Enter valid departure and arrival cities<br>2. Select travel dates<br>3. Specify passenger count and cabin class<br>4. Click the Search button | User is redirected to the flight listing page with relevant results displayed | high |
| TC013 |  | Successful car rental search | User is on the home page, User selects the Cars tab | 1. Enter valid pick-up and drop-off locations<br>2. Select pick-up and drop-off dates and times<br>3. Enter driver age<br>4. Click the Search button | User is redirected to the car listing page with relevant results displayed | high |
| TC016 |  | Successful tour search | User is on the home page, User selects the Tours tab | 1. Enter valid destination<br>2. Select travel dates<br>3. Specify tour type and budget range<br>4. Click the Search button | User is redirected to the tour listing page with relevant results displayed | high |
| TC019 |  | Successful visa application submission | User is on the visa services page | 1. Select nationality and destination country<br>2. Fill in all required fields with valid data<br>3. Upload required documents<br>4. Click the Submit button | Visa application is submitted successfully, and a confirmation message is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Hotel search with missing required fields | User is on the home page, User selects the Hotels tab | 1. Leave destination field empty<br>2. Click the Search button | Inline error message appears indicating that the destination is required | high |
| TC005 |  | User registration with invalid email format | User is on the registration page | 1. Fill in all required fields with valid data<br>2. Enter an invalid email format (e.g., 'user@domain')<br>3. Click the Submit button | Inline error message appears indicating that the email format is invalid | high |
| TC008 |  | User login with incorrect password | User has a registered account, User is on the login page | 1. Enter valid email and incorrect password<br>2. Click the Login button | Error message appears indicating invalid credentials, and the password field is cleared | high |
| TC011 |  | Flight search with missing required fields | User is on the home page, User selects the Flights tab | 1. Leave departure city field empty<br>2. Click the Search button | Inline error message appears indicating that the departure city is required | high |
| TC014 |  | Car rental search with missing required fields | User is on the home page, User selects the Cars tab | 1. Leave pick-up location field empty<br>2. Click the Search button | Inline error message appears indicating that the pick-up location is required | high |
| TC017 |  | Tour search with missing required fields | User is on the home page, User selects the Tours tab | 1. Leave destination field empty<br>2. Click the Search button | Inline error message appears indicating that the destination is required | high |
| TC020 |  | Visa application submission with missing required fields | User is on the visa services page | 1. Leave passport number field empty<br>2. Click the Submit button | Inline error message appears indicating that the passport number is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC003 |  | Hotel search with maximum input values | User is on the home page, User selects the Hotels tab | 1. Enter a valid destination<br>2. Select check-in and check-out dates<br>3. Specify maximum number of rooms (e.g., 10) and guest count (e.g., 20 adults, 10 children)<br>4. Click the Search button | User is redirected to the hotel listing page with relevant results displayed | medium |
| TC006 |  | User registration with maximum length fields | User is on the registration page | 1. Fill in all required fields with maximum length data (e.g., 255 characters for First Name and Last Name)<br>2. Enter a valid email<br>3. Click the Submit button | User account is created, and the user is redirected to the dashboard | medium |
| TC009 |  | User login after multiple failed attempts | User has a registered account, User is on the login page | 1. Enter valid email and incorrect password multiple times<br>2. Click the Login button after the last attempt | CAPTCHA verification is displayed after multiple failed attempts | medium |
| TC012 |  | Flight search with maximum input values | User is on the home page, User selects the Flights tab | 1. Enter valid departure and arrival cities<br>2. Select travel dates<br>3. Specify maximum passenger count (e.g., 9 adults)<br>4. Click the Search button | User is redirected to the flight listing page with relevant results displayed | medium |
| TC015 |  | Car rental search with maximum input values | User is on the home page, User selects the Cars tab | 1. Enter valid pick-up and drop-off locations<br>2. Select pick-up and drop-off dates and times<br>3. Enter maximum driver age (e.g., 100)<br>4. Click the Search button | User is redirected to the car listing page with relevant results displayed | medium |
| TC018 |  | Tour search with maximum input values | User is on the home page, User selects the Tours tab | 1. Enter valid destination<br>2. Select travel dates<br>3. Specify maximum duration and budget range<br>4. Click the Search button | User is redirected to the tour listing page with relevant results displayed | medium |
| TC021 |  | Visa application submission with maximum input values | User is on the visa services page | 1. Fill in all required fields with maximum length data<br>2. Upload required documents<br>3. Click the Submit button | Visa application is submitted successfully, and a confirmation message is displayed | medium |

---
