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

    # Get document type
    doc_type = request.form["doc_type"]

    # Get uploaded file
    file = request.files["document"]

    # Save file
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(file_path)

    # OCR Processing
    ocr = OCRProcessor()

    text = ocr.extract_text(file_path)

    print("Document Type:", doc_type)
    print("File Path:", file_path)
    print("OCR Text:")
    print(text)

    # Dynamic fields based on document type
    if doc_type == "aadhaar":

        fields = [
            "name",
            "aadhaar_number",
            "gender",
            "dob"
        ]

    elif doc_type == "resume":

        fields = [
            "name",
            "email",
            "phone",
            "skills",
            "education"
        ]

    elif doc_type == "passport":

        fields = [
            "name",
            "passport_number",
            "nationality",
            "dob"
        ]

    elif doc_type == "invoice":

        fields = [
            "invoice_number",
            "date",
            "total_amount",
            "vendor_name"
        ]

    else:

        return "Unsupported Document Type"

    # Gemini Processing
    llm = LLMProcessor()

    result = llm.extract_fields(
        text,
        fields
    )

    print("RAW RESULT:")
    print(result)

    try:

        clean_result = result.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        data = json.loads(clean_result)

    except Exception as e:

        return f"JSON Error: {e}"

    # Save to Database
    db = DatabaseManager()

    db.save_document(
        doc_type,
        data
    )

    # Show Result Page
    return render_template(
        "result.html",
        result=data
    )


if __name__ == "__main__":
    app.run(
        debug=True
    )
