# How an LLM works (next-token prediction)

[← back to topic index](../README.md)

The core loop:

```
input text  →  [LLM predicts next token]  →  append token  →  repeat
```

A **token** is a piece of a word (~3–4 characters). The model generates one token, adds it to the input, and predicts the next, until it decides to stop.

It doesn't produce a whole answer at once. It produces one token, appends it, and re-runs the prediction with the longer input. This is why responses "stream" out piece by piece.
