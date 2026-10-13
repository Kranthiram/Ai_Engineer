from fastapi import FastAPI
from pathlib import Path
from pypdf import PdfReader

app=FastAPI()

#pdf exraction
def read_pdf(file_path: Path):
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

@app.get("/")
def home():
    resume_text = read_pdf(Path("Kranthi_Ram_Resume_SeptUpdate.pdf"))
    print(resume_text)
    return {
        "message" : "Resume Parsed!"
    }

