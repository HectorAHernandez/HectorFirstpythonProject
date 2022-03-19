# Data driven and parameterization allow to pass parameters/data to a testCase at execution time
# and repeat the execution for the number of parameters defined in the fixture associated to the
# method returning the parameters to pass to the testCases.
# This is we can send multiple set of data and make the testCase to run multiple times.

# *** This program is using a testCases WRAPPED in a class.
# This is use a class wrapping all the testCases (TestSuite) and executing the code in the
# fixture only ONCE IN EACH ITERATION, NO MATTER THE NUMBER OF testCases in the wrapping
# class/TestSuite, before the execution of the first testCase wrapped in the class/TestSuite.

# For example we want to run a testCase that execute for the browser's name and credentials indicated in the
# fixture method. And that runs for as many browsers indicated in this fixture. Below the steps:

# 1- In the conftest.py program, create the fixture and method that will pass/return the
#    parameters (browser's name and credentials).
import pytest


@pytest.mark.usefixtures("cross_browsers_data_fixture04_class")
class TestSuiteClassWitDataDriven:


    # Using Fixture 04 from conftest.py:

    def test_cross_browser04(self, cross_browsers_data_fixture04_class):
        print(" 03 ** cross_browsers_data_fixture04_class content:", self.hectorParametersList)
        # note: hectorParametersList is defined as a global variable in the method cross_browsers_data_fixture04_class,
        # therefore to access it we have to use self.xx i.e. self.hectorParametersList.

        number_parms = len(self.hectorParametersList)
        print("**** number_parms: ", number_parms)  # if the received parameter from the iteration is
        #                          a tuple, then number_parms will have how many elements in the tuple,
        #                          if it is a simple String element, then it will have the number of
        #                          characters in the string.

        if number_parms == 3:
            # 3 the data element is a tuple with 3 attributes:
            wk_browser_name = self.hectorParametersList[0]
            wk_user_id = self.hectorParametersList[1]
            wk_password = self.hectorParametersList[2]
            print("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id, "Password:", wk_password)
        else:
            if number_parms == 2:
                # 3 the data element is a tuple with 3 attributes:
                wk_browser_name = self.hectorParametersList[0]
                wk_user_id = self.hectorParametersList[1]
                print("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id)
            else:
                wk_browser_name = self.hectorParametersList
                print("03 *** ONLY ONE PARM, browser name is: ", wk_browser_name)
                print(" 1 length is:", number_parms)
                # Note: if we pass only one parameter (not a tuple) then
                # Python will assume the length as the number of characters in the recieved parameter
                # 'cross_browsers_data_fixture04_class' in this case 6 for Chrome.

    # Using a test without paramater need:
    def test_without_parameters(self):
        print("*** Executing a test without parameters ***")

    # Using Fixture 03, using only the first parameter brower's name:
    # #@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")])
    def test_only_name(self, cross_browsers_data_fixture04_class):
        print("*** 03-name, browser's name:", self.hectorParametersList[0])