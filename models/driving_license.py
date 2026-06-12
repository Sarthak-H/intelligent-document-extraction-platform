from models.document import Document

class DrivingLicenseDocument(Document):

    def get_document_type(self):
        return "driving_license"

    def get_required_fields(self):
        return [
            "license_number",
            "name",
            "date_of_birth",
            "issue_date",
            "expiry_date"
        ]