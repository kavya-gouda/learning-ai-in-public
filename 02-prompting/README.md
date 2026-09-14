# 02 · Prompting & Context

**Status:** � Learning

How to talk to an LLM so it does what you want. Prompting is the highest-leverage skill in AI engineering — every other topic (agents, RAG, fine-tuning) depends on getting the prompt right.

## Mindmap

```mermaid
flowchart LR
  ROOT([Prompting & Context])

  ROOT --> P1[1 · What a prompt is]
  ROOT --> P2[2 · Message roles]
  ROOT --> P3[3 · Context assembly]
  ROOT --> P4[4 · Zero-shot & few-shot]
  ROOT --> P5[5 · Chain-of-thought]
  ROOT --> P6[6 · Best practices]
  ROOT --> P7[7 · Failure modes]
  ROOT --> P8[8 · Parameters]

  P1 --> P1a[Text fed to the model]
  P1 --> P1b[Steers next-token prediction]

  P2 --> P2a[System / user / assistant]
  P2 --> P2b[Tool results]

  P3 --> P3a[All parts concatenated]
  P3 --> P3b[Order matters]

  P4 --> P4a[Zero-shot = just ask]
  P4 --> P4b[Few-shot = show examples]

  P5 --> P5a[Think step by step]
  P5 --> P5b[Reasoning as tokens]

  P6 --> P6a[Be specific + give format]
  P6 --> P6b[Delimiters + role framing]

  P7 --> P7a[Prompt injection]
  P7 --> P7b[Hallucination + ambiguity]

  P8 --> P8a[Temperature / top-p]
  P8 --> P8b[Max tokens / stop]
```

## Notes

Each point lives in its own file under [`notes/`](./notes).

| # | Point | Status | Note |
|---|-------|--------|------|
| 1 | What a prompt really is | ✅ | [01-what-is-a-prompt.md](./notes/01-what-is-a-prompt.md) |
| 2 | Message roles (system / user / assistant / tool) | ✅ | [02-message-roles.md](./notes/02-message-roles.md) |
| 3 | Context assembly | ✅ | [03-context-assembly.md](./notes/03-context-assembly.md) |
| 4 | Zero-shot & few-shot prompting | ✅ | [04-zero-shot-few-shot.md](./notes/04-zero-shot-few-shot.md) |
| 5 | Chain-of-thought & reasoning | ✅ | [05-chain-of-thought.md](./notes/05-chain-of-thought.md) |
| 6 | Prompt structure & best practices | ✅ | [06-best-practices.md](./notes/06-best-practices.md) |
| 7 | Failure modes (injection, hallucination, ambiguity) | ✅ | [07-failure-modes.md](./notes/07-failure-modes.md) |
| 8 | Prompting parameters (temperature, top-p, max tokens) | ✅ | [08-parameters.md](./notes/08-parameters.md) |

## Projects

_(none yet — a prompt-engineering playground is a good candidate)_
