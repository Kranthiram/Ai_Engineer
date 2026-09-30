# AI Resume Screening & Job Matching System

An AI-powered resume screening system that extracts job requirements, parses candidate resumes, and calculates a resume-to-job match score using **Groq LLM** and **Pydantic**.

## Technologies Used

* Python
* Groq API
* OpenAI GPT-OSS 120B
* Pydantic
* PyPDF
* python-docx
* python-dotenv
* uv

## Project Flow

### Part 1 — Job Description Analysis

The system sends the job description to the LLM and extracts structured information such as:

* Job role
* Required skills
* Preferred skills
* Minimum experience
* Education requirements
* Responsibilities

Pydantic is used to define and validate the structured output.

### Part 2 — Resume Schema

A structured `Resume` model is created using Pydantic.

It stores candidate information such as:

* Name, email and phone
* Experience
* Skills
* Education
* Projects
* Certifications

### Part 3 — Resume Reading

The system supports both **PDF and DOCX** resumes.

* `PyPDF` → extracts text from PDF files
* `python-docx` → extracts text from DOCX files

### Part 4 — Resume Parsing

The extracted resume text is sent to the LLM.

The LLM converts unstructured resume content into the predefined `Resume` schema and extracts skills, experience, education, projects and certifications.

### Part 5 — Resume Matching

The parsed resume is compared with the structured job description.

The LLM returns:

* Matching skills
* Missing important skills
* Experience requirement status
* Overall match percentage
* Short final verdict

### Part 6 — Candidate Ranking

The system processes all PDF/DOCX resumes inside the `resumes` folder.

Each resume goes through:

**Read Resume → Parse Resume → Compare with Job → Generate Score**

Finally, candidates are sorted based on their score and the **Top 2** and **Lowest 2** candidates are displayed.

## Important Concepts to Revise

* Environment variables and `.env`
* Groq API / LLM API calls
* Prompt engineering
* JSON structured output
* Pydantic `BaseModel`
* Pydantic schema validation
* PDF/DOCX text extraction
* LLM-based information extraction
* Resume-job matching
* Sorting using `key` and `reverse=True`
* File handling using `pathlib`
* Multiple LLM calls in a workflow
* API rate limiting using `time.sleep()`

## LLM Calls

**Call 1:** Job Description → Structured Job Data

**Call 2:** Resume Text → Structured Resume Data

**Call 3:** Job + Resume → Match Score

## Output

The system produces a match percentage for each candidate and identifies the highest and lowest scoring candidates.
