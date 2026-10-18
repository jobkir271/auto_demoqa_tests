import allure
from playwright.sync_api import Page, expect


class RadioButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.result_text = page.locator("p.mt-3")
        self.no_radio = page.locator("#noRadio")

    @allure.step("Click radio button: {radio_id}")
    def click_radio(self, radio_id):
        self.page.locator(radio_id).click()

    @allure.step("Check selected text: {text}")
    def check_selected_text(self, text):
        expect(self.result_text).to_contain_text(f"You have selected {text}")

    @allure.step("Check No radio is disabled")
    def check_no_radio_disabled(self):
        expect(self.no_radio).to_be_disabled()