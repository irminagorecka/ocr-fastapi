from app.ocr.printed import ocr_printed_from_bytes
from app.ocr.handwritten import ocr_handwritten_from_bytes

def run_ocr(image_bytes: bytes, document_type: str):
    if document_type == "printed":
        return ocr_printed_from_bytes(image_bytes)

    if document_type == "handwritten":
        return ocr_handwritten_from_bytes(image_bytes)

    raise ValueError("Unsupported document_type")
