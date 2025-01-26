from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу 
driver.get("http://uitestingplayground.com/textinput") 

# Найти поле ввода и указать текст 
element = driver.find_element(By.ID, "newButtonName") 
element.send_keys("SkyPro") 

# Найти синюю кнопку и кликнуть по ней 
blue_button = driver.find_element(By.ID, "updatingButton") 
blue_button.click() 

driver.implicitly_wait(5) # seconds

# Получить текст кнопки и вывести его в консоль 
print( driver.find_element(By.CSS_SELECTOR, "#updatingButton").text )

# Закрыть браузер
driver.quit()