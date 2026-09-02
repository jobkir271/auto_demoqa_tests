from pages.base_page import BasePage

class DatePickerPage(BasePage):
    def select_date(self,month,year,day):
        day_int = int(day)
        self.page.locator("#datePickerMonthYearInput").click()
        self.page.locator(".react-datepicker__month-select").select_option(month)
        self.page.locator(".react-datepicker__year-select").select_option(year)
        self.page.locator(f".react-datepicker__day--{day_int:03d}:not(.react-datepicker__day--outside-month)").click()

    def select_datetime(self,month,year,day,time):
        day_int = int(day)
        self.page.locator("#dateAndTimePickerInput").click()
        self.page.locator(".react-datepicker__month-read-view--selected-month").click()
        self.page.locator(f".react-datepicker__month-option:has-text('{month}')").click()
        self.page.locator(".react-datepicker__year-read-view--selected-year").click()

        target_year = str(year)
        while self.page.locator(f".react-datepicker__year-option:has-text('{target_year}')").count() == 0:
            self.page.locator(".react-datepicker__navigation--years-previous").click()

        self.page.locator(f".react-datepicker__year-option:has-text('{target_year}')").click()
        self.page.locator(f".react-datepicker__day--{day_int:03d}:not(.react-datepicker__day--outside-month)").click()
        self.page.locator(f".react-datepicker__time-list-item:has-text('{time}')").click()

