import allure
from playwright.sync_api import Page, expect


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page
        self.alert_button = page.locator("#alertButton")
        self.timer_alert_button = page.locator("#timerAlertButton")
        self.confirm_button = page.locator("#confirmButton")
        self.prompt_button = page.locator("#promtButton")
        self.confirm_result = page.locator("#confirmResult")
        self.prompt_result = page.locator("#promptResult")

    @allure.step("Process base alert")
    def alert_processing_base(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.alert_button.click()

    @allure.step("Process delayed alert")
    def alert_processing_delay(self):
        with self.page.expect_event("dialog") as event_info:
            self.timer_alert_button.click()
        dialog = event_info.value
        assert dialog.message == "This alert appeared after 5 seconds"
        dialog.accept()

    @allure.step("Process confirm with action: {action}")
    def confirm_processing(self, action):
        handler = lambda dialog: dialog.accept() if action == "accept" else dialog.dismiss()
        self.page.once("dialog", handler)
        self.confirm_button.click()

    @allure.step("Check confirm result: {ok_or_cancel}")
    def check_confirm_result(self, ok_or_cancel):
        expect(self.confirm_result).to_have_text(f"You selected {ok_or_cancel}")

    @allure.step("Process prompt with text: {text}")
    def prompt_processing(self, text):
        self.page.on("dialog", lambda dialog: dialog.accept(text))
        self.prompt_button.click()

    @allure.step("Check prompt result: {text}")
    def check_prompt_result(self, text):
        expect(self.prompt_result).to_have_text(f"You entered {text}")