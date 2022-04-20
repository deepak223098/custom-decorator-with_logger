import traceback
import sys
from datetime import datetime
import logging
import json


class my_logger:
    def __init__(self, logPath='exc_logger.log'):
        self.logPath = logPath
        self.logger = logging.getLogger(self.logPath[:-4])
        self.logger.setLevel(logging.INFO)

        # create a file to store all the
        # logged exceptions
        logfile = logging.FileHandler(self.logPath)

        # fmt = '%(asctime)s - %(levelname)s - %(message)s'
        # # fmt = '%(asctime)-15s %(levelname)-8s %(message)s'
        # formatter = logging.Formatter(fmt)
        formatter = logging.Formatter(
            json.dumps({'time': '%(asctime)s', 'level': '%(levelname)s', 'message': '%(message)s'}))

        logfile.setFormatter(formatter)
        self.logger.addHandler(logfile)

    def create_logger(self):
        return self.logger


def exception_handler_logger(func_obj=None, loggerObj=None):
    def wrapper(func):
        def inner_function(*args, **kwargs):
            loggerObj.info(f"{func.__name__} Started")
            value = None
            flag = 1
            try:
                value = func(*args, **kwargs)
            except Exception as err:
                flag = 0
                loggerObj.exception(err)
            finally:
                loggerObj.info(f"{func.__name__} Completed")
            return value, flag, func_obj

        return inner_function

    return wrapper


class EMAIL:
    def __init__(self):
        ''' add the new functionality '''
