from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(16) # seconds

#открыть страницу
driver.get("http://uitestingplayground.com/ajax")

# Найти синюю кнопку и кликнуть по ней 
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary") 
blue_button.click() 

# Получить текст из зеленой плашки и вывести его в консоль 
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt) 

# Закрыть браузер
driver.quit()
