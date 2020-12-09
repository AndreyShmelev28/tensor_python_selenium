
from pages.main_page import MainPage
from pages.picture_category_page import PictureCategoryPage




link_yandex_main_page = "https://yandex.ru/"


def test_pictures_on_yandex(browser):
    main_page = MainPage(browser, link_yandex_main_page)
    main_page.open()
    main_page.should_be_pictures_category_on_nav_bar()
    main_page.go_to_picture_page()
    picture_category_page = PictureCategoryPage(browser, browser.current_url)
    picture_category_page.check_is_url_correct()
    picture_category_page.open_first_category()
    picture_category_page.open_first_picture()
    first_picture_before_click_next_src = picture_category_page.get_picture_src()
    picture_category_page.click_on_next_picture_button()
    picture_category_page.should_be_another_picture(first_picture_before_click_next_src)
    picture_category_page.click_on_previous_picture_button()
    picture_category_page.should_be_same_picture(first_picture_before_click_next_src)



