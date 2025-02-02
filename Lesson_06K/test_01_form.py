from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))


# Открыть страницу 
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html") 

# Заполнить форму
driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

# Нажать кнопку Submit
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

waiter = WebDriverWait(driver, 40)

# Проверить, что поле Zip code подсвечено красным

alert_danger_color = "rgba(248, 215, 218, 1)"
zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
color_zip = zip_code.value_of_css_property("background-color")
assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

# Проверить, что остальные поля подсвечены зеленым
fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
for field in fields:
  element = driver.find_element(By.ID, field)
  color = element.value_of_css_property("background-color")
  assert color == "rgba(209, 231, 221, 1)", f"Field {field} is not highlighted in green"


print("Все проверки прошли успешно!")


# Закрыть браузер
driver.quit()
