# Build a tiny agent loop

[← back to topic index](../README.md)

The payoff: a minimal, runnable agent that ties together everything — an LLM (mocked), tools with schemas, the JSON tool-calling handshake, and the loop.

**Project code:** [`../projects/tiny-agent-loop/`](../projects/tiny-agent-loop/)

## What it demonstrates

- **Tools with schemas** — each tool has a name, description, and parameters (point 6).
- **The agent loop** — the "LLM" is asked, proposes a tool call, the framework runs it, feeds the result back, and loops until it produces a final answer (point 4).
- **JSON tool-calling** — the mock model emits a structured tool request; the framework parses and executes it (point 6).
- **Context as a growing message list** — every step appends to the conversation, just like a real context window (point 5).

## Why the "LLM" is mocked

The mock model follows simple rules instead of calling a paid API, so you can run it with **zero dependencies and no API key** and focus on the *mechanics* of the loop. The project README explains exactly how to swap in a real LLM (OpenAI/Anthropic/local) — the loop structure stays identical; only the "decide" step changes.

## How to run

```bash
cd projects/tiny-agent-loop
python agent.py
```

See the [project README](../projects/tiny-agent-loop/README.md) for a full walkthrough of the output.
