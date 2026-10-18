import pytest
import allure
from pages.elements.check_box_page import CheckBoxPage


@pytest.mark.parametrize(
    "notes, commands, react, angular, veu, public, private, classified, general, wordFile, excelFile",
    [
        (True, True, True, True, True, True, True, True, True, True, True),
        (False, True, False, True, False, True, False, True, False, True, False),
        (False, False, False, False, False, False, False, False, False, False, False),
    ]
)
@allure.epic("demoqa_tests")
@allure.feature("check_box")
@allure.story("Filling in check boxes")
@allure.severity(allure.severity_level.NORMAL)
def test_checkbox_tree(test_checkbox_tree, notes, commands, react, angular, veu, public, private,
                       classified, general, wordFile, excelFile):
    check_box = CheckBoxPage(test_checkbox_tree)
    check_box.expand_tree()

    names = ["notes", "commands", "react", "angular", "veu", "public", "private",
             "classified", "general", "wordFile", "excelFile"]
    flags = (notes, commands, react, angular, veu, public, private, classified, general, wordFile, excelFile)

    selected = check_box.select_checkboxes(names, flags)
    check_box.check_results(selected)