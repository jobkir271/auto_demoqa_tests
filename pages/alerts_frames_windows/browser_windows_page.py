from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):

    def open_new_page(self,button_name):
        with self.page.context.expect_page() as new_page_info:
            self.page.get_by_role("button", name=f"{button_name}").first.click()
        new_page = new_page_info.value
        return new_page