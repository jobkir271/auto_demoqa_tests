import allure
from pages.widgets.tab_page import TabPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking tabs")
@allure.severity(allure.severity_level.NORMAL)
def test_tabstools(test_tab):
    tabs = TabPage(test_tab)
    tabs.check_initial_state()
    tabs.click_origin_tab()
    tabs.click_use_tab()
    tabs.check_more_tab_disabled()

