# This program explains how to use fixture to implement the execution of testCases/
# or setup methods that need to run before and after the execution of a testCase, i.e
# defining the driver and opening the webpage before executing the testCase or closing the
# opened browser after completing the test.
# - Method marked as fixtures are equivalent to the @before_Test and @after_test annotations in TestNG.
# - A fixture can be declared any where in the pyTest python program.
# - A method marked as fixture can be declared but ONLY will be executed when it is called or
#   referenced by another testCase/method (def test_01ValidateEntries(browserSetupFixture))
#  - A method marked as fixture method does not count as a textCase during execution even
#    if it's name start with 'test_'
#  - in a fixture method, all the code after the 'yield' command/statement will be executed
#    after the calling testCase/Method is completed, this is the equivalent of the
#    @after_test annotation in TestNG for tear down the execution.
#  - Any other testCase in the pyTest program that does not make reference to this marked
#    as fixtures method won't be affected by it.
import pytest


def test_01ValidateEntries(browserSetupFixture):
    print("*** 01 Executing test_01ValidateEntries ***")


@pytest.fixture()
def browserSetupFixture():
    print("*** 88 Executing the before part of method browserSetupFixture ***")
    yield
    print("*** 99 Executing the AFTER part of method browserSetupFixture ***")

def test_02VerifyReceipt():
    print("*** 02 Executed test_02VerifyReceipt ***")