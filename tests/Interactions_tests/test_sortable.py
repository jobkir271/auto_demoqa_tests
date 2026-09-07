import allure

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("interactions")
@allure.story("checking sortable list")
@allure.severity(allure.severity_level.NORMAL)
def test_sortable_grid(test_sortable: Page):
    page = test_sortable
    with allure.step("Switch to Grid tab"):
        page.locator("#demo-tab-grid").click()

    grid_items = page.locator("#demo-tabpane-grid .list-group-item")

    with allure.step("Check initial order in Grid"):
        expect(grid_items.nth(0)).to_have_text("One")
        expect(grid_items.nth(1)).to_have_text("Two")
    with allure.step("Drag 'One' to the position of 'Two'"):
        grid_items.nth(0).drag_to(grid_items.nth(1))
    with allure.step("Verify new order in Grid"):
        expect(grid_items.nth(0)).to_have_text("Two")
        expect(grid_items.nth(1)).to_have_text("One")

@allure.epic("demoqa_tests")
@allure.feature("interactions")
@allure.story("checking sortable grid")
@allure.severity(allure.severity_level.NORMAL)
def test_sortable_list(test_sortable:Page):
    page = test_sortable
    items = page.locator("#demo-tabpane-list .list-group-item")
    with allure.step("Check initial order in List"):
        expect(items.nth(0)).to_have_text("One")
        expect(items.nth(1)).to_have_text("Two")
    with allure.step("Drag 'One' to the position of 'Two'"):
        items.nth(0).drag_to(items.nth(1), target_position={"x": 20, "y": 40})
    with allure.step("Verify new order in List"):
        expect(items.nth(0)).to_have_text("Two")
        expect(items.nth(1)).to_have_text("One")



