import pytest
from pages.main_page import MainPage
from pages.forms_page import AlertsFrameAndWindows

@pytest.fixture
def browser_windows_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_alerts_frame_and_windows()
    form = AlertsFrameAndWindows(page)
    form.click_browser_windows()
    return page
