import allure

from playwright.sync_api import Page,expect

@allure.epic("demoqa_tests")
@allure.feature("frames")
@allure.story("Catching frames")
@allure.severity(allure.severity_level.NORMAL)
def test_frames(page:Page,browser_windows_page:Page):
    with allure.step("Opening a tab with frames"):
        page = browser_windows_page
        page.locator('a[href="/frames"]').click()
    with allure.step("Checking text in frames"):
        expect(page.frame_locator("#frame1").locator("body")).to_have_text("This is a sample page")
        expect(page.frame_locator("#frame2").locator("body")).to_have_text("This is a sample page")

