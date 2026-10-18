import allure
from playwright.sync_api import Page, expect


class DynamicPropertiesPage:
    def __init__(self, page: Page):
        self.page = page
        self.random_text = page.get_by_text("This text has random Id")
        self.enable_button = page.get_by_role("button", name="Will enable 5 seconds")
        self.color_button = page.get_by_role("button", name="Color Change")
        self.invisible_button = page.get_by_role("button", name="Visible After 5 Seconds")

    @allure.step("Check text with random ID is visible")
    def check_random_text_visible(self):
        expect(self.random_text).to_contain_text("This text has random Id")

    @allure.step("Check button is disabled initially")
    def check_button_disabled(self):
        expect(self.enable_button).to_be_disabled()

    @allure.step("Wait for button to become enabled")
    def check_button_enabled_after_wait(self):
        self.page.wait_for_timeout(5000)
        expect(self.enable_button).to_be_enabled()

    @allure.step("Check color changes after wait")
    def check_color_changes(self):
        before_color = self.color_button.evaluate("el => getComputedStyle(el).color")
        self.page.wait_for_timeout(5000)
        after_color = self.color_button.evaluate("el => getComputedStyle(el).color")
        assert before_color != after_color, "Color did not change"

    @allure.step("Wait and check invisible button becomes visible")
    def check_invisible_button_appears(self):
        self.page.wait_for_timeout(5000)
        expect(self.invisible_button).to_be_visible()