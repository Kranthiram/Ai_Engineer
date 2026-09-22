import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

role="user"
prompt="i want a name for my food application strictly only one name please"

message_system={
    "role":"system",
    "content":"you are my brand manager suggests a good one word name"
}

message={
    "role" : role,
    "content" : prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model,messages=messages, temperature=2)
#print(response)

print("######################################################")
answer=response.choices[0].message.content
print(answer)
