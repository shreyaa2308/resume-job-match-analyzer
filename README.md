# Resume Job Match Analyzer

An AI-powered function built on Rival's CortexOne platform that analyzes a resume against a job description and returns a match score, aligned skills, skill gaps, and improvement tips.

## Live Tool
https://cortexone.rival.io/marketplace/shreyaa/resume-job-match-analyzer

## Input
- `resume` (string) — full resume text
- `job_description` (string) — full job posting text

## Output
- `match_score` (0-100)
- `matching_skills` (list)
- `missing_skills` (list)
- `strengths` (string)
- `improvement_tip` (string)

## Tech Stack
Python, OpenAI GPT-3.5-turbo, Rival CortexOne
