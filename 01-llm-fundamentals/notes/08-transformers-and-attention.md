# Transformers and attention

[← back to topic index](../README.md)

The architecture that makes LLMs possible. No math needed — the intuition is what matters.

## The core problem

To predict the next token, the model needs to know which earlier words matter. In:

> "The animal didn't cross the street because **it** was too tired,"

what does "it" refer to? A good model must connect "it" back to "animal."

## Attention

**Attention** is the mechanism that does this. For every token, the model computes how much it should "pay attention to" every other token in the context. High attention = strong relevance. This is how it captures relationships between words that are far apart.

## The Transformer

The architecture (from the 2017 paper *"Attention Is All You Need"*) built around stacking many attention layers.

Key properties:
- Processes all tokens **in parallel** (unlike older sequential models) → trains fast on huge data.
- **Self-attention** lets every token look at every other token. This is quadratic, **O(n²)**, which is exactly *why* context windows have limits — double the context, roughly quadruple the compute.
- Stacking many layers builds up from simple patterns (grammar) to abstract ones (reasoning, style).

## Why it ties back to earlier notes

Attention explains two things you already met:
1. *Why* the model is good at understanding relationships between words.
2. *Why* the context window can't be infinite (the O(n²) cost).
