# Test Cases — Moodleteacher

Generated: 2026-06-09T12:05:06.151192Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 2 | 20 | 10 | 4 | 6 | 11 | 8 | 1 |

## Dashboard — Edit Mode

Total: **20** (positive: 10, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Enable Edit mode shows edit controls | User logged in as Student, Dashboard has at least one block | 1. Navigate to Dashboard<br>2. Toggle 'Edit mode' checkbox to ON | Dashboard switches to Edit state: 'Reset page to default' button visible top-right; '+ Add a block' button visible below the Dashboard heading; each existing block shows move handle and three-dot options menu | high |
| TC-002 | WF-001 | Disable Edit mode hides edit controls | User logged in as Student, Dashboard currently in Edit mode | 1. Navigate to Dashboard<br>2. Toggle 'Edit mode' checkbox to OFF | Dashboard switches to View state: 'Reset page to default' and '+ Add a block' are not visible; move handles and three-dot options are not visible on blocks | medium |
| TC-004 | WF-002 | Open Add a block page from '+ Add a block' in Edit mode | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Navigate to Dashboard<br>2. Click '+ Add a block' button | Add a block page opens listing all available block types (Comments, Course overview, Latest announcements, Latest badges, Learning plans, Logged in user, Mentees, Online users, Private files, Random glossary entry, Recently accessed courses, Starred courses, Tags, Text, Upcoming events) and shows 'Add selected block' button and 'Cancel' link | high |
| TC-006 | WF-002 | Add a new block (Text) from Add a block page | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Navigate to Dashboard<br>2. Click '+ Add a block'<br>3. Select 'Text' from the list of block types<br>4. Click 'Add selected block' button | The selected 'Text' block is added to the user's dashboard (visible in the Blocks container) and layout change persists for the current user (block remains after page reload) | high |
| TC-007 | WF-003 | Cancel Add a block returns to Dashboard without changes | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Navigate to Dashboard<br>2. Click '+ Add a block'<br>3. Click 'Cancel' link at the bottom of Add a block page | Returns to Dashboard view in Edit mode and no new block is added to the Blocks container | high |
| TC-008 | WF-006 | Open Configure for a block from options menu | User logged in as Student, Dashboard in Edit mode (Edit mode ON), At least one block present | 1. Navigate to Dashboard<br>2. For a block, open the three-dot options menu<br>3. Click 'Configure' option | Block configuration UI opens for that block (configuration panel/modal/page is displayed) | high |
| TC-009 | WF-006 | Delete a block from options menu | User logged in as Student, Dashboard in Edit mode (Edit mode ON), At least one block present | 1. Navigate to Dashboard<br>2. For a block, open the three-dot options menu<br>3. Click 'Delete' option | The block is removed from the Blocks container and the layout change persists for the current user (block remains removed after page reload) | high |
| TC-010 | WF-006 | Initiate move via options menu 'Move' action | User logged in as Student, Dashboard in Edit mode (Edit mode ON), At least two blocks present | 1. Navigate to Dashboard<br>2. For a block, open the three-dot options menu<br>3. Click 'Move' option<br>4. Complete the move as prompted by the UI (if move mode requires additional steps) | Move mode is initiated or block is reordered as appropriate and layout change persists for the current user | medium |
| TC-011 | WF-005 | Drag reorder blocks using move handle | User logged in as Student, Dashboard in Edit mode (Edit mode ON), At least two blocks present | 1. Navigate to Dashboard<br>2. Use move handle on a block to drag it to a new position within the Blocks container<br>3. Release to drop the block | Blocks reorder visually to reflect new order and layout change persists for the current user (order remains after page reload) | high |
| TC-012 | WF-004 | Reset page to default reverts user layout | User logged in as Student, Dashboard in Edit mode (Edit mode ON), User layout differs from default | 1. Navigate to Dashboard<br>2. Click 'Reset page to default' button at top-right<br>3. Confirm reset if a confirmation is shown | Layout reverts to the default dashboard for the current user: any added/removed/reordered blocks are restored to default positions; change persists for the current user (after reload remains default) | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-008 | Attempt edit-only actions when Edit mode is off are blocked/invisible | User logged in as Student, Dashboard in View state (Edit mode OFF) | 1. Navigate to Dashboard<br>2. Attempt to locate or click '+ Add a block' button<br>3. Attempt to click move handle on a block<br>4. Attempt to open three-dot options menu on a block | No edit-only UI elements are available: '+ Add a block' not visible; move handles and options menus are not visible and cannot be interacted with | medium |
| TC-005 | WF-002 | '+ Add a block' not available when Edit mode is off | User logged in as Student, Dashboard in View state (Edit mode OFF) | 1. Navigate to Dashboard<br>2. Look for '+ Add a block' button below the Dashboard heading | '+ Add a block' button is not present in the UI and cannot be clicked | medium |
| TC-016 | WF-002 | Attempt to add a block without selecting a Block Type (validation) | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Navigate to Dashboard<br>2. Click '+ Add a block'<br>3. Do NOT select any block type<br>4. Click 'Add selected block' button | Add action is blocked and a validation error is shown indicating 'Block Type' is required; no block is added to the Dashboard | high |
| TC-018 | WF-005 | Attempt to drag reorder when Edit mode is off fails | User logged in as Student, Dashboard in View state (Edit mode OFF), At least two blocks present | 1. Navigate to Dashboard<br>2. Attempt to drag a block by where the move handle would appear (move handle should not be visible) | No drag handle is present; user cannot start a drag reorder action; blocks remain in original order | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 | WF-007 | Layout changes persist across sessions for the same user | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. While logged in, add a 'Text' block and reorder blocks<br>2. Save changes implicitly (by UI persistence) and log out<br>3. Log back in as the same user and navigate to Dashboard | The added block and reordering persist and are visible after login (layout retained for the same user) | high |
| TC-014 | WF-007 | Layout changes isolated per user (user B unaffected by user A changes) | User A and User B have separate accounts, User A has modified their dashboard layout | 1. Log in as User A and add or reorder blocks<br>2. Log out<br>3. Log in as User B and navigate to Dashboard | User B sees their own dashboard layout (no changes made by User A are visible to User B) | high |
| TC-015 | WF-002 | Add the same block type twice | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Navigate to Dashboard<br>2. Click '+ Add a block'<br>3. Select 'Text' and click 'Add selected block'<br>4. Repeat steps 2-3 to add another 'Text' block | Both 'Text' blocks are added to the Blocks container (duplicates allowed) and both persist for the current user | medium |
| TC-017 | WF-002 | Add a large number of blocks (scale test) | User logged in as Student, Dashboard in Edit mode (Edit mode ON) | 1. Repeat: Click '+ Add a block', select 'Text', click 'Add selected block' until 100 blocks have been added<br>2. Observe UI responsiveness and layout after additions | 100 blocks are added to the Blocks container; UI remains responsive and displays scroll/overflow as appropriate; layout changes persist for the current user | medium |
| TC-019 | WF-006 | Delete all blocks until Blocks container is empty | User logged in as Student, Dashboard in Edit mode (Edit mode ON), One or more blocks present | 1. Navigate to Dashboard<br>2. For each block, open three-dot options and click 'Delete' until no blocks remain<br>3. Reload the page | All blocks are removed; Blocks container displays an empty state (no blocks visible); the empty layout persists for the current user after reload | medium |
| TC-020 | WF-004 | Click Reset when no changes made (no-op) | User logged in as Student, Dashboard in Edit mode (Edit mode ON), User layout is already default | 1. Navigate to Dashboard<br>2. Click 'Reset page to default' button at top-right | Action completes with no visible layout changes (no-op) and dashboard remains in default layout; user remains on Dashboard in Edit mode | low |

---

## Course Page

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times
