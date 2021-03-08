from base.base_page import BasePage
from utilities.utilities_for_studio_page import Util
from datetime import date


class FindWorkshopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    #Find Workshop Page Locators
    _expected_title = "Find WW Studios & Meetings Near You | WW USA"
    _find_your_workshop_header = "pageTitle-1fqXB"  # class
    _studio_tab_under_find_your_workshop = "studioIcon-2TdMR" #class
    _search_location_box = "location-search" #id
    _search_button = "rightArrow-daPRP" #class
    _filters_button = "showHideFilters-3TLXe" #class

    _studio_name = "linkUnderline-1_h4g" #class
    _distance_to_studio = "distance-OhP63" #class

    #Individual Studio Page locators
    _studio_name_on_studio_page = "locationName-1jro_" #class
    _business_hours_dropdown = "title-3o8Pv" # class
    _todays_business_hours = "//div[contains(text(), '{}')]/following-sibling::div".format(date.today().strftime("%A")) #xpath
    _all_schedules_nodes = "dayName-1UpF5" #class
    _meetings = './/following-sibling::div[@class="meeting-14qIm"]' #xpath


    #Elements actions and methods on Find Your Workshop Page
    def verify_find_workshop_page_title(self):
        return self.verify_page_title(expected_title=self._expected_title)

    def select_studio_tab(self):
        self.driver.find_element_by_class_name(self._studio_tab_under_find_your_workshop).click()

    def enter_location(self, zip_code):
        self.driver.find_element_by_id(self._search_location_box).send_keys(zip_code)

    def click_search_button(self):
        self.driver.find_element_by_class_name(self._search_button).click()

    def get_studio_name_text_for_10011(self):
        studio_name_element = self.driver.find_element_by_class_name(self._studio_name)
        print(studio_name_element.text)
        return studio_name_element.text

    def print_distance_to_studio(self):
        distance_to_studio = self.driver.find_element_by_class_name(self._distance_to_studio)
        print(distance_to_studio.text)
        return distance_to_studio.text

    def go_to_studio_page(self):
        self.driver.find_element_by_class_name(self._studio_name).click()

    def search_studio_by_location(self, zip_code="10011"):
        self.select_studio_tab()
        self.enter_location(zip_code)
        self.click_search_button()
        """
        Verify results are shown on the page by finding Filter button on the page
        """
        try:
            element = self.driver.find_element_by_class_name(self._filters_button)
            result = bool(element)
            return result
        except:
            return False

    # Elements actions and methods on Individual Studio Page
    def get_studio_name_on_studio_page(self):
        studio_name_on_studio_page = self.driver.find_element_by_class_name(self._studio_name_on_studio_page)
        print(studio_name_on_studio_page.text)
        return studio_name_on_studio_page.text

    def click_business_hours_dropdown(self):
        self.driver.find_element_by_class_name(self._business_hours_dropdown).click()

    def find_todays_business_hours(self):
        return self.driver.find_element_by_xpath(self._todays_business_hours)

    def print_todays_business_hours(self):
        self.click_business_hours_dropdown()
        todays_business_hours = self.find_todays_business_hours().text
        print(todays_business_hours)
        return todays_business_hours

    def two_schedules(self):
        two_schedules = self.driver.find_elements_by_class_name(self._all_schedules_nodes)
        return two_schedules

    def print_schedule_in_person(self):
        two_schedules = self.two_schedules()
        schedule_in_person = two_schedules[:7]
        print("_________________")
        print("Studio Workshops: ")
        self.util.print_workshops(schedule_in_person)

    def print_schedule_virtual(self):
        two_schedules = self.two_schedules()
        schedule_virtual = two_schedules[7:]
        print("_________________")
        print("Virtual Workshops:")
        self.util.print_workshops(schedule_virtual)

