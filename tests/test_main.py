from backend.main import extract_skills, analyze, AnalyzeRequest

def test_extract_skills():
    skills = extract_skills("Python SQL Pandas Docker AWS")
    assert "python" in skills
    assert "sql" in skills
    assert "pandas" in skills
    assert "docker" in skills
    assert "aws" in skills

def test_match_score():
    result = analyze(AnalyzeRequest(
        resume_text="Python SQL Pandas Git",
        job_description="Python SQL Pandas Docker AWS"
    ))
    assert result["match_percentage"] == 60.0
    assert "docker" in result["missing_skills"]
    assert "python" in result["matched_skills"]
