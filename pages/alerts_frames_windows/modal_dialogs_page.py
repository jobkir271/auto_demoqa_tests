import allure
from playwright.sync_api import Page, expect


class ModalDialogsPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_link = page.locator('a[href="/modal-dialogs"]')

    @allure.step("Open Modal Dialogs tab")
    def open_modal_dialogs_tab(self):
        self.menu_link.click()

    @allure.step("Click button: {button_name}")
    def click_modal_button(self, button_name):
        self.page.get_by_role("button", name=button_name).click()

    @allure.step("Check modal text and close with Escape")
    def check_modal_text_and_close(self, class_button, text_modal):
        expect(self.page.locator(class_button)).to_contain_text(text_modal)
        self.page.keyboard.press("Escape")