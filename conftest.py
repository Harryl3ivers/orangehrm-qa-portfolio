import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from pages.user_management import UserManagementPage
@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def login_ease(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin","admin123")
    return page

@pytest.fixture
def employee_page(login_ease):
    return EmployeePage(login_ease)

@pytest.fixture
def user_management_page(login_ease):
    return UserManagementPage(login_ease)

# @pytest.fixture(autouse=True)
# def screenshot_failure(page,request):
#     yield
#     if request.node.rep_call.failed:
#         page.screenshot(path=f"reports/{request.node.name}.png")

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):

#     outcome = yield

#     report = outcome.get_result()

#     setattr(
#         item,
#         "rep_" + report.when,
#         report
#     )