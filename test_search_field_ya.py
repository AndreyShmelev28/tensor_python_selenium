import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
import time
from selenium.webdriver.common.by import By

link_ya_main_page = "https://yandex.ru/"


def test_search_on_yandex(browser):
    main_page = MainPage(browser, link_ya_main_page)
    main_page.open()
    main_page.should_be_search_field()
    main_page.enter_word_in_search_field()
    main_page.should_be_suggestion_table()
    main_page.press_return_to_start_searching()
    search_page = SearchResultPage(browser, browser.current_url)
    search_page.should_be_present_link_in_range_of_results(5)

