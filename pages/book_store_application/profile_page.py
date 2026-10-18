import allure
from playwright.sync_api import Page, expect


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Verify book '{title}' is in profile")
    def verify_book_in_profile(self, title):
        self.page.wait_for_timeout(5000)
        expect(self.page.locator("table tbody")).to_contain_text(title)

    @allure.step("Delete book with ISBN: {isbn}")
    def delete_book(self, isbn):
        self.page.locator(f"#delete-record-{isbn}").click()
        self.page.locator("#closeSmallModal-ok").click()

    @allure.step("Verify book '{title}' is removed from profile")
    def verify_book_deleted(self, title):
        expect(self.page.locator("table tbody")).not_to_contain_text(title)