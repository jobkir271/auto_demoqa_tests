import pytest
import allure

from pages.forms_page import Elements
from pages.main_page import MainPage
from playwright.sync_api import Page,expect

@pytest.mark.parametrize(
"text, radio_id",
[
    ("Yes","#yesRadio"),
    ("Impressive","#impressiveRadio"),

]
)

@allure.epic("demoqa_tests")
@allure.feature("radio_button")
@allure.story("Filling in radio button")
@allure.severity(allure.severity_level.NORMAL)

def test_radio_button(page: Page, text, radio_id ):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
        main.click_elements()
    with allure.step("Go to the tab Elements"):
        form = Elements(page)
        form.click_radio_button()
    with allure.step("Click radio button"):
        page.locator(radio_id).click()
    with allure.step("checking that the No button is not displayed"):
        expect(page.locator("p.mt-3")).to_contain_text(f"You have selected {text}")
        expect(page.locator("#noRadio")).to_be_disabled()



