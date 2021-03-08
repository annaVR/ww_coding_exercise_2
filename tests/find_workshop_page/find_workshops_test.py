from pages.home.home_page import HomePage
from pages.workshops.find_workshop_page import FindWorkshopPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("module_setup_to_test_class", "method_setup")
class FindWorkshopTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, module_setup_to_test_class):
        self.find_workshop_page = FindWorkshopPage(self.driver)
        self.home_page = HomePage(self.driver)


    def test_find_workshops_page(self):
        print("step 3")
        self.home_page.navigate_to_workshops_page()
        print("step 4")
        result = self.find_workshop_page.verify_find_workshop_page_title()
        assert result is True
        time.sleep(1)
        print("step 5")
        result = self.find_workshop_page.search_studio_by_location()
        assert result is True
        time.sleep(1)
        print("step 6")
        studio_search_result = self.find_workshop_page.get_studio_name_text_for_10011()
        assert studio_search_result == "WW Studio Flatiron"
        time.sleep(1)
        self.find_workshop_page.print_distance_to_studio()
        time.sleep(1)
        print("step7")
        self.find_workshop_page.go_to_studio_page()
        studio_name_on_studio_page = self.find_workshop_page.get_studio_name_on_studio_page()
        assert studio_name_on_studio_page == studio_search_result
        print("step 8")
        self.find_workshop_page.print_todays_business_hours()
        print("step 9")
        self.find_workshop_page.print_schedule_in_person()
        self.find_workshop_page.print_schedule_virtual()

