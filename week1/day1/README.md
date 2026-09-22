# Day 1 - Calling an LLM using Groq API

## Overview

Today I learned how to connect a Python application with an LLM using the Groq API. I created a simple Python program that sends a user prompt to the `openai/gpt-oss-120b` model through Groq and extracts the generated response.

## Topics Learned

- Loading environment variables using `python-dotenv`
- Reading API keys securely using `os.getenv()`
- Creating a Groq API client
- Selecting an LLM model
- Understanding chat messages and roles
- Sending a prompt to an LLM
- Receiving and processing the API response
- Extracting the generated text from the response

## Technologies Used

- Python
- Groq API
- Groq Python SDK
- python-dotenv
- OpenAI GPT-OSS 120B

## Implementation

The API key is stored in a `.env` file and loaded using `load_dotenv()`.

The application creates a Groq client and sends a user message to the LLM:

```python
response = client.chat.completions.create(
    model=model,
    messages=messages
)

The generated response is extracted using:

answer = response.choices[0].message.content
Key Learning

I learned the basic flow of an LLM API application:

Python Application
        ↓
    Groq API
        ↓
    LLM Model
        ↓
    Generated Response
        ↓
Extract Response Content


Security Note
The Groq API key is stored in a .env file and is not committed to GitHub.