def calculate_ats_score(
    name,
    email_result,
    phone_result,
    found_skills,
    found_education,
    found_experience
):

    ats_score = 0

    # Name
    if name != "Name Not Found":
        ats_score += 10

    # Email
    if email_result != "Email Not Found":
        ats_score += 15

    # Phone
    if phone_result != "Phone Not Found":
        ats_score += 15

    # Skills
    if found_skills:
        ats_score += 30

    # Education
    if found_education:
        ats_score += 15

    # Experience
    if found_experience:
        ats_score += 15


    # ATS Strength and Color

    if ats_score >= 85:

        strength = "🟢 Strong Resume"
        color = "green"

    elif ats_score >= 60:

        strength = "🟡 Average Resume"
        color = "orange"

    else:

        strength = "🔴 Weak Resume"
        color = "red"


    return ats_score, strength, color