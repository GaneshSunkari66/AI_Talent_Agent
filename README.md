# 🤖 AI-Powered Talent Scouting & Engagement Agent

## 📌 Overview
This project is an AI-powered recruitment assistant that automates candidate discovery, matching, and engagement.

It takes a Job Description (JD) as input and outputs a ranked list of candidates based on:
- Match Score (skill alignment)
- Interest Score (AI-simulated candidate response)

---

## 🚀 Features
- 🔍 AI-based skill extraction from job descriptions
- 👥 Candidate matching using skill comparison
- 💬 AI-powered interest simulation (LLM-based responses)
- 📊 Ranked candidate shortlist
- 🧠 Explainable scoring system
- 🌐 Simple interactive UI using Streamlit

---

## 🏗️ Architecture
User Input (JD)
    ↓
Skill Extraction
    ↓
Candidate Matching
    ↓
Interest Simulation
    ↓
Score Calculation
    ↓
Ranking Output
---

## 🛠️ Tech Stack
- Python
- Streamlit
- OpenAI API (LLM)
- JSON (dataset)

---

## 📂 Project Structure
ai-talent-agent/
│
├── app.py              ← MAIN CODE
├── candidates.json     ← DATASET
├── requirements.txt    ← LIBRARIES
└── README.md           ← DOCUMENTATION
---

## ▶️ How to Run Locally

### 1. Clone Repo
git clone  cd ai-talent-agent
### 2. Install Dependencies
pip install -r requirements.txt
### 4. Run App
Streamlit run app.py
