import allure

from playwright.sync_api import Page,expect
from pages.widgets.auto_complete_page import AutoCompletePage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking auto complete")
@allure.severity(allure.severity_level.NORMAL)
def test_auto_complete(test_auto_complete: Page):
    page = test_auto_complete
    auto = AutoCompletePage(page)

    with allure.step("Select Red and Green (multiple)"):
        auto.select_multiple_color("Red")
        auto.select_multiple_color("Green")

    with allure.step("Verify multiple colors"):
        tags = auto.get_multiple_tags()
        expect(tags.nth(0)).to_have_text("Red")
        expect(tags.nth(1)).to_have_text("Green")

    with allure.step("Select Purple (single)"):
        auto.select_single_color("Purple")

    with allure.step("Verify single color"):
        expect(auto.get_single_tag()).to_have_text("Purple")


