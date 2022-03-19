# In order to avoid creating the same fixture method in all the pyTest program for the
# browser opening and all other settings methods, we can create a file with this exact
# name 'conftest.py' in the project package (with all the others pyTest programs). this
# program then make all the fixtures, defined in it, available to all the testCases in all the
# pyTest program (which are the ones with name staring with 'test_...') in the project package.

# When a testCase makes reference to fixture method, if it is not found in the same program
# then it will automatically search into this conftest.py program.
# Below implementation is not efficient because all testCase execute will be repeating
# calling the execution of the browser_settings_fixture. So the fixture will be executed
# n times. The solution is to wrap up all testCases in a Class and modify the conftest.py
# program, see the pyTest program test_05FixtureConftestFileAndClass.py
def test_fixturedemo_01(browser_settings_fixture):
    print(" This code is from test_fixtureDemo_01 ")


def test_fixturedemo_02(browser_settings_fixture):
    print(" This code is from test_fixtureDemo_02 ")


def test_fixturedemo_03(browser_settings_fixture):
    print(" This code is from test_fixtureDemo_03 ")


def test_fixturedemo_04(browser_settings_fixture):
    print(" This code is from test_fixtureDemo_04 ")


def test_fixturedemo_05(browser_settings_fixture):
    print(" This code is from test_fixtureDemo_05 ")

