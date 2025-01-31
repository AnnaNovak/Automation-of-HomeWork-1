import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тестовая функция
def test_purchase_flow(driver):
    # Открытие сайта магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    username_field = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    password_field = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Переход в корзину
    driver.get("https://www.saucedemo.com/cart.html")

    # Нажатие на Checkout
    checkout_button = driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    first_name_field = driver.find_element(By.ID, "first-name").send_keys("Anna")
    last_name_field = driver.find_element(By.ID, "last-name").send_keys("Novak")
    postal_code_field = driver.find_element(By.ID, "postal-code").send_keys("12345")
    continue_button = driver.find_element(By.ID, "continue").click()

    # Ожидание загрузки итоговой стоимости
    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    # Получение итоговой стоимости
    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    price = "Total: $58.29"
    assert total == price, f"Ожидаемая стоимость: {price}, Фактическая стоимость: {total}"
