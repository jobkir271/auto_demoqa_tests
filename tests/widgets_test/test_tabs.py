import allure

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking tabs")
@allure.severity(allure.severity_level.NORMAL)
def test_tabstools(test_tab: Page):
    page = test_tab
    what_tab = page.get_by_role("tab", name ="What")
    origin_tab = page.get_by_role("tab", name ="Origin")
    use_tab = page.get_by_role("tab", name ="Use")
    more_tab = page.get_by_role("tab", name ="More")

    what_panel = page.locator("#demo-tabpane-what")
    origin_panel = page.locator("#demo-tabpane-origin")
    use_panel = page.locator("#demo-tabpane-use")
    more_panel = page.locator("#demo-tabpane-more")

    with allure.step("Check initial state: What visible, others hidden"):
        expect(what_panel).to_be_visible()
        expect(origin_panel).to_be_hidden()
        expect(use_panel).to_be_hidden()
        expect(more_panel).to_be_hidden()
    with allure.step("Click Origin tab"):
        origin_tab.click()
        expect(what_panel).to_be_hidden()
        expect(origin_panel).to_be_visible()
        expect(use_panel).to_be_hidden()
        expect(more_panel).to_be_hidden()
    with allure.step("Click Use tab"):
        use_tab.click()
        expect(what_panel).to_be_hidden()
        expect(origin_panel).to_be_hidden()
        expect(use_panel).to_be_visible()
        expect(more_panel).to_be_hidden()
    with allure.step("Check that More tab is disabled"):
        expect(more_tab).to_be_disabled()