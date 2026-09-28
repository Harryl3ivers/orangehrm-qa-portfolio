from pages.base_page import BasePage

class EmployeePage(BasePage):
    EMPLOYEE_MENU = "a[href='/web/index.php/pim/viewPimModule']"
    EMPLOYEE_LIST = "a[href='/web/index.php/pim/viewEmployeeList']"
    SEARCH_INPUT = "input[placeholder='Type for hints...']"
    SEARCH_BUTTON = "button[type='submit']"

    def open_employee_menu(self):
        self.click(self.EMPLOYEE_MENU)

    def search_employee(self, employee_name):
        self.page.locator(self.SEARCH_INPUT).first.fill(employee_name)
        self.click(self.SEARCH_BUTTON)

