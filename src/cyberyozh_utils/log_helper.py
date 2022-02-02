# -*- coding: utf-8 -*-
import logging


class LogHelper:

    def __init__(self, name, level, log_to_file):
        """
        Create and configure logger
        Create console handler and logfile handlers
        :param_name name: logger name and logfile name if also log to file
        :param_name level: change to logging.DEBUG for verbose output, change to logging.INFO for standard output
        :param_name log_to_file: boolean
        :return: created and configured logger object
        """
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(level)

        console = logging.StreamHandler()
        console.setLevel(level)
        formatter = logging.Formatter('[%(asctime)s - %(levelname)s] %(message)s')
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        if log_to_file:
            logfile = logging.FileHandler('{0}.log'.format(self.name), mode='w')
            logfile.setLevel(logging.DEBUG)
            logfile.setFormatter(formatter)
            self.logger.addHandler(logfile)

    def info(self, message, *args):
        """
        """
        self.logger.info(message)

    def warning(self, message, *args):
        """
        """
        self.logger.warning(message)

    def error(self, message, *args):
        """
        """
        self.logger.error(message)

    def fatal(self, message, *args):
        """
        """
        self.logger.fatal(message)

    def debug(self, message, *args):
        """
        """
        self.logger.debug(message)


logger = LogHelper("ip_check", logging.DEBUG, True)
