#teste de criacao de aplicacao web em python 

import numpy as np
import pandas as pd 
import seaborn as sns
import streamlit as st 
import matplotlib.pyplot as plt
 
# Importando a base de dados a ser analisada 
df = df = pd.read_excel('/Users/linomartins/Downloads/BaseDados ATUALIZADA.xlsx', sheet_name=1)
df.drop(['Unnamed: 0'], axis =1, inplace = True)
df.dropna(how = 'all', inplace = True)
colunas = df.columns
fundacao = df.Fundação.unique().tolist()
quantidade_fundacao = df.groupby(['Fundação']).Fundação.count().sort_values()

# Função que mostra a quantidade de linhas 
def mostra_qntd_linhas(df):
    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela',min_value = 1, max_value = len(df), step =1)
    st.write(df.head(qntd_linhas).style.format(subset = ['Valor'], formatter = "{:.2f}"))


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

st.title('Análise Exploratória de Dados - Carbyne Investimentos')
st.write('Análise de dados referentes aos fundos de pensão presentes na base consolidada')

st.sidebar.title('Menu')
paginaselecionada = st.sidebar.selectbox('Selecione a base que deseja ter informações',['Fundos de Pensão','Base 1', 'Base 2'])
mostrar_tabela = st.sidebar.checkbox('Mostrar Tabela')

if mostrar_tabela:

        #Configuracoes do filtro da aplicacao 
        st.sidebar.markdown('Filtro para a tabela')
        #Filtro coluna fundacao 
        fundacoes = list(df['Fundação'].unique())
        fundacoes.append('Fundação Banrisul')

        fundacao = st.sidebar.selectbox('Selecione a Fundação', options = fundacoes)

        #Filtro coluna gestor 
        st.sidebar.markdown('Filtro por Gestor')
        gestores = list(df['Gestor'].unique())
        gestores.append('Absolute')

        gestor = st.sidebar.selectbox('Selecione o Gestor', options = gestores)

        if fundacao != 'Fundação Banrisul':
            df_fundacao = df.query('Fundação == @fundacao')
            mostra_qntd_linhas(df_fundacao)
        else:
            mostra_qntd_linhas(df)
        
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




