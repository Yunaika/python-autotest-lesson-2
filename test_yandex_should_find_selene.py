from selene import be, have
from selene.support.shared import browser

# ищем search_text в yandex и проверяем есть ли в результатах result_text
def search_text_in_yandex(search_text: str, result_text: str):
    browser.element('#text').should(be.blank).type(search_text).press_enter()
    browser.element('[class="content__left"]').should(have.text(result_text))

class TestYandexSearch:
    # позитивный тест
    def test_yandex_should_find_selene_positive(self):
        search_text_in_yandex('selene', 'User-oriented Web UI browser tests in Python')

    # негативный тест
    def test_yandex_should_find_selene_negative(self):
        search_text_in_yandex('asdfgghjgdfgdfg', 'По вашему запросу ничего не нашлось')
