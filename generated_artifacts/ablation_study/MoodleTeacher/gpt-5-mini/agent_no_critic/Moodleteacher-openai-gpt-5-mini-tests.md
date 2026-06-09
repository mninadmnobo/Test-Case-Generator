# Test Cases — Moodleteacher

Generated: 2026-06-09T11:58:25.426015Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 7 | 64 | 22 | 23 | 19 | 28 | 29 | 7 |

## Login

Total: **9** (positive: 0, negative: 6, edge: 3)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit with Username left blank (representative text required-field) | User is on the Login page and unauthenticated | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click the Log in button | Inline validation error appears on the Username field indicating it is required; form does not submit and there is no redirect to Dashboard; Password field is cleared; Username remains blank and highlighted as required. | high |
| TC-002 | WF-001 | Submit with Password left blank (password required-field representative) | User is on the Login page and unauthenticated | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Log in button | Inline validation error appears on the Password field indicating it is required; form does not submit and there is no redirect to Dashboard; Password field remains empty; Username field retains the entered value. | high |
| TC-003 | WF-001 | Submit with all required fields empty | User is on the Login page and unauthenticated | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Log in button | Inline validation errors appear on both Username and Password fields indicating they are required; form does not submit and there is no redirect to Dashboard; Password field remains cleared/empty; Username remains blank. | high |
| TC-004 | WF-001 | Attempt login with invalid credentials (authentication failure) | User is on the Login page and unauthenticated | 1. Enter <username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Log in button | Inline authentication error is displayed (login fails); Password field is cleared; Username field retains the entered value for correction; form does not redirect to Dashboard and no session is granted. | high |
| TC-005 | WF-002 | Attempt 'Access as a guest' while authenticated (precondition not met) | User is authenticated and on the Login page | 1. Attempt to locate the 'Access as a guest' button on the page<br>2. If the button is visible, click the 'Access as a guest' button | The 'Access as a guest' control is not available for authenticated users (button is not visible or is disabled); clicking it does not grant a guest session or navigate; the user remains authenticated and on the current page. | high |
| TC-006 |  | Click disabled 'Lost password?' link when feature is turned off | User is on the Login page and unauthenticated | 1. Attempt to click the 'Lost password?' link | The 'Lost password?' link is disabled/unavailable on this site (control is disabled and not clickable); clicking it does not navigate or open a recovery flow; there is no change of page or state. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-001 | Username with leading and trailing whitespace is handled | Login page is displayed, An existing account exists with username <username> and password <password> | 1. Click the Username field<br>2. Type the Username value with one or more leading and trailing space characters (i.e. ' <username> ')<br>3. Click the Password field<br>4. Type <password> into the Password field<br>5. Click the 'Log in' button | If the system trims leading/trailing whitespace from Username: the page redirects to the Dashboard (succeeds). If the system does not trim: the form submission is blocked with the inline error message shown; the Password field is cleared; the Username field retains the entered value including leading/trailing whitespace (is blocked / error shown). | medium |
| TC-008 (input_edge) | WF-001 | Credentials that include emoji and special characters are accepted when account exists | Login page is displayed, An existing account exists whose Username and Password include special characters and emoji (e.g. Username contains emoji/special characters, Password contains emoji/special characters) | 1. Click the Username field<br>2. Enter the account's Username (contains emoji/special characters)<br>3. Click the Password field<br>4. Enter the account's Password (contains emoji/special characters)<br>5. Click the 'Log in' button | Form submits successfully and redirects to the Dashboard (succeeds). | medium |
| TC-009 (interaction_edge) | WF-001 | Rapid double-click of 'Log in' does not cause duplicate navigation or duplicate session creation | Login page is displayed, A valid account exists with Username <username> and Password <password> | 1. Click the Username field<br>2. Enter <username> into the Username field<br>3. Click the Password field<br>4. Enter <password> into the Password field<br>5. Click the 'Log in' button twice rapidly (two clicks within one second) | Only a single successful submission is processed: the browser performs a single redirect to the Dashboard (succeeds); no duplicate Dashboard pages or duplicate sessions are created; no duplicate error messages are shown. | medium |

---

## Assignment Creation

