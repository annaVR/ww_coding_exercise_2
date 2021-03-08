from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        # wait = WebDriverWait(self.driver, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])
        # page_title_loaded = wait.until(EC.title_contains(expected_title))
        # print("Page_title_loaded: {}".format(page_title_loaded))
        #
        # print(self.driver.title)
        return self.driver.title
