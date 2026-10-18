import allure
from playwright.sync_api import Page,expect

class MenuPage:

    def __init__(self, page: Page):
        self.page = page
        self.main_item_2 = page.locator("ul#nav > li:nth-child(2) > a")
        self.sub_item_2 = page.locator("ul#nav > li:nth-child(2) > ul")
        self.sub_sub_list_link = page.locator("ul#nav > li:nth-child(2) > ul > li:last-child > a")
        self.sub_sub_item = page.locator("ul#nav > li:nth-child(2) > ul > li:last-child > ul")

    @allure.step("Hover on Main Item 2")
    def hover_main_item_2(self):
        self.main_item_2.hover()
        expect(self.sub_item_2).to_be_visible()

    @allure.step("Hover on SUB SUB LIST")
    def hover_sub_sub_list(self):
        self.sub_sub_list_link.hover()
        expect(self.sub_sub_list_link).to_be_visible()
