import allure

from pages.Interactions.dragabble_page import DragabblePage

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking simple drag")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_simple(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.drag_simple()


@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking axis restricted X")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_axis_x(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.switch_to_axis_restricted()
    drag.drag_axis_x()


@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking axis restricted Y")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_axis_y(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.switch_to_axis_restricted()
    drag.drag_axis_y()


@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking container restricted within box")
@allure.severity(allure.severity_level.NORMAL)
def test_container_restricted_box(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.switch_to_container_restricted()
    drag.drag_container_box()


@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking container restricted within parent")
@allure.severity(allure.severity_level.NORMAL)
def test_container_restricted_parent(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.switch_to_container_restricted()
    drag.drag_container_parent()


@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking cursor style")
@allure.severity(allure.severity_level.NORMAL)
def test_cursor_style(test_dragabble):
    drag = DragabblePage(test_dragabble)
    drag.switch_to_cursor_style()
    drag.drag_cursor_style()