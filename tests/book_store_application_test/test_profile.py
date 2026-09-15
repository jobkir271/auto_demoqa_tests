import allure
from playwright.sync_api import Page, expect

from pages.book_store_application.profile_page import BookStorePage, ProfilePage


@allure.epic("demoqa_tests")
@allure.feature("book_store")
@allure.story("checking add book to profile")
@allure.severity(allure.severity_level.NORMAL)
def test_add_book_to_profile(logged_in_page: Page):
    page = logged_in_page
    store = BookStorePage(page)
    profile = ProfilePage(page)

    store.open_book_store()
    store.search_book("You")
    store.open_book("You Don't Know JS")
    store.add_to_collection()

    profile.verify_book_in_profile("You")
    profile.delete_book("9781491904244")
    profile.verify_book_deleted("You")


