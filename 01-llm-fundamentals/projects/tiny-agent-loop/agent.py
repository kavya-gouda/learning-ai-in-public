"""
Tiny Agent Loop
===============

A minimal, dependency-free demonstration of how an AI agent works:

  1. Tools are defined with a name, description, and parameter schema.
  2. A (mocked) "LLM" looks at the conversation and either:
       - emits a JSON tool call, or
       - emits a final text answer.
  3. The framework runs the requested tool and feeds the result back.
  4. Repeat until the model produces a final answer.

The "LLM" here is faked with simple rules so you can run this with NO
API key and NO dependencies, and focus on the *mechanics* of the loop.
See README.md for how to swap in a real LLM.

Run:  python agent.py
"""

import json
import re


# ---------------------------------------------------------------------------
# 1. TOOLS  --  each has a schema (name + description + parameters) and an impl.
#    In a real agent, the schema is what gets sent to the LLM so it knows what
#    tools exist and how to call them.
# ---------------------------------------------------------------------------

def tool_add(a, b):
    return a + b


def tool_multiply(a, b):
    return a * b


TOOLS = {
    "add": {
        "description": "Add two numbers together.",
        "parameters": {"a": "number", "b": "number"},
        "run": tool_add,
    },
    "multiply": {
        "description": "Multiply two numbers together.",
        "parameters": {"a": "number", "b": "number"},
        "run": tool_multiply,
    },
}


def tool_schemas():
    """The 'menu' of tools handed to the model before it runs."""
    return [
        {"name": name, "description": t["description"], "parameters": t["parameters"]}
        for name, t in TOOLS.items()
    ]


# ---------------------------------------------------------------------------
# 2. THE MOCK "LLM"  --  stands in for a real model's "decide" step.
#    A real LLM would read `messages` (the whole context) and produce text.
#    Here we use simple rules, but the OUTPUT SHAPE is exactly what a real
#    tool-calling model produces: either a tool_call or a final answer.
# ---------------------------------------------------------------------------

def mock_llm(messages):
    """
    Returns either:
      {"tool_call": {"name": ..., "arguments": {...}}}
      {"final": "text answer"}
    """
    last = messages[-1]

    # If the last message is a tool result, turn it into a final answer.
    if last["role"] == "tool":
        return {"final": f"The answer is {last['content']}."}

    # Otherwise it's the user's question. Parse a simple "X op Y" request.
    text = last["content"].lower()

    add_match = re.search(r"(\d+)\s*(?:plus|\+|add)\s*(\d+)", text)
    mul_match = re.search(r"(\d+)\s*(?:times|\*|x|multiply(?:\s+by)?)\s*(\d+)", text)

    if mul_match:
        a, b = int(mul_match.group(1)), int(mul_match.group(2))
        return {"tool_call": {"name": "multiply", "arguments": {"a": a, "b": b}}}
    if add_match:
        a, b = int(add_match.group(1)), int(add_match.group(2))
        return {"tool_call": {"name": "add", "arguments": {"a": a, "b": b}}}

    return {"final": "I can only add or multiply two numbers right now."}


# ---------------------------------------------------------------------------
# 3. THE AGENT LOOP  --  this is the "framework". It never does the thinking;
#    it just runs tools the model asks for and feeds results back.
# ---------------------------------------------------------------------------

def run_agent(user_message, max_steps=5, verbose=True):
    messages = [{"role": "user", "content": user_message}]

    if verbose:
        print(f"\n[tools available] {json.dumps(tool_schemas())}\n")
        print(f"USER: {user_message}")

    for step in range(max_steps):
        decision = mock_llm(messages)

        # Case A: the model wants to use a tool.
        if "tool_call" in decision:
            call = decision["tool_call"]
            name, args = call["name"], call["arguments"]
            if verbose:
                print(f"LLM  -> tool_call: {name}({json.dumps(args)})")

            tool = TOOLS.get(name)
            if tool is None:
                result = f"ERROR: unknown tool '{name}'"
            else:
                result = tool["run"](**args)

            if verbose:
                print(f"FRAMEWORK -> ran {name}, result = {result}")

            # Record the model's request AND the tool result in the context.
            messages.append({"role": "assistant", "content": json.dumps(call)})
            messages.append({"role": "tool", "content": str(result)})
            continue  # loop again so the model can react to the result

        # Case B: the model produced a final answer. Done.
        if verbose:
            print(f"LLM  -> FINAL: {decision['final']}")
        return decision["final"]

    return "Stopped: hit the step limit without a final answer."


# ---------------------------------------------------------------------------
# 4. TRY IT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_agent("What is 6 times 7?")
    run_agent("Can you add 15 plus 27?")
    run_agent("What's the weather today?")
