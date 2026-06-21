from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    def fill_form(self,first_name,last_name,email,mobile,date,subject,
                  number_hobby,file_set,address,state,city):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.locator('input[value="Male"]').check()
        self.page.get_by_placeholder("Mobile Number").fill(mobile)
        self.page.locator("#dateOfBirthInput").fill(date)
        self.page.locator(".col-12.mt-4.col-md-3.col-xl-3").click()
        self.page.locator("#subjectsInput").fill(subject)
        self.page.get_by_text("Maths", exact=True).or_(self.page.get_by_text("English", exact=True)).click()
        for hobby in number_hobby:
            self.page.locator(f"#hobbies-checkbox-{hobby}").check()
        self.page.set_input_files("#uploadPicture", file_set)
        self.page.get_by_placeholder('Current Address').fill(address)
        self.page.locator("#state .css-19bb58m").click()
        self.page.get_by_text(state, exact=True).click()
        self.page.locator("#city .css-19bb58m").click()
        self.page.get_by_text(city, exact=True).click()
        self.page.get_by_role("button", name="submit").click()

