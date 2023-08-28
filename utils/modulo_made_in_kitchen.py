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


# ==================================
# Maps Home 
# ==================================
def create_map(dataframe):

    """ Esta função tem a responsabilidade de criar um map usando a bíblioteca Folium,
    que retorna um mapa com marcadores de cada restaurante com informações que contém o
    nome do restaurante, custo do prato para duas pessoas, tipo de culinária, a moeda aceita,
    a nota de avaliação e a cor da avaliação. 
    
    Input: DataFrame
    Output: Mapa Com Macações
    """

    # Criando Map
    my_map = folium.Map(max_boounds=True, zoom_start=25, height=500, width=1024)

    # Criando marcadores de agrupamento.
    marker_cluster = MarkerCluster().add_to(my_map)

    # Percorrendo cada linhas do DataFrame para preencher as informações dos marcadores de cada restaurante.
    for _, line in dataframe.iterrows():
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["rating_color"]}'

        html = f"<p><strong>{name}</strong></p>"
        html += f"<p>Preço: {price_for_two},00 ({currency}) for two"
        html += f"<br />Tipo: {cuisine}"
        html += f"<br />Avaliação: {rating}/5.0"

        # Crianção do marcador localização. 
        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        # Marcador com de acordo com cores da avaliação.
        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    return my_map

# ==================================
# Visão Países 
# ==================================

