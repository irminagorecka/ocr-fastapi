import easyocr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import io
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-base-handwritten"
)
model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

def recognize_line(pil_image: Image.Image) -> str:
    pil_image = pil_image.convert("RGB")
    pixel_values = processor(images=pil_image, return_tensors="pt").pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    return processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

def ocr_handwritten_from_bytes(image_bytes: bytes):
    pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(pil_image)
    detections = reader.readtext(image_np)

    lines = []

    for box, _, _ in detections:
        x_coords = [p[0] for p in box]
        y_coords = [p[1] for p in box]

        crop = pil_image.crop((
            int(min(x_coords)),
            int(min(y_coords)),
            int(max(x_coords)),
            int(max(y_coords))
        ))

        text = recognize_line(crop)
        if text.strip():
            lines.append(text)

    return lines
