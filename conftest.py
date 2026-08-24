import pytest
from pages.main_page import MainPage
from pages.forms_page import AlertsFrameAndWindows
from pages.forms_page import Elements

@pytest.fixture
def browser_windows_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_alerts_frame_and_windows()
    form = AlertsFrameAndWindows(page)
    form.click_browser_windows()
    return page
@pytest.fixture

def test_web_tables(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_elements()
    forms = Elements(page)
    forms.click_web_tables()
    page.wait_for_selector("table tbody tr", state="visible")
    return page
@pytest.fixture
def test_links(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_elements()
    form = Elements(page)
    form.click_links()
    return page
@pytest.fixture
def test_broken(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_elements()
    form = Elements(page)
    form.click_broken()
    return page
