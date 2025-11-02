# 📈 Investment Tracker

**Investment Tracker** é uma aplicação para **análise e acompanhamento de investimentos pessoais**, desenvolvida com foco em boas práticas de **engenharia de dados** e **automação analítica**.

O sistema realiza um pipeline completo de **ETL (Extração, Transformação e Carga)** a partir de dados exportados da B3, organiza as informações em formato **parquet otimizado** e disponibiliza **dashboards interativos** construídos com **Streamlit** e **Plotly**.

Com ele, é possível explorar movimentações de compra e venda, rendimentos, volume investido e comportamento de ativos ao longo do tempo — tudo a partir de dados processados automaticamente.

---

## 🧭 Objetivos do Projeto

- Organizar e tratar movimentações financeiras exportadas da B3  
- Criar um pipeline de ETL reutilizável e transparente  
- Oferecer visualizações interativas para análise de comportamento de investimento  
- Demonstrar boas práticas de engenharia de dados aplicadas a um caso real  
- Servir como base para estudos e aprimoramentos em automação financeira

---

## ⚙️ Tecnologias e Ferramentas Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | **Python 3.10+** |
| Manipulação de dados | **pandas**, **numpy**, **regex** |
| Armazenamento de dados | **Apache Parquet**, **CSV** |
| Visualização | **Plotly Express**, **Streamlit** |
| Automação / ETL | **Jupyter Notebook**, **scripts Python** |
| Outras | **datetime**, **dotenv**, **requests** |

---

## 🏗️ Estrutura do Projeto
```
investment-tracker/
│
├── data/
│ ├── raw/ # Dados brutos exportados da B3 (sem arquivos, pois estou utilizando dados reais)
│ ├── processed/ # Dados tratados e limpos
│ └── analytics/ # Dados prontos para visualização (Parquet)
│
├── etl/
│ ├── init.py
│ └── etl.py # Pipeline de transformação e classificação
│
├── notebooks/
│ └── extractDiscover.ipynb # Análises e exploração inicial dos dados
│
├── pages/
│ └── Ações.py # Página de visualização detalhada (Streamlit multipage)
│
├── app.py # Aplicação principal do Streamlit
├── requirements.txt # Dependências do projeto
├── README.md # Documentação
└── LICENSE # Licença
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seuusuario/investment-tracker.git
cd investment-tracker
```

### 2️⃣ Crie e ative um ambiente virtual
```
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3️⃣ Instale as dependências
```
pip install -r requirements.txt
```

### 4️⃣ Adicione seus dados brutos
Coloque o arquivo exportado da B3 (ex: movimentacao-YYYY-MM-DD.xlsx) dentro da pasta:
```
/data/raw/
```

### 5️⃣ Execute o ETL

```
python etl/etl.py
```
Os arquivos processados serão salvos em /data/processed e /data/analytics.

### 6️⃣ Inicie o dashboard
```
streamlit run app.py

```
Abra no navegador o link exibido no terminal (geralmente: http://localhost:8501).


## 📊 Principais Funcionalidades

- 📅 Filtro por período: selecione datas predefinidas (7 dias, 30 dias, ano atual, etc.)

- 💰 Visualização de movimentações: gráficos de compras e vendas por tipo e produto

- 📈 Métricas gerais: total investido, número de operações e produtos distintos

- 🔍 Filtros dinâmicos: por tipo de investimento e produto

- 🧩 Classificação automática: Tesouro, LCI, LCA, CDB, Ações, FIIs e outros

- ⚡ Desempenho otimizado: leitura via arquivos Parquet

## 🧠 Aprendizados e Boas Práticas Aplicadas

- Uso de pandas para manipulação eficiente de dados financeiros

- Estrutura modular de ETL separando camadas de dados brutos, tratados e analíticos

- Armazenamento otimizado com Apache Parquet para leitura rápida no Streamlit

- Criação de dashboards interativos com Plotly Express

- Aplicação de regex para classificação automática de produtos financeiros

- Organização de projeto seguindo boas práticas de engenharia de dados

## 🧩 Próximos Passos (Roadmap)

- Integração com APIs externas (ex: brapi.dev) para enriquecer dados de ativos

- Cálculo de rentabilidade histórica e custo médio de compra

- Comparativos automáticos entre ativos e indicadores de mercado

- Exportação de relatórios personalizados em PDF

- Implementação de banco de dados (MongoDB ou PostgreSQL)

## 🪪 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

**Daniel Bispo**
Desenvolvedor e entusiasta de engenharia de dados, automação e finanças pessoais.
📫 [LinkedIn](https://www.linkedin.com/in/udanielbispo/) • [GitHub](https://github.com/uDanielBispo)