def quant_rest_por_pais(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'country'
    e realiza a contagem dos restaurante e ordenar em ordem decrescente

        Em seguida gera um gráfico de barras interativo com dataframe selecionado. 
    
    Input: DataFrame
    Output: Gráfico de Barras"""

    # Quantidade de Restaurantes por País.
    grouped = (dataframe.loc[:, ['country', 'restaurant_id']]
            .groupby(['country'])
            .count()
            .reset_index()
            .sort_values(['restaurant_id'], ascending=False))
    #renomeando colunas
    grouped = grouped.rename(columns={'country': 'Pais', 'restaurant_id': 'Quant_Restaurantes'})
    
    # plotando gráfico do país que possui mais restaurantes registados

    fig = px.bar(
        grouped, 
        x='Pais', 
        y='Quant_Restaurantes',
        title='Quantidade de restaurantes por País',
        labels={'Pais': 'País', 'Quant_Restaurantes': 'Quantidade de Restaurantes'})

    # adicionando valores em cima da barra
    fig.update_traces(text=grouped['Quant_Restaurantes'], textposition='auto')

    return fig

def quant_cidade_pais(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'country'
    e 'city' realizando a contagem das cidades, depois ordenar em ordem decrescente.

        Em seguida gera um gráfico de barras interativo.
    
    Input: DataFrame
    Output: Gráfico de Barras"""

    # País que possui mais cidade registradas.  
    grouped = (dataframe.loc[:,['country', 'city']]
               .groupby(['country'])
               .nunique()
               .reset_index()
               .sort_values('city', ascending=False))
    #renomeando colunas
    grouped = grouped.rename(columns={'country': 'Pais', 'city': 'Quant_Cidades'})


    # plotando o gráfico
    fig = px.bar(
        grouped, 
        x='Pais', 
        y='Quant_Cidades',
        title='Quantidade de cidades por País',
        labels={'Pais': 'País', 'Quant_Cidades': 'Quantidade de Cidades'})

    # adicionando valores em cima da barra
    fig.update_traces(text=grouped['Quant_Cidades'], textposition='auto')

    return fig

def quant_rest_reserva(dataframe):
    
    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'country' e 'votes'
    realizando a contagem dos restaurantes que aceitam reservas, depois organiza em ordem 
    decrescente.

        Em seguida gera um gráfico de barras interativo com dataframe selecionado. 

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Pais que possuir a maior média de avaliação
    grouped = (dataframe[['country', 'votes']]
                .groupby(['country'])
                .mean()
                .round(2)
                .reset_index()
                .sort_values('votes', ascending=False))

    # renomeando colunas
    grouped = grouped.rename(columns={'country': 'Pais', 'votes': 'avalicao_media'})

    # plot gráfico
    fig = px.bar(
        grouped, 
        x='Pais', 
        y='avalicao_media',
        title='Quantidade de Restaurantes que Aceitem Reservas por País',
        labels={'Pais': 'País', 'avalicao_media': 'Quantidade Avaliação'})

    # adicionando valores em cima da barra
    fig.update_traces(text=grouped['avalicao_media'], textposition='auto')

    return fig

def quant_rest_avaliacao(dataframe):
    
    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'country'
    e realiza a contagem dos restaurantes que aceitam reservas, depois organiza em ordem 
    decrescente e apresenta um gráfico de barra com a quantidade restaurentes que aceitam
    reservas agrupados pelos países. 
        
        Em seguida gera um gráfico de barras interativo.

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Pais que possuir a maior média a menor nota média de avaliação
    grouped = (dataframe[['country', 'average_cost_for_two']]
                .groupby(['country'])
                .mean()
                .round(2)
                .reset_index()
                .sort_values('average_cost_for_two', ascending=False))

    # renomeando colunas
    grouped = grouped.rename(columns={'country': 'Pais', 'average_cost_for_two': 'media_preco_duas_pessoa'})
    # plot gráfico dos países que possui na média menor quantidade de avaliações média

    fig = px.bar(
        grouped, 
        x='Pais', 
        y='media_preco_duas_pessoa',
        title='Preço Médio Prato Para Duas Pesoas por País',
        labels={'Pais': 'País', 'media_preco_duas_pessoa': 'Preço'})

    # adicionando valores em cima da barra
    fig.update_traces(text=grouped['media_preco_duas_pessoa'], textposition='auto')

    return fig

# ==================================
# Visão Cidadades 
# ==================================

def top_cidades_resturantes(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'city', 'country' e 
    'restaurant_id', em seguida realiza a contagem dos restaurantes por cidade.
        
        Depois é gerado um gráfico de barras interativo que usar a culuna 'country',
    para mudar a cor da barra.

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Cidade que possui mais restaurantes
    grouped = (dataframe[['restaurant_id', 'city', 'country']]
           .groupby(['country', 'city'])
           .count()
           .sort_values(['restaurant_id', 'city'], ascending=[False, True])
           .reset_index())

    # renomeando colunas
    grouped = grouped.rename(columns={'restaurant_id': 'quantidade_rest'})
    
    grouped = grouped[:10]
    
    #plotando grafico cidades com mais restaurantes
    fig = px.bar(
        grouped,
        x="city",
        y="quantidade_rest",
        text="quantidade_rest",
        text_auto=".2",
        color="country",
        title="Top 10 Cidades com mais Restaurantes",
        labels={"city": "Cidade",
                "restaurant_id": "Quantidade de Restaurantes",
                "country": "País"})

    return fig

def avaliacoes_restaurante_cidade_acima_quatro(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'city', 'country',
    'restaurant_id' e 'aggregate_rating', em seguida realiza a contagem da quantidade
    de avaliações acima de 4 por cidade e país. 
        
        Depois é gerado um gráfico de barras interativo que exibe a contagem realizada, também
    a culuna 'country', é usada para mudar a cor da barra do gráfico.

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Cidades que possui mais restaurantes com nota média acima 4.
    grouped = (dataframe.loc[dataframe['aggregate_rating'] >= 4, ['restaurant_id', 'country', 'city']]
                .groupby(['country', 'city'])
                .count()
                .sort_values(['restaurant_id', 'city'], ascending=[False, True])
                .reset_index())

    # renomeando colunas
    grouped = grouped.rename(columns={'restaurant_id': 'nota_media'})

    grouped = grouped[:10]
    
    # plotando grafico cidades com mais restaurantes
    fig = px.bar(
        grouped,
        x="city",
        y="nota_media",
        text="nota_media",
        text_auto=".2",
        color="country",
        title=f"Top 10 Cidades com Restaurantes Acima da Média de 4",
        labels={"city": "Cidade",
                "nota_media": "Qtd de Restaurantes",
                "country": "País",})

    return fig

def avaliacoes_restaurante_cidade_abaixo_dois(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'city', 'country',
    'restaurant_id' e 'aggregate_rating', em seguida realiza a contagem da quantidade
    de avaliações abaixo de 2 por cidade e país. 
        
        Depois é gerado um gráfico de barras interativo que exibe a contagem realizada, também
    a culuna 'country', é usada para mudar a cor da barra do gráfico.

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Cidades que possui mais restaurantes com nota média abaixo 2.
    grouped = (dataframe.loc[dataframe['aggregate_rating'] <= 2, ['restaurant_id', 'country', 'city']]
                .groupby(['country', 'city'])
                .count()
                .sort_values(['restaurant_id', 'city'], ascending=[False, True])
                .reset_index())

    # renomeando colunas
    grouped = grouped.rename(columns={'restaurant_id': 'nota_media'})

    grouped = grouped[:10]
    
    # plotando grafico cidades com mais restaurantes
    fig = px.bar(
        grouped,
        x="city",
        y="nota_media",
        text="nota_media",
        text_auto=".2",
        color="country",
        title=f"Top 10 Cidades com Restaurantes Acima da Média de 2",
        labels={"city": "Cidade",
                "nota_media": "Qtd de Restaurantes",
                "country": "País",})

    return fig

def top_cidade_restaurantes_culinaria(dataframe):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'city', 'cuisines e'country',
    em seguida realiza a contagem da quantidade de restaurantes agrupados pelos tipos de culinária 
    distintos e por cidade.
        
        Depois é gerado um gráfico de barras interativo que exibe a contagem realizada, também
    a culuna 'country', é usada para mudar a cor da barra do gráfico.

    Input: DataFrame
    Output: Gráfico de Barras"""

    # Quantidade de tipos de culinária por cidade
    grouped = (dataframe[['city', 'cuisines', 'country']]
        .groupby(['country', 'city'])
        .nunique()
        .sort_values('cuisines', ascending=False)
        .reset_index())

    # renomeando colunas
    grouped = grouped.rename(columns={'cuisines': 'quant_tipos_culinarios'})

    grouped = grouped[:10]

    # Plot do Gráfico das Cidades que possui mais restaurantes com nota abaixo de 2.5
    fig = px.bar(
        grouped,
        x="city",
        y="quant_tipos_culinarios",
        text="quant_tipos_culinarios",
        text_auto=".2",
        color="country",
        title="Top 10 Cidades com mais restaurantes com tipos culinários distintos",
        labels={"city": "Cidade",
                "quant_tipos_culinarios": "Culinaria",
                "country": "País"})
    
    # adicionando valores em cima da barra
    fig.update_traces(text=grouped['quant_tipos_culinarios'], textposition='auto')

    return fig

# ==================================
# Visão Cuzinhas 
# ==================================

def metric_melhores_restaurantes(dataframe, tipo_culinaria):
    
    """ Esta função recebe um dataframe e faz um selação das culunas ['restaurant_id', 'city', 
    'country', 'restaurant_name', 'average_cost_for_two', 'currency', 'aggregate_rating'] somente
    as linhas da coluna 'cuisines' de acordo com tipo de culinária escolhida. Em seguinda faz uma 
    ordenação de culuna 'aggregate_rating' retornando o primeiro indíce.

        Em Seguida usamos a função metric da streamlit para apresenta o as informações que sejamos
    conforme função a baixo.

    Input: DataFrame
    Output: > O melhor restaurante de acordo com tipo de culinária escolhido,
            > Nome do Restaurante
            > Nota do Restaurante
            > País do Restaurante
            > Cidade do Restaurante
            > Valor do Prato para Duas Pessoas. 
    """
    # Maior média de avaliação dos Restaurantes do tipo culinária Italiana
    grouped = (dataframe.loc[dataframe['cuisines'] == tipo_culinaria, ['restaurant_id', 'city', 'country', 'restaurant_name', 'average_cost_for_two', 'currency', 'aggregate_rating']]
           .sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index(drop=True))

    x_culinauria = st.metric(
        label=f'{tipo_culinaria}: {grouped.loc[0, "restaurant_name"]}',
        value=f'{grouped.loc[0, "aggregate_rating"]}/5.0',
        help=f"""
            País: {grouped.loc[0, "country"]}\n
            Cidade: {grouped.loc[0, "city"]}\n
            Média Prato para dois: {grouped.loc[0, "average_cost_for_two"]} ({grouped.loc[0, "currency"]})
            """)
    
    return x_culinauria
    
def top_restaurantes(dataframe, culinaria, filtro_pais, quantidade):

    """ Esta função recebe um dataframe e faz um selação dos melhores restaurantes de acordo
    com os países escolhidos, tipo de culinária, e quantidade escolhida pelo usuário.

        Em Seguida usamos a função metric da streamlit para apresenta o as informações que sejamos
    conforme função a baixo.

    Input:  > DataFrame
            > Lista com Tipo de Culinária 
            > Lista com Países Escolhidos
            > Quantidade de linhas a ser exibido. 
    Output: DataFrame com os tops resutaurantes.
    """

    lines = (dataframe["cuisines"].isin(culinaria)) & (dataframe["country"].isin(filtro_pais))

    cols = ['restaurant_id', 'restaurant_name', 'country', 'city', 
               'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']

    df_top = dataframe.loc[lines, cols].sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
    
    df_top = df_top[:quantidade]

    return df_top

def top_melhor_pior_culinaria(dataframe, quantidade, bool):

    """ Esta função recebe um dataframe e faz um agrupamento pela coluna 'cuisines', e 'aggregate_rating'
    em seguida realiza a media das culuna 'aggregate_rating' agrupados pelo tipo de culinária.

        Depois é gerado um gráfico de barras interativo que exibe o resultado.

    Input:  > DataFrame
            > Quantidade 
            > Tipo Boleano True ou False
    Output: Gráfico de Barras
    """

    # Melhor tipo culinárias de acordo com nota média
    grouped = (dataframe[['cuisines', 'aggregate_rating']]
        .groupby(['cuisines'])  
        .mean()
        .sort_values('aggregate_rating', ascending=bool)
        .reset_index())
    
    #plotando grafico top melhores tipos de culinárias.
    fig = px.bar(
        grouped[:quantidade],
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2",
        # title=f"Top {quantidade} Melhores Tipos de Culinárias",
        labels={"cuisines": "Tipos de Cozinhas",
                "aggregate_rating": "Nota Média"})
    
    return fig