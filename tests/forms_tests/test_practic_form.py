import pytest
import allure
from pages.forms.practice_form_page import PracticeFormPage

@pytest.mark.smoke
@pytest.mark.parametrize(
    "form_data,expected_success",
    [
        (("Andrey", "Vararpaev", "hello22@gmial.com", "8999555555", "06 Jun 1901",
          "Maths", [1, 2], "235 Station Road, Aberystwyth, NP23 5ET, Wales",
          "NCR", "Noida"), True),
        (("Андрей", "Варапаев", "hel@yandex.ru", "122231113213", "20 Jun 2125",
          "E", [1, 3], "г.Москва, ул.Красный, д.11",
          "Haryana", "Karnal"), True),
        (("ООО", "ООО", "HHH@yandex.ru", "0000000000000000", "01 Jun 1800",
          "E", [3], "ООО", "Uttar Pradesh", "Lucknow"), True),
        (("ООО", "ООО", "HHH@яндекс.ру", "+79236525587", "03 Jun 2025",
          "E", [3], "ООО", "Uttar Pradesh", "Lucknow"), False),
    ],
    ids=["valid", "cyrillic", "long-mobile", "invalid-email"]
)
@allure.epic("demoqa_tests")
@allure.feature("practic_form")
@allure.story("Filling out the form")
@allure.severity(allure.severity_level.NORMAL)
def test_practic_form(test_practice_form, form_data, expected_success):
    form = PracticeFormPage(test_practice_form)
    form.fill_form(form_data)
    form.check_form_result(expected_success)