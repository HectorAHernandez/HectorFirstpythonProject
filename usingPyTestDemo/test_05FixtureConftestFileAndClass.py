#The solution in program test_04FixtureWithConfTestFile.py was not efficient so here
# we wrap up all testCases in a Class and modify the fixture in the conftest.py
# program to use the parameter (scope="class") for the new fixture browser_settings_fixture_99
# This will execute the fixture only once, before the execution of the first testCase in
# the class and the after 'yield' code, after the last testCase in the class.
# see the new fixture browser_settings_fixture_99 in the conftest.py
import pytest


@pytest.mark.usefixtures("browser_settings_fixture_99")  # In "", effective at class level.
#    this browser_settings_fixture_99 was modified to use the scope="class" level.
class TestSuiteDemo:  # To wrap all below testCases and be able to execute the fixture at class
    # level, which means execute ONLY ONCE, at the before the first testCase and the after 'yield' code, after
    # the last testCase wrapped in the class/TestSuite.

    # In pyTest, the name of the class must start with Test... to avoid the "Empty Suite" error:
    # == = == == == = test session starts == == === == == == == == == == =
    # collecting...collected 0 items
    # == == == == ==  no tests ran in 0.01 s  == == == == == == == == == ==
    # Process finished with exit code 5
    # Empty suite


    def test_fixturedemo_01(self):  # self is mandatory parameter when defining method or
        # testCases wrapped in a class.
        # Note: we do not need to indicate the fixture's name because the fixture will run
        # automatically at class level before any testCase. But if the testCase needs data defined
        # or contained in the fixture, then we can call/use add the fixture's name (as a parameter)
        # to have access to the data defined in the fixture, see script "test_06FixtureToLoadDataIntoTestCase.py",
        # but the code in the fixture will be executed only once (at class level)
        print(" This code is from test_fixtureDemo_01 ")


    def test_fixturedemo_02(self):
        print(" This code is from test_fixtureDemo_02 ")


    def test_fixturedemo_03(self):
        print(" This code is from test_fixtureDemo_03 ")


    def test_fixturedemo_04(self):
        print(" This code is from test_fixtureDemo_04 ")


    def test_fixturedemo_05(self):
        print(" This code is from test_fixtureDemo_05 ")

