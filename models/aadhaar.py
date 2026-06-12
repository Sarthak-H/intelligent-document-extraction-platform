from models.document import Document

class AadhaarDocument(Document):

    def get_document_type(self):
        return "aadhaar"

    def get_required_fields(self):
        return [
            "name",
            "aadhaar_number",
            "dob",
            "gender"
        ]