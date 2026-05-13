import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Configuração do Navegador (com Headless e User-Agent)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") # Roda em segundo plano
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
wait = WebDriverWait(navegador, 15)

try:
    print("Iniciando busca no Buscapé (Modo Silencioso)...")
    navegador.get("https://www.buscape.com.br/")

    # Busca o Notebook
    busca = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))
    busca.send_keys("Notebook Lenovo")
    busca.send_keys(Keys.ENTER)

    print("Carregando resultados e aplicando scroll...")
    # 2. Scroll suave para carregar o Lazy Loading
    for _ in range(3):
        navegador.execute_script("window.scrollBy(0, 1000);")
        import time
        time.sleep(2)

    # Captura todos os cards de produtos
    produtos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="product-card"]')))
    
    lista_produtos = []
    for produto in produtos:
        try:
            nome = produto.find_element(By.CSS_SELECTOR, 'h2').text
            preco = produto.find_element(By.CSS_SELECTOR, '[data-testid="product-card::price"]').text
            lista_produtos.append({"modelo": nome, "valor": preco})
        except:
            continue

    # 3. Inteligência com Pandas
    if lista_produtos:
        df = pd.DataFrame(lista_produtos)

        # Função de limpeza: Explicação da Regex [^\d,]
        # Ela remove tudo que NÃO é dígito ou vírgula. 
        # Ex: "R$ 1.999,00" -> "1999,00" -> "1999.00"
        def limpar_preco(preco_texto):
            apenas_numeros = re.sub(r'[^\d,]', '', preco_texto)
            return float(apenas_numeros.replace(',', '.'))

        df['valor_num'] = df['valor'].apply(limpar_preco)

        # 4. Filtros Coerentes: i3 ou i5 E preço < 2000
        # O símbolo | significa "OU". O str.contains ignora maiúsculas/minúsculas
        filtro_processador = df['modelo'].str.contains('i3|i5', case=False)
        filtro_preco = df['valor_num'] < 2000
        
        df_final = df[filtro_processador & filtro_preco].sort_values(by='valor_num')

        # 5. Exportação para Excel (CSV com ponto e vírgula)
        df_final.to_csv("ofertas_lenovo_filtradas.csv", 
                       index=False, 
                       sep=';', 
                       encoding='utf-8-sig')
        
        print(f"Sucesso! {len(df_final)} notebooks encontrados e salvos no CSV.")
    else:
        print("Nenhum produto encontrado.")

except Exception as e:
    print(f"Erro na automação: {e}")

finally:
    print("Finalizando processo...")
    navegador.quit()