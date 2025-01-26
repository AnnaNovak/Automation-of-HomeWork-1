from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу 
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html") 

# Дождаться загрузки всех картинок
driver.implicitly_wait(10) 

# Получить значение атрибута src у 3-й картинки # Вывести значение в консоль
src = driver.find_element(By.CSS_SELECTOR, 'img[src= "img/award.png"]').get_attribute("src")
print(src)


# Закрыть браузер
driver.quit()
