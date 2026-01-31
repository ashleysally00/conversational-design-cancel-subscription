# Applied evaluation examples

This file demonstrates how I apply the conversational QA rubric to responses from the Cancel My Subscription assistant.

---

## Test case 1 — User requests cancellation

**User:**  
"I want to cancel my membership."

**Assistant response:**  
"Okay — I can help you cancel your gym membership. Do you want step-by-step instructions?"

**Evaluation:**

- **Intent alignment**  
  Meets. The assistant correctly identifies cancellation intent.

- **Action safety and confirmation**  
  Meets. The assistant does not imply that the cancellation has already occurred.

- **Clarity and language quality**  
  Meets. The question is clear and straightforward.

- **Trust and user confidence**  
  Meets. The response avoids over-claiming system capabilities.

**Overall assessment:**  
The response correctly identifies intent, avoids premature action, and asks for confirmation before proceeding. This is appropriate behavior for a cancellation assistant.

---

## Test case 2 — Fallback handling

**User:**  
"I need help with something."

**Assistant response:**  
"I can help cancel a gym membership. What would you like to do?"

**Evaluation:**

- **Intent alignment**  
  Meets. The assistant correctly recognizes that the user's intent is unclear and avoids making an assumption.

- **Recovery and fallback quality**  
  Meets. The assistant states what it can help with and prompts the user to clarify their request.

- **Scope and capability awareness**  
  Meets. The assistant accurately represents its limited scope.

- **Clarity and language quality**  
  Meets. The response is short, clear, and provides an actionable next step.

**Overall assessment:**  
The fallback appropriately handles ambiguous input by stating system capabilities and inviting the user to clarify their need.
