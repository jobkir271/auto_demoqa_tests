import allure
from pages.Interactions.selectable_page import SelectablePage


@allure.epic("demoqa_tests")
@allure.feature("selectable")
@allure.story("checking selectable list")
@allure.severity(allure.severity_level.NORMAL)
def test_selectable_list(test_selectable):
    selectable = SelectablePage(test_selectable)
    selectable.select_list_first_and_fourth()
    selectable.check_list_selection()


@allure.epic("demoqa_tests")
@allure.feature("selectable")
@allure.story("checking selectable grid")
@allure.severity(allure.severity_level.NORMAL)
def test_selectable_grid(test_selectable):
    selectable = SelectablePage(test_selectable)
    selectable.switch_to_grid()
    selectable.select_grid_1_5_9()
    selectable.check_grid_selection()