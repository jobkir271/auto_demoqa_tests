import allure
import pytest

from playwright.sync_api import Page, expect

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking slider")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('slider_value', ["0","33","45","88","100",])
def test_slider(test_slider: Page, slider_value):
    with allure.step(f"Set slider to {slider_value}"):
        page = test_slider
        page.locator("#slider").fill(slider_value)
    with allure.step(f"Verify slider value is {slider_value}"):
        expect(page.locator("#sliderValue")).to_have_value(slider_value)