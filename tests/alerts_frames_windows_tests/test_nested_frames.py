import allure

from playwright.sync_api import expect

@allure.epic("demoqa_tests")
@allure.feature("nested frames")
@allure.story("Catching text in nested frames")
@allure.severity(allure.severity_level.NORMAL)
def test_nested_frames(browser_windows_page):
    with allure.step("Opening a tab with nested frames"):
        page = browser_windows_page
        page.locator('a[href="/nestedframes"]').click()
    with allure.step("Checking text in nested frames"):
        expect(page.frame_locator("#frame1").locator("body")).to_have_text(" Parent frame ")
        expect(page.frame_locator("#frame1").frame_locator("iframe").locator("body")).to_have_text("Child Iframe")


