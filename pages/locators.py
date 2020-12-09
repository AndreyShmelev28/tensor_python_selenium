from selenium.webdriver.common.by import By


class YandexMainPageLocators:
    SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "#text")
    SUGGESTION_TABLE_LOCATOR = (By.CSS_SELECTOR, "[role=listbox]")
    NAV_BAR_LOCATOR = (By.CSS_SELECTOR, ".services-new__item-title")
    PICTURE_LINK_LOCATOR = (By.CSS_SELECTOR, '[data-statlog="services_new.item.images.1"]')
    WORD_FOR_SEARCHING = "Тензор"


class YandexSearchResultsPageLocators:
    RESULT_LINK_LOCATOR = (By.CSS_SELECTOR, '[class="path organic__path"] .link b')


class YandexPicturesCategoryLocators:
    PICTURE_CATEGORY_LOCATOR = (By.CSS_SELECTOR, ".ImagesList .PopularRequestList-Item")
    #TITLE_IN_PICTURE_LOCATOR = (By.CSS_SELECTOR, '[name="description"]')
    PICTURE_LOCATOR = (By.CSS_SELECTOR, '.serp-item__link')
    PICTURE_SOURCE_LOCATOR = (By.CSS_SELECTOR, ".MMImage-Origin")
    NEXT_PICTURE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".CircleButton_type_next")
    PREVIOUS_PICTURE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".CircleButton_type_prev")

