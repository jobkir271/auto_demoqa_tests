import allure
from pages.Interactions.resizable_page import ResizablePage


@allure.epic("demoqa_tests")
@allure.feature("resizable")
@allure.story("checking limited box")
@allure.severity(allure.severity_level.NORMAL)
def test_resizable_limited(test_resizable):
    resizable = ResizablePage(test_resizable)
    resizable.resize_limited_box()


@allure.epic("demoqa_tests")
@allure.feature("resizable")
@allure.story("checking unlimited box")
@allure.severity(allure.severity_level.NORMAL)
def test_resizable_unlimited(test_resizable):
    resizable = ResizablePage(test_resizable)
    resizable.resize_unlimited_box()