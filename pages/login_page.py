from pages.base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    REQUIRED_MESSAGE = ".oxd-input-field-error-message"

    def load(self):
        self.navigate(BASE_URL)

    def login(self,username,password):
        self.fill(self.USERNAME,username)
        self.fill(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def get_required_message(self):
        return self.get_text(self.REQUIRED_MESSAGE)

    def is_logged_in(self):
        self.page.wait_for_url("**/dashboard/**", timeout=10000)
        return "dashboard" in self.page.url
    


