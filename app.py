from flask import Flask, render_template, request
from processors.ocr_processor import OCRProcessor
from processors.llm_processor import LLMProcessor
from database.database_manager import DatabaseManager
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():

    file = request.files["document"]

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(file_path)

    # OCR
    ocr = OCRProcessor()

    text = ocr.extract_text(file_path)

    # Gemini
    fields = [
        "name",
        "aadhaar_number",
        "gender",
        "dob"
    ]

    llm = LLMProcessor()

    result = llm.extract_fields(
        text,
        fields
    )

    clean_result = result.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    data = json.loads(clean_result)

    # Save Database
    db = DatabaseManager()

    db.save_document(
        "aadhaar",
        data
    )

    return render_template(
        "result.html",
        result=data
    )


if __name__ == "__main__":
    app.run(debug=True) 