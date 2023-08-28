# ==================================
# Libraries 
# ==================================
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from utils import modulo_made_in_kitchen as mod

# ==================================
# DataSet
# ==================================
df = pd.read_csv('dataset/zomato_tratado.csv')

# ==================================
# Configurações Página 
# ==================================
st.set_page_config(page_title='Home', page_icon='📈', layout='wide')

# ==================================
# Sidebar
# ==================================
st.sidebar.markdown("""---""")
st.sidebar.markdown('# 🍜 Made in Kitchen')
st.sidebar.markdown("""---""")

# ==================================
# Sidebar > Filtro País
# ==================================
st.sidebar.markdown("## Filtros")

filtro_pais = st.sidebar.multiselect(
    'Escolhas os Países para Vizualização',
    df.loc[:, "country"].unique().tolist(),
    default=['Australia', 'Brazil', 'Canada', 'England', 'Qatar', 'United States of America'])

df_filtro = df[df['country'].isin(filtro_pais)]

st.sidebar.markdown("""---""")

st.sidebar.markdown("### Dados Tratados")

# ==================================
# Sidebar > Download Dados
# ==================================

processed_data = pd.read_csv("dataset/zomato_tratado.csv")

st.sidebar.download_button(
    label="Download",
    data=processed_data.to_csv(index=False, sep=";"),
    file_name="zomato_tratado.csv",
    mime="text/csv",
)

# ==================================
# Head
# ==================================
st.title('📈 Made in Kitchen')

st.header('Análise de Restaurantes da Plataforma')

# ==================================
# Containers
# ==================================
with st.container():
    st.subheader('Dados da Plataforma:')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1: 
        st.metric(
            label=f'Total de Restaurantes',
            value=df_filtro.shape[0])
    
    with col2: 
        st.metric(
            label='Total de Países',
            value=df_filtro['country'].nunique())

    with col3: 
        st.metric(
            label='Total de Cidades',
            value=df_filtro['city'].nunique())


    with col4: 
        st.metric(
            label='Total de Avaliações',
            value=f"{df_filtro['votes'].sum():,}".replace(",", "."))

    with col5: 
        st.metric(
            label='Total Tipos de Culinárias',
            value=df_filtro['cuisines'].nunique())

with st.container():
    # Chamando a função e passando DataFrame como argumento
    map = mod.create_map(df_filtro)
    folium_static(map, height=500, width=1024)
    