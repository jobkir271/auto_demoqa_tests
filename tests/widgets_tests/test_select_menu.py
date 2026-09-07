import allure
import pytest

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking select value")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    ("Group 1, option 1"),
    ("Group 2, option 1"),
    ("A root option"),
    ("Another root option")             ])
def test_select_value(test_menu_select: Page, text_select):
    page = test_menu_select
    with allure.step(f"Open dropdown and select '{text_select}'"):
        page.locator("#react-select-2-input").click()
        page.get_by_text(text_select,exact=True).click()
    with allure.step("Verify selected value"):
        expect(page.locator(".css-1dimb5e-singleValue")).to_have_text(text_select)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking select one")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", ['Dr.','Mr.','Mrs.','Ms.','Prof.','Other'])
def test_select_one(test_menu_select: Page, text_select):
    page = test_menu_select
    with allure.step(f"Open dropdown and select '{text_select}'"):
        page.locator("#selectOne").click()
        page.get_by_text(text_select,exact=True).click()
    with allure.step("Verify selected value"):
        expect(page.locator(".css-1dimb5e-singleValue")).to_have_text(text_select)

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking old style menu")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", ['red','1','2','3','9','10'])
def test_old_style_menu(test_menu_select: Page, text_select):
    page = test_menu_select
    with allure.step(f"Select option with value '{text_select}'"):
        page.select_option("#oldSelectMenu", text_select)
    with allure.step("Verify selected option"):
        expect(page.locator("#oldSelectMenu option:checked")).to_have_attribute("value", text_select)

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking test menu select")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    ('Green','Red'),
    ('Blue',),
    ('Black','Blue'),
    ('Red',)                            ])
def test_multiselect_drop_down(test_menu_select: Page, text_select):
    page = test_menu_select
    input_fild = page.locator("#react-select-4-input")
    with allure.step(f"Select colors: {', '.join(text_select)}"):
        for color in text_select:
            input_fild.fill(color)
            page.get_by_text(color,exact=True).nth(1).click()
    with allure.step("Verify selected colors"):
        expect(page.locator(".css-1p3m7a8-multiValue")).to_have_count(len(text_select))

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking standard multi select")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("text_select", [
    ['Volvo','Saab'],
    ['Opel','Audi'],
    ['Volvo','Audi']                    ])
def test_standard_multi_select(test_menu_select: Page,text_select):
    page = test_menu_select
    with allure.step(f"Select cars: {', '.join(text_select)}"):
        page.select_option("#cars", value=text_select)
    with allure.step("Verify selected cars"):
        for car in text_select:
            is_selected = page.locator(f"#cars option:has-text('{car}')").evaluate("el => el.selected")
            assert is_selected, f"Option '{car}' is not selected"
