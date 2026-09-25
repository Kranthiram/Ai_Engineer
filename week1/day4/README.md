# Day 4 - Structured LLM Output

## Topics Learned

- Pydantic `BaseModel`
- JSON Schema
- Structured JSON output
- `json.loads()`
- Dictionary unpacking using `**`

## Key Concepts

- Pydantic `BaseModel` defines and validates the expected data structure.
- `model_json_schema()` generates a JSON schema from the Pydantic model.
- `response_format` requests JSON output from the LLM.
- `json.loads()` converts a JSON string into a Python dictionary.
- `Ticket(**data_file)` converts the dictionary into a validated Pydantic object.

## Flow

LLM → JSON → Python Dictionary → Pydantic Object

## Key Learning

I learned how to extract structured information from an LLM response and validate it using Pydantic.