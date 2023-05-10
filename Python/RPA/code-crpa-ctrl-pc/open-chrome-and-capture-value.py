from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

# name, id, xpath
options = Options()
options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.google.com.br')

pyautogui.sleep(3)

navegador.find_element(By.NAME, 'q').send_keys('Dolar hoje')

pyautogui.sleep(3)

navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

pyautogui.sleep(3)

valorDolarGoogle = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorDolarGoogle)
