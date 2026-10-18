import allure
from playwright.sync_api import Page, expect


class SelectMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.react_select_2 = page.locator("#react-select-2-input")
        self.select_one_input = page.locator("#selectOne")
        self.old_select = page.locator("#oldSelectMenu")
        self.react_select_4 = page.locator("#react-select-4-input")
        self.cars = page.locator("#cars")
        self.single_value = page.locator(".css-1dimb5e-singleValue")
        self.multi_value = page.locator(".css-1p3m7a8-multiValue")

    @allure.step("Open dropdown and select '{text_select}'")
    def select_value_from_react(self, text_select: str):
        self.react_select_2.click()
        self.page.get_by_text(text_select, exact=True).click()

    @allure.step("Verify selected value '{text_select}'")
    def check_single_value(self, text_select: str):
        expect(self.single_value).to_have_text(text_select)

    @allure.step("Open selectOne and select '{text_select}'")
    def select_one(self, text_select: str):
        self.select_one_input.click()
        self.page.get_by_text(text_select, exact=True).click()

    @allure.step("Select option with value '{text_select}'")
    def select_old_style(self, text_select: str):
        self.old_select.select_option(text_select)

    @allure.step("Verify old style option '{text_select}'")
    def check_old_style(self, text_select: str):
        expect(self.page.locator("#oldSelectMenu option:checked")).to_have_attribute("value", text_select)

    @allure.step("Select colors: {colors}")
    def select_multiple_colors(self, colors: tuple):
        for color in colors:
            self.react_select_4.fill(color)
            self.page.get_by_text(color, exact=True).nth(1).click()

    @allure.step("Verify selected colors count")
    def check_multiple_colors(self, colors: tuple):
        expect(self.multi_value).to_have_count(len(colors))

    @allure.step("Select cars: {cars}")
    def select_cars(self, cars: list):
        self.cars.select_option(value=cars)  

    @allure.step("Verify selected cars")
    def check_cars_selected(self, cars: list):
        for car in cars:
            is_selected = self.page.locator(f"#cars option:has-text('{car}')").evaluate("el => el.selected")
            assert is_selected, f"Option '{car}' is not selected"