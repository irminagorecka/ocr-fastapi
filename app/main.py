from fastapi import FastAPI
from app.schemas import OCRRequest, OCRResponse
from app.ocr.pipeline import run_ocr
import base64
import time

app = FastAPI(
    title="Custom OCR API",
    description="OCR API for Power Platform automation",
    version="1.0.0"
)

@app.post("/ocr", response_model=OCRResponse)
def ocr_endpoint(request: OCRRequest):
    start_time = time.time()

    image_bytes = base64.b64decode(request.file_base64)
    text_lines = run_ocr(image_bytes, request.document_type)

    processing_time = int((time.time() - start_time) * 1000)

    return OCRResponse(
        text=text_lines,
        document_type=request.document_type,
        processing_time_ms=processing_time
    )
