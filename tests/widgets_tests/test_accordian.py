import allure

from pages.widgets.accordian_page import AccordianPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("Checking accordian")
@allure.severity(allure.severity_level.NORMAL)
def test_accordian(test_accordian):
    accordian = AccordianPage(test_accordian)
    accordian.check_initial_state()
    accordian.click_second_button()
    accordian.check_state_after_click()