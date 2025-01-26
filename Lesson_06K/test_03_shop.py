from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))


# Открыть страницу
driver.get("https://www.saucedemo.com/")


# Авторизация
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Добавление товаров в корзину
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "inventory_container"))
    )
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Перейти в корзину
driver.find_element(By.ID, "shopping_cart_container").click()

# Нажать кнопку Checkout
driver.find_element(By.ID, "checkout").click()

# Заполнение формы
driver.find_element(By.ID, "first-name").send_keys("Имя")
driver.find_element(By.ID, "last-name").send_keys("Фамилия")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Ожидание загрузки итоговой стоимости
total_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
# Получение итоговой стоимости
total = total_element.text

# Проверка итоговой суммы
assert total == "Total: $58.29", f"Ожидаемая итоговая сумма: $58.29, полученная сумма: {total}"

print (total)

# Закрыть браузер
driver.quit()
   
    