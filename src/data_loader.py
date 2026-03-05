from pypdf import PdfReader

def load_resume():
    reader = PdfReader("data/resume.pdf")
    resume = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume += text
    return resume

def load_summary():
    with open("data/summary.txt", "r", encoding="utf-8") as f:
        return f.read()
