from claim_extractor import extract_claims
from citation_detector import extract_citations

text = """Albert Einstein won the Nobel Prize in 1921 (Einstein, 1921).
Python was created in 1989."""

claims = extract_claims(text)
citations = extract_citations(text)

print("Claims:")
for c in claims:
    print("-", c)

print("\nCitations:")
for c in citations:
    print("-", c)
