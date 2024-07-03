# taskmaster/interfaces/ai_model_interface.py

from typing import Dict

class MockAIModel:
    def generate_text(self, prompt: str) -> str:
        return f"Generated text based on: {prompt[:30]}..."

    def classify_text(self, text: str) -> Dict[str, float]:
        return {"positive": 0.8, "negative": 0.2}

ai_model = MockAIModel()