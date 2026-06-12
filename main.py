from processors.ocr_processor import OCRProcessor
from processors.llm_processor import LLMProcessor
from database.database_manager import DatabaseManager
import json

# OCR
ocr = OCRProcessor()

text = ocr.extract_text("fake adhar.jpg")

print(text)

# Fields
fields = [
    "name",
    "aadhaar_number",
    "gender",
    "dob"
]

# Gemini
llm = LLMProcessor()

result = llm.extract_fields(
    text,
    fields
)

print(result)

clean_result = result.replace("```json", "").replace("```", "").strip()

data = json.loads(clean_result)

# Database
db = DatabaseManager()

db.save_document(
    "aadhaar",
    data
)

print("Saved Successfully")