import easyocr
import numpy as np
from PIL import Image
import io

reader = easyocr.Reader(['en', 'pl'], gpu=False)

def ocr_printed_from_bytes(image_bytes: bytes):
    pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(pil_image)
    results = reader.readtext(image_np)

    lines = []
    for item in results:
        if len(item) == 3:
            _, text, conf = item
        else:
            _, text = item
        lines.append(text)

    return lines
