from pages.base_page import BasePage

class FormsPage(BasePage):
    def click_practice_form(self):
        self.page.get_by_role('link', name="Practice Form").click()

class AlertsFrameAndWindows(BasePage):
    def click_alerts(self):
        self.page.get_by_role('link', name="Alerts").click()
    def click_browser_windows(self):
        self.page.get_by_role('link', name="Browser Windows").click()