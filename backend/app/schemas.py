from pydantic import BaseModel

class TranscriptSegment(BaseModel):
    start_sec: float
    end_sec: float
    text: str



class BrollDescription(BaseModel):
    broll_id: str
    description: str
