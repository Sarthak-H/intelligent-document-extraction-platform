import easyocr

class OCRProcessor:

    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path):

        result = self.reader.readtext(image_path)

        text = ""

        for item in result:
            text += item[1] + " "

        return text