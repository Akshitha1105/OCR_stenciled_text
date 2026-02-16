import os
import easyocr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

print("Downloading EasyOCR model...")
reader = easyocr.Reader(['en'])
print("EasyOCR downloaded.")

print("Downloading TrOCR model...")
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")

os.makedirs("trocr_model", exist_ok=True)

processor.save_pretrained("trocr_model")
model.save_pretrained("trocr_model")

print("TrOCR saved locally in ./trocr_model")
print("All models downloaded successfully ✅")