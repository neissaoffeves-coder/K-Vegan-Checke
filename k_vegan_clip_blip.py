#!/usr/bin/env python3
import torch, json
from PIL import Image
from transformers import CLIPModel, CLIPProcessor, Blip2ForConditionalGeneration, Blip2Processor

NON_VEGAN_KEYWORDS = {
    "소고기": "beef", "돼지고기": "pork", "닭고기": "chicken", "고기": "meat",
    "멸치액젓": "anchovy sauce", "새우": "shrimp", "오징어": "squid", "게": "crab",
    "조개": "shellfish", "굴": "oyster", "굴소스": "oyster sauce", "생선": "fish",
    "어류": "fish", "젓갈": "fish sauce", "액젓": "fish sauce", "새우젓": "salted shrimp",
    "우유": "milk", "분유": "powdered milk", "버터": "butter", "치즈": "cheese",
    "계란": "egg", "달걀": "egg", "난황": "egg yolk", "꿀": "honey",
    "젤라틴": "gelatin", "콜라겐": "collagen", "멸치": "anchovy"
}

class KVeganChecker:
    def __init__(self, device=None):
        self.device = device or ("mps" if torch.backends.mps.is_available() else "cpu")
        print(f"🔧 K-Vegan Checker (device: {self.device})")
        print("📥 Loading CLIP...")
        self.clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
        self.clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        print("📥 Loading BLIP-2...")
        self.blip2_model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl", torch_dtype=torch.float16)
        self.blip2_processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
        print("✅ Models loaded!\n")
    
    def check_text(self, ingredient_text):
        print(f"🔍 Text Analysis: {ingredient_text[:50]}...")
        non_vegan_detected = []
        for korean in sorted(NON_VEGAN_KEYWORDS.keys(), key=len, reverse=True):
            if korean in ingredient_text:
                non_vegan_detected.append((korean, NON_VEGAN_KEYWORDS[korean]))
        if non_vegan_detected:
            return {"status": "❌ NOT VEGAN", "cause": f"Contains {non_vegan_detected[0][0]}", "confidence": 0.98}
        return {"status": "✅ VEGAN", "cause": "No animal products", "confidence": 0.95}
    
    def check_image(self, image_path):
        print(f"🖼️ Image Analysis: {image_path}")
        image = Image.open(image_path).convert("RGB")
        print("   Stage 1: CLIP scoring...")
        ingredient_texts = list(NON_VEGAN_KEYWORDS.keys())
        inputs = self.clip_processor(text=ingredient_texts, images=image, return_tensors="pt", padding=True).to(self.device)
        with torch.no_grad():
            outputs = self.clip_model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1).cpu().numpy()[0]
        non_vegan = [(ingredient_texts[i], NON_VEGAN_KEYWORDS[ingredient_texts[i]], probs[i]) for i in range(len(ingredient_texts)) if probs[i] > 0.15]
        print("   Stage 2: BLIP-2...")
        inputs_blip = self.blip2_processor(images=image, text="What ingredients are in this label?", return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.blip2_model.generate(**inputs_blip, max_length=100, num_beams=3)
        blip_text = self.blip2_processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        print(f"   BLIP-2: {blip_text}\n")
        if non_vegan:
            return {"status": "❌ NOT VEGAN", "cause": f"Detected: {non_vegan[0][0]}", "confidence": 0.90, "blip2": blip_text}
        return {"status": "✅ VEGAN", "cause": "No animal products", "confidence": 0.90, "blip2": blip_text}

if __name__ == "__main__":
    import sys
    checker = KVeganChecker()
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "밀가루, 설탕, 소금"
    result = checker.check_text(text) if not text.endswith(('.jpg', '.png')) else checker.check_image(text)
    print(f"\n{result['status']}\nCause: {result['cause']}\n")
