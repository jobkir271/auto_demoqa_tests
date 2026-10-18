import allure
from pages.Interactions.sortable_page import SortablePage


@allure.epic("demoqa_tests")
@allure.feature("interactions")
@allure.story("checking sortable list")
@allure.severity(allure.severity_level.NORMAL)
def test_sortable_grid(test_sortable):
    sortable = SortablePage(test_sortable)
    sortable.switch_to_grid()
    sortable.check_grid_initial_order()
    sortable.drag_grid_one_to_two()
    sortable.check_grid_new_order()


@allure.epic("demoqa_tests")
@allure.feature("interactions")
@allure.story("checking sortable grid")
@allure.severity(allure.severity_level.NORMAL)
def test_sortable_list(test_sortable):
    sortable = SortablePage(test_sortable)
    sortable.check_list_initial_order()
    sortable.drag_list_one_to_two()
    sortable.check_list_new_order()