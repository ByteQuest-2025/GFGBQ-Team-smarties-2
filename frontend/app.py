import streamlit as st
from backend.claim_extractor import extract_claims
from backend.citation_detector import extract_citations

st.title("AI Hallucination & Citation Verification")

text = st.text_area("Paste AI-generated text")

if st.button("Analyze"):
    claims = extract_claims(text)
    citations = extract_citations(text)

    st.subheader("Extracted Claims")
    for c in claims:
        st.write("-", c)

    st.subheader("Source Mentioned")

    if not citations:
        st.write("None")
    else:
        for c in citations:
            st.write("-", c)
            
