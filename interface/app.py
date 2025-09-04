import streamlit as st
import pandas as pd
from io import BytesIO


# Função get_field real
def get_field(base_df: pd.DataFrame, ref_df: pd.DataFrame, base_key: str, ref_key: str,
              search_field: str) -> pd.DataFrame:
    """
    Busca valores em ref_df com base em uma chave de base_df e retorna o DataFrame base atualizado
    com uma nova coluna chamada 'resultado' contendo os valores encontrados.
    """
    ref_dict = ref_df.set_index(ref_key)[search_field].to_dict()
    base_df['resultado'] = base_df[base_key].map(ref_dict)
    return base_df


st.title("ContPy - Manipulação de Planilhas")
st.write("""
    Bem vindo ao *contabilipy*
    Um sistema de programadores, para contadores!
""")

st.write("Faça upload das planilhas para usar a função `get_field`")

# Upload dos arquivos
base_file = st.file_uploader("Upload da planilha base (Excel/CSV)", type=["xlsx", "csv"])
ref_file = st.file_uploader("Upload da planilha de referência (Excel/CSV)", type=["xlsx", "csv"])

if base_file and ref_file:
    # Detecta extensão e lê o arquivo
    if base_file.name.endswith("csv"):
        base_df = pd.read_csv(base_file)
    else:
        base_df = pd.read_excel(base_file)

    if ref_file.name.endswith("csv"):
        ref_df = pd.read_csv(ref_file)
    else:
        ref_df = pd.read_excel(ref_file)

    st.write("Planilha Base")
    st.dataframe(base_df)

    st.write("Planilha de Referência")
    st.dataframe(ref_df)

    # Seleção de colunas
    base_key = st.selectbox("Selecione a coluna chave da base", base_df.columns)
    ref_key = st.selectbox("Selecione a coluna chave da referência", ref_df.columns)
    search_field = st.selectbox("Selecione a coluna que deseja buscar na referência", ref_df.columns)

    if st.button("Executar get_field"):
        result_df = get_field(base_df, ref_df, base_key, ref_key, search_field)
        st.write("Resultado")
        st.dataframe(result_df)

        # Criar arquivo para download
        towrite = BytesIO()
        if base_file.name.endswith("csv"):
            result_df.to_csv(towrite, index=False)
            file_ext = "csv"
        else:
            result_df.to_excel(towrite, index=False, engine='openpyxl')
            file_ext = "xlsx"
        towrite.seek(0)

        st.download_button(
            label="Baixar resultado",
            data=towrite,
            file_name=f"resultado.{file_ext}",
            mime=f"application/{file_ext}"
        )
