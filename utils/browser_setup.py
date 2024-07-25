from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_browser(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    return driver