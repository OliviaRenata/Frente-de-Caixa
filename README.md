Sistema de Frente de Caixa – Análise de Produtos e Dashboard Interativo
Descrição
Este projeto consiste em um sistema de análise de produtos para lojas de varejo, desenvolvido em Python, com foco no controle de estoque, análise de margem de lucro e geração de relatórios gerenciais. Além das análises automatizadas via terminal, o sistema conta com um dashboard web interativo, criado com Streamlit, facilitando a visualização e tomada de decisão.

Tecnologias Utilizadas
Python – Linguagem principal

Pandas – Análise e manipulação de dados

OpenPyXL – Exportação de relatórios para Excel

Streamlit – Dashboard web interativo

CSV – Arquivo de entrada de dados

Visual Studio Code – Ambiente de desenvolvimento

Funcionalidades
Leitura automática do arquivo Produtos.csv.

Identificação de:

Produtos inativos.

Produtos com estoque zerado.

Produtos com estoque abaixo do mínimo.

Cálculo da margem de lucro (valor e percentual).

Geração automática de relatórios Excel:

Produtos inativos.

Estoque zerado.

Reposição necessária.

Margens de lucro.

Sugestões de promoção.

Dashboard interativo:

Tabelas com análises de estoque e margem.

Gráficos de barras das maiores margens.

Sugestões de promoções.

Execução local com comandos simples.

Como Executar
1. Análises e Relatórios via Terminal
bash
Copiar
Editar
python analise_produtos.py
Relatórios serão gerados automaticamente na pasta relatorios/.

2. Dashboard Interativo
bash
Copiar
Editar
streamlit run dashboard_produtos.py
Acesse o dashboard no navegador:
http://localhost:8501

Estrutura do Projeto
markdown
Copiar
Editar
FRENTE DE CAIXA/
└── frente_caixa_analise/
    ├── Produtos.csv
    ├── analise_produtos.py
    ├── dashboard_produtos.py
    ├── README.md
    ├── requirements.txt
    └── relatorios/
Instalação das Dependências
bash
Copiar
Editar
pip install -r requirements.txt
Ou manualmente:

bash
Copiar
Editar
pip install pandas streamlit openpyxl
