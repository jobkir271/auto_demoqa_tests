import allure

from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.forms_page import Elements
from pages.elements.check_buttons_page import ButtonsPage

@allure.epic("demoqa_tests")
@allure.feature("buttons")
@allure.story("Checking button presses")
@allure.severity(allure.severity_level.NORMAL)

def test_buttons(page: Page):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
        main.click_elements()
    with allure.step("Go to the tab Elements"):
        forms = Elements(page)
        forms.click_buttons()
    with allure.step("pressing a buttons"):
        buttons_test = ButtonsPage(page)
        buttons_test.pressing_buttons()

    with allure.step("Check the button presses"):
        expect(page.locator("#doubleClickMessage")).to_contain_text("You have done a double click")
        expect(page.locator("#rightClickMessage")).to_contain_text("You have done a right click")
        expect(page.locator("#dynamicClickMessage")).to_contain_text("You have done a dynamic click")


