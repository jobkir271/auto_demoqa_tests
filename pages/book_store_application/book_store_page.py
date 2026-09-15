import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class BookStorePage(BasePage):

    @allure.step("Go to Book Store")
    def open_book_store(self):
        self.page.get_by_role("button", name="Go To Book Store").click()

    @allure.step("Verify books list is not empty")
    def verify_books_list_not_empty(self):
        expect(self.page.locator("table tbody tr")).not_to_have_count(0)

    @allure.step("Search for book: '{title}'")
    def search_book(self, title: str):
        self.page.locator("#searchBox").fill(title)
        self.page.wait_for_timeout(3000)

    @allure.step("Verify results contain '{title}'")
    def verify_results_contain(self, title: str):
        expect(self.page.locator("table tbody")).to_contain_text(title)