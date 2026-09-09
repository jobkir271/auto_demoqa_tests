import re
import allure

from playwright.sync_api import expect

@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("Checking simple")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_simple(test_droppable):
    page = test_droppable
    with allure.step("Switch to Simple tab"):
        page.get_by_role("tab", name="Simple").click()
    drag = page.locator("#draggable")
    drop = page.locator("#droppableExample-tabpane-simple #droppable")
    with allure.step("Wait a bit and drag element"):
        page.wait_for_timeout(500)
        drag.drag_to(drop)
    with allure.step("Verify drop text changed to 'Dropped!'"):
        expect(drop).to_have_text("Dropped!")

@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("Checking accept")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_accept(test_droppable):
    page = test_droppable
    with allure.step("Switch to Accept tab"):
        page.get_by_role("tab", name="Accept").click()
    drop = page.locator("#acceptDropContainer .drop-box")
    acceptable = page.locator("#acceptable")
    with allure.step("Drag Acceptable element to drop zone"):
        page.wait_for_timeout(500)
        acceptable.drag_to(drop)
        page.wait_for_timeout(500)
    with allure.step("Verify drop zone contains 'Dropped!'"):
        expect(drop).to_have_text("Dropped!")

@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking not acceptable")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_not_accept(test_droppable):
    page = test_droppable
    with allure.step("Switch to Accept tab"):
        page.get_by_role("tab", name="Accept").click()
    drop = page.locator("#acceptDropContainer .drop-box")
    not_acceptable = page.locator("#acceptDropContainer .drag-box").nth(1)
    with allure.step("Drag Not Acceptable element to drop zone"):
        page.wait_for_timeout(500)
        not_acceptable.drag_to(drop)
    with allure.step("Verify drop zone still shows 'Drop here'"):
        expect(drop).to_have_text("Drop here")

@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking prevent propagation")
@allure.severity(allure.severity_level.NORMAL)
def test_droppable_prevent_propogation(test_droppable):
    page = test_droppable
    with allure.step("Switch to Prevent Propogation tab"):
        page.get_by_role("tab", name="Prevent Propogation").click()
    drag = page.locator("#dragBox")
    outer_not_greedy = page.locator("#notGreedyDropBox")
    inner_not_greedy = page.locator("#notGreedyInnerDropBox")
    with allure.step("Drag to inner not greedy drop zone"):
        page.wait_for_timeout(500)
        drag.drag_to(inner_not_greedy)
    with allure.step("Verify both outer and inner got highlight"):
        expect(outer_not_greedy).to_have_class(re.compile(r"ui-state-highlight"))
        expect(inner_not_greedy).to_have_class(re.compile(r"ui-state-highlight"))
    with allure.step("Reload and switch back to Prevent Propogation"):
        page.reload()
        page.get_by_role("tab", name="Prevent Propogation").click()
    drag = page.locator("#dragBox")
    outer_greedy = page.locator("#greedyDropBox")
    inner_greedy = page.locator("#greedyDropBoxInner")
    with allure.step("Drag to inner greedy drop zone"):
        page.wait_for_timeout(500)
        drag.drag_to(inner_greedy)
    with allure.step("Verify only inner got highlight"):
        expect(outer_greedy).not_to_have_class(re.compile(r"ui-state-highlight"))
        expect(inner_greedy).to_have_class(re.compile(r"ui-state-highlight"))

@allure.epic("demoqa_tests")
@allure.feature("droppable")
@allure.story("checking revert draggable")
def test_droppable_revert_draggable(test_droppable):
    page = test_droppable
    with allure.step("Switch to Revert Draggable tab"):
        page.get_by_role("tab", name="Revert Draggable").click()
    drop = page.locator("#revertableDropContainer .drop-box")
    revertable = page.locator("#revertable")
    not_revertable = page.locator("#notRevertable")
    with allure.step("Get initial positions"):
        revertable_box = revertable.bounding_box()
        not_revertable_box = not_revertable.bounding_box()
        revertable_x = revertable_box["x"]
        not_revertable_x = not_revertable_box["x"]
    with allure.step("Drag revertable element and check it returns"):
        page.wait_for_timeout(500)
        revertable.drag_to(drop)
        page.wait_for_timeout(500)
        new_revertable_box = revertable.bounding_box()
        assert new_revertable_box["x"] == revertable_x
    with allure.step("Drag not revertable element and check it does not return"):
        page.wait_for_timeout(500)
        not_revertable.drag_to(drop)
        page.wait_for_timeout(500)
        new_not_revertable_box = not_revertable.bounding_box()
        assert new_not_revertable_box["x"] != not_revertable_x



