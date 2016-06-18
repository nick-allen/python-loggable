import logging

__version__ = '0.1.0'
__author__ = 'Nick Allen <nick.allen.cse@gmail.com>'


class Loggable(object):
    """Simple mixin adding a logging.logger instance to all class instances"""

    __logger = None

    @property
    def logger(self):
        """Return logger instance, instantiating on-demand using self.build_logger() hook"""
        if self.__logger is None:
            self.__logger = self.build_logger()

        return self.__logger

    def build_logger(self):
        """Hook to customize how logger instance is instantiated"""
        return logging.getLogger(self.__module__)
