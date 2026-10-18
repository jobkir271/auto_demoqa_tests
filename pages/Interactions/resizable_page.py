import allure
from playwright.sync_api import Page


class ResizablePage:
    def __init__(self, page: Page):
        self.page = page
        self.limited_box = page.locator("#resizableBoxWithRestriction")
        self.limited_handle = self.limited_box.locator(".react-resizable-handle")
        self.unlimited_box = page.locator("#resizable")
        self.unlimited_handle = self.unlimited_box.locator(".react-resizable-handle")

    @allure.step("Drag limited box handle to resize")
    def resize_limited_box(self):
        initial_width = self.limited_box.evaluate("el => el.offsetWidth")
        initial_height = self.limited_box.evaluate("el => el.offsetHeight")
        self.limited_handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(initial_width + 200, initial_height + 100)
        self.page.mouse.up()
        new_width = self.limited_box.evaluate("el => el.offsetWidth")
        new_height = self.limited_box.evaluate("el => el.offsetHeight")
        assert initial_width != new_width
        assert initial_height != new_height
        assert new_width <= 500
        assert new_height <= 300

    @allure.step("Drag unlimited box handle to resize")
    def resize_unlimited_box(self):
        initial_width = self.unlimited_box.evaluate("el => el.offsetWidth")
        initial_height = self.unlimited_box.evaluate("el => el.offsetHeight")
        self.unlimited_handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(initial_width + 300, initial_height + 300)
        self.page.mouse.up()
        new_width = self.unlimited_box.evaluate("el => el.offsetWidth")
        new_height = self.unlimited_box.evaluate("el => el.offsetHeight")
        assert initial_width != new_width
        assert initial_height != new_height