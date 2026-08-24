import allure

from playwright.sync_api import expect, Page

@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking dynamic text")
@allure.severity(allure.severity_level.NORMAL)
def test_dynamic_text(test_dynamic: Page):
    with allure.step("Check text with random ID is visible"):
        page = test_dynamic
        expect(page.get_by_text("This text has random Id")).to_contain_text("This text has random Id")

@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking enable buttons")
@allure.severity(allure.severity_level.NORMAL)
def test_enable_buttons(test_dynamic: Page):
    with allure.step("Check button is disabled initially"):
        page = test_dynamic
        enabled_page = page.get_by_role("button", name="Will enable 5 seconds")
        expect(enabled_page).to_be_disabled()
    with allure.step("Wait for button to become enabled"):
        page.wait_for_timeout(5000)
        expect(enabled_page).to_be_enabled()

@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking color button")
@allure.severity(allure.severity_level.NORMAL)
def test_color_button(test_dynamic: Page):
    with allure.step("Get initial color"):
        page = test_dynamic
        color_button = page.get_by_role("button", name="Color Change")
        before_color = color_button.evaluate("el => getComputedStyle(el).color")
    with allure.step("Wait for color change"):
        page.wait_for_timeout(5000)
        after_color = color_button.evaluate("el => getComputedStyle(el).color")
    with allure.step("Assert color has changed"):
        assert before_color != after_color, "Цвет не изменился"

@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking invisible button")
@allure.severity(allure.severity_level.NORMAL)
def test_invisible_button(test_dynamic: Page):
    with allure.step("Wait for invisible button to appear"):
        page = test_dynamic
        page.wait_for_timeout(5000)
    with allure.step("Check button is visible"):
        button_invisible = page.get_by_role("button", name="Visible After 5 Seconds")
        expect(button_invisible).to_be_visible()