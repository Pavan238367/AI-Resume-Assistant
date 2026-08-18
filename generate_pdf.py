from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    name,
    email,
    phone,
    skills,
    education,
    experience,
    resume_score,
    rating,
    ats_score,
    strength,
    match_score,
    resume_summary
):

    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(
        Paragraph(
            "AI Resume Analyzer",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Personal Details
    content.append(
        Paragraph(
            "<b>Name:</b> " + str(name),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Email:</b> " + str(email),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Phone:</b> " + str(phone),
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    # Skills
    skills_text = ", ".join(skills) if skills else "No Skills Found"

    content.append(
        Paragraph(
            "<b>Skills:</b> " + skills_text,
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # Education
    education_text = (
        ", ".join(education)
        if education
        else "No Education Found"
    )

    content.append(
        Paragraph(
            "<b>Education:</b> " + education_text,
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # Experience
    experience_text = (
        ", ".join(experience)
        if experience
        else "No Experience Found"
    )

    content.append(
        Paragraph(
            "<b>Experience:</b> " + experience_text,
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

        # Resume Summary

    content.append(
        Paragraph(
            "<b>Resume Summary</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "<b>Skills:</b> "
            + str(resume_summary.get("skills", "")),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Education:</b> "
            + str(resume_summary.get("education", "")),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Experience:</b> "
            + str(resume_summary.get("experience", "")),
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    # Scores
    content.append(
        Paragraph(
            "<b>Resume Score:</b> "
            + str(resume_score)
            + "/100",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Rating:</b> "
            + str(rating),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>ATS Score:</b> "
            + str(ats_score)
            + "%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>ATS Strength:</b> "
            + str(strength),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "<b>Job Match Score:</b> "
            + str(match_score)
            + "%",
            styles["Normal"]
        )
    )

    # Build PDF
    document.build(content)