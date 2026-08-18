from flask import Flask, render_template, request, send_file, session
import os
from werkzeug.utils import secure_filename

from resume_parser import extract_text
from extractor import extract_details
from score import calculate_score
from suggestions import generate_suggestions
from ats import calculate_ats_score
from keywords import find_keywords
from job_match import calculate_job_match
from improvement import generate_improvements
from summary import generate_summary
from strength import calculate_strength
from score_breakdown import get_score_breakdown
from generate_pdf import generate_pdf
from comparison import compare_resumes

from database import (
    create_database,
    save_result,
    get_history,
    get_statistics
)


app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
# Security settings
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


# ---------------------------------------
# Create Database
# ---------------------------------------

create_database()


# ---------------------------------------
# Upload Folder Configuration
# ---------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------------------------------
# Home Page
# ---------------------------------------

@app.route("/")
def home():

    return render_template("upload.html")

# ---------------------------------------
# About Page
# ---------------------------------------

@app.route("/about")
def about():

    return render_template("about.html")


# ---------------------------------------
# Upload Resume
# ---------------------------------------

@app.route("/upload", methods=["POST"])
def upload_file():

    # ---------------------------------------
    # Validate Upload
    # ---------------------------------------

    if "resume" not in request.files:

        return render_template(
            "upload.html",
            error="❌ No resume was uploaded."
        )

    file = request.files["resume"]

    # Get Job Description

    job_description = request.form.get(
        "job_description",
        ""
    ).strip()

    # Check file name
    if file.filename == "":
      return render_template(
        "upload.html",
        error="❌ Please select a resume PDF."
    )


    filename = secure_filename(file.filename)


    if not filename:
      return render_template(
        "upload.html",
        error="❌ Invalid file name."
    )


    if not filename.lower().endswith(".pdf"):
      return render_template(
        "upload.html",
        error="❌ Only PDF files are allowed."
    )


    if job_description == "":
       return render_template(
        "upload.html",
        error="❌ Please enter a job description."
    )


    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)


    # ---------------------------------------
    # Extract Text From PDF
    # ---------------------------------------

    text = extract_text(filepath)


    # ---------------------------------------
    # Job Description Matching
    # ---------------------------------------

    (
        required_keywords,
        matched_keywords,
        match_score
    ) = calculate_job_match(
        text,
        job_description
    )


    # ---------------------------------------
    # Keyword Extraction
    # ---------------------------------------

    found_keywords = find_keywords(text)


    # ---------------------------------------
    # Resume Details Extraction
    # ---------------------------------------

    (
        name,
        email_result,
        phone_result,
        found_skills,
        found_education,
        found_experience
    ) = extract_details(text)


    # ---------------------------------------
    # Resume Score
    # ---------------------------------------

    resume_score, rating = calculate_score(
        name,
        email_result,
        phone_result,
        found_skills,
        found_education,
        found_experience
    )


    # ---------------------------------------
    # ATS Score
    # ---------------------------------------

    (
        ats_score,
        strength,
        color
    ) = calculate_ats_score(
        name,
        email_result,
        phone_result,
        found_skills,
        found_education,
        found_experience
    )

    improvements = generate_improvements(
    name,
    email_result,
    phone_result,
    found_skills,
    found_education,
    found_experience,
    resume_score,
    ats_score,
    match_score
    )


    # ---------------------------------------
    # AI Resume Suggestions
    # ---------------------------------------

    suggestions = generate_suggestions(
        found_skills,
        found_education,
        found_experience,
        email_result,
        phone_result,
        resume_score
    )
      

    summary = generate_summary(
        name,
        found_skills,
        found_education,
        found_experience,
        resume_score,
        ats_score,
        match_score
    )

    session["resume_data"] = {
    "name": name,
    "email": email_result,
    "phone": phone_result,
    "skills": found_skills,
    "education": found_education,
    "experience": found_experience,
    "resume_score": resume_score,
    "rating": rating,
    "ats_score": ats_score,
    "strength": strength,
    "match_score": match_score,
    "resume_summary": summary
    }


    # ---------------------------------------
    # Resume Score Breakdown
    # ---------------------------------------

    score_breakdown = get_score_breakdown(
    name,
    email_result,
    phone_result,
    found_skills,
    found_education,
    found_experience
)    

    # ---------------------------------------
    # Resume Strength Breakdown
    # ---------------------------------------

    (
       
      contact_strength,
      skills_strength,
      education_strength,
      experience_strength
    ) = calculate_strength(
       
       email_result,
       phone_result,
       found_skills,
       found_education,
       found_experience
    )


    # ---------------------------------------
    # Save Result to Database
    # ---------------------------------------

    save_result(
        name,
        email_result,
        resume_score,
        ats_score,
        match_score
    )


    # ---------------------------------------
    # Display Result
    # ---------------------------------------

    return render_template(
        "result.html",

        name=name,

        email=email_result,

        phone=phone_result,

        skills=found_skills,

        education=found_education,

        experience=found_experience,

        score=resume_score,

        rating=rating,

        suggestions=suggestions,
        improvements=improvements,

        ats_score=ats_score,

        strength=strength,

        color=color,

        keywords=found_keywords,

        required_keywords=required_keywords,

        matched_keywords=matched_keywords,

        match_score=match_score,

        resume_summary=summary,

        contact_strength=contact_strength,
        
        skills_strength=skills_strength,

        education_strength=education_strength,

        experience_strength=experience_strength,

        score_breakdown=score_breakdown
    )


