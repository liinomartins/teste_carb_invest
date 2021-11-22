#teste de criacao de aplicacao web em python 

import numpy as np
import pandas as pd 
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
 
# Importando a base de dados a ser analisada 
df = pd.read_excel('BaseDados ATUALIZADA.xlsx', sheet_name=1)
df.drop(['Unnamed: 0'], axis =1, inplace = True)
df.dropna(how = 'all', inplace = True)
colunas = df.columns
fundacao = df.Fundação.unique().tolist()
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

# Função que cria o gráfico
#def plot_fundacao(df, fundacao):

#    dados_plot = df.query('Fundação == @fundacao')

#    fig, ax = plt.subplots(figsize=(8,6))
#    ax = sns.barplot(x = 'Fundação', y = quantidade_fundacao, data = dados_plot)
#    ax.set_title(f'Quantidade em estoque dos produtos de {fundacao}', fontsize = 16)
#    ax.set_xlabel('Fundação', fontsize = 12)
#    ax.tick_params(rotation = 20, axis = 'x')
#    ax.set_ylabel('Porte', fontsize = 12)
  
#    return fig
if paginaselecionada == 'Fundos de Pensão':

    #Configuracoes página 1 - Fundos de Pensão
    st.title('Análise Exploratória de Dados')
    st.title('- Carbyne Investimentos')
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

    mostrar_tabela = st.checkbox('Mostrar Tabela')
    if mostrar_tabela:

            #Configuracoes do filtro da aplicacao 
            st.markdown('Filtro para a tabela')
            #Filtro coluna fundacao 
            fundacoes = list(df['Fundação'].unique())
            fundacoes.append('Fundação Banrisul')

            fundacao = st.selectbox('Selecione a Fundação', options = fundacoes)

            #Filtro coluna gestor 
            #st.markdown('Filtro por Gestor')
            #gestores = list(df['Gestor'].unique())
            #gestores.append('Absolute')

            #gestor = st.selectbox('Selecione o Gestor', options = gestores)

            if fundacao != 'Fundação Banrisul':
                df_fundacao = df.query('Fundação == @fundacao')
                mostra_qntd_linhas(df_fundacao)
            else:
                mostra_qntd_linhas(df)
     
    #Configuração do Gráfico de quantitativo de fundações 
    st.title('Visualização Gráfica')
    quantidade_fundacao = df.groupby(['Fundação']).Fundação.count().sort_values()
    fundacoes = df['Fundação'].unique()
    fig = px.bar(x = quantidade_fundacao,
                y = fundacoes,
                orientation='h', title="Quantitativo de Fundações",
                labels={'x':'Quantidade','y':'Fundação'})
    st.plotly_chart(fig)

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

        


#if paginaselecionada == 'Fundos de Pensão':
#    st.write('Fundos de Pensão - Consolidado')
#    st.write('Análise de dados referentes aos fundos de pensão presentes na base consolidada')
#    st.selectbox('Selecione a Fundação', [fundacao])
#elif paginaselecionada == 'Base 1':
#    st.title('Análise de Dados - Base 1')
#    x = st.slider('x') #slider interativo, bom para data science 
#    str.write(x,'squared is', x * x)
#elif paginaselecionada == 'Base2':
#    st.title('Análise de Dados - Base 2')




