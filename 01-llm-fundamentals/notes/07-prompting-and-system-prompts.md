# Prompting and system prompts

[← back to topic index](../README.md)

A **prompt** is just the text you feed the model. In a real agent it isn't one blob — it's assembled from layered parts, each with a role.

## The layers of a prompt

- **System prompt** — top-level instructions defining *who the model is* and *the rules it follows*. Set by the app, not the end user. Holds the agent's personality, constraints, and tool descriptions. Sits at the very start of the context and shapes everything after.
- **User prompt** — what you actually type.
- **Assistant messages** — the model's prior replies (kept so it remembers the conversation).
- **Tool results** — outputs fed back in from the tool-calling loop.

All of these are concatenated into the context window in order. So "prompting" at the agent level is really **context assembly**.

## Prompting techniques

- **Zero-shot** — just ask ("Translate this to French"). Works when the task is common.
- **Few-shot** — show 2–3 examples of input→output before the real one. Big improvement in consistency for formatting or niche tasks.
- **Chain-of-thought** — ask it to "think step by step." Reasoning tasks improve because the model generates intermediate steps as tokens before the answer. (It predicts token by token, so writing the steps helps it reach a better final token.)
- **Role / instruction framing** — "You are an expert Go reviewer." Nudges style and depth.

## Powerful but fragile

System prompts steer the whole session, but they:
- Compete for context space (tokens).
- Can be overridden by cleverly crafted user input (**prompt injection**).

This is why external/tool content should be treated as untrusted data, not as instructions to obey.
