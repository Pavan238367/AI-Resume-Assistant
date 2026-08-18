def find_keywords(text):

    keywords = [
        "Python",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "MySQL",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "TensorFlow",
        "PyTorch",
        "NumPy",
        "Pandas",
        "Scikit-learn",
        "Git",
        "GitHub"
    ]

    text_lower = text.lower()

    found_keywords = []

    for keyword in keywords:

        if keyword.lower() in text_lower:
            found_keywords.append(keyword)

    return found_keywords