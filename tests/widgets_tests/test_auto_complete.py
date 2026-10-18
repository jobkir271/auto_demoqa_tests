import allure
from pages.widgets.auto_complete_page import AutoCompletePage


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking auto complete")
@allure.severity(allure.severity_level.NORMAL)
def test_auto_complete(test_auto_complete):
    auto = AutoCompletePage(test_auto_complete)
    auto.select_red_and_green()
    auto.check_multiple_colors()
    auto.select_purple()
    auto.check_single_color()