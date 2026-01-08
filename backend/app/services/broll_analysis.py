import json
from pathlib import Path
from app.schemas import BrollDescription


def load_and_normalize_brolls(metadata_path: str):
    """
    Load B-roll metadata and normalize it into a clean semantic format
    """
    with open(metadata_path, "r", encoding="utf-8") as f:
        raw_brolls = json.load(f)

    normalized = []

    for item in raw_brolls:
        normalized.append(
            BrollDescription(
                broll_id=item["id"],
                description=item["metadata"].strip()
            ).dict()
        )

    return normalized
