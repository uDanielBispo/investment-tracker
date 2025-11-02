import pandas as pd
import streamlit as st 
import plotly.express as px
import datetime

from datetime import date, timedelta 


df_movimentacoes = pd.read_parquet('./data/analytics/movimentacoes.parquet')

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Analisador de Investimentos",
)
st.write("# 📊 Movimentações")

#===================================== Cabeçalho e filtros =====================================#
col1, col2, col3 = st.columns(3)

start = datetime.date(2023, 1, 1)
end = datetime.date.today()

opcao = col1.selectbox(
    "Período:",
    ["Todo o período", "Últimos 7 dias", "Últimos 30 dias", "Este ano", "Há dois anos"],
)

hoje = date.today()

if opcao == "Últimos 7 dias":
    start_date, end_date = hoje - timedelta(days=7), hoje
elif opcao == "Últimos 30 dias":
    start_date, end_date = hoje - timedelta(days=30), hoje
elif opcao == "Este ano":
    start_date, end_date = date(hoje.year, 1, 1), hoje
elif opcao == "Há dois anos":
    start_date, end_date = date(hoje.year-1, 1, 1), hoje
else:
    start_date, end_date = df_movimentacoes['Data'].min().date(), df_movimentacoes['Data'].max().date()


mask = (df_movimentacoes['Data'] >= pd.to_datetime(start_date)) & (df_movimentacoes['Data'] <= pd.to_datetime(end_date))
df_movimentacoes = df_movimentacoes.loc[mask]
df_movimentacoes = df_movimentacoes.sort_values(by='Data')    



# filtro por tipo
tipos = df_movimentacoes['Tipo'].unique().tolist()

opcao_tipo = col2.multiselect(
    "Tipos de Investimentos:", 
    tipos
)

if opcao_tipo:
    df_movimentacoes = df_movimentacoes[df_movimentacoes['Tipo'].isin(opcao_tipo)]


produtos = df_movimentacoes['Produto'].unique().tolist()

opcao_produto = col3.multiselect(
    "Tipos de Investimentos:", 
    produtos
)

if opcao_produto:
    df_movimentacoes = df_movimentacoes[df_movimentacoes['Produto'].isin(opcao_produto)]

#===================================== Cabeçalho e filtros =====================================#

#===================================== Métricas =====================================#

col1, col2, col3 = st.columns(3)
col1.metric(label='Total Investido (R$)', value=f"{df_movimentacoes['Valor da Operação'].sum():,.2f}")
col2.metric(label='Número de Operações', value=f"{df_movimentacoes.shape[0]}")
col3.metric(label='Produtos Diferentes', value=f"{df_movimentacoes['Produto'].nunique()}")

#===================================== Métricas =====================================#

df_movi_cred = df_movimentacoes[df_movimentacoes['Entrada/Saída'] == 'Credito']
df_movi_deb = df_movimentacoes[df_movimentacoes['Entrada/Saída'] == 'Debito']

fig1 = px.line(
    df_movi_cred,
    x="Data",
    y="Valor da Operação",
    color="Produto" if opcao_produto else "Tipo",
    title="Compras de Investimentos",
    text='Valor da Operação',
    hover_data={
        "Produto": True,
        "Quantidade": True,
        "Valor da Operação": ":,.2f"
    }
)
# Layout
fig1.update_layout(
    xaxis_title="Data",
    yaxis_title="Valor da Operação (R$)",
    hovermode="x unified",
    legend_title="Produto" if opcao_produto else "Tipo",
    margin=dict(l=20, r=20, t=40, b=60)
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(
    df_movi_deb,
    x="Data",
    y="Valor da Operação",
    color="Produto" if opcao_produto else "Tipo",
    title="Vendas de Investimentos",
    text='Valor da Operação',
    hover_data={
        "Produto": True,
        "Quantidade": True,
        "Valor da Operação": ":,.2f"
    }
)
# Layout
fig2.update_layout(
    xaxis_title="Data",
    yaxis_title="Valor da Operação (R$)",
    hovermode="x unified",
    legend_title="Produto" if opcao_produto else "Tipo",
    margin=dict(l=20, r=20, t=40, b=60)
)


st.plotly_chart(fig2, use_container_width=True, key="fig2")