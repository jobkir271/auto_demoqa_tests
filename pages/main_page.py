from pages.base_page import BasePage

class MainPage(BasePage):

    def click_forms(self):
        self.page.get_by_role('link', name="Forms").click()

    def click_alerts_frame_and_windows(self):
        self.page.get_by_role('link', name="Alerts, Frame & Windows").click()

    def click_elements(self):
        self.page.get_by_role('link', name="Elements").click()

    def click_widgets(self):
        self.page.get_by_role('link', name = "widgets").click()

