from models.document import Document

class PassportDocument(Document):

    def get_document_type(self):
        return "passport"

    def get_required_fields(self):
        return [
            "passport_number",
            "name",
            "nationality",
            "date_of_birth",
            "expiry_date"
        ]