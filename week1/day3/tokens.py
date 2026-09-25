import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key :
    raise ValueError("Api key not found")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

role = "user"
prompt1 = "Hi!"
prompt2 = "explain time travel in 30 words"
prompt3 = "write essay on india in 1000 words"

prompts = [prompt1,prompt2,prompt3]

for prompt in prompts :
    message={
        "role": role,
        "content":prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model,messages=messages, max_tokens=500)
    usage = response.usage
    print(f"Prompt:{prompt}--> your tokens : {usage.prompt_tokens} completion tokens : {usage.completion_tokens} total tokens  : {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
    
