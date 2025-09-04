import pandas as pd

def get_field(
    base_df: pd.DataFrame,
    ref_df: pd.DataFrame,
    base_key: str,
    ref_key: str,
    search_field: str
) -> pd.DataFrame:
    """
    Faz um 'join' para buscar campo de outra tabela.

    Args:
        base_df (pd.DataFrame): DataFrame principal.
        ref_df (pd.DataFrame): DataFrame de referência.
        base_key (str): Coluna no base_df usada como chave.
        ref_key (str): Coluna no ref_df que corresponde à chave.
        search_field (str): Coluna do ref_df que será buscada.

    Returns:
        pd.DataFrame: DataFrame resultante do merge.
    """
    return base_df.merge(
        ref_df[[ref_key, search_field]],
        left_on=base_key,
        right_on=ref_key,
        how="left"
    )

# contpy_sheets.py

def read_sheet(file_path):
    """
    Lê uma planilha do caminho fornecido.
    Suporta formatos .xls, .xlsx e .csv.
    """
    return None


def extract_columns(df, columns_list):
    """
    Extrai colunas específicas de um DataFrame.
    """
    return None


def filter_rows(df, condition_dict):
    """
    Filtra linhas com base em condições fornecidas em um dicionário.
    Exemplo: {"Cliente": "ABC Corp", "Mês": "2025-09"}
    """
    return None


def validate_required_fields(df, required_fields):
    """
    Verifica se todos os campos obrigatórios existem e não estão vazios.
    """
    return None


def detect_duplicates(df, key_columns):
    """
    Identifica registros duplicados com base em colunas-chave.
    """
    return None


def sum_by_category(df, category_column, value_column):
    """
    Agrega valores por uma coluna de categoria.
    """
    return None


def compare_sheets(df1, df2, key_columns, value_columns):
    """
    Compara duas planilhas e detecta discrepâncias nos valores.
    """
    return None


def merge_sheets(df_base, df_ref, base_key, ref_key, fields_to_merge):
    """
    Mescla dados de dois DataFrames com base em chaves comuns.
    """
    return None


def calculate_field(df, new_field_name, formula):
    """
    Cria um novo campo calculado com base em uma fórmula.
    """
    return None


def clean_data(df, cleaning_rules):
    """
    Normaliza e limpa os dados com base nas regras fornecidas.
    """
    return None


def detect_empty_cells(df):
    """
    Detecta células vazias ou inválidas no DataFrame.
    """
    return None


def log_changes(df, change_type, description):
    """
    Registra alterações ou validações para fins de auditoria.
    """
    return None


def sort_rows(df, sort_columns, ascending=True):
    """
    Ordena as linhas pelas colunas especificadas.
    """
    return None


def group_and_aggregate(df, group_columns, agg_dict):
    """
    Agrupa os dados por colunas e aplica funções de agregação.
    """
    return None


def generate_chart(df, chart_type, x_column, y_column):
    """
    Gera um gráfico simples a partir dos dados do DataFrame.
    """
    return None


def export_to_excel(df, output_path):
    """
    Exporta o DataFrame para um arquivo Excel (.xlsx).
    """
    return None


def export_to_pdf(df, output_path, template=None):
    """
    Exporta o DataFrame para um relatório em PDF.
    """
    return None


def schedule_report(df, interval, recipients):
    """
    Agenda a geração e envio automático de relatórios.
    """
    return None


def convert_format(df, target_format):
    """
    Converte o DataFrame para um formato de arquivo diferente
    (.xls, .xlsx, .csv, .json).
    """
    return None


def highlight_inconsistencies(df, rules):
    """
    Destaca inconsistências ou valores fora do padrão no DataFrame.
    """
    return None
