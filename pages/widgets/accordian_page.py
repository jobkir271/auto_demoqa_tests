import allure
from playwright.sync_api import Page, expect


class AccordianPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_button = page.get_by_role("button", name="What is Lorem Ipsum?")
        self.second_button = page.get_by_role("button", name="Where does it come from?")

    @allure.step("Check initial state")
    def check_initial_state(self):
        expect(self.first_button).to_have_attribute("aria-expanded", "true")
        expect(self.second_button).to_have_attribute("aria-expanded", "false")

    @allure.step("Click second button")
    def click_second_button(self):
        self.second_button.click()

    @allure.step("Check states after click")
    def check_state_after_click(self):
        expect(self.first_button).to_have_attribute("aria-expanded", "false")
        expect(self.second_button).to_have_attribute("aria-expanded", "true")