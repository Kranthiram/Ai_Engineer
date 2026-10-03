# Day 8 - Reasoning + Acting Agent

## Overview

Today I learned how to build a simple reasoning and acting agent using an LLM and Python tools.

The agent can decide which tool to use, execute the tool, receive the result as an observation, and then continue reasoning until it produces a final answer.

## Topics Learned

- Reasoning + Acting (ReAct) concept
- Tool calling
- Python functions as tools
- Regular expressions using `re`
- Extracting tool name and arguments
- Tool execution using a dictionary
- Observations
- Maintaining conversation history
- Agent loop

## Tools Used

The agent has two tools:

- `get_product_price()` - Returns the price of a product.
- `calculator()` - Performs calculations.

## How the Agent Works

The agent follows this basic flow:

```text
User Question
      ↓
     LLM
      ↓
 Decide which tool to use
      ↓
  Action generated
      ↓
 Regex extracts tool name and argument
      ↓
 Python executes the tool
      ↓
   Observation
      ↓
     LLM
      ↓
 Another Action or Final Answer