import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("c:\chromedriver.exe")
    yield browser
    browser.quit()




