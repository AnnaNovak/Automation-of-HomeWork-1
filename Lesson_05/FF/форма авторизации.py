import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login") 

# Найти поле username и ввести значение "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
    
# Найти поле password и ввести значение "SuperSecretPassword!"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
    
# Найти кнопку Login и кликнуть по ней
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
    
# Проверка
print("Логин выполнен успешно!")

# Закрыть браузер через 5 секунд
time.sleep(5)
driver.quit()




