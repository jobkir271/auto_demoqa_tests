import allure
from playwright.sync_api import Page, expect


class AutoCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.multiple_input = page.locator("#autoCompleteMultipleInput")
        self.single_input = page.locator("#autoCompleteSingleInput")
        self.multi_value_label = page.locator(".auto-complete__multi-value__label.css-9jq23d")
        self.single_value = page.locator(".auto-complete__single-value.css-1dimb5e-singleValue")

    @allure.step("Select Red and Green (multiple)")
    def select_red_and_green(self):
        self.multiple_input.fill("Red")
        self.page.get_by_text("Red", exact=True).click()
        self.multiple_input.fill("Green")
        self.page.get_by_text("Green", exact=True).click()

    @allure.step("Verify multiple colors")
    def check_multiple_colors(self):
        expect(self.multi_value_label.nth(0)).to_have_text("Red")
        expect(self.multi_value_label.nth(1)).to_have_text("Green")

    @allure.step("Select Purple (single)")
    def select_purple(self):
        self.single_input.fill("Purple")
        self.page.get_by_text("Purple", exact=True).click()

    @allure.step("Verify single color")
    def check_single_color(self):
        expect(self.single_value).to_have_text("Purple")