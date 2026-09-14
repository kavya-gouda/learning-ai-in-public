# Message roles (system / user / assistant / tool)

[← back to topic index](../README.md)

In a real app the prompt isn't one blob of text — it's a list of **messages**, each tagged with a **role**. The model treats each role differently.

## The four roles

| Role | Who writes it | Purpose |
|---|---|---|
| **system** | The app/developer | Top-level instructions: who the model is, rules, tone, available tools. Highest authority. |
| **user** | The end user | The actual request or question. |
| **assistant** | The model | Its previous replies — kept so it remembers the conversation. |
| **tool** | The framework | Results returned from tool calls (topic 01, note 06). |

## What a message list looks like

```json
[
  { "role": "system",    "content": "You are a concise Go tutor. Answer in under 100 words." },
  { "role": "user",      "content": "What is a goroutine?" },
  { "role": "assistant", "content": "A goroutine is a lightweight thread..." },
  { "role": "user",      "content": "How is it different from an OS thread?" }
]
```

The whole list is sent to the model every turn. That's how it "remembers" — there's no hidden memory, the history is literally re-sent each time (ties back to the context window, topic 01 note 05).

## The system prompt is special

- It sits **first** and carries the most weight.
- It defines the persona and the rules the model should follow across the whole conversation.
- The end user usually can't see or change it — it's set by whoever built the app.
- Kiro, ChatGPT, every agent: they all have a big system prompt behind the scenes.

## Takeaway

A prompt is a **list of role-tagged messages**, not a single string. System = rules, user = request, assistant = past replies, tool = tool outputs. All of it is re-sent every turn.
