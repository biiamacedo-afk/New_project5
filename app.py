import streamlit as st
import pandas as pd 
import plotly.express as px
#importei as bibliotecas necessárias 

car_data = pd.read_csv('vehicles.csv') #carregando arquivos

st.header('Análise de anúncios de veículos') #nosso cabeçalho 
hist_button= st.button('Criar histograma') #criando o botão

if hist_button: #se o botão for carregado
    st.write('A criar um histograma para o conjunto de dados de anúncio de vendas de carro') #mensagem
    fig= px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

#criando o segundo botão 
scatter_button= st.button('Criar gráfico de disperção')

if scatter_button:
    st.write('A criar um gráfico de dispersão')
    fig= px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)
    