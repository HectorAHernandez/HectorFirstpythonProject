# Data driven and parameterization allow to pass parameters/data to a testCase at execution time
# and repeat the execution for the number of parameters defined in the fixture associated to the
# method returning the parameters to pass to the testCases.
# This is we can send multiple set of data and make the testCase to run multiple times.

# *** This program is using a testCase not wrapped in a class. (for simplicity) we will create another
# program with a wrapping class.  ***

# For example we want to run a testCase that execute for the browser's name and credentials indicated in the
# fixture method. And that runs for as many browsers indicated in this fixture. Below the steps:

# 1- In the conftst.py program, create the fixture and method that will pass/return the
#    parameters (browser's name and credentials).

# Using the fixture-01  @pytest.fixture(params=["Chrome","Firefox","IE"])
def test_add_employee01(cross_browsers_data_fixture01):
    wk_browser_name = cross_browsers_data_fixture01
    print("01 *** Running the test for browser: ", wk_browser_name)
    print("01 The current fixture element is:  ", cross_browsers_data_fixture01)


# Using Fixture 02:
# #@pytest.fixture(params=[("Chrome","userId1","password1"),("userId2", "Firefox")])
def test_modify_empoloyee02(cross_browsers_data_fixture02):
    received_parms_list = cross_browsers_data_fixture02
    print("received_parms_list", received_parms_list)

    if len(received_parms_list) == 3:
        wk_browser_name = received_parms_list[0]
        wk_user_id = received_parms_list[1]
        wk_password = received_parms_list[2]
        print(" 3 Elements in parms List:", len(received_parms_list))
        print("Browser to Test: ", wk_browser_name)
        print("UserId: ", wk_user_id, "Password: ", wk_password)

    if len(received_parms_list) == 2:
        wk_browser_name = received_parms_list[1]
        wk_user_id = received_parms_list[0]
        print(" 2 Elements in parms List:", len(received_parms_list))
        print("Browser to Test: ", wk_browser_name)
        print("userid: ", wk_user_id)


# Using Fixture 03:
# #@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")])
def test_delete03(cross_browsers_data_fixture03):
    print(" 03 ** cross_browsers_data_fixture03 content:", cross_browsers_data_fixture03)
    number_parms = len(cross_browsers_data_fixture03)
    print("**** number_parms: ", number_parms)   # if the received parameter from the iteration is
    #                          a tuple, then number_parms will have how many elements in the tuple,
    #                          if it is a simple String element, then it will have the number of
    #                          characters in the string.

    if number_parms == 3:
        # 3 the data element is a tuple with 3 attributes:
        wk_browser_name = cross_browsers_data_fixture03[0]
        wk_user_id = cross_browsers_data_fixture03[1]
        wk_password = cross_browsers_data_fixture03[2]
        print("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id, "Password:", wk_password)
    else:
        if number_parms == 2:
            # 3 the data element is a tuple with 3 attributes:
            wk_browser_name = cross_browsers_data_fixture03[0]
            wk_user_id = cross_browsers_data_fixture03[1]
            print("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id)
        else:
            wk_browser_name = cross_browsers_data_fixture03
            print("03 *** ONLY ONE PARM, browser name is: ", wk_browser_name)
            print(" 1 length is:", number_parms)
            # Note: if we pass only one parameter (not a tuple) then
            # Python will assume the length as the number of characters in the received parameter
            # 'cross_browsers_data_fixture04_class' in this case 6 for Chrome.


# Using Fixture 03, using only the first parameter brower's name:
# #@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")])
def test_delete_name(cross_browsers_data_fixture03):
    print("*** 03-name, browser's name:",cross_browsers_data_fixture03[0])