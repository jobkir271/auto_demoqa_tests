import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage

@allure.epic("demoqa_tests")
@allure.feature("login")
@allure.story("login test")
@allure.severity("CRITICAL")
def test_login(page: Page):
     main = MainPage(page)
     with allure.step("Login to the site"):
          main.open("https://demoqa.com/")
     with allure.step("Checking that you are logged in to the site"):
          expect(page).to_have_title("demosite")

