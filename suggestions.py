def generate_suggestions(
    found_skills,
    found_education,
    found_experience,
    email_result,
    phone_result,
    resume_score
):

    suggestions = []

    if not found_skills:
        suggestions.append("Add more technical skills.")

    if not found_education:
        suggestions.append("Mention your education details.")

    if not found_experience:
        suggestions.append("Add internship or work experience.")

    if email_result == "Email Not Found":
        suggestions.append("Add your email address.")

    if phone_result == "Phone Not Found":
        suggestions.append("Add your phone number.")

    if resume_score < 70:
        suggestions.append(
            "Improve your resume by adding more relevant information."
        )

    return suggestions