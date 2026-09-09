import allure

from playwright.sync_api import Page

@allure.epic("demoqa_tests")
@allure.feature("resizable")
@allure.story("checking limited box")
@allure.severity(allure.severity_level.NORMAL)
def test_resizable_limited(test_resizable:Page):
    page = test_resizable
    with allure.step("Get box and handle"):
        box = page.locator("#resizableBoxWithRestriction")
        handle = box.locator(".react-resizable-handle")
    with allure.step("Get initial size"):
        initial_width = box.evaluate("el => el.offsetWidth")
        initial_height = box.evaluate("el => el.offsetHeight")
    with allure.step("Drag handle to resize"):
        handle.hover()
        page.mouse.down()
        page.mouse.move(initial_width + 200, initial_height + 100)
        page.mouse.up()
    with allure.step("Get new size"):
        new_width = box.evaluate("el => el.offsetWidth")
        new_height = box.evaluate("el => el.offsetHeight")
    with allure.step("Verify size changed and within limits"):
        assert initial_width != new_width
        assert initial_height != new_height
        assert new_width <= 500
        assert new_height <= 300

@allure.epic("demoqa_tests")
@allure.feature("resizable")
@allure.story("checking unlimited box")
@allure.severity(allure.severity_level.NORMAL)
def test_resizable_unlimited(test_resizable:Page):
    page = test_resizable
    with allure.step("Get box and handle"):
        box = page.locator("#resizable")
        handle = box.locator(".react-resizable-handle")
    with allure.step("Get initial size"):
        initial_width = box.evaluate("el => el.offsetWidth")
        initial_height = box.evaluate("el => el.offsetHeight")
    with allure.step("Drag handle to resize"):
        handle.hover()
        page.mouse.down()
        page.mouse.move(initial_width + 300, initial_height + 300)
        page.mouse.up()
    with allure.step("Get new size"):
        new_width = box.evaluate("el => el.offsetWidth")
        new_height = box.evaluate("el => el.offsetHeight")
    with allure.step("Verify size changed"):
        assert initial_width != new_width
        assert initial_height != new_height


