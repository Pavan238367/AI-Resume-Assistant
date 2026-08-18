def generate_summary(
    name,
    skills,
    education,
    experience,
    resume_score,
    ats_score,
    match_score
):

    if skills:
        skills_text = ", ".join(skills)
    else:
        skills_text = "No skills found"


    if education:
        education_text = ", ".join(education)
    else:
        education_text = "No education found"


    if experience:
        experience_text = ", ".join(experience)
    else:
        experience_text = "No experience found"


    summary = {
        "name": name,
        "skills": skills_text,
        "education": education_text,
        "experience": experience_text,
        "resume_score": resume_score,
        "ats_score": ats_score,
        "match_score": match_score
    }


    return summary