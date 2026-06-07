# Skill / SOP: Understanding, Calculating, and Writing a Test Coverage Plan

This document defines what test coverage means in the context of comparing Agent-Generated (GEN) test suites against a structured Ground Truth (GT) suite, and outlines the standard operating procedure (SOP) for analyzing and authoring a test coverage report.

## 1. What is Coverage?
In this testing framework, **Coverage** is defined as the measure of *behavioral alignment* between the agent's output and the expected human-authored ground truth. It answers the question: "Did the agent independently discover and test the same business logic and edge cases that a human expert deemed necessary?"

Coverage is evaluated generously to account for agent behavior:
- **Covered (1):** The agent generated at least one test case that exercises the target observable behavior, a closely related behavior, or an edge case that implies the core functionality was tested. Partial coverage of UI elements also qualifies.
- **Missing / Gap (0):** The agent completely failed to interact with the target feature or generated a test that is entirely unrelated to the core semantic requirement.

## 2. Relaxed Coverage Calculation (Core Definitions)
When evaluating whether a generated test covers a Ground Truth scenario, apply the following relaxed rules:
- **Behaviour Match:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same, similar, or an implied observable behaviour.
- **Implied and Partial Coverage:** If an agent tests a specific edge case of a feature, it implicitly covers the basic functional test of that feature. Similarly, testing a subset of UI elements covers a general "elements displayed" requirement.
- **Ignore Fixtures:** Ignore exact fixture names or string variables (e.g., using "Test User" instead of "Student A") unless they fundamentally change the business logic.

## 3. Key Considerations When Calculating Coverage

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

### G. Implied and Partial Coverage
To accommodate the agent's exploratory nature, partial or implied coverage is acceptable.
- **Implied Coverage:** If a generated test interacts with a core component or tests a complex edge case of a feature (e.g., searching with special characters), it implicitly covers the basic functional requirement of that feature (e.g., standard search).
- **Partial Element Coverage:** If a GT scenario requires verifying multiple UI elements are displayed, an agent test that explicitly verifies a subset of those elements is considered to cover the scenario.

### H. Avoiding Extreme "Hallucinated" Mappings
While the rules are relaxed, avoid completely hallucinated mappings. If an agent tests a purely visual layout aspect, it shouldn't count for a complex business logic requirement. However, reasonable associations between tested behaviors and GT requirements should be accepted.

Always ask: *Does the generated test interact with the same core feature and achieve a similar functional validation?* If yes, it is covered.

## 4. Fixed Document Structure
A proper coverage report must be written in Markdown and contain the following exact sections in order. Do not deviate from this fixed structure.

### A. Header & Metadata
Include the Ground Truth version, the Generated Suite name (and total case count), the Analysis Date, and a brief statement defining the coverage rules.

### B. Executive Summary
A high-level markdown table summarizing the macro metrics:
- GT total cases
- GT cases covered by GEN
- GT cases not covered by GEN
- Overall coverage percentage
- GEN cases with no GT counterpart (extras)

### C. Per-Module Coverage
A summary table breaking down the coverage metrics module by module (e.g., Login, Dashboard, My Courses). Columns must include:
`Module` | `GT Cases` | `Covered` | `Not Covered` | `Coverage %`

### D. Missing Scenarios (Gaps)
A detailed bulleted list of all GT test cases that were entirely absent from the generated suite, grouped by module.
**Format:**
```markdown
### [Module Name] ([X] missing)
- [GT-ID] [Test Case Name]
```
*(Note: Do not include a detailed table mapping all covered cases. Only document the gaps to keep the report concise and actionable.)*

### E. Extra Scenarios
Document the test cases generated by the agent that exceed the scope of the Ground Truth. Group them by module using bullet points. Include the approximate count of extra types.
**Format:**
```markdown
### [Module Name] (~[X] extra types)
- [Brief description of the extra test case]
```

## 5. Tone and Formatting Guidelines
- **Strict Adherence:** The format must perfectly match the bulleted structure. Do not introduce redundant mapping tables.
- **Active Voice:** Write "The agent missed the unauthenticated redirect" rather than "The unauthenticated redirect was missed by the agent."
- **Clear Assertions:** Avoid speculative language. If a test is missing, state it clearly based on behavioral analysis.
- **Avoid Cliché AI-isms:** Do not use excessive em-dashes. Avoid starting paragraphs with filler transition words ("Furthermore", "Moreover", "In conclusion").

## 6. Generic Example Template

Below is a complete, generic example of how a coverage report must be formatted:

```markdown
# Test Coverage Report

**Ground Truth:** ExampleApp GT v1.0  
**Generated Suite:** openai/gpt-X — 100 cases  
**Analysis Date:** 2026-06-07  
**Coverage Definition:** A GT scenario is *covered* if the generated suite contains at least one test exercising the same observable behaviour, regardless of fixture names or implementation wording.

---

## Executive Summary

| Metric | Value |
|--------|-------|
| GT total cases | 50 |
| GT cases covered by GEN | 40 |
| GT cases not covered by GEN | 10 |
| **Overall coverage** | **80.0%** |
| GEN cases with no GT counterpart (extras) | ~15 |

---

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|--------|----------|---------|-------------|------------|
| Authentication | 20 | 18 | 2 | **90%** |
| Dashboard | 30 | 22 | 8 | **73%** |
| **Total** | **50** | **40** | **10** | **80.0%** |

---

## Missing Scenarios (Gaps)

The following GT test cases were entirely absent from the generated suite:

### Authentication (2 missing)
- AUTH-005 Submit with invalid username format containing special characters
- AUTH-012 Rapid double submission of login form

### Dashboard (8 missing)
- DASH-001 Dashboard page loads with user information visible
- DASH-007 Dashboard blocked while unauthenticated
- [ ... additional missing cases ... ]

---

## Extra Scenarios

The agent generated the following cases that had no direct equivalent in the GT scope:

### Authentication (~1 extra types)
- "Lost password?" link is disabled under specific conditions

### Dashboard (~5 extra types)
- Block drag handles functionality
- Calendar import/export functionality
- [ ... additional extra cases ... ]
```
