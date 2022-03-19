import pytest

from usingPyTestDemo.LoggerClass import LoggerClass  # The class containing the logger.


@pytest.mark.usefixtures("cross_browsers_data_fixture04_class")
class TestSuiteClassWitDataDriven(LoggerClass):  # to inherit the class where the logger is defined.
    # pyTest will automatically integrate into the html report, all the logged messages.

    # Using Fixture 04 from conftest.py:
    # (#@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")]))
    def test_add_customer(self, cross_browsers_data_fixture04_class):
        # create a 'log_01' object to instantiate the logger defined in the LoggerClass.
        log_01 = self.get_logger()  # get_logger() method is available because of inheritance of LoggerClass
        # now we can use the log_01 object instead of the Print() to send message to the log file defined
        # in the LoggerClass.
        log_01.info("First message sent with the get_logger() from a class wrapped testCase")

        log_01.info((" 03 ** cross_browsers_data_fixture04_class content:", cross_browsers_data_fixture04_class))
        print(" 03 ** cross_browsers_data_fixture04_class content:", cross_browsers_data_fixture04_class)
        number_parms = len(cross_browsers_data_fixture04_class)
        log_01.debug("**** number_parms: ")
        #log_01.debug("**** number_parms: ", number_parms)

        if number_parms == 3:
            # 3 the data element is a tuple with 3 attributes:
            wk_browser_name = cross_browsers_data_fixture04_class[0]
            wk_user_id = cross_browsers_data_fixture04_class[1]
            wk_password = cross_browsers_data_fixture04_class[2]
            log_01.info("03 *** Browser: User Id: Password:")
            #log_01.info("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id, "Password:", wk_password)
        else:
            if number_parms == 2:
                # 3 the data element is a tuple with 3 attributes:
                wk_browser_name = cross_browsers_data_fixture04_class[0]
                wk_user_id = cross_browsers_data_fixture04_class[1]
                log_01.error("03 *** Browser:  User Id: ")
                #log_01.error("03 *** Browser:", wk_browser_name, "User Id: ", wk_user_id)
            else:
                wk_browser_name = cross_browsers_data_fixture04_class
                print("03 *** ONLY ONE PARM, browser name is: ", wk_browser_name)
                log_01.warning(" 1 length is:")
                #log_01.warning(" 1 length is:", number_parms)

    # Using a test without paramater need:
    def test_without_parameters(self):
        log_02 = self.get_logger()
        log_02.info("*** Executing a test without parameters ***")


    # Using Fixture 03, using only the first parameter brower's name:
    # #@pytest.fixture(params=[("Firefox","userId3","password3"),"Chrome",("Firefox","userId2")])
    def test_only_name(self, cross_browsers_data_fixture04_class):
        # here, for accessing the data from the fixture, instead of the 'cross_browsers_data_fixture04_class' we
        # are going to use the class variable 'parametersList' defined in the fixture (in conftest.py) with the
        # command 'request.cls.parametersList = request.parm'. All of this is because, in the fixture, we are not
        # using the 'return request.param' to avoid conflict with the 'yield' command to execute the closing
        # statements after the last testCase in the class is executed.
        log_02 = self.get_logger()
        log_02.info("*** 03-name, browser's name:")
        if len(self.parametersList) == 3:
            browser_name = self.parametersList[0]
            user_id = self.parametersList[1]
            password = self.parametersList[2]
            print("**** browser_name", browser_name)
            print("*** userId: ", user_id)
            print("*** password: ", password)
        elif len(self.parametersList) == 2:
            browser_name = self.parametersList[0]
            user_id = self.parametersList[1]
            print("**** browser_name", browser_name)
            print("*** userId: ", user_id)
        else:
            browser_name = self.parametersList   # when leg() == 1, then it is not a list but a string var.
            print("**** browser_name", browser_name)


        #log_02.info("*** 03-name, browser's name:", cross_browsers_data_fixture04_class[0])
