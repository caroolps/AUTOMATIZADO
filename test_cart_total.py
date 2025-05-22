import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver

def test_cart_total():
    driver = get_driver()
    driver.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(driver, 8) # Inicializa o navegador, acessa o site e espera até 10 segundos

    def add_product(product_name, category):
        # Seleciona a categoria (ex: "Laptops", "Phones")
        driver.find_element(By.LINK_TEXT, category).click()
        time.sleep(5)  # aguarda os produtos carregarem

        # Aguarda que o produto esteja disponível
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, product_name)))
        driver.find_element(By.LINK_TEXT, product_name).click()
        time.sleep(5)

        # Clica em "Add to cart" e aguarda o alerta
        driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        # Retorna para a página inicial para resetar a visualização
        driver.get("https://www.demoblaze.com/index.html")
        time.sleep(5)

    # Adiciona os produtos com suas respectivas categorias
    add_product("Sony vaio i7", "Laptops")
    add_product("Iphone 6 32gb", "Phones")

    # Acessa a página do carrinho
    driver.find_element(By.ID, "cartur").click()
    time.sleep(5)

    # Lista os nomes dos produtos no carrinho
    produtos = driver.find_elements(By.XPATH, "//tr[@class='success']/td[2]")
    nomes = [produto.text for produto in produtos]

    print("\n Products in cart:")
    for nome in nomes:
        print(f"- {nome}")

    # Obtém o total do carrinho
    total = driver.find_element(By.ID, "totalp").text
    print(f"\n Cart total: ${total}")

    # Validação: total deve ser maior que zero
    assert int(total) > 0

    driver.quit()

if __name__ == "__main__":
    test_cart_total()
