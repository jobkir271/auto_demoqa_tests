import pytest
import allure
from pages.elements.link_page import LinksPage


@pytest.mark.parametrize("tab_link", ["#simpleLink", "#dynamicLink"])
@allure.epic("demoqa_tests")
@allure.feature("links")
@allure.story("Checking new tab")
@allure.severity(allure.severity_level.NORMAL)
def test_home_link_new_tab(test_links, tab_link):
    links = LinksPage(test_links)
    links.click_and_check_new_tab(tab_link)


@pytest.mark.parametrize("link_text, expected_code", [
    ("Created", 201),
    ("No Content", 204),
    ("Moved", 301),
    ("Bad Request", 400),
    ("Unauthorized", 401),
    ("Forbidden", 403),
    ("Not Found", 404),
])
@allure.epic("demoqa_tests")
@allure.feature("links")
@allure.story("Checking API links")
@allure.severity(allure.severity_level.NORMAL)
def test_api_links(test_links, link_text, expected_code):
    links = LinksPage(test_links)
    links.click_and_check_api_link(link_text, expected_code)