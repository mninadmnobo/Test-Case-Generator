# Test Cases — 

Generated:   
Model:   

## MoodleStudent

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Log in with valid credentials | A registered student account exists | 1. Navigate to the Moodle login page<br>2. Enter <valid username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | User is redirected to the Dashboard with a personalized greeting | high |
| P-002 |  | View the Dashboard and see upcoming activities | User logged in as Student, There are upcoming activities in enrolled courses | 1. Navigate to the Dashboard<br>2. Observe the Timeline block | The Timeline block displays a list of upcoming activities | high |
| P-003 |  | Submit an assignment using the online text editor | User logged in as Student, An assignment with online text submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <submission text> in the online text editor<br>4. Click 'Save changes' | Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the submission time | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Attempt to log in with an empty username |  | 1. Navigate to the Moodle login page<br>2. Leave the Username field empty<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | An inline error message is displayed; the Password field is cleared | high |
| N-002 |  | Attempt to filter the Timeline block with no activities | User logged in as Student, No activities are due within the next 7 days | 1. Navigate to the Dashboard<br>2. In the Timeline block, select 'Next 7 days' from the time range dropdown | An empty state message is displayed indicating no upcoming activities | high |
| N-003 |  | Attempt to submit an assignment without any text | User logged in as Student, An assignment with online text submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Leave the online text editor empty<br>4. Click 'Save changes' | An inline error message is displayed indicating that submission cannot be empty | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Log in with a username that is at the maximum length | A registered student account exists with maximum length username | 1. Navigate to the Moodle login page<br>2. Enter <maximum length username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | User is redirected to the Dashboard with a personalized greeting | medium |
| E-002 |  | Filter the My Courses page with a very long search term | User logged in as Student, Multiple courses are available | 1. Navigate to the My Courses page<br>2. Enter <very long search term> in the search field<br>3. Click 'Search' | The system processes the search and displays relevant courses or a message indicating no results | medium |
| E-003 |  | Submit an assignment with maximum length text | User logged in as Student, An assignment with online text submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <maximum length submission text> in the online text editor<br>4. Click 'Save changes' | Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the submission time | medium |

---
