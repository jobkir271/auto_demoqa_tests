import pytest
from pages.main_page import MainPage
from pages.forms_page import AlertsFrameAndWindows, Elements, WidgetsPage


@pytest.fixture
def afw_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_alerts_frame_and_windows()
    return page

@pytest.fixture
def elements_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_elements()
    return page

@pytest.fixture
def widgets_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_widgets()
    return page

@pytest.fixture
def browser_windows_page(afw_page):
    form = AlertsFrameAndWindows(afw_page)
    form.click_browser_windows()
    return afw_page

@pytest.fixture
def test_web_tables(elements_page):
    form = Elements(elements_page)
    form.click_web_tables()
    elements_page.wait_for_selector("table tbody tr", state="visible")
    return elements_page

@pytest.fixture
def test_links(elements_page):
    form = Elements(elements_page)
    form.click_links()
    return elements_page

@pytest.fixture
def test_broken(elements_page):
    form = Elements(elements_page)
    form.click_broken()
    return elements_page

@pytest.fixture
def test_download_fix(elements_page):
    form = Elements(elements_page)
    form.click_download()
    return elements_page

@pytest.fixture
def test_dynamic(elements_page):
    form = Elements(elements_page)
    form.click_dynamic()
    return elements_page

@pytest.fixture
def test_accordian(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_accordian()
    return widgets_page

@pytest.fixture
def test_auto_complete(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_auto_complete()
    return widgets_page


