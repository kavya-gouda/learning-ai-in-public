# Tokens and the context window

[← back to topic index](../README.md)

## Tokens: the unit the model actually sees

The model doesn't read words or letters. It reads **tokens** — chunks of text produced by a *tokenizer*.

Rough rule of thumb for English:
- 1 token ≈ **4 characters** ≈ **¾ of a word**
- 100 tokens ≈ **75 words**

How text splits:
- `"cat"` → 1 token
- `"unbelievable"` → often 3 tokens: `un` + `believ` + `able`
- `"ChatGPT"` → `Chat` + `GPT` (2 tokens)
- A space usually attaches to the following word, so `" dog"` is one token
- Numbers and code split oddly; whitespace/indentation each cost tokens

**Why chunks and not whole words?** With a fixed vocabulary of ~50,000–100,000 tokens, the model can build *any* word (even unseen ones) by combining pieces. This is **subword tokenization** — a compromise between one-token-per-letter (too many steps) and one-token-per-word (infinite vocabulary).

Two practical consequences:
1. **Bad at spelling / character-level tasks** (e.g. "count the r's in strawberry") because it sees `straw` + `berry`, not letters.
2. **Cost and speed are measured in tokens**, not words — for both input (what you send) and output (what you get back).

## The context window: the model's working memory

The **context window** is the maximum number of tokens the model can consider at once, input **and** output combined. It's the size of the desk the model works on.

```
┌─────────────── context window (e.g. 128,000 tokens) ───────────────┐
│  system prompt │ conversation history │ your message │ its reply    │
└─────────────────────────────────────────────────────────────────────┘
```

Everything must fit: the system prompt, the whole conversation so far, any files or tool results pulled in, and the response being generated.

Modern models range widely: some 8K tokens, many 128K, a few 1M+. Bigger isn't automatically better, for the two reasons below.

## The two things everyone gets surprised by

1. **No memory outside the window.** The model has zero recollection of anything not currently on the desk. When a conversation gets long and older messages fall off the edge (or get summarized away), that info is gone from the model's view. It's not "forgetting" like a human — it literally cannot see it. This is why an agent keeps feeding relevant context back in.
2. **"Lost in the middle."** Even within the window, models pay most attention to the **beginning** and **end**, and can gloss over content buried in the middle. *Where* you put important info matters, not just whether it fits.

## Why this matters for agents

Every time a tool runs and returns a result, that result gets stuffed into the context window and fed back to the model. Read ten files, run five commands, and you can fill the desk. That's why real agents:
- **Summarize/compact** old context to make room
- **Retrieve only relevant chunks** instead of dumping everything (this is what RAG is for)
- **Manage context carefully** so important stuff stays visible

The context window is the physical constraint that motivates half the techniques you'll learn later (RAG, memory systems, prompt engineering).

## The mental model

| Concept | What it is | Why you care |
|---|---|---|
| Token | Subword chunk the model reads/writes | Cost, speed, spelling quirks |
| Tokenizer | Splits text into tokens | Explains weird splits |
| Context window | Max tokens in at once (in + out) | The model's working memory limit |
| Lost in the middle | Attention favors start/end | Placement of key info matters |
