#teste de criacao de aplicacao web em python 

import numpy as np
import pandas as pd 
import seaborn as sns
import streamlit as st 
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Importando a base de dados a ser analisada 
df = pd.read_excel('BaseDados ATUALIZADA.xlsx', sheet_name=1)
df.drop(['Unnamed: 0'], axis =1, inplace = True)
df.dropna(how = 'all', inplace = True)
colunas = df.columns
fundacao = df.Fundação.unique().tolist()
df['Fundo'].astype(str)
quantidade_fundacao = df.groupby(['Fundação']).Fundação.count().sort_values()

# Função que mostra a quantidade de linhas 
def mostra_qntd_linhas(df):
    qntd_linhas = st.slider('Selecione a quantidade de linhas que deseja mostrar na tabela',min_value = 1, max_value = len(df), step =1)
    st.write(df.head(qntd_linhas).style.format(subset = ['Valor'], formatter = "{:.2f}"))

# Criacao do sidebar menu
image = ('carbyne.png')
st.sidebar.image(image, use_column_width = True)
st.sidebar.title('Menu')
paginaselecionada = st.sidebar.selectbox('Selecione a base que deseja ter informações',['Fundos de Pensão','Base 1', 'Base 2'])
st.sidebar.write('  ')
st.sidebar.write('Essas informações estão restritas a equipe da Carbyne Investimentos')

# Configurações de cada página do menu 
if paginaselecionada == 'Fundos de Pensão':

    #Configuracoes página 1 - Fundos de Pensão
    st.title('Análise Exploratória de Dados')
    st.markdown("<h1 style='color:#46A1C0;'>Carbyne Investimentos</h1>", unsafe_allow_html=True)
    #st.title('- Carbyne Investimentos')
    st.write('Análise de dados referentes aos fundos de pensão presentes na base consolidada')
    st.markdown('''
    __*Dicionário dos dados*__
    - Fundação: Entidade fechada de previdência complementar
    - Plano: Estratégia de Investimento
    - Fundo: Fundo de Investimento
    - CNPJ Fundo: Cadastro Naciona de Pessoas Jurídicas do Fundo 
    - Gestor: Gestor do Fundo de Investimentos
    - Classificação: Classificação do tipo de Investimento 
            - FIP / FMIEE
            - MM Estruturado
    - Valor: Valor do Investimento no Fundo
    - %AUM: Asset Under Managment (Ativos sob gestão)
    - Data_Base: Data que a informação foi buscada
    - Já Falamos: Notificação de debate
    ''')
    st.write('   ')
#    st.dataframe(df)
    
    #Configuração de botão para mostrar tabela e aparecer filtros 
#    mostrar_tabela = st.checkbox('Mostrar Tabela')
#    if mostrar_tabela:

            #Configuracoes do filtro da aplicacao 
#            st.markdown('Filtro para a tabela')

            #Filtro coluna fundacao 
#            fundacoes = list(df['Fundação'].unique())
#            fundacoes.append('Fundação Banrisul')

#            fundacao = st.selectbox('Selecione a Fundação', options = fundacoes)

            #Filtro coluna gestor 
            #st.markdown('Filtro por Gestor')
            #gestores = list(df['Gestor'].unique())
            #gestores.append('Absolute')

            #gestor = st.selectbox('Selecione o Gestor', options = gestores)

