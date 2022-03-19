# Fixtures can be used to load data into testCases for execution and to parametrize or pass
# parameter to the testCase execution so that we can run the testCase with multiple dataset.
# So fixture is also used to load data into testCase execution, because the data should be
# ready before the testCase execution begins
# Below the process to follow:
# 1- In the conftest.py, create a method (load_profile_dataFixture) with the data to be passed for the
#       testCase execution.
#       In this method we must have a 'return' command with all the data we want to pass to any
#       calling testCase.
# 2- In the conftest.py, Connect the created method to a class level fixture, see
#        @pytest.fixture(scope="class").
#
import pytest
# 3- Wrap all testCases in a class with name starting with Test..., and mark the class to use
#    the fixture with the commands/statements to execute before the first testCase and after the
#    last testCase. And with the data to load/use in each testCase that calls for the data
#    available in the fixture.

#    It is a best practice to wrap all testCases into a class, this way it is easy to use a
#    fixture at class level to make the data available to all the testCases in the class, so any
#    testCase/method wanting to use it just have to indicate the fixture's name in the parameter
#    list, after self, at definition time.

@pytest.mark.usefixtures("load_profile_dataFixture")
class TestSuiteDemoForLoadingDataToTestCases:
    # In pyTest, the name of the class must start with Test... to avoid the "Empty Suite" error:
    # == = == == == = test session starts == == === == == == == == == == =
    # collecting...collected 0 items
    # == == == == ==  no tests ran in 0.01 s  == == == == == == == == == ==
    # Process finished with exit code 5
    # Empty suite

    # below testCase uses/load the data from the fixture 'load_profile_dataFixture', because it calls the execution
    # of the load_profile_dataFixture method which returns the data needed:
    def test_editprofile(self, load_profile_dataFixture):
        print("The whole list received: ", load_profile_dataFixture)

        # Now we can access each individual item in the list directly or with a For...loop.
        firstname = load_profile_dataFixture[0]
        lastname = load_profile_dataFixture[1]
        website = load_profile_dataFixture[2]
        print("firstname:", firstname, "lastname:", lastname)
        print("website: ", website)

# below testCase DOES NOT use/load the data from the fixture 'load_profile_dataFixture' because it is not
    # calling the fixture name in the parameter after the self and the fixture, in the conftest.py file, was defined
    # with scope="class"
    def test_sayHello(self):
        print("Hello hello")

    def test_sayHelloAgain(self):
        print("hello")