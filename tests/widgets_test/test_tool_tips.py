import allure

from playwright.sync_api import Page,expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking tool tips")
@allure.severity(allure.severity_level.NORMAL)
def test_tool_tips_hover(test_tool_tips):
    page = test_tool_tips
    with allure.step("Hover over button and check tooltip"):
        page.locator('#toolTipButton').hover()
        expect(page.locator(".tooltip-inner:has-text('You hovered over the Button')")).to_be_visible()
    with allure.step("Hover over text field and check tooltip"):
        page.locator('#toolTipTextField').hover()
        expect(page.locator(".tooltip-inner:has-text('You hovered over the text field')")).to_be_visible()
    with allure.step("Hover over link and check tooltip"):
        page.locator("a:has-text('Contrary')").hover()
        expect(page.locator(".tooltip-inner:has-text('You hovered over the Contrary')")).to_be_visible()
