# Ablation Study Methodology

**Objective:** To systematically evaluate the contribution of each architectural component within the Agentic Pipeline. By stripping away individual modules while holding the underlying LLM constant, we isolate the performance impact of Structural Modeling, Workflow Extraction, and Critic Validation.

This study uses the following four configurations:

### 1. No Structural Model (`agent_no_ast`)
*   **Configuration:** The pipeline explicitly skips generating the UI-AST, feeding an empty structural model (`{}`) into the subsequent agents.
*   **ON:** Workflow Extraction, Critic Validation.
*   **OFF:** Structural Model (UI-AST).
*   **Purpose:** Tests if the Agent framework can successfully extract workflows and generate edge-case tests using *only* the raw Functional Description without any structural scaffolding.

### 2. Structure + Workflows, No Reflection (`agent_no_critic`)
*   **Configuration:** The pipeline generates both the UI-AST and Workflows, but all reflection/validator agents are bypassed.
*   **ON:** Structural Model (UI-AST), Workflow Extraction.
*   **OFF:** Critic Validation (`StructuralModelValidatorAgent`, `WorkflowValidatorAgent`).
*   **Purpose:** Evaluates the necessity of the self-correction loops. It proves whether the initial generative passes are sufficient, or if the "Critic" framework is required to catch missing phantoms and structural hallucinations before test generation.

### 3. Structure + Reflection, No Workflows (`agent_no_workflows`)
*   **Configuration:** The pipeline generates the UI-AST and critiques it, but skips the Workflow Extraction stage. The final test agents only receive the structural model and the raw spec.
*   **ON:** Structural Model (UI-AST), Critic Validation (`StructuralModelValidatorAgent`).
*   **OFF:** Workflow Extraction, Critic Validation (`WorkflowValidatorAgent`).
*   **Purpose:** **Isolates the value of explicitly enumerating execution paths.** If the test suite quality drops without the workflow list, it proves that simply giving an LLM the structural elements (UI-AST) is not enough for it to systematically deduce complex interaction permutations. If quality doesn't drop, it proves the Workflow Extractor is redundant overhead.

### 4. Full Agentic Pipeline (`agent`)
*   **Configuration:** The complete framework is executed.
*   **ON:** Structural Model (UI-AST), Workflow Extraction, Critic Validation.
*   **OFF:** None.
*   **Purpose:** Serves as the upper-bound baseline to measure the degraded configurations against.
