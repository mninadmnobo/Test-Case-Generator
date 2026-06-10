# Correctness Verification: Mifos (gpt-5-mini — zero_shot_per_module)

**Objective:** Manually verify the logical correctness of generated test cases, checking for hallucinations in preconditions, test steps, and expected results.

**Source File:** `results/Mifos/gpt-5-mini/zero_shot_per_module/test-cases.md`  
**Functional Description:** `dataset/functional_description/Mifos.md`  
**Total Generated Test Cases:** 621  
**Modules Covered:** 32 Mifos Modules

---

## Error Analysis

### A. Precondition Errors

**Total:** 18

- **TC IDs:** Client Management TC-015, TC-016 *(Biometric Scanners)*; Loan Products TC-020, TC-022 *(Blockchain ledgers)*
- *Reasoning:*
  - The zero-shot model suffered from heavy domain drift, assuming standard core banking always includes biometric integrations and distributed ledger (blockchain) preconditions, ignoring the strict Apache Fineract boundaries defined in the document.

---

### B. Test Steps Errors

**Total:** 10

- **TC IDs:** Accounting TC-018 *(AI Anomaly Detection)*; Delinquency Management TC-012 *(Robo-calling)*
- *Reasoning:*
  - Instructs users to "Run AI Anomaly Detection" and "Trigger automated robo-calls to delinquent clients", entirely fabricating AI and VoIP integrations.

---

### C. Expected Result Errors

**Total:** 7

- **TC IDs:** Organization Settings TC-010 *(Real-time Forex)*; Tax Management TC-009 *(Direct IRS filing)*
- *Reasoning:*
  - Asserts that forex rates update in real-time via external APIs and that taxes are filed directly to government agencies via the Mifos interface.

---

## Success Rate Calculation

- **Total Generated Test Cases:** 621
- **Total Test Cases with Errors:** 35
- **Total Correct Test Cases:** 586

**Overall Success Rate: 586 / 621 (94.36%)**

---

## Thesis Analysis

The GPT-5-mini Zero-Shot Per Module approach generated a high volume of cases (621), but the lack of agentic refinement led to significant domain drift, resulting in 35 errors (a **94.36% correctness rate**). It hallucinated biometrics, AI anomalies, and blockchain ledgers. While it yielded 586 valid cases, it falls vastly short of the Agent's 753 valid cases, proving that raw generation in complex domains without iterative grounding creates a massive verification overhead.
