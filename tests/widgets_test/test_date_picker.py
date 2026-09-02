import allure
import pytest

from playwright.sync_api import Page, expect
from pages.widgets.date_picker_page import DatePickerPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("date picker")
@pytest.mark.parametrize("month, year, day, expected", [
    ("April", "2002", "7", "04/07/2002"),
    ("May", "2026", "26", "05/26/2026"),
    ("August", "2020", "3", "08/03/2020"),
])
def test_select_date(test_date_picker: Page, month, year, day, expected):
    page = test_date_picker
    date_picker = DatePickerPage(page)
    with allure.step(f"select date {month},{year},{day}"):
        date_picker.select_date(month,year,day)
    with allure.step(f"Verify input has value: {expected}"):
        expect(page.locator("#datePickerMonthYearInput")).to_have_value(expected)


@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("date and time picker")
@pytest.mark.parametrize("month, year, day, time, expected", [
    ("May", "2015", "14", "00:15", "May 14, 2015 12:15 AM"),
    ("August", "2020", "3", "12:30", "August 3, 2020 12:30 PM"),
])
def test_data_and_time(test_date_picker: Page,month, year, day, time, expected):
    page = test_date_picker
    date_picker = DatePickerPage(page)
    with allure.step(f"Select datetime: {month} {day}, {year} at {time}"):
        date_picker.select_datetime(month, year, day, time)
    with allure.step(f"Verify input has value: {expected}"):
        expect(page.locator("#dateAndTimePickerInput")).to_have_value(expected)