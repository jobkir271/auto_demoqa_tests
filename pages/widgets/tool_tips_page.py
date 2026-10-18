import allure
from playwright.sync_api import Page, expect

class ToolTipsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Hover over button and check tooltip")
    def hover_button_and_check_tooltip(self):
        self.page.locator('#toolTipButton').hover()
        expect(self.page.locator(".tooltip-inner:has-text('You hovered over the Button')")).to_be_visible()

    @allure.step("Hover over text field and check tooltip")
    def hover_text_field_and_check_tooltip(self):
        self.page.locator('#toolTipTextField').hover()
        expect(self.page.locator(".tooltip-inner:has-text('You hovered over the text field')")).to_be_visible()

    @allure.step("Hover over link and check tooltip")
    def hover_contrary_link_and_check_tooltip(self):
        self.page.locator("a:has-text('Contrary')").hover()
        expect(self.page.locator(".tooltip-inner:has-text('You hovered over the Contrary')")).to_be_visible()
        