Total: **15** (positive: 7, negative: 8, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Create assignment using 'Save and return to course' with required fields | User logged in as <Teacher>, required fields must be valid | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. Click 'Save and return to course' | creates the assignment and redirects to the course page | high |
| TC-002 |  | Create assignment using 'Save and display' and open new assignment page | User logged in as <Teacher>, required fields must be valid | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. Click 'Save and display' | creates the assignment and opens the new assignment's page | high |
| TC-003 |  | Cancel assignment creation discards edits | User logged in as <Teacher> | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. Click 'Cancel' | discards all changes | medium |
| TC-004 |  | Enable File submissions to reveal and set file-related controls, then save and display | User logged in as <Teacher>, required fields must be valid | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. In the 'Submission Types' panel, check the 'File submissions' checkbox<br>4. Enter <maximum number> in Maximum number of uploaded files<br>5. Enter <maximum size> in Maximum submission size<br>6. Enter/select <Accepted_file_types> in Accepted file types<br>7. Click 'Save and display' | creates the assignment and opens the new assignment's page; the Submission Types section on the assignment page shows File submissions enabled with the configured Maximum number of uploaded files, Maximum submission size, and Accepted file types | medium |
| TC-005 |  | Enable availability toggles and set dates, then save and display | User logged in as <Teacher>, required fields must be valid | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. In the 'Availability' panel, check 'Allow submissions from' toggle and set <Allow_submissions_from><br>4. Check 'Due date' toggle and set <Due_date><br>5. (optional) Check 'Cut-off date' toggle and set <Cut_off_date><br>6. Click 'Save and display' | creates the assignment and opens the new assignment's page; the Availability section on the assignment page shows the entered <Allow_submissions_from> and <Due_date> (and <Cut_off_date> if set) | medium |
| TC-006 |  | Enable group submissions, configure grouping and require-all setting, then save and display | User logged in as <Teacher>, required fields must be valid | 1. Click 'Assignment' in the Activity chooser<br>2. Enter <Assignment name> in the Assignment Name field<br>3. In the 'Group Submission Settings' panel, check 'Group submissions'<br>4. Select <Grouping_selection> in the Grouping selection control<br>5. Check 'Require all group members to submit' (enabled when Group submissions is checked)<br>6. Click 'Save and display' | creates the assignment and opens the new assignment's page; the assignment page shows Group submissions enabled with the selected <Grouping_selection> and 'Require all group members to submit' set | medium |
| TC-007 |  | Add an access restriction via the '+ Add restriction' picker | User logged in as <Teacher> | 1. Click 'Assignment' in the Activity chooser<br>2. Scroll to the 'Access Restrictions' panel<br>3. Click the '+ Add restriction' button to open the Restriction Type picker<br>4. In the Restriction Type picker, select <Restriction_Type><br>5. Enter <Restriction_Parameters> if applicable<br>6. Click 'Add restriction' in the picker | adds a restriction instance to Assignment_Creation_Form.Restrictions; a new restriction appears in the Access Restrictions list displaying the selected <Restriction_Type> | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Submit with required Assignment Name left blank (Save and return to course) | User is on the Assignment Creation form | 1. Leave the Assignment Name field blank<br>2. Click the 'Save and return to course' button | Inline validation error appears on the Assignment Name field indicating it is required; the form does not submit; the page remains on the Assignment Creation form (no redirect to course page) | high |
| TC-009 |  | Submit with ALL required fields empty (Save and display) | User is on the Assignment Creation form, No restrictions have been added | 1. Ensure the Assignment Name field is blank (no required fields filled)<br>2. Click the 'Save and display' button | Inline validation error appears on the Assignment Name field indicating it is required; the form does not submit; the page remains on the Assignment Creation form (no assignment page opened) | high |
| TC-010 |  | Add restriction: required Restriction Type left blank in picker dialog | User is on the Assignment Creation form | 1. Click '+ Add restriction' to open the Restriction Type picker<br>2. Leave the Restriction Type field blank in the picker<br>3. Click the 'Add restriction' button in the picker | Inline validation error appears on the Restriction Type field inside the picker indicating it is required; the picker remains open; no restriction is added to the Assignment Creation form's Restrictions list | high |
| TC-011 |  | Enable Due date but leave Due date blank and submit | User is on the Assignment Creation form | 1. Toggle Due_date_Enabled to ON<br>2. Leave the Due date field blank<br>3. Click the 'Save and return to course' button | Inline validation error appears on the Due date field indicating a date/time is required when Due date is enabled; the form does not submit; the page remains on the Assignment Creation form | high |
| TC-012 |  | Enter invalid date format into Due date when enabled | User is on the Assignment Creation form | 1. Toggle Due_date_Enabled to ON<br>2. Enter <invalid date format> into the Due date field<br>3. Click the 'Save and display' button | Inline validation error appears on the Due date field indicating the entered value is not a valid date/time format; the form does not submit; no assignment page opens | medium |
| TC-013 |  | Non-numeric input in numeric field 'Maximum points' | User is on the Assignment Creation form | 1. Enter <non-numeric input> into the Maximum points field<br>2. Click the 'Save and return to course' button | Inline validation error appears on the Maximum points field stating it must be a number; the form does not submit; the page remains on the Assignment Creation form | medium |
| TC-014 |  | Non-numeric input in file-submission numeric field shown only when File submissions enabled | User is on the Assignment Creation form | 1. Check the File_submissions checkbox to reveal file-related controls<br>2. Enter <non-numeric input> into the Maximum submission size field<br>3. Click the 'Save and display' button | Inline validation error appears on the Maximum submission size field stating it must be a number; the form does not submit; no assignment page opens | medium |
| TC-015 |  | Attempt to set Maximum number of uploaded files while File submissions is disabled (control should not be available) | User is on the Assignment Creation form, File_submissions checkbox is unchecked | 1. Attempt to enter a value into the Maximum number of uploaded files control while File_submissions is unchecked | Maximum number of uploaded files control is not visible/accessible when File_submissions is unchecked; user cannot enter a value into it (no input field present or it is disabled) | medium |

---

## Participants Management

Total: **11** (positive: 0, negative: 5, edge: 6)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-002 | Enrol users: leave User Search blank and submit | User is logged in and on the Participants page, Enrol users dialog is opened | 1. Click the 'Enrol users' button to open the Enrol Users dialog<br>2. Leave the User Search field blank<br>3. In the Role dropdown, select <a valid role><br>4. Click the 'Confirm' button | Inline validation error appears on the User Search field indicating it is required; the Enrol Users dialog remains open; no user is added to the course. | high |
| TC-002 | WF-002 | Enrol users: leave Role blank and submit | User is logged in and on the Participants page, Enrol users dialog is opened | 1. Click the 'Enrol users' button to open the Enrol Users dialog<br>2. In the User Search field, select <a user from search results><br>3. Leave the Role dropdown blank / unselected<br>4. Click the 'Confirm' button | Inline validation error appears on the Role field indicating it is required; the Enrol Users dialog remains open; the selected user is not enrolled in the course. | high |
| TC-003 | WF-002 | Enrol users: submit with all required dialog fields empty | User is logged in and on the Participants page, Enrol users dialog is opened | 1. Click the 'Enrol users' button to open the Enrol Users dialog<br>2. Leave the User Search field blank<br>3. Leave the Role dropdown blank / unselected<br>4. Click the 'Confirm' button | Inline validation errors appear on both User Search and Role fields indicating they are required; the Enrol Users dialog remains open; no user is enrolled and no changes are applied. | high |
| TC-004 | WF-012 | Bulk actions: attempt to open 'With selected users…' when no users are selected (precondition not met) | User is logged in and on the Participants page, No participant checkboxes are selected | 1. Ensure zero participant checkboxes are selected in the Participants table<br>2. Click the 'With selected users…' dropdown | The 'With selected users…' control is disabled or otherwise not actionable when no participants are selected; clicking does not open the bulk actions menu and a visible helper/tooltip indicates that at least one participant must be selected to use bulk actions. | high |
| TC-005 | WF-012 | Bulk actions timing: verify bulk actions are blocked immediately when selection precondition is false | User is logged in and on the Participants page, No participant checkboxes are selected | 1. Ensure zero participant checkboxes are selected in the Participants table<br>2. Focus the 'With selected users…' control (keyboard or mouse) and attempt to activate it (press Enter or click)<br>3. Attempt to select a bulk action option (if the menu appears) | Bulk actions are not accessible while no users are selected: the menu does not present actionable options (options are absent or greyed out) and a visible helper/inline message indicates selection of at least one user is required; no bulk action can be executed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) | WF-001 | Very long string entered into Enrol Users search is retained and executed | Participants page is open, "Enrol users" button is visible | 1. Click the "Enrol users" button<br>2. Enter a very long string (200+ characters) into the User_Search field<br>3. Observe the User_Search input field and the dialog search results area | The User_Search input retains the full entered string with no visible truncation and the dialog search executes; if there are no matches the dialog shows zero result rows and a visible empty-state message (search executes and input retention succeeds). | low |
| TC-007 (input_edge) | WF-001 | Leading/trailing whitespace in User_Search is trimmed and still matches existing user | Participants page is open, There is an existing user whose searchable identifier will match the trimmed input, "Enrol users" dialog is open | 1. Enter a username with leading and trailing whitespace into the User_Search field<br>2. Press Enter (or trigger the search action) | Leading and trailing whitespace is trimmed by the search; the trimmed value is used for matching and the existing user appears in the results list (search succeeds). | medium |
| TC-008 (interaction_edge) | WF-002 | Rapid double-click Confirm in Enrol Users dialog prevents duplicate enrollment | Participants page is open, "Enrol users" dialog is open, User appears in the dialog search results, A Role is available to select | 1. Select the target user from the dialog search results<br>2. Select a Role from the Role dropdown<br>3. Click the Confirm button twice in rapid succession | The Confirm action succeeds once and the second submission attempt is blocked; only one new participant entry for that user appears in the Participants table (second click is blocked / error shown if a duplicate would occur). | medium |
| TC-009 (interaction_edge) | WF-012 | Opening bulk actions after deselecting all is blocked when no users selected | Participants page is open, At least one selectable participant row is present | 1. Select a participant's checkbox in the Participants table<br>2. Deselect that same participant's checkbox so zero participants are selected<br>3. Click the "With selected users…" dropdown | Opening the bulk actions is blocked; the dropdown does not open and displays a visible disabled state or tooltip indicating that at least one user must be selected (attempt to open bulk actions is blocked). | medium |
| TC-010 (data_edge) | WF-004 | Apply First_Name_Initial_Filter = 'All' returns the unfiltered full list | Participants page is open, Participants table contains multiple users with various first-name initials | 1. Select 'All' in the First_Name_Initial_Filter dropdown<br>2. Click the Apply filters button | Apply filters succeeds; the Participants table displays the full, unfiltered list of users (the filter action succeeds and the participants table shows all rows). | low |
| TC-011 (interaction_edge) | WF-006 | Add multiple filter conditions then Clear filters removes all condition rows and Apply filters succeeds | Participants page is open, Filter system is visible | 1. Click the '+ Add condition' button<br>2. Click the '+ Add condition' button (second time)<br>3. Click the '+ Add condition' button (third time)<br>4. Click the 'Clear filters' button<br>5. Click the 'Apply filters' button | All condition rows are removed by Clear filters and Apply filters succeeds with zero conditions; the Participants table shows the unfiltered list and no validation error is shown (applying with zero conditions succeeds). | low |

