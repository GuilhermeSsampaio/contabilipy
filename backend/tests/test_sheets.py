# # tests/test_utils_sheets.py
# import pandas as pd
# from pathlib import Path
# from backend.services.utils_sheets import get_field
#
# def test_get_field_and_save(tmp_path):
#     # --- Dados fictícios ---
#     base_df = pd.DataFrame({
#         "id": [1, 2, 3],
#         "nome": ["Ana", "Bruno", "Carla"]
#     })
#
#     ref_df = pd.DataFrame({
#         "id_cooperador": [1, 2, 3],
#         "agencia": ["1234", "5678", "4321"]
#     })
#
#     # --- Executa função ---
#     result = get_field(
#         base_df=base_df,
#         ref_df=ref_df,
#         base_key="id",
#         ref_key="id_cooperador",
#         search_field="agencia"
#     )
#
#     # --- Salva em /planilhas ---
#     output_dir = Path("planilhas")
#     output_dir.mkdir(exist_ok=True)
#     output_file = output_dir / "resultado.xlsx"
#
#     result.to_excel(output_file, index=False)
#
#     # --- Validações ---
#     assert output_file.exists()
#     df_loaded = pd.read_excel(output_file)
#     assert "agencia" in df_loaded.columns
#     assert df_loaded.loc[0, "agencia"] == "1234"


# tests/test_utils_sheets.py
import pandas as pd
from pathlib import Path
from backend.services.utils_sheets import get_field

def test_get_field_from_excels():
    # --- Caminhos ---
    base_file = Path("planilhas/cooperadores.xlsx")
    ref_file = Path("planilhas/contas.xlsx")
    output_file = Path("planilhas/resultado.xlsx")

    # --- Carrega arquivos ---
    base_df = pd.read_excel(base_file)
    ref_df = pd.read_excel(ref_file)

    # --- Executa função ---
    result = get_field(
        base_df=base_df,
        ref_df=ref_df,
        base_key="id",
        ref_key="id_cooperador",
        search_field="agencia"
    )

    # --- Salva resultado ---
    result.to_excel(output_file, index=False)

    # --- Validações ---
    assert output_file.exists()
    df_loaded = pd.read_excel(output_file)
    assert "agencia" in df_loaded.columns
    assert len(df_loaded) > 0
