import pytest


@pytest.fixture()
def browser_settings_fixture():
    print("*** 88 from conftest.py file: Executing the before part of method browser_settings_fixture ***")
    yield
    print("*** 99 from conftest.py file: Executing the AFTER part of method browser_settings_fixture ***")


@pytest.fixture(scope="class")   # to execute only once before the first testCase in the class
# and then after 'yield' code, after the last testCase in the class.
# By using the scope="class" we are indicating that this fixture apply at class level which means, excute only
# once because there is only one class. If the scope is NOT indicated then the default is at testCase/Method level,
# which means execute for every time a step/testcase/method is executed.
def browser_settings_fixture_99():
    print("*** 88 from conftest.py file: Executing the before part of method browser_settings_fixture ***")
    yield
    print("*** 99 from conftest.py file: Executing the AFTER part of method browser_settings_fixture ***")


# Fixture to pass data to a testCase while execution:
@pytest.fixture(scope="class")  # At class level only.
def load_profile_dataFixture():
    print("** Executing the Fixture 'load_profile_dataFixture' ")
    return ["Hector", "Hernandez", "rahulshettyacademy.com"]
#            :name,    lastName,    website
#          to pass the data we are using a Python 'List' data structure [], {} for Dictionary and () for tuple,
#          because we are passing multiple data.

# Fixture for DataDriven and Parameterization (multiple execution). This is equivalent to the
# dataProvider in TestNG:
# Fixture 01:
@pytest.fixture(params=["Chrome","Firefox","IE"])  # A Python's List with 3 simple parameters, 3 times
#   execution, each time passing one of the defined parameter until the last one in the List.

# params=[] --> indicate that the fixture defines a Python's List of parameters. The len()/size of this
# parameters list indicate how many time the calling testCase will be executed.

def cross_browsers_data_fixture01(request):   # 'request' is an object/parameter that will receive the parameter
    #  defined in the fixture and that needs to be passed in each one of the iteration.
    return request.param  # to return the content of the request object.


# Fixture 02:
@pytest.fixture(params=[("Chrome","userId1","password1"),("userId2", "Firefox")])
    # above is for A list with 2 tuples parameters with 3 attribute each. 2 times execution

def cross_browsers_data_fixture02(request):   # 'request' is an object/parameter that will receive the parameter
    #  defined or passed from the fixture definition and that needs to be passed in each one of the iteration.
    return request.param  # to return the content of the request object.


# Fixture 03:
@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")])
    # above is for: A list with 1 simple parameter and 1 tuple parameter with 3 attributes. 2 times execution

def cross_browsers_data_fixture03(request):   # 'request' is an object/parameter that will receive the parameter
    #  defined in the fixture and that needs to be passed in each one of the iteration.
    print(" --- BEFORE: From conftest.py Executing the fixture cross_browsers_data_fixture03 --- ")
    return request.param  # to return the content of the request object.


# Fixture 04: to be used with a class wrapping all the testCases (TestSuite) and executing only ONCE IN EACH
# ITERATION NO MATTER THE NUMBER OF testCases in the wrapping class or TestSuite. before the execution
# of the first testCase wrapped in the class/TestSuite.
@pytest.fixture(scope="class",params=[("Class-Firefox","Class-userId4","Class-password4"),
                                      "Class-Chrome",("Class-Firefox","Class-userId4")])
    # above is for: A list with 1 simple parameter and 1 tuple parameter with 3 attributes. 2 times execution

def cross_browsers_data_fixture04_class(request):   # 'request' is an object/parameter that will receive the parameter
    #  defined in the fixture and that needs to be passed in each one of the iteration.
    # here, for making available the data to any calling class/method/testCase, instead of the
    # 'cross_browsers_data_fixture04_class' we
    # are going to use the class variable 'parametersList' defined here with the
    # command 'request.cls.parametersList = request.parm'. All of this is because we are not
    # using the 'return request.param' to avoid conflict with the 'yield' command to execute the closing
    # statements after the last testCase in the class is executed.

    print(" --- BEFORE(Class): From conftest.py Executing the fixture cross_browsers_data_fixture04_class --- ")

    request.cls.hectorParametersList = request.param
    # parametersList is defined as a global variable that is available/returned to the calling test_ method by
    # using the self.xxx format i.e. self.parametersList. And in this conftest.py code as request.cls.parametersList.
    print("**** **** request.cls.hectorParametersList", request.cls.hectorParametersList)
    # # NOT USED HERE: return request.param  # to return the content of the request object; instead used the
    # request.cls.hectorParametersList
    yield
    print(" 01--- AFTER(Class): From conftest.py Executing the fixture cross_browsers_data_fixture04_class --- ")
    print(" 02--- AFTER(Class): From conftest.py Executing the fixture cross_browsers_data_fixture04_class --- ")
    print(" 03--- AFTER(Class): From conftest.py Executing the fixture cross_browsers_data_fixture04_class --- ")


