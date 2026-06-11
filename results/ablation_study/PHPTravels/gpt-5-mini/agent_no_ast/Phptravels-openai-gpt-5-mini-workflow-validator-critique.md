# Workflow Critique — Phptravels

Generated: 2026-06-10T20:50:48.879676Z

## Home Page & Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows contain conditional_branch expressions that reference fields/states not present in the AST (AST has no components); regenerate with correct conditions or update the AST.

**Missing workflows:**

- Workflow WF-001 conditional_branch references non-existent field 'active_tab' (active_tab == Hotels).
- Workflow WF-002 conditional_branch references non-existent fields 'active_tab' and 'Trip_Type' (active_tab == Flights AND Trip_Type == One-way).
- Workflow WF-003 conditional_branch references non-existent fields 'active_tab' and 'Trip_Type' (active_tab == Flights AND Trip_Type == Round-trip).
- Workflow WF-004 conditional_branch references non-existent fields 'active_tab' and 'Trip_Type' (active_tab == Flights AND Trip_Type == Multi-city).
- Workflow WF-005 conditional_branch references non-existent field 'active_tab' (active_tab == Tours).
- Workflow WF-006 conditional_branch references non-existent field 'active_tab' (active_tab == Cars).

**Phantom workflows:** none

**Fixes applied:**

- Add UI components to the AST for the search widget and its tab state: define a field (or visible_when) for 'active_tab' with possible values Hotels, Flights, Tours, Cars so conditional_branch expressions can reference it.
- Add the Flights form fields to the AST including a 'Trip_Type' field with possible values One-way, Round-trip, Multi-city so workflows WF-002, WF-003, WF-004 can validate against real fields.
- Regenerate workflows after updating the AST so conditional_branch expressions reference real AST fields (or remove conditional_branch from workflows if tab/state is not modeled).
- For each workflow (WF-001..WF-006) either: (a) keep the terminal_action='Search' but update conditional_branch to reference the exact AST field names/state keys, or (b) remove the conditional_branch if the module will not model tab/state in the AST.
- If the AST intentionally remains empty, remove these workflows (WF-001..WF-006) because their conditional branches reference nonexistent fields — regenerate workflows consistent with the empty AST.

---

## User Registration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list is empty but the description defines a registration form with multiple terminal outcomes (successful create + auto-login or create + require email verification) and several validation-failure paths that are missing.

**Missing workflows:**

- Form (Registration) — terminal_action=Create Account (auto-login and redirect to dashboard) missing
- Form (Registration) — terminal_action=Create Account (email verification required; prompt to verify email) missing
- Form (Registration) — terminal_action=Show validation errors: required fields missing (e.g., First Name/Last Name/Email/Password/Terms unchecked) missing
- Form (Registration) — terminal_action=Show validation errors: password mismatch missing
- Form (Registration) — terminal_action=Show validation errors: invalid email format missing
- Form (Registration) — terminal_action=Show validation errors: email already in use (uniqueness violation) missing

**Phantom workflows:** none

**Fixes applied:**

- Add an AST form node for the registration form (e.g., components.registration_form) if it is missing so workflows can be tied to it.
- Regenerate workflows to include one workflow for the successful submit that results in account creation with auto-login and redirect to dashboard (terminal_action name should match AST submit_actions).
- Regenerate workflows to include one workflow for the successful submit that results in account creation but requires email verification (terminal_action should reflect 'require email verification' outcome).
- Regenerate workflows for each validation failure path separately: required fields missing, password mismatch, invalid email format, and email already in use — each should have a distinct conditional_branch referencing the real field/validation flag (e.g., password_match == false, email_valid == false, email_unique == false, terms_accepted == false).
- Ensure each workflow's on_success matches the concrete on_success behavior described in the AST/description (e.g., redirect to dashboard or show verification prompt) rather than a generic single-word value.

---

