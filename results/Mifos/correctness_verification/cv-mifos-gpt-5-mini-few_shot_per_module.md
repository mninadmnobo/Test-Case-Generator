# Correctness Verification: Mifos (gpt-5-mini — few_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Mifos/gpt-5-mini/few_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Mifos.md`  
**Total Generated Test Cases:** 503  
**Modules Covered:** 32 Mifos Modules

---

## Error Analysis

### A. Precondition Errors

**Total:** 4

- **TC IDs:** Loan Account TC-011 *(Mobile Money API)*, Savings Account TC-010 *(Mobile Money API)*
- *Reasoning:*
  - Preconditions assumed the configuration of an M-Pesa / Mobile Money gateway which was absent from the specific deployment spec provided.

---

### B. Test Steps Errors

**Total:** 4

- **TC IDs:** Reports TC-011 *(Export to XML)*, Users & Roles TC-012 *(OAuth config)*
- *Reasoning:*
  - Instructs exporting standard reports to XML (only CSV/PDF are defined) and configuring OAuth providers inside standard Role creation.

---

### C. Expected Result Errors

**Total:** 3

- **TC IDs:** Fixed Deposit TC-009 *(Early withdrawal auto-penalty)*
- *Reasoning:*
  - Asserts a specific mathematical auto-penalty is immediately deducted upon a button click, misunderstanding the manual override steps required in the Fineract UX for early withdrawal penalties.

---

## Success Rate Calculation

- **Total Generated Test Cases:** 503
- **Total Test Cases with Errors:** 11
- **Total Correct Test Cases:** 492

**Overall Success Rate: 492 / 503 (97.81%)**

---

## Thesis Analysis

The GPT-5-mini Few-Shot Per Module approach achieved a strong **97.81% correctness rate** with only 11 errors. However, its total valid volume of 492 test cases covers less than 80% of the 607-case ground truth limit, proving that static few-shot prompting fails to trigger deep exploratory behavior in highly complex, multi-module enterprise systems.
