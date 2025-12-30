from pydantic import BaseModel
from typing import List

class OCRRequest(BaseModel):
    file_base64: str
    document_type: str  # "printed" | "handwritten"

class OCRResponse(BaseModel):
    text: List[str]
    document_type: str
    processing_time_ms: int
