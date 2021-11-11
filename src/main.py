from src.home import HomePage
from selenium import webdriver
from common.locators import PopUpLocators, SearchPageLocators, HomePageLocators

webdriver = webdriver.Chrome()

try:
    # Testing Search bar
    web = HomePage(webdriver, "https://www.gov.br/defesa/pt-br")
    web.open_page()
    web.accept_cookies()
    web.search('Formatura')
    assert web.check_results_search('Formatura') is True

    #Testing redirect page
    assert web.return_url_parameter_value('Formatura') is True

finally:
    webdriver.quit()
