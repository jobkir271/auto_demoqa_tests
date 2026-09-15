import allure
from playwright.sync_api import Page,expect

@allure.epic("demoqa_tests")
@allure.feature("book_store")
@allure.story("checking login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_book_story(logged_in_page: Page):
    page = logged_in_page
    with allure.step("expect UI element,go to book story"):
        expect(page.locator("#gotoStore")).to_have_text("Go To Book Store")

