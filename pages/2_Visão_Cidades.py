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
st.set_page_config(page_title='Visão Cidades', page_icon='🏙️', layout='wide')

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
    default=['Australia', 'Brazil', 'Canada', 'England', 'Qatar', 'United States of America'])

st.sidebar.markdown("""---""")

df_filtro = df[df['country'].isin(filtro_pais)]

st.title('🏙️ Visão Cidades')

# ==================================
# Containers
# ==================================
with st.container():
    # Top 10 Cidades com mais Restaurantes.
    fig = mod.top_cidades_resturantes(df_filtro)
    st.plotly_chart( fig, use_container_width=True )

    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Top Quantidade de Cidades que possui mais restaurantes com nota média acima de 4
        fig = mod.avaliacoes_restaurante_cidade_acima_quatro(df_filtro)
        st.plotly_chart( fig, use_container_width=True )
    
    with col2:
        # # Top Quantidade de Cidades que possui mais restaurantes com nota média abaixo de 2
        fig = mod.avaliacoes_restaurante_cidade_abaixo_dois(df_filtro)
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    # Top Cidades com mais restaurantes distintos.
    fig = mod.top_cidade_restaurantes_culinaria(df_filtro)
    st.plotly_chart(fig, use_container_width=True)
