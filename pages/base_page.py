from playwright.sync_api import Page,expect

class BasePage:

    def __init__(self,page: Page):
        self.page = page
    def open(self,url: str):
        self.page.goto(url)
