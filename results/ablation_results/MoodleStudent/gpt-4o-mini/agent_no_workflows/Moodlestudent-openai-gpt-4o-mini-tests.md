# Test Cases — Moodlestudent

Generated: 2026-06-09T12:07:22.512223Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 1 | 2 | 0 | 2 | 0 | 2 | 0 | 0 |

## Grades

Total: **2** (positive: 0, negative: 2, edge: 0)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Attempt to access the Grades page without authentication |  | 1. Navigate to the Grades page | User is redirected to the login page | high |
| TC-002 |  | Attempt to view another student's grades |  | 1. Attempt to access the grades of another student | Access is denied; user cannot view grades of other students | high |

---
