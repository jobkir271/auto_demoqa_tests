import allure
from playwright.sync_api import Page, expect


class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.output_block = page.locator(".border.col-md-12.col-sm-12")

    @allure.step("Fill text box form")
    def fill_text_box(self, name, email, current_address, permanent_address):
        self.page.get_by_placeholder("Full Name").fill(name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Current Address").fill(current_address)
        self.page.locator("textarea#permanentAddress").fill(permanent_address)
        self.page.get_by_role("button", name="Submit").click()

    @allure.step("Check output block visible")
    def check_output_visible(self):
        expect(self.output_block).to_be_visible()

    @allure.step("Check output block hidden")
    def check_output_hidden(self):
        expect(self.output_block).to_be_hidden()