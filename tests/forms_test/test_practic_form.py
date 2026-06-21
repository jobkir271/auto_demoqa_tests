import pytest
import allure
from playwright.sync_api import Page,expect
from pages.forms.practice_form_page import PracticeFormPage
from pages.forms_page import FormsPage
from pages.main_page import MainPage

@pytest.mark.parametrize(
    "first_name,last_name,email,mobile,date,subject,number_hobby,address,state,city,expected_success",
    [
        ("Andrey", "Vararpaev", "hello22@gmial.com", "8999555555", "06 Jun 1901",
          "Maths", [1, 2], "235 Station Road, Aberystwyth, NP23 5ET, Wales",
         "NCR", "Noida", True),
        ("Андрей", "Варапаев", "hel@yandex.ru", "122231113213", "20 Jun 2125",
                  "E", [1, 3], "г.Москва, ул.Красный, д.11",
                 "Haryana", "Karnal", True),
        ("ООО", "ООО", "HHH@yandex.ru", "0000000000000000", "01 Jun 1800",
                  "E", [3], "ООО", "Uttar Pradesh", "Lucknow", True),
        ("ООО", "ООО", "HHH@яндекс.ру", "+79236525587", "03 Jun 2025",
                  "E", [3], "ООО", "Uttar Pradesh", "Lucknow", False),

    ]
)
@allure.epic("demoqa_tests")
@allure.feature("practic_form")
@allure.story("Filling out the form")
@allure.severity(allure.severity_level.NORMAL)
def test_practic_form(page: Page,first_name,last_name,email,mobile,date,subject,
                      number_hobby,address,state,city,expected_success):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
        main.click_forms()
    with allure.step("Go to the tab Form"):
        forms = FormsPage(page)
        forms.click_practice_form()

    form = PracticeFormPage(page)
    form.fill_form(
        first_name=first_name,
        last_name=last_name,
        date=date,
        email=email,
        mobile=mobile,
        subject=subject,
        number_hobby=number_hobby,
        file_set="resources/file_test.txt",
        address=address,
        state=state,
        city= city,
    )
    with allure.step("Negative and positive test check"):
        if expected_success:
            expect(page.locator(".modal-content")).to_be_visible()
            page.wait_for_timeout(4000)
            # input("Press Enter to continue...")
            page.keyboard.press("Escape")
            page.wait_for_timeout(500)
        else:
            # input("Press Enter to continue...")
            expect(page.locator(".modal-content")).to_be_hidden()
            #input("Press Enter to continue...")
            page.wait_for_timeout(4000)


