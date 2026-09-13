# How tool-calling actually works (JSON under the hood)

[← back to topic index](../README.md)

## The problem it solves

The LLM only outputs text. If it asked for a tool in plain English ("please read config.json"), the framework would have to guess and parse fuzzy language — too unreliable. Solution: the model is trained to output a **structured, machine-readable request (JSON)** when it wants to act.

## The four-step handshake

Three parties: **you**, the **agent framework** (the program), and the **LLM**.

### Step 1 — The framework tells the LLM what tools exist

Before the LLM runs, the framework sends a list of tools, each described by a schema:

```json
{
  "name": "read_file",
  "description": "Read the contents of a file from disk",
  "parameters": {
    "type": "object",
    "properties": {
      "path": { "type": "string", "description": "Path to the file" }
    },
    "required": ["path"]
  }
}
```

This schema is the model's "instruction manual." The `description` fields matter a lot — the model chooses which tool and how to fill arguments based mostly on these words. Vague descriptions → wrong choices.

### Step 2 — The LLM decides and emits a tool call

Instead of prose, the model outputs a structured request:

```json
{
  "tool_call": {
    "name": "read_file",
    "arguments": { "path": "config.json" }
  }
}
```

Key insight: **the model is not running the tool.** It's just producing text that happens to be valid JSON matching the schema. Still plain next-token prediction — but fine-tuned to produce clean JSON in these moments.

### Step 3 — The framework executes and returns the result

The framework parses the JSON, runs the real function, and feeds the output back:

```json
{
  "tool_result": {
    "name": "read_file",
    "content": "{ \"port\": 8080, \"debug\": true }"
  }
}
```

This result now lives in the context window (it costs tokens).

### Step 4 — The LLM continues

With the result in context, the model either asks for another tool (loop back to step 2) or writes a normal prose answer. Repeats until done.

## A concrete walkthrough

Ask: *"What port does my config use?"*

```
You:        "What port does my config use?"
LLM:        → tool_call: read_file(path="config.json")
Framework:  → runs it, returns: { "port": 8080, "debug": true }
LLM:        → reads result → "Your config uses port 8080."
```

Two round-trips to the model, one real function call in the middle. The model never touched the disk — it only produced text. The framework did the work.

## Things worth burning in

- **The model proposes, the framework disposes.** The LLM only *requests* a tool; a separate program decides whether to run it. This is where permission prompts and safety checks live.
- **Descriptions are the API.** The model picks tools based on names and descriptions — writing good ones is a real skill (prompt engineering for tools).
- **Structured output is the whole trick.** Tool-calling is just the model reliably producing schema-valid JSON. Newer models are specifically tuned for this, which is why it works well now.
- **Results cost context.** Every tool result is stuffed back into the window. Big results (dumping a huge file) eat your token budget fast.

## Mental model

| Party | Role |
|---|---|
| Framework (before) | Hands the LLM a menu of tools (schemas) |
| LLM | Picks a tool, emits JSON with arguments |
| Framework (after) | Runs the real tool, returns the result |
| LLM | Reads result, loops or answers |
