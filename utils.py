from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") # inicia com a janela maximizada
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # Instancia o driver do Chrome automaticamente com o ChromeDriverManager
    return driver
