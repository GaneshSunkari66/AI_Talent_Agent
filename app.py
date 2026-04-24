import streamlit as st
import json
import os
from openai import OpenAI

# 🔐API key (environment variable use karo)
client = OpenAI(api_key='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')

# Load candidates
with open("candidates.json") as f:
    candidates = json.load(f)

st.title("🤖 AI Talent Scouting Agent")

jd_input = st.text_area("Paste Job Description")


# -------------------------------
# ✅ Cached AI Skill Extraction
# -------------------------------
@st.cache_data(show_spinner=False)
def extract_skills_ai(jd):
    try:
        prompt = f"""
        Extract key technical skills from the following job description.
        Return only a comma-separated list.

        JD:
        {jd}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        skills = response.choices[0].message.content
        return [s.strip() for s in skills.split(",")]

    except Exception:
        # 🔁 Fallback (no API crash)
        return extract_skills_basic(jd)


# -------------------------------
# ✅ FREE fallback (no API)
# -------------------------------
def extract_skills_basic(text):
    keywords = ["python", "sql", "machine learning", "java", "aws", "react"]
    return [k for k in keywords if k in text.lower()]


# -------------------------------
# ✅ Replace with rule-based logic
# -------------------------------
def simulate_interest(candidate, jd_skills):
    common = set(candidate["skills"]).intersection(set(jd_skills))

    if len(common) >= 3:
        return 85, "Yes, I am very interested in this role."
    elif len(common) == 2:
        return 65, "Maybe, this role looks interesting."
    else:
        return 45, "Not very interested."


# -------------------------------
# Match Score
# -------------------------------
def calculate_match(candidate_skills, jd_skills):
    if not jd_skills:
        return 0
    common = set(candidate_skills).intersection(set(jd_skills))
    return (len(common) / len(jd_skills)) * 100


# -------------------------------
# 🚀 Run
# -------------------------------
if st.button("Find Candidates"):

    if jd_input.strip() == "":
        st.warning("Please enter a job description")

    else:
        with st.spinner("Analyzing candidates..."):

            jd_skills = extract_skills_ai(jd_input)

            results = []

            for candidate in candidates:
                match_score = calculate_match(candidate["skills"], jd_skills)

                # ✅ No API call here
                interest_score, reply = simulate_interest(candidate, jd_skills)

                final_score = (0.7 * match_score) + (0.3 * interest_score)

                results.append({
                    "Name": candidate["name"],
                    "Match Score": round(match_score, 2),
                    "Interest Score": interest_score,
                    "Final Score": round(final_score, 2),
                    "AI Response": reply
                })

            results = sorted(results, key=lambda x: x["Final Score"], reverse=True)

        st.subheader("🏆 Ranked Candidates")
        st.table(results)

        st.subheader("🔍 Extracted Skills")
        st.write(jd_skills)
