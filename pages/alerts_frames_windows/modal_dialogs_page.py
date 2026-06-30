from pages.base_page import BasePage


class ModalDialogsPage(BasePage):

    def cheking_modal_dialogs(self,browser_windows_page,name_button):
        self.page.locator('a[href="/modal-dialogs"]').click()
        self.page.get_by_role("button", name=name_button).click()