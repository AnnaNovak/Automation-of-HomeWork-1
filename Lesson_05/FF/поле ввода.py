import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs") 

#Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")
    
#Ввести в поле текст "1000"
input_field.send_keys("1000")
time.sleep(1)
    
# Очистить поле
input_field.clear()
time.sleep(1)
    
# Ввести в поле текст "999"
input_field.send_keys("999")
time.sleep(1)
    
# Проверка
print("Текст введен успешно!")


# Закрыть браузер через 5 секунд
time.sleep(5)
driver.quit()
