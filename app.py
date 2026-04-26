import streamlit as st
import json
import os
from openai import OpenAI

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="AI Talent Agent",
    page_icon="🤖",
    layout="wide"
)

# ------------------ API SETUP ------------------
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

# ------------------ LOAD DATA ------------------
with open("candidates.json") as f:
    candidates = json.load(f)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main-title {
    text-align: center;
    font-size: 42px;
    color: #38bdf8;
    font-weight: bold;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
}
.score {
    font-size: 16px;
    color: #22c55e;
}
.tag {
    display: inline-block;
    padding: 5px 10px;
    margin: 3px;
    border-radius: 8px;
    background-color: #334155;
    color: white;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">🤖 AI Talent Agent</div>', unsafe_allow_html=True)

jd_input = st.text_area("📄 Enter Job Description", height=180)

# ------------------ FUNCTIONS ------------------

# ✅ Dynamic skill extraction
def extract_skills_advanced(text, candidates):
    text = text.lower()
    all_skills = set()

    for c in candidates:
        for skill in c["skills"]:
            all_skills.add(skill.lower())

    return [skill for skill in all_skills if skill in text]


# ✅ Match score (skills + experience)
def calculate_match(candidate, jd_skills):
    candidate_skills = [s.lower() for s in candidate["skills"]]

    if not jd_skills:
        return 0

    common = set(candidate_skills).intersection(set(jd_skills))
    skill_score = (len(common) / len(jd_skills)) * 100

    exp_score = min(candidate["years_experience"] / 10, 1) * 100

    return (0.6 * skill_score) + (0.4 * exp_score)


# ✅ Interest score (based on response + relevance)
def simulate_interest(candidate, jd_skills):
    overlap = len(set([s.lower() for s in candidate["skills"]]).intersection(jd_skills))
    base = candidate["response_rate"] * 100

    interest = base + (overlap * 5)

    if interest > 90:
        msg = "🔥 Highly Interested"
    elif interest > 70:
        msg = "🙂 Moderately Interested"
    else:
        msg = "😐 Low Interest"

    return min(round(interest, 2), 100), msg


# ✅ Role match boost
def role_match_score(candidate, jd_text):
    if candidate["title"].lower() in jd_text.lower():
        return 20
    return 0


# ------------------ BUTTON ------------------
if st.button("🚀 Find Candidates"):

    if not jd_input.strip():
        st.warning("⚠️ Please enter a job description")
    else:
        jd_skills = extract_skills_advanced(jd_input, candidates)

        results = []

        for c in candidates:
            match = calculate_match(c, jd_skills)
            interest, msg = simulate_interest(c, jd_skills)
            role_score = role_match_score(c, jd_input)

            final = (0.6 * match) + (0.3 * interest) + (0.1 * role_score)

            results.append({
                "name": c["name"],
                "title": c["title"],
                "skills": c["skills"],
                "experience": c["years_experience"],
                "match": match,
                "interest": interest,
                "final": final,
                "msg": msg,
                "location": c["location"],
                "salary": c["expected_salary"]
            })

        results = sorted(results, key=lambda x: x["final"], reverse=True)

        # ------------------ OUTPUT ------------------
        st.markdown("## 🏆 Top Candidates")

        for r in results:
            skills_html = "".join([f'<span class="tag">{s}</span>' for s in r["skills"]])

            st.markdown(f"""
            <div class="card">
                <h3>👤 {r['name']} — {r['title']}</h3>
                <p>📍 {r['location']} | 💼 {r['experience']} yrs | 💰 {r['salary']}</p>
                <p>{skills_html}</p>
                <p class="score">Match Score: {round(r['match'],2)}%</p>
                <p class="score">Interest Score: {r['interest']}%</p>
                <p class="score">Final Score: {round(r['final'],2)}%</p>
                <p>{r['msg']}</p>
            </div>
            """, unsafe_allow_html=True)

        # ------------------ DEBUG / INSIGHT ------------------
        st.markdown("### 🔍 Extracted Skills from JD")
        if jd_skills:
            st.success(", ".join(jd_skills))
        else:
            st.warning("No matching skills found. Try adding keywords like Python, AWS, React, etc.")
