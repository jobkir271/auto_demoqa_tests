from pages.base_page import BasePage

class ButtonsPage(BasePage):
    def pressing_buttons(self):
        self.page.get_by_role('button', name="Double Click Me").dblclick()
        self.page.get_by_role('button', name="Right Click Me").click(button='right')
        self.page.get_by_role("button", name='Click Me').last.click()