## User Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows contain conditional_branch expressions that reference fields or state keys not present in the provided AST (which has no components), so the workflow list must be regenerated after the AST is corrected.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- WF-001 conditional_branch 'Credentials == Valid' references field 'Credentials' which is not defined in the AST; add a login form component with appropriate visible_when/required_when fields or remove/replace this conditional_branch.
- WF-002 conditional_branch 'Credentials == Invalid' references field 'Credentials' which is not defined in the AST; add the login form and explicit credential validation states or remove/replace this conditional_branch.
- WF-003 conditional_branch 'Multiple_Consecutive_Failed_Attempts == true' references a state/field not present in the AST; either add a field/state representing failed attempt count/CAPTCHA visibility (e.g., captcha_required visible_when) or remove/replace this conditional_branch.
- WF-004 terminal_action 'Forgot Password?' is referenced in the description but the AST has no components; ensure the AST includes the login form with a 'Forgot Password?' link action in the form's submit_actions/links so the workflow maps to an AST action.
- WF-005 conditional_branch 'Google_Login_Enabled == true' references a flag not in the AST; add a property or visible_when condition for social login enablement (Google) in the AST or remove/replace this conditional_branch.
- WF-006 conditional_branch 'Facebook_Login_Enabled == true' references a flag not in the AST; add a property or visible_when condition for social login enablement (Facebook) in the AST or remove/replace this conditional_branch.
- Regenerate the workflows after updating the AST to include a login form component (fields: Email, Password, Remember Me), submit_actions containing 'Login', an explicit action or link for 'Forgot Password?', optional social login buttons (Google, Facebook) with visible_when flags, and a mechanism/state for CAPTCHA visibility after failed attempts so conditional_branch expressions can be validated and workflows mapped to AST actions.

---

## Forgot Password

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference a conditional_branch field 'email_found' that does not exist in the AST and the AST contains no form node for the Reset Password action, so the workflows cannot be validated.

**Missing workflows:**

- AST has no form node for the email reset flow (no submit_actions including 'Reset Password') — workflows cannot be validated against a missing form.
- conditional_branch references unknown field 'email_found' in WF-001 (Submit valid email (reset link sent))
- conditional_branch references unknown field 'email_found' in WF-002 (Submit unknown email (error shown))

**Phantom workflows:** none

**Fixes applied:**

- Add a form component to the AST (e.g., components.reset_password_form) with a submit_actions array including 'Reset Password' and an 'email' field so the Reset Password workflows can be validated.
- Model the branching in the AST: add a visible_when/required_when condition or a field/state named 'email_found' (with possible values true/false), so conditional_branch expressions 'email_found == true' and 'email_found == false' reference a real field/state.
- Alternatively, remove the conditional_branch from the workflows and instead represent the two outcomes as separate submit action variants tied to concrete AST form conditions; then regenerate the workflow list after updating the AST.

---

## Hotels Search & Listing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional branches/state/fields that do not exist in the AST and several terminal actions are not explicitly present in the AST or description (phantoms); regenerate after fixing these issues.

**Missing workflows:**

- Workflow WF-008 conditional_branch references unknown field 'Price_Filter' (terminal_action=Remove Price Filter).
- Workflow WF-009 conditional_branch references unknown field 'Star_Filter' (terminal_action=Remove Star Filter).
- Workflow WF-010 conditional_branch references unknown field 'Facility_Filter' (terminal_action=Remove Facility Filter).
- Workflow WF-011 conditional_branch references unknown field 'HotelType_Filter' (terminal_action=Remove Hotel Type Filter).
- Workflow WF-012 conditional_branch references unknown field 'BoardBasis_Filter' (terminal_action=Remove Board Basis Filter).
- Workflow WF-013 conditional_branch references unknown field 'Any_Filter_Active' (terminal_action=Reset All Filters).

**Phantom workflows:**

- WF-003 terminal_action='Apply Price Range' not found in AST and not explicitly named in the description text.
- WF-004 terminal_action='Toggle Star Rating' not found in AST and not explicitly named in the description text.
- WF-005 terminal_action='Toggle Facility Filter' not found in AST and not explicitly named in the description text.
- WF-006 terminal_action='Select Hotel Type' not found in AST and not explicitly named in the description text.
- WF-007 terminal_action='Select Board Basis' not found in AST and not explicitly named in the description text.

**Fixes applied:**

- For WF-008: either add 'Price_Filter' as a visible/required field or state in the AST, or remove/replace the conditional_branch from the workflow.
- For WF-009: either add 'Star_Filter' as a visible/required field or state in the AST, or remove/replace the conditional_branch from the workflow.
- For WF-010: either add 'Facility_Filter' as a visible/required field or state in the AST, or remove/replace the conditional_branch from the workflow.
- For WF-011: either add 'HotelType_Filter' as a visible/required field or state in the AST, or remove/replace the conditional_branch from the workflow.
- For WF-012: either add 'BoardBasis_Filter' as a visible/required field or state in the AST, or remove/replace the conditional_branch from the workflow.
- For WF-013: either add 'Any_Filter_Active' (or equivalent combined filter-active indicator) to the AST, or remove/replace the conditional_branch from the workflow.
- For WF-003, WF-004, WF-005, WF-006, WF-007: ensure the exact terminal_action labels appear in the AST (e.g., as submit_actions/row_actions/available_actions) or make the description explicitly name these actions; otherwise remove or rename these workflows to match AST/description.

---

## Hotel Details & Booking

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

WF-002 uses a conditional_branch referencing a non-existent field/state and there is no workflow handling Book Now when the user is not logged in; regenerate workflows after fixing the AST or workflows.

**Missing workflows:**

- WF-002 conditional_branch references non-existent field 'User_Logged_In' (no such field or state in AST)
- No workflow for terminal_action='Book Now' when User_Logged_In == false (should redirect to login or prompt authentication)

**Phantom workflows:** none

**Fixes applied:**

