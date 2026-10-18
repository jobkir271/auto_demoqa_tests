import allure
from playwright.sync_api import Page, expect


class DatePickerPage:
    def __init__(self, page: Page):
        self.page = page
        self.date_input = page.locator("#datePickerMonthYearInput")
        self.datetime_input = page.locator("#dateAndTimePickerInput")

    @allure.step("Select date {month}, {year}, {day}")
    def select_date(self, month, year, day):
        day_int = int(day)
        self.date_input.click()
        self.page.locator(".react-datepicker__month-select").select_option(month)
        self.page.locator(".react-datepicker__year-select").select_option(year)
        self.page.locator(f".react-datepicker__day--{day_int:03d}:not(.react-datepicker__day--outside-month)").click()

    @allure.step("Select datetime: {month} {day}, {year} at {time}")
    def select_datetime(self, month, year, day, time):
        day_int = int(day)
        self.datetime_input.click()
        self.page.locator(".react-datepicker__month-read-view--selected-month").click()
        self.page.locator(f".react-datepicker__month-option:has-text('{month}')").click()
        self.page.locator(".react-datepicker__year-read-view--selected-year").click()

        target_year = str(year)
        while self.page.locator(f".react-datepicker__year-option:has-text('{target_year}')").count() == 0:
            self.page.locator(".react-datepicker__navigation--years-previous").click()

        self.page.locator(f".react-datepicker__year-option:has-text('{target_year}')").click()
        self.page.locator(f".react-datepicker__day--{day_int:03d}:not(.react-datepicker__day--outside-month)").click()
        self.page.locator(f".react-datepicker__time-list-item:has-text('{time}')").click()

    @allure.step("Verify date input has value: {expected}")
    def check_date_value(self, expected):
        expect(self.date_input).to_have_value(expected)

    @allure.step("Verify datetime input has value: {expected}")
    def check_datetime_value(self, expected):
        expect(self.datetime_input).to_have_value(expected)