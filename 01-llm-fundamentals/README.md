# 01 · LLM Fundamentals

**Status:** 🚧 Learning

Understanding the "brain" behind AI agents: what a Large Language Model is, how it works, and why it enables agents.

## Checklist

- [x] What an LLM is (the one-sentence version)
- [x] How an LLM works (next-token prediction)
- [x] How it's trained (pre-training, fine-tuning, RLHF)
- [x] Why an LLM enables "agents"
- [ ] Tokens and the context window
- [ ] How tool-calling actually works (JSON under the hood)
- [ ] Prompting and system prompts
- [ ] Transformers and attention (architecture deep dive)
- [ ] Build a tiny agent loop myself

---

## Notes

### The one-sentence version

An **LLM (Large Language Model)** is the "brain" inside an AI agent. It's a giant statistical model trained on huge amounts of text that, given some input text, predicts the most likely next chunk of text. Everything an agent "thinks" or "decides" runs through that prediction engine.

### What an LLM actually is

Think of it as sophisticated autocomplete:

- **Language Model** = a program that assigns probabilities to sequences of words. Given "The sky is ___", it knows "blue" beats "spaghetti."
- **Large** = billions of internal parameters (tunable numbers), trained on a large slice of the internet, books, and code.

The core loop:

```
input text  →  [LLM predicts next token]  →  append token  →  repeat
```

A **token** is a piece of a word (~3–4 characters). The model generates one token, adds it to the input, and predicts the next, until it decides to stop.

### How it got smart: the training story

1. **Pre-training** — reads massive text, plays fill-in-the-blank billions of times. Learns grammar, facts, reasoning, code. The text itself is the answer key (no manual labeling).
2. **Fine-tuning / instruction tuning** — trained on "request → good response" examples so it learns to *follow instructions* instead of just continuing text.
3. **RLHF (Reinforcement Learning from Human Feedback)** — humans rank responses, model is nudged toward preferred ones. Makes it feel helpful and safe.

### Why it enables "agents"

Key insight: **an LLM by itself only produces text.** It can't browse, run code, or edit files. So how does an agent act?

The text the LLM produces can be a **structured request to use a tool**. The surrounding program (the agent framework) runs this loop:

```
1. User asks something
2. LLM reads the request + a list of available tools
3. LLM outputs: "I want to call tool X with these arguments"
4. The agent framework actually runs tool X (reads a file, runs a command)
5. The result is fed back to the LLM as new input
6. LLM decides: call another tool, or answer the user
7. Repeat until done
```

So the **LLM is the decision-maker (brain)** and the **agent is the LLM plus a body** (tools, memory, and a loop). Remove the LLM → empty shell. Remove the tools → just a smart chatbot.

### The mental model

| Concept | Role | Analogy |
|---|---|---|
| LLM | Predicts text, makes decisions | The brain |
| Prompt / context | What the brain currently "sees" | Short-term memory / desk |
| Tools | Actions it can trigger | Hands |
| Agent loop | Ties it together, acts repeatedly | Nervous system |

### Things to internalize early

- **It predicts, it doesn't "know."** Facts are high-probability guesses from training. This is why it can be confidently wrong (*hallucination*). Agents fix this by checking real sources with tools.
- **Context is everything.** The model only sees what's in its current context window. No memory beyond that unless the agent feeds it back.
- **Same brain, different behavior.** The same LLM can be a coding agent, a support bot, or a researcher purely based on instructions and available tools.

## Projects

_(none yet — a tiny agent loop is planned)_
