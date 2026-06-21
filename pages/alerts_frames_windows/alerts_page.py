import pytest
from pages.base_page import BasePage

class AlertsPage(BasePage):

    def alert_processing_base(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.locator("#alertButton").click()

    def alert_processing_delay(self):
        with self.page.expect_event("dialog") as event_info:
            self.page.locator("#timerAlertButton").click()
        dialog = event_info.value
        assert dialog.message == "This alert appeared after 5 seconds"
        dialog.accept()

    def confirm_processing(self,action:str):
        handler = lambda dialog: dialog.accept() if action == "accept" else dialog.dismiss()
        self.page.once("dialog", handler)
        self.page.locator("#confirmButton").click()


    def prompt_processing(self,text:str):
        self.page.on('dialog', lambda dialog: dialog.accept(text))
        self.page.locator("#promtButton").click()

