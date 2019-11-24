import logging
from logging.handlers import TimedRotatingFileHandler
import os


class Logger:

    @staticmethod
    def get_logger(name):
        """create new logger with application standards"""
        
        Logger.__create_logs_directory()
        logger = Logger.__create_logger(name)

        app_handler = Logger.__create_time_handler('logs/app.log', logging.INFO)
        debug_handler = Logger.__create_stream_handler(logging.DEBUG)

        logger.addHandler(app_handler)
        logger.addHandler(debug_handler)

        return logger
    
    @staticmethod
    def __create_logs_directory():
        try:
            os.mkdir('logs')
        except OSError:  # directory already exists
            pass

    @staticmethod
    def __create_logger(name):
        """create new logger instance"""

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        return logger
    
    @staticmethod
    def __create_formatter():
        """return logger formatter"""
        
        format_str = '%(asctime)s : %(levelname)s : %(filename)s : %(message)s'
        return logging.Formatter(format_str)
    
    @staticmethod
    def __create_time_handler(filename, level):
        """create file logging handler"""

        handler = TimedRotatingFileHandler(filename=filename, when='M', interval=1)
        handler.setLevel(level)
        handler.setFormatter(Logger.__create_formatter())
        handler.suffix = '%Y-%m-%d'

        return handler
    
    @staticmethod
    def __create_stream_handler(level):
        """create stream logging handler"""

        main_handler = logging.StreamHandler()
        main_handler.setLevel(level)
        main_handler.setFormatter(Logger.__create_formatter())

        return main_handler
