import streamlit as st
from backend.claim_extractor import extract_claims
from backend.citation_detector import extract_citations

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="TruthCheck AI")

st.title("TruthCheck AI")
st.caption("Checking the safety and reliability of AI-generated information")

# ------------------------
# User Input
# ------------------------
text = st.text_area(
    "Paste AI-generated information here",
    height=200
)

# ------------------------
# Analyze Button
# ------------------------
if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # ------------------------
        # Extract information
        # ------------------------
        claims = extract_claims(text)
        citations = extract_citations(text)

        # ------------------------
        # Fallback: detect simple source words
        # ------------------------
        trusted_sources = [
            "wikipedia", "who", "nasa", "britannica",
            "research", "journal", "doi", "source"
        ]

        text_lower = text.lower()

        if not citations:
            for src in trusted_sources:
                if src in text_lower:
                    citations.append(src.capitalize())
                    break

        # ------------------------
        # Display extracted statements
        # ------------------------
        st.subheader("Extracted Information Statements")
        for c in claims:
            st.write("•", c)

        # ------------------------
        # Display source info
        # ------------------------
        st.subheader("Source Mentioned (if any)")
        if citations:
            for c in citations:
                st.write("•", c)
        else:
            st.write("None")

        # ------------------------
        # Final Decision Logic
        # ------------------------
        st.markdown("---")

        if citations:
            # GREEN – Source exists
            st.markdown(
                "<h3 style='color:green;'>✅ Content Appears Safe</h3>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='color:green;'>A source is mentioned, which improves reliability.</p>",
                unsafe_allow_html=True
            )
        else:
            # RED – No source
            st.markdown(
                "<h3 style='color:red;'>⚠️ Potentially Unsafe Content</h3>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='color:red;'>No source was mentioned to support the information.</p>",
                unsafe_allow_html=True
            )
