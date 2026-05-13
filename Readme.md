🔍 Buscapé Smart Scraper - Notebook Finder
📝 Descrição do Projeto
Este projeto é uma automação de busca e mineração de dados (Web Scraping) desenvolvida para encontrar as melhores ofertas de notebooks Lenovo no site Buscapé. O objetivo é transformar uma pesquisa manual cansativa em uma planilha organizada, filtrando apenas o que realmente interessa ao usuário (custo-benefício).

O robô navega pelo e-commerce, lida com carregamento dinâmico de produtos, limpa os dados financeiros e exporta um relatório pronto para análise no Excel.

🚀 Funcionalidades
Modo Headless: Execução em segundo plano para maior performance e economia de recursos.

Bypass de Segurança: Utilização de User-Agents reais para evitar bloqueios e CAPTCHAs.

Scroll Dinâmico: Simulação de interação humana para carregar produtos via Lazy Loading.

Data Cleaning: Tratamento de strings complexas (R$, pontos e vírgulas) usando Expressões Regulares (Regex).

Filtros Inteligentes (Pandas): * Seleção automática de processadores Intel Core i3 ou i5.

Filtro de preço máximo configurado para R$ 2.000,00.

Exportação Excel-Ready: Geração de arquivo CSV com codificação e separadores específicos para abertura direta no Microsoft Excel brasileiro.

🛠️ Tecnologias e Bibliotecas
Python 3.x

Selenium: Automação de navegação web.

Pandas: Manipulação e análise de dados.

Regex (re): Limpeza e padronização de textos.

Webdriver-Manager: Gerenciamento automático de drivers do navegador.

📖 O que eu aprendi neste projeto
Este projeto marcou minha evolução de scripts simples de interação para uma Pipeline de Dados completa:

Engenharia de Prompt: Uso de IA (GitHub Copilot) como mentor técnico para refatoração de código.

Tratamento de Dados: Entendi a importância de converter dados "sujos" da web em tipos numéricos (float) para possibilitar cálculos.

Resiliência de Código: Implementação de WebDriverWait em vez de esperas fixas, tornando o robô mais rápido e estável.

Versionamento: Organização de commits semânticos para contar a história da evolução do projeto no Git.

🔧 Como rodar o projeto
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

Bash
pip install pandas selenium webdriver-manager
Execute o script:

Bash
python seu_script.py
📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
