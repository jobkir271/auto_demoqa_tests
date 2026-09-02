import allure

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking progress bar 100%")
@allure.severity(allure.severity_level.NORMAL)
def test_progress_bar(test_progress_bar: Page):
    page = test_progress_bar
    with allure.step("Click Start"):
        page.get_by_role("button", name="Start").click()
    with allure.step("Wait for progress to reach 100%"):
        progress = page.locator("#progressBar .progress-bar")
        expect(progress).to_have_attribute("aria-valuenow", "100",timeout=13000)

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking progress bar 50%")
@allure.severity(allure.severity_level.NORMAL)
def test_progress_bar_stop(test_progress_bar: Page):
    page = test_progress_bar
    progress = page.locator("#progressBar .progress-bar")
    with allure.step("Start progress"):
        page.get_by_role("button", name="Start").click()
    with allure.step("Wait until progress reaches at least 50%"):
        page.wait_for_function("(element) => Number(element.getAttribute('aria-valuenow')) >= 50", arg=progress.element_handle())
    with allure.step("Stop progress"):
        page.locator("#startStopButton").click()
    with allure.step("Check that stopped value is at least 50"):
        value_progress = int(progress.get_attribute("aria-valuenow") or 0)
        assert value_progress >= 50