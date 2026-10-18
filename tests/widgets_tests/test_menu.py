import allure

from pages.widgets.menu_page import MenuPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking menu>menu")
@allure.severity(allure.severity_level.NORMAL)
def test_menu(test_menu):
    menu = MenuPage(test_menu)
    menu.hover_main_item_2()
    menu.hover_sub_sub_list()

