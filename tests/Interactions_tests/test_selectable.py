import re
import allure

from playwright.sync_api import expect

@allure.epic("demoqa_tests")
@allure.feature("selectable")
@allure.story("checking selectable list")
@allure.severity(allure.severity_level.NORMAL)
def test_selectable_list(test_selectable):
    page = test_selectable
    with allure.step("Get list items"):
        all_selectable_list = page.locator("#verticalListContainer li")
        one_selectable_list =  all_selectable_list.nth(0)
        two_selectable_list = all_selectable_list.nth(1)
        three_selectable_list = all_selectable_list.nth(2)
        four_selectable_list = all_selectable_list.nth(3)
    with allure.step("Select first and fourth items"):
        one_selectable_list.click()
        four_selectable_list.click()
    with allure.step("Verify selection"):
        expect(one_selectable_list).to_have_class(re.compile(r"active"))
        expect(two_selectable_list).not_to_have_class(re.compile(r"active"))
        expect(three_selectable_list).not_to_have_class(re.compile(r"active"))
        expect(four_selectable_list).to_have_class(re.compile(r"active"))

@allure.epic("demoqa_tests")
@allure.feature("selectable")
@allure.story("checking selectable grid")
@allure.severity(allure.severity_level.NORMAL)
def test_selectable_grid(test_selectable):
    page = test_selectable
    with allure.step("Switch to Grid tab"):
        page.get_by_role('tab', name = "Grid").click()
    with allure.step("Get grid items"):
        all_selectable_grid = page.locator("#gridContainer li")
        one_selectable_grid = all_selectable_grid.nth(0)
        two_selectable_grid = all_selectable_grid.nth(1)
        tree_selectable_grid = all_selectable_grid.nth(2)
        four_selectable_grid = all_selectable_grid.nth(3)
        five_selectable_grid = all_selectable_grid.nth(4)
        six_selectable_grid = all_selectable_grid.nth(5)
        seven_selectable_grid = all_selectable_grid.nth(6)
        eight_selectable_grid = all_selectable_grid.nth(7)
        nine_selectable_grid = all_selectable_grid.nth(8)
    with allure.step("Select items 1, 5, 9"):
        one_selectable_grid.click()
        five_selectable_grid.click()
        nine_selectable_grid.click()
    with allure.step("Verify selection"):
        expect(one_selectable_grid).to_have_class(re.compile(r"active"))
        expect(two_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(tree_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(four_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(five_selectable_grid).to_have_class(re.compile(r"active"))
        expect(six_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(seven_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(eight_selectable_grid).not_to_have_class(re.compile(r"active"))
        expect(nine_selectable_grid).to_have_class(re.compile(r"active"))




