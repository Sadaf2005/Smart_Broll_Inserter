# import whisper

# model = whisper.load_model("base")

# def transcribe_audio(audio_path: str):
#     result = model.transcribe(audio_path)

#     segments = []
#     for seg in result["segments"]:
#         segments.append({
#             "start": seg["start"],
#             "end": seg["end"],
#             "text": seg["text"]
#         })

#     return segments


# from pathlib import Path
# import json
# from app.services.broll_analysis import load_and_normalize_brolls

# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     metadata_path = BASE_DIR / "data" / "b_roll" / "broll_metadata.json"
#     output_path = BASE_DIR / "data" / "outputs" / "broll_descriptions.json"

#     output_path.parent.mkdir(parents=True, exist_ok=True)

#     brolls = load_and_normalize_brolls(str(metadata_path))

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(brolls, f, indent=2, ensure_ascii=False)

#     print("✅ B-roll understanding completed")

#phase 3
# from pathlib import Path
# import json

# from app.services.embeddings import EmbeddingService
# from app.services.matcher import match_brolls_to_transcript

# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     transcript_path = BASE_DIR / "data" / "transcripts" / "a_roll_transcript.json"
#     brolls_path = BASE_DIR / "data" / "outputs" / "broll_descriptions.json"
#     output_path = BASE_DIR / "data" / "outputs" / "matches.json"

#     with open(transcript_path, "r", encoding="utf-8") as f:
#         transcript_segments = json.load(f)

#     with open(brolls_path, "r", encoding="utf-8") as f:
#         brolls = json.load(f)

#     embedder = EmbeddingService()
#     matches = match_brolls_to_transcript(transcript_segments, brolls, embedder)

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(matches, f, indent=2, ensure_ascii=False)

#     print("✅ Semantic matching completed")



#previous to phase 3
# from pathlib import Path
# import json
# from app.services.transcription import extract_audio, transcribe_audio

# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     video_path = BASE_DIR / "data" / "a_roll" / "a_roll.mp4"
#     audio_path = BASE_DIR / "data" / "a_roll" / "a_roll.mp3"
#     transcript_path = BASE_DIR / "data" / "transcripts" / "a_roll_transcript.json"

#     extract_audio(str(video_path), str(audio_path))

#     segments = transcribe_audio(str(audio_path))

#     transcript_path.parent.mkdir(parents=True, exist_ok=True)

#     with open(transcript_path, "w", encoding="utf-8") as f:
#         json.dump(segments, f, indent=2, ensure_ascii=False)

#     print("✅ Transcript regenerated")



##----phase 4

# from pathlib import Path
# import json

# from app.services.planner import build_timeline_plan

# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     matches_path = BASE_DIR / "data" / "outputs" / "matches.json"
#     output_path = BASE_DIR / "data" / "outputs" / "timeline_plan.json"

#     with open(matches_path, "r", encoding="utf-8") as f:
#         matches = json.load(f)

#     timeline_plan = build_timeline_plan(matches)

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(timeline_plan, f, indent=2, ensure_ascii=False)

#     print("✅ Timeline planning completed")





##----timleine tester main code
# from pathlib import Path
# import json

# from app.services.embeddings import EmbeddingService
# from app.services.matcher import match_brolls_to_transcript

# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     transcript_path = BASE_DIR / "data" / "transcripts" / "a_roll_transcript.json"
#     brolls_path = BASE_DIR / "data" / "outputs" / "broll_descriptions.json"
#     output_path = BASE_DIR / "data" / "outputs" / "matches.json"

#     with open(transcript_path, "r", encoding="utf-8") as f:
#         transcript_segments = json.load(f)

#     with open(brolls_path, "r", encoding="utf-8") as f:
#         brolls = json.load(f)

#     print("DEBUG transcript segments:", len(transcript_segments))
#     print("DEBUG broll descriptions:", len(brolls))

#     embedder = EmbeddingService()
#     matches = match_brolls_to_transcript(transcript_segments, brolls, embedder)

#     print("DEBUG matches produced:", len(matches))

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(matches, f, indent=2, ensure_ascii=False)

#     print("✅ Matching step finished")


## final main code
# from pathlib import Path
# import json

# from app.services.planner import build_timeline_plan



# BASE_DIR = Path(__file__).resolve().parent.parent

# if __name__ == "__main__":
#     matches_path = BASE_DIR / "data" / "outputs" / "matches.json"
#     output_path = BASE_DIR / "data" / "outputs" / "timeline_plan.json"

#     with open(matches_path, "r", encoding="utf-8") as f:
#         matches = json.load(f)

#     timeline_plan = build_timeline_plan(matches)

#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(timeline_plan, f, indent=2, ensure_ascii=False)

#     print("✅ Final timeline plan generated")


import uvicorn
from app.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
