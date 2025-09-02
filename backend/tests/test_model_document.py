import pytest
from backend.models.Document import Document
from backend.services import utils_document
from pathlib import Path

class TestModelDocument:

    @pytest.fixture
    def tmp_docs(self, tmp_path):
        """Cria arquivos temporários para teste"""
        file1 = tmp_path / "doc1.txt"
        file1.write_text("conteúdo 1")
        file2 = tmp_path / "doc2.txt"
        file2.write_text("conteúdo 2")
        return tmp_path

    def test_list_files(self, tmp_docs):
        files = utils_document.list_archive_files(directory=tmp_docs)
        assert len(files) == 2
        assert all(isinstance(f, Path) for f in files)

    def test_import_document_choice(self, tmp_docs):
        # importa primeiro arquivo
        file_path = utils_document.import_document(choice=1, directory=tmp_docs)
        doc = Document(file_path)
        assert isinstance(doc, Document)
        assert doc.title == "doc1"

    def test_export_document(self, tmp_path):
        content = "teste de export"
        file_path = utils_document.export_document(content, "teste_export.txt", save_dir=tmp_path)
        saved_file = tmp_path / "teste_export.txt"
        assert saved_file.exists()
        assert saved_file.read_text() == content
