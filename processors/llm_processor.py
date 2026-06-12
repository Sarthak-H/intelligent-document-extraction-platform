import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class LLMProcessor:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        print("API Key Found:", api_key is not None)

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def extract_fields(self, text, fields):

        prompt = f"""
Extract the following fields:

{fields}

From this OCR text:

{text}

Return only JSON.
"""

        response = self.model.generate_content(prompt)

        return response.text