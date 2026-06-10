# Test Cases — 

Generated:   
Model:   

## MoodleTeacher

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| P-001 |  | Log in with valid credentials | User is on the login page | 1. Enter a valid Username<br>2. Enter a valid Password<br>3. Click 'Log in' | User is redirected to the Dashboard with a personalized greeting | high |
| P-002 |  | Create a new course successfully | User logged in as Teacher, User is on the Dashboard | 1. Click on 'My Courses'<br>2. Click on 'Add a new course'<br>3. Fill in the required fields: Course full name, Course short name, Course category<br>4. Click 'Save and display' | The new course appears in the My Courses page | high |
| P-003 |  | View assignment submissions | User logged in as Teacher, An assignment exists with submissions | 1. Navigate to the Course page<br>2. Click on the assignment link<br>3. Click on the 'Submissions' tab | The submissions table displays all student submission records | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| N-001 |  | Attempt to log in with invalid credentials | User is on the login page | 1. Enter an invalid Username<br>2. Enter an invalid Password<br>3. Click 'Log in' | An inline error message is displayed; the password field is cleared, and the username remains | high |
| N-002 |  | Attempt to create a course without required fields | User logged in as Teacher, User is on the Dashboard | 1. Click on 'My Courses'<br>2. Click on 'Add a new course'<br>3. Leave the Course full name field empty<br>4. Click 'Save and display' | An inline validation error highlights the Course full name field; the form is not submitted and remains open | high |
| N-003 |  | Attempt to view submissions for an assignment with no submissions | User logged in as Teacher, An assignment exists with no submissions | 1. Navigate to the Course page<br>2. Click on the assignment link<br>3. Click on the 'Submissions' tab | An empty state message is displayed indicating no submissions exist | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| E-001 |  | Log in with maximum length username and password | User is on the login page | 1. Enter a username with maximum allowed length<br>2. Enter a password with maximum allowed length<br>3. Click 'Log in' | User is redirected to the Dashboard with a personalized greeting | medium |
| E-002 |  | Create a course with maximum length name | User logged in as Teacher, User is on the Dashboard | 1. Click on 'My Courses'<br>2. Click on 'Add a new course'<br>3. Enter a Course full name with maximum allowed length<br>4. Fill in other required fields<br>5. Click 'Save and display' | The new course is created successfully and appears in the My Courses page | medium |
| E-003 |  | View submissions with maximum number of students enrolled | User logged in as Teacher, An assignment exists with maximum allowed submissions | 1. Navigate to the Course page<br>2. Click on the assignment link<br>3. Click on the 'Submissions' tab | The submissions table displays all student submission records without performance issues | medium |

---