# ---------------------------------------
# Resume History
# ---------------------------------------

@app.route("/history")
def history():

    records = get_history()

    return render_template(
        "history.html",
        records=records
    )


# ---------------------------------------
# Analytics Dashboard
# ---------------------------------------

@app.route("/dashboard")
def dashboard():

    (
        total_resumes,
        average_resume_score,
        average_ats_score,
        average_job_match
    ) = get_statistics()


    return render_template(
        "dashboard.html",

        total_resumes=total_resumes,

        average_resume_score=average_resume_score,

        average_ats_score=average_ats_score,

        average_job_match=average_job_match
    )


# ---------------------------------------
# File Too Large Error
# ---------------------------------------

@app.errorhandler(413)
def request_entity_too_large(error):

    return render_template(
        "error.html",
        message="The resume file is too large. Maximum size is 5 MB."
    ), 413
# ---------------------------------------
# General Error Handler
# ---------------------------------------

@app.errorhandler(500)
def internal_server_error(error):

    return render_template(
        "error.html",
        message="An unexpected error occurred while processing your resume."
    ), 500

# ---------------------------------------
# Page Not Found Error
# ---------------------------------------

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


# ---------------------------------------
# Run Flask Application
# ---------------------------------------
@app.route("/download-report")
def download_report():

    resume_data = session.get("resume_data")

    if not resume_data:
        return "Please analyze a resume first."

    filename = "resume_analysis.pdf"

    filepath = os.path.join(
        BASE_DIR,
        filename
    )

    generate_pdf(
        filepath,
        resume_data["name"],
        resume_data["email"],
        resume_data["phone"],
        resume_data["skills"],
        resume_data["education"],
        resume_data["experience"],
        resume_data["resume_score"],
        resume_data["rating"],
        resume_data["ats_score"],
        resume_data["strength"],
        resume_data["match_score"],
        resume_data.get("resume_summary", "")
    )

    return send_file(
        filepath,
        as_attachment=True,
        download_name="resume_analysis.pdf"
    )

@app.route("/compare")
def compare():

    records = get_history()

    if len(records) < 2:
        return "Please analyze at least 2 resumes before comparing."

    record1 = records[0]
    record2 = records[1]

    resume1 = {
        "name": record1[1],
        "email": record1[2],
        "resume_score": record1[3],
        "ats_score": record1[4],
        "match_score": record1[5]
    }

    resume2 = {
        "name": record2[1],
        "email": record2[2],
        "resume_score": record2[3],
        "ats_score": record2[4],
        "match_score": record2[5]
    }

    comparison = compare_resumes(
        resume1,
        resume2
    )

    return render_template(
        "comparison.html",
        comparison=comparison
    )



if __name__ == "__main__":

    app.run(debug=True)