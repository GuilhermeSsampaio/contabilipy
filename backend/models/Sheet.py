from backend.models.Document import Document

class Sheet(Document):
    def __init__(self, title:str, description: str, doc_type:str, actor: str = None, number_lines: int=0):
        super().__init__(title, description, doc_type="sheet")
        self.number_lines = number_lines

    def add_line(self, amount_lines: int):
        self.number_lines += amount_lines



