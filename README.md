# 1. Problema de negócio

O Made in Kitchen é um aplicativo criado e administrado por uma empresa de tecnologia que conecta restaurantes em todas as partes do mundo com os amantes da culinária.

Através desse aplicativo é possível realizar pedidos e recebe-los nos conforto da sua casa de acordo com a possibilidade de entrega do restaurante. Os restaurantes fazem o cadastro dentro da plataforma ddo Made in Kitchen, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Você foi contratado como um Cientista de Dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um os principais KPIs estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes.

A Made in Kitchen possui um modelo de negócio Marketplace que facilita o encontro e negociações de clientes e restaurantes. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:

## Pais

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 2. Premissas assumidas para a análise

1. A extração dos dados é limitada; apenas os 100 melhores restaurantes (por cidade) podem ser obtidos.
2. O modelo de negócios adotado foi o Marketplace.
3. As principais perspectivas de negócios são: Visão Países, Visão Cidades, Visão Restaurantes e Visão Culinárias.
4. Os Principais tipos de Culinária são Italian, American, Arabian, Japanese e Home-made.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:

1. Visão do crescimento dos Países em que emprese atende. 
2. Visão do crescimento das Cidades em que emprese atende. 
3. Visão do crescimento dos Tipos de Culinárias em que emprese oferece. 

Cada visão é representada pelo seguinte conjunto de métricas:

1. Visão do crescimento dos Países em que emprese atende. 
    1. Quantidade de restaurantes registrados por País
    2. Quantidade de cidades registradas por País 
    3. Média de avaliações feitas por País
    4. Média de preço de um prata para duas pessoas por País
2. Visão do crescimento das Cidades em que emprese atende. 
    1. Top 10 cidades com restaurantes da base de dados recolhidos. 
    2. Top 10 cidades com restaurantes com média de avaliação de 4 acima.
    3. Top 10 cidades com restaurantes com média de avaliação de 2 abaixo.
    4. Top 10 cidades com mais restaurantes com tipos de culinárias distintos.
3. Visão do crescimento dos Tipos de Culinárias em que emprese oferece. 
    1. Melhores restaurantes dos principais tipos Culinária.
    2. Melhores restaurantes de acordo com as avaliações feitas. 
    3. Melhores tipos culinários.
    4. Piores tipos culinários.

# Top 3 Insights de dados

1. A maior quantidade de restaurantes cadastrados fica na Índia.
2. A quantidade de restaurantes que aceitam reservas por país e a média de preço para duas pessoas é maior na Indonésia.
3. As cidades com mais restaurantes possuem similaridade na quantidade de restaurantes cadastrados.

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://made-in-kitchen-2023.streamlit.app/

# 6. Conclusão

O objetivo deste projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. A partir da Visão Países, observamos que a maior quantidade de restaurantes está na Índia, e o preço médio do prato para duas pessoas é mais alto na Indonésia. A Inglaterra é o país que possui o maior número de restaurantes com tipos de culinárias distintas.

Na Visão Cidades, as cidades com mais restaurantes têm 80 estabelecimentos cadastrados. Londres é a cidade com mais restaurantes avaliados acima da média 4. As piores avaliações dos restaurantes estão localizadas na cidade de Gangtok, na Índia.

Na Visão Cozinha, os melhores restaurantes dos principais tipos culinários são: Darshan (Italian), Burger & Lobster (American), Mandi@36 (Arabian),  Sushi Sambae (Japanese) e  Kanaat Lokantası (Home-made). De acordo com as avaliações, os tipos culinários mais bem avaliados são Others, Ramen e Ottoman, enquanto os piores são Drinks Only, Mineira e Afghan.

# 7. Próximo passos

1. Coletar mais dados.
2. Adicionar novas perspectivas de negócios.
3. Reduzir o número de métricas.
4. Aprimorar as principais visualizações dos dados.
