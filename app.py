import streamlit as st
import json
from openai import OpenAI

# ⚠️ Use env variable later (not hardcoded)
client = OpenAI(api_key="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")

# Load data
with open("candidates.json") as f:
    candidates = json.load(f)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main-title {
    text-align: center;
    font-size: 40px;
    color: #38bdf8;
    font-weight: bold;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}
.score {
    font-size: 18px;
    color: #22c55e;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🤖 AI Talent Agent</div>', unsafe_allow_html=True)

jd_input = st.text_area("📄 Enter Job Description")

# ---------------- FUNCTIONS ----------------
def extract_skills_basic(text):
    keywords = ["python", "sql", "machine learning", "java", "aws", "react"]
    return [k for k in keywords if k in text.lower()]

def calculate_match(candidate_skills, jd_skills):
    if not jd_skills:
        return 0
    common = set(candidate_skills).intersection(set(jd_skills))
    return (len(common) / len(jd_skills)) * 100

def simulate_interest(candidate, jd_skills):
    common = set(candidate["skills"]).intersection(set(jd_skills))

    if len(common) >= 3:
        return 85, "Highly interested"
    elif len(common) == 2:
        return 65, "Moderately interested"
    else:
        return 45, "Less interested"

# ---------------- BUTTON ----------------
if st.button("🚀 Find Candidates"):

    jd_skills = extract_skills_basic(jd_input)

    results = []

    for c in candidates:
        match = calculate_match(c["skills"], jd_skills)
        interest, msg = simulate_interest(c, jd_skills)
        final = (0.7 * match) + (0.3 * interest)

        results.append({
            "name": c["name"],
            "skills": c["skills"],
            "match": match,
            "interest": interest,
            "final": final,
            "msg": msg
        })

    results = sorted(results, key=lambda x: x["final"], reverse=True)

    # ---------------- OUTPUT UI ----------------
    st.markdown("## 🏆 Top Candidates")

    for r in results:
        st.markdown(f"""
        <div class="card">
            <h3>👤 {r['name']}</h3>
            <p><b>Skills:</b> {", ".join(r['skills'])}</p>
            <p class="score">Match Score: {round(r['match'],2)}%</p>
            <p class="score">Interest Score: {r['interest']}%</p>
            <p class="score">Final Score: {round(r['final'],2)}%</p>
            <p>💬 {r['msg']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔍 Extracted Skills")
    st.write(jd_skills)
