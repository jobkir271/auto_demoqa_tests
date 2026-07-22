import pytest
import allure

from pages.elements.check_box_page import CheckBoxPage
from pages.forms_page import Elements
from pages.main_page import MainPage
from playwright.sync_api import Page,expect

@pytest.mark.parametrize(
"notes, commands, react, angular, veu, public, private, classified, general, wordFile, excelFile",
 [
    (True,True,True,True,True,True,True,True,True,True,True),
    (False,True,False,True,False,True,False,True,False,True,False),
    (False,False,False,False,False,False,False,False,False,False,False)
 ]
)
@allure.epic("demoqa_tests")
@allure.feature("check_box")
@allure.story("Filling in check boxes")
@allure.severity(allure.severity_level.NORMAL)

def test_check_box(page:Page,notes,commands,react, angular, veu, public, private, classified, general, wordFile, excelFile):
    with allure.step("open url demoqa.com"):
        main = MainPage(page)
        main.open("https://demoqa.com/")
        main.click_elements()
    with allure.step("Go to the tab Elements"):
        form = Elements(page)
        form.click_check_box()
    with allure.step("expand tree"):
        check_box = CheckBoxPage(page)
        check_box.expand_tree()

    names = ["notes", "commands", "react", "angular", "veu", "public", "private", "classified", "general", "wordFile", "excelFile"]
    flags = (notes, commands, react, angular, veu, public, private, classified, general, wordFile, excelFile)

    with allure.step("Sets the specified checkbox"):
        selected = check_box.select_checkboxes(names,flags)

    with allure.step("Verify that the selected data is the result of the"):
        for name in selected:
            expect(page.locator("#result")).to_contain_text(name)

