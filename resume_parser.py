import pdfplumber

def extract_text(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text