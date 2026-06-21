from pages.base_page import BasePage

class MainPage(BasePage):
    def click_forms(self):
        self.page.get_by_role('link', name="Forms").click()
        