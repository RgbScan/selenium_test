from  utils.browser_setup import get_browser
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Устанавливаем браузер
driver = get_browser()

# Запрашиваем ресурс по ссылке
driver.get("http://www.google.com")

# Выбираем поле поиска, вводим значение и жмем ENTER
search_from = driver.find_element(By.NAME, 'q')
search_from.send_keys('Selenium')
search_from.send_keys(Keys.RETURN)

# Ждем 10 секунд, затем првоеряем закружен ли элемент с id search
# Если загружен то выводим первый текст, если нет то второй
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )
    print('Результаты поиска отображаются')
except TimeoutException:
    print('Результаты поиска не были найден в течении 10 минут')

driver.quit()