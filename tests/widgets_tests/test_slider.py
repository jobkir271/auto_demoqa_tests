import allure
import pytest
from pages.widgets.slider_page import SliderPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking slider")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('slider_value', ["0","33","45","88","100",])
def test_slider(test_slider, slider_value):
    slider = SliderPage(test_slider)
    slider.set_slider_value(slider_value)
    slider.check_slider_value(slider_value)
