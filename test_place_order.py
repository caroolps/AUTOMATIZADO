import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver

def test_place_order():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com/index.html")

    # Ir para a categoria Phones
    driver.find_element(By.LINK_TEXT, "Phones").click()
    time.sleep(5)

    # Adicionar Nokia lumia 1520
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Nokia lumia 1520"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Add to cart']"))).click()
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    # Ir para carrinho
    driver.find_element(By.ID, "cartur").click()
    time.sleep(5)

    # Clicar em "Place Order"
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
    time.sleep(5)

    # Preencher dados do pedido
    driver.find_element(By.ID, "name").send_keys("Hanzo Hasashi")
    driver.find_element(By.ID, "country").send_keys("Japan")
    driver.find_element(By.ID, "city").send_keys("Tokyo")
    driver.find_element(By.ID, "card").send_keys("4485572801000971")
    driver.find_element(By.ID, "month").send_keys("01")
    driver.find_element(By.ID, "year").send_keys("2039")

    # Clicar no botão "Purchase"
    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
    time.sleep(15)

    # Verificar confirmação do pedido
    confirmation = driver.find_element(By.CLASS_NAME, "sweet-alert").text
    print("Order confirmation:")
    print(confirmation)
    assert "Thank you for your purchase!" in confirmation

    driver.quit()

# Chamada da função
if __name__ == "__main__":
    test_place_order()
