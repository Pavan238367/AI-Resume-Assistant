def calculate_job_match(resume_text, job_description):

    keyword_groups = {

        "Python": [
            "python"
        ],

        "Java": [
            "java"
        ],

        "C": [
            "c programming",
            "language c"
        ],

        "C++": [
            "c++"
        ],

        "HTML": [
            "html"
        ],

        "CSS": [
            "css"
        ],

        "JavaScript": [
            "javascript",
            "js"
        ],

        "SQL": [
            "sql"
        ],

        "MySQL": [
            "mysql"
        ],

        "Flask": [
            "flask"
        ],

        "Django": [
            "django"
        ],

        "Machine Learning": [
            "machine learning",
            "ml"
        ],

        "Deep Learning": [
            "deep learning",
            "dl"
        ],

        "Artificial Intelligence": [
            "artificial intelligence",
            "ai"
        ],

        "TensorFlow": [
            "tensorflow"
        ],

        "PyTorch": [
            "pytorch"
        ],

        "NumPy": [
            "numpy"
        ],

        "Pandas": [
            "pandas"
        ],

        "Scikit-learn": [
            "scikit-learn",
            "sklearn"
        ],

        "Git": [
            "git"
        ],

        "GitHub": [
            "github"
        ]
    }


    resume_text = resume_text.lower()

    job_description = job_description.lower()


    required_keywords = []

    matched_keywords = []


    # ---------------------------------------
    # Find Required Keywords
    # ---------------------------------------

    for keyword, variations in keyword_groups.items():

        for variation in variations:

            if variation in job_description:

                required_keywords.append(keyword)

                break


    # ---------------------------------------
    # Find Matching Keywords
    # ---------------------------------------

    for keyword in required_keywords:

        variations = keyword_groups[keyword]

        for variation in variations:

            if variation in resume_text:

                matched_keywords.append(keyword)

                break


    # ---------------------------------------
    # Calculate Match Score
    # ---------------------------------------

    if required_keywords:

        match_score = int(
            (len(matched_keywords) / len(required_keywords)) * 100
        )

    else:

        match_score = 0


    return (
        required_keywords,
        matched_keywords,
        match_score
    )