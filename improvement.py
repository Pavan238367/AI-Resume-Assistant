def generate_improvements(
    name,
    email,
    phone,
    skills,
    education,
    experience,
    resume_score,
    ats_score,
    match_score
):

    improvements = []


    # ---------------------------------------
    # Contact Information
    # ---------------------------------------

    if email == "Email Not Found":

        improvements.append(
            "Add a professional email address to your resume."
        )


    if phone == "Phone Not Found":

        improvements.append(
            "Add your phone number to your resume."
        )


    # ---------------------------------------
    # Skills
    # ---------------------------------------

    if len(skills) < 3:

        improvements.append(
            "Add more relevant technical skills to strengthen your resume."
        )


    # ---------------------------------------
    # Education
    # ---------------------------------------

    if not education:

        improvements.append(
            "Add your educational qualifications."
        )


    # ---------------------------------------
    # Experience
    # ---------------------------------------

    if not experience:

        improvements.append(
            "Add internships, projects, or work experience."
        )


    # ---------------------------------------
    # Resume Score
    # ---------------------------------------

    if resume_score < 60:

        improvements.append(
            "Your resume score is low. Improve your contact details, "
            "skills, education and experience sections."
        )


    # ---------------------------------------
    # ATS Score
    # ---------------------------------------

    if ats_score < 60:

        improvements.append(
            "Improve your ATS score by adding relevant skills "
            "and important job-related keywords."
        )


    # ---------------------------------------
    # Job Match
    # ---------------------------------------

    if match_score < 60:

        improvements.append(
            "Your resume has a low job match. Add keywords and skills "
            "from the target job description where they genuinely apply."
        )


    # ---------------------------------------
    # Excellent Resume
    # ---------------------------------------

    if not improvements:

        improvements.append(
            "Your resume looks strong. Keep your skills and experience "
            "updated for each job application."
        )


    return improvements