import allure
from playwright.sync_api import Page, expect


class SortablePage:
    def __init__(self, page: Page):
        self.page = page
        self.grid_tab = page.locator("#demo-tab-grid")
        self.grid_items = page.locator("#demo-tabpane-grid .list-group-item")
        self.list_items = page.locator("#demo-tabpane-list .list-group-item")

    @allure.step("Switch to Grid tab")
    def switch_to_grid(self):
        self.grid_tab.click()

    @allure.step("Check initial order in Grid")
    def check_grid_initial_order(self):
        expect(self.grid_items.nth(0)).to_have_text("One")
        expect(self.grid_items.nth(1)).to_have_text("Two")

    @allure.step("Drag 'One' to the position of 'Two' in Grid")
    def drag_grid_one_to_two(self):
        self.grid_items.nth(0).drag_to(self.grid_items.nth(1))

    @allure.step("Verify new order in Grid")
    def check_grid_new_order(self):
        expect(self.grid_items.nth(0)).to_have_text("Two")
        expect(self.grid_items.nth(1)).to_have_text("One")

    @allure.step("Check initial order in List")
    def check_list_initial_order(self):
        expect(self.list_items.nth(0)).to_have_text("One")
        expect(self.list_items.nth(1)).to_have_text("Two")

    @allure.step("Drag 'One' to the position of 'Two' in List")
    def drag_list_one_to_two(self):
        self.list_items.nth(0).drag_to(self.list_items.nth(1), target_position={"x": 20, "y": 40})

    @allure.step("Verify new order in List")
    def check_list_new_order(self):
        expect(self.list_items.nth(0)).to_have_text("Two")
        expect(self.list_items.nth(1)).to_have_text("One")