import pandas as pd
from backend.models.Document import Document
from backend.services.utils_sheets import get_field

class Sheet(Document):
    def __init__(self, title: str, description: str, actor: str = None, number_lines: int = 0, df: pd.DataFrame = None):
        """
        Representa uma planilha no ContPy.
        """
        super().__init__(title, description, doc_type="sheet", actor=actor)
        self.number_lines = number_lines
        self.df = df if df is not None else pd.DataFrame()

    def add_line(self, amount_lines: int) -> None:
        """
        Adiciona linhas à contagem total.
        """
        self.number_lines += amount_lines

    def get_field_call(
        self,
        ref_df: pd.DataFrame,
        base_key: str,
        ref_key: str,
        search_field: str
    ) -> pd.DataFrame:
        """
        Faz a chamada ao utilitário para buscar um campo de outra tabela
        e atualiza o dataframe interno.
        """
        self.df = get_field(self.df, ref_df, base_key, ref_key, search_field)
        return self.df
