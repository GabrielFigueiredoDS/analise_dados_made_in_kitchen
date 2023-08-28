# ==================================
# Libraries 
# ==================================
import pandas as pd
import streamlit as st
import plotly.express as px
from utils import modulo_made_in_kitchen as mod

# ==================================
# DataSet
# ==================================
df = pd.read_csv('dataset/zomato_tratado.csv')

# ==================================
# Configurações Página 
# ==================================
st.set_page_config(page_title='Visão Cozinhas', page_icon='🍽️', layout='wide')

# ==================================
# Sidebar
# ==================================
st.sidebar.markdown("""---""")
st.sidebar.markdown('# 🍜 Made in Kitchen')
st.sidebar.markdown("""---""")

# ==================================
# Sidebar > Filtro data
# ==================================
st.sidebar.markdown("## Filtros")

filtro_pais = st.sidebar.multiselect(
    'Escolhas os Países para Vizualização',
    df.loc[:, "country"].unique().tolist(),
    default= ['Australia', 'Brazil', 'Canada', 'England', 'Qatar', 'United States of America'])

st.sidebar.markdown("""---""")

quantidade = st.sidebar.slider('Quantidade de Restaurantes', 1, 20, 10)

df_filtro = df[df['country'].isin(filtro_pais)]

st.sidebar.markdown("""---""")

culinaria = st.sidebar.multiselect(
    'Tipos de Culinária',
    df.loc[:, "cuisines"].unique().tolist(),
    default=["Home-made", "BBQ", "Japanese", "Brazilian", 
             "Arabian", "American", "Italian"])

st.title('🍽️ Visão Cozinhas')

# ==================================
# Containers
# ==================================

st.header('Melhores Restaurantes dos Principais tipos Culinários')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        # Maior média de avaliação dos Restaurantes do tipo culinária Italian        
        mod.metric_melhores_restaurantes(df, 'Italian')
        
    with col2:
        # Maior média de avaliação dos Restaurantes do tipo culinária Americana
        mod.metric_melhores_restaurantes(df, 'American')

    with col3:
        # Maior média de avaliação dos Restaurantes do tipo culinária Árabe
        mod.metric_melhores_restaurantes(df, 'Arabian')

    with col4:
        # Maior média de avaliação dos Restaurantes do tipo culinária Japanese
        mod.metric_melhores_restaurantes(df, 'Japanese')
        
    with col5:
        # Maior média de avaliação dos Restaurantes do tipo culinária Árabe
        mod.metric_melhores_restaurantes(df, 'Home-made')


with st.container():
    # Tops Restaurantes 
    st.header(f'Top {quantidade} Restaurantes')    
    top_rest = mod.top_restaurantes(df_filtro, culinaria, filtro_pais, quantidade)
    st.dataframe(top_rest)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Tops Melhores Tipos de Culinárias
        st.subheader(f"Top {quantidade} Melhores Tipos de Culinárias")
        fig = mod.top_melhor_pior_culinaria(df_filtro, quantidade, False)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # Tops Piores Tipos de Culinárias
        st.subheader(f"Top {quantidade} Piores Tipos de Culinárias")
        fig = mod.top_melhor_pior_culinaria(df_filtro, quantidade, True)
        st.plotly_chart(fig, use_container_width=True)

