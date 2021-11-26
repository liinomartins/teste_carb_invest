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
paginaselecionada = st.sidebar.selectbox('Selecione a base que deseja ter informações',['Fundos de Pensão','Cadastro de Fundo', 'Base 2'])
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
    st.markdown('Filtro para a tabela e gráficos')

    #Filtro coluna fundacao 
    fundacoes = list(df['Fundação'].unique())
    fundacoes.append('Todas')
    fundacao = st.selectbox('Selecione a Fundação', options = fundacoes)
    #Filtro coluna gestor
    #gestores= list(df['Gestor'].unique()):
    #gestores.append('Todos')
    #gestor = st.selectbox('Selecione um Gestor', options = gestores)

    if fundacao !='Todas':
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
                orientation='h', title="Quantitativo da Fundação: " + fundacao,
                labels={'x':'Quantidade','y':'Fundação'})
    st.plotly_chart(fig)
    
    #Gráfico de setores 
    quantidade_classificacao = df.groupby(['Classificação']).Classificação.count().sort_values()
    classificacao = df['Classificação'].unique()
    fig1 = px.pie(df, values= quantidade_classificacao, names=classificacao, 
                title='Representação da Classificação por Fundo') 
    st.plotly_chart(fig1)

    #Gráfico de box_plot 
    #fundos = list(df['Fundo'].unique())
    #valor = df['Valor']
    box_x = st.selectbox("Variáveis do Blox_plot", options=df.columns, index=df.columns.get_loc("Valor"))
    box_cat = st.selectbox("Variáveis Categóricas", options = df.columns)
    box_fig = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_cat, template="plotly_white", category_orders=fundacoes)
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
    
    #Histograma 
    st.write('  ')
    st.write('Histograma')
    hist_x = st.selectbox('Variáveis do Histograma', options = df.columns, index = df.columns.get_loc('Valor'))
    hist_bins = st.slider(label = 'Histogram bins', min_value = 10, max_value = 50, value = 25, step = 1)
    hist_fig = px.histogram(df, x = hist_x, nbins = hist_bins)
    hist_fig = px.histogram(df, x=hist_x, nbins=hist_bins, title="Histogram of " + hist_x,
                        template="plotly_white")
    st.write(hist_fig)

    #Estatísticas da Base (colunas específicas)
    st.write('  ')
    st.write('Estatísticas das colunas CNPJ, Valor e %AuM')
    st.write(df.describe())

    #download da tabela filtrada
    st.title('Download da Tabela Filtrada')
    def convert_df(df_new):
        return df_new.to_csv().encode('utf-8')
    
    csv = convert_df(df)

    st.download_button(label = 'Download da base filtrada como CSV', data = csv, file_name = 'fundos_de_pensao.csv', mime = 'text/csv')


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


elif paginaselecionada == 'Cadastro de Fundo':     
    st.title('Cadastro de Fundos')
    st.markdown(''' Formulário de Cadastro de novos Fundos no Banco de Dados da Carbyne Investimentos   ''')  
    fundacoes_selecao = list(df['Fundação'].unique())
    gestor_selecao = list(df['Gestor'].unique())
    classificacao_selecao = list(df['Classificação'].unique())
    ja_falado_selecao = list(df['Já Falamos'].unique())
    plano_selecao = list(df['Plano'].unique())

    #Formulário de cadastro de clientes   
    with st.form(key='form'):
        fundacao_form = st.selectbox('Selecione a Fundação', options = fundacoes_selecao)
        gestor_form = st.selectbox('Selecione o Gestor', options = gestor_selecao)
        fundo_form = st.text_input('Insira o nome do Fundo')
        cnpj_form = st.text_input('Insira o CNPJ do Fundo')
        segmento_form = st.selectbox('Selecione o Segmento',['Renda Fixa','Renda Variável', 'Estruturado', 'Imobiliário', 'Exterior','Operações com Participantes'])
        estrategia_form = st.selectbox('Selecione a Estratégia',['Títulos Públicos - Indexados Selic','Títulos Públicos - Indexados Inflação','Títulos Públicos - Indexados Pré-Fixados','Ações de Empresas Brasileiras','Ações de empresas internacionais negociadas na Bolsa local','Participações em empresas de capital fechado',
        'Multimercado','Cotas Representativas de Imóveis','Títulos Públicos - Indexados Taxa Básica de Juros','Ações de empresas internacionais','Participações em empresas de capital fechado','Empréstimos'])
        veiculo_form = st.selectbox('Selecione o Veículo',['Ativo', 'Fundo de Investimento','Fundo de Investimento em cotas de fundos de invstimentos','Fundo de Investimentos em Participações','Fundo de Investimentos em Direitos Creditórios','Fundo de Investimentos Imobiliário', 'Fundo de Índice'])
        classificacao_form = st.selectbox('Selecione a Classificação', options = classificacao_selecao)
        valor_form = st.number_input('Insira o Valor do Fundo')
        aum_form = st.number_input('Insira o %AuM')
        ddn= st.date_input('Data da Coleta da Informação')
        #uf = st.selectbox('Selecione o Estado',['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])
        #Configuração do botão de envio
        botao = st.form_submit_button(label = "Cadastrar Fundo")
        if botao:
            st.success('Fundo cadastrado no banco de dados com sucesso')


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
