# Prompt structure & best practices

[← back to topic index](../README.md)

Practical rules that reliably improve results. Think of these as the "clean code" of prompting.

## 1. Be specific about the task

Vague in → vague out.

- ❌ "Write about dogs."
- ✅ "Write a 3-sentence friendly intro about golden retrievers for a pet-adoption website."

## 2. State the output format explicitly

Tell it exactly what shape you want.

- "Answer in a bullet list."
- "Return valid JSON with keys `title` and `summary`."
- "Reply in at most 50 words."

## 3. Use delimiters to separate instructions from data

Wrap the content the model should act on so it can't confuse it with your instructions.

```
Summarize the text between the triple quotes.
"""
{user text here}
"""
```

This also reduces prompt-injection risk (note 07).

## 4. Give the model a role

"You are an expert Python code reviewer." Role framing nudges tone, depth, and vocabulary.

## 5. Break big tasks into steps

Either tell it the steps, or ask it to plan first, then execute. Easier for the model and easier for you to check.

## 6. Show, don't just tell

If format matters, add a few-shot example (note 04). One good example often beats three sentences of explanation.

## 7. Tell it what to do, not just what not to do

- ❌ "Don't be verbose."
- ✅ "Answer in one short paragraph."

## 8. Iterate

Prompting is empirical. Try, look at the output, adjust one thing, try again. Keep a copy of prompts that work well.

## Quick template

```
[Role]      You are a ...
[Task]      Your job is to ...
[Context]   Here is the relevant info: """ ... """
[Format]    Respond as ...
[Examples]  (optional few-shot)
```

## Takeaway

Be specific, state the format, delimit your data, give a role, and iterate. Good prompting is mostly clarity, not tricks.
