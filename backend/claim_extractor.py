def extract_claims(text):
    sentences = text.split(".")
    return [s.strip() for s in sentences if len(s.strip()) > 20]
