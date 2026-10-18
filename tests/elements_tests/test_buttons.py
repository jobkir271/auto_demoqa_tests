import allure
from pages.elements.buttons_page import ButtonsPage


@allure.epic("demoqa_tests")
@allure.feature("buttons")
@allure.story("Checking button presses")
@allure.severity(allure.severity_level.NORMAL)
def test_buttons(test_buttons):
    buttons = ButtonsPage(test_buttons)
    buttons.pressing_buttons()
    buttons.check_double_click_message()
    buttons.check_right_click_message()
    buttons.check_dynamic_click_message()