from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseHelper:
    """Store of Base helpers"""

    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait (self.driver, timeout=5)

    def wait_until_element_find(self, locator_type, locator):
        """Wait until element find and return it"""
        self.wait.until (EC.presence_of_element_located ((locator_type, locator)))
        return self.driver.find_element (by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until (EC.element_to_be_clickable ((locator_type, locator)))
        self.driver.find_element (by=locator_type, value=locator).click ()

    def fill_input_fields(self, by, locator, value):
        """Find element, clear it and add value"""
        email=self.wait_until_element_find (locator_type=by, locator=locator)
        email.clear ()
        email.send_keys (value)

    def find_and_input_search_field(self, by, locator, value):
        """Find search input and add value, and click search button"""
        search_field=self.driver.find_element (by=by, value=locator)
        search_field.clear ()
        search_field.send_keys (value)

    def find_by_contains_text(self, text):
        """Find element using XPATH contains function by text"""
        return self.driver.find_element_by_xpath (text)
