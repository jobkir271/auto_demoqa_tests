import allure
from pages.elements.broken_page import BrokenPage

@allure.epic("demoqa_tests")
@allure.feature("Broken Links - Images")
@allure.story("Checking img")
@allure.severity(allure.severity_level.NORMAL)
def test_broken_image(test_broken):
    broken = BrokenPage(test_broken)
    broken.check_valid_image_broken()
    broken.check_broken_image()

@allure.epic("demoqa_tests")
@allure.feature("Broken Links - Images")
@allure.story("Checking links")
@allure.severity(allure.severity_level.NORMAL)
def test_broken_links(test_broken):
    broken = BrokenPage(test_broken)
    broken.click_valid_link_and_check()
    broken.check_broken_link_href()