import pytest
import allure
from pages.elements.text_box_page import TextBoxPage


@pytest.mark.parametrize(
    "name, email, current_address, permanent_address, expected_success",
    [
        ("Kirill", "dsa@gmail.com", "text", "text", True),
        ("Danila", "dasd@da.com", "te3t", "1234", True),
        ("213", "", "", "", True),
        ("кит", "", "123", "море", True),
        ("", "", "", "", False),
    ]
)
@allure.epic("demoqa_tests")
@allure.feature("text_box")
@allure.story("Filling out the form")
@allure.severity(allure.severity_level.NORMAL)
def test_check_box(test_check_box, name, email, current_address, permanent_address, expected_success):
    box = TextBoxPage(test_check_box)
    box.fill_text_box(name, email, current_address, permanent_address)
    if expected_success:
        box.check_output_visible()
    else:
        box.check_output_hidden()