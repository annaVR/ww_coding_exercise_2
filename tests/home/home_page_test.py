import unittest
from pages.home.home_page import HomePage
import pytest
import time


@pytest.mark.usefixtures("module_setup_to_test_class", "method_setup")
class HomePageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    def test_home_page(self):
        print("step 1")
        print("step 2")
        result = self.home_page.verify_home_page_title()
        assert result is True
        time.sleep(1)
        result = self.home_page.verify_redirected_to_workshops_page()
        assert result is True
        time.sleep(1)
