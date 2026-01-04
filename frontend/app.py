import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
    
import streamlit as st
from backend.claim_extractor import extract_claims
from backend.verifier import verify_claim


st.set_page_config(page_title="TruthCheck AI")

st.title("TruthCheck AI")
st.caption("Checking the safety and reliability of AI-generated information")

text = st.text_area("Paste AI-generated information here", height=200)

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        claims = extract_claims(text)

        st.subheader("Extracted Information Statements")
        for c in claims:
            st.write("•", c)

        st.markdown("---")
        st.subheader("Verification Results")

        for claim in claims:
            result = verify_claim(claim)

            if result["status"] == "verified":
                st.markdown(
                    f"""
                    <div style="color:green;">
                    ✅ <b>VERIFIED</b><br>
                    Claim: {claim}<br>
                    Source: {result['source']}<br>
                    Confidence: {result['confidence']}%<br>
                    Evidence: {result['evidence']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif result["status"] == "false":
                st.markdown(
                    f"""
                    <div style="color:red;">
                    ❌ <b>FALSE</b><br>
                    Claim: {claim}<br>
                    Reason: {result['evidence']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    f"""
                    <div style="color:orange;">
                    ⚠️ <b>UNCERTAIN</b><br>
                    Claim: {claim}<br>
                    Source: {result['source']}<br>
                    Confidence: {result.get("confidence", "N/A")}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )
