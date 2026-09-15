import allure
from playwright.sync_api import Page
from pages.book_store_application.book_store_page import BookStorePage


@allure.epic("demoqa_tests")
@allure.feature("book_store")
@allure.story("checking book store list")
@allure.severity(allure.severity_level.NORMAL)
def test_book_store_has_books(logged_in_page: Page):
    page = logged_in_page
    store = BookStorePage(page)

    store.open_book_store()
    store.verify_books_list_not_empty()


@allure.epic("demoqa_tests")
@allure.feature("book_store")
@allure.story("checking book search")
@allure.severity(allure.severity_level.NORMAL)
def test_search_book(logged_in_page: Page):
    page = logged_in_page
    store = BookStorePage(page)

    store.open_book_store()
    store.search_book("Git")
    store.verify_results_contain("Git")