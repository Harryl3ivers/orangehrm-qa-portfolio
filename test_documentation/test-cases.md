# Test Cases

## TC001 - Successful Login

Priority:
High

Type:
Functional Test

Preconditions:
User has valid credentials


Steps:

1. Navigate to login page
2. Enter valid username
3. Enter valid password
4. Click Login


Expected Result:

User is redirected to dashboard

## TC002 - Login With Invalid Password

Priority:
High

Type:
Negative Test


Steps:

1. Navigate to login page
2. Enter valid username
3. Enter incorrect password
4. Click Login


Expected Result:

Error message displayed
User remains on login page

## TC003 - Login With Empty Username

Priority:
High

Type:
Negative Test

Preconditions:
User is on login page


Steps:

1. Leave username field empty
2. Enter valid password
3. Click Login


Expected Result:

Validation message displayed requesting username

## TC004 - Login With Empty Password

Priority:
High

Type:
Negative Test


Steps:

1. Enter valid username
2. Leave password field empty
3. Click Login


Expected Result:

Validation message displayed requesting password

## TC005 - View Employee List

Priority:
Medium

Type:
Functional Test


Steps:

1. Login successfully
2. Navigate to Employee List


Expected Result:

Employee records are displayed

## TC006 - Search For Employee

Priority:
Medium

Type:
Functional Test


Steps:

1. Login
2. Navigate to Employee List
3. Enter employee name
4. Click Search


Expected Result:

Matching employee record is displayed

## TC007 - Search For Non Existing Employee

Priority:
Medium

Type:
Negative Test


Steps:

1. Search for invalid employee name


Expected Result:

No matching records message displayed

## TC008 - Create New User

Priority:
High

Type:
Functional Test


Steps:

1. Navigate to User Management
2. Click Add User
3. Enter valid information
4. Save


Expected Result:

New user account created

## TC009 - View UserManagement page