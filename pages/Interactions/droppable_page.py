import re
import allure
from playwright.sync_api import Page, expect


class DroppablePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Switch to Simple tab")
    def switch_to_simple(self):
        self.page.get_by_role("tab", name="Simple").click()

    @allure.step("Wait a bit and drag element")
    def drag_simple(self):
        drag = self.page.locator("#draggable")
        drop = self.page.locator("#droppableExample-tabpane-simple #droppable")
        self.page.wait_for_timeout(5000)
        drag.drag_to(drop)
        expect(drop).to_have_text("Dropped!")

    @allure.step("Switch to Accept tab")
    def switch_to_accept(self):
        self.page.get_by_role("tab", name="Accept").click()

    @allure.step("Drag Acceptable element to drop zone")
    def drag_acceptable(self):
        drop = self.page.locator("#acceptDropContainer .drop-box")
        acceptable = self.page.locator("#acceptable")
        self.page.wait_for_timeout(5000)
        acceptable.drag_to(drop)
        self.page.wait_for_timeout(5000)
        expect(drop).to_have_text("Dropped!")

    @allure.step("Drag Not Acceptable element to drop zone")
    def drag_not_acceptable(self):
        drop = self.page.locator("#acceptDropContainer .drop-box")
        not_acceptable = self.page.locator("#acceptDropContainer .drag-box").nth(1)
        self.page.wait_for_timeout(5000)
        not_acceptable.drag_to(drop)
        expect(drop).to_have_text("Drop here")

    @allure.step("Switch to Prevent Propogation tab")
    def switch_to_prevent_propogation(self):
        self.page.get_by_role("tab", name="Prevent Propogation").click()

    @allure.step("Drag to inner not greedy drop zone")
    def drag_to_inner_not_greedy(self):
        drag = self.page.locator("#dragBox")
        outer_not_greedy = self.page.locator("#notGreedyDropBox")
        inner_not_greedy = self.page.locator("#notGreedyInnerDropBox")
        self.page.wait_for_timeout(5000)
        drag.drag_to(inner_not_greedy)
        expect(outer_not_greedy).to_have_class(re.compile(r"ui-state-highlight"))
        expect(inner_not_greedy).to_have_class(re.compile(r"ui-state-highlight"))

    @allure.step("Reload and switch back to Prevent Propogation")
    def reload_and_switch_to_prevent_propogation(self):
        self.page.reload()
        self.page.get_by_role("tab", name="Prevent Propogation").click()

    @allure.step("Drag to inner greedy drop zone")
    def drag_to_inner_greedy(self):
        drag = self.page.locator("#dragBox")
        outer_greedy = self.page.locator("#greedyDropBox")
        inner_greedy = self.page.locator("#greedyDropBoxInner")
        self.page.wait_for_timeout(5000)
        drag.drag_to(inner_greedy)
        expect(outer_greedy).not_to_have_class(re.compile(r"ui-state-highlight"))
        expect(inner_greedy).to_have_class(re.compile(r"ui-state-highlight"))

    @allure.step("Switch to Revert Draggable tab")
    def switch_to_revert_draggable(self):
        self.page.get_by_role("tab", name="Revert Draggable").click()

    @allure.step("Drag revertable element and check it returns")
    def drag_revertable(self):
        drop = self.page.locator("#revertableDropContainer .drop-box")
        revertable = self.page.locator("#revertable")
        revertable_x = revertable.bounding_box()["x"]
        self.page.wait_for_timeout(5000)
        revertable.drag_to(drop)
        self.page.wait_for_timeout(5000)
        new_x = revertable.bounding_box()["x"]
        assert abs(new_x - revertable_x) < 1, f"Element did not return: {new_x} != {revertable_x}"

    @allure.step("Drag not revertable element and check it does not return")
    def drag_not_revertable(self):
        drop = self.page.locator("#revertableDropContainer .drop-box")
        not_revertable = self.page.locator("#notRevertable")
        not_revertable_x = not_revertable.bounding_box()["x"]
        self.page.wait_for_timeout(5000)
        not_revertable.drag_to(drop)
        self.page.wait_for_timeout(5000)
        new_x = not_revertable.bounding_box()["x"]
        assert abs(new_x - not_revertable_x) > 1, f"Element returned but should not: {new_x} == {not_revertable_x}"