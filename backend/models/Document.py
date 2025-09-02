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

    @staticmethod
    def list_archive_files(cls):
        """Lista arquivos da pasta docs/ """
        docs_path = Path("./docs")
        return list(docs_path.glob("*"))

    @classmethod
    def import_document(cls, choice: int = None):
        """Selecionar um arquivo e importar"""
        archives = cls.list_archive_files()
        if not archives:
            print("Nenhum documento encontrado")
            return None

        print("Documentos disponíveis:")
        for i, archive in enumerate(archives):
            print(f"{i + 1}. {archive.name}")

        if choice is None:
            choice = int(input("Escolha o número do arquivo para importar: ")) - 1
        else:
            choice = choice - 1  # para compatibilidade com input

        if choice < 0 or choice >= len(archives):
            print("Documento inválido")
            return None

        return cls(str(archives[choice]))

    @staticmethod
    def export_document(cls, doc_file:str = None):
        saved = False
        save_dir = "./saved_files"

        if not exists(save_dir):
            os.makedirs(save_dir)
            print("Criando diretorio...")

        if doc_file is None:
            doc_file = str(input("Digite o nome do arquivo e sua extensão para salvar no disco"))

        file_path = os.path.join(save_dir, doc_file)

        with open(file_path, "w", encoding="utf-8") as saved_file:
                saved_file.write("teste")

        print(f"Arquivo salvo: {file_path}")

        saved = True
        return saved

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def __repr__(self):
        return f"<Document id={self.id} title={self.title} doc_type={self.doc_type}>"

Document.export_document(doc_file="teste.txt")