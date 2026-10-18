import allure
import pytest
from pages.widgets.select_menu_page import SelectMenuPage


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking select value")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    "Group 1, option 1",
    "Group 2, option 1",
    "A root option",
    "Another root option",
])
def test_select_value(test_menu_select, text_select):
    menu = SelectMenuPage(test_menu_select)
    menu.select_value_from_react(text_select)
    menu.check_single_value(text_select)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking select one")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"])
def test_select_one(test_menu_select, text_select):
    menu = SelectMenuPage(test_menu_select)
    menu.select_one(text_select)
    menu.check_single_value(text_select)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking old style menu")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", ["red", "1", "2", "3", "9", "10"])
def test_old_style_menu(test_menu_select, text_select):
    menu = SelectMenuPage(test_menu_select)
    menu.select_old_style(text_select)
    menu.check_old_style(text_select)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking test menu select")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    ("Green", "Red"),
    ("Blue",),
    ("Black", "Blue"),
    ("Red",),
])
def test_multiselect_drop_down(test_menu_select, text_select):
    menu = SelectMenuPage(test_menu_select)
    menu.select_multiple_colors(text_select)
    menu.check_multiple_colors(text_select)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking standard multi select")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    ["Volvo", "Saab"],
    ["Opel", "Audi"],
    ["Volvo", "Audi"],
])
def test_standard_multi_select(test_menu_select, text_select):
    menu = SelectMenuPage(test_menu_select)
    menu.select_cars(text_select)
    menu.check_cars_selected(text_select)