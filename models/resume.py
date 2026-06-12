from models.document import Document

class ResumeDocument(Document):

    def get_document_type(self):
        return "resume"

    def get_required_fields(self):
        return [
            "name",
            "email",
            "phone",
            "skills",
            "education"
        ]