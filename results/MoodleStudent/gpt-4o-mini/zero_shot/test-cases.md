# Test Cases — 

Generated:   
Model:   

## MoodleStudent

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC001 |  | Successful login with valid credentials | User is on the login page, User has valid username and password | 1. Enter valid username<br>2. Enter valid password<br>3. Click on 'Log in' button | User is redirected to the Dashboard page with a personalized greeting | high |
| TC004 |  | View Dashboard with upcoming activities | User is logged in, User has upcoming activities in enrolled courses | 1. Navigate to Dashboard | Timeline block displays upcoming activities and deadlines | high |
| TC007 |  | View grades for enrolled course | User is logged in, User is enrolled in a course with grades | 1. Navigate to Grades page | User sees their grades displayed in the grade table | high |
| TC010 |  | Logout from the application | User is logged in | 1. Click on user initials icon<br>2. Select 'Log out' option | User is logged out and redirected to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC002 |  | Unsuccessful login with invalid credentials | User is on the login page, User has invalid username or password | 1. Enter invalid username<br>2. Enter invalid password<br>3. Click on 'Log in' button | Inline error message is displayed, password field is cleared, and username is retained | high |
| TC005 |  | Attempt to access Dashboard without logging in | User is not logged in | 1. Attempt to navigate to Dashboard | User is redirected to the login page | high |
| TC008 |  | Attempt to view grades without being enrolled in any course | User is logged in, User is not enrolled in any course | 1. Navigate to Grades page | User sees a message indicating no grades available | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC003 |  | Login with empty username and password fields | User is on the login page | 1. Leave username field empty<br>2. Leave password field empty<br>3. Click on 'Log in' button | Inline error message is displayed for both fields | medium |
| TC006 |  | Filter participants with no conditions applied | User is on the Participants page, User is logged in | 1. Click on 'Apply filters' without selecting any conditions | All participants are displayed without any filtering | medium |
| TC009 |  | View profile with maximum character limit in description | User is logged in, User has a profile description at maximum length | 1. Navigate to Profile page | Profile description is displayed correctly without truncation | low |

---
