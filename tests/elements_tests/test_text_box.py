import pytest
import allure
from pages.elements.text_box_page import TextBoxPage
from pages.forms_page import Elements
from pages.main_page import MainPage
from playwright.sync_api import Page,expect

@pytest.mark.parametrize(
"name, email, current_address, permanent_address,expected_success",
 [
    ("Kirill", "dsa@gmail.com", "text", "text",True),
    ("Danila", "dasd@da.com", "te3t", "1234",True ),
    ("213", "", "", "",True ),
    ("кит", "", "123", "море",True ),
    ("", "", "", "",False )


 ]
)
@allure.epic("demoqa_tests")
@allure.feature("text_box")
@allure.story("Filling out the form")
@allure.severity(allure.severity_level.NORMAL)

def test_text_box(page: Page,name,email,current_address,permanent_address,expected_success):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
        main.click_elements()
    with allure.step("Go to the tab Elements"):
        form = Elements(page)
        form.click_text_box()
    with allure.step("form filling"):
        new_page = TextBoxPage(page)
        new_page.fill_text_box(name,email,current_address,permanent_address)
    with allure.step("Negative and positive test check"):
        if expected_success:
            expect(page.locator(".border.col-md-12.col-sm-12")).to_be_visible()
        else:
            expect(page.locator(".border.col-md-12.col-sm-12")).to_be_hidden()