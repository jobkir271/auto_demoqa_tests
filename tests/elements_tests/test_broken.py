import allure

from playwright.sync_api import expect

@allure.epic("demoqa_tests")
@allure.feature("Broken Links - Images")
@allure.story("Checking img")
@allure.severity(allure.severity_level.NORMAL)
def test_broken_image(test_broken):
    with allure.step("Open broken page"):
        page = test_broken
    with allure.step("Check valid image(broken) width"):
        valid = page.locator("img[src='/images/Toolsqa.jpg']")
        valid_width = valid.evaluate("el => el.naturalWidth")

        assert valid_width == 0,f"Ожидалась ширина 0, получено {valid_width}"
    with allure.step("Check broken image width"):
        broken = page.locator("img[src='/images/Toolsqa_1.jpg']")
        broken_width = broken.evaluate("el => el.naturalWidth")

    assert broken_width == 0,f"Ожидалась ширина 0, получено {broken_width}"

@allure.epic("demoqa_tests")
@allure.feature("Broken Links - Images")
@allure.story("Checking links")
@allure.severity(allure.severity_level.NORMAL)
def test_broken_links(test_broken):
    with allure.step("Open broken page"):
        page = test_broken
    with allure.step("Click valid link and check URL"):
        page.get_by_role('link', name="Click Here for Valid Link").click()
        expect(page).to_have_url("https://demoqa.com/")
        page.go_back()
    with allure.step("Check broken link href"):
        broken_link = page.get_by_role('link', name="Click Here for Broken Link")
        href = broken_link.get_attribute("href")
        assert href == "http://the-internet.herokuapp.com/status_codes/500", \
            f"Неверный href: {href}"