# Day 2 - System Messages, User Messages and Temperature

## Overview

Today I learned how to control the behavior of an LLM using system and user messages. I created a simple food application naming example where the LLM acts as a brand manager and suggests a suitable one-word name.

## Topics Learned

- System messages
- User messages
- Message roles
- Prompt structure
- Passing multiple messages to an LLM
- Temperature parameter
- Controlling LLM behavior using instructions
- Extracting the generated response

## Technologies Used

- Python
- Groq API
- Groq Python SDK
- python-dotenv
- OpenAI GPT-OSS 120B

## System Message

A system message provides instructions that define how the model should behave.

Example:

```python
message_system = {
    "role": "system",
    "content": "you are my brand manager suggests a good one word name"
}

Here, the model is instructed to behave like a brand manager.

User Message

The user message contains the actual request given to the model.

message = {
    "role": "user",
    "content": "i want a name for my food application strictly only one name please"
}
Combining Messages

Both system and user messages are passed to the model as a list:

messages = [message_system, message]

This allows the model to understand both its role and the user's request.

Temperature

I also learned about the temperature parameter.

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)

Temperature influences the randomness and variation of the model's responses. Higher values generally allow more variation, while lower values make responses more consistent and focused.

Key Learning

The basic message structure learned today is:

System Message
      ↓
Defines model behavior
      ↓
User Message
      ↓
Provides the actual request
      ↓
LLM
      ↓
Generated Response
Example

The application asks the LLM to act as a brand manager and generate a one-word name for a food application.

Security Note
The Groq API key is stored in a .env file and is not committed to GitHub.