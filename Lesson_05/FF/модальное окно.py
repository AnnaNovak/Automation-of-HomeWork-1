import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad") 
time.sleep(5)

# Найти кнопку "Close" в модальном окне и кликнуть по ней 
close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p") 
close_button.click() 

# Проверка 
print("Модальное окно закрыто успешно!") 

# Закрыть браузер через 5 секунд 
time.sleep(5)
driver.quit()