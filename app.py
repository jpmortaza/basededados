import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Banco colaborativo de bases de dados publicos",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":books:"
)

# Carrega o arquivo CSV
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSeCLKw-9aJ7VBmnAdJAdjT0A69NMxPLlg9viKQn_kUsr_yjr_UlYObLZ2rmoEiGgFNqwELtMWYg7rK/pub?output=csv'
df = pd.read_csv(url)

# Cria os filtros de pesquisa com a coluna Categoria e Categoria Unificada
categorias = df['Categoria'].unique().tolist()
categorias_unificadas = df[' Categoria Unificada'].unique().tolist()

# Adiciona a opção "todas" aos filtros
categorias.insert(0, "Todas")
categorias_unificadas.insert(0, "Todas")

with st.sidebar:
    st.title("Base de Dados")
    filtro_categoria = st.selectbox("Selecione a categoria:", categorias)
    filtro_categoria_unificada = st.selectbox("Selecione a categoria unificada:", categorias_unificadas)

# Cria o campo de pesquisa em todas as colunas
search_term = st.text_input("Pesquisar base de dados:")

# Seleciona as colunas que possuem valores do tipo string
string_columns = df.select_dtypes(include=["object"]).columns

# Filtra os dados de acordo com os filtros selecionados
if filtro_categoria != "Todas":
    df = df[df['Categoria'] == filtro_categoria]

if filtro_categoria_unificada != "Todas":
    df = df[df[' Categoria Unificada'] == filtro_categoria_unificada]

if search_term:
    df = df[df[string_columns].apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)]

# Exibe a tabela com a coluna de links clicáveis
st.experimental_data_editor(df,num_rows="dynamic")

st.caption("""
           Esta ferramenta de pesquisa foi criada com base na planilha colaborativa mantida pela Associação Brasileira de Jornalismo Investigativo (ABRAJI), com mais de 250 bases de dados abertos provenientes de diversas fontes nacionais e internacionais. A curadoria da planilha é feita por Tiago Mali, especialista em jornalismo de dados e coordenador de cursos da ABRAJI. Através desta ferramenta, é possível pesquisar e filtrar as bases de dados disponíveis de acordo com categorias e termos de busca específicos, facilitando o acesso a informações relevantes para análises e investigações jornalísticas.
           """)
st.caption("Acesse o site da ABRAJI [www.abraji.org.br](https://www.abraji.org.br/help-desk/banco-colaborativo-de-bases-de-dados-publicos)")

st.caption("Ferramenta desenvolvida por Jean Mortaza [www.jeanmortaza.com.br](https://jeanmortaza.com.br)")
