import allure

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking simple drag")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_simple(test_dragabble):
    page = test_dragabble
    with allure.step("Get draggable element and scroll to it"):
        drag = page.locator("#dragBox")
        drag.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
    with allure.step("Get initial position"):
        box = drag.bounding_box()
        start_x = box['x'] + box['width'] / 2
        start_y = box['y'] + box['height'] / 2
    with allure.step("Drag element 150px right and 80px down"):
        page.mouse.move(start_x, start_y)
        page.mouse.down()
        page.mouse.move(start_x + 150, start_y + 80)
        page.mouse.up()
        page.wait_for_timeout(1000)
    with allure.step("Check that position changed"):
        new_box = drag.bounding_box()
        assert new_box["x"] != box["x"]

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking axis restricted X")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_axis_x(test_dragabble):
    page = test_dragabble
    with allure.step("Switch to Axis Restricted tab"):
        page.get_by_role("tab", name="Axis Restricted").click()
    with allure.step("Get X-restricted element"):
        drag = page.locator("#restrictedX")
        box = drag.bounding_box()
    if box is not None:
        with allure.step("Drag element horizontally"):
            page.wait_for_timeout(1000)
            drag.hover()
            page.mouse.down()
            page.mouse.move(box["x"] + 150, box["y"])
            page.mouse.up()
            page.wait_for_timeout(1000)
    with allure.step("Check X changed, Y unchanged"):
        new_box = drag.bounding_box()
        if new_box is not None and box is not None:
            assert new_box["x"] != box["x"]
            assert new_box["y"] == box["y"]

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking axis restricted Y")
@allure.severity(allure.severity_level.NORMAL)
def test_dragabble_axis_y(test_dragabble):
    page = test_dragabble
    with allure.step("Switch to Axis Restricted tab"):
        page.get_by_role("tab", name="Axis Restricted").click()
    with allure.step("Get Y-restricted element"):
        drag = page.locator("#restrictedY")
        box = drag.bounding_box()
    if box is not None:
        with allure.step("Drag element vertically"):
            page.wait_for_timeout(1000)
            drag.hover()
            page.mouse.down()
            page.mouse.move(box["x"], box["y"] + 150)
            page.mouse.up()
            page.wait_for_timeout(1000)
    with allure.step("Check Y changed, X unchanged"):
        new_box = drag.bounding_box()
        if new_box is not None and box is not None:
            assert new_box["y"] != box["y"]
            assert new_box["x"] == box["x"]

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking container restricted within box")
@allure.severity(allure.severity_level.NORMAL)
def test_container_restricted_box(test_dragabble):
    page = test_dragabble
    with allure.step("Switch to Container Restricted tab"):
        page.get_by_role("tab", name="Container Restricted").click()
    with allure.step("Get element and drag beyond limits"):
        drag = page.locator("#containmentWrapper .draggable.ui-widget-content")
        box = drag.bounding_box()
        drag.hover()
        page.mouse.down()
        page.mouse.move(box["x"] + 500, box["y"] + 500)
        page.mouse.up()
    with allure.step("Check position is limited"):
        new_box = drag.bounding_box()
        assert new_box["x"] >= box["x"]
        assert new_box["y"] != box["y"]

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking container restricted within parent")
@allure.severity(allure.severity_level.NORMAL)
def test_container_restricted_parent(test_dragabble):
    page = test_dragabble
    with allure.step("Switch to Container Restricted tab"):
        page.get_by_role("tab", name="Container Restricted").click()
    with allure.step("Get element and drag it"):
        drag = page.locator('.draggable.ui-widget-content.m-3 .ui-widget-header ')
        box = drag.bounding_box()
        drag.hover()
        page.mouse.down()
        page.mouse.move(box["x"] + 100, box["y"] + 100)
        page.mouse.up()
    with allure.step("Check position changed within limits"):
        new_box = drag.bounding_box()
        assert new_box["x"] >= box["x"]
        assert new_box["y"] >= box["y"]

@allure.epic("demoqa_tests")
@allure.feature("dragabble")
@allure.story("checking cursor style")
@allure.severity(allure.severity_level.NORMAL)
def test_cursor_style(test_dragabble):
    page = test_dragabble
    with allure.step("Switch to Cursor Style tab"):
        page.get_by_role("tab", name="Cursor Style").click()
    with allure.step("Get all draggable elements"):
        drag_center = page.locator('#cursorCenter')
        drag_top_left = page.locator('#cursorTopLeft')
        drag_bottom = page.locator('#cursorBottom')
        box_center = drag_center.bounding_box()
        box_top_left = drag_top_left.bounding_box()
        box_bottom = drag_bottom.bounding_box()
    with allure.step("Drag center element"):
        drag_center.hover()
        page.mouse.down()
        page.mouse.move(box_center["x"] + 100, box_center["y"] + 100)
        page.mouse.up()
        new_box = drag_center.bounding_box()
        assert new_box["x"] >= box_center["x"]
    with allure.step("Drag top-left element"):
        drag_top_left.hover()
        page.mouse.down()
        page.mouse.move(box_top_left["x"] + 100, box_top_left["y"] + 100)
        page.mouse.up()
        new_box = drag_top_left.bounding_box()
        assert new_box["x"] >= box_top_left["x"]
    with allure.step("Drag bottom element"):
        drag_bottom.hover()
        page.mouse.down()
        page.mouse.move(box_bottom["x"] + 100, box_bottom["y"] + 100)
        page.mouse.up()
        new_box = drag_bottom.bounding_box()
        assert new_box["x"] >= box_bottom["x"]
