# Test Cases — Moodlestudent

Generated: 2026-06-09T12:08:14.405233Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 1 | 8 | 5 | 2 | 1 | 4 | 4 | 0 |

## Activities

Total: **8** (positive: 5, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Assignments Section | User logged in as Student, User on Activities page | 1. Observe the Assignments section<br>2. Check the displayed columns: Name, Due date, Submission status | Assignments section is visible with correct columns displayed | high |
| TC-002 | WF-001 | Navigate to Activity from Assignments | User logged in as Student, User on Activities page, At least one assignment is listed | 1. Click on the name of an assignment | User is redirected to the selected activity's page | high |
| TC-003 | WF-001 | Expand Forums Section | User logged in as Student, User on Activities page | 1. Click on the arrow to expand the Forums section | Forums section expands to show its contents | medium |
| TC-004 | WF-001 | Expand Resources Section | User logged in as Student, User on Activities page | 1. Click on the arrow to expand the Resources section | Resources section expands to show its contents | medium |
| TC-005 | WF-001 | Expand Additional Activity Types Section | User logged in as Student, User on Activities page | 1. Click on the arrow to expand the Additional Activity Types section | Additional Activity Types section expands to show its contents | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Check Empty Assignments Section | User logged in as Student, User on Activities page, No assignments available | 1. Observe the Assignments section | Assignments section displays a message indicating no assignments available | high |
| TC-008 | WF-001 | Check Disabled Navigation on Empty Assignments | User logged in as Student, User on Activities page, No assignments available | 1. Attempt to click on an assignment name | Navigation is disabled and no action occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Check Assignments Section Sorting | User logged in as Student, User on Activities page, Multiple assignments listed | 1. Click on the 'Due date' column header to sort assignments by due date | Assignments are sorted by due date in ascending order | medium |

---
