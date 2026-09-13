# Tiny Agent Loop

A minimal, dependency-free agent that demonstrates the full mechanism from the LLM Fundamentals notes: tools with schemas, JSON tool-calling, and the agent loop.

**No API key. No dependencies. Pure Python.**

## Run it

```bash
python agent.py
```

## What you'll see

```
[tools available] [{"name": "add", ...}, {"name": "multiply", ...}]

USER: What is 6 times 7?
LLM  -> tool_call: multiply({"a": 6, "b": 7})
FRAMEWORK -> ran multiply, result = 42
LLM  -> FINAL: The answer is 42.
```

The model never does the multiplication itself. It *asks* for the `multiply` tool by emitting a JSON tool call; the framework runs the real function and feeds `42` back; then the model turns that into a final answer. That round-trip is the entire idea behind agents.

## How it maps to the notes

| Part of the code | Concept | Note |
|---|---|---|
| `TOOLS` + `tool_schemas()` | Tools described by schemas | 06 (tool-calling) |
| `mock_llm()` | The "decide" step — proposes a tool call or a final answer | 04 (why agents) |
| `run_agent()` loop | Framework runs tools, feeds results back, repeats | 04 + 06 |
| `messages` list | The growing context / conversation | 05 (context window) |

## Swapping in a real LLM

The loop structure never changes — only the `mock_llm()` function does. A real version would:

1. Send `messages` **and** `tool_schemas()` to a real model (OpenAI, Anthropic, or a local model).
2. The model returns either a tool call or a text answer (real models have native "tool calling" / "function calling" support that returns this structured shape for you).
3. Return that in the same `{"tool_call": ...}` / `{"final": ...}` shape.

Everything else — running the tool, appending results to `messages`, looping — stays identical. That's the point: the agent loop is simple and universal; the intelligence lives entirely in the model behind the `decide` step.

## Extend it (exercises)

- Add a `subtract` and `divide` tool.
- Add a tool that reads a real file from disk and answer questions about it.
- Add a step counter print so you can see how many round-trips each question takes.
- Replace `mock_llm` with a real API call and compare.
