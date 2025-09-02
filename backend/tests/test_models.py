import pytest
from backend.models.Document import Document

class TestModels:

    def test_list_files(self, tmp_path):
        # cria arquivos temporários
        file1 = tmp_path / "doc1.txt"
        file1.write_text("teste")
        file2 = tmp_path / "doc2.txt"
        file2.write_text("teste2")

        # sobrescreve a pasta docs temporária
        Document.list_archive_files = classmethod(lambda cls: list(tmp_path.glob("*")))

        documents = Document.list_archive_files()
        assert len(documents) == 2

    def test_choice_file(self, tmp_path):
        file1 = tmp_path / "doc1.txt"
        file1.write_text("teste")
        Document.list_archive_files = classmethod(lambda cls: list(tmp_path.glob("*")))

        doc = Document.import_document(choice=1)
        assert isinstance(doc, Document)
        assert doc.title == "doc1"

    def test_export_document(self):
        saved = Document.export_document(doc_file="teste2.txt")
        assert saved is True