---

## Assignment — Teacher View

Total: **4** (positive: 0, negative: 0, edge: 4)

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 (interaction_edge) | WF-001 | Double-click Grade button for the same student rapidly | Teacher is signed in and on the Assignment — Teacher View page, A student row with a visible Grade button exists for the assignment | 1. Click the Grade button for the student<br>2. Immediately click the same Grade button again within a short interval (e.g., before the modal finishes animating) | Only one Grading_Interface modal is visible; the second click is ignored (no duplicate modals or duplicate grading contexts are created) — succeeds | medium |
| TC-002 (interaction_edge) | WF-001 | Attempt to navigate tabs while Grading_Interface modal is open | Teacher is signed in and on the Assignment — Teacher View page, A student row with a visible Grade button exists for the assignment | 1. Click the Grade button for the student to open the Grading_Interface modal<br>2. Click the Submissions tab in the tab bar while the Grading_Interface modal is visible | Tab navigation is blocked while the Grading_Interface modal is open; Submissions tab content is not displayed and the Grading_Interface modal remains visible (is blocked) | medium |
| TC-003 (input_edge) | WF-002 | Assignment description with very long text and special characters/emoji is displayed | An assignment exists whose description contains a very long string (200+ characters) including special characters and emoji, Teacher is signed in and on the Assignment — Teacher View page | 1. Open the Assignment tab | Assignment tab displays the full description text including special characters and emoji; the text is not truncated in the visible description area and attached files (if any) are listed — succeeds | medium |
| TC-004 (input_edge) |  | Assignment description containing leading and trailing whitespace is rendered | An assignment exists whose description includes visible leading and trailing whitespace (spaces or blank lines) around the main text, Teacher is signed in and on the Assignment — Teacher View page | 1. Open the Assignment tab | Displayed description does not show unintended leading/trailing blank space in the page layout; leading/trailing whitespace is normalized/trimmed for display so no extra blank lines appear at the start or end of the description — succeeds | low |

