from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    def expand_tree(self):
        self.page.wait_for_timeout(50)
        while self.page.locator(".rc-tree-switcher.rc-tree-switcher_close").count() > 0:
            self.page.locator(".rc-tree-switcher.rc-tree-switcher_close").first.click()

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