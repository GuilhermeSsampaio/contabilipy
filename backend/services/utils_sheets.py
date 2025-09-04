import pandas as pd

def get_field(
    base_df: pd.DataFrame,     # DataFrame principal (onde quero adicionar os dados)
    ref_df: pd.DataFrame,      # DataFrame de referência (onde está o campo buscado)
    base_key: str,             # Nome da coluna-chave no base_df
    ref_key: str,              # Nome da coluna-chave correspondente no ref_df
    search_field: str          # Nome da coluna que será trazida do ref_df
) -> pd.DataFrame:             # Retorna sempre um DataFrame atualizado
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
