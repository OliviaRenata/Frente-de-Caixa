import pandas as pd
import os

# Criar pasta de saída
os.makedirs("relatorios", exist_ok=True)

# Carregar CSV
df = pd.read_csv("Produtos.csv", sep=";", engine="python")

# Conversões
df["Preço de Custo"] = pd.to_numeric(df["Preço de Custo"], errors="coerce")
df["Preço Venda Varejo"] = pd.to_numeric(df["Preço Venda Varejo"], errors="coerce")
df["Quantidade Mínima Atacado"] = pd.to_numeric(df["Quantidade Mínima Atacado"], errors="coerce")
df["Ativo"] = df["Ativo"].str.strip().str.lower()

# Detectar estoque
estoque_col = next((col for col in df.columns if "estoque" in col.lower()), None)
if estoque_col:
    df[estoque_col] = pd.to_numeric(df[estoque_col], errors="coerce")

# Produtos inativos
inativos = df[df["Ativo"] != "sim"]
print("\n📌 PRODUTOS INATIVOS:")
print(inativos[["Descrição", "Ativo"]])
inativos.to_excel("relatorios/relatorio_inativos.xlsx", index=False)

# Estoque zerado
if estoque_col:
    zerado = df[df[estoque_col] <= 0]
    print("\n📌 PRODUTOS COM ESTOQUE ZERADO:")
    print(zerado[["Descrição", estoque_col]])
    zerado.to_excel("relatorios/relatorio_estoque_zerado.xlsx", index=False)

    reposicao = df[
        (df[estoque_col] < df["Quantidade Mínima Atacado"]) &
        (df["Quantidade Mínima Atacado"] > 0)
    ]
    print("\n📌 PRODUTOS COM ESTOQUE ABAIXO DO MÍNIMO:")
    print(reposicao[["Descrição", estoque_col, "Quantidade Mínima Atacado"]])
    reposicao.to_excel("relatorios/relatorio_reposicao.xlsx", index=False)

# Evitar divisão por zero
df = df[df["Preço de Custo"] > 0]

# Margens
df["Margem Lucro (%)"] = ((df["Preço Venda Varejo"] - df["Preço de Custo"]) / df["Preço de Custo"]) * 100
df["Margem Lucro (R$)"] = df["Preço Venda Varejo"] - df["Preço de Custo"]

margem_top = df[["Descrição", "Preço de Custo", "Preço Venda Varejo", "Margem Lucro (%)"]] \
    .sort_values(by="Margem Lucro (%)", ascending=False) \
    .head(10)

print("\n📌 MARGEM DE LUCRO POR PRODUTO:")
print(margem_top)
margem_top.to_excel("relatorios/relatorio_margem.xlsx", index=False)

promocoes = df[(df["Margem Lucro (%)"] > 100) & (df[estoque_col] > 10)]
print("\n📌 SUGESTÕES DE PROMOÇÕES:")
print(promocoes[["Descrição", "Margem Lucro (%)", estoque_col]])
promocoes.to_excel("relatorios/relatorio_promocoes.xlsx", index=False)
