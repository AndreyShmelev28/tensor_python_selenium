from pages.base_page import BasePage
from pages.locators import YandexMainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def should_be_search_field(self):
        assert self.is_element_present(*YandexMainPageLocators.SEARCH_FIELD_LOCATOR), "Search field is not presented"

    def enter_word_in_search_field(self):
        search_field = self.browser.find_element(*YandexMainPageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(YandexMainPageLocators.WORD_FOR_SEARCHING)

    def should_be_suggestion_table(self):
        assert self.is_element_present(*YandexMainPageLocators.SUGGESTION_TABLE_LOCATOR), "Suggestion table is not " \
                                                                                      "presented "

    def press_return_to_start_searching(self):
        search_field = self.browser.find_element(*YandexMainPageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(Keys.RETURN)

    def should_be_pictures_category_on_nav_bar(self):
        all_list = self.browser.find_elements(*YandexMainPageLocators.NAV_BAR_LOCATOR)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        assert "Картинки" in nav_bar_menu, "'Картинки' is not presented in main page"

    def go_to_picture_page(self):
        picture_link = self.browser.find_element(*YandexMainPageLocators.PICTURE_LINK_LOCATOR)
        picture_link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])




