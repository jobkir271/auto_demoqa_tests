import allure
from pages.base_page import BasePage
from playwright.sync_api import expect

class BookStorePage(BasePage):
    @allure.step("go to Book Store")
    def open_book_store(self):
        self.page.get_by_role("button", name="Go To Book Store").click()

    @allure.step("Search for book: '{title}'")
    def search_book(self,title):
        self.page.locator("#searchBox").fill(title)

    @allure.step("Open first book in results")
    def open_first_book(self):
        self.page.locator(".action-buttons a").click()

    @allure.step("Add book to collection and go to Profile")
    def add_to_collection(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Add To Your Collection").click()
        self.page.wait_for_timeout(1000)  # ждём завершения операции
        self.page.get_by_role("link", name="Profile").click()

class ProfilePage(BasePage):

    @allure.step("Verify book '{title}' is in profile")
    def verify_book_in_profile(self, title: str):
        self.page.wait_for_timeout(5000)
        expect(self.page.locator("table tbody tr")).to_contain_text(title)

    @allure.step("Delete book with ISBN: {isbn}")
    def delete_book(self, isbn: str):
        self.page.locator(f"#delete-record-{isbn}").click()
        self.page.locator("#closeSmallModal-ok").click()

    @allure.step("Verify book '{title}' is removed from profile")
    def verify_book_deleted(self, title: str):
        expect(self.page.locator("table tbody")).not_to_contain_text(title)