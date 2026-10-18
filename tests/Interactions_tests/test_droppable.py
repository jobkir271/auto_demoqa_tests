import allure
from pages.Interactions.droppable_page import DroppablePage


@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("Checking simple")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_simple(test_droppable):
    droppable = DroppablePage(test_droppable)
    droppable.switch_to_simple()
    droppable.drag_simple()


@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("Checking accept")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_accept(test_droppable):
    droppable = DroppablePage(test_droppable)
    droppable.switch_to_accept()
    droppable.drag_acceptable()


@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking not acceptable")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_not_accept(test_droppable):
    droppable = DroppablePage(test_droppable)
    droppable.switch_to_accept()
    droppable.drag_not_acceptable()


@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking prevent propagation")
@allure.severity(allure.severitygo_level.NORMAL)
def test_droppable_prevent_propogation(test_droppable):
    droppable = DroppablePage(test_droppable)
    droppable.switch_to_prevent_propogation()
    droppable.drag_to_inner_not_greedy()
    droppable.reload_and_switch_to_prevent_propogation()
    droppable.drag_to_inner_greedy()


@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking revert draggable")
def test_droppable_revert_draggable(test_droppable):
    droppable = DroppablePage(test_droppable)
    droppable.switch_to_revert_draggable()
    droppable.drag_revertable()
    droppable.drag_not_revertable()