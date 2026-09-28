# Bug Reports


## BUG001 - Login Error Message Does Not Explain Failure

Severity:
Medium

Priority:
Medium


Environment:

Browser:
Chrome

OS:
Windows 11


Steps:

1. Enter invalid password
2. Click Login


Expected:

Clear error message explaining invalid credentials


Actual:

Generic error message displayed

## BUG002 - Empty Username Field Does Not Display Validation Message

Severity:Medium

Priority:Medium

Environment:
Browser:Chrome

OS:Windows 11

Steps:

1. Navigate to the OrangeHRM login page
2. Leave the username field empty
3. Enter a valid password (`admin123`)
4. Click Login

Expected:

A validation message should be displayed informing the user that the username field is required.

Actual:

No validation message is displayed. The login error message element is not shown, causing the login attempt to fail without clear feedback to the user.

Impact:

Users who leave the username field empty are not given clear guidance on how to correct the issue, which can lead to confusion during login.

Evidence:

Automated Playwright test failure:

`test_invalid_login[chromium--admin123]`

Failure reason:

`TimeoutError: waiting for locator(".oxd-alert-content-text")`
