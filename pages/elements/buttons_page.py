import allure
from playwright.sync_api import Page, expect


class ButtonsPage:
    def __init__(self, page: Page):
        self.page = page
        self.double_click_message = page.locator("#doubleClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.dynamic_click_message = page.locator("#dynamicClickMessage")

    @allure.step("Pressing buttons: double, right, dynamic")
    def pressing_buttons(self):
        self.page.get_by_role("button", name="Double Click Me").dblclick()
        self.page.get_by_role("button", name="Right Click Me").click(button="right")
        self.page.get_by_role("button", name="Click Me", exact=True).click()

    @allure.step("Check double click message")
    def check_double_click_message(self):
        expect(self.double_click_message).to_contain_text("You have done a double click")

    @allure.step("Check right click message")
    def check_right_click_message(self):
        expect(self.right_click_message).to_contain_text("You have done a right click")

    @allure.step("Check dynamic click message")
    def check_dynamic_click_message(self):
        expect(self.dynamic_click_message).to_contain_text("You have done a dynamic click")