import allure
from playwright.sync_api import Page, expect

class TabPage:
    def __init__(self, page: Page):
        self.page = page
        self.what_tab = page.get_by_role("tab", name="What")
        self.origin_tab = page.get_by_role("tab", name="Origin")
        self.use_tab = page.get_by_role("tab", name="Use")
        self.more_tab = page.get_by_role("tab", name="More")

        self.what_panel = page.locator("#demo-tabpane-what")
        self.origin_panel = page.locator("#demo-tabpane-origin")
        self.use_panel = page.locator("#demo-tabpane-use")
        self.more_panel = page.locator("#demo-tabpane-more")

    @allure.step("Check initial state: What visible, others hidden")
    def check_initial_state(self):
        expect(self.what_panel).to_be_visible()
        expect(self.origin_panel).to_be_hidden()
        expect(self.use_panel).to_be_hidden()
        expect(self.more_panel).to_be_hidden()

    @allure.step("Click Origin tab")
    def click_origin_tab(self):
        self.origin_tab.click()
        expect(self.what_panel).to_be_hidden()
        expect(self.origin_panel).to_be_visible()
        expect(self.use_panel).to_be_hidden()
        expect(self.more_panel).to_be_hidden()

    @allure.step("Click Use tab")
    def click_use_tab(self):
        self.use_tab.click()
        expect(self.what_panel).to_be_hidden()
        expect(self.origin_panel).to_be_hidden()
        expect(self.use_panel).to_be_visible()
        expect(self.more_panel).to_be_hidden()

    @allure.step("Check that More tab is disabled")
    def check_more_tab_disabled(self):
        expect(self.more_tab).to_be_disabled()