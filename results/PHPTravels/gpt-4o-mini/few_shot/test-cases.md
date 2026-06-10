# Test Cases — 

Generated:   
Model:   

## PHPTravels

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Search for hotels with valid destination and date range | User is on the PHPTravels home page | 1. Click the Hotels tab on the search widget<br>2. Enter 'New York' in the Destination field<br>3. Select '2023-12-01' as the check-in date and '2023-12-05' as the check-out date<br>4. Set 1 room and 2 guests<br>5. Click the Search button | User is redirected to the hotel listing page showing available hotels for New York from December 1 to December 5; each card displays hotel name, rating, and starting price per night | high |
| P-002 |  | Login with valid credentials | User is on the Login page | 1. Enter a valid email in the Email field<br>2. Enter the correct password in the Password field<br>3. Click the Login button | User is redirected to their dashboard with a welcome message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Register a new account with an invalid email format | User is on the Registration page | 1. Fill in First Name, Last Name, and Mobile Number with valid values<br>2. Enter 'invalidemail' in the Email field<br>3. Enter 'Password123' in the Password field<br>4. Enter 'Password123' in the Confirm Password field<br>5. Check the Terms and Conditions checkbox<br>6. Click Register | An inline validation error is shown on the Email field indicating an invalid email format; the account is not created | high |
| N-002 |  | Login with invalid password | User is on the Login page | 1. Enter a valid email in the Email field<br>2. Enter an incorrect password in the Password field<br>3. Click the Login button | An error message is displayed indicating invalid credentials; the password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Search for flights with check-in date equal to check-out date (same-day trip) | User is on the PHPTravels home page | 1. Click the Flights tab on the search widget<br>2. Select 'One-way' as the trip type<br>3. Enter 'Los Angeles' as the departure city and 'San Francisco' as the arrival city<br>4. Select today's date as the travel date<br>5. Set 1 adult passenger<br>6. Click Search | User is redirected to the flight listing page; results show available one-way flights departing today, or an appropriate message if no flights are available | medium |
| E-002 |  | Search for tours with maximum length of travel dates | User is on the PHPTravels home page | 1. Click the Tours tab on the search widget<br>2. Enter 'Paris' in the Destination field<br>3. Select a travel date range of 1 year from today<br>4. Set a budget range of $1000 to $100000<br>5. Click Search | User is redirected to the tours listing page; results show available tours for the specified criteria | medium |

---
