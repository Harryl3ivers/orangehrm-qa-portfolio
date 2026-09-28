import time

def test_open_user_management(user_management_page):
    user_management_page.open_admin_menu()
    assert "admin" in user_management_page.page.url

def test_create_user(user_management_page):
    user_management_page.open_admin_menu()
    user_management_page.click_add()

    username = f"testuser{int(time.time())}"

    user_management_page.add_user(
        "Peter Mac Anderson",
        username,
        "Password123!"
    )

    assert user_management_page.is_visible(
    "text=Successfully Saved"
)

def test_passwords_do_not_match(user_management_page):
    user_management_page.open_admin_menu()
    user_management_page.click_add()
    user_management_page.select_user_role()
    user_management_page.enter_employee_name("Peter")
    user_management_page.select_status()
    user_management_page.enter_username("testuser123")
    user_management_page.enter_password("Password123!")
    user_management_page.enter_confirm_password("DifferentPassword123!")
    user_management_page.save_user()
    assert user_management_page.is_visible( "text=Passwords do not match")

def test_create_user_empty_username(user_management_page):
    user_management_page.open_admin_menu()
    user_management_page.click_add()
    user_management_page.select_user_role()
    user_management_page.enter_employee_name("Peter")
    user_management_page.select_status()
    user_management_page.enter_password("Password123!")
    user_management_page.enter_confirm_password("Password123!")
    user_management_page.save_user()
    assert user_management_page.is_visible(".oxd-input-field-error-message:has-text('Required')")

def test_duplicate_username(user_management_page):
    user_management_page.open_admin_menu()
    user_management_page.click_add()

    user_management_page.add_user(
        "Peter Mac Anderson",
        "testuser12345",
        "Password123!"
    )


   
    assert user_management_page.is_duplicate_username_message_visible()