import allure
from pages.elements.web_tables_page import WebTablesPage


@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking add record")
@allure.severity(allure.severity_level.NORMAL)
def test_add_record(test_web_tables):
    web = WebTablesPage(test_web_tables)
    count_rows = web.get_row_count()
    web.add_record("Artem", "Ganzal", "artem@gmail.com", 23, 180000, "Legal")
    row = web.get_row_by_text("Artem")
    web.check_row_contains(row, "Artem")
    web.check_rows_count(count_rows + 1)


@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking delete record")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_record(test_web_tables):
    web = WebTablesPage(test_web_tables)
    count_rows = web.get_row_count()
    web.delete_record()
    web.check_rows_count(count_rows - 1)


@allure.epic("demoqa_tests")
@allure.feature("web_tables")
@allure.story("Checking edit record")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_record(test_web_tables):
    web = WebTablesPage(test_web_tables)
    web.edit_record("Artem", "180000")
    row = web.get_row_by_text("Artem")
    web.check_row_contains(row, "Artem")
    web.check_row_contains(row, "180000")