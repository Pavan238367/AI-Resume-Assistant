def compare_resumes(resume1, resume2):

    score_difference = (
        resume2["resume_score"]
        - resume1["resume_score"]
    )

    ats_difference = (
        resume2["ats_score"]
        - resume1["ats_score"]
    )

    match_difference = (
        resume2["match_score"]
        - resume1["match_score"]
    )

    # Calculate overall performance
    total1 = (
        resume1["resume_score"]
        + resume1["ats_score"]
        + resume1["match_score"]
    )

    total2 = (
        resume2["resume_score"]
        + resume2["ats_score"]
        + resume2["match_score"]
    )

    average1 = round(total1 / 3, 1)
    average2 = round(total2 / 3, 1)

    if average1 > average2:

        winner = resume1["name"]
        winner_score = average1

    elif average2 > average1:

        winner = resume2["name"]
        winner_score = average2

    else:

        winner = "Both Resumes"
        winner_score = average1

    return {
        "resume1": resume1,
        "resume2": resume2,

        "score_difference": score_difference,
        "ats_difference": ats_difference,
        "match_difference": match_difference,

        "winner": winner,
        "winner_score": winner_score
    }