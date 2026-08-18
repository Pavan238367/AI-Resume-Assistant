def calculate_score(
    name,
    email_result,
    phone_result,
    found_skills,
    found_education,
    found_experience
):

    resume_score = 0

    if name != "Name Not Found":
        resume_score += 20

    if email_result != "Email Not Found":
        resume_score += 20

    if phone_result != "Phone Not Found":
        resume_score += 20

    if found_skills:
        resume_score += 15

    if found_education:
        resume_score += 15

    if found_experience:
        resume_score += 10

    if resume_score >= 90:
        rating = "Excellent ⭐⭐⭐⭐⭐"

    elif resume_score >= 75:
        rating = "Very Good ⭐⭐⭐⭐"

    elif resume_score >= 60:
        rating = "Good ⭐⭐⭐"

    elif resume_score >= 40:
        rating = "Average ⭐⭐"

    else:
        rating = "Needs Improvement ⭐"

    return resume_score, rating