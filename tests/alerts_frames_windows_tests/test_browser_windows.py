import pytest
import allure
from pages.alerts_frames_windows.browser_windows_page import BrowserWindowsPage


@allure.epic("demoqa_tests")
@allure.feature("browser_windows")
@allure.story("Catching new page")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("button_name, text_expect", [
    ("New Tab", "This is a sample page"),
    ("New Window", "This is a sample page"),
    ("New Window Message", "Knowledge increases by sharing"),
])
def test_browser_windows(browser_windows_page, button_name, text_expect):
    main_browser = BrowserWindowsPage(browser_windows_page)
    new_page = main_browser.open_new_page(button_name)
    main_browser.check_new_page_text(new_page, text_expect)