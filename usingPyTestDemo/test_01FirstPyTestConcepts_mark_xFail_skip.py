# PyTest is a framework to write automated test with Python. It is like TestNG and JUnit for Java.
# We will understand all the features of PyTest using only the Python print() command, no Selenium
# this is to be able to focus on the learning.
# to install Pytest use this command in the console: pip install pytest
# To see the current version issue: pytest --version
# Naming convention for Python program/script to be consider as pyTest program/script:
# 1- Name must start/end with 'test_' i.e. test_01MyTestName.py OR test_01FirstPyTestConcepts_mark_xFail_skip.py

# 2- All code in the python script must be declare in a function/method using the key
#    word 'def', this is, all code must be wrapped in a method/function.
#    Every method defined with 'def' is treated as a testCase, and therefore will be reported
#    as pass or fail, the amount of time for execution and it's own 'print()' message identified.

# 3- All testCase/method/function name should start with 'test_' i.e. test_validateInput()

# 4- All testCase/method/function name should be unique, if repeated, no error will be generated but the
#    execution report only will show the result of the last method/test-name executed.

# 5- A pyTest package contains pyTest programs/scripts.
#    A pyTest program/script contains testCases.

# 6- From the console terminal and in the directory/path of the pyTest package
#    C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo> we
#    can execute:
#    + All pyTest programs in a pyTest package with: py.test -v -s
#    + Specific pyTest program with: py.test test_02AddCustomer.py -v -s
#    + Specific testCases in all pyTest programs in a pyTest package, we have to identify
#      a series of keywords (non case sensitive) in the name of each testCases and use
#      the parameter '-k':
#           py.test -k CreditCard -v -s   (all testCases with 'CreditCard' in their name)
#    + Specific testCases in one specific pyTest program in a pyTest package, we have to
#      identify a series of keywords (non case sensitive) in the name of each testCases and
#      use the parameter '-k':
#           py.test test_02AddCustomer.py -k creditcard -v -s
#     + To run certain testCases as Smoke Test or Regression we have to use 'Marks' to
#       identify or tag them in the pyTest program and then use these 'Marks' in the
#       execution command. Marks are similar to Tag (@) in Cucumber, or Groups in TestNG.
#       So in the pyTest program add the Marks, to each testCase, using this format:
#          @pytest.mark.keywordWeWantToUse.  i.e. @pytest.mark.regression, @pytest.mark.smoke01
#          we can mark one testCase with more than one mark:
#          @pytest.mark.regression
#          @pytest.mark.smoke01
#          def test_validateReceip():
#               print(xxx)
#
#        And in the execution command use the parameter -m keywordWeWantToUse (-m for mark):
#        py.test -m regression -v -s
#        py.test -m smoke01 -v -s
#        + To skip execution of the testCase we can mark it as skip and when we send execution
#          of all the tests the ones marked as skip won't be executed. We have to use the mark:
#          @pytest.mark.skip before the 'def' for the testCase
#         + If we have a testCase that we know that it is failing but we want to execute it
#           and not report it as failing because it creates something that is needed in others
#           testCases, so we can mark it with the xfail (exclude failing report):
#           @pytest.mark.xfail.

# 7- Parameters used:
#     -k stands for only execute the testCases/Methods having 'keywords' in the names.
#     -s indicates log the output indicated by the print() python's method.
#     -v indicates provide more information (meta data) about the execution.
#     -m indicates only execute the testcases marked with the indicated keyword.
import pytest


def test_01validateHello():
    print("hello Hector!!!!!!")


@pytest.mark.xfail
def test_validateAddition():
    a = 4
    b = 64
    assert a+2 == b, "Addition does not match"

@pytest.mark.regression
@pytest.mark.smoke01
def test_02validateFooterLine():
    print("** The footer line is perfect **")

@pytest.mark.skip
def test_03CreditCardSale():
    print("Executed test_03CreditCardSale")

# the above two commands is a PyTest test. To execute it with can use:
#   1- The command prompt/console:
#      + Copy the path of the pyTest package containing all the pyTest 'usingPyTestDemo' (package)
#      + go to the command prompt console and cd to the copied path/directory
#      + issue the command: py.test -v -s
#         where -v is the option verbose to give a lot of details on the execution of each test_ file.
#               -s is the option to show all 'print()' log messages sent to the console. the
#                format used is pyTestName.py:: methodName message sent in the print(), see below:
#                test_01FirstPyTestConcepts_mark_xFail_skip.py::test_validateHello hello Hector!!!!!!
#      + all tests in the pyTest package will be executed based on the naming convention 'test_'
#      + To run specific pyTest program/scrip in the package, instead of all, we just need
#        add the name of the specific pyTest program: py.test test_02AddCustomer.py -v -s
#
#   2- The test runner available in PyCharm. We cannot run the PyTest script like any other Python
#     script click the Run button, because the PyTest framework won't be activated while the execution,
#     we have to run the script as PyTest we have to use the plugin already built in Python, to do this
#       + Open the listbox with the active program in Pycharm, and select the "Edit configurations.."
#       + Click on the '+' in the top left corner to "Add New Configuration"
#       + Under the 'Python tests' menu select the 'pytest' framework
#       + Click OK button.
#       + Verify that the current program in the listbox now says 'pytest in bin'
#       + Now to indicate which pyTest to run:
#           * Again, Open the listbox with the active program in Pycharm, and select the "Edit configurations.."
#           * The new 'pytest in bin' configuration framework is opened in the 'Configuration' tab for
#           * with the 'Target' radio button checked for 'Script path'
#           * Open the folder listbox located the folder and select the pytest test we want to run
#           * click Apply and Okay button.
#           * Verify that the current program in the listbox now says the name of the pytest we want to
#           run 'test_01FirstPyTestConcepts_mark_xFail_skip.py'
#        + Now we can use the PyCharm Runner button to run the PyTest test and call the PyTest framwork
#        + the below is now displayed in the console:
# C:\Users\ssshh\AppData\Local\Programs\Python\Python39\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/ssshh/PycharmProjects/HectorFirstpythonProject/usingPyTestDemo/test_01FirstPyTestConcepts_mark_xFail_skip.py
# Testing started at 7:11 AM ...
# Launching pytest with arguments C:/Users/ssshh/PycharmProjects/HectorFirstpythonProject/usingPyTestDemo/test_01FirstPyTestConcepts_mark_xFail_skip.py --no-header --no-summary -q in C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_01FirstPyTestConcepts_mark_xFail_skip.py::test_validateHello PASSED                 [100%]hello Hector!!!!!!
#
# ============================== 1 passed in 0.06s ==============================
#
# Process finished with exit code 0
