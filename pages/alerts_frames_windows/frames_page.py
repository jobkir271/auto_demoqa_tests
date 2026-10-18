import allure
from playwright.sync_api import Page, expect


class FramesPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_link = page.locator('a[href="/frames"]')
        self.frame1_body = page.frame_locator("#frame1").locator("body")
        self.frame2_body = page.frame_locator("#frame2").locator("body")

    @allure.step("Open frames tab")
    def open_frames_tab(self):
        self.menu_link.click()

    @allure.step("Check frame 1 text")
    def check_frame1_text(self):
        expect(self.frame1_body).to_have_text("This is a sample page")

    @allure.step("Check frame 2 text")
    def check_frame2_text(self):
        expect(self.frame2_body).to_have_text("This is a sample page")