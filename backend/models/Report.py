from backend.models.Document import Document


class Report(Document):
    def __init__(self, title:str, description: str, doc_type:str, actor: str = None, paginated: bool = True):
        super().__init__(title, description, doc_type="report", actor=actor)
        self.paginated = paginated

    def toggle_pagination(self):
        self.paginated = not self.paginated
