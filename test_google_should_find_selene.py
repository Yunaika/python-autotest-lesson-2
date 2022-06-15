from selene import be, have
from selene.support.shared import browser

# ищем search_text в гугл и проверяем есть ли в результатах result_text
def search_text_in_google(search_text: str, result_text: str):
    browser.element('[name="q"]').should(be.blank).type(search_text).press_enter()
    browser.element('[id="search"]').should(have.text(result_text))

class TestGoogleSearch:
    # позитивный тест
    def test_google_should_find_selene_positive(self):
        search_text_in_google('selene', 'User-oriented Web UI browser tests in Python')

    # негативный тест
    def test_google_should_find_selene_negative(self):
        search_text_in_google('selene', 'Selenium Webdriver Java')
