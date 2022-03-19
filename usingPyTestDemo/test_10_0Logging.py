# logging is used to put the detail of why the testCase execution fail. so we have to log all the
# information of what the script did. Or provide description of how the script is running, what data
# was used: MID, Company, userId, transaction executed... The Script execution should speak by using
# the log, so that if something was wrong we can get all the trouble shooting information in the log file.
# Example of a log entry:
# "2021-09-27 12:25:14, 788 :ERROR : <TestCase name> : Fatal error in submitting credit card payment on
#       step # 4. Cannot Continue processing" This detail help a non-technical person to read the log file
# and understand what the problem is.
# The debug is mainly for technical people.
# Logging is implemented by sending everything to a separate file using an Industry standard format which
# May contains:
# 1- The specific TimeStamp when the step was executed.
# 2- The kind of log displayed: DEBUG, INFORMATION, WARNING, ERROR, CRITICAL.
#  DEBUG: Is for programmer display information that they can use to trouble shoot the program.
#           - log.DEBUG: hector_logger.debug("")
#  INFO: Is used to provide information of what the test is doing: what step/function is being executed,
#        but not related to execution failure.
#           - log.INFO: hector_logger("statement read Employees file successfully executed, similar to debug, but for non-technical people")
#  WARNING: Is used to provide information not expected, but that does not requires that the program
#           execution fail. This is mainly to alert the user about something in the execution, for
#           example when processing a Credit card payment and found a negative balance we can use
#           the warning message; but not failing the testCase execution:
#           - log.WARNING: hector_logger.warning("Negative balance found when Credit Card payment")
#  ERROR: Is used when we think that the testCase execution should fail, for example, when an assertion
#         fail we want to send the error log message
#           - log.ERROR: hector_logger.error(" Account not found")
#  CRITICAL: Is used when the error in this particular testCase is blocking the execution of the other
#           testCases in the whole Framework
#           - log.CRITICAL(): hector_logger.critical("Failing signing in the main web page ")

# We have to import the logging class/package:
import logging

# We have to create the method/ to contain the logging definition:
def test_logging_method():

    # We have to create an object (hector_logger) to be used to log everything that need to be logged,
    # by using the logging's class method getLogger() (logging.getLogger()). this object is responsible
    # for printing all the messages

    # A log file will contains information for all the testCases executed in the TestSuite, so we need to
    # indicate the name of the physical file (pyTest.py), containing all the testCases, in each logged message.
    # this physical program name is passed in the logger object creation using the "__name__"  parameter.

    hector_logger = logging.getLogger(__name__)

    # for the hector_logger to know in which file has to print the logged message we have to connect it to
    # a file handler object by using the hector_logger object's 'addHandler() method.
    fileHandlerLogFile = logging.FileHandler("hectorLogFile_01.log")  # connect file location to fileHandle
    # OR:
    # fileHandlerLogFile = logging.FileHandler("C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo\LogReports\hectorLogFile_02.log")

    # We have to connect the message format to the 'fileHandlerLogfileLocation', the format says how to print the message.
    # We have to create a formatter object (firstFormatterObject) with the format definition and then connect it to the
    # fileHandleLogFileLocation using the setFormatter() method:
    # we will use this format: "2021-09-27 12:25:14, 788 :   ERROR       : <PYTest.py file name> : Fatal error in step # 4."
    #                                %(asctime)s         : %(levelname)s :  $(name)s             : %(message)s
    # % --> use to indicate the start of a variable definition and that this variable will loaded at run time.
    # asctime --> variable for the TimeStamp.
    # s --> indicate a string variable.
    # levelname --> indicate the log level variable: DEBUT, INFO, WARNING, ERROR, CRITICAL
    # name --> is the PyTest.py file/script name from where the log was sent.
    #       Note: when calling the logger from a class, the name will be the name of the class defining the
    #       logger instead of the name of the testCase calling the loggerClass. to fix this we have to use the
    #       command loggerName = inspect.stack() [1][3], in the class definition.
    # message --> is the actual message.

    firstFormatterObject = logging.Formatter("%(asctime)s  :  %(levelname)s  :  %(name)s  :  %(message)s ")

    fileHandlerLogFile.setFormatter(firstFormatterObject)  # connect formatter to fileHandle.

    hector_logger.addHandler(fileHandlerLogFile)  # Connect the fileHandler to the logger and we are almost ready.

    # last part is to set the log level to be sent to the log file used by the hector_logger:
    # The log level is used to determine which log type to send to the file based on the log's type hierarchy:
    # logger.setLevel(loging.XXX) indicate from which level to start and continue in the hierarchy.
    # 0 --> debug  --> send starting on 'debug' and all others (info, warning...Critical)
    # 1 --> info   --> send starting on 'info' and then all others (warning, error, critical)
    # 2 --> warning -> send starting on 'warning' and then all others (error, critical)
    # 3 --> error  --> send starting on 'error' and then critical
    # 4 --> critical -> send only critical.
    #hector_logger.setLevel(logging.INFO)
    #hector_logger.setLevel(logging.ERROR)
    #hector_logger.setLevel(logging.WARNING)
    hector_logger.setLevel(logging.CRITICAL)


    hector_logger.debug("Number of elements in Address List is 20")
    hector_logger.info("statement read Employees file successfully executed")
    hector_logger.debug("Number of elements in Order List is 60")
    hector_logger.warning("Negative balance found when Credit Card payment")
    hector_logger.error(" Account not found")
    hector_logger.critical("Failing signing in the main web page")