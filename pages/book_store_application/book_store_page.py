import allure
from playwright.sync_api import Page, expect


class BookStorePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Go to Book Store")
    def open_book_store(self):
        self.page.get_by_role("button", name="Go To Book Store").click()

    @allure.step("Verify books list is not empty")
    def verify_books_list_not_empty(self):
        expect(self.page.locator("table tbody tr")).not_to_have_count(0)

    @allure.step("Search for book: '{title}'")
    def search_book(self, title):
        self.page.locator("#searchBox").fill(title)

    @allure.step("Verify results contain '{title}'")
    def verify_results_contain(self, title):
        expect(self.page.locator("table tbody")).to_contain_text(title)

    @allure.step("Open book '{title}'")
    def open_book(self, title):
        self.page.get_by_role("link", name=title).click()

    @allure.step("Add book to collection and go to Profile")
    def add_to_collection(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Add To Your Collection").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("link", name="Profile").click()