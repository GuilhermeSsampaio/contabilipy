import os
from os.path import exists
from pathlib import Path
from uuid import uuid4
from datetime import datetime

class Document:
    def __init__(self, file_path: str, actor: str = None):
        self.id = str(uuid4())
        self.file_path = Path(file_path)
        self.title = self.file_path.stem
        self.doc_type = self.file_path.suffix[1:]
        self.actor = actor
        self.active = True
        self.creation_date = datetime.now()

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def __repr__(self):
        return f"<Document id={self.id} title={self.title} doc_type={self.doc_type}>"

