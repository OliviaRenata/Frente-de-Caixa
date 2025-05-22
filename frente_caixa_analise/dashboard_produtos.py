import pandas as pd
import streamlit as st

# Carregar CSV
df = pd.read_csv("Produtos.csv", sep=";", engine="python")

# Limpeza e conversões
df["Preço de Custo"] = pd.to_numeric(df["Preço de Custo"], errors="coerce")
df["Preço Venda Varejo"] = pd.to_numeric(df["Preço Venda Varejo"], errors="coerce")
df["Quantidade Mínima Atacado"] = pd.to_numeric(df["Quantidade Mínima Atacado"], errors="coerce")
df["Ativo"] = df["Ativo"].str.strip().str.lower()

# Detectar a coluna de estoque
estoque_col = next((col for col in df.columns if "estoque" in col.lower()), None)
if estoque_col:
    df[estoque_col] = pd.to_numeric(df[estoque_col], errors="coerce")

# Layout do Streamlit
st.set_page_config(page_title="Análise de Produtos", layout="wide")
st.title("Análise de Produtos da Loja")

# Produtos inativos
inativos = df[df["Ativo"] != "sim"]
st.subheader("Produtos Inativos")
st.dataframe(inativos[["Descrição", "Ativo"]])

# Estoque zerado
if estoque_col:
    zerado = df[df[estoque_col] <= 0]
    st.subheader("Produtos com Estoque Zerado")
    st.dataframe(zerado[["Descrição", estoque_col]])

    # Reposição
    reposicao = df[
        (df[estoque_col] < df["Quantidade Mínima Atacado"]) &
        (df["Quantidade Mínima Atacado"] > 0)
    ]
    st.subheader("Produtos com Estoque Abaixo do Mínimo")
    st.dataframe(reposicao[["Descrição", estoque_col, "Quantidade Mínima Atacado"]])

# Cálculo das margens (excluindo custo = 0)
df = df[df["Preço de Custo"] > 0]
df["Margem Lucro (%)"] = ((df["Preço Venda Varejo"] - df["Preço de Custo"]) / df["Preço de Custo"]) * 100
df["Margem Lucro (R$)"] = df["Preço Venda Varejo"] - df["Preço de Custo"]

# Top margens
top_margem = df.sort_values(by="Margem Lucro (%)", ascending=False).head(10)
st.subheader("Top 10 Produtos com Maior Margem de Lucro")
st.dataframe(top_margem[["Descrição", "Preço de Custo", "Preço Venda Varejo", "Margem Lucro (%)"]])

# Gráfico
st.subheader("Gráfico de Margem de Lucro")
st.bar_chart(top_margem.set_index("Descrição")["Margem Lucro (%)"])

# Promoções sugeridas
promocoes = df[(df["Margem Lucro (%)"] > 100) & (df[estoque_col] > 10)]
st.subheader("Sugestões de Promoções")
st.dataframe(promocoes[["Descrição", "Margem Lucro (%)", estoque_col]])
