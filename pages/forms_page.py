from pages.base_page import BasePage

class FormsPage(BasePage):
    def click_practice_form(self):
        self.page.get_by_role('link', name="Practice Form").click()

