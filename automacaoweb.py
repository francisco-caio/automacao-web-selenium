# imporatndo nossas bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
time.sleep(3)


print("Iniciando o robô... aguarde.")
# Configura o serviço e tenta instalar o driver
servico = Service(ChromeDriverManager().install())

    # Abre o navegador
navegador = webdriver.Chrome(service=servico)

    # Tenta entrar no site
# O robô vai digitar o site e dar enter
navegador.get("https://www.saucedemo.com/")
time.sleep(3)

# vai pegar o campo_usuario(objeto) pelo elemento id e vai fazer o metodo send_keys
campo_usuario = navegador.find_element(By.ID, "user-name")
campo_usuario.send_keys("standard_user")

# vai pegar o campo_senha(objeto) pelo elemento id e vai fazer o metodo send_keys
campo_senha = navegador.find_element(By.ID, "password")
campo_senha.send_keys("secret_sauce")

time.sleep(5)

# vai pegar o botao(enviar) pelo elemento dele e vai fazer a funcao onclick
botao_enviar = navegador.find_element(By.CSS_SELECTOR, "input[type='submit']")
botao_enviar.click()

print("Dados preenchidos e botão clicado!")
print(f"Sucesso! O site aberto foi: {navegador.title}")

    # espera carregar a tela por 20 segundos
time.sleep(20)

