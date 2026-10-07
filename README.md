<<<<<<< HEAD

=======
# AI Resume Analyzer & Job Match System

A portfolio-ready AI/NLP application that analyzes a candidate resume against a job description.

## What it does

- Accepts a resume in TXT format and can be extended to PDF/DOCX extraction.
- Extracts common technical skills using a curated skill dictionary.
- Calculates a transparent skill-match percentage.
- Identifies matched and missing skills.
- Extracts basic resume sections such as education, experience and projects.
- Generates interview questions based on detected skills.
- Provides an API using FastAPI.
- Includes a simple browser frontend.
- Includes automated tests.

## Architecture

```text
Resume / Job Description
          |
          v
     FastAPI Backend
          |
   +------+------+
   |             |
Skill Parser   Section Parser
   |             |
   +------+------+
          |
    Match Engine
          |
   +------+------+
   |             |
Match %       Missing Skills
          |
    Interview Q&A
          |
      Frontend
```

## Tech Stack

- Python
- FastAPI
- Pydantic
- NLP-style text processing
- HTML/CSS/JavaScript
- Pytest

## Run Locally

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

uvicorn backend.main:app --reload
```

Open:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

### POST `/analyze`

Request:

```json
{
  "resume_text": "Python SQL Pandas FastAPI...",
  "job_description": "Looking for Python, SQL, Pandas and AWS..."
}
```

Response includes:

- match percentage
- matched skills
- missing skills
- detected resume skills
- job-required skills
- resume sections
- interview questions

### GET `/health`

Returns application status.

## Example

Resume skills:

```text
Python, SQL, Pandas, FastAPI, Git
```

Job requirements:

```text
Python, SQL, Pandas, AWS, Docker
```

The system identifies:

- Matched: Python, SQL, Pandas
- Missing: AWS, Docker

The score is based on required skills found in the job description, making the result explainable rather than an opaque AI score.

## Why this is a strong portfolio project

This project demonstrates:

1. REST API development
2. Text preprocessing
3. Information extraction
4. Explainable matching logic
5. JSON API design
6. Frontend/backend integration
7. Testing
8. Product-oriented thinking

## Future Improvements

- PDF/DOCX parsing
- Sentence-transformer semantic similarity
- LLM-generated resume feedback
- PostgreSQL persistence
- Authentication
- Resume version tracking
- Job recommendation engine
- Deployment with Docker

## Interview Explanation

> "I built an explainable resume-to-job matching system. Instead of producing an unexplained AI score, I extract skills from both documents, calculate the overlap against job requirements, identify missing skills, and generate interview questions from the detected skills. I exposed the processing pipeline through a FastAPI REST API and connected it to a browser frontend."

## Dataset / Privacy

The included sample resume and job description are fictional. Do not upload confidential personal resumes to a public repository.
>>>>>>> c3bca92 (Initial commit)
