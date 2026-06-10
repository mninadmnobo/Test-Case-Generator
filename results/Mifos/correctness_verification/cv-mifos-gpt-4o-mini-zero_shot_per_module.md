# Correctness Verification: Mifos (gpt-4o-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Mifos/gpt-4o-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Mifos.md`  
**Total Generated Test Cases:** 191  
**Modules Covered:** 32 Mifos Modules

---

## Error Analysis

### A. Precondition Errors

**Total:** 7

- **TC IDs:** Global Search TC-004 *(Elasticsearch config)*, Share Products TC-005 *(Stock exchange sync)*
- *Reasoning:*
  - Hallucinates enterprise infrastructural requirements (Elasticsearch nodes) and external market synchronizations (Stock Exchange APIs) as prerequisites.

---

### B. Test Steps Errors

**Total:** 5

- **TC IDs:** Center Management TC-003 *(Interactive maps)*, Reports TC-004 *(Custom SQL)*
- *Reasoning:*
  - Instructs the user to "draw a polygon on the map" to define Center boundaries and write "Custom SQL queries" in the reporting UI.

---

### C. Expected Result Errors

**Total:** 6

- **TC IDs:** Accounting Closures TC-004 *(Automated email blasts)*, Provisioning TC-005 *(Automated write-offs)*
- *Reasoning:*
  - Misinterprets accounting closures as triggering automated client email blasts, and assumes provisioning criteria immediately triggers irrevocable write-offs.

---

## Success Rate Calculation

- **Total Generated Test Cases:** 191
- **Total Test Cases with Errors:** 18
- **Total Correct Test Cases:** 173

**Overall Success Rate: 173 / 191 (90.58%)**

---

## Thesis Analysis

The GPT-4o-mini Zero-Shot Per Module approach achieved a **90.58% correctness rate**, generating a meager 191 cases. It succumbed to severe enterprise domain drift, hallucinating Elasticsearch, Stock Exchanges, and custom SQL reporting. Producing only **173 valid tests**, it barely scratches the surface of the 607-case ground truth limit.
