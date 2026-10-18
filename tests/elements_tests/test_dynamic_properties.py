import allure
from pages.elements.dynamic_properties_page import DynamicPropertiesPage


@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking dynamic text")
@allure.severity(allure.severity_level.NORMAL)
def test_dynamic_text(test_dynamic):
    dynamic = DynamicPropertiesPage(test_dynamic)
    dynamic.check_random_text_visible()


@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking enable buttons")
@allure.severity(allure.severity_level.NORMAL)
def test_enable_buttons(test_dynamic):
    dynamic = DynamicPropertiesPage(test_dynamic)
    dynamic.check_button_disabled()
    dynamic.check_button_enabled_after_wait()


@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking color button")
@allure.severity(allure.severity_level.NORMAL)
def test_color_button(test_dynamic):
    dynamic = DynamicPropertiesPage(test_dynamic)
    dynamic.check_color_changes()


@allure.epic("demoqa_tests")
@allure.feature("Dynamic Properties")
@allure.story("Checking invisible button")
@allure.severity(allure.severity_level.NORMAL)
def test_invisible_button(test_dynamic):
    dynamic = DynamicPropertiesPage(test_dynamic)
    dynamic.check_invisible_button_appears()