# from fastapi import FastAPI
# from pathlib import Path
# import json

# from app.services.planner import build_timeline_plan

# app = FastAPI(title="Smart B-Roll Inserter")

# BASE_DIR = Path(__file__).resolve().parent.parent


# @app.get("/health")
# def health_check():
#     return {"status": "ok"}


# @app.post("/generate-plan")
# def generate_plan():
#     matches_path = BASE_DIR / "data" / "outputs" / "matches.json"

#     with open(matches_path, "r", encoding="utf-8") as f:
#         matches = json.load(f)

#     timeline_plan = build_timeline_plan(matches)

#     return timeline_plan


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json

from app.services.planner import build_timeline_plan

app = FastAPI(title="Smart B-Roll Inserter")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


@app.get("/health")
def health_check():
    return {"status": "ok"}


# @app.post("/generate-plan")
# def generate_plan():
#     matches_path = BASE_DIR / "data" / "outputs" / "matches.json"

#     with open(matches_path, "r", encoding="utf-8") as f:
#         matches = json.load(f)

#     timeline_plan = build_timeline_plan(matches)

#     return timeline_plan


@app.post("/generate-plan")
def generate_plan():
    transcript_path = BASE_DIR / "data" / "transcripts" / "a_roll_transcript.json"
    brolls_path = BASE_DIR / "data" / "outputs" / "broll_descriptions.json"
    matches_path = BASE_DIR / "data" / "outputs" / "matches.json"

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    with open(brolls_path, "r", encoding="utf-8") as f:
        brolls = json.load(f)

    with open(matches_path, "r", encoding="utf-8") as f:
        matches = json.load(f)

    timeline_plan = build_timeline_plan(matches)

    return {
        "a_roll": {
            "transcript_segments": transcript
        },
        "b_rolls": brolls,
        "timeline_plan": timeline_plan
    }
