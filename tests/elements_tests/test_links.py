import pytest
import allure

from playwright.sync_api import Page,expect

@pytest.mark.parametrize("tab_link", ["#simpleLink","#dynamicLink"])
def test_home_link_new_tab(test_links ,tab_link):
    with allure.step(f"Click link {tab_link} and switch to new tab"):
        page = test_links
        with page.context.expect_page() as new_page_info:
            page.locator(tab_link).click()
        new_page = new_page_info.value
    with allure.step("Check that new tab URL is correct"):
        expect(new_page).to_have_url("https://demoqa.com/")

@pytest.mark.parametrize("link_text, expected_code", [
    ("Created", 201),
    ("No Content", 204),
    ("Moved", 301),
    ("Bad Request", 400),
    ("Unauthorized", 401),
    ("Forbidden", 403),
    ("Not Found", 404),
])
def test_api_links(test_links,link_text,expected_code):
    with allure.step(f"Click link {link_text}"):
        page = test_links
        page.get_by_role("link", name=link_text).click()
    with allure.step(f"Check that response contains status {expected_code}"):
        expect(page.locator("#linkResponse")).to_contain_text(str(expected_code))