- Add 'User_Logged_In' boolean field/state to the AST (for example as part of the booking form's visible_when/required_when or as a state in a state_bound_action_bar) so WF-002's conditional_branch is valid, or update WF-002 to reference an existing AST field/state.
- Add a workflow for terminal_action='Book Now' with conditional_branch 'User_Logged_In == false' that redirects the user to the login page or shows the login prompt (name the workflow and terminal action accordingly).
- Ensure the AST includes the booking form component with submit_actions including 'Book Now' and that there is at least one workflow per visibility/requirement condition × submit_action (e.g., logged-in Book Now -> proceed to payment; logged-out Book Now -> prompt login).

---

## Flights Search & Listing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Some terminal actions in the workflow list cannot be matched to the provided AST or to explicit action verbs in the description and must be corrected or the AST must be updated.

**Missing workflows:** none

**Phantom workflows:**

- WF-004 terminal_action='Apply Airline filter' not found in AST and not explicitly present as an action verb in the description
- WF-005 terminal_action='Apply Stops filter' not found in AST and not explicitly present as an action verb in the description

**Fixes applied:**

- Update the Structural Model AST to include filter components (e.g., a data_table/sidebar_filters node) with explicit actions matching 'Apply Airline filter' and 'Apply Stops filter', or
- Rename the workflow terminal_action values to match explicit verbs present in the description (e.g., use 'Select Airline filter' or 'Choose Airline' and 'Select Stops filter' / 'Choose Number of Stops') so they clearly appear in the description text, and regenerate workflows.
- Ensure all terminal_action strings in workflows exactly match action names in the AST nodes' action arrays (submit_actions[], row_actions[], bulk_actions[], available_actions[]) before regenerating.

---

## Flight Booking

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference a conditional_branch field that does not exist in the AST (AST is empty); regenerate after adding form fields or remove/replace invalid conditional branches.

**Missing workflows:**

- WF-001 conditional_branch references unknown field 'booking_form.all_required_fields_valid'
- WF-002 conditional_branch references unknown field 'booking_form.all_required_fields_valid'
- AST missing form component 'booking_form' and its fields (title, first_name, last_name, date_of_birth, passport_number, passport_expiry, lead_email, lead_phone, meal_preferences, seat_selection) and submit_actions including 'Continue'

**Phantom workflows:** none

**Fixes applied:**

- Add a 'booking_form' form node to the AST with explicit field definitions (title, first_name, last_name, date_of_birth, passport_number, passport_expiry, lead_email, lead_phone, meal_preferences, seat_selection), validation rules, and a submit_actions array containing 'Continue'; then regenerate workflows so conditional_branch uses an actual field (e.g., booking_form.all_required_fields_valid) or multiple workflows cover each visible/required condition.
- Alternatively, remove or replace the conditional_branch 'booking_form.all_required_fields_valid' from WF-001 and WF-002 with a condition that references an existing AST field or leave conditional_branch null if not modelled; then regenerate workflows.
- Ensure regenerated workflows include one workflow per form.submit_action and per visible/required condition combination (e.g., valid submission -> Continue -> proceed to payment; invalid submission -> Continue -> inline errors shown).

---

## Tours Search & Listing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows use conditional_branch conditions that reference fields or states not present in the AST, so the workflow list must be regenerated to match the structural model.

**Missing workflows:**

- Workflow WF-006 conditional_branch references field 'Filter == Destination' which does not exist in AST visible_when/required_when or state keys
- Workflow WF-007 conditional_branch references field 'Filter == Tour_Type' which does not exist in AST visible_when/required_when or state keys
- Workflow WF-008 conditional_branch references field 'Filter == Price_Range' which does not exist in AST visible_when/required_when or state keys
- Workflow WF-009 conditional_branch references field 'Filter == Duration' which does not exist in AST visible_when/required_when or state keys
- Workflow WF-010 conditional_branch references field 'Filter == Departure_Dates' which does not exist in AST visible_when/required_when or state keys

**Phantom workflows:** none

**Fixes applied:**

- Remove or correct conditional_branch values for WF-006 through WF-010 to reference real field names defined in the AST (visible_when/required_when) or add those filter fields into the AST before regenerating workflows
- If the design intent is to have unconditional filter actions, set conditional_branch to null for WF-006 through WF-010 and regenerate
- If the AST should include a search form and filter fields, update the AST to include the form and filter field definitions (destination, tour_type, price_range, duration, departure_dates) and then regenerate workflows so conditional branches align with AST

---

## Tour Details & Booking

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Conditional branches reference an undefined field/state ('user_authenticated') in the AST; workflows must be regenerated after fixing AST or conditions.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- WF-001: conditional_branch 'user_authenticated == true' references undefined field/state 'user_authenticated' — either add this field/state to the AST (e.g., model authentication state or visible_when/required_when entry) or remove/replace the conditional; ensure the AST includes the booking form with submit_action 'Book Now' so a matching workflow can be validated.
- WF-002: conditional_branch 'user_authenticated == false' references undefined field/state 'user_authenticated' — either add this field/state to the AST or remove/replace the conditional; also ensure the AST explicitly represents the redirect-to-login behavior (as an action or in description) so the terminal action can be validated.

---

## Cars Search & Listing

**Verdict:** yes  
**Forced ship:** no  

Workflows match the description and there are no missing or phantom workflows relative to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Car Booking

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional fields that do not exist in the AST (Terms_Accepted, Invalid_Fields); regenerate with AST-aligned conditions or add the missing form and fields.

**Missing workflows:**

- Conditional branch references unknown field: Terms_Accepted
- Conditional branch references unknown field: Invalid_Fields

**Phantom workflows:** none

**Fixes applied:**

- Add a booking form component to the AST (e.g., components.booking_form) with submit_actions including 'Confirm Booking' and explicit form fields: Driver_Full_Name, Age, License_Number, License_Issue_Country, Email, Phone, Addons (GPS, Child_Seat, Additional_Driver), Insurance_Plan, Terms_Accepted (boolean). Ensure workflows' conditional_branch expressions use these exact field names.
- If 'Invalid_Fields' is intended as an AST-visible flag, add it to the form (or model) as a boolean or represent validation via per-field validation rules and update workflows to reference those actual field names or validation-visible flags.
- Alternatively, remove or replace the workflows' conditional_branch clauses so they don't reference non-existent fields (or mirror the real visible_when/required_when/state keys present in the regenerated AST).

---

## Visa Services

**Verdict:** yes  
**Forced ship:** no  

Workflow list matches the description and AST (no missing required workflows or phantom actions detected).

**Missing workflows:** none

**Phantom workflows:** none

---

## User Dashboard

**Verdict:** yes  
**Forced ship:** no  

All provided workflows correspond to actions described in the functional description, there are no AST components requiring additional workflows, and no phantom or incorrect conditional workflows were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Booking Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional fields/states that do not exist in the AST (AST is empty) and must be reconciled or the workflows regenerated.

**Missing workflows:**

- Workflow WF-001 conditional_branch references unknown fields: Booking_Type_Allows_Modify, Cancellation_Policy_Allows_Modify (no corresponding visible_when/required_when or state in AST).
- Workflow WF-002 conditional_branch references unknown fields: Booking_Type_Allows_Modify, Cancellation_Policy_Allows_Modify (no corresponding visible_when/required_when or state in AST).
- Workflow WF-003 conditional_branch references unknown fields: Booking_Type_Allows_Modify, Cancellation_Policy_Allows_Modify (no corresponding visible_when/required_when or state in AST).
- Workflow WF-004 conditional_branch references unknown fields: Booking_Type_Allows_Cancellation, Cancellation_Policy_Allows_Cancellation (no corresponding visible_when/required_when or state in AST).
- AST is empty but workflows describe interactive components (Modify and Cancel flows); corresponding AST components (forms, form.submit_actions, or state_bound_action_bar entries) are missing.

**Phantom workflows:** none

**Fixes applied:**

- Add the referenced conditional fields or states to the AST: define visible_when/required_when boolean fields (Booking_Type_Allows_Modify, Cancellation_Policy_Allows_Modify, Booking_Type_Allows_Cancellation, Cancellation_Policy_Allows_Cancellation) on the relevant form or component, or add a state_bound_action_bar with matching state keys. This will allow the existing workflows' conditional_branch values to validate.
- Alternatively, if those condition names are incorrect, update the workflows to use the actual field/state names present in the AST.
- Populate the AST with components that represent the Modify and Cancel flows (e.g., forms or wizards for Modify with submit_actions: 'Change Travel Dates', 'Add Special Requests', 'Update Traveler Information'; a cancellation confirmation form with submit_action 'Confirm Cancellation'), so each workflow terminal_action maps to an AST action.
- If the module intentionally has no AST components, remove these workflows and regenerate from the (empty) AST or provide a correct AST that matches the described behaviors.

---

## Payment Processing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional fields/states that do not exist in the provided AST (no components or fields defined); regenerate after adding those fields/components or removing the invalid conditional branches.

**Missing workflows:**

- Conditional branch references unknown field 'Payment_Method' (used by WF-001, WF-002, WF-003, WF-004, WF-005)
- Conditional branch references unknown field 'Save_Card' (used by WF-001, WF-002)
- Conditional branch references unknown field/state 'Payment_Result' (used by WF-006)

**Phantom workflows:** none

**Fixes applied:**

- Define the 'Payment_Method' field or state in the AST (e.g., a form select or state key) so workflows WF-001..WF-005 can validly reference it, or remove/replace 'Payment_Method' references in workflows.
- Add the 'Save_Card' form field to the card payment form in the AST (used by WF-001 and WF-002), or remove/replace the Save_Card conditional in those workflows.
- Add a 'Payment_Result' state or field (or a state_bound_action_bar) to the AST to support WF-006's conditional_branch, or change WF-006 to use an existing AST condition.
- If these terminal actions (e.g., 'Complete payment (redirect to booking confirmation)', 'Show payment error and allow Retry') are intended to come from specific form submit_actions or state/row actions, add corresponding submit_actions/available_actions entries to the appropriate AST nodes so workflows map to real AST actions.

---

## Currency & Language Selection

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the actions described in the functional description (Update Currency and Switch Language); no missing workflows, phantom workflows, wrong conditional branches, or empty on_success issues were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Search & Filters

**Verdict:** yes  
**Forced ship:** no  

Workflow list appears complete and correct: no missing workflows, phantoms, or invalid conditional branches were detected against the provided AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Reviews & Ratings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference conditional fields and states that do not exist in the provided AST (empty), so the workflow list must be regenerated after the AST is fixed.

**Missing workflows:**

- Workflow WF-001 (terminal_action=Filter Reviews): conditional_branch references unknown field(s): ['Filter']
- Workflow WF-002 (terminal_action=Filter Reviews): conditional_branch references unknown field(s): ['Filter']
- Workflow WF-003 (terminal_action=Filter Reviews): conditional_branch references unknown field(s): ['Filter']
- Workflow WF-004 (terminal_action=Submit Review): conditional_branch references unknown field(s): ['Entry_Point','User_Authenticated','Booking_Status']
- Workflow WF-005 (terminal_action=Submit Review): conditional_branch references unknown field(s): ['Entry_Point','User_Authenticated','Booking_Status']

**Phantom workflows:** none

**Fixes applied:**

- Add AST definitions for the filter control and its possible values (e.g., a list/listing component or form control with a field named 'Filter' and possible values 'Rating','Date','Traveler_Type'), OR remove/replace references to 'Filter' in the workflows' conditional_branch expressions.
- Add AST entries for authentication and booking state fields used by the review submission flows: define fields or visible_when/required_when entries for 'Entry_Point', 'User_Authenticated', and 'Booking_Status' (or model the submission as a form node with visible_when conditions reflecting these fields), OR remove/replace those conditions in the workflows.
- Add a form node in the AST representing the Review Submission form with submit_actions including 'Submit Review' (and visible_when/required_when conditions that match the intended preconditions: authenticated + completed booking), so form submit workflows can be validated.
- Add a list/data_table or listing component in the AST for the Reviews list and/or filter controls so 'Filter Reviews' can be validated as an action on that component.
- After updating the AST (adding the fields/components above), regenerate workflows so conditional_branch expressions reference real AST fields and each form/list action maps to an AST action.

---

## Offers & Deals

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows use conditional_branch fields or states that do not exist in the provided AST; regenerate with valid conditions or update the AST.

**Missing workflows:**

- Workflow WF-001: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')
- Workflow WF-002: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')
- Workflow WF-003: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')
- Workflow WF-004: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')
- Workflow WF-005: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')
- Workflow WF-006: conditional_branch references unknown fields 'Service_Type' and 'BookNow_Behavior' (terminal_action='Book Now')

**Phantom workflows:** none

**Fixes applied:**

- WF-001: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.
- WF-002: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.
- WF-003: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.
- WF-004: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.
- WF-005: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.
- WF-006: Add 'Service_Type' and 'BookNow_Behavior' to the AST (with values e.g., Hotels/Flights/Packages and Apply_Promo_Code/Redirect_PreFilled_Search), or remove/adjust the conditional_branch and regenerate workflows.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: the single 'Logout' workflow matches the description and there are no AST components requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---
