from base.selenium_driver import SeleniumDriver
from utilities.utilities_for_studio_page import Util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class BasePage(SeleniumDriver):

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, expected_title):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.title_contains(expected_title))
            actual_title = self.get_title()
            if expected_title in actual_title:
                print("Expected title: {}, Actual title: {}".format(expected_title, actual_title))
                return True
            else:
                return False
        except:
            print("Failed to get page title")
            return False
