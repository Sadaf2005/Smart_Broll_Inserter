def build_timeline_plan(
    matches,
    min_gap_sec=4,
    max_insertions=5,
    default_duration=2.0,
    min_confidence=0.15
):
    timeline = []
    last_insert_time = -min_gap_sec

    for match in matches:
        start = match["start_sec"]
        confidence = match["confidence"]

        # confidence filter
        if confidence < min_confidence:
            continue

        # spacing rule
        if start - last_insert_time < min_gap_sec:
            continue

        timeline.append({
            "start_sec": round(start, 2),
            "duration_sec": default_duration,
            "broll_id": match["broll_id"],
            "confidence": round(confidence, 2),
            "reason": (
                "B-roll selected because it visually reinforces the spoken "
                f"content: '{match['text']}'"
            )
        })

        last_insert_time = start

        if len(timeline) >= max_insertions:
            break

    return {
        "total_insertions": len(timeline),
        "insertions": timeline
    }
