import allure

from playwright.sync_api import expect
from pages.elements.web_tables_page import WebTablesPage

@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking add record")
@allure.severity(allure.severity_level.NORMAL)
def test_add_record(test_web_tables):
    with allure.step("Get initial row count"):
        page = test_web_tables
        web = WebTablesPage(page)
        count_rows = web.get_row_count()
    with allure.step("Add a new record"):
        web.add_record("Artem","Ganzal","artem@gmail.com",23,180000,"Legal")
        row = web.get_row_by_text("Artem")
    with allure.step("Verify the new record appears"):
        expect(row).to_contain_text('Artem')
        expect(page.locator("table tbody tr")).to_have_count(count_rows + 1)

@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking delete record")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_record(test_web_tables):
    with allure.step("Get initial row count"):
        page = test_web_tables
        web = WebTablesPage(page)
        count_rows = web.get_row_count()
    with allure.step("Delete a record"):
        web.delete_record()
    with allure.step("Verify the row count decreased by one"):
        expect(page.locator("table tbody tr")).to_have_count(count_rows - 1)

@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking edit record")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_record(test_web_tables):
    with allure.step("Edit an existing record"):
        page = test_web_tables
        web = WebTablesPage(page)
        web.edit_record("Artem","180000")
    with allure.step("Verify the record was edited"):
        row = page.locator("table tbody tr:has-text('Artem')")
        expect(row).to_contain_text('Artem')
        expect(row).to_contain_text('180000')





