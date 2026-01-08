# Smart B-Roll Inserter for UGC Videos

## 📌 Overview

This project implements a **Smart B-Roll Inserter system** that automatically plans how B-roll clips should be inserted into an A-roll (talking-head / UGC) video.

Given:
- One A-roll video (speaker talking to camera)
- Multiple B-roll clips (product shots, lifestyle shots, etc.)

The system:
1. Understands **what is being said and when** in the A-roll
2. Understands **what each B-roll clip represents**
3. Uses **semantic matching** to decide:
   - **where** B-roll should be inserted
   - **which** B-roll fits best
4. Outputs a **structured timeline plan in JSON format**
5. Exposes the pipeline via **FastAPI (Swagger UI)** and a **minimal React UI**

The focus of this project is **reasoning, system design, and correctness**, not UI polish.

---

## 🧠 System Architecture (High Level)
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


---

## 🛠️ Tech Stack & Justification

### Backend

| Technology | Why it is used |
|----------|---------------|
| Python | Required by assignment, strong ecosystem for ML/NLP/video |
| FastAPI | Lightweight, fast, auto Swagger UI, ideal for ML services |
| ffmpeg | Industry-standard tool for video/audio processing |
| Whisper (local) | Accurate timestamped transcription without API limits |
| Sentence Transformers | Local semantic embeddings for matching |
| scikit-learn | Cosine similarity for semantic matching |

### Frontend

| Technology | Why it is used |
|----------|---------------|
| React | Required by assignment, simple UI for triggering pipeline |
| Fetch API | Minimal dependency approach |

### UI Strategy

- **Swagger UI** is intentionally used as a *developer/editor interface* to:
  - Trigger timeline generation
  - Inspect transcript, B-rolls, and final plan
- **React UI** is kept minimal to demonstrate end-to-end integration

---


---

## 🔍 Core Pipeline Explained

### 1️⃣ A-Roll Understanding
- Audio extracted from video using `ffmpeg`
- Transcription generated with **Whisper**
- Sentence-level timestamps preserved

### 2️⃣ B-Roll Understanding
- Provided metadata normalized into semantic descriptions
- Each B-roll represented as a textual concept

### 3️⃣ Semantic Matching
- Transcript segments and B-roll descriptions embedded
- Cosine similarity used for semantic alignment
- Best matching B-roll chosen per segment
- Thresholds relaxed to handle **Hinglish + abstract visuals**

### 4️⃣ Timeline Planning
- Enforced rules:
  - Minimum gap between insertions
  - Maximum number of B-rolls
  - Confidence threshold
- Output includes timestamp, duration, confidence, and reasoning

---

## 📤 Output Format (Required)

Example output (`timeline_plan.json`):

```json
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
```


## 🚀 How to Run the Project
## 1️⃣ Create & activate virtual environment

``` cd backend
python -m venv venv
venv\Scripts\activate   # Windows
```

## 2️⃣ Install dependencies

```
pip install -r requirements.txt
pip install fastapi uvicorn

```
## 3️⃣ Verify ffmpeg

```
ffmpeg -version
```

## ▶️ Start FastAPI Backend (Swagger UI)

```
cd backend
uvicorn app.main:app --reload


OR

python -m uvicorn app.main:app --reload

```

```
Access:

Health check:
http://localhost:8000/health

Swagger UI:
http://localhost:8000/docs

From Swagger UI:

Use POST /generate-plan

Click Try it out → Execute

Inspect transcript, B-rolls, and timeline plan
```
## 🌐 Frontend (React UI)
## 1️⃣ Install dependencies

```
cd frontend
npm install

```


## 2️⃣ Start React app

```
npm start
```


## Sharing Environmental File (.env)
```
OPENAI_API_KEY=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

```
