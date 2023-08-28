# ==================================
# Libraries 
# ==================================
import pandas as pd
import plotly.express as px
import streamlit as st
from utils import modulo_made_in_kitchen as mod

# ==================================
# DataSet
# ==================================
df = pd.read_csv('dataset/zomato_tratado.csv')

# ==================================
# Configurações Página 
# ==================================
st.set_page_config(page_title='Visão Países', page_icon='🌍', layout='wide')

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

st.sidebar.markdown("""---""")

df_filtro = df[df['country'].isin(filtro_pais)]

st.title('🗺️ Visão Países')

# ==================================
# Containers
# ==================================
with st.container():
    # Quantidade de Restaurantes por País
    fig = mod.quant_rest_por_pais(df_filtro)
    st.plotly_chart( fig, use_container_width=True )
    
with st.container():
    # Quantidade de Cidade por País
    fig = mod.quant_cidade_pais(df_filtro)
    st.plotly_chart( fig, use_container_width=True )
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Quantidade de Restaurantes que Aceitem Reservas por País
        fig = mod.quant_rest_reserva(df_filtro)
        st.plotly_chart( fig, use_container_width=True )
        
    with col2:
        # Preço Médio Prato Para Duas Pesoas por País
        fig = mod.quant_rest_avaliacao(df_filtro)
        st.plotly_chart( fig, use_container_width=True )


