# Why an LLM enables "agents"

[← back to topic index](../README.md)

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

## The mental model

| Concept | Role | Analogy |
|---|---|---|
| LLM | Predicts text, makes decisions | The brain |
| Prompt / context | What the brain currently "sees" | Short-term memory / desk |
| Tools | Actions it can trigger | Hands |
| Agent loop | Ties it together, acts repeatedly | Nervous system |

## Things to internalize early

- **It predicts, it doesn't "know."** Facts are high-probability guesses from training. This is why it can be confidently wrong (*hallucination*). Agents fix this by checking real sources with tools.
- **Context is everything.** The model only sees what's in its current context window. No memory beyond that unless the agent feeds it back.
- **Same brain, different behavior.** The same LLM can be a coding agent, a support bot, or a researcher purely based on instructions and available tools.
