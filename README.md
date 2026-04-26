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
---

## 🌐 Deployment
Deployed using Streamlit Cloud:
👉 (https://aiagentforrecruiters.streamlit.app/)
\
---

## 📊 Sample Input
Looking for Senior Software Engineer with skills "Python", "Django", "REST APIs", "PostgreSQL", "AWS", "Docker", "Kubernetes", "Redis", "CI/CD", "Microservices"
---

## 📈 Sample Output
- Ranked list of candidates
- Match Score
- Interest Score
- AI-generated response

---

## 🎥 Demo Video
👉 (https://drive.google.com/file/d/1SwHJTp7fN2PZ4kzQxviw4v46p7htymqB/view?usp=sharing)

---

## 🔗 GitHub Repository
👉 (https://github.com/GaneshSunkari66/AI_Talent_Agent)

---

## 💡 Future Improvements
- Real-time candidate scraping (LinkedIn APIs)
- Resume parsing
- Advanced ML-based scoring
---

## 👤 Author
Ganesh Sunkari
