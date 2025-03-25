# Dashboard Fortwone Investimentos

Este é um dashboard interativo desenvolvido com Streamlit para apresentar a análise de vendas anuais da Fortwone Investimentos. O objetivo é destacar o desempenho, identificar tendências e fornecer insights para oportunidades de melhoria para o ano de 2025.

## Visão Geral

O dashboard oferece as seguintes seções para análise:

* **Visão Geral:** Apresenta um resumo geral do desempenho de vendas, incluindo o faturamento anual e uma tendência de faturamento mensal (atualmente exibida como um gráfico de linha).
* **Vendas Mensais:** Exibe o faturamento total por cada mês do ano em um gráfico de barras.
* **Produtos Mais Vendidos:** Mostra o faturamento por cada produto comprado em um gráfico de barras horizontais, além de uma tabela com os valores totais e um destaque para o produto com maior faturamento.
* **Distribuição de Idade:** Apresenta um histograma da distribuição de idade dos compradores.
* **Tráfego Pago:** Informa o total investido em tráfego pago e sua representatividade no lucro total.

## Tecnologias Utilizadas

* **Streamlit:** Framework Python para criar aplicativos web interativos para ciência de dados e machine learning.
* **Pandas:** Biblioteca Python para análise e manipulação de dados.
* **Plotly Express:** Biblioteca Python para criar gráficos interativos.

## Pré-requisitos

Antes de executar o dashboard, você precisará ter o Python instalado em seu sistema, juntamente com as bibliotecas necessárias. Você pode instalar as dependências usando o pip:

```bash
pip install streamlit
pip install pandas
pip install plotly