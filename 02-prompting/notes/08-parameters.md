# Prompting parameters (temperature, top-p, max tokens)

[← back to topic index](../README.md)

Besides the text, most APIs let you tune **how** the model picks tokens. These are the dials worth knowing.

## Temperature

Controls randomness / creativity.

- **Low (0–0.3)** → focused, deterministic, repeatable. Best for facts, code, extraction, classification.
- **High (0.7–1.0+)** → varied, creative, surprising. Best for brainstorming, story writing, marketing copy.

Mechanism: the model produces a probability for every possible next token. Low temperature sharpens the distribution (almost always pick the top token); high temperature flattens it (give less-likely tokens a real chance).

## Top-p (nucleus sampling)

An alternative way to control randomness. Instead of a temperature, you say "only consider the most likely tokens that together add up to p probability."

- `top_p = 1.0` → consider everything.
- `top_p = 0.3` → only the top chunk of most-likely tokens.

Usually you tune **either** temperature **or** top-p, not both.

## Max tokens

A cap on how many tokens the model may **output**. Controls length and cost. Note: if set too low, the answer gets cut off mid-sentence.

## Stop sequences

Strings that tell the model "stop generating when you produce this." Useful for structured output (e.g. stop at `\n\n` or `"###"`).

## Frequency / presence penalties

Nudge the model to repeat itself less (frequency) or introduce new topics (presence). Handy to reduce repetitive text.

## Practical defaults

| Goal | Temperature |
|---|---|
| Code, facts, extraction | 0 – 0.2 |
| Balanced Q&A | 0.3 – 0.7 |
| Creative writing | 0.8 – 1.0 |

## Takeaway

Temperature/top-p control randomness (low = precise, high = creative), max tokens caps output length, stop sequences end generation cleanly. Reach for low temperature when you want reliability.