#            if fundacao != 'Fundação Banrisul':
#                df_fundacao = df.query('Fundação == @fundacao')
#                mostra_qntd_linhas(df_fundacao)
#            else:
#                mostra_qntd_linhas(df)

    #Configuracoes do filtro da aplicacao 
    st.markdown('Filtro para a tabela')

    #Filtro coluna fundacao 
    fundacoes = list(df['Fundação'].unique())
    fundacoes.append('Todas')
    fundacao = st.selectbox('Selecione a Fundação', options = fundacoes)
    #Filtro coluna gestor
    #gestores= list(df['Gestor'].unique()):
    #gestores.append('Todos')
    #gestor = st.selectbox('Selecione um Gestor', options = gestores)

    if fundacao != 'Todas':
        df = df.query('Fundação == @fundacao')
        mostra_qntd_linhas(df)
    else:
        mostra_qntd_linhas(df)

    #Filtro coluna gestor
    #gestores= list(df['Gestor'].unique())
    #gestores.append('Todas')
    #gestor = st.selectbox('Selecione um Gestor', options = gestores)
    #if gestor != 'Todas':
    #    df = df.query('Gestor == @gestor')
    #    mostra_qntd_linhas(df)
    #else:
     #   mostra_qntd_linhas(df)

    # Visualização Gráfica
    st.title('Visualização Gráfica')
    quantidade_fundacao = df.groupby(['Fundação']).Fundação.count().sort_values()
    fundacoes = df['Fundação'].unique()

    # Gráfico de Barras Horizontal 
    fig = px.bar(x = quantidade_fundacao,
                y = fundacoes,
                orientation='h', title="Quantitativo de Fundações",
                labels={'x':'Quantidade','y':'Fundação'})
    st.plotly_chart(fig)
    
    #Gráfico de setores 
    quantidade_classificacao = df.groupby(['Classificação']).Classificação.count().sort_values()
    classificacao = df['Classificação'].unique()
    fig1 = px.pie(df, values= quantidade_classificacao, names=classificacao, 
                title='Representação da Classficação por Fundo') 
    st.plotly_chart(fig1)
    
    #Gráfico de box_plot 
    fundo = df['Fundo'].unique()
    box_x = st.selectbox("Variáveis do Blox_plot", options=df.columns, index=df.columns.get_loc("Valor"))
    box_cat = st.selectbox("Variáveis Categóricas", options = df.columns)
    box_fig = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_x, template="plotly_white", category_orders=fundacoes)
    st.write(box_fig)

    #Configurações do wordcloud
    stop_words = ['em','sao','ao','de','da','do','para','c','kg','un','ml',
                  'pct','und','das','no','ou','pc','gr','pt','cm','vd','com',
                  'sem','gfa','jg','la','1','2','3','4','5','6','7','8','9',
                  '0','a','b','c','d','e','lt','f','g','h','i','j','k','l',
                  'm','n','o','p','q','r','s','t','u','v','x','w','y','z']
    st.write('Word Cloud dos Fundos da Base')
    if st.checkbox('Mostrar WordCloud'):
        all_words = ','.join(str(s) for s in df['Fundo'].values)
        # criar uma wordcloud
        wc = WordCloud(stopwords=stop_words, background_color="white", width=1600, height=800)
        wordcloud = wc.generate(all_words)
        # plotar wordcloud
        fig, ax = plt.subplots(figsize=(10,6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_axis_off()
        st.pyplot(fig,ax)

    #Criar uma wordcloud
#    st.write('Word Cloud dos Fundos da Base')
#    wc = WordCloud(stopwords = stop_words, background_color="white", width=1600, height=800)
#    wordcloud = wc.generate(all_words)
#    #Plotar wordcloud
#    fig, ax = plt.subplots(figsize=(10,6))
#    ax.imshow(wordcloud, interpolation='bilinear')
#    ax.set_axis_off()
#    st.pyplot(fig,ax)

    
    # Valores do gráfico de Fundos 
#   quantidade_fundos = df.groupby(['Fundação']).Fundo.count().sort_values()
#  fig1 = px.bar(df, height=600, width=1200)

#    fig1.update_layout(title='Taxa mensal de notificações por 100 mil hab.', 
#                   xaxis_title='Mês',
#                   yaxis_title='Casos/100 mil hab.',
#                   barmode='group')

#    st.plotly_chart(fig1)	



elif paginaselecionada == 'Base 1':     
    st.title('Base 1')
    st.markdown('''
    Página em Construção....
    
    Aguarde... ficará pronta em breve 

    - Carbyne Investimentos
    
    ''')     

elif paginaselecionada == 'Base 2': 
    st.title('Base 2')    
    st.markdown('''
    Página em Construção....
    
    Aguarde... ficará pronta em breve 

    - Carbyne Investimentos
    
    ''')     


# filtro para o gráfico
#st.sidebar.markdown('## Filtro para o gráfico')

#fundacao_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = df['Fundação'].unique())
#figura = plot_fundacao(df, fundacao_grafico)
#st.pyplot(figura)
