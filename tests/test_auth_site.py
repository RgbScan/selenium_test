import selenium
from utils.browser_setup import get_browser
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


drive = get_browser()
drive.get('https://the-internet.herokuapp.com/login')
w_login = drive.find_element(By.ID, 'username')
w_password = drive.find_element(By.ID, 'password')
w_login.send_keys('tomsmith ')
w_password.send_keys('SuperSecretPassword')
button = drive.find_element(By.CLASS_NAME, 'radius')


try:
    EC.presence_of_element_located((By.ID, 'flash error'))
    print('Введены не корректные данные - тест пройден')
except TimeoutException:
    print('Ошибка - тест не пройден')


drive.quit()
