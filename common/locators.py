from selenium.webdriver.common.by import By


class HomePageLocators:
    search_field_min = (By.CSS_SELECTOR, 'span[class^="fas fa-search"]')
    search_field_max = (By.CSS_SELECTOR, 'input[class^="aa-Input"]')
    search_field_submit = (By.CSS_SELECTOR, 'button[class^="aa-SubmitButton"]')
    login = (By.CSS_SELECTOR, 'a[class^="link-acesso"]')


class PopUpLocators:
    accept_cookie = (By.CSS_SELECTOR, 'button[class^="lcb-botao"]')


class SearchPageLocators:
    results_search_page = (By.CSS_SELECTOR, 'a[target^="_blank"]')

