from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict
import re

app = FastAPI(
    title="AI Resume Analyzer & Job Matcher",
    version="1.0.0",
    description="Explainable resume-to-job matching API."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SKILLS = [
    "python","java","c++","javascript","typescript","sql","mysql","postgresql",
    "mongodb","pandas","numpy","scikit-learn","tensorflow","pytorch",
    "fastapi","flask","django","react","node.js","html","css","git","github",
    "docker","kubernetes","aws","azure","gcp","power bi","tableau",
    "excel","spark","hadoop","airflow","rest api","machine learning",
    "deep learning","nlp","data analysis","data visualization","statistics",
    "linux","bash"
]

INTERVIEW_TEMPLATES = {
    "python": "Explain how you have used Python for a real project. What data structures did you choose and why?",
    "sql": "Write a SQL query to find the top 5 customers by total revenue and explain your approach.",
    "pandas": "How would you use Pandas to clean missing values and remove duplicate records?",
    "machine learning": "Describe an end-to-end machine-learning workflow, including validation and model evaluation.",
    "fastapi": "How would you design a FastAPI endpoint for a production application?",
    "react": "Explain how state and component communication work in React.",
    "docker": "What problem does Docker solve and how would you containerize an API?",
    "aws": "Which AWS services would you choose to deploy a Python API and why?",
    "power bi": "How would you design a Power BI dashboard for an e-commerce business?",
    "git": "Describe a Git workflow you would use when working with a team."
}

class AnalyzeRequest(BaseModel):
    resume_text: str = Field(min_length=20)
    job_description: str = Field(min_length=20)

def normalize(text: str) -> str:
    text = text.lower().replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text)

def extract_skills(text: str) -> List[str]:
    t = normalize(text)
    found = []
    for skill in SKILLS:
        # Preserve +, # and dots in terms like C++ and C#
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, t):
            found.append(skill)
    return sorted(found)

def extract_sections(text: str) -> Dict[str, str]:
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    section_names = ["education", "experience", "projects", "skills", "certifications"]
    result = {}
    current = None
    buckets = {s: [] for s in section_names}

    for line in lines:
        clean = re.sub(r"[:#\-]+$", "", line.lower()).strip()
        if clean in section_names:
            current = clean
            continue
        if current:
            buckets[current].append(line)

    for s, items in buckets.items():
        result[s] = "\n".join(items[:20])
    return result

def generate_questions(skills: List[str]) -> List[str]:
    questions = []
    for skill in skills:
        if skill in INTERVIEW_TEMPLATES:
            questions.append(INTERVIEW_TEMPLATES[skill])
    if len(questions) < 5:
        questions.append("Walk me through the most challenging project on your resume.")
        questions.append("How did you measure the success of your project?")
    return questions[:8]

@app.get("/health")
def health():
    return {"status": "healthy", "service": "resume-analyzer"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    resume_skills = extract_skills(request.resume_text)
    job_skills = extract_skills(request.job_description)

    matched = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))

    score = round((len(matched) / len(set(job_skills))) * 100, 1) if job_skills else 0.0

    return {
        "match_percentage": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "resume_skills": resume_skills,
        "job_required_skills": job_skills,
        "resume_sections": extract_sections(request.resume_text),
        "interview_questions": generate_questions(matched)
    }
