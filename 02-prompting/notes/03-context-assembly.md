# Context assembly

[← back to topic index](../README.md)

"Prompting" in a real app is really **context assembly** — gathering the right pieces and arranging them into the message list before the model runs.

## What gets assembled

A single request to the model might be built from:

1. **System prompt** — rules, persona, tool descriptions.
2. **Retrieved knowledge** — relevant documents pulled in (this is what RAG does, topic 04).
3. **Conversation history** — previous user + assistant messages.
4. **Tool results** — outputs from earlier tool calls.
5. **The current user message** — the actual new request.

All of it is concatenated (in order) into the context window and sent to the model.

```
┌──────────────── context window ────────────────┐
│ system │ retrieved docs │ history │ user message │
└─────────────────────────────────────────────────┘
```

## Two things that matter a lot

**1. Order / placement.** Models attend most to the **start** and **end** of the context ("lost in the middle", topic 01 note 05). So put critical instructions in the system prompt (start) and the actual task near the end (last user message). Don't bury key info in the middle.

**2. Budget.** Everything competes for the same token limit. Long history + big retrieved docs + a huge system prompt can crowd out room for the answer. This is why agents **summarize old history** and **retrieve only relevant chunks** instead of everything.

## Why this is the heart of AI engineering

Most of the work in building a good AI app is **deciding what goes into the context and in what order** — not the model itself. Get the assembly right and a mediocre model shines; get it wrong and the best model flounders.

## Takeaway

Context assembly = choosing and ordering the pieces (system, docs, history, tools, user msg) that fit in the window. Placement and token budget are the two levers.
