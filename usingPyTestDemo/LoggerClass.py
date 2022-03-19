import inspect
import logging


class LoggerClass:
    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        print("*** loggerName", logger_name)

        hector_logger = logging.getLogger(logger_name)
        # hector_logger = logging.getLogger(__name__)

        file_handler_log_file = logging.FileHandler("hectorLogFile_InClass02.log")  # connect file location to fileHandle
        # OR:
        # file_handler_log_file = logging.FileHandler("C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo\LogReports\hectorLogFile_02.log")

        first_formatter_object = logging.Formatter("%(asctime)s  :  %(name)s  :  %(levelname)s  :  %(message)s ")

        file_handler_log_file.setFormatter(first_formatter_object)  # connect formatter to fileHandle.

        hector_logger.handlers.clear()   # This avoid the repetition n times the log info sent to the log.

        hector_logger.addHandler(file_handler_log_file)  # Connect the fileHandler to the logger and we are almost ready.

        hector_logger.setLevel(logging.INFO)

        return hector_logger


