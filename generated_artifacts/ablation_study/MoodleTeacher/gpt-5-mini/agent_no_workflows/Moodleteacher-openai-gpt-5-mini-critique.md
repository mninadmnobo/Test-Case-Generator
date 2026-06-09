# Semantic Critique — Moodleteacher

Generated: 2026-06-09T12:00:58.342628Z

## Login

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Dashboard

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Dashboard — Edit Mode

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## My Courses

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive controls, course link navigation, and per-card actions; only minor inferred properties are present.

**Missing:** none

**Phantoms (hallucinations):**

- Controls_Bar.type (form was not specified in description)
- Courses_Grid.min (min: 0 is an inferred constraint not stated in description)

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements: navigation tab bar, collapse-all link, collapsible sections with chevron and section name, and clickable activity/resource names.

**Missing:** none

**Phantoms:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements from the description; only two minor inferred 'required' flags were added which are non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- components.Sections.item_fields.Section_Inline_Rename.required (was not specified in description)
- components.Sections.item_fields.Activities_Table.row_actions[0].fields.New_Name.required (was not specified in description)

---

## Assignment Creation

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Course Settings

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Participants Management

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Assignment — Teacher View

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Assignment Submissions

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Gradebook — Grader Report

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Profile

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures all interactive elements and behaviors from the description; only a minor specificity (the Description field should be marked as a rich-text editor) is not encoded.

**Missing:**

- components.Edit_Profile_Form.sections[0].fields.Description (should be type: rich_text_editor)

**Phantoms:** none

---

## Logout

> **Error:** litellm.RateLimitError: RateLimitError: OpenAIException - You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. LiteLLM Retried: 2 times
