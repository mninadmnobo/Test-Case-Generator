# Test Cases — Moodleteacher

Generated: 2026-06-09T11:54:17.635107Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 2 | 10 | 6 | 3 | 1 | 4 | 6 | 0 |

## Dashboard

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Course Edit Mode and Activity Chooser

Total: **10** (positive: 6, negative: 3, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Enable Edit Mode | User logged in as Instructor, Course page is open | 1. Click on the 'Edit Mode' button | The Course page turns into an authoring interface | high |
| TC-002 | WF-002 | Add Activity using Activity Chooser | User logged in as Instructor, Edit Mode is enabled | 1. Click on the '+ Add an activity or resource' button<br>2. Select 'Assignment' tile<br>3. Click 'Add' | Activity creation form for 'Assignment' opens | high |
| TC-003 | WF-003 | Batch Delete Activities | User logged in as Instructor, Multiple activities are selected | 1. Click on 'Batch Delete' in the Bulk Actions Toolbar<br>2. Confirm deletion | Selected activities are deleted from the Course page | medium |
| TC-007 | WF-007 | Add Subsection | User logged in as Instructor, Edit Mode is enabled | 1. Click on the '+ Add a subsection' button | A new subsection is created and visible in the Course page | medium |
| TC-008 | WF-008 | Batch Move Activities | User logged in as Instructor, Multiple activities are selected | 1. Click on 'Batch Move' in the Bulk Actions Toolbar<br>2. Select destination for moving | Selected activities are moved to the specified destination | medium |
| TC-009 | WF-009 | Edit Activity Settings | User logged in as Instructor, Edit Mode is enabled, Activity exists | 1. Click on the activity's three-dot menu<br>2. Select 'Edit Settings' | Activity settings form opens for editing | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-004 | Attempt to Add Activity without Edit Mode | User logged in as Instructor, Course page is open but Edit Mode is disabled | 1. Click on the '+ Add an activity or resource' button | Button is disabled or no action occurs | high |
| TC-005 | WF-005 | Search for Non-existent Activity | User logged in as Instructor, Edit Mode is enabled | 1. Click on the '+ Add an activity or resource' button<br>2. Enter 'Non-existent Activity' in the search field | No results found message is displayed | medium |
| TC-010 | WF-010 | Attempt to Batch Delete without Selection | User logged in as Instructor, Edit Mode is enabled | 1. Click on 'Batch Delete' in the Bulk Actions Toolbar | No action occurs or an error message is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-006 | Add Activity with Empty Search Field | User logged in as Instructor, Edit Mode is enabled | 1. Click on the '+ Add an activity or resource' button<br>2. Leave the search field empty<br>3. Click 'Search' | All activity/resource tiles are displayed | medium |

---
