# Skill / SOP: Understanding and Calculating Test Coverage

This document defines what test coverage means in the context of comparing Agent-Generated (GEN) test suites against a structured Ground Truth (GT) suite. It outlines the factors to consider to ensure an accurate but fair gap analysis.

## 1. What is Coverage?
In this testing framework, **Coverage** is defined as the measure of *behavioral alignment* between the agent's output and the expected human-authored ground truth. It answers the question: "Did the agent independently discover and test the same business logic and edge cases that a human expert deemed necessary?"

Coverage is evaluated generously to account for agent behavior:
- **Covered (1):** The agent generated at least one test case that exercises the target observable behavior, a closely related behavior, or an edge case that implies the core functionality was tested. Partial coverage of UI elements also qualifies.
- **Missing / Gap (0):** The agent completely failed to interact with the target feature or generated a test that is entirely unrelated to the core semantic requirement.

---

## 2. Key Considerations When Calculating Coverage

### A. Semantic Equivalence vs. Textual Similarity
Never rely on keyword matching or superficial textual similarity. Agents frequently use different vocabulary or phrasing than the Ground Truth.
- **✅ Valid Match:** GT requires "Empty username rejected." GEN tests "Submit form with blank user ID." -> **COVERED.**
- **❌ Invalid Match:** GT requires "HTML/XSS injection in Profile Description is sanitised." GEN tests "Student cannot edit another user's profile." -> **MISSING.** (Both involve profile security, but test completely different technical behaviors).

### B. Core Boundaries vs. Generic Tests
A generic test case does not cover a specific boundary, negative, or edge-case test.
- **Example:** If the GT requires "Submit with invalid username format containing *special characters*", a GEN test that simply says "Submit with invalid credentials" does **NOT** cover it. The specific boundary condition (special characters) must be explicitly tested and asserted by the agent.

### C. Fixture and Data Agnosticism
Ignore the specific test data or fixture names used, provided they achieve the exact same logical outcome.
- If GT uses "Student A" and GEN uses "Test User 1", they are functionally equivalent.
- If GT tests clicking "Course 101" and GEN tests clicking "Math 102", they are functionally equivalent.

### D. Combined vs. Split Scenarios
Agents frequently structure their test steps differently from humans. Coverage is about the *behavior*, not the 1:1 mapping of test steps.
- **Combined Coverage:** If GEN has a single comprehensive test "Validate all required fields" that explicitly checks an empty username and an empty password, it successfully covers BOTH GT scenarios (Empty username, Empty password).
- **Split Coverage:** If GT has a single test "Verify login page elements visible" (checking cookies notice and lost password link), and GEN creates two separate tests doing the same, the single GT scenario is considered covered.

### E. Negative Assertions & State Checks
Pay close attention to tests verifying that something is *not* supposed to happen or *not* supposed to be visible.
- **Example:** If GT requires "Student cannot access Settings tab", the GEN test must explicitly check for the *absence* of the settings tab or a permission denial when trying to access it. A test that merely checks that "Course tabs are visible" without explicitly asserting the absence of the Settings tab does not cover the negative requirement.

### F. Equivalence Classes & Target Field Agnosticism
While behavioral strictness is required for edge cases, the *exact field* or *target element* being tested can be flexible if they belong to the same functional equivalence class and trigger the exact same underlying logic.
- **✅ Valid Match:** GT requires "Leave *First name* blank and attempt to Update profile" (testing required field validation). GEN tests "Attempt to save profile with a required field (*Email*) left empty." -> **COVERED.** (Both test the core behavior of blocking a save when a mandatory profile field is empty).
- **✅ Valid Match:** GT tests "Collapse the *Forums* activity group." GEN tests "Collapse the *Assignments* activity group." -> **COVERED.** (Both test the accordion collapse functionality).

---

### G. Implied and Partial Coverage
To accommodate the agent's exploratory nature, partial or implied coverage is acceptable.
- **Implied Coverage:** If a generated test interacts with a core component or tests a complex edge case of a feature (e.g., searching with special characters), it implicitly covers the basic functional requirement of that feature (e.g., standard search).
- **Partial Element Coverage:** If a GT scenario requires verifying multiple UI elements are displayed, an agent test that explicitly verifies a subset of those elements is considered to cover the scenario.

## 3. Avoiding Extreme "Hallucinated" Mappings
While the rules are relaxed, avoid completely hallucinated mappings. If an agent tests a purely visual layout aspect, it shouldn't count for a complex business logic requirement. However, reasonable associations between tested behaviors and GT requirements should be accepted.

Always ask: *Does the generated test interact with the same core feature and achieve a similar functional validation?* If yes, it is covered.
