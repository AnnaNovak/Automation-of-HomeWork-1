import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Создаем экземпляр драйвера
    driver = webdriver.Chrome()
    yield driver
    # Закрываем браузер после завершения теста
    driver.quit()

def test_form_submission(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидание загрузки страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))
       
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнить форму значениями
    driver.find_element(By.CSS_SELECTOR,  "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажать кнопку Submit
    
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    # Проверка полей на соответствие цветов
    zip_code_red = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert 'alert-danger' in zip_code_red.get_attribute('class')

    green_color = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    assert len(green_color) == 9
