import allure

from playwright.sync_api import Page, expect

class ProgressBarPage:

    def __init__(self, page: Page):
        self.page = page
        self.start_stop_button = page.locator("#startStopButton")
        self.progress_bar = page.locator("#progressBar .progress-bar")

    @allure.step("Click Start")
    def click_start(self):
        self.page.get_by_role("button", name="Start").click()

    @allure.step("Wait for progress to reach 100%")
    def wait_for_100_percent(self):
        expect(self.progress_bar).to_have_attribute("aria-valuenow", "100", timeout=13000)

    @allure.step("Wait until progress reaches at least 50%")
    def wait_for_at_least_50_percent(self):
        self.page.wait_for_function(
            "(element) => Number(element.getAttribute('aria-valuenow')) >= 50",
            arg=self.progress_bar.element_handle()
        )

    @allure.step("Stop progress")
    def click_stop(self):
        self.start_stop_button.click()

    @allure.step("Check that stopped value is at least 50")
    def check_stopped_value(self):
        value_progress = int(self.progress_bar.get_attribute("aria-valuenow") or 0)
        assert value_progress >= 50