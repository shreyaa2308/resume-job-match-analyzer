import json
import os
import urllib.request
import urllib.error

def handler(event, context):
    return cortexone_handler(event, context)

def cortexone_handler(event, context):
    try:
        resume = event.get("resume", "")
        job_description = event.get("job_description", "")

        if not resume or not job_description:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Both resume and job_description fields are required."
                })
            }

        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Missing OPENAI_API_KEY"})
            }

        prompt = (
            "You are a professional resume screener. "
            "Analyze the resume against the job description. "
            "Return ONLY a valid JSON object with these keys: "
            "match_score (integer 0-100), "
            "matching_skills (list of strings), "
            "missing_skills (list of strings), "
            "strengths (string), "
            "improvement_tip (string). "
            "No extra text, just JSON.\n\n"
            "RESUME:\n" + resume + "\n\nJOB DESCRIPTION:\n" + job_description
        )

        payload = json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + api_key
            },
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result["choices"][0]["message"]["content"]
            analysis = json.loads(content)

        return {
            "statusCode": 200,
            "body": json.dumps(analysis)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
