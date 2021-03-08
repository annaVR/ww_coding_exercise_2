"""
Created webdriver instance
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverFactory():

    def get_webdriver_instance(self):

        url = "https://www.weightwatchers.com/us/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(url)
        return driver
