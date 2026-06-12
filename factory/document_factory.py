from models.aadhaar import AadhaarDocument
from models.passport import PassportDocument
from models.driving_license import DrivingLicenseDocument
from models.invoice import InvoiceDocument
from models.resume import ResumeDocument


class DocumentFactory:

    @staticmethod
    def create_document(doc_type, file_path):

        if doc_type == "aadhaar":
            return AadhaarDocument(file_path)

        elif doc_type == "passport":
            return PassportDocument(file_path)

        elif doc_type == "driving_license":
            return DrivingLicenseDocument(file_path)

        elif doc_type == "invoice":
            return InvoiceDocument(file_path)

        elif doc_type == "resume":
            return ResumeDocument(file_path)

        else:
            raise ValueError("Unsupported document type")