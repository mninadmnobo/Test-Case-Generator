# Test Cases — 

Generated:   
Model:   

## MoodleTeacher

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful login with valid credentials | User has valid username and password | 1. Navigate to the login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click on 'Log in' button | User is redirected to the Dashboard | high |
| TC004 |  | Accessing the Dashboard after login | User is logged in | 1. Click on 'Dashboard' link in the navigation bar | Dashboard is displayed with personalized greeting and blocks | high |
| TC007 |  | Creating an assignment successfully | User is in Course Edit mode, User has selected 'Assignment' from Activity Chooser | 1. Fill in the required Assignment name<br>2. Fill in other optional fields as needed<br>3. Click 'Save and return to course' | Assignment is created and user is redirected to the course page | high |
| TC010 |  | Logging out successfully | User is logged in | 1. Click on user initials icon<br>2. Select 'Log out' from the dropdown | User is logged out and redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Unsuccessful login with invalid credentials | User is on the login page | 1. Enter invalid username<br>2. Enter invalid password<br>3. Click on 'Log in' button | Inline error message is displayed, password field is cleared, and username is retained | high |
| TC005 |  | Attempt to add a block without Edit mode | User is on the Dashboard | 1. Click on '+ Add a block' button | No action is taken, and a message indicating Edit mode is required is displayed | medium |
| TC008 |  | Failing to create an assignment with missing required fields | User is in Assignment creation form | 1. Leave Assignment name field empty<br>2. Click 'Save and return to course' | Inline error message is displayed indicating that the Assignment name is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC003 |  | Login with empty username and password fields | User is on the login page | 1. Leave username field empty<br>2. Leave password field empty<br>3. Click on 'Log in' button | Inline error message is displayed for both fields | medium |
| TC006 |  | Adding a block in Edit mode | User is on the Dashboard, Edit mode is enabled | 1. Click on '+ Add a block' button<br>2. Select a block type from the list<br>3. Click 'Add' | Selected block is added to the Dashboard | medium |
| TC009 |  | Creating an assignment with maximum length name | User is in Assignment creation form | 1. Enter a maximum length string in the Assignment name field<br>2. Fill in other fields as needed<br>3. Click 'Save and return to course' | Assignment is created successfully with the maximum length name | medium |

---
