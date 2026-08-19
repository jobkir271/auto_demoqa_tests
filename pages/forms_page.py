from pages.base_page import BasePage

class FormsPage(BasePage):
    def click_practice_form(self):
        self.page.get_by_role('link', name="Practice Form").click()

class AlertsFrameAndWindows(BasePage):
    def click_alerts(self):
        self.page.get_by_role('link', name="Alerts").click()
    def click_browser_windows(self):
        self.page.get_by_role('link', name="Browser Windows").click()

class Elements(BasePage):
    def click_text_box(self):
        self.page.get_by_role('link', name="Text Box").click()
    def click_check_box(self):
        self.page.get_by_role('link', name="Check Box").click()
    def click_radio_button(self):
        self.page.get_by_role('link', name="Radio Button").click()
    def click_buttons(self):
        self.page.get_by_role('link', name="Buttons").click()
    def click_web_tables(self):
        self.page.get_by_role('link', name = "Web Tables").click()
    def click_links(self):
        self.page.get_by_role('link', name = "Links", exact=True).click()
