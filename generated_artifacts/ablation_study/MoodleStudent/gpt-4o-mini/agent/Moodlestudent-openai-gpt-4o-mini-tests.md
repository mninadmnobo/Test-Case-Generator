# Test Cases — Moodlestudent

Generated: 2026-06-09T12:05:52.764248Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 3 | 6 | 4 | 2 | 0 | 5 | 1 | 0 |

## Grades

Total: **2** (positive: 2, negative: 0, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Display student's own grades in the Grades table | User logged in as <Student> | 1. Navigate to the Grades page | The Grades table displays the student's grades with the correct columns: Grade item, Calculated weight, Grade, Range, Percentage, Feedback, and Contribution to course total. | high |
| TC-002 |  | Check visibility of AGGREGATION Course total row | User logged in as <Student> | 1. Navigate to the Grades page | The AGGREGATION Course total row displays the cumulative grade across all weighted items. | high |

---

## Activities

Total: **3** (positive: 1, negative: 2, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Navigate to an activity's page from the Assignments section | User logged in as <Student>, Assignments section is visible | 1. Click on the activity name in the Assignments section | redirects to activity's page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to navigate to an activity without any activities listed |  | 1. Open the Activities page<br>2. Observe that there are no activities listed | No activities are displayed; user remains on the Activities page | high |
| TC-003 |  | Attempt to expand collapsed sections without any activities |  | 1. Open the Activities page<br>2. Click to expand the Forums section<br>3. Click to expand the Resources section | Sections expand but no content is displayed; user remains on the Activities page | medium |

---

## Logout

Total: **1** (positive: 1, negative: 0, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click the Logout button | terminates the current authenticated session and redirects to the login page | high |

---
