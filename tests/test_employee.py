from playwright.sync_api import expect


def test_view_employee_list(employee_page):
    employee_page.open_employee_menu()
    assert "pim" in employee_page.page.url


def test_search_employee(employee_page):
    employee_page.open_employee_menu()
    employee_page.search_employee("Peter")

    expect(
        employee_page.page.get_by_text("Peter Mac", exact=True)
    ).to_be_visible(timeout=10000)

def test_search_non_existing_employee(employee_page):
    employee_page.open_employee_menu()
    employee_page.search_employee("ThisEmployeeDoesntExist")

    employee_page.page.pause()

    assert employee_page.is_visible(
        "span:has-text('No Records Found')"
    )
