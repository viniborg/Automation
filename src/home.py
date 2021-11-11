from page_objects.objects import Page, Selenium, PageElement
from common.locators import HomePageLocators, PopUpLocators, SearchPageLocators


class HomePage(Page):

    def accept_cookies(self):
        element = self.element_is_visible(PopUpLocators.accept_cookie)
        if element:
            element.click()
        else:
            print("PopUpLocaters is not visible")

    def search(self, string):
        self.find_element(HomePageLocators.search_field_min).click()

        search = self.element_is_visible(HomePageLocators.search_field_max)
        if search:
            search.send_keys(string)

        submit = self.element_is_visible(HomePageLocators.search_field_submit)
        if submit:
            self.find_element(HomePageLocators.search_field_submit).click()

    def check_results_search(self, text):
        return self.text_to_be_present_in_element_atribute_href(SearchPageLocators.results_search_page, text)

