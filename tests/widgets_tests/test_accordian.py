import allure

from playwright.sync_api import Page,expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("Checking accordian")
@allure.severity(allure.severity_level.NORMAL)
def test_accordian(test_accordian: Page):
    with allure.step("Get buttons by text"):
        page = test_accordian
        first_button = page.get_by_role("button", name = "What is Lorem Ipsum?")
        second_button = page.get_by_role("button", name = "Where does it come from?")
    with allure.step("Check initial state"):
        expect(first_button).to_have_attribute("aria-expanded", "true")
        expect(second_button).to_have_attribute("aria-expanded", "false")
    with allure.step("Click second button"):
        second_button.click()
    with allure.step("Check states after click"):
        expect(first_button).to_have_attribute("aria-expanded", "false")
        expect(second_button).to_have_attribute("aria-expanded", "true")
