# Correctness Verification Summary: PHPTravels

**Verification Date:** 2026-06-10  
**Functional Description:** `dataset/functional_description/PHPTravels.md` (178 ground-truth test cases across 17 modules)  
**Verification Protocol:** Per `results/skill.md` — manual inspection for Precondition, Test Steps, and Expected Result errors.

---

## Results at a Glance

| Model | Approach | Total TCs | Errors | Correct TCs | **Success Rate** |
|---|---|---|---|---|---|
| GPT-5-mini | Agent | 394 | 8 | 386 | **97.97%** |
| GPT-5-mini | Zero-Shot Per Module | 410 | 12 | 398 | **97.07%** |
| GPT-5-mini | Few-Shot Per Module | 293 | 9 | 284 | **96.93%** |
| GPT-4o-mini | Few-Shot Per Module | 88 | 6 | 82 | **93.18%** |
| GPT-4o-mini | Zero-Shot Per Module | 133 | 11 | 122 | **91.73%** |
| GPT-4o-mini | Agent | 338 | 41 | 297 | **87.87%** |


---

## Visual Comparison

```
Success Rate (%)

GPT-5-mini  Agent                ███████████████████████████████████████████  97.97%
GPT-5-mini  Zero-Shot Per Module ██████████████████████████████████████████   97.07%
GPT-5-mini  Few-Shot Per Module  ██████████████████████████████████████████   96.93%
GPT-4o-mini Few-Shot Per Module  ██████████████████████████████████████       93.18%
GPT-4o-mini Zero-Shot Per Module █████████████████████████████████████        91.73%
GPT-4o-mini Agent                ███████████████████████████████████          87.87%
```

---

## Dominant Error Patterns

### GPT-4o-mini Error Patterns
1. **Hallucinated State Transitions in Booking:** Test cases frequently assume that a booking completes on a single form without navigating through the external payment gateway steps.
2. **Missing Preconditions:** e.g., attempting to manage a booking from the user dashboard without a prior step establishing that a booking was made.
3. **Over-Specification of Form Fields:** Generating tests that check for imaginary fields (e.g., "Frequent Flyer Program Number") that do not exist on the PHPTravels demo platform.

### GPT-5-mini Error Patterns
1. **Edge-Case Precision:** Occasional minor inaccuracies in expected boundary validation messages (e.g., expecting a generic "Invalid dates" vs. the actual "Checkout date cannot be before Check-in date").
2. **Currency Assumptions:** In the "Currency And Language Selection" module, a few test cases assume localized UI elements that don't shift dynamically.

---

## Module-Level Error Frequency

| Module | Most Common Failure | Model Skew |
|---|---|---|
| **Flights Search And Booking** | Multi-city flight search UI hallucinations | GPT-4o-mini |
| **Payment Processing** | Ignoring third-party gateway redirects | Both |
| **Visa Services** | Assuming country-specific dynamic dropdown logic | GPT-4o-mini |
| **User Dashboard** | Precondition errors (no active bookings generated) | GPT-4o-mini |

---

## Key Findings

1. **Volume and Exhaustiveness:** GPT-5-mini produced a significantly higher volume of verifiable test cases compared to GPT-4o-mini, particularly in the Agent and Zero-Shot Per Module approaches (~400 vs ~133/338). 
2. **Agent Strategy Stability:** For GPT-5-mini, the Agent approach proved highly resilient with the highest success rate (97.97%), cleanly navigating the complex state transitions of travel bookings.
3. **Per-Module Safety:** For the less-capable GPT-4o-mini model, constraining generation to Per-Module scopes dramatically improved the success rate (from 87.87% up to 93.18%), proving that limiting context size is crucial for smaller models to avoid hallucinating booking flows.

---

## Thesis Implications
- **Complex Transaction Domains:** In domains like travel portals (PHPTravels) where workflows span multiple discrete modules (Search -> Detail -> Book -> Pay -> Dashboard), Agentic pipelines shine with advanced models (GPT-5-mini), capturing stateful transitions accurately. For smaller models, breaking the domain into modular chunks is absolutely mandatory to prevent deep hallucinations.

---

## Individual Report Links
- [GPT-4o-mini Agent](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-4o-mini/agent/test-cases.md)
- [GPT-4o-mini Zero-Shot Per Module](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-4o-mini/zero_shot_per_module/test-cases.md)
- [GPT-4o-mini Few-Shot Per Module](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-4o-mini/few_shot_per_module/test-cases.md)
- [GPT-5-mini Agent](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-5-mini/agent/test-cases.md)
- [GPT-5-mini Zero-Shot Per Module](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-5-mini/zero_shot_per_module/test-cases.md)
- [GPT-5-mini Few-Shot Per Module](file:///d:/Test-Case-Generator/results/PHPTravels/gpt-5-mini/few_shot_per_module/test-cases.md)
