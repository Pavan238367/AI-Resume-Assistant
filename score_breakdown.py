def get_score_breakdown(
    name,
    email,
    phone,
    skills,
    education,
    experience
):

    breakdown = []

    # Name
    if name != "Name Not Found":
        breakdown.append({
            "section": "👤 Name",
            "score": 20,
            "max_score": 20
        })
    else:
        breakdown.append({
            "section": "👤 Name",
            "score": 0,
            "max_score": 20
        })


    # Email
    if email != "Email Not Found":
        breakdown.append({
            "section": "📧 Email",
            "score": 20,
            "max_score": 20
        })
    else:
        breakdown.append({
            "section": "📧 Email",
            "score": 0,
            "max_score": 20
        })


    # Phone
    if phone != "Phone Not Found":
        breakdown.append({
            "section": "📱 Phone",
            "score": 20,
            "max_score": 20
        })
    else:
        breakdown.append({
            "section": "📱 Phone",
            "score": 0,
            "max_score": 20
        })


    # Skills
    if skills:
        breakdown.append({
            "section": "💻 Skills",
            "score": 15,
            "max_score": 15
        })
    else:
        breakdown.append({
            "section": "💻 Skills",
            "score": 0,
            "max_score": 15
        })


    # Education
    if education:
        breakdown.append({
            "section": "🎓 Education",
            "score": 15,
            "max_score": 15
        })
    else:
        breakdown.append({
            "section": "🎓 Education",
            "score": 0,
            "max_score": 15
        })


    # Experience
    if experience:
        breakdown.append({
            "section": "💼 Experience",
            "score": 10,
            "max_score": 10
        })
    else:
        breakdown.append({
            "section": "💼 Experience",
            "score": 0,
            "max_score": 10
        })


    return breakdown