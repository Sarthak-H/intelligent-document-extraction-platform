from abc import ABC, abstractmethod

class Document(ABC):

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def get_document_type(self):
        pass

    @abstractmethod
    def get_required_fields(self):
        pass