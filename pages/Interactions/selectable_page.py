import re
import allure
from playwright.sync_api import Page, expect


class SelectablePage:
    def __init__(self, page: Page):
        self.page = page
        self.list_items = page.locator("#verticalListContainer li")
        self.grid_tab = page.get_by_role("tab", name="Grid")
        self.grid_items = page.locator("#gridContainer li")

    @allure.step("Select first and fourth list items")
    def select_list_first_and_fourth(self):
        self.list_items.nth(0).click()
        self.list_items.nth(3).click()

    @allure.step("Verify list selection")
    def check_list_selection(self):
        expect(self.list_items.nth(0)).to_have_class(re.compile(r"active"))
        expect(self.list_items.nth(1)).not_to_have_class(re.compile(r"active"))
        expect(self.list_items.nth(2)).not_to_have_class(re.compile(r"active"))
        expect(self.list_items.nth(3)).to_have_class(re.compile(r"active"))

    @allure.step("Switch to Grid tab")
    def switch_to_grid(self):
        self.grid_tab.click()

    @allure.step("Select grid items 1, 5, 9")
    def select_grid_1_5_9(self):
        self.grid_items.nth(0).click()
        self.grid_items.nth(4).click()
        self.grid_items.nth(8).click()

    @allure.step("Verify grid selection")
    def check_grid_selection(self):
        expect(self.grid_items.nth(0)).to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(1)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(2)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(3)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(4)).to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(5)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(6)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(7)).not_to_have_class(re.compile(r"active"))
        expect(self.grid_items.nth(8)).to_have_class(re.compile(r"active"))