import pytest
import allure
from pages.elements.radio_button_page import RadioButtonPage

@allure.epic("demoqa_tests")
@allure.feature("radio_button")
@allure.story("Filling in radio button")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "text, radio_id",
    [
        ("Yes", "#yesRadio"),
        ("Impressive", "#impressiveRadio"),
    ]
)
def test_radio_button(test_radio_button, text, radio_id):
    radio = RadioButtonPage(test_radio_button)
    radio.click_radio(radio_id)
    radio.check_selected_text(text)
    radio.check_no_radio_disabled()