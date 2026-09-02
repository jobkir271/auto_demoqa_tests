from pages.base_page import BasePage

class AutoCompletePage(BasePage):

    MULTIPLE_INPUT = "#autoCompleteMultipleInput"
    SINGLE_INPUT = "#autoCompleteSingleInput"
    MULTI_VALUE_LABEL = ".auto-complete__multi-value__label.css-9jq23d"
    SINGLE_VALUE = ".auto-complete__single-value.css-1dimb5e-singleValue"

    def select_multiple_color(self, color: str):
        self.page.locator(self.MULTIPLE_INPUT).fill(color)
        self.page.get_by_text(color, exact = True).click()

    def select_single_color(self, color: str):
        self.page.locator(self.SINGLE_INPUT).fill(color)
        self.page.get_by_text(color, exact = True).click()

    def get_multiple_tags(self):
        return self.page.locator(self.MULTI_VALUE_LABEL)

    def get_single_tag(self):
        return self.page.locator(self.SINGLE_VALUE)
