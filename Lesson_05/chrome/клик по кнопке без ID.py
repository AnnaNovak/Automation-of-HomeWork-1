from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By\

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

#открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary") 
blue_button.click() 

# Проверка 
print("Кнопка нажата успешно!") 
# Закрыть браузер 
driver.quit()