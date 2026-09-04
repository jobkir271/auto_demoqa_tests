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
    def click_broken(self):
        self.page.get_by_role('link', name = "Broken Links - Images").click()
    def click_download(self):
        self.page.get_by_role('link', name = "Upload and Download").click()
    def click_dynamic(self):
        self.page.get_by_role('link', name = "Dynamic Properties").click()

class WidgetsPage(BasePage):
    def click_accordian(self):
        self.page.get_by_role('link', name = "Accordian").click()
    def click_auto_complete(self):
        self.page.get_by_role('link', name = "Auto Complete").click()
    def click_date_picker(self):
        self.page.get_by_role('link', name = "Date Picker").click()
    def click_slider(self):
        self.page.get_by_role('link', name = "Slider").click()
    def click_progress_bar(self):
        self.page.get_by_role('link', name = "Progress Bar").click()
    def click_tabs(self):
        self.page.get_by_role('link', name = "Tabs").click()
    def click_tool_tips(self):
        self.page.get_by_role('link', name = "Tool Tips").click()
    def click_menu(self):
        self.page.get_by_role('link', name = "Menu", exact=True).click()
    def click_select_menu(self):
        self.page.get_by_role('link', name = "Select Menu", exact=True).click()
