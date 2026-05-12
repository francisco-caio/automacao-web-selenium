
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configuração do Navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
wait = WebDriverWait(navegador, 15)

try:
    print("Iniciando busca no Buscapé...")
    navegador.get("https://www.buscape.com.br/")

    # Aguarda até o campo de busca estar disponível
    busca = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))

    #  Busca o Notebook
    busca.send_keys("Notebook Lenovo")
    busca.send_keys(Keys.ENTER)
    
    print("carregando resultados...")
    produtos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="product-card"]')))

    lista_produtos = []
    
    # vamos pegar os cards de produtos
    print(f"Foram encontrados {len(produtos)} produtos na tela.")
    for produto in produtos[:10]: # Pega os 10 primeiros
        try:
            nome = produto.find_element(By.CSS_SELECTOR, 'h2').text
            preco = produto.find_element(By.CSS_SELECTOR, '[data-testid="product-card::price"]').text
            
            lista_produtos.append({
                "modelo": nome,
                "valor": preco
            })
        except:
            continue # Se um card falhar, pula para o próximo

except Exception as e:
    print(f"erro na automação: {e}")

finally:
    print("finalizando processo...")
   
