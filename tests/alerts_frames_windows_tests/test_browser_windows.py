import pytest
import allure

from playwright.sync_api import expect
from pages.alerts_frames_windows.browser_windows_page import BrowserWindowsPage

@allure.epic("demoqa_tests")
@allure.feature("browser_windows")
@allure.story("Catching new page")
@allure.severity(allure.severity_level.NORMAL)

@pytest.mark.parametrize("button_name, text_expect",
    [("New Tab","This is a sample page"),
     ("New Window","This is a sample page"),
     ("New Window Message","Knowledge increases by sharing")
     ])
def test_browser_windows(browser_windows_page, button_name, text_expect):
    with allure.step("fixture, which opens the Browser Windows"):
        page = browser_windows_page
    with allure.step("Processing of three buttons that open new windows"):
        main_browser = BrowserWindowsPage(page)
        new_page = main_browser.open_new_page(button_name)
    with allure.step("checking that there is text on the new page"):
        expect(new_page.locator("body")).to_contain_text(f"{text_expect}")

