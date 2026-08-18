import re

def extract_details(text):

    text_lower = text.lower()

    # Name
    lines = text.split("\n")

    name = "Name Not Found"

    for line in lines:
        if line.strip():
            name = line.strip()
            break

    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email_result = email.group() if email else "Email Not Found"

    # Phone
    phone = re.search(r'\b\d{10}\b', text)
    phone_result = phone.group() if phone else "Phone Not Found"

    # Skills
    skills = [
        "Python","Java","C","C++","HTML","CSS","JavaScript",
        "SQL","MySQL","Flask","Django","Machine Learning",
        "Deep Learning","Artificial Intelligence","TensorFlow",
        "PyTorch","NumPy","Pandas","Scikit-learn","Git","GitHub"
    ]

    found_skills = [
        skill for skill in skills
        if skill.lower() in text_lower
    ]

    # Education
    education_list = [
        "Bachelor of Technology","B.Tech","BTech",
        "Bachelor of Engineering","B.E",
        "M.Tech","MCA","MBA",
        "B.Sc","B.Com","Intermediate",
        "SSC","Diploma"
    ]

    found_education = [
        edu for edu in education_list
        if edu.lower() in text_lower
    ]

    # Experience
    experience_list = [
        "Intern","Internship","Software Engineer",
        "Software Developer","Python Developer",
        "Java Developer","Web Developer",
        "Frontend Developer","Backend Developer",
        "Full Stack Developer","AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist","Data Analyst","Fresher"
    ]

    found_experience = [
        exp for exp in experience_list
        if exp.lower() in text_lower
    ]

    return (
        name,
        email_result,
        phone_result,
        found_skills,
        found_education,
        found_experience
    )