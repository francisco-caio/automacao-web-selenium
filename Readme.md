[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-43B02A?style=flat&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat)](https://github.com/francisco-caio/automacao-scraper)

# 🔍 Buscapé Smart Scraper - Notebook Finder

Automação inteligente para mineração de dados (**Web Scraping**) que encontra as melhores ofertas de **Notebooks Lenovo** no Buscapé, transformando pesquisa manual em relatórios estruturados.

---

## 📝 Descrição do Projeto

Este bot navega pelo e-commerce de forma automatizada, carrega produtos via **lazy loading**, limpa dados financeiros com **Regex** e exporta um relatório **pronto para Excel**.

**Objetivo:** Filtrar notebooks com processador **Intel Core i3/i5** e preço abaixo de **R$ 2.000** com zero intervenção humana.

---

## 🚀 Funcionalidades

- **Modo Headless** — Execução em background para melhor performance
- **Bypass de Segurança** — User-Agent real para evitar bloqueios e CAPTCHAs
- **Scroll Dinâmico** — Simulação de interação humana para carregar produtos
- **Data Cleaning** — Tratamento de strings financeiras com **Expressões Regulares**
- **Filtros Inteligentes** — Seleção automática por processador e faixa de preço
- **Exportação Excel-Ready** — CSV com separador `;` e codificação `utf-8-sig`

---

## 🛠️ Stack Tecnológico

- **Python 3.8+** — Linguagem base
- **Selenium** — Automação de navegação web
- **Pandas** — Manipulação e análise de dados
- **Regex (re)** — Limpeza e padronização de textos
- **WebDriver-Manager** — Gerenciamento automático de drivers

---

## 💡 Pipeline de Dados

```
Busca no Buscapé
    ↓
Carregamento com Scroll (3x)
    ↓
Extração de elementos HTML
    ↓
Limpeza de preços (Regex)
    ↓
Filtro Pandas (i3|i5 + preço < 2000)
    ↓
Exportação CSV (ofertas_lenovo_filtradas.csv)
```

---

## 📖 Aprendizados Principais

- ✅ **Engenharia de Prompt** — Refatoração com IA como mentor técnico
- ✅ **Tratamento de Dados** — Conversão de strings sujas em tipos numéricos
- ✅ **Resiliência** — **WebDriverWait** ao invés de esperas fixas
- ✅ **Versionamento** — Commits semânticos contando a história do projeto
- ✅ **Pipeline de Dados** — Do raw data ao relatório estruturado

---

## 🔧 Como Rodar

### 1. Clone o repositório

```bash
git clone https://github.com/francisco-caio/automacao-scraper.git
cd automacao-scraper
```

### 2. Instale as dependências

```bash
pip install pandas selenium webdriver-manager
```

### 3. Execute o bot

```bash
python automacaoweb.py
```

### 4. Verifique a saída

Um arquivo `ofertas_lenovo_filtradas.csv` será gerado no diretório raiz, pronto para abrir no Excel.

---

## 📊 Exemplo de Saída

| Modelo | Valor Bruto | Valor Numérico |
|--------|------------|----------------|
| Lenovo IdeaPad 3 (i3) | R$ 1.899,00 | 1899.0 |
| Lenovo ThinkBook (i5) | R$ 1.799,99 | 1799.99 |

---

## 🎯 Próximos Passos

- [ ] Adicionar suporte a múltiplos e-commerce
- [ ] Implementar notificações via email
- [ ] Criar dashboard com Streamlit
- [ ] Adicionar agendamento com APScheduler

---

## 📄 Licença

Projeto de código aberto para fins educacionais sob licença MIT.