import allure
from playwright.sync_api import Page, expect

class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = page.locator("#slider")
        self.slider_value = page.locator("#sliderValue")

    @allure.step("Set slider to {slider_value}")
    def set_slider_value(self, slider_value):
        self.slider.fill(slider_value)

    @allure.step("Verify slider value is {slider_value}")
    def check_slider_value(self, slider_value: str):
        expect(self.slider_value).to_have_value(slider_value)
    