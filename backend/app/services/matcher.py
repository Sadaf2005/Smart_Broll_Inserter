from sklearn.metrics.pairwise import cosine_similarity


def match_brolls_to_transcript(transcript_segments, brolls, embedder):
    transcript_texts = [seg["text"] for seg in transcript_segments]
    broll_texts = [b["description"] for b in brolls]

    transcript_embeddings = embedder.embed_texts(transcript_texts)
    broll_embeddings = embedder.embed_texts(broll_texts)

    similarity_matrix = cosine_similarity(
        transcript_embeddings.cpu(),
        broll_embeddings.cpu()
    )

    matches = []

    for i, seg in enumerate(transcript_segments):
        best_idx = similarity_matrix[i].argmax()
        confidence = float(similarity_matrix[i][best_idx])

        # IMPORTANT: relaxed threshold for Hinglish + abstract visuals
        if confidence < 0.15:
            continue

        matches.append({
            "start_sec": seg["start"],
            "end_sec": seg["end"],
            "text": seg["text"],
            "broll_id": brolls[best_idx]["broll_id"],
            "confidence": round(confidence, 2)
        })

    return matches
