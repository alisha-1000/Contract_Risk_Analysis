import streamlit as st
from pypdf import PdfReader
from agent.graph import build_agent

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ContractRisk AI", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
body { background-color: #0E1117; color: white; }

.risk-card { 
    background-color: #161B22; 
    border-radius: 12px; 
    padding: 16px; 
    border: 1px solid #30363D; 
    margin-bottom: 12px;
}

<<<<<<< HEAD
# INPUT SECTION
st.subheader(" Input")
=======
.badge {
    padding: 4px 10px;
    border-radius: 10px;
    font-size: 12px;
    float: right;
    color: white;
}
>>>>>>> 970add7760af7a819298df005baabc35c00195f9

.high { background: #F85149; }
.medium { background: #F59E0B; }
.low { background: #10B981; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📂 Upload Contract")
    file = st.file_uploader("Upload PDF", type="pdf")

    if file:
        reader = PdfReader(file)
        text = "\n".join([p.extract_text() for p in reader.pages])

        st.success("PDF Loaded")

<<<<<<< HEAD
    if uploaded_file:
        contract_text = extract_text_from_pdf(uploaded_file)
        st.success(" PDF processed successfully")

# ANALYZE BUTTON 
if st.button(" Analyze Contract"):

    if not contract_text.strip():
        st.warning("Please provide contract text or upload a PDF.")
    else:
        with st.spinner(" Agent analyzing contract..."):
            result = agent.invoke({"text": contract_text})
=======
        if st.button("🚀 Run Analysis", use_container_width=True):
            agent = build_agent()
            result = agent.invoke({"text": text})
            st.session_state["data"] = result

# ---------------- MAIN ----------------
if "data" in st.session_state:

    res = st.session_state["data"]
    clauses = res["results"]
>>>>>>> 970add7760af7a819298df005baabc35c00195f9

    col1, col2 = st.columns([1.2, 2])

<<<<<<< HEAD
        st.subheader(" Risk Analysis Report")
        st.text(report)

        # DOWNLOAD BUTTON
=======
    # LEFT: DOCUMENT
    with col1:
        st.subheader("📄 Document")
        st.text_area("Preview", res["text"][:5000], height=600)

    # RIGHT: ANALYSIS
    with col2:
        st.subheader("📊 Clause Analysis")

        for item in clauses:

            txt = item["analysis"].lower()

            if "high" in txt:
                color = "high"
                label = "High Risk"
            elif "medium" in txt:
                color = "medium"
                label = "Medium Risk"
            else:
                color = "low"
                label = "Low Risk"

            st.markdown(f"""
            <div class="risk-card">
                <span class="badge {color}">{label}</span>

                <b>Clause:</b><br>
                <div style="color:#9ca3af;">
                    {item['clause']}
                </div>

                <br><b>Analysis:</b><br>
                {item['analysis']}
            </div>
            """, unsafe_allow_html=True)

>>>>>>> 970add7760af7a819298df005baabc35c00195f9
        st.download_button(
            "📄 Download Report",
            res["report"],
            file_name="report.txt"
        )

<<<<<<< HEAD
#DISCLAIMER
st.markdown("---")
st.caption(" This analysis is AI-generated and does not constitute legal advice.")
=======
else:
    st.info("Upload a contract and click Run Analysis")
>>>>>>> 970add7760af7a819298df005baabc35c00195f9
