from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By\

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

#открыть страницу
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Найти кнопку "Add Element" и нажать её 5 раз
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for i in range(5):
    add_button.click()
    
# Найти все кнопки "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    
# Вывести количество кнопок "Delete"
print("Количество кнопок 'Delete':", len(delete_buttons))

# Закрыть браузер через 5 секунд
sleep(5)

driver.quit()
