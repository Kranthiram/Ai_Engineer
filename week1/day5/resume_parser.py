import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Key not found")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"

job_description="""
Job Title: Java Full Stack Developer

Responsibilities
Develop and maintain web applications using Java and Spring Boot.
Design and develop RESTful APIs for communication between frontend and backend.
Build responsive frontend applications using React.js, JavaScript, HTML5 and CSS3.
Work with relational databases such as MySQL/PostgreSQL/Oracle and write SQL queries.
Implement application business logic using Java and Spring Boot.
Work with Spring Data JPA/Hibernate for database persistence.
Implement authentication and authorization using Spring Security/JWT.
Debug and troubleshoot application issues.
Write unit tests and participate in code reviews.
Use Git for source-code management.
Work with developers, testers, product teams and other stakeholders in an Agile/Scrum environment.
Participate in the complete SDLC: requirements → development → testing → deployment → support.

Required Skills
Core Java / Java 8+
OOP concepts
Collections, Exception Handling, Multithreading basics
Spring Framework
Spring Boot
Spring MVC
Spring Data JPA / Hibernate
REST APIs
Spring Security / JWT basics
SQL
MySQL/PostgreSQL
HTML, CSS, JavaScript
React.js or Angular
Git/GitHub
Maven/Gradle
Basic understanding of Microservices

Good to Have
Docker
Jenkins / GitHub Actions
AWS / Azure
Kafka
Redis
JUnit / Mockito
TypeScript
Kubernetes

"""

from pydantic import BaseModel, Field
class JobD(BaseModel):
    role:str
    required_skills:list[str]
    preferred_skills:list[str]
    minimum_experience: float | None
    education_requirements : list[str]
    responsibilities : list[str]

jobd_schema = JobD.model_json_schema()

system_prompt = """
You are an expert HR assistant.
Your job is to analyze job descriptions and extract structured information from them.

return ONLY valid JSON matching this schema

{jobd_schema}

IMPORTANT
Do not return schema itself
Do not return fields like "properties", "title" or "type"
Fill the schema with actual information extracted from the job description.

If minimum experience is not mentioned, return null.
If information for a list is missing, return an empty list.
Do not invent information.
"""

user_prompt = """
Analyze the following job description
{job_description}
"""

message_system = {
    "role":"system",
    "content": system_prompt
}

message_user = {
    "role": "user",
    "content":user_prompt
}

response_format={
    "type" : "json_object"
}

messages = [message_system, message_user]
response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)
answer = response.choices[0].message.content
print(answer)
raw_json = answer

import json
job_data = json.loads(raw_json)
job = JobD(**job_data)

print(job.minimum_experience)
print(job.education_requirements)








