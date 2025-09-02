import os
from pathlib import Path

def list_archive_files(directory: str = "./docs"):
    """Lista arquivos de uma pasta"""
    docs_path = Path(directory)
    return list(docs_path.glob("*"))

def import_document(choice: int = None, directory: str = "./docs"):
    """Selecionar um arquivo e importar"""
    archives = list_archive_files(directory)
    if not archives:
        print("Nenhum documento encontrado")
        return None

    print("Documentos disponíveis:")
    for i, archive in enumerate(archives):
        print(f"{i + 1}. {archive.name}")

    if choice is None:
        choice = int(input("Escolha o número do arquivo para importar: ")) - 1
    else:
        choice = choice - 1  # compatibilidade com input

    if choice < 0 or choice >= len(archives):
        print("Documento inválido")
        return None

    return str(archives[choice])

def export_document(content: str, doc_file: str, save_dir: str = "./saved_files"):
    """Salva o conteúdo em disco"""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Criando diretório {save_dir}...")

    file_path = os.path.join(save_dir, doc_file)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Arquivo salvo: {file_path}")
    return file_path
