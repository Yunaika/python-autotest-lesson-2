import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True)
def open_yandex(resize_window):
    browser.open('https://yandex.ru')

@pytest.fixture(autouse=True)
def resize_window():
    browser.config.window_width = 1600
    browser.config.window_height = 800