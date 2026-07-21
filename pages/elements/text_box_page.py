from pages.base_page import BasePage

class TextBoxPage(BasePage):

    def fill_text_box(self,name,email,current_address,permanent_address):
        self.page.get_by_placeholder("Full Name").fill(name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Current Address").fill(current_address)
        self.page.locator("textarea#permanentAddress").fill(permanent_address)
        self.page.get_by_role("button", name="Submit").click()