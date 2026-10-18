import allure
from playwright.sync_api import Page


class DragabblePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Switch to Axis Restricted tab")
    def switch_to_axis_restricted(self):
        self.page.get_by_role("tab", name="Axis Restricted").click()
        self.page.wait_for_timeout(10000)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(5000)

    @allure.step("Switch to Container Restricted tab")
    def switch_to_container_restricted(self):
        self.page.get_by_role("tab", name="Container Restricted").click()
        self.page.wait_for_timeout(10000)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(5000)

    @allure.step("Switch to Cursor Style tab")
    def switch_to_cursor_style(self):
        self.page.get_by_role("tab", name="Cursor Style").click()
        self.page.wait_for_timeout(10000)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(5000)

    @allure.step("Drag element 150px right and 80px down")
    def drag_simple(self):
        drag = self.page.locator("#dragBox")
        drag.scroll_into_view_if_needed()
        self.page.wait_for_timeout(10000)
        box = drag.bounding_box()
        start_x = box['x'] + box['width'] / 2
        start_y = box['y'] + box['height'] / 2
        self.page.mouse.move(start_x, start_y)
        self.page.mouse.down()
        self.page.mouse.move(start_x + 150, start_y + 80)
        self.page.mouse.up()
        self.page.wait_for_timeout(10000)
        new_box = drag.bounding_box()
        assert new_box["x"] != box["x"]

    @allure.step("Drag element horizontally")
    def drag_axis_x(self):
        drag = self.page.locator("#restrictedX")
        drag.scroll_into_view_if_needed()
        drag.wait_for(state="visible")
        self.page.wait_for_timeout(5000)
        box = drag.bounding_box()
        if box is not None:
            self.page.wait_for_timeout(10000)
            drag.hover()
            self.page.mouse.down()
            self.page.mouse.move(box["x"] + 150, box["y"])
            self.page.mouse.up()
            self.page.wait_for_timeout(10000)
        new_box = drag.bounding_box()
        if new_box is not None and box is not None:
            assert new_box["x"] != box["x"]
            assert new_box["y"] == box["y"]

    @allure.step("Drag element vertically")
    def drag_axis_y(self):
        drag = self.page.locator("#restrictedY")
        drag.scroll_into_view_if_needed()
        drag.wait_for(state="visible")
        self.page.wait_for_timeout(5000)
        box = drag.bounding_box()
        if box is not None:
            self.page.wait_for_timeout(10000)
            drag.hover()
            self.page.mouse.down()
            self.page.mouse.move(box["x"], box["y"] + 150)
            self.page.mouse.up()
            self.page.wait_for_timeout(10000)
        new_box = drag.bounding_box()
        if new_box is not None and box is not None:
            assert new_box["y"] != box["y"]
            assert new_box["x"] == box["x"]

    @allure.step("Drag element beyond container limits")
    def drag_container_box(self):
        drag = self.page.locator("#containmentWrapper .draggable.ui-widget-content")
        drag.scroll_into_view_if_needed()
        drag.wait_for(state="visible")
        self.page.wait_for_timeout(5000)
        box = drag.bounding_box()
        drag.hover()
        self.page.mouse.down()
        self.page.mouse.move(box["x"] + 500, box["y"] + 500)
        self.page.mouse.up()
        new_box = drag.bounding_box()
        assert new_box["x"] >= box["x"]
        assert new_box["y"] != box["y"]

    @allure.step("Drag element within parent")
    def drag_container_parent(self):
        drag = self.page.locator('.draggable.ui-widget-content.m-3 .ui-widget-header ')
        drag.scroll_into_view_if_needed()
        drag.wait_for(state="visible")
        self.page.wait_for_timeout(5000)
        box = drag.bounding_box()
        drag.hover()
        self.page.mouse.down()
        self.page.mouse.move(box["x"] + 100, box["y"] + 100)
        self.page.mouse.up()
        new_box = drag.bounding_box()
        assert new_box["x"] >= box["x"]
        assert new_box["y"] >= box["y"]

    @allure.step("Drag all cursor style elements")
    def drag_cursor_style(self):
        drag_center = self.page.locator('#cursorCenter')
        drag_top_left = self.page.locator('#cursorTopLeft')
        drag_bottom = self.page.locator('#cursorBottom')
        drag_center.scroll_into_view_if_needed()
        drag_center.wait_for(state="visible")
        drag_top_left.wait_for(state="visible")
        drag_bottom.wait_for(state="visible")
        self.page.wait_for_timeout(5000)
        box_center = drag_center.bounding_box()
        box_top_left = drag_top_left.bounding_box()
        box_bottom = drag_bottom.bounding_box()

        drag_center.hover()
        self.page.mouse.down()
        self.page.mouse.move(box_center["x"] + 100, box_center["y"] + 100)
        self.page.mouse.up()
        new_box = drag_center.bounding_box()
        assert new_box["x"] >= box_center["x"]

        drag_top_left.hover()
        self.page.mouse.down()
        self.page.mouse.move(box_top_left["x"] + 100, box_top_left["y"] + 100)
        self.page.mouse.up()
        new_box = drag_top_left.bounding_box()
        assert new_box["x"] >= box_top_left["x"]

        drag_bottom.hover()
        self.page.mouse.down()
        self.page.mouse.move(box_bottom["x"] + 100, box_bottom["y"] + 100)
        self.page.mouse.up()
        new_box = drag_bottom.bounding_box()
        assert new_box["x"] >= box_bottom["x"]