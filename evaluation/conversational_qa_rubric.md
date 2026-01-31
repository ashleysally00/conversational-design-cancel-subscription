# Conversational QA rubric for a task-oriented cancellation assistant

This rubric evaluates assistant responses in a task-oriented conversational assistant designed to help users cancel a gym membership. It focuses on response quality, intent handling, and trust-critical behavior rather than model performance or UI.

---

## 1. Intent alignment

**Question:**  
Does the response correctly reflect what the user is trying to do?

**Meets:**
* The assistant correctly identifies cancellation-related intent
* No unrelated actions are introduced

**Does not meet:**
* The assistant assumes an action the user did not request
* The assistant ignores or misinterprets the user's goal

---

## 2. Action safety and confirmation

**Question:**  
Does the assistant avoid implying or performing irreversible actions without explicit user confirmation?

**Meets:**
* The assistant confirms intent before proceeding
* The assistant avoids implying that cancellation has already occurred

**Does not meet:**
* The assistant states or implies the membership is canceled without confirmation

---

## 3. Scope and capability awareness

**Question:**  
Does the assistant accurately represent what it can and cannot do?

**Meets:**
* The assistant clearly states system limitations when needed
* The assistant does not claim access to user accounts or backend systems

**Does not meet:**
* The assistant claims it completed or verified real-world actions

---

## 4. Recovery and fallback quality

**Question:**  
When the request cannot be handled directly, does the assistant recover appropriately?

**Meets:**
* The assistant provides a helpful fallback or redirection
* The assistant explains why the request cannot be completed

**Does not meet:**
* The assistant responds with a generic apology without guidance

---

## 5. Clarity and language quality

**Question:**  
Is the response easy to understand and actionable?

**Meets:**
* Instructions are clear and concise
* No unnecessary technical language

**Does not meet:**
* The response is vague or overly verbose

---

## 6. Trust and user confidence

**Question:**  
Does the response avoid over-confidence and misleading language?

**Meets:**
* The assistant avoids definitive statements about real-world changes
* The assistant uses appropriate uncertainty language when needed

**Does not meet:**
* The assistant uses authoritative language for actions it cannot perform

---

## How I use this rubric

I apply this rubric to individual assistant messages and short conversational exchanges to identify failure patterns, decide which issues should be fixed first, and inform prompt and response-design changes.

**Common failure patterns I look for include:**
* premature confirmation of cancellation
* over-claiming system capabilities
* missing clarification before action
* fallback responses that do not move the user forward

---

## Why this rubric

I designed this rubric for trust-critical, task-oriented assistants where incorrect assumptions, premature confirmations, or misleading capability claims can directly harm user confidence.

Unlike open-ended chat systems, cancellation and account-related assistants must:

- avoid implying real-world actions were completed  
- confirm intent before proceeding  
- clearly communicate system boundaries  
- provide recovery paths when requests cannot be fulfilled  

These criteria reflect common conversational failure patterns in task-oriented AI assistants and are applied here to a cancellation use case.

