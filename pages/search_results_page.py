from .base_page import BasePage
from pages.locators import YandexSearchResultsPageLocators


class SearchResultPage(BasePage):

    def should_be_present_link_in_range_of_results(self, r):
        list_of_links = self.browser.find_elements(*YandexSearchResultsPageLocators.RESULT_LINK_LOCATOR)
        text_list_of_links = [x.text for x in list_of_links if len(x.text) > 0]

        assert "tensor.ru" in text_list_of_links[0:r+1], "Has no 'tensor.ru' in first 5 results"
