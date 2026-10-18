import allure
from playwright.sync_api import Page, expect


class LinksPage:
    def __init__(self, page: Page):
        self.page = page
        self.response = page.locator("#linkResponse")

    @allure.step("Click link {tab_link} and check new tab URL")
    def click_and_check_new_tab(self, tab_link):
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(tab_link).click()
        new_page = new_page_info.value
        expect(new_page).to_have_url("https://demoqa.com/")

    @allure.step("Click link {link_text} and check status {expected_code}")
    def click_and_check_api_link(self, link_text, expected_code):
        self.page.get_by_role("link", name=link_text).click()
        expect(self.response).to_contain_text(str(expected_code))