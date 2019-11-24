import logging


def get_logger(name):
    """create new logger with application standards"""
    
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # formatter
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(message)s')

    # main handler
    file_handler = logging.FileHandler('main.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # debugging handler
    debug_handler = logging.FileHandler('debug.log')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(debug_handler)

    return logger
