Smart B-Roll Inserter for UGC Videos
📌 Overview

This project implements a Smart B-Roll Inserter system that automatically plans how B-roll clips should be inserted into an A-roll (talking-head / UGC) video.

Given:

One A-roll video (speaker talking to camera)

Multiple B-roll clips (product shots, lifestyle shots, etc.)

The system:

Understands what is being said and when in the A-roll

Understands what each B-roll clip represents

Uses semantic matching to decide:

where B-roll should be inserted

which B-roll fits best

Outputs a structured timeline plan in JSON format

Exposes the pipeline via FastAPI (Swagger UI) and a minimal React UI

The focus of this project is reasoning, system design, and correctness, not UI polish.

🧠 System Architecture (High Level)
A-roll Video
   ↓
Audio Extraction (ffmpeg)
   ↓
Speech Transcription (Whisper)
   ↓
Transcript Segmentation (timestamps)

B-roll Metadata
   ↓
Semantic Descriptions

Transcript + B-roll Descriptions
   ↓
Embeddings (Sentence Transformers)
   ↓
Semantic Matching
   ↓
Timeline Planning
   ↓
JSON Timeline Plan

FastAPI (Swagger UI) + React UI

🛠️ Tech Stack & Justification
Backend
Technology	Why it is used
Python	Required by assignment, best ecosystem for ML, NLP, and video tooling
FastAPI	Lightweight, fast, auto-generated Swagger UI, ideal for ML pipelines
ffmpeg	Industry-standard tool for video/audio processing
Whisper (local)	Accurate timestamped transcription, avoids API quota limits
Sentence Transformers	Local semantic embeddings for matching speech to visuals
scikit-learn	Cosine similarity for semantic matching
Frontend
Technology	Why it is used
React	Required by assignment, simple UI for triggering pipeline and viewing output
Fetch API	Minimal dependency approach
UI Strategy

Swagger UI is intentionally used as a developer/editor interface to:

Trigger timeline generation

Inspect transcript, B-rolls, and final plan

React UI is kept minimal to demonstrate end-to-end integration

📂 Project Structure
smart-broll-inserter/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI entry point
│   │   ├── api.py             # API routes
│   │   ├── schemas.py         # Data models
│   │   ├── services/
│   │   │   ├── transcription.py
│   │   │   ├── broll_analysis.py
│   │   │   ├── embeddings.py
│   │   │   ├── matcher.py
│   │   │   └── planner.py
│   ├── data/
│   │   ├── a_roll/
│   │   ├── b_roll/
│   │   └── outputs/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── App.js
│   └── package.json
│
└── README.md

🔍 Core Pipeline Explained
1️⃣ A-Roll Understanding

Audio extracted from video using ffmpeg

Transcription generated with Whisper

Sentence-level timestamps retained for reasoning

2️⃣ B-Roll Understanding

Provided metadata normalized into semantic text descriptions

Each B-roll represented as a textual concept

3️⃣ Semantic Matching

Transcript segments and B-roll descriptions embedded

Cosine similarity used for semantic alignment

Best matching B-roll chosen per segment

Thresholds relaxed to handle Hinglish + abstract visuals

4️⃣ Timeline Planning

Filters applied:

Minimum gap between insertions

Maximum number of B-rolls

Confidence threshold

Output includes:

Timestamp

Duration

B-roll ID

Confidence

Human-readable reason

📤 Output Format (Required)

Example output (timeline_plan.json):

{
  "total_insertions": 4,
  "insertions": [
    {
      "start_sec": 12.4,
      "duration_sec": 2.0,
      "broll_id": "broll_3",
      "confidence": 0.28,
      "reason": "B-roll selected because it visually reinforces the spoken content: 'Street food khate waqt hygiene...'"
    }
  ]
}

🚀 How to Run the Project
🔧 Backend Setup
1️⃣ Create & activate virtual environment
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install dependencies
pip install -r requirements.txt
pip install uvicorn fastapi

3️⃣ Make sure ffmpeg is installed
ffmpeg -version

▶️ Start FastAPI Backend (Swagger UI)
cd backend
uvicorn app.main:app --reload


OR (fallback):

python -m uvicorn app.main:app --reload

Access:

Health check:
👉 http://localhost:8000/health

Swagger UI:
👉 http://localhost:8000/docs

From Swagger UI:

Use POST /generate-plan

Click Try it out → Execute

View transcript, B-rolls, and timeline plan

🌐 Frontend (React UI)
1️⃣ Install dependencies
cd frontend
npm install

2️⃣ Start React app
npm start

Access:

👉 http://localhost:3000

Features:

Button to trigger timeline generation

Timeline JSON rendered in readable format

🎯 Design Trade-Offs & Decisions

Swagger UI used intentionally as a functional interface for inspecting system behavior

Local Whisper chosen to avoid API quota issues

Minimal React UI to demonstrate integration without overengineering

No video rendering UI (explicitly optional per assignment)

✅ Assignment Requirements Coverage
Requirement	Status
Python backend	✅
ffmpeg usage	✅
Semantic matching	✅
Timeline JSON output	✅
React interface	✅
Swagger UI	✅
Video rendering	Optional (not implemented)
📌 Final Notes

This project focuses on:

Correctness

Explainability

System design clarity

Practical engineering trade-offs

It mirrors how such systems are evaluated internally before editor-facing tools are built.
