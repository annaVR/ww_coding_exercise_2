from base.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Homepage Locators
    _attend_dropdown = "Icon_icon__wrapper__3dIsp" #class_name
    _virtual_and_in_person_workshops = "MenuItem_subtitle__3LoiE" #class_name

    _expected_title = "WW (Weight Watchers): Weight Loss Program & Wellness Help | WW USA"

    #Location from Find Your Workshop page - to test redirect
    _find_your_workshop_header = "pageTitle-1fqXB"  # class

    #Elements actions and methods
    def verify_home_page_title(self):
        return self.verify_page_title(expected_title=self._expected_title)

    def click_attend_dropdown(self):
        self.driver.find_element_by_class_name(self._attend_dropdown).click()

    def select_virtual_and_in_person_workshops(self):
        self.driver.find_element_by_class_name(self._virtual_and_in_person_workshops).click()

    def navigate_to_workshops_page(self):
        """
        Navigate to workshops page
        """
        self.click_attend_dropdown()
        self.select_virtual_and_in_person_workshops()

    def verify_redirected_to_workshops_page(self):
        """
        Verify redirected to workshops page by finding "Find You Workshop" header on the page
        """
        self.navigate_to_workshops_page()
        try:
            element = self.driver.find_element_by_class_name(self._find_your_workshop_header)
            result = bool(element)
            return result
        except:
            return False



