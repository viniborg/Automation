from urllib.parse import parse_qs, urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from abc import ABC


class Selenium:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

    def text_to_be_present_in_element_atribute_href(self, locator, text):
        element = self.element_is_visible(locator)
        element = element.get_attribute('href')

        if element:
            return text.lower() in element
        else:
            raise ValueError('Element text_to_be_present_in_element_atribute_href not visible')

    def valid_button_actived(self, locator):
        return conditions.element_to_be_clickable(locator)

    def element_is_visible(self, locator):
        try:
            condition = conditions.presence_of_element_located(locator)
            element = WebDriverWait(self.webdriver, 6).until(condition)
            return element

        except Exception as ex:
            print(f'Exception ElementIsNotVisible {ex}')


class Page(ABC, Selenium):
    def __init__(self, webdriver, url):
        super().__init__(webdriver)
        self.url = url
        self.validate_url()

    def open_page(self):
        self.webdriver.get(self.url)

    def return_url_parameter_value(self, text):
        url_query = urlparse(self.webdriver.current_url).query
        return text in url_query

    def validate_url(self):
        if not self.url.strip():
            raise "Invalid URL"


class PageElement(ABC, Selenium):
    def __init__(self, webdriver=None):
        super().__init__(webdriver)
