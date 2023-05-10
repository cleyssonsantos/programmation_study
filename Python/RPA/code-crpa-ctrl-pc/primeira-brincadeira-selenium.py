"""
Extraindo dollar e euro da internet e lançando numa planilha"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Crie o espaço para o detach dentro de uma variável
options = Options()
options.add_experimental_option("detach", True)

# Adicione o parâmetro no código
abrirNavegador = webdriver.Chrome(options=options)

abrirNavegador.get('https://www.google.com.br')
