import allure
from playwright.sync_api import Page, expect


class PracticeFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.file = "resources/file_test.txt"

    @allure.step("Fill practice form")
    def fill_form(self, data):
        first_name, last_name, email, mobile, date, subject, hobbies, address, state, city = data
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.locator('input[value="Male"]').check()
        self.page.get_by_placeholder("Mobile Number").fill(mobile)
        self.page.locator("#dateOfBirthInput").fill(date)
        self.page.locator(".col-12.mt-4.col-md-3.col-xl-3").click()
        self.page.locator("#subjectsInput").fill(subject)
        self.page.get_by_text("Maths", exact=True).or_(self.page.get_by_text("English", exact=True)).click()
        for hobby in hobbies:
            self.page.locator(f"#hobbies-checkbox-{hobby}").check()
        self.page.set_input_files("#uploadPicture", self.file)
        self.page.get_by_placeholder("Current Address").fill(address)
        self.page.locator("#state .css-19bb58m").click()
        self.page.get_by_text(state, exact=True).click()
        self.page.locator("#city .css-19bb58m").click()
        self.page.get_by_text(city, exact=True).click()
        self.page.get_by_role("button", name="submit").click()

    @allure.step("Check form result: expected_success={expected_success}")
    def check_form_result(self, expected_success):
        modal = self.page.locator(".modal-content")
        if expected_success:
            expect(modal).to_be_visible()
            self.page.wait_for_timeout(4000)
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)
        else:
            expect(modal).to_be_hidden()
            self.page.wait_for_timeout(4000)