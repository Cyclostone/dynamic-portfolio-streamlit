def match_skills(job_description, user_skills):
    job_keywords = set(job_description.lower().split())
    matches = [skill for skill in user_skills if skill.lower() in job_keywords]
    return matches