# How it got smart: the training story

[← back to topic index](../README.md)

1. **Pre-training** — reads massive text, plays fill-in-the-blank billions of times. Learns grammar, facts, reasoning, code. The text itself is the answer key (no manual labeling).
2. **Fine-tuning / instruction tuning** — trained on "request → good response" examples so it learns to *follow instructions* instead of just continuing text.
3. **RLHF (Reinforcement Learning from Human Feedback)** — humans rank responses, model is nudged toward preferred ones. Makes it feel helpful and safe.
