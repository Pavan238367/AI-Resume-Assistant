import sqlite3


DATABASE = "resume_history.db"


# ---------------------------------------
# Create Database
# ---------------------------------------

def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            email TEXT,

            resume_score INTEGER,

            ats_score INTEGER,

            job_match_score INTEGER,

            analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


# ---------------------------------------
# Save Resume Result
# ---------------------------------------

def save_result(
    name,
    email,
    resume_score,
    ats_score,
    job_match_score
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO resume_history
        (
            name,
            email,
            resume_score,
            ats_score,
            job_match_score
        )

        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        email,
        resume_score,
        ats_score,
        job_match_score
    ))

    connection.commit()

    connection.close()


# ---------------------------------------
# Get Resume History
# ---------------------------------------

def get_history():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            email,
            resume_score,
            ats_score,
            job_match_score,
            analysis_date

        FROM resume_history

        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


# ---------------------------------------
# Get Dashboard Statistics
# ---------------------------------------

def get_statistics():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(resume_score),
            AVG(ats_score),
            AVG(job_match_score)

        FROM resume_history
    """)

    statistics = cursor.fetchone()

    connection.close()


    total_resumes = statistics[0] or 0

    average_resume_score = round(
        statistics[1] or 0,
        1
    )

    average_ats_score = round(
        statistics[2] or 0,
        1
    )

    average_job_match = round(
        statistics[3] or 0,
        1
    )


    return (
        total_resumes,
        average_resume_score,
        average_ats_score,
        average_job_match
    )