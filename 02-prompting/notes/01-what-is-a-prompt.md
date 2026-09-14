# What a prompt really is

[← back to topic index](../README.md)

## The plain definition

A **prompt** is simply the text you feed the model. That's it. There's no magic layer — the model reads your text and predicts what comes next (next-token prediction, from topic 01).

## Why prompting works at all

Because the model was trained on a huge amount of text, it has absorbed patterns like:
- "Question: ... Answer: ..." → so asking a question nudges it toward answering.
- "Translate to French: ..." → so it learned that this phrasing means translate.
- Examples followed by a new case → so it continues the pattern.

**Prompting is steering the prediction.** You're not programming the model with rules; you're setting up a context where the most likely next tokens happen to be the answer you want.

## The key mental shift

Think of the model as an extremely well-read improv partner. It will "yes, and..." whatever you give it, continuing in the style and direction you set. So:
- Vague prompt → vague, generic continuation.
- Specific prompt with clear intent, format, and examples → focused, useful continuation.

You are not commanding a computer. You are **shaping the most probable output** by controlling what the model sees.

## One-line takeaway

A prompt is the text that sets up the model's prediction; good prompting = making your desired answer the most likely continuation.
