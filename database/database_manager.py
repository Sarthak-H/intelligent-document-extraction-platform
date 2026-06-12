import sqlite3
import json

class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "documents.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS extracted_documents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_type TEXT,
            extracted_data TEXT
        )
        """)

        self.connection.commit()

    def save_document(
        self,
        document_type,
        data
    ):

        self.cursor.execute(
            """
            INSERT INTO extracted_documents
            (
                document_type,
                extracted_data
            )
            VALUES (?,?)
            """,
            (
                document_type,
                json.dumps(data)
            )
        )

        self.connection.commit()

    def get_all_documents(self):

        self.cursor.execute(
            "SELECT * FROM extracted_documents"
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()