# Zero-shot & few-shot prompting

[← back to topic index](../README.md)

Two of the most useful prompting techniques. "Shot" = an example you show the model.

## Zero-shot: just ask

No examples, just the instruction.

```
Classify the sentiment of this review as positive or negative:
"The battery lasts forever and the screen is gorgeous."
```

Works well when the task is common and the model has seen tons of it during training. Fast and simple — always try this first.

## Few-shot: show examples first

Give 2–5 examples of input → output, then the real input. The model picks up the *pattern* and continues it.

```
Review: "Terrible, broke in a week." → negative
Review: "Absolutely love it, best purchase ever." → positive
Review: "It's okay, nothing special." → neutral
Review: "The battery lasts forever and screen is gorgeous." →
```

The model will output `positive`, matching your format exactly.

## When few-shot wins

- You need a **specific output format** (JSON shape, label set, style).
- The task is **niche or ambiguous** and zero-shot gives inconsistent results.
- You want to **constrain** the answer to certain categories.

## Why it works

Remember: the model predicts the next token by continuing patterns (topic 01). Examples literally set up a pattern in the context, so the most probable continuation is "another item in the same format." You're not teaching it — you're showing it the groove to stay in.

## Trade-offs

- Few-shot uses more tokens (each example costs context budget).
- Too many examples can bias it or waste the window.
- Start zero-shot; add examples only when quality isn't good enough.

## Takeaway

Zero-shot = just ask (try first). Few-shot = show 2–5 examples to lock in format and consistency, at the cost of tokens.
