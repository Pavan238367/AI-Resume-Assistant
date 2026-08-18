def calculate_strength(
    email,
    phone,
    skills,
    education,
    experience
):

    # Contact Score
    contact_score = 0

    if email != "Email Not Found":
        contact_score += 50

    if phone != "Phone Not Found":
        contact_score += 50


    # Skills Score
    if len(skills) >= 5:
        skills_score = 100

    elif len(skills) >= 3:
        skills_score = 80

    elif len(skills) >= 1:
        skills_score = 50

    else:
        skills_score = 0


    # Education Score
    if education:
        education_score = 100
    else:
        education_score = 0


    # Experience Score
    if experience:
        experience_score = 100
    else:
        experience_score = 40


    return (
        contact_score,
        skills_score,
        education_score,
        experience_score
    )