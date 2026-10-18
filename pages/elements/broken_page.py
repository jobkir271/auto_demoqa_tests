import allure
from playwright.sync_api import Page, expect

class BrokenPage:
    def __init__(self, page: Page):
        self.page = page
        self.valid_image = page.locator("img[src='/images/Toolsqa.jpg']")
        self.broken_image = page.locator("img[src='/images/Toolsqa_1.jpg']")
        self.valid_link = page.get_by_role("link", name="Click Here for Valid Link")
        self.broken_link = page.get_by_role("link", name="Click Here for Broken Link")

    @allure.step("Check valid image is broken (width=0)")
    def check_valid_image_broken(self):
        width = self.valid_image.evaluate("el => el.naturalWidth")
        assert width == 0, f"Expected width 0, got {width}"

    @allure.step("Check broken image width=0")
    def check_broken_image(self):
        width = self.broken_image.evaluate("el => el.naturalWidth")
        assert width == 0, f"Expected width 0, got {width}"

    @allure.step("Click valid link and check URL")
    def click_valid_link_and_check(self):
        self.valid_link.click()
        expect(self.page).to_have_url("https://demoqa.com/")
        self.page.go_back()

    @allure.step("Check broken link href")
    def check_broken_link_href(self):
        href = self.broken_link.get_attribute("href")
        assert href == "http://the-internet.herokuapp.com/status_codes/500", f"Wrong href: {href}"