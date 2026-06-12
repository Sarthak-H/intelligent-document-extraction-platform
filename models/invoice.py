from models.document import Document

class InvoiceDocument(Document):

    def get_document_type(self):
        return "invoice"

    def get_required_fields(self):
        return [
            "invoice_number",
            "invoice_date",
            "vendor_name",
            "total_amount"
        ]