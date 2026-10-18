import allure
from playwright.sync_api import Page, expect


class CheckBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator("#result")
        self.tree_switchers = page.locator(".rc-tree-switcher.rc-tree-switcher_close")

    @allure.step("Expand tree")
    def expand_tree(self):
        self.page.wait_for_timeout(50)
        while self.tree_switchers.count() > 0:
            self.tree_switchers.first.click()

    @allure.step("Select checkboxes")
    def select_checkboxes(self, names, flags):
        selected = []
        for i in range(len(names)):
            if flags[i]:
                selected.append(names[i])
                click_name = names[i]
                if names[i] == "wordFile":
                    click_name = "Word File.doc"
                elif names[i] == "excelFile":
                    click_name = "Excel File.doc"
                self.page.get_by_role("checkbox", name=click_name).click()
        return selected

    @allure.step("Verify result contains selected items")
    def check_results(self, selected):
        for name in selected:
            expect(self.result).to_contain_text(name)