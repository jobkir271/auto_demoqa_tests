import allure

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking menu>menu")
@allure.severity(allure.severity_level.NORMAL)
def test_menu(test_menu):
    page = test_menu
    with allure.step("Hover on Main Item 2"):
        page.locator("ul#nav > li:nth-child(2) > a").hover()
        sub_item_2 = page.locator("ul#nav > li:nth-child(2) > ul")
        expect(sub_item_2).to_be_visible()
    with allure.step("Hover on SUB SUB LIST"):
        page.locator("ul#nav > li:nth-child(2) > ul > li:last-child > a").hover()
        sub_sub_item = page.locator("ul#nav > li:nth-child(2) > ul > li:last-child > ul")
        expect(sub_sub_item).to_be_visible()


