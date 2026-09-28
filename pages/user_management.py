from pages.base_page import BasePage

class UserManagementPage(BasePage):
    ADMIN_MENU = "a[href='/web/index.php/admin/viewAdminModule']"
    USERNAME_INPUT = ".oxd-input-group:has-text('Username') input"
    PASSWORD_INPUT = ".oxd-input-group:has(label:text-is('Password')) input"
    CONFIRM_PASSWORD = ".oxd-input-group:has(label:text-is('Confirm Password')) input"

    USER_ROLE = ".oxd-input-group:has-text('User Role') .oxd-select-text"
    ADMIN_INPUT = "[role='listbox'] >> text=Admin"
    EMPLOYEE_NAME_INPUT = ".oxd-input-group:has-text('Employee Name') input"
    EMPLOYEE_OPTION = "[role='listbox']"

    STATUS = ".oxd-input-group:has-text('Status') .oxd-select-text"
    STATUS_ENABLED_OPTION = "[role='listbox'] >> text=Enabled"

    ADD_BUTTON = "button:has-text('Add')"
    SAVE_BUTTON = "button[type='submit']"
    
    def open_admin_menu(self):
        self.click(self.ADMIN_MENU)

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def enter_username(self,username):
        self.fill(self.USERNAME_INPUT,username)
    
    def select_user_role(self):
        self.click(self.USER_ROLE)
        self.click(self.ADMIN_INPUT)

    def enter_employee_name(self, employee_name):
        self.fill(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.click(f".oxd-autocomplete-option:has-text('{employee_name}')")

    def select_status(self):
        self.click(self.STATUS)
        self.click(self.STATUS_ENABLED_OPTION)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT,password)

    def enter_confirm_password(self, password):
        self.fill(self.CONFIRM_PASSWORD,password)

    def save_user(self):
        self.click(self.SAVE_BUTTON)

        errors = self.page.locator(
        ".oxd-input-field-error-message"
    ).all_text_contents()

        print("ERRORS:", errors)
        

    def add_user(self,employee_name,username,password):
        self.select_user_role()
        self.enter_employee_name(employee_name)
        self.select_status()
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.save_user()

    def is_username_visible(self, username):
        return self.is_visible(f"text={username}")

    def is_duplicate_username_message_visible(self):
        return self.is_visible(
        "span.oxd-input-field-error-message:has-text('Already exists')"
    )