import allure
from playwright.sync_api import Page, expect


class BrowserWindowsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open new page via button: {button_name}")
    def open_new_page(self, button_name):
        with self.page.context.expect_page() as new_page_info:
            self.page.get_by_role("button", name=f"{button_name}").first.click()
        return new_page_info.value

    @allure.step("Check new page body contains: {text}")
    def check_new_page_text(self, new_page, text):
        expect(new_page.locator("body")).to_contain_text(text)