import allure
from playwright.sync_api import Page, expect


class NestedFramesPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_link = page.locator('a[href="/nestedframes"]')
        self.parent_frame_body = page.frame_locator("#frame1").locator("body")
        self.child_frame_body = page.frame_locator("#frame1").frame_locator("iframe").locator("body")

    @allure.step("Open nested frames tab")
    def open_nested_frames_tab(self):
        self.menu_link.click()

    @allure.step("Check parent frame text")
    def check_parent_frame_text(self):
        expect(self.parent_frame_body).to_have_text(" Parent frame ")

    @allure.step("Check child frame text")
    def check_child_frame_text(self):
        expect(self.child_frame_body).to_have_text("Child Iframe")