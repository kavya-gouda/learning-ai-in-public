# Chain-of-thought & reasoning

[← back to topic index](../README.md)

## The idea

Ask the model to **show its reasoning step by step** before giving the final answer. The magic phrase: *"Let's think step by step."*

Compare:

**Without (often wrong on multi-step problems):**
```
Q: A shop had 23 apples, sold 8, then got 12 more. How many now?
A: 27
```

**With chain-of-thought:**
```
Q: A shop had 23 apples, sold 8, then got 12 more. How many now?
A: Let's think step by step.
   Start: 23. Sold 8 → 23 - 8 = 15. Got 12 more → 15 + 12 = 27.
   Final answer: 27.
```

## Why it actually works

This connects straight to next-token prediction (topic 01). The model generates one token at a time, and each token it writes becomes part of the context for the next one. By writing out the intermediate steps, it **gives itself more useful context to condition on** before committing to the final number. It literally "reasons on paper."

Skipping the steps forces it to jump to an answer token with less to go on — more error-prone on anything multi-step.

## When to use it

- Math and logic problems.
- Multi-step decisions or planning.
- Anywhere the answer depends on a chain of sub-conclusions.

## Modern note: "reasoning models"

Newer models (the "reasoning" or "thinking" variants) do chain-of-thought **automatically and internally** before answering. You often don't need to prompt for it — but understanding the mechanism explains *why* those models are better at hard problems: they're spending tokens on reasoning first.

## Trade-offs

- Uses more output tokens (slower, costs more).
- Overkill for simple lookups or one-step tasks.

## Takeaway

Chain-of-thought = "think step by step." Writing intermediate steps as tokens gives the model better context for the final answer. Great for reasoning, wasteful for trivial tasks.
