# This is the second test using pyTest concepts
import pytest


def test_validateMessage():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because the msg content is not 'Hello' "

@pytest.mark.smoke01
def test_validateAddVar():
    a = 4
    b = 6
    assert a+2 == b, "Addition does not match"

@pytest.mark.smoke01
@pytest.mark.regression
def test_03AuthCreditCard():
    print("Executed test_03AuthCreditCard")