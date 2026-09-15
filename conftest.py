import pytest
from pages.main_page import MainPage
from pages.forms_page import AlertsFrameAndWindows, Elements, WidgetsPage, InteractionsPage, BookStoreApplicationPage
from playwright.sync_api import expect


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
def interactions_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_interactions()
    return page

@pytest.fixture
def bsa_page(page):
    main = MainPage(page)
    main.open("https://demoqa.com/")
    main.click_book_store_application()
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

@pytest.fixture
def test_date_picker(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_date_picker()
    return widgets_page

@pytest.fixture
def test_slider(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_slider()
    return widgets_page

@pytest.fixture
def test_progress_bar(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_progress_bar()
    return widgets_page

@pytest.fixture
def test_tab(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_tabs()
    return widgets_page

@pytest.fixture
def test_tool_tips(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_tool_tips()
    return widgets_page

@pytest.fixture
def test_menu(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_menu()
    return widgets_page

@pytest.fixture
def test_menu_select(widgets_page):
    form = WidgetsPage(widgets_page)
    form.click_select_menu()
    return widgets_page

@pytest.fixture
def test_sortable(interactions_page):
    form = InteractionsPage(interactions_page)
    form.click_sortable()
    return interactions_page

@pytest.fixture
def test_selectable(interactions_page):
    form = InteractionsPage(interactions_page)
    form.click_selectable()
    return interactions_page

@pytest.fixture
def test_resizable(interactions_page):
    form = InteractionsPage(interactions_page)
    form.click_resizable()
    return interactions_page

@pytest.fixture
def test_droppable(interactions_page):
    form = InteractionsPage(interactions_page)
    form.click_droppable()
    return interactions_page

@pytest.fixture
def test_dragabble(interactions_page):
    form = InteractionsPage(interactions_page)
    form.click_dragabble()
    return interactions_page

@pytest.fixture
def test_login(bsa_page):
    form = BookStoreApplicationPage(bsa_page)
    form.click_login()
    return bsa_page

@pytest.fixture
def logged_in_page(page):
    page.goto("https://demoqa.com/login")
    page.get_by_placeholder("UserName").fill("Ara271")
    page.get_by_placeholder("Password").fill("889134509963Zx*")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Logout")).to_be_visible(timeout=15000)
    return page