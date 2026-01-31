# Cancel My Subscription Assistant

This is a simple conversational assistant to help cancel a gym membership.

It covers conversational design, keyword extraction, relevance classification, and fallback handling based on a [FigJam conversation flow](images/conversation-flow.png).

## How to run
```bash
python3 gym_agent.py
```

When prompted:
```
What would you like help with?
```

Type something like:
* `cancel my membership`
* `end my gym membership`
* `cancel my gym subscription`

The assistant will route your input and respond accordingly.

## Additional project details

This assistant follows a safety-first conversational design approach focused on:
* confirming user intent before collecting personal information
* validating user input before proceeding
* providing clear exit paths
* being transparent that this is a prototype and does not perform real account actions

The goal is to demonstrate trust-critical conversational behavior rather than full backend integration.

### Input validation and exit handling

During the email collection step, the assistant:
* validates the email format using a regular expression
* detects exit commands using whole-word matching (for example: `no`, `cancel`, `stop`, `exit`, `nevermind`) and the explicit phrase "never mind"

This prevents accidental exits when an exit keyword (like "no") appears inside a valid email address such as `noah@example.com`.

### Explicit confirmation checkpoint

Before any cancellation action is simulated, the assistant requires an explicit yes / no confirmation. This creates a clear final confirmation step and prevents premature or accidental cancellation.

### Prototype-safe capability language

The assistant does not claim access to real user accounts or backend systems. When a cancellation is completed in the prototype, the assistant explicitly states that this is where real processing would occur in a production system.

## Conversational QA rubric

This repository includes a conversational QA rubric focused on evaluating trust-critical assistant behavior rather than only technical correctness.

The rubric evaluates:
* intent alignment
* action safety and confirmation
* scope and capability awareness
* recovery and fallback quality
* clarity and language quality
* trust and user confidence

Location: `evaluation/conversational_qa_rubric.md`

## Applied evaluation examples

Annotated test cases demonstrating how the rubric is applied to assistant responses are provided in: `evaluation/test_cases.md`

These examples show how individual assistant messages and short conversational exchanges are evaluated for safety, clarity, and recovery behavior.

## Design notes

While testing, I noticed that simple keyword matching could incorrectly treat parts of an email address (for example, the "no" in noah@example.com) as an exit command.  
To avoid this, exit detection was changed to check whole words and the specific phrase "never mind", instead of matching substrings inside the input.
