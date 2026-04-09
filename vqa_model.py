from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch

# Load model only once (important)
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def get_answer(image_path, question):
    try:
        # Load image
        image = Image.open(image_path).convert('RGB')

        # Prepare inputs
        inputs = processor(image, question, return_tensors="pt")

        # Generate answer
        out = model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)

        return answer

    except Exception as e:
        return "Error processing image"