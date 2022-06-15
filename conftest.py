import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True)
def maximaze_windows():
    browser.open('https://google.com').driver.maximize_window()