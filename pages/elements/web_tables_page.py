from pages.base_page import BasePage

class WebTablesPage(BasePage):

    def add_record(self,first_name,last_name,email,age,salary,department):
        self.page.get_by_role('button', name='Add').click()
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Age").fill(str(age))
        self.page.get_by_placeholder("Salary").fill(str(salary))
        self.page.get_by_placeholder("Department").fill(department)
        self.page.get_by_role('button', name='submit').click()

    def edit_record(self,firts_name,salary):
        self.page.locator("#edit-record-2").click()
        self.page.get_by_placeholder("First Name").fill(firts_name)
        self.page.get_by_placeholder("Salary").fill(salary)
        self.page.get_by_role('button', name='Submit').click()


    def get_row_count(self):
        return self.page.locator("table tbody tr").count()

    def get_row_by_text(self,text):
        return self.page.locator(f"table tbody tr:has-text('{text}')")

    def delete_record(self):
        self.page.locator("#delete-record-3").click()