# Skill: Manual Correctness Verification (Success Rate)

**Description:** 
This skill defines the process for performing a manual "Correctness Verification" analysis. Because the Agentic Pipeline often discovers and generates far more valid edge cases than baseline ground truths, simply measuring coverage against a baseline is insufficient. Instead, we must manually inspect the generated test cases to verify their logical correctness. 

This verification checks three core components for hallucination or logical errors:
1. **Preconditions:** Are the preconditions valid and possible within the application state?
2. **Test Steps:** Are the steps logically sound, achievable, and grounded in the system's features?
3. **Expected Result:** Is the expected outcome correct according to the system's business rules?

## Inputs
1. **Functional Description:** `dataset/functional_description/[Dataset].md`
2. **Generated Test Cases:** `results/[Dataset]/[Model]/[Approach]/test-cases.md`

## Output
* **Verification Report File:** `results/[Dataset]/correctness_verification/cv-[dataset]-[model]-[approach].md`

---

## Detailed Step-by-Step Instructions

### 1. Review Generated Test Cases
*   Open the `test-cases.md` file for the specific model/approach.
*   Read through the test cases module by module. Keep the `functional_description.md` open as your single source of truth.

### 2. Critically Evaluate for Errors
For every test case, you must check for the following three types of errors. **If a test case fails in any of these, it is considered an incorrect test case.**

#### A. Precondition Errors
*   **What to check:** Does the test case assume a system state, user role, or prior data that is impossible or not supported by the application?
*   **Example of an Error:** The functional description for a basic login app only mentions standard users. A generated test case says: *Precondition: User is logged in as a Super Admin.* 
*   **Action:** Record this TC ID under Precondition Errors.

#### B. Test Steps Errors
*   **What to check:** Do the steps interact with UI elements, forms, or features that do not actually exist in the requirements? Are the steps illogical?
*   **Example of an Error:** The app only allows adding items to a cart. A generated test case says: *Step 3: Click the 'Export Cart to PDF' button.*
*   **Action:** Record this TC ID under Test Steps Errors.

#### C. Expected Result Errors
*   **What to check:** Does the expected outcome contradict the core business logic? Does it hallucinate a success message for an invalid flow?
*   **Example of an Error:** The requirement states "Passwords must be 8 characters". A generated negative test uses a 6-character password, but the expected result says: *System registers the user successfully.*
*   **Action:** Record this TC ID under Expected Result Errors.

### 3. Record Errors and Calculate Success Rate
*   Track the specific TC IDs that fail in each category. A single test case might fail in multiple categories (e.g., hallucinated step AND wrong expected result).
*   Count the **Unique** number of test cases that have at least one error.
*   Subtract this from the Total Generated Test Cases to find the Total Correct Test Cases.
*   Calculate the Success Rate: `(Correct Test Cases / Total Test Cases) * 100`

---

## Full Structured Example (Template)

```markdown
# Correctness Verification: [Dataset] ([Model] [Approach])

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

### Error Analysis

*   **Precondition Errors Total:** 2
    *   **Test Cases:** TC-012, TC-045
    *   *Reasoning:* TC-012 assumes an Admin role which does not exist. TC-045 assumes an account balance can be negative, which contradicts business logic.

*   **Test Steps Errors Total:** 1
    *   **Test Cases:** TC-034
    *   *Reasoning:* TC-034 instructs clicking an 'Export to Excel' button that is never mentioned in the functional requirements.

*   **Expected Result Errors Total:** 2
    *   **Test Cases:** TC-012, TC-091
    *   *Reasoning:* TC-012 expects an admin dashboard to load. TC-091 expects a 3-character password to be accepted despite the 8-character minimum requirement.

### Success Rate Calculation

*   **Total Generated Test Cases:** 100
*   **Total Test Cases with Errors:** 4 *(Note: TC-012 had both Precondition and Expected Result errors, so it counts as 1 unique error)*
*   **Total Correct Test Cases:** 96

**Overall Success Rate:** 96 / 100 (96.00%)
```

## Thesis Analysis
*   After calculating the success rate, briefly compare the findings to the thesis. For example, if the Agentic Pipeline achieved a 95% success rate while generating 230 tests, highlight how the pipeline successfully scaled its exploration without sacrificing logical correctness or hallucinating bloat.