---

## Assignment Submissions

Total: **2** (positive: 0, negative: 2, edge: 0)

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Attempt to edit Final Grade while Quick grading is disabled | User is viewing the Submissions view | 1. Navigate to the Submissions view<br>2. Ensure the Quick_Grading_Mode checkbox is unchecked (click it if it is checked)<br>3. Click the Final_Grade cell for any student row in the Submissions_Table | Final_Grade cell is not editable: no inline grade input or edit controls appear; clicking the cell does not open an editor; the displayed Final_Grade value remains unchanged (inline grading is disabled when Quick_Grading_Mode == false). | high |
| TC-002 |  | Begin inline edit, then disable Quick grading and attempt to save | User is viewing the Submissions view | 1. Navigate to the Submissions view<br>2. Ensure the Quick_Grading_Mode checkbox is checked (click it if it is unchecked)<br>3. Click the Final_Grade cell for a student row to open the inline grade editor<br>4. Without saving, click the Quick_Grading_Mode checkbox to uncheck it (disable Quick grading)<br>5. While the inline editor is still visible, attempt to save the inline grade (press Enter or click the inline Save control) | Save is blocked and inline editing is cancelled: the inline grade editor closes or becomes read-only immediately after Quick_Grading_Mode is unchecked; the Final_Grade value remains unchanged; no grade update is submitted (Quick_Grading_Mode disabling prevents inline grade submission). | high |

