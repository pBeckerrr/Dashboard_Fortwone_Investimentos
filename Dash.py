import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- CSS Personalizado para aprimoramentos visuais e fonte Open Sans ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');

    body, h1, h2, h3, h4, h5, h6, p, li, a, span {
        font-family: 'Open Sans', sans-serif !important;
        color: white !important; /* Texto branco padrão */
    }

    .reportview-container {
        background-color: #1e1e1e !important; /* Fundo cinza escuro */
    }

    .reportview-container .main .block-container{
        padding-top: 1rem;
        padding-bottom: 2rem;
        padding-left: 5rem; /* Mantendo o padding para alinhar com a sidebar */
    }
    .st-sidebar {
        background-color: #2c2c2c !important; /* Fundo um pouco mais claro para a sidebar */
        color: white !important; /* Texto branco na sidebar */
    }
    .st-metric {
        padding: 1rem;
        border-radius: 5px;
        background-color: #333 !important; /* Fundo mais claro para os métricos */
        color: white !important;
        border: 1px solid #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título principal do Dashboard
st.title("Dashboard Fortwone Investimentos")

# --- Carregamento e tratamento dos dados ---
try:
    df = pd.read_csv("vendas_anuais.csv")
    # Converte a coluna de data para o tipo datetime
    df['Data da Compra'] = pd.to_datetime(df['Data da Compra'])
except FileNotFoundError:
    st.error("Arquivo CSV 'vendas_anuais.csv' não encontrado. Certifique-se de que ele está no mesmo diretório do script.")
    st.stop()
except Exception as e:
    st.error(f"Ocorreu um erro ao ler o CSV: {e}")
    st.stop()

# --- Barra Lateral de Navegação ---
with st.sidebar:
    st.header("Opções de Visualização")
    opcao = st.radio(
        "Selecione a seção:",
        ("Visão Geral", "Vendas Mensais", "Produtos Mais Vendidos", "Distribuição de Idade", "Tráfego Pago")
    )

# --- Conteúdo Principal com base na seleção do menu ---
if opcao == "Visão Geral":
    st.header("Visão Geral")
    st.write("""
    Bem-vindo ao Dashboard de Análise de Vendas da Fortwone Investimentos,
    este Dashboard tem como intuito apresentar nosso relatório anual de vendas,
    destacando o desempenho e identificando oportunidades de melhoria para 2025.
    """)

    # --- Gráfico Resumo de Vendas Mensais ---
    df['Mes'] = df['Data da Compra'].dt.month
    vendas_mensais = df.groupby('Mes')['Faturamento (Valor da Venda)'].sum().reset_index()
    meses_nomes = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    vendas_mensais['Mes_Nome'] = vendas_mensais['Mes'].map(meses_nomes)

    fig_tendencia_mensal = px.line(vendas_mensais, x='Mes_Nome', y='Faturamento (Valor da Venda)',
                                  labels={'Faturamento (Valor da Venda)': 'Faturamento', 'Mes_Nome': 'Mês'},
                                  markers=True,
                                  template="plotly_dark")
    st.plotly_chart(fig_tendencia_mensal)

    st.markdown("---")

    # --- Desempenho Anual (Sem o retângulo) ---
    st.subheader("Desempenho Anual")
    total_faturamento = df['Faturamento (Valor da Venda)'].sum()
    faturamento_formatado = f"R$ {total_faturamento:,.2f}"
    percentual_aumento = 20

    st.markdown(f"""
    <h2 style="color: #ADD8E6; font-size: 2.5em; margin-bottom: 5px;">
        {faturamento_formatado}
        <span style="color: #90EE90; font-size: 0.7em;">&#9650; {percentual_aumento}%</span>
    </h2>
    <p style="font-size: 0.9em; color: #cccccc; margin-top: 0;">Faturamento Total (Comparado ao ano anterior)</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("Créditos: Analista de Dados Paulo Becker")

elif opcao == "Vendas Mensais":
    st.header("Vendas Mensais")
    df['Mes'] = df['Data da Compra'].dt.month
    vendas_mensais = df.groupby('Mes')['Faturamento (Valor da Venda)'].sum().reset_index()
    meses_nomes = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    vendas_mensais['Mes_Nome'] = vendas_mensais['Mes'].map(meses_nomes)

    fig_vendas_mensais = px.bar(vendas_mensais, x='Mes_Nome', y='Faturamento (Valor da Venda)',
                                 title='Faturamento Total por Mês',
                                 labels={'Faturamento (Valor da Venda)': 'Faturamento Total', 'Mes_Nome': 'Mês'},
                                 template="plotly_dark")
    st.plotly_chart(fig_vendas_mensais)

elif opcao == "Produtos Mais Vendidos":
    st.header("Produtos Mais Vendidos")

    # Agrupa os dados por produto e calcula o faturamento total, ordenando por faturamento
    vendas_por_produto = df.groupby('Produto Comprado')['Faturamento (Valor da Venda)'].sum().sort_values(ascending=False).reset_index()

    # --- Gráfico de Barras Horizontais ---
    fig_barras_produtos = px.bar(vendas_por_produto,
                                 x='Faturamento (Valor da Venda)',
                                 y='Produto Comprado',
                                 orientation='h',
                                 title='Faturamento por Produto',
                                 labels={'Faturamento (Valor da Venda)': 'Faturamento Total',
                                         'Produto Comprado': 'Produto'},
                                 color='Faturamento (Valor da Venda)',
                                 color_continuous_scale='viridis',
                                 template="plotly_dark")
    st.plotly_chart(fig_barras_produtos)

    st.markdown("---")

    # --- Tabela de Valores Totais por Produto ---
    st.subheader("Valores Totais por Produto")
    # Formata a coluna de faturamento para exibição em moeda
    vendas_por_produto['Faturamento (Valor da Venda)'] = vendas_por_produto['Faturamento (Valor da Venda)'].map(lambda x: f'R$ {x:,.2f}')
    st.dataframe(vendas_por_produto)

    # --- Destaque do Produto Principal (Opcional) ---
    if not vendas_por_produto.empty:
        produto_principal = vendas_por_produto.iloc[0]['Produto Comprado']
        faturamento_principal = vendas_por_produto.iloc[0]['Faturamento (Valor da Venda)']
        st.info(f"Produto com maior faturamento: **{produto_principal}** com **{faturamento_principal}**.")

    st.markdown("---")

elif opcao == "Distribuição de Idade":
    st.header("Distribuição de Idade dos Compradores")
    fig_idade = px.histogram(df, x='Idade do Comprador', nbins=20,
                              title='Distribuição de Idade dos Compradores',
                              labels={'Idade do Comprador': 'Idade', 'count': 'Número de Compradores'},
                              template="plotly_dark")
    st.plotly_chart(fig_idade)

elif opcao == "Tráfego Pago":
    st.header("Investimento em Tráfego Pago")
    total_investido = df['Investimento em Tráfego Pago'].sum()
    st.metric(label="Total Investido em Tráfego Pago", value=f"R$ {total_investido:,.2f}")
    st.write("O valor investido equivale a 21,5% do faturamento.")