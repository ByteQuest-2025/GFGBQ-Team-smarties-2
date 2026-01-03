import re

def extract_citations(text):
    pattern = r"\(.*?\d{4}.*?\)|https?://\S+"
    return re.findall(pattern, text)
