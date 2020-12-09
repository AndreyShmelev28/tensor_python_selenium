from pages.base_page import BasePage
from pages.locators import YandexPicturesCategoryLocators


class PictureCategoryPage(BasePage):

    def check_is_url_correct(self):
        assert "https://yandex.ru/images/" in self.browser.current_url, "Incorrect url for pictures category"

    def get_name_of_first_category(self):
        name_of_category = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_CATEGORY_LOCATOR)
        return name_of_category.text

    def get_picture_src(self):
        picture = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_SOURCE_LOCATOR)
        src = picture.get_attribute("src")
        return str(src)


    def open_first_category(self):
        picture_category = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_CATEGORY_LOCATOR)
        picture_category.click()


    def open_first_picture(self):
        link = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_LOCATOR)
        link.click()

    def click_on_next_picture_button(self):
        button = self.browser.find_element(*YandexPicturesCategoryLocators.NEXT_PICTURE_BUTTON_LOCATOR)
        button.click()

    def click_on_previous_picture_button(self):
        button = self.browser.find_element(*YandexPicturesCategoryLocators.PREVIOUS_PICTURE_BUTTON_LOCATOR)
        button.click()

    def should_be_another_picture(self, first_picture_src):
        second_picture = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_SOURCE_LOCATOR)
        second_picture_src = second_picture.get_attribute("src")
        assert first_picture_src != str(second_picture_src), "It is same pictures"

    def should_be_same_picture(self, first_picture_before_click_next_src):
        first_picture_after_click_previous = self.browser.find_element(*YandexPicturesCategoryLocators.PICTURE_SOURCE_LOCATOR)
        first_picture_after_click_previous_src = str(first_picture_after_click_previous.get_attribute("src"))
        assert first_picture_before_click_next_src == first_picture_after_click_previous_src, "It is another picture"


