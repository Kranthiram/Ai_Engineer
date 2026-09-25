import os
from groq import Groq
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api key not found")
client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    phone:int
    issue:str

schema = Ticket.model_json_schema()

text = "Hi my name is kranthiram , i bought an iphone but it is not working, my email address is akr@gmail.com, my phone number is 645143649, i live in infinity vision"
role = "user"
prompt = f"""
    this is customer ticket, Extract personal information from this text. 
    {text}
"""

system_prompt = f"""
    please Extract personal details by strictly following this schema and give me a json output.
    {schema}
"""

message_system={
    "role":"system",
    "content":system_prompt
}

response_format={
    "type" : "json_object"
}

message = {
    "role":role,
    "content":prompt
}
messages = [message_system, message]

response = client.chat.completions.create(model = model, messages=messages, response_format = response_format)
answer = response.choices[0].message.content
print(answer)

# how to read json
import json
# raw_json = answer
data_file = json.loads(answer)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.phone)
print(ticket.issue)