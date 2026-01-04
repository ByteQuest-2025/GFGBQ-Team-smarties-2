import re

def extract_citations(text):
    patterns = [
        r"wikipedia",
        r"\(\d{4}\)",
        r"https?://"
    ]
    citations = []
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            citations.append(p)
    return citations
