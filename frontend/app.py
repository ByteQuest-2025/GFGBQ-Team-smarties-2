import streamlit as st
from backend.claim_extractor import extract_claims
from backend.citation_detector import extract_citations

st.set_page_config(page_title="TruthCheck AI")

st.title("TruthCheck AI")
st.caption("Checking the safety and reliability of AI-generated information")

text = st.text_area("Paste AI-generated information here", height=200)

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        claims = extract_claims(text)
        citations = extract_citations(text)

        # ------------------------
        # Show extracted information
        # ------------------------
        st.subheader("Extracted Information Statements")
        for c in claims:
            st.write("•", c)

        # ------------------------
        # Show source info
        # ------------------------
        st.subheader("Source Mentioned (if any)")
        if citations:
            for c in citations:
                st.write("•", c)
        else:
            st.write("None")

        # ------------------------
        # Generic Risk / Hallucination Detection
        # ------------------------
        issues = []

        # Rule 1: No source provided
        if not citations:
            issues.append("No source was provided to support the information.")

        # Rule 2: Absolute words (often unreliable)
        absolute_words = ["always", "never", "all", "100%", "guaranteed", "completely"]
        for claim in claims:
            for word in absolute_words:
                if word in claim.lower():
                    issues.append(
                        f"The statement uses absolute wording ('{word}'), which may be unreliable."
                    )

        # Rule 3: Future predictions stated as facts
        future_words = ["will", "by 2030", "by 2040", "in the future"]
        for claim in claims:
            for word in future_words:
                if word in claim.lower():
                    issues.append(
                        "A future prediction is stated as a fact without evidence."
                    )

        # ------------------------
        # Final Result (RED = Unsafe, GREEN = Safe)
        # ------------------------
        st.markdown("---")

        if issues:
            st.markdown(
                "<h3 style='color:red;'>⚠️ Unsafe Content Detected</h3>",
                unsafe_allow_html=True
            )
            for issue in set(issues):
                st.markdown(
                    f"<p style='color:red;'>• {issue}</p>",
                    unsafe_allow_html=True
                )
        else:
            st.markdown(
                "<h3 style='color:green;'>✅ Content Appears Safe</h3>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='color:green;'>No major hallucination or source-related risks were detected.</p>",
                unsafe_allow_html=True
            )