---

## Profile

Total: **18** (positive: 10, negative: 2, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open messaging composer from Profile via Message button | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Message button | Messaging composer opened | high |
| TC-002 | WF-002 | Open Edit Profile page from Profile | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Edit profile link in the User details card | Edit Profile page opened | high |
| TC-003 | WF-003 | Open Data retention summary from Privacy and policies card | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Data retention summary link in the Privacy and policies card | Data retention summary page opened | medium |
| TC-004 | WF-004 | Open a Course profile from the Course details list | User logged in as <teacher>, <at least one course profile associated with the teacher> | 1. Navigate to the Profile page<br>2. Click one of the Course profile links in the Course details card | Course profile page opened | high |
| TC-005 | WF-005 | Open Blog entries from Miscellaneous links | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Blog entries link in the Miscellaneous card | Blog entries page opened | medium |
| TC-006 | WF-006 | Open Forum posts from Miscellaneous links | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Forum posts link in the Miscellaneous card | Forum posts page opened | medium |
| TC-007 | WF-007 | Open Forum discussions from Miscellaneous links | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Forum discussions link in the Miscellaneous card | Forum discussions page opened | medium |
| TC-008 | WF-008 | Open Learning plans from Miscellaneous links | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Learning plans link in the Miscellaneous card | Learning plans page opened | medium |
| TC-009 | WF-009 | Open Browser sessions report from Reports card | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Browser sessions link in the Reports card | Browser sessions page opened | high |
| TC-010 | WF-010 | Open Grades overview report from Reports card | User logged in as <teacher> | 1. Navigate to the Profile page<br>2. Click the Grades overview link in the Reports card | Grades overview page opened | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Unauthenticated user cannot view Profile page | User is not authenticated / not logged in | 1. Open the Profile page URL for <teacher> (navigate to the Profile page while not logged in) | The Login page is displayed; Profile page content (initials icon, full name, information cards) is not visible or accessible. The user is not able to interact with Profile controls (e.g., Message, Edit profile). | high |
| TC-012 | WF-001 | Unauthenticated click on Message button is blocked and redirects to login | User is not authenticated / not logged in | 1. Open the Profile page URL for <teacher> while not logged in<br>2. Click the Message button on the Profile page | User is redirected to the Login page; the messaging composer is not opened and no messaging UI appears. The Profile's Message action does not complete and no composer is visible. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-004 | Profile page with exactly zero Course_Profiles (minimum boundary) | Test account exists with zero associated course profiles, User is signed in | 1. Navigate to the Profile page | Page renders successfully; Course details card shows exactly zero Course_Profile_Link entries (no links listed). The empty state for Course details is visible (no course links shown) — view succeeds. | medium |
| TC-014 (boundary) | WF-004 | Profile page with one Course_Profile entry (one above minimum) | Test account exists with exactly one associated course profile, User is signed in | 1. Navigate to the Profile page<br>2. Observe the Course details card and count the Course_Profile_Link entries<br>3. Click the single Course_Profile_Link | Course details card shows exactly one Course_Profile_Link entry (count = 1) and page interaction succeeds; clicking the link navigates to the corresponding course profile page (navigation succeeds and course profile page opens). | medium |
| TC-015 (input_edge) | WF-002 | Edit profile — very long profile description (render/truncation edge) | User is signed in and on their Profile page | 1. Click the Edit profile link<br>2. In the profile description field, enter a very long string (200+ characters)<br>3. Click Save (or Update) on the Edit Profile page<br>4. Return to the Profile page (if not auto-redirected) | Save action succeeds. On the Profile page the saved description is visible. If the UI truncates long descriptions, a visibly truncated string with an ellipsis is shown in the Profile card; otherwise the full long description is shown. There is a clear visible indicator (truncation or full text) — save succeeds and the final rendered state is observable. | low |
| TC-016 (input_edge) | WF-002 | Edit profile — full name with emoji and special/unicode characters | User is signed in and on their Profile page | 1. Click the Edit profile link<br>2. In the full name field, enter a name containing emoji and non-ASCII unicode characters<br>3. Click Save (or Update) on the Edit Profile page<br>4. Return to the Profile page (if not auto-redirected) | Save action succeeds; Profile page displays the saved full name. The special/unicode characters and emoji are rendered visibly (unicode supported) or, if the UI cannot render them, a visible replacement/escaping is shown. The saved value is visible on the Profile page — save succeeds. | low |
| TC-017 (interaction_edge) | WF-001 | Rapid repeat-click on Message button (duplicate composer prevention) | User is signed in and on their Profile page, Messaging feature is available for the user | 1. Click the Message button<br>2. Immediately click the Message button again (within a short interval) | First click opens the messaging composer (succeeds). The second click does not create a second composer instance; either focus returns to the already-open composer or the second click is ignored. Only one messaging composer instance is visible; duplicate composers are not created (subsequent clicks are effectively blocked/ignored). | medium |
| TC-018 (interaction_edge) | WF-004 | Rapid double-click on a Course_Profile_Link (single navigation enforcement) | User is signed in and Profile page shows at least one Course_Profile_Link | 1. On the Profile page, rapidly click the same Course_Profile_Link twice (double-click or two quick clicks) | Single navigation occurs to the course profile page (navigation succeeds once). The second rapid click does not cause a duplicate navigation or an application error; only one course profile page is opened/loaded and no duplicate requests produce visible errors. | medium |

---

## Profile Edit

Total: **5** (positive: 5, negative: 0, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Update required General fields and save | User logged in as <User>, Profile Edit page is open with existing profile data for <User> | 1. If the General section is collapsed, expand it (click the section header) or click 'Expand all' to reveal it<br>2. Enter <new First name> in the First name field<br>3. Enter <new Last name> in the Last name field<br>4. Enter <valid email> in the Email address field<br>5. Click the 'Update profile' button | Profile page refreshes and displays the updated First name, updated Last name, and the updated Email address entered in the form | high |
| TC-002 |  | Upload a valid profile picture via drag-and-drop and save | User logged in as <User>, Profile Edit page is open with an existing profile picture for <User> | 1. Click the 'Expand all' link to reveal the User picture section<br>2. Drag and drop a <valid image file> into the Picture upload area<br>3. Enter <picture description> in the Picture description field<br>4. Click the 'Update profile' button | Profile page refreshes and shows the new profile picture thumbnail in place of the previous picture and displays the Picture description entered | high |
| TC-003 |  | Add interests using the tag-based input and save | User logged in as <User>, Profile Edit page is open for <User> | 1. Click the 'Expand all' link or expand the Interests section to reveal the Interests field<br>2. Enter <interest tag 1> in the Interests field and confirm (e.g., press Enter)<br>3. Enter <interest tag 2> in the Interests field and confirm (optional)<br>4. Click the 'Update profile' button | Profile page refreshes and displays the added interest tag(s) on the profile | medium |
| TC-004 |  | Use 'Expand all' to reveal every collapsible section | User logged in as <User>, Profile Edit page is open with sections collapsed by default | 1. Click the 'Expand all' link at the top right of the form | All collapsible sections (General, User picture, Additional names, Interests, Optional fields) are expanded and fields within each section are visible | low |
| TC-005 |  | Cancel edits and return to profile view without saving | User logged in as <User>, Profile Edit page is open with existing profile data for <User> | 1. In the General section, enter <new First name> in the First name field<br>2. Click the 'Cancel' button | User is returned to the profile view page and the profile displays the original First name and Last name unchanged (the edits are not present) | high